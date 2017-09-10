
import os
import json
import facebook
import requests

token = "AAP21xkIcuwBABrE4gfuEahZAqDyQwhraDwBpyrZCBZB9maSSQbncJhPYzSQwCmFO0J5AmXPNglT20RbasN2UUhSKuGQssEULZCHef9qj6LoSLCdGHBQZAWFcgYAMoYA8Ybiw6U6qgzsaTTZC0a3wyFnfsIlVUL3QxUW8h3lFOxwgzeGwXTNqxP7eHTZA2973ZA6VQv3wS3ZBuwZDZD"
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

