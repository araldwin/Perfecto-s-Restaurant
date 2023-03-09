from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from book.forms import RegisterUserForm
from django.contrib.auth import authenticate
from datetime import date
from food.models import Food
from .models import Book


class RegisterUserFormTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('register_user')

    def test_valid_form_creates_user(self):
        form_data = {
            'username': 'aldwin',
            'email': 'araldwin@gmail.com',
            'first_name': 'Aldwin',
            'last_name': 'Arriola',
            'password1': 'testcasedjango2023',
            'password2': 'testcasedjango2023',
        }
        form = RegisterUserForm(data=form_data)
        self.assertTrue(form.is_valid())

        response = self.client.post(self.url, form_data)
        self.assertEqual(response.status_code, 200)

        user = User.objects.get(username=form_data['username'])
        self.assertIsNotNone(user)
        self.assertEqual(user.email, form_data['email'])

    def test_invalid_form_returns_error(self):
        form_data = {
            'username': 'aldwin',
            'email': 'araldwingmail.com',
            'first_name': 'Aldwin',
            'last_name': 'Arriola',
            'password1': 'testcasedjango2023',
            'password2': 'testcasedjango2023',
        }
        form = RegisterUserForm(data=form_data)
        self.assertFalse(form.is_valid())

        response = self.client.post(self.url, form_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'Enter a valid email address.', response.content)

    def test_username_already_exists(self):
        User.objects.create_user(
            username='aldwin',
            email='araldwin@gmail.com',
            password='testcasedjango2023'
        )

        form_data = {
            'username': 'aldwin',
            'email': 'araldwin@gmail.com',
            'first_name': 'Aldwin',
            'last_name': 'Arriola',
            'password1': 'testcasedjango2023',
            'password2': 'testcasedjango2023',
        }
        form = RegisterUserForm(data=form_data)
        self.assertFalse(form.is_valid())

        response = self.client.post(self.url, form_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'A user with that username already exists.',
                      response.content)

    def test_email_already_exists(self):
        User.objects.create_user(
            username='alwin',
            email='araldwin@gmail.com',
            password='testcasedjango2023'
        )

        form_data = {
            'username': 'winald',
            'email': 'araldwin@gmail.com',
            'first_name': 'winald',
            'last_name': 'Arriola',
            'password1': 'win08032023',
            'password2': 'win08032023',
        }
        form = RegisterUserForm(data=form_data)
        self.assertFalse(form.is_valid())

        response = self.client.post(self.url, form_data)
        self.assertEqual(response.status_code, 400)
        self.assertIn(b'This email address already exists.', response.content)

    def test_register_user_renders_correct_template(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register_modal.html')
        self.assertIsInstance(response.context['form'], RegisterUserForm)


class LoginTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='aldwin',
            password='testcasedjango2023'
        )

    def test_login_with_valid_credentials(self):
        url = reverse('login')
        response = self.client.post(
            url,
            {
                'username': 'aldwin',
                'password': 'testcasedjango2023'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Success')
        self.assertTrue(
            authenticate(
                username='aldwin',
                password='testcasedjango2023'
            )
        )

    def test_login_with_invalid_credentials(self):
        url = reverse('login')
        response = self.client.post(
            url,
            {
                'username': 'aldwin',
                'password': '1234567abc'
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            'There Was An Error Logging In, Try Again...'
        )
        self.assertFalse(
            authenticate(
                username='testuser',
                password='1234567abc'
            )
        )

    def test_login_renders_login_page(self):
        url = reverse('login')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')


class LogoutTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('logout')
        self.user = User.objects.create_user(
            username='aldwin',
            email='araldwin@gmail.com',
            password='testcasedjango2023'
        )

    def test_logout(self):

        self.client.login(username='aldwin', password='testcasedjango2023')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertRedirects(response, reverse('home'))


class HomeViewTest(TestCase):
    def setUp(self):
        self.url = reverse('home')
        Food.objects.create(name='Burger',
                            description='Juicy beef burger with cheese',
                            price=9.99)

    def test_home_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, 'Burger')
        self.assertContains(response, 'Juicy beef burger with cheese')
        self.assertContains(response, '9.99')


class AddReservationTestCase(TestCase):
    def setUpTestCase(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='aldwin',
            password='testcasedjango2023'
        )

    def test_reservation_submitted(self):
        self.client.login(username='aldwin', password='testcasedjango2023')
        response = self.client.post(reverse('add-reservation'), {
            'name': 'Aldwin Arriola',
            'phone': '1234567890',
            'email': 'araldwin@gmail.com',
            'book_date': '2024-03-08',
            'book_time': '12:00',
            'people': 2,
            'message': '',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url,
                         reverse('add-reservation') + '?submitted=True')
        self.assertTrue(
            Book.objects.filter(user=self.user, name='Aldwin Arriola').exists()
        )

        url = reverse('add-reservation') + '?submitted=True'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_reservation.html')
        self.assertTrue(response.context['submitted'])

    def test_reservation_already_exists(self):
        self.client.login(username='aldwin', password='testcasedjango2023')

        existing_reservation = Book.objects.create(
            user=self.user,
            name='Juan Tamad',
            phone='1234567890',
            email='araldwin@gmail.com',
            book_date='2023-05-08',
            book_time='12:00',
            people=2,
            message='',
        )

        response = self.client.post(reverse('add-reservation'), {
            'name': 'Aldwin Arriola',
            'phone': '1234567890',
            'email': 'araldwin@gmail.com',
            'book_date': '2023-05-08',
            'book_time': '12:00',
            'people': 2,
            'message': '',
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['form'].is_valid())
        self.assertFalse(
            Book.objects.filter(user=self.user, name='Aldwin Arriola').exists()
                )
        self.assertTrue(
            Book.objects.filter(user=self.user, name='Juan Tamad').exists()
            )
        expected_error = 'You have already reserved a table for this date.'
        self.assertEqual(
            response.context['form'].errors['book_date'],
            [expected_error],
            msg='Incorrect error message for booking date.'
        )

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='aldwin',
            password='testcasedjango2023'
        )

    def test_reservation_invalid(self):
        self.client.login(username='aldwin', password='testcasedjango2023')
        response = self.client.post(reverse('add-reservation'), {
            'name': '',
            'phone': '1234567890',
            'email': 'araldwin@gmail.com',
            'book_date': '2023-03-08',
            'book_time': '12:00',
            'people': 2,
            'message': '',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_reservation.html')
        self.assertFalse(response.context['form'].is_valid())
        self.assertFalse(
            Book.objects.filter(user=self.user, name='Aldwin Arriola').exists()
        )


class ListReservationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='aldwin',
            password='testcasedjango2023'
        )
        self.client.login(username='aldwin', password='testcasedjango2023')
        Book.objects.create(
            book_date='2022-06-30',
            book_time='19:30:00',
            people='4',
            email='araldwin',
            phone='1234567890',
            message='This is a test message'
        )

    def test_list_reservation(self):
        response = self.client.get(reverse('list-reservation'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Reservation list')
        self.assertTemplateUsed(response, 'reservation_list.html')

    def test_list_reservation_user_filter(self):
        other_user = User.objects.create_user(
            username='other_user',
            password='testcasedjango2023'
        )
        Book.objects.create(
            book_date='2023-06-30',
            book_time='19:30:00',
            people='4',
            email='other_user',
            phone='1234567890',
            message='This is a test message',
            user=other_user
        )
        Book.objects.create(
            book_date='2023-07-01',
            book_time='20:00:00',
            people='2',
            email='aldwin',
            phone='0987654321',
            message='This is another test message',
            user=self.user
        )
        response = self.client.get(reverse('list-reservation'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Reservation list')
        self.assertTemplateUsed(response, 'reservation_list.html')
        self.assertContains(response, 'aldwin')
        self.assertNotContains(response, 'other_user')


class UpdateReservationTestCase(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(
            username='aldwin',
            password='testcasedjango2023'
        )
        self.reservation = Book.objects.create(
            user=self.user,
            book_date=date(2023, 3, 10))
        self.url = reverse('update-reservation', args=[self.reservation.pk])

    def test_update_reservation_success(self):
        data = {
            'name': 'Aldwin Arriola',
            'phone': '1234567890',
            'email': 'araldwin@gmail.com',
            'book_date': '2023-03-11',
            'book_time': '12:00',
            'people': 2,
            'message': '',
        }
        self.client.login(username='aldwin', password='testcasedjango2023')
        url = reverse('update-reservation', args=[self.reservation.pk])
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('list-reservation'))
        self.reservation.refresh_from_db()
        self.assertEqual(self.reservation.book_date, date(2023, 3, 11))


class DeleteReservationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='aldwin',
            password='testcasedjango2023'
        )
        self.reservation = Book.objects.create(
            user=self.user,
            book_date=date(2023, 3, 10)
        )

    def test_delete_reservation(self):
        self.client.login(username='aldwin', password='testcasedjango2023')
        url = reverse('delete-reservation', args=[self.reservation.pk])
        response = self.client.post(url)
        self.assertRedirects(response, reverse('list-reservation'))
        self.assertFalse(Book.objects.filter(pk=self.reservation.pk).exists())