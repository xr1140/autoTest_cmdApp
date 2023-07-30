from blog import Blog
from post import Post

MENU_PROMPT = ('Enter "c" to create a blog, '
               '"l" to list blogs, '
               '"r" to read blogs, '
               '"p" to create a post, '
               'or "q" to quit: ')

POST_TEMPLATE = '''
--- {} ---
 
{}

'''

blogs = dict()  # blog_name : Blog object


def menu():
    # show the use the available blogs
    # let the use make a choice
    # do something with that choice
    # eventualy exit

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':

        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    # print available blogs
    print("Blogs!")
    for key, blog in blogs.items():  # [(blog_name, Blog), (blog_name, Blog)]
        print(f'- {blog}')


def print_posts(blog):
    for post in blog.posts:
        print_post(post)


def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))


def ask_create_blog():
    title = input("Enter your blog title: ")
    author = input("Enter your name: ")

    b = Blog(title, author)
    blogs[title] = b
    # sau
    # blogs[title] = Blog(title, author)


def ask_read_blog():
    title = input("Enter the blog title: ")

    print_posts(blogs[title])


def ask_create_post():
    blog_name = input("Enter the blog title you want to post in: ")
    title = input("Enter the title of the post: ")
    content = input("Enter the content of the post: ")

    blogs[blog_name].create_post(title, content)
