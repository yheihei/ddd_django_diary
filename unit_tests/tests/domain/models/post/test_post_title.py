from django.test import TestCase
from domain.models.post.post_title import PostTitle


class TestPostTitle(TestCase):
    def test_1(self):
        with self.assertRaises(ValueError):
            PostTitle('')

    def test_2(self):
        with self.assertRaises(ValueError):
            PostTitle('a'*4097)

    def test_3(self):
        with self.assertRaises(ValueError):
            PostTitle(['str以外'])

    def test_4(self):
        post_title = PostTitle('a' * 4096)
        self.assertEqual(True, post_title == PostTitle('a' * 4096))
