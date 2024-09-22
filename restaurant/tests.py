from django.test import TestCase
from .models import Menu, Booking

# Create your tests here.
class MenuItemTest(TestCase):
    def test_get_menu_items(self):
        items = Menu.objects.all()
        for item in items:
         return self.assertCountEqual(item.title, 'Test Success')

class BookingTest(TestCase):
    def test_get_booking_(self):
        bookings = Booking.objects.all()
        for booking in bookings:
         return self.assertCountEqual(booking.name, 'Test Success')