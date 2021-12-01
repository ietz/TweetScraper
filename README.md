# Introduction #
`TweetScraper` can get tweets from [Twitter Search](https://twitter.com/explore). 
It is built on [Scrapy](http://scrapy.org/) without using [Twitter's APIs](https://dev.twitter.com/rest/public).
The crawled data is not as *clean* as the one obtained by the APIs, but the benefits are you can get rid of the API's rate limits and restrictions. Ideally, you can get all the data from Twitter Search.

**WARNING:** please be polite and follow the [crawler's politeness policy](https://en.wikipedia.org/wiki/Web_crawler#Politeness_policy).

# Usage #
The recommended way to use the scraper is via the official [ietz/tweet-scraper](https://hub.docker.com/r/ietz/tweet-scraper) docker image.
By using a docker image, you don't have to install the required dependencies such as Firefox or the selenium drivers.
Call the image with
```shell
docker run -it --rm \
  -v <OUTPUT_DIR>:/root/TweetScraper/Data \
  scrapy crawl TweetScraper -s USER_AGENT="Your Name <yourmail@example.com>" -a query="@BarackObama"
```
The query will be used as input for the twitter search, and can use any [twitter advanced search field](https://twitter.com/search-advanced).
The scraper will create a `tweets.jsonl` and a `users.jsonl` in the `<OUTPUT_DIR>`.
Both files are in [jsonlines](https://jsonlines.org/) format, containing one JSON object per line.

# Acknowledgement #
Keeping the crawler up to date requires continuous efforts, please support our work via [opencollective.com/tweetscraper](https://opencollective.com/tweetscraper).


# License #
TweetScraper is released under the [GNU GENERAL PUBLIC LICENSE, Version 2](https://github.com/jonbakerfish/TweetScraper/blob/master/LICENSE)
