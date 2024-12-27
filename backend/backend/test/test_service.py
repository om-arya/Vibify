from django.test import TestCase
from http import HTTPStatus
import json
import backend.service.user_service as user_service
import backend.service.vibe_service as vibe_service

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
        self.assertEqual(create_user_response2.status_code, HTTPStatus.BAD_REQUEST)

        create_user_response3 = user_service.create_user(username2, self.email, password2, first_name2, last_name2) # Email taken
        self.assertEqual(create_user_response3.status_code, HTTPStatus.BAD_REQUEST)

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


class VibeServiceTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.username = "bob123"
        cls.name = "Relaxing beach day"
        cls.color = "green"
        user_service.create_user(cls.username, "bob@mail.com", "bobpass", "Bob", "Smith")

    def test_vibe_create_delete_success(self):
        create_vibe_response = vibe_service.create_vibe(self.username, self.name, self.color)
        self.assertEqual(create_vibe_response.status_code, HTTPStatus.CREATED)

        delete_vibe_response = vibe_service.delete_vibe(self.username, self.name)
        self.assertEqual(delete_vibe_response.status_code, HTTPStatus.OK)

    def test_vibe_read_one_success(self):
        vibe_service.create_vibe(self.username, self.name, self.color)

        get_vibe_response = vibe_service.get_vibe(self.username, self.name)
        self.assertEqual(get_vibe_response.status_code, HTTPStatus.OK)

        vibe = json.loads(get_vibe_response.content.decode())
        self.assertEqual(vibe["user"], self.username)
        self.assertEqual(vibe["name"], self.name)
        self.assertEqual(vibe["color"], self.color)

        vibe_service.delete_vibe(self.username, self.name)

    def test_vibe_read_many_success(self):
        name2 = "Sadness :("
        name3 = "Tuff stuff"
        name4 = "Watching the sunset at 6:34pm"

        vibe_service.create_vibe(self.username, self.name, self.color)
        vibe_service.create_vibe(self.username, name2, "blue")
        vibe_service.create_vibe(self.username, name3, "yellow")
        vibe_service.create_vibe(self.username, name4, "red")

        get_user_vibes_response = vibe_service.get_user_vibes(self.username)
        self.assertEqual(get_user_vibes_response.status_code, HTTPStatus.OK)

        vibes = json.loads(get_user_vibes_response.content.decode())
        self.assertEqual(len(vibes), 4)
        
        # Should be in alphabetical order
        self.assertEqual(vibes[0]["fields"]["name"], self.name)
        self.assertEqual(vibes[1]["fields"]["name"], name2)
        self.assertEqual(vibes[2]["fields"]["name"], name3)
        self.assertEqual(vibes[3]["fields"]["name"], name4)

        vibe_service.delete_vibe(self.username, self.name)
        vibe_service.delete_vibe(self.username, name2)
        vibe_service.delete_vibe(self.username, name3)
        vibe_service.delete_vibe(self.username, name4)

    def test_vibe_update_success(self):
        vibe_service.create_vibe(self.username, self.name, self.color)

        new_color = "orange"

        set_vibe_color_response = vibe_service.set_vibe_color(self.username, self.name, new_color)
        self.assertEqual(set_vibe_color_response.status_code, HTTPStatus.OK)

        get_vibe_response = vibe_service.get_vibe(self.username, self.name)
        self.assertEqual(get_vibe_response.status_code, HTTPStatus.OK)

        updated_vibe = json.loads(get_vibe_response.content.decode())
        self.assertEqual(updated_vibe["color"], new_color)

        vibe_service.delete_vibe(self.username, self.name)

    def test_vibe_create_success_and_failure(self):
        name2 = "idk"

        create_vibe_response1 = vibe_service.create_vibe(self.username, self.name, self.color)
        self.assertEqual(create_vibe_response1.status_code, HTTPStatus.CREATED)

        create_vibe_response2 = vibe_service.create_vibe(self.username, self.name, self.color) # Name taken
        self.assertEqual(create_vibe_response2.status_code, HTTPStatus.BAD_REQUEST)

        create_vibe_response3 = vibe_service.create_vibe(self.username, name2, self.color)
        self.assertEqual(create_vibe_response3.status_code, HTTPStatus.CREATED)

        vibe_service.delete_vibe(self.username, self.name)
        vibe_service.delete_vibe(self.username, name2)

    def test_vibe_read_failure(self):
        vibe_service.create_vibe(self.username, self.name, self.color)

        name2 = "Coding."
        
        get_vibe_response1 = vibe_service.get_vibe(self.username, name2)
        self.assertEqual(get_vibe_response1.status_code, HTTPStatus.NOT_FOUND)

        vibe_service.delete_vibe(self.username, self.name)

        get_vibe_response2 = vibe_service.get_vibe(self.username, self.name)
        self.assertEqual(get_vibe_response2.status_code, HTTPStatus.NOT_FOUND)