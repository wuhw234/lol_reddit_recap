import os
from os.path import exists
import urllib.request

def isImage(post):
    if not post.is_self and post.is_reddit_media_domain and post.domain == "i.redd.it":
        return True
def downloadImage(post):
    if post.url.endswith(".png"):
        filetype = ".png"
    elif post.url.endswith(".jpg"):
        filetype = ".jpg"
    elif post.url.endswith(".gif"):
        filetype = ".gif"
    else:
        print("unsupported image type")
        return False

    filepath = os.path.join("lol_reddit", post.id + filetype)
    urllib.request.urlretrieve(post.url, filepath)
    
    mb_size = os.path.getsize(filepath) / 1000000
    if filetype == ".gif" and mb_size >= 15:
        print("gif size too large")
        os.remove(filepath)
        return False
    elif filetype != ".gif" and mb_size >= 5:
        print("jpg/png size too large")
        os.remove(filepath)
        return False
    return filepath
def tweetImage():
    pass


def isText(post):
    return post.is_self and len(post.title) < 250
def condenseText(post):
    title = post.title
    max_length = 280 - 30 - len(title)
    text = post.selftext[:max_length] + "..."
    
    url = getUrl(post)
    return title + "\n" + url + "\n" + text
def tweetText():
    pass

def getUrl(post):
    url = "https://redd.it/" + post.id
    return url

def getFileSize():
    path = "lol_reddit/recent_tweets.txt"
    if not exists(path):
        return 0
    with open(path, "r") as file:
        lines = file.readlines()
    return len(lines)

def replaceFile():
    path = "lol_reddit/recent_tweets.txt"
    with open(path, "r") as old:
        prev_lines = old.readlines()
    new_lines = prev_lines[-10:]
    os.remove(path)

    with open(path, "w") as new:
        for line in new_lines:
            new.write(line)

def writeToFile(id):
    path = "lol_reddit/recent_tweets.txt"
    with open(path, "a") as file:
        file.write(id)
        file.write("\n")
def checkDuplicate(id):
    path = "lol_reddit/recent_tweets.txt"
    if not exists(path):
        return False
    with open(path) as file:
        if id in file.read():
            return True
        return False


# def isVideo(post):
#     if not post.is_self and post.is_video and post.is_reddit_media_domain and post.domain == "v.redd.it":
#         url = "https://www.reddit.com/" + post.permalink + ".json"
#         response = requests.get(url, headers={"User-agent": os.environ["USER_AGENT"]})
#         json = response.json()
#         video_length = json[0]["data"]["children"][0]["data"]["secure_media"]["reddit_video"]["duration"]
#         print(video_length)
        
#         if video_length <= 40:    #might modify later to download video here
#             return True
#     else:
#         return False
# def downloadVideo(post):
#     filepath = os.path.join("lol_reddit", post.id + ".mp4")
#     url = post.media["reddit_video"]["fallback_url"]
#     print(url)
#     urllib.request.urlretrieve(url, filepath)
#     return filepath
# def tweetVideo():
#     pass
