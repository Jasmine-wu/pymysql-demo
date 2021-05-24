
from app2.page.app import App


class TestMain():

    def test_go_to_market(self):
        App().start().main().goto_market()