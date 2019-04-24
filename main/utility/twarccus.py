from twarc import Twarc
import json
import time
from simplesentiment.stence import sentanceanalyser


t = Twarc('EZ4MUdjIR22V8y6TDia6vRrEf', 'ARY5AgvJKvRWfb6nPeTugnvyKDY8VdQh0HdHpYLhcrUX2AvBdz',
          '1103185799841902592-g6OFAdGgV4vYkeg5KCK2gZwCmI3XzH', '6IW8bDnxeBZwLEDNa4GAEBWzvgDkAkh7bRRVrV4xcSfpc')


class TwarcCustom:
    """ getting list of top n tweets reply in a list
    by providing the screen_name and count prams
    e.g: if n=2 for some screen_name then for 2 tweets you will get
    all the replies of two tweets as list wise in plain text.
    """

    def getTweetRepliesList(self, screen_name=None, count=1, limit=100):
        tweet_reply = []
        timeline = t.timeline(screen_name=screen_name, count=count)
        for tw in timeline:
            tweet = t.tweet(tw['id_str'])
            tweet_text = ""
            for index, tweet in zip(range(limit), t.replies(tweet)):
                tweet_text += tweet['full_text'] + " "
            tweet_reply.append(tweet_text)
        return tweet_reply

    """ this will return tweets reply as single text of all tweets """

    def getTweetRepliesText(self, screen_name=None, count=1, pages=1):
        tweet_reply = ""
        timeline = t.timeline(screen_name=screen_name,
                              count=count)
        for tw in timeline:
            tweet = t.tweet(tw['id_str'])
            # open('tweet.json', 'w').write(self.getTweetInJson(tw['id_str']))
            tweet_text = ""
            # in t.replies max_pages set to 1 wich will give around 15 replies
            # for index, tweet in zip(range(limit), t.replies(tweet, max_pages=5)):
            for tweet in t.replies(tweet, max_pages=pages):
                tweet_text += tweet['full_text'] + " "
            tweet_reply += tweet_text
            #open('userTweets/{}.json'.format(screen_name), 'w').write(tweet_reply)
        return tweet_reply
        # tweet = t.timeline(screen_name=screen_name,
        #                    count=count, max_pages=pages)
        # tweet_reply = ""
        # for x in tweet:
        #     rep = t.search('to:{}'.format(
        #         x['user']['screen_name']), since_id=x['id_str'], max_pages=pages)
        #     for y in rep:
        #         if y['in_reply_to_status_id_str'] == x['id_str']:
        #             # json_data = json.dumps(x)
        #             tweet_reply += y['full_text']+'\n'
        # return tweet_reply
    """ this will return tweets text as text by providing
    screen_name and pages. One page will return 200 tweets text"""

    def getTweetText(self, screen_name=None, pages=1):
        timeline = t.timeline(screen_name=screen_name, max_pages=pages)
        tweet_text = ""
        for tw in timeline:
            tweet_text += tw['full_text'] + " "
        # open('userTweetsText/{}.json'.format(screen_name), 'w').write(tweet_text)
        return tweet_text

    """
    getting tweets in json format
    """

    def getTweetInJson(self, screen_name=None, count=1):
        timeline = t.timeline(screen_name=screen_name,
                              count=count)
        # tweet = t.tweet(tweet_id)
        status = json.dumps(list(timeline))
        open('tweet.json', 'w').write(status)
        # return status

    """ Sentiment analysis """

    def getSentimentAnalysis(self, text=""):
        p = sentanceanalyser()
        try:
            a, b, c = p.sentance_sentiment(text)
        except:
            print(text)
            c = [{'Total_Positive': 33.33,
                  'Total_Negative': 33.33, 'Total_Neutral': 33.33}]
        t_pos = c[0]['Total_Positive']
        t_neg = c[0]['Total_Negative']
        t_neu = c[0]['Total_Neutral']
        t_sum = t_pos + t_neg + t_neu
        positive = round(t_pos/t_sum*100, 2)
        negative = round(t_neg/t_sum*100, 2)
        neutral = round(t_neu/t_sum*100, 2)
        data = {'pos': positive, 'neg': negative, 'neu': neutral}
        return data

    # """ This is fetch user name with screen_name  """

    # def getScreenName(self, screen_name=None, count=1):
    #     tweet = t.timeline(screen_name=screen_name, count=count)
    #     for x in tweet:
    #         name = x['user']['name']
    #     return name

    # """ This will fetch user image url """

    # def getProfileImage(self, screen_name=None):
    #     if '@' in screen_name:
    #         screen_name = screen_name.lstrip('@')
    #     user = t.user_lookup(ids=[screen_name], id_type="screen_name")
    #     url = list(user)[0]["profile_image_url"]
    #     image_user_url = url.replace('_normal', '')
    #     return image_user_url

    def getUserDataInJson(self, screen_name=None):
        if '@' in screen_name:
            screen_name = screen_name.lstrip('@')
        user = t.user_lookup(ids=[screen_name], id_type="screen_name")
        f = open('userProfile/{}.json'.format(screen_name), 'w')
        f.write(json.dumps(list(user)))
        f.close()

    def getBasicInfo(self, screen_name=None):
        if '@' in screen_name:
            screen_name = screen_name.lstrip('@')
        user = t.user_lookup(ids=[screen_name], id_type="screen_name")
        # f = open('userProfile/{}.json'.format(screen_name), 'w')
        # f.write(json.dumps(list(user)))
        # f.close()
        # f = open('userProfile/{}.json'.format(screen_name), 'r')
        # data_str = ""
        # for x in f:
        #     data_str = data_str+x
        user = list(user)
        follow_count = user[0]['followers_count']
        status_count = user[0]['statuses_count']
        desc = user[0]['description']
        name = user[0]['name']
        profile_url = user[0]['url']
        image_url = user[0]['profile_image_url']
        retweet_count = user[0]['status']['retweet_count']
        fav_count = user[0]['status']['favorite_count']
        image_url = image_url.replace('_normal', '')
        data_dict = {'follow_count': follow_count, 'status_count': status_count,
                     'desc': desc, 'name': name, 'profile_url': profile_url, 'image_url': image_url, 'retweet_count': retweet_count, 'fav_count': fav_count}
        return data_dict

    def arrangeData(self, screen_name_list):
        main_data = []
        for x in screen_name_list:
            basic = self.getBasicInfo(x)
            name = basic['name']
            follow_count = basic['follow_count']
            status_count = basic['status_count']
            desc = basic['desc']
            profile_url = basic['profile_url']
            image_url = basic['image_url']
            retweet_count = basic['retweet_count']
            fav_count = basic['fav_count']
            # f = open('senti.json', 'r')
            # data_str = ""
            # for y in f:
            #     data_str = data_str+y
            # json_data = json.loads(data_str)
            # tweet_reply_senti = json_data[0][x]['reply']
            # tweet_text_senti = json_data[0][x]['text']
            main_dict = {'name': name, 'follow_count': follow_count, 'status_count': status_count,
                         'desc': desc,  'profile_url': profile_url, 'image_url': image_url, 'retweet_count': retweet_count, 'fav_count': fav_count, 'screen_name': x}
            main_data.append(main_dict)
        return main_data

        """ Analysis Code """
    # def test():
    #     leader_list = [
    #         'narendramodi', 'amitshah',
    #         'arvindkejriwal', 'rahulgandhi', 'mayawati', 'MamataOfficial']
    #     for leader in leader_list:
    #         f = open('userTweetsText/{}.json'.format(leader), 'r')
    #         reply = ""
    #         for x in f:
    #             reply += x
    #         reply_senti_dict = self.getSentimentAnalysis(reply)
    #         f.close()
    #         g = open('senti.json', 'a')
    #         g.write(
    #             '"{}" tweet text analysis {}\n'.format(leader, reply_senti_dict))
    #         g.close()
