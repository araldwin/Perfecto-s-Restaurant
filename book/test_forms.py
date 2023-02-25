from django.test import TestCase
from datetime import date, time
from .models import Book
from .forms import BookForm, RegisterUserForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class BookFormTest(TestCase):

    def test_required_fields(self):
        """
        The method creates an empty dictionary form_data and uses it to create
        an instance of the BookForm form. Then, it checks if the form is valid
        using the is_valid() method. Since the form is empty, it should not be
        valid, so the test asserts that form.is_valid() returns False.

        The method then checks that each of the required fields has an error
        message in the form.errors dictionary. This is done using the
        assertIn() method, which checks whether a given value is in a given
        list or dictionary.

        If any of the required fields is missing, the BookForm form should not
        be valid, and the errors dictionary should contain an error message
        for each missing field. Therefore, this test ensures that the required
        fields of the BookForm form are properly validated and that error
        messages are generated when necessary.
        """
        form_data = {}
        form = BookForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('phone', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('book_date', form.errors)
        self.assertIn('book_time', form.errors)
        self.assertIn('people', form.errors)

    def test_valid_form(self):
        """
        The method creates a dictionary form_data that contains valid data for
        all fields of the BookForm form. It then creates an instance of the
        BookForm form with this data, and checks whether the form is valid
        using the is_valid() method.

        Since all fields have valid data, the test expects form.is_valid() to
        return True. Therefore, the test uses the assertTrue() method to
        assert that the result of form.is_valid() is True.

        This test ensures that the BookForm form can properly validate and
        process valid data, and that a valid form instance can be created
        using this form.
        """
        form_data = {
            'name': 'Juan tamad',
            'phone': '123456789',
            'email': 'jtmad@email.com',
            'book_date': date.today(),
            'book_time': time(10, 30),
            'people': '4',
            'message': 'This is a test message.',
        }
        form = BookForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """
        The method creates a dictionary form_data that contains invalid data
        for the people field of the BookForm form. The value of people in
        form_data is -1, which is less than the minimum value of 1 that was
        set by the clean_people() method in the BookForm class.

        The method then creates an instance of the BookForm form with this
        invalid data and checks whether the form is valid using the is_valid()
        method. Since the value of people is invalid, the is_valid() method
        should return False. Therefore, the test uses the assertFalse() method
        to assert that the result of form.is_valid() is False.

        Finally, the test also checks whether the people field in the form has
        the expected error message. It does this by checking if people is in
        the form.errors dictionary, and whether the error message is the
        expected ['Please enter the number of guests.']. The test uses
        the assertIn() and assertEqual() methods to make these assertions.

        This test ensures that the clean_people() method in the BookForm class
        correctly validates the people field, and that the BookForm form
        correctly identifies and displays error messages for invalid field
        values.
        """
        form_data = {
            'name': 'Juan tamad',
            'phone': '123456789',
            'email': 'jtmad@email.com',
            'book_date': date.today(),
            'book_time': time(10, 30),
            'people': '-1',
            'message': 'This is a test message.',
        }
        form = BookForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('people', form.errors)
        self.assertEqual(form.errors['people'], [
                         'Please enter the number of guests.'])

   
    def test_clean_people(self):
        form_data = {
            'name': 'Juan tamad',
            'phone': '123456789',
            'email': 'jtmad@email.com',
            'book_date': date.today(),
            'book_time': time(10, 30),
            'people': 'ab',
            'message': 'This is a test message.',
        }
        form = BookForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('people', form.errors)
        self.assertEqual(form.errors['people'], [
                         'Invalid value for number of people.'])

        # Test with valid value
        form_data['people'] = '3'
        form = BookForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['people'], 3)

        # Test with zero value
        form_data['people'] = '0'
        form = BookForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('people', form.errors)
        self.assertEqual(form.errors['people'], ['Please enter the number of guests.'])


    


    def test_message_fields_not_required(self):
        """
        It tests whether the form is valid when the message field is left
        blank or empty.

        It first sets up form data with required fields (name, phone, email,
        book_date, book_time, and people) and an empty message field. Then it
        creates an instance of the BookForm with the form_data.

        Finally, it asserts that the form is valid, which means it should pass
        the validation despite the empty message field. If the form is not
        valid, the test would fail.
        """

        form_data = {
            'name': 'Juan tamad',
            'phone': '123456789',
            'email': 'jtmad@email.com',
            'book_date': date.today(),
            'book_time': time(10, 30),
            'people': '4',
            'message': '',
        }
        form = BookForm(data=form_data)
        self.assertTrue(form.is_valid())


class RegisterUserFormTest(TestCase):

    def test_valid_form(self):
        """
        A test function that tests whether the RegisterUserForm form is valid
        when given valid data.

        The function first creates a dictionary form_data with valid data for
        a new user, including a username, first and last name, email, and two
        identical passwords. Then, it creates an instance of the
        RegisterUserForm form, passing in the form_data dictionary as the
        form data. Finally,the function uses the assertTrue method to check
        that the form is valid.

        If the form is valid, this test function should pass without raising
        any errors.
        """
        form_data = {
            'username': 'Juantamad',
            'first_name': 'Juan',
            'last_name': 'Tamad',
            'email': 'jtmad@email.com',
            'password1': 'pass123456789',
            'password2': 'pass123456789',
        }
        form = RegisterUserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """
        It tests for two cases where the form should be invalid.

        The first case is where the password fields do not match. The test
        creates form data with a valid username, email, and password1, but an
        invalid password2. It then creates a form object using this data and
        asserts that the form is not valid, and that the 'password2' field is
        in the form errors.

        The second case is where the username already exists. The test creates
        a user with the same username, and then creates form data with the
        same username, email, and valid passwords. It then creates a form
        object using this data and asserts that the form is not valid, and
        that the 'username' field is in the form errors.
        """

        # Test if the form is invalid when the password fields do not match.
        form_data = {
            'username': 'Juantamad',
            'first_name': 'Juan',
            'last_name': 'Tamad',
            'email': 'jtmad@email.com',
            'password1': 'pass123456789',
            'password2': 'wrongpass123',
        }
        form = RegisterUserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('password2', form.errors)

        # Test if the form is invalid when the username already exists.
        User.objects.create_user(
            username='Juantamad', password='pass123456789')
        form_data = {
            'username': 'Juantamad',
            'first_name': 'Juan',
            'last_name': 'Tamad',
            'email': 'jtmad@email.com',
            'password1': 'pass123456789',
            'password2': 'pass123456789',
        }
        form = RegisterUserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)

    def test_required_fields_empty(self):
        """
        This function tests whether the RegisterUserForm form raises
        validation errors when required fields are left empty.

        The function creates a dictionary form_data with values for username,
        first_name, last_name, email, password1, and password2. first_name,
        last_name, and email are intentionally left empty.

        The function then creates an instance of RegisterUserForm with the
        form_data. Since first_name, last_name, and email are required fields,
        the form should not be valid and should raise validation errors.

        The function then checks whether first_name, last_name, and email are
        in the form's errors dictionary and that the corresponding error
        messages are 'This field is required.' using the self.assertIn and
        self.assertEqual methods.
        """
        form_data = {
            'username': 'user123',
            'first_name': '',
            'last_name': '',
            'email': '',
            'password1': 'pass123456789',
            'password2': 'pass123456789',
        }
        form = RegisterUserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('first_name', form.errors)
        self.assertEqual(form.errors['first_name'],
                         ['This field is required.'])
        self.assertIn('last_name', form.errors)
        self.assertEqual(form.errors['last_name'], ['This field is required.'])
        self.assertIn('email', form.errors)
        self.assertEqual(form.errors['email'], ['This field is required.'])

    def setUp(self):
        # create a user with the email address we will use in the test
        User.objects.create_user(
            username='testuser', email='test@example.com',
            password='password123')

    def test_email_already_exists(self):
        form_data = {
            'username': 'newuser',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'test@example.com',
            'password1': 'password123',
            'password2': 'password123',
        }
        form = RegisterUserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)
        self.assertEqual(form.errors['email'], [
                         'This email address already exists.'])
