from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient


User = get_user_model()

from .models import Tweet, TweetLike
# Create your tests here.

class TweetTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='abc', password='1234')
        tweet_obj = Tweet.objects.create(content='wassup',  user = self.user)
        tweet_obj = Tweet.objects.create(content='hey',  user = self.user)
        tweet_obj = Tweet.objects.create(content='heid',  user = self.user)


    def test_tweet_created(self):
        tweet_obj = Tweet.objects.create(content='wassup',  user = self.user)
        self.assertEqual(len(Tweet.objects.all()), 4)
        

    def get_client(self):
        client = APIClient()
        client.login(username=self.user.username, password='1234')
        return client

    def test_tweet_list(self):
        client = self.get_client()
        response = client.get('/api/tweet/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)

    def test_action_like(self):
        client = self.get_client()
        response = client.post('/api/tweet/action/', {'id': 1, 'action': 'like'})
        print(response.json())
        self.assertEqual(response.status_code, 200)
        