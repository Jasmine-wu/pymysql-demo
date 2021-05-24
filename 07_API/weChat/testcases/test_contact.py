from app.WeChat.weChat.page.app import App


class TestContact:
    def setup(self):
        self.app = App()
        self.main = self.app.start().goto_main()

    def teardown(self):
        pass

    def test_contact(self):
        invite_page = self.main.goto_addresslist().add_menber() \
            .addmenber_by_manul() \
            .input_username() \
            .set_gender() \
            .input_phonenumber() \
            .click_save()
        assert "Toast" in invite_page.get_toast()