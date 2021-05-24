from app.testcases.utils import *
from app.page.app import App
import pytest


class TestSearch():
    def setup(self):
        self.search = App().start().main().goto_market().goto_search()

    @pytest.mark.parametrize("company, code, expect", load_data("search.yaml", "search"))
    def test_search(self, company, code, expect):
        self.search.search(company, code)

        # assert_that(self.search.get_toast_text(), equal_to("添加成功"))
