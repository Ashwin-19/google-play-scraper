from google_play_scraper import Sort, reviews

all_results = []
old_results = []
review_ids = []

continuation_token = None

result, continuation_token = reviews(
    'com.nianticlabs.pokemongo',
    lang='en', # defaults to 'en'
    country='us', # defaults to 'us'
    sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
    count=100, # defaults to 100
    # filter_score_with=5 # defaults to None(means all score)
)

for i in all_results: old_results.append(i)
for i in result: all_results.append(i)
# print(len(all_results))
# print(len(old_results))

print(continuation_token)

while len(old_results) < len(all_results):

    result, continuation_token = reviews(
    'com.fantome.penguinisle',
    continuation_token=continuation_token # defaults to None(load from the beginning)
    )

    print(continuation_token)

    for i in all_results: old_results.append(i)
    for i in result: all_results.append(i)
    for i in result: review_ids.append(i["reviewId"])

    print(len(all_results))
    print(len(old_results))


print("review ids " + str(len(set(review_ids))))
# print(review_ids)







