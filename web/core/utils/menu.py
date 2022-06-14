from django.http import HttpRequest


class MenuItem:

    def __init__(self, title, url=None, perm=None):
        self.title = title
        self.url = url
        self.perm = perm
        self.children = None

    def has_access(self, user):
        if not callable(self.perm):
            return True
        return self.perm(user)

    def with_children(self, children):
        self.children = children
        return self

    def is_active(self, request: HttpRequest):
        if self.url == '/':
            return self.url == request.path
        if not self.as_item:
            return False
        return request.path.startswith(self.url)

    def get_children(self, request):
        if self.has_children:
            return filter(lambda item: item.has_access(request.user), self.children)
        return []

    @property
    def as_title(self):
        if not self.url:
            return self.title

    @property
    def as_item(self):
        if self.url:
            return self

    @property
    def has_children(self):
        try:
            return len(self.children) > 0
        except TypeError:
            return False

    def __str__(self):
        if self.as_title:
            return self.as_title
        return f"[{self.title}]({self.url})"

    def __repr__(self):
        return f"<{self.__class__.__name__} {self}>"
