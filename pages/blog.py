from pages.base_page import Page


class Blog(Page):

    def verify_opened(self):
        self.verify_partial_url('www.aboutamazon.com')