# lol_reddit_recap
A twitter bot that tweets the top posts from r/leagueoflegends and r/leagueofmemes daily.
https://twitter.com/lolredditrecap

# Prerequisites:
- a twitter account + twitter developer account
- a .env file at the root of your project that contains:
    - twitter access token, 
    - twitter access secret, 
    - twitter api key,
    - twitter api secret, 
    - reddit client id, 
    - reddit client secret
    - reddit user agent
Your env file should look like the following:
```
TWITTER_ACCESS_SECRET=""
TWITTER_ACCESS_TOKEN=""
TWITTER_API_KEY=""
TWITTER_API_SECRET=""
CLIENT_ID=""
CLIENT_SECRET=""
USER_AGENT=""
```

#Running the bot
Run twitterbot.py after you have created the .env file.

#Built with:
- [Tweepy](https://docs.tweepy.org/en/stable/)
- [Praw](https://praw.readthedocs.io/en/stable/)
