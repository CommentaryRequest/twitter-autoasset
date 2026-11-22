#!/usr/bin/env python3
import asyncio
import datetime
import time
import upload
from twscrape import API
from loguru import logger
from config import parse_config
from state import get_state, save_state
from tweetlog import get_tweetlog, save_tweetlog, add_to_tweetlog

__version__ = "1.0"

def hrdatetime():
    return datetime.datetime.now().strftime("%Y-%b-%d %H:%M:%S")

def get_timestamp(tweet_id):
    return tweet_id >> 22

def is_newer(id_a, id_b):
    return get_timestamp(id_a) > get_timestamp(id_b)

async def main():
    config = parse_config()
    list_id = config["list_id"]

    if not config["enable_twscrape_logging"]:
        logger.disable("twscrape")

    api = API("accounts.db")
    await api.pool.add_account_cookies(config["account"], f"auth_token={config['auth_token']}; ct0={config['ct0']}")

    state = get_state()
    tweetlog = get_tweetlog()

    print(f"twitter-autoasset {__version__} is up")

    while True:
        async for tweet in api.search(f"list:{list_id} filter:media since_id:{state.last_id}", limit=20):
            if is_newer(tweet.id, state.last_id):
                state.last_id = tweet.id

            user = tweet.user
            media_count = len(tweet.media.photos) + len(tweet.media.videos) + len(tweet.media.animated)

            print(
                f"[{hrdatetime()}] \033[0;32mFound new tweet:\033[0m\n"
                f"twitter #{tweet.id} \033[0;33m({media_count} media)\033[0m\n"
                f"Caption: \033[0;36m{tweet.rawContent}\033[0m\n"
                f"Artist: \033[0;36m{user.displayname}\033[0m (@{user.username})\n"
            )

            add_to_tweetlog(tweetlog, tweet)

            print(f"Uploading {tweet.url}...")
            upload.create(config, tweet.url)

        save_state(state)
        save_tweetlog(tweetlog)
        time.sleep(config["check_interval"])

if __name__ == "__main__":
    asyncio.run(main())
