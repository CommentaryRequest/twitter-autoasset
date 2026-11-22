from danbooru_netclient import NetworkClient

def create(config, tweet_url):
    client = NetworkClient("https://danbooru.donmai.us", config["danbooru_login"], config["danbooru_apikey"], config["danbooru_useragent"], 0)
    client.post("uploads.json", {"source": tweet_url})
