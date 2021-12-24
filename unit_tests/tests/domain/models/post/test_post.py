from django.test import TestCase
from domain.models.post.post import Post
from domain.models.post.post_id import PostId
from domain.models.post.post_title import PostTitle
from domain.models.post.post_body import PostBody


class TestPost(TestCase):
    def test_1(self):
        '''IDで等価性を担保できること'''
        post_1 = Post(
            PostId(1),
            PostTitle('title1'),
            PostBody('body1'),
        )
        post_2 = Post(
            PostId(1),
            PostTitle('title2'),
            PostBody('body2'),
        )
        self.assertEqual(True, post_1 == post_2)

    def test_2(self):
        '''タイトルを変更できること'''
        post_1 = Post(
            PostId(1),
            PostTitle('title1'),
            PostBody('body1'),
        )

        post_1.change_title('title1 modified')
        self.assertEqual(
            True,
            post_1.title == PostTitle('title1 modified')
        )

    def test_3(self):
        '''本文を変更できること'''
        post_1 = Post(
            PostId(1),
            PostTitle('title1'),
            PostBody('body1'),
        )

        post_1.change_body('body1 modified')
        self.assertEqual(
            True,
            post_1.body == PostBody('body1 modified')
        )

