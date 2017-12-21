from textblob import TextBlob
import pylab as pl
import csv
import re
import time

tweets = []

trump_positive = 0
trump_negative = 0
trump_objective = 0
trump_subjective = 0


def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


with open("trump.csv", 'rt', encoding='utf8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    next(reader)
    for row in reader:

        tweet= dict()
        tweet['orig'] = row[2]
        tweet['id'] = int(row[0])
        tweet['pubdate'] = time.strftime('%Y/%m/%d', time.strptime(row[1],'%Y-%m-%d %H:%M:%S'))

        if re.match(r'^RT.*', tweet['orig']):
            continue

        tweet['clean'] = tweet['orig']

        tweet['clean'] = strip_non_ascii(tweet['clean'])

        tweet['clean'] = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', tweet['clean'])

        tweet['clean'] = re.sub(r'\bthats\b', 'that is', tweet['clean'])
        tweet['clean'] = re.sub(r'\bive\b', 'i have', tweet['clean'])
        tweet['clean'] = re.sub(r'\bim\b', 'i am', tweet['clean'])
        tweet['clean'] = re.sub(r'\bya\b', 'yeah', tweet['clean'])
        tweet['clean'] = re.sub(r'\bcant\b', 'can not', tweet['clean'])
        tweet['clean'] = re.sub(r'\bwont\b', 'will not', tweet['clean'])
        tweet['clean'] = re.sub(r'\bid\b', 'i would', tweet['clean'])
        tweet['clean'] = re.sub(r'wtf', 'what the fuck', tweet['clean'])
        tweet['clean'] = re.sub(r'\bwth\b', 'what the hell', tweet['clean'])
        tweet['clean'] = re.sub(r'\br\b', 'are', tweet['clean'])
        tweet['clean'] = re.sub(r'\bu\b', 'you', tweet['clean'])
        tweet['clean'] = re.sub(r'\bk\b', 'OK', tweet['clean'])
        tweet['clean'] = re.sub(r'\bsux\b', 'sucks', tweet['clean'])
        tweet['clean'] = re.sub(r'\bno+\b', 'no', tweet['clean'])
        tweet['clean'] = re.sub(r'\bcoo+\b', 'cool', tweet['clean'])
        tweet['clean'] = re.sub(r'\\n', ' ', tweet['clean'])
        tweet['clean'] = re.sub(r'\\r', ' ', tweet['clean'])
        tweet['clean'] = re.sub(r'&gt;', '', tweet['clean'])
        tweet['clean'] = re.sub(r'&amp;', 'and', tweet['clean'])
        tweet['clean'] = re.sub(r'\$ *hit', 'shit', tweet['clean'])
        tweet['clean'] = re.sub(r' w\/', 'with', tweet['clean'])
        tweet['clean'] = re.sub(r'\ddelay', '\d delay', tweet['clean'])

        tweet['TextBlob'] = TextBlob(tweet['clean'])

        tweets.append(tweet)


for tweet in tweets:
    tweet['polarity'] = float(tweet['TextBlob'].sentiment.polarity)

    if tweet['polarity'] >= 0.1:
        tweet['sentiment'] = 'positive'
        trump_positive += 1
    elif tweet['polarity'] <= -0.1:
        tweet['sentiment'] = 'negative'
        trump_negative += 1

labels = 'Trump positive', 'Trump negative'
sizes = [trump_positive, trump_negative]
colors = ['gold', 'yellowgreen']
explode = (0.1, 0,)

fig = pl.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax1.set_title("True/Positive")

ax1.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

ax1.axis('equal')

for tweet in tweets:
    tweet['subjectivity'] = float(tweet['TextBlob'].sentiment.subjectivity)

    if tweet['subjectivity'] <= 0.5:
        tweet['sentiment'] = 'objective'
        trump_objective += 1
    elif tweet['subjectivity'] >= 0.6:
        tweet['sentiment'] = 'subjective'
        trump_subjective += 1

labels = 'Trump objective', 'Trump subjective'
sizes = [trump_objective, trump_subjective]
colors = ['gold', 'yellowgreen']
explode = (0.1, 0,)

ax2 = fig.add_subplot(1, 2, 2)
ax2.set_title("Objective/Subjectiv")
ax2.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
ax2.axis('equal')

pl.show()
