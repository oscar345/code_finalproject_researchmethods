import sys
import re
from collections import defaultdict
import json
import datetime


def open_file(file_name):
    with open(file_name, "r", encoding='UTF-8') as file:
        return file.readlines()


def privacy_tweet(tweet):
    privacy_words = ["privacy", "privéleven", "privégegevens",
                     "persoonlijkelevenssfeer", "veiliginternet",
                     "encryptie", "privacyschending", "rechtopprivacy",
                     "privacyvangebruikers", "onlineprivacy",
                     "onlineveiligheid", "gepersonaliseerdeadvertenties",
                     "privacyissues", "privacyproblemen", "privacybewust",
                     "privacygevaar", "privacyvoorwaarden"]
    for word in privacy_words:
        if word in tweet:
            return True
    return False


def get_date_tweet(tweet):
    pattern_tweet_date = re.compile("[0-9][0-9][0-9][0-9]-[0-9][0-9]"
                                    "-[0-9][0-9] [0-9][0-9]:[0-9][0-9]:"
                                    "[0-9][0-9] [A-Z][A-Z][A-Z] "
                                    "[A-Z][a-z][a-z]")
    match_tweet_date = pattern_tweet_date.search(tweet)
    if match_tweet_date:
        tweet_date = match_tweet_date.group()
        pattern_date = re.compile("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]")
        match_date = pattern_date.search(tweet_date)
        date = match_date.group()
    else:
        date = "no date"
    return pattern_tweet_date.sub("", tweet), date


def count_tweets(tweets):
    def privacy_count_dict():
        return {"privacy_related": 0, "other": 0}
    data = defaultdict(privacy_count_dict)

    for tweet in tweets:
        tweet_and_date = get_date_tweet(tweet)
        privacy_related = privacy_tweet(tweet_and_date[0].replace(" ", ""))
        if privacy_related:
            data[tweet_and_date[1]]["privacy_related"] += 1
        else:
            data[tweet_and_date[1]]["other"] += 1
    return data


def main(argument):
    try:
        json_data = json.dumps(count_tweets(open_file(argument[1])))
    except IndexError:
        json_data = json.dumps(count_tweets(sys.stdin))

    name_file = f"output_privacy_data_{datetime.datetime.now()}.json"
    name_file = name_file.replace(" ", "_")

    print(f"The file name is '{name_file}'.")

    with open(name_file, "w") as output:
        output.write(json_data)


if __name__ == "__main__":
    main(sys.argv)
