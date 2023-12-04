from django.test import TestCase, RequestFactory
from restaurant.views import MenuItemsView
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        menu_item = Menu.objects.create(title = "IceCream", price = 10, inventory = 100)
        return super().setUp()

    def test_getall(self):
        req = RequestFactory().get('/restaurant/menu/')
        view = MenuItemsView()
        view.setup(req)

        ctx = str(view.get_queryset())
        self.assertIn("IceCream : 10.00", ctx)

