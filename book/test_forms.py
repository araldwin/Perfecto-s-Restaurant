from django.test import TestCase
from .forms import BookForm



class BookFormTest(TestCase):

    def test_form_valid_data(self):
        form = BookForm(data={
            'name': 'Juan Tamad',
            'phone': '1234567890',
            'book_date': '2023-03-01',
            'book_time': '12:00',
            'people': '4',
            'message': 'This is a test message.'
        })
        self.assertTrue(form.is_valid())

    def test_form_missing_required_fields(self):
        form = BookForm(data={
            'name': '',
            'phone': '',
            'book_date': '',
            'book_time': '',
            'people': '',
            'message': ''
        })
        self.assertFalse(form.is_valid())
        # should have 5 errors for missing required fields
        self.assertEqual(len(form.errors), 5)

    def test_form_invalid_data(self):
        form = BookForm(data={
            'name': 'John Smith',
            'phone': '1234567890',
            'book_date': 'invalid date',
            'book_time': 'invalid time',
            'people': '-1',
            'message': 'This is a test message.'
        })
        self.assertFalse(form.is_valid())
        # should have 3 errors for invalid data
        self.assertEqual(len(form.errors), 3)
