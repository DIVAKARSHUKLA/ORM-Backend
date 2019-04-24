from main.models import UserAnalysis
from main.utility import twarccus
import traceback


def twitterUpdateTweetText():
    try:
        tc = twarccus.TwarcCustom()
        user_data = [
            'narendramodi', 'amitshah',
            'arvindkejriwal', 'rahulgandhi', 'mayawati', 'MamataOfficial']
        for user in user_data:
            tweet_text = tc.getTweetText(screen_name=user, pages=10)
            tweet_text_senti = tc.getSentimentAnalysis(tweet_text)
            user_basic = tc.getBasicInfo(screen_name=user)
            name = user_basic['name']
            follow_count = user_basic['follow_count']
            status_count = user_basic['status_count']
            profile_url = user_basic['profile_url']
            image_url = user_basic['image_url']
            retweet_count = user_basic['retweet_count']
            fav_count = user_basic['fav_count']
            positive = tweet_text_senti['pos']
            negative = tweet_text_senti['neg']
            neutral = tweet_text_senti['neu']
            desc = user_basic['desc']
            values_to_update = {
                'name': name, 'tweet_positive': positive, 'tweet_negative': negative, 'tweet_neutral': neutral, 'fav_count': fav_count, 'retweet_count': retweet_count, 'image_url': image_url, 'profile_url': profile_url, 'status_count': status_count, 'follow_count': follow_count, 'desc': desc}
            obj_store, created = UserAnalysis.objects.update_or_create(
                screen_name=user, defaults=values_to_update)

    except Exception:
        f = open('/home/siddhant/error.txt', 'a')
        traceback.print_exc(file=f)
        f.write('========================================================')
        f.close()


def twitterUpdateTweetReply():
    try:
        tc = twarccus.TwarcCustom()
        user_data = [
            'narendramodi', 'amitshah',
            'arvindkejriwal', 'rahulgandhi', 'mayawati', 'MamataOfficial']
        for user in user_data:
            tweet_text = tc.getTweetRepliesText(
                screen_name=user, count=5, pages=3)
            tweet_text_senti = tc.getSentimentAnalysis(tweet_text)
            positive = tweet_text_senti['pos']
            negative = tweet_text_senti['neg']
            neutral = tweet_text_senti['neu']
            values_to_update = {
                'reply_positive': positive, 'reply_negative': negative, 'reply_neutral': neutral}
            obj_store, created = UserAnalysis.objects.update_or_create(
                screen_name=user, defaults=values_to_update)

    except Exception:
        f = open('/home/siddhant/error.txt', 'a')
        traceback.print_exc(file=f)
        f.write('========================================================'+'\n')
        f.close()
