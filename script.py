import sys
import re
from collections import defaultdict
import json
import datetime


def open_file(file_name):
    """
    opening and closing the file while reading and returning the lines.
    This is more for testing, when you have a text file with tweets.
    """
    with open(file_name, "r", encoding='UTF-8') as file:
        return file.readlines()


def privacy_tweet(tweet):
    """
    The function will check if the tweet contains privacy related terms.

    :param tweet: the plain text of the tweet, but with the spaced
    removed, so "in" works on terms that consist of multiple words as
    well.
    :returns: a boolean value whether the tweet is privacy related or
    not.
    """
    privacy_words = ["privacy", "privéleven", "privégegevens",
                     "persoonlijkelevenssfeer", "veiliginternet",
                     "encryptie", "persoonlijkevrijheid", "privésfeer",
                     "privacyvangebruikers", "onlineveiligheid",
                     "gepersonaliseerdeadvertenties", "persoonsgegevens"]
    # Some words are stuck together like "gepersonaliseerdeadvertenties"
    # which would be "gepersonaliseerde advertenties". This is done
    # because of `in` that can be used in conditions and can now be used
    # more easily.
    for word in privacy_words:
        if word in tweet:
            return True
            # if one of the above words is found in the tweet the
            # function will return True and stops searching
    return False


def get_date_tweet(tweet):
    """
    The tweet has text and a date in the same string, that get seperated
    with this function.

    :param tweet: this string contains the text of the tweet and the
    date the tweet was written.
    :returns: the tweet text and the date are seperated.
    """
    pattern_tweet_date = re.compile("[0-9][0-9][0-9][0-9]-[0-9][0-9]"
                                    "-[0-9][0-9] [0-9][0-9]:[0-9][0-9]:"
                                    "[0-9][0-9] [A-Z][A-Z][A-Z] "
                                    "[A-Z][a-z][a-z]")
    # the structure of the date with the time
    match_tweet_date = pattern_tweet_date.search(tweet)
    if match_tweet_date:
        tweet_date = match_tweet_date.group()
        pattern_date = re.compile("[0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]")
        # the structure of the date. Since I will only use the date, the
        # time should be removed
        match_date = pattern_date.search(tweet_date)
        date = match_date.group()
    else:
        date = "no date"
    return pattern_tweet_date.sub("", tweet), date


def count_tweets(tweets):
    """
    With a for loop every tweets is processed with the functions created
    above

    :param tweets: all tweets that will be processed by the script.
    :returns: a dictionary that for every date has another dictionary as
    value. This second dictionary contains information about the number
    of privacy and non privacy related tweets.
    """

    def privacy_count_dict():
        return {"privacy_related": 0, "other": 0}
    data = defaultdict(privacy_count_dict)

    for tweet in tweets:
        tweet_and_date = get_date_tweet(tweet)
        privacy_related = privacy_tweet(tweet_and_date[0].replace(" ", ""))
        # the replace is needed so "in" in the function privacy_tweets
        # will work on terms containing more than two words as well
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
    # If the file name is given, do the first. If the file is already
    # opened by linux commands, do the second

    name_file = "output_privacy_data_{0}.json".format(datetime.datetime.now())
    # So every file name is unique the date and time are added
    name_file = name_file.replace(" ", "_")

    print("The file name is '{0}'.".format(name_file))

    with open(name_file, "w") as output:
        output.write(json_data)


if __name__ == "__main__":
    main(sys.argv)
