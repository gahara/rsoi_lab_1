#!/usr/bin/env python3
import urllib
import base64
import requests
#import json

#use consumer_key and consumer_secret to access bearer token
#token = password
CONSUMER_KEY = 'ngxZKzzVvFaHJUkAsjoAuKt4O'
CONSUMER_SECRET = 'z1UJK9bVvsAZZVTvsi1qHbTHVogZJsMQL0pEQXqjDUMiw8JAp7'

#encode key and secret just because twitter says so
encodedConsumerKey = urllib.parse.quote(CONSUMER_KEY)
encodedConsumerSecret = urllib.parse.quote(CONSUMER_SECRET)
a = encodedConsumerKey+ ':' + encodedConsumerSecret
b = base64.b64encode(bytes(a, 'ASCII')).decode('ASCII')

#this is how we obtain bearer token
headers = {'Authorization': 'Basic ' + b, 'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}
r = requests.post('https://api.twitter.com/oauth2/token', headers = headers, data = 'grant_type=client_credentials')
#if the request was formatted correctly, the server will respond with a JSON-encoded payload

c = r.json() #decode json
#print(c)
#if we made a bad request (a 4XX client error or 5XX server error response), we can raise it 
r.raise_for_status()
#check the token's type
if c['token_type'] != 'bearer':
  raise Exception('smth is wrong: token_type is not bearer')	
#the value associated with access_token key is the bearer token
bearer = c['access_token']

#this is how we get user's timeline
h = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json', params = {'screen_name': 'twitterapi', 'count': 5}, headers = {'Authorization': 'Bearer '+ bearer})

res = h.json()
print(res)
h.raise_for_status()

#invalidating our bearer token
r = requests.post('https://api.twitter.com/oauth2/invalidate_token', headers = headers, data = 'access_token=' + bearer)
r.raise_for_status()
#ACCESS_TOKEN '2969725293-vxcKuVrm8TGg0mZKS2VbthoSBVihe1ZrnywzARy'
#ACCESS_TOKEN_SECRET =  'mEsg1qbikb4ZD7Iev3rx5AYGXDJhHirTttAj5DckDxsFH' 

