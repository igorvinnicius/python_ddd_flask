class Post(object):
    def __init__(self, id=None, title=None, author=None, text=None,
            post_date=None, posts=None):
        self.id = id
        self.title = title
        self.author = author
        self.text = text
        self.post_date = post_date