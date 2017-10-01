
import os
import json
import facebook
import requests

token = "EAAP21xkIcuwBAC8rnZB8DIltkyoifUJKRnJiJV0gCK7vPsdGZCrSkMk7gUwTckQLbxuLkKZB1qQE2sukamQo58wZCPV0a11SnCySAgZA0tgcKOaYSli6xBZAZCGHfOuVJybVGCAgXTgYVGwT9VQ9WPoKdpVsHFnVVBNQtA0kDN9Ran8Ozgjce787xPmx7ZCP2P1PcCoZAuWj64QZDZD"
graph = facebook.GraphAPI(token)
all_fields={
    'message',
    'created_time',
    'description',
    'caption',
    'link',
    'place',
    'status_type'
}
all_fields=','.join(all_fields)
posts = graph.get_connections('me','posts',fields=all_fields)

while True:
    try:
        with open('my_posts2.jsonl','a') as f:
            for post in posts['data']:
                f.write(json.dumps(post)+"\n")

            posts=requests.get(posts['paging']['next']).json()
    except KeyError:
        break

