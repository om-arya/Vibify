from django.test import TestCase
from http import HTTPStatus
import json
import backend.service.user_service as user_service

class UserServiceTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.username = "Bob123"
        cls.first_name = "Bob"
        cls.last_name = "Smith"
        cls.email = "bobsmith123@mail.com"
        cls.password = "bobpassword"

    def test_user_create_delete_success(self):
        create_user_response = user_service.create_user(self.username, self.email, self.password, self.first_name, self.last_name)
        self.assertEqual(create_user_response.status_code, HTTPStatus.CREATED)

        delete_user_response = user_service.delete_user(self.username)
        self.assertEqual(delete_user_response.status_code, HTTPStatus.OK)

    def test_user_read_success(self):
        user_service.create_user(self.username, self.email, self.password, self.first_name, self.last_name)

        get_user_by_username_response = user_service.get_user_by_username(self.username)
        self.assertEqual(get_user_by_username_response.status_code, HTTPStatus.OK)

        user_by_username = json.loads(get_user_by_username_response.content.decode())
        self.assertEqual(user_by_username["username"], self.username)
        self.assertEqual(user_by_username["email"], self.email)
        self.assertNotEqual(user_by_username["password"], self.password) # Should be hashed
        self.assertEqual(user_by_username["first_name"], self.first_name)
        self.assertEqual(user_by_username["last_name"], self.last_name)

        get_user_by_email_response = user_service.get_user_by_email(self.email)
        self.assertEqual(get_user_by_email_response.status_code, HTTPStatus.OK)
        
        user_by_email = json.loads(get_user_by_email_response.content.decode())
        self.assertEqual(user_by_email["username"], self.username)
        self.assertEqual(user_by_email["email"], self.email)
        self.assertNotEqual(user_by_email["password"], self.password) # Should be hashed
        self.assertEqual(user_by_email["first_name"], self.first_name)
        self.assertEqual(user_by_email["last_name"], self.last_name)

        user_service.delete_user(self.username)

    def test_user_update_success(self):
        user_service.create_user(self.username, self.email, self.password, self.first_name, self.last_name)

        new_first_name = "Johnny"
        new_last_name = "Johnson"
        new_email = "jojo@mail.com"
        new_password = "jj123"

        set_user_first_name_response = user_service.set_user_first_name(self.username, new_first_name)
        self.assertEqual(set_user_first_name_response.status_code, HTTPStatus.OK)
        
        set_user_last_name_response = user_service.set_user_last_name(self.username, new_last_name)
        self.assertEqual(set_user_last_name_response.status_code, HTTPStatus.OK)

        set_user_email_response = user_service.set_user_email(self.username, new_email)
        self.assertEqual(set_user_email_response.status_code, HTTPStatus.OK)

        set_user_password_response = user_service.set_user_password(self.username, new_password)
        self.assertEqual(set_user_password_response.status_code, HTTPStatus.OK)

        get_user_by_username_response = user_service.get_user_by_username(self.username)
        self.assertEqual(get_user_by_username_response.status_code, HTTPStatus.OK)

        updated_user = json.loads(get_user_by_username_response.content.decode())
        self.assertEqual(updated_user["username"], self.username)
        self.assertEqual(updated_user["email"], new_email)
        self.assertNotEqual(updated_user["password"], new_password) # Should be hashed
        self.assertEqual(updated_user["first_name"], new_first_name)
        self.assertEqual(updated_user["last_name"], new_last_name)

        get_user_by_email_response1 = user_service.get_user_by_email(self.email)
        self.assertEqual(get_user_by_email_response1.status_code, HTTPStatus.NOT_FOUND)

        get_user_by_email_response2 = user_service.get_user_by_email(new_email)
        self.assertEqual(get_user_by_email_response2.status_code, HTTPStatus.OK)

        user_service.delete_user(self.username)

    def test_user_create_success_and_failure(self):
        username2 = "jjson"
        first_name2 = "Johnny"
        last_name2 = "Johnson"
        email2 = "jojo@mail.com"
        password2 = "jj123"

        create_user_response1 = user_service.create_user(self.username, self.email, self.password, self.first_name, self.last_name)
        self.assertEqual(create_user_response1.status_code, HTTPStatus.CREATED)

        create_user_response2 = user_service.create_user(self.username, email2, password2, first_name2, last_name2) # Username taken
        self.assertEqual(create_user_response2.status_code, HTTPStatus.CONFLICT)

        create_user_response3 = user_service.create_user(username2, self.email, password2, first_name2, last_name2) # Email taken
        self.assertEqual(create_user_response3.status_code, HTTPStatus.CONFLICT)

        create_user_response4 = user_service.create_user(username2, email2, password2, first_name2, last_name2)
        self.assertEqual(create_user_response4.status_code, HTTPStatus.CREATED)

        user_service.delete_user(self.username)
        user_service.delete_user(username2)

    def test_user_read_failure(self):
        user_service.create_user(self.username, self.email, self.password, self.first_name, self.last_name)

        username2 = "jjson"
        email2 = "jojo@mail.com"
        
        get_user_by_username_response1 = user_service.get_user_by_username(username2)
        self.assertEqual(get_user_by_username_response1.status_code, HTTPStatus.NOT_FOUND)

        get_user_by_email_response1 = user_service.get_user_by_email(email2)
        self.assertEqual(get_user_by_email_response1.status_code, HTTPStatus.NOT_FOUND)

        user_service.delete_user(self.username)

        get_user_by_username_response2 = user_service.get_user_by_username(self.username)
        self.assertEqual(get_user_by_username_response2.status_code, HTTPStatus.NOT_FOUND)

        get_user_by_email_response2 = user_service.get_user_by_email(self.email)
        self.assertEqual(get_user_by_email_response2.status_code, HTTPStatus.NOT_FOUND)