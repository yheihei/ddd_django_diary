from django.test import TestCase
from domain.models.post.post_id import PostId


class TestPostId(TestCase):
    def test_1(self):
        with self.assertRaises(ValueError):
            PostId('int以外')

    def test_2(self):
        self.assertEqual(True, PostId(1) == PostId(1))
