from django.test import TestCase, Client

class TestSite(TestCase):
    #fixtures = ['test_data.json']
    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        resp = self.client.get("/")
        self.assertEquals(resp.status_code, 200)
        cont = {
            "flag": "{flag:DoYouWantToTestThis?}"
        }
        self.assertEquals(resp.context["flag"], "{flag:DoYouWantToTestThis?}")
        self.assertTemplateUsed("pages/index.html")

    def test_statistic_page(self):
        resp = self.client.post("/login/", {"username": "qwerty", "password": "qwerty"})
        self.assertEquals(resp.status_code, 200)
        resp = self.client.get("check/")
        #self.assertEquals(resp.context["statistic"], "")
        self.assertTemplateUsed("pages/check.html")

    def test_profile_page(self):
        resp = self.client.post("/login/", {"username": "qwerty", "password": "qwerty"})
        self.assertEquals(resp.status_code, 200)
        resp = self.client.get("profile/")
        self.assertEquals(resp.context["request_path"], "/profile")
        self.assertTemplateUsed("pages/profile.html")
