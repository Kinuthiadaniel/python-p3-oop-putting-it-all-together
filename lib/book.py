#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, pages):
        if isinstance(pages, int):
            self._page_count = pages
        else:
            print("page_count must be an integer")
    
    # @turn_page.setter
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")