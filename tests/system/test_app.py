from unittest import TestCase
from unittest.mock import patch
import app
from blog import Blog
from post import Post


class AppTest(TestCase):
    def setUp(self):
        b = Blog('Blog Title', 'Author')  # creaza un blog
        app.blogs = {'Blog Title': b}  # il adauga in dictionarul de bloguri al app


    def test_print_blogs(self):
        # functie print_blogs printeaza in consola trebuie capturat si analizat textul de acolo
        # cu ajutorul unittest.mock.patch care o sa "inlocuisca" the print function cu "mocked_print" basically
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
            mocked_print.assert_called_with('- Blog Title by Author (0 posts)')
            # mocked_print.assert_called_with('- Blog Title by Author (1 post)')


    def test_menu_calls_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value='q'):
                app.menu()
                mocked_print_blogs.assert_called()





    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value='q') as mocked_input:
            # mocked_input.side_effect = ('q')
            app.menu()
            mocked_input.assert_called_with(app.MENU_PROMPT)

    # def test_menu_calls_ask_create_blog1(self):
    #     with patch('app.ask_create_blog') as mocked_ask_create_blog:
    #         with patch('builtins.input') as mocked_input:
    #             mocked_input.side_effect = ('c', 'q')
    #             app.menu()
    #             mocked_ask_create_blog.assert_called()

    def test_menu_calls_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('c', 'BlogName', 'BlogAuthor', 'q')
            app.menu()
            self.assertIsNotNone(app.blogs['BlogName'])

    # aici verifica doar daca a fost chemata
    def test_menu_call_print_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input') as mocked_input:
                mocked_input.side_effect = ('l', 'q')
                app.menu()
                mocked_print_blogs.assert_called()

    # aici verifica daca functia a fost chemata si totul a functinat in interior
    def test_menu_call_ask_create_post(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('BlogName', 'BlogAuthor', 'p', 'BlogName', 'PostTitle', 'PostContent', 'q')
            app.ask_create_blog()
            app.menu()

            self.assertEqual(app.blogs['BlogName'].posts[0].title, 'PostTitle')





    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Blog title', 'Author')
            app.ask_create_blog()

            self.assertIsNotNone(app.blogs.get('Blog title'))


    def test_ask_read_blog(self):
        b = app.blogs['Blog Title']

        #  simulez ca user vrea sa citeasca blogul cu titlu 'Blog Title'
        with patch('builtins.input', return_value='Blog Title'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog()
                mocked_print_posts.assert_called_with(b)


    def test_print_posts(self):
        b = app.blogs['Blog Title']
        b.create_post('Post', 'Content')

        with patch('app.print_post') as mocked_print_post:
            app.print_posts(b)
            mocked_print_post.assert_called_with(b.posts[0])


    def test_print_post(self):
        # creaza un post
        p = Post("Titlu", "Continut")
        expected_print = '''
--- Titlu ---
 
Continut

'''
        with patch('builtins.print') as mocked_print:
            app.print_post(p)

            mocked_print.assert_called_with(expected_print)


    def test_ask_create_post(self):
        b = app.blogs['Blog Title']
        #  simulez ca userul vrea sa creeze un post in blogul numit 'Blog Title'
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Blog Title', 'POst Title', 'POst Content')
            app.ask_create_post()

            self.assertEqual(b.posts[0].title, 'POst Title')
            self.assertEqual(b.posts[0].content, 'POst Content')
