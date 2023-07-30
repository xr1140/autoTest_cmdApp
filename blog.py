from post import Post


class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        p_count = len(self.posts)
        end_s = 's' if p_count != 1 else ''

        return f'{self.title} by {self.author} ({p_count} post{end_s})'

    def create_post(self, title, content):
        p = Post(title, content)
        self.posts.append(p)
        pass

    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': [post.json() for post in self.posts]
        }