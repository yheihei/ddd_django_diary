from django.test import TestCase
from domain.models.post.post_body import PostBody


class TestPostBody(TestCase):
    def test_1(self):
        post_body = PostBody('body')
        self.assertEqual(True, post_body == PostBody('body'))

    def test_2(self):
        with self.assertRaises(ValueError):
            PostBody(['str以外'])
