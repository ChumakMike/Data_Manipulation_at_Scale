import json
import sys
import re
import collections

def main():
    tweet_file = open(sys.argv[1])
    terms = collections.defaultdict(int)

    for line in tweet_file.readlines():
        tweet = json.loads(line)
        if "text" in tweet:
            tweet['text'].encode('ascii', 'replace')
            text = tweet["text"]
            text = text.rstrip("\n")
            text = " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", text).split())

            words_split = re.split(r"[\s.,?:\n]+", text)
            for word in words_split:
                terms[word] += 1

    for term in terms:
        print (term + " " + str(round(terms[term] / float(len(terms)), 4)))


if __name__ == '__main__':
    main()