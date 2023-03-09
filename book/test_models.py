from django.test import TestCase
from .models import Book
from django.contrib.auth.models import User


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user for testing purposes
        cls.user = User.objects.create_user(
            username='aldwin',
            password='testcasedjango2023'
        )

        # Create a book for testing purposes
        cls.book = Book.objects.create(
            user=cls.user,
            name='Aldwin Arriola',
            phone='555-555-5555',
            email='araldwin@gmail.com',
            people='2',
            message='Test message'
        )

    def test_book_str_method(self):
        self.assertEqual(str(self.book), 'Aldwin Arriola')

    def test_book_user_relationship(self):
        self.assertEqual(self.book.user, self.user)

    def test_book_fields(self):
        self.assertEqual(self.book.name, 'Aldwin Arriola')
        self.assertEqual(self.book.phone, '555-555-5555')
        self.assertEqual(self.book.email, 'araldwin@gmail.com')
        self.assertEqual(self.book.people, '2')
        self.assertEqual(self.book.message, 'Test message')
