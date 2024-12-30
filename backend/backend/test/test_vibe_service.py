from django.test import TestCase
from http import HTTPStatus
import json
import backend.service.user_service as user_service
import backend.service.vibe_service as vibe_service

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