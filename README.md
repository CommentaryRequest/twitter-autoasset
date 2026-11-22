# Twitter Autoasset

Automatically upload tweets from a list into Danbooru's media assets.

## Installation

This program requires twscrape: `pip install twscrape`

## Configuration

Create a new `settings.json` file for configuration, example at `settings.json.example`.

* `list_id`: ID of the Twitter list you wish to monitor
* `account`: Your Twitter username
* `auth_token`: Twitter `auth_token` cookie
* `ct0`: Twitter `ct0` cookie
* `check_interval`: Interval between checks in seconds
* `enable_twscrape_logging1`: Enable twscrape logging, for debugging
* `danbooru_login`: Your Danbooru username
* `danbooru_apikey`: Your Danbooru API key

Danbooru API key requires `uploads:` permissions.
