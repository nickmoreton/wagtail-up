from wagtail.tests.utils import WagtailPageTests

from app.home.models import HomePage


class MyPageTests(WagtailPageTests):
    # There's only one page model, so we can only test one page type
    def test_can_create_home_page(self):
        self.assertCanCreateAt(HomePage, HomePage)
