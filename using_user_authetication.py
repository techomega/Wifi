
import os
import json
import facebook
import requests

token = "EAAP21xkIcuwBALZBJYOW44tp2C0kou1Ma4WziuWYaDOpqbjujtUEaKFghUGjFYlsvWdOu9hPq9qz2niEJoKpwz8TDUIcnhxKvR06gMhBwKkxPHnBvBQR3i3gxbY6kVFDTMb24ZA1XdP8pPnfb11Wv4794Uin9tQymVeXnneGZCZAf33pUPEaxuZCgvpe35b9AQGuyaWBoRwZDZD"
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

