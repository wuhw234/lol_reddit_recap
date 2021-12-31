import praw
import utils
import os
import tweepy
from dotenv import load_dotenv
# import time

def main():
    load_dotenv()
    api = connectTwitter()
    reddit = getReddit()
    subreddits = ["leagueoflegends", "leagueofmemes"]
    # replace_tweets = False
    # while True:
    for sub in subreddits:
        curr_posts = 0
        for post in reddit.subreddit(sub).top("day", limit=50):
            if utils.checkDuplicate(str(post.id)):
                continue
            if utils.isText(post):
                tweet_body = utils.condenseText(post)
                try:
                    api.update_status(status=tweet_body)   #TODO add try catch?
                    curr_posts += 1
                    utils.writeToFile(str(post.id))
                except:
                    print("exception - duplicate post? possible that lockout is > 24")
            elif utils.isImage(post):
                filepath = utils.downloadImage(post)
                if filepath and len(post.title) < 250:
                    if filepath.endswith(".gif"):
                        media_object = api.media_upload(filename=filepath, chunked=True, \
                            media_category="tweet_gif")
                    else:
                        media_object = api.media_upload(filename=filepath)
                    tweet_body = post.title + "\n" + utils.getUrl(post)
                    try:
                        api.update_status(status=tweet_body, media_ids=[media_object.media_id_string])

                        os.remove(filepath)
                        curr_posts += 1
                        utils.writeToFile(str(post.id))
                    except:
                        print("duplicate post? check twitter lockout or image exception")
            else:
                print("link or video or title > 250 characters")

            if curr_posts == 5:
                break
        if utils.getFileSize() >= 20:
            utils.replaceFile()
        # if replace_tweets:
        #     utils.replaceFile()
        # replace_tweets = not replace_tweets
        # time.sleep(86400)




def getReddit():
    id = os.environ["CLIENT_ID"]
    print(id)
    secret = os.environ["CLIENT_SECRET"]
    print(secret)
    agent = os.environ["USER_AGENT"]    
    reddit = praw.Reddit(
        client_id = id,
        client_secret = secret,
        user_agent = agent,
    )

    return reddit

def connectTwitter():
    twitter_key = os.environ["TWITTER_API_KEY"]
    twitter_secret = os.environ["TWITTER_API_SECRET"]
    access_token = os.environ["TWITTER_ACCESS_TOKEN"]
    access_secret = os.environ["TWITTER_ACCESS_SECRET"]

    auth = tweepy.OAuthHandler(twitter_key, twitter_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    
    return api

if __name__ == "__main__":
    main()
        

