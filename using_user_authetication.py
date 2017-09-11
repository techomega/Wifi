
import os
import json
import facebook
import requests

token = "EAAP21xkIcuwBAOBhVZCycaFIA8P6W32u2dHmsilwZCsSDJIztGoOjYFDksjV7Wm47CqdtjpZB60pOqaZC3SYtCVtiGX79GFTZBGuDlJcVjZCfsC6ZBpoOmzUoSKY9536YZC0yuDlZBqv0MpEGhUKZBFVWVuA9yuuL5D5GrgA0OjAZCjlZAPFWNHdmplfVZAujLJGLcb0JZCtNLI4WeQwZDZD"
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

