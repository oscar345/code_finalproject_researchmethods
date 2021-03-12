

def privacy_tweet(tweet):
    privacy_words = ["privacy", "privéleven", "privégegevens",
                     "persoonlijke levenssfeer", "veilig internet",
                     "encryptie", "privacy schending", "recht op privacy",
                     "privacy van gebruikers", "online privacy",
                     "online veiligheid", "gepersonaliseerde advertenties",
                     "privacy issues", "privacy problemen", "privacy bewust",
                     "privacygevaar"]
    for word in privacy_words:
        if word in tweet:
            return True
    return False


def count_tweets(tweets):
    privacy_tweets = 0
    other_tweets = 0
    
    for tweet in tweets:
        privacy_related = privacy_tweet(tweet)
        if privacy_related:
            privacy_tweets += 1
        else:
            other_tweets += 1
    return privacy_tweets, other_tweets


def main(argument):
    print(count_tweets(argument[1]))


if __name__ == "__main__":
    main()