import requests
from operator import itemgetter

# execute api calls and store responses
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# processing information about each article
submission_ids = r.json()
submission_dicts = []
# for submission_id in submission_ids[:30]:
for submission_id in submission_ids[:30]:
    # for each article, execute an api call
    url = 'https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json'
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'title': response_dict['title'],
        'link': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'comments': response_dict.get('descendants', 0)
    }

    submission_dicts.append(submission_dict)

    print(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)
print(submission_dicts)

for submission_dict in submission_dicts:
    print("\nTitle:", submission_dict['title'])
    print("Discussion link:", submission_dict['link'])
    print("Comments:", submission_dict['comments'])
