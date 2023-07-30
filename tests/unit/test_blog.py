from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Title', 'Author')

        self.assertEqual('Title', b.title)
        self.assertEqual('Author', b.author)
        self.assertListEqual([], b.posts)
        # self.assertEqual(0, len(b.posts))

    def test_repr(self):
        b = Blog('Title', 'Author')
        b2 = Blog('Smecherie de Title', 'Alin')
        # print(b.__repr__())

        self.assertEqual(b.__repr__(), 'Title by Author (0 posts)')
        self.assertEqual(b2.__repr__(), 'Smecherie de Title by Alin (0 posts)')

    def test_repr_manyPosts(self):
        b = Blog('Title', 'Author')
        b.posts = ['werewr']

        b2 = Blog('Title', 'Author')
        b2.posts = ['werewr', 'sads']

        self.assertEqual(b.__repr__(), 'Title by Author (1 post)')
        self.assertEqual(b2.__repr__(), 'Title by Author (2 posts)')

