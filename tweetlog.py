import os
import json

def get_tweetlog():
    if not os.path.exists("tweetlog.json"):
        return []

    with open("tweetlog.json", "r") as tweetlog_json:
        return json.load(tweetlog_json)

def save_tweetlog(tweetlog):
    with open("tweetlog.json.tmp", "w", encoding="utf-8") as tweetlog_json:
        json.dump(tweetlog, tweetlog_json, indent=2, ensure_ascii=False)

    os.replace("tweetlog.json.tmp", "tweetlog.json")

def add_to_tweetlog(tweetlog, tweet):
    existing_ids = [tweet["id"] for tweet in tweetlog]
    if tweet.id in existing_ids:
        return

    tweetlog.append({
        "id": tweet.id,
        "caption": tweet.rawContent,
        "user": {
            "name": tweet.user.displayname,
            "handle": tweet.user.username
        }
    })
