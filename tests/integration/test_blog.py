from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog('Title', 'Author')
        b.create_post('titlu', 'continut')

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'titlu')
        self.assertEqual(b.posts[0].content, 'continut')

    def test_json_no_posts(self):
        b = Blog('Title', 'Author')
        expected = {'title': 'Title',
                    'author': 'Author',
                    'posts': [],
        }

        self.assertDictEqual(expected, b.json())

    def test_json(self):
        b = Blog('Title', 'Author')
        b.create_post('Titlu', 'Continut')

        expected = {'title': 'Title',
                    'author': 'Author',
                    'posts': [
                        {
                            'title': 'Titlu',
                            'content': 'Continut'
                        }
                    ],
        }

        self.assertDictEqual(expected, b.json())
