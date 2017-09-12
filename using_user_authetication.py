
import os
import json
import facebook
import requests

token = "EAAP21xkIcuwBAHYMQseZBZC2SabBajs6AZBqv6FYZAxKbZA7hn8C6HZBk9cHvFmvNzyz6LPETRgWIbqtIujPkOWtZBHHJywmgZBZAxTNHXcyBWNUx9435qSk4Bn9kAZBJPKEloWNacW4nvRKEr5YyjJYHzLn1klZBCW9ivnoFQwrN2zGwZDZD"
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

