import json
import sys
from collections import Counter


def main():
    hashtags = {}
    tweet_file = open(sys.argv[1])
    for line in tweet_file.readlines():
        tweet = json.loads(line)
        if "entities" in tweet:
            entities = tweet["entities"]
            hashtags_in_tweet = entities["hashtags"]

            for hashtag in hashtags_in_tweet:
                text = hashtag["text"]
                if text in hashtags.keys():
                    hashtags[text] += 1
                else:
                    hashtags[text] = 1

    sorted_col_of_hashtags = Counter(hashtags)
    top_ten = sorted_col_of_hashtags.most_common(10)
    for top in top_ten:
        print(top[0] + " " + str(top[1]))


if __name__ == '__main__':
    main()