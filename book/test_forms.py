from django.test import TestCase
from datetime import date, timedelta
from .forms import BookForm, RegisterUserForm
from django.contrib.auth.models import User


class BookFormTest(TestCase):
    """
    A TestCase class for testing the BookForm form used to make reservations
    in a restaurant application.

    Methods:
    -------
    setUp():
        Sets up the test data to be used in the test methods.
    test_valid_form():
        Tests that a valid form is indeed valid.
    test_message_not_required():
        Tests that a form without a message field is valid.
    test_past_date():
        Tests that the form is invalid if the book date is in the past.
    test_invalid_time():
        Tests that the form is invalid if the book time is outside
        the restaurant's opening hours.
    test_maximum_people():
        Tests that the form is invalid if the number of people is
        greater than the restaurant's maximum capacity.
    test_minimum_people():
        Tests that the form is invalid if the number of people is
        less than the restaurant's minimum capacity.
    """
    def setUp(self):
        self.form_data = {
            'name': 'Aldwin Arriola',
            'phone': '123-456-7890',
            'email': 'araldwin@gmail.com',
            'book_date': '2023-08-31',
            'book_time': '13:00',
            'people': 4,
            'message': 'This is a Test message',
        }

    def test_valid_form(self):
        form = BookForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_message_not_required(self):
        form_data = {
            'name': 'Aldwin Arriola',
            'phone': '123-456-7890',
            'email': 'araldwin@gmail.com',
            'book_date': '2023-03-14',
            'book_time': '12:30',
            'people': '2',
        }
        form = BookForm(data=form_data)
        self.assertTrue(form.is_valid(), form.errors)

    def test_past_date(self):
        self.form_data['book_date'] = date.today() - timedelta(days=1)
        form = BookForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('book_date', form.errors)
        self.assertEqual(
            form.errors['book_date'], ['Book date cannot be in the past'])

    def test_invalid_time(self):
        self.form_data['book_time'] = '09:00'
        form = BookForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('book_time', form.errors)
        self.assertEqual(
            form.errors['book_time'],
            ['You can only reserve a table between 10:00 to 19:00.'])

    def test_maximum_people(self):
        self.form_data['people'] = 15
        form = BookForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('people', form.errors)
        self.assertEqual(
            form.errors['people'],
            ['Ensure this value is less than or equal to 10.'])

    def test_minimum_people(self):
        self.form_data['people'] = 0
        form = BookForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('people', form.errors)
        self.assertEqual(
            form.errors['people'],
            ['Ensure this value is greater than or equal to 1.'])


class RegisterUserFormTest(TestCase):
    """
    A TestCase class for testing the RegisterUserForm form used
    to register users in a Django application.

    Methods:
    --------
    setUp():
        Sets up the test data to be used in the test methods.
    test_valid_form():
        Tests that a valid form is indeed valid.
    test_duplicate_email():
        Tests that the form is invalid if a user with the
        same email already exists.
    test_username_already_exists():
        Tests that the form is invalid if a user with the
        same username already exists.
    """
    def setUp(self):
        self.user_data = {
            'username': 'aldwin',
            'email': 'araldin@gmail.com',
            'first_name': 'Aldwin',
            'last_name': 'Arriola',
            'password1': 'testcasedjango2023',
            'password2': 'testcasedjango2023',
        }

    def test_valid_form(self):
        form = RegisterUserForm(data=self.user_data)
        self.assertTrue(form.is_valid())

    def test_duplicate_email(self):
        User.objects.create_user(
            username='aldwin2',
            email='araldin@gmail.com',
            password='testcasedjango2023'
        )
        form = RegisterUserForm(data=self.user_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        self.assertEqual(
            form.errors['email'], ['This email address already exists.'])

    def test_username_already_exists(self):
        User.objects.create_user(
            username='aldwin',
            email='araldin@gmail.com',
            password='testcasedjango2023'
        )
        form = RegisterUserForm(data=self.user_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertEqual(
            form.errors['username'],
            ['A user with that username already exists.'])
