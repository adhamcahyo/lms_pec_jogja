from django.test import TestCase
from django.urls import reverse

class ChatbotTestCase(TestCase):
    def test_chatbot_response(self):
        # Test chatbot response for a given user input
        user_input = "Hello"
        response = self.client.post(reverse('get_response'), {'user_message': user_input})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'response': 'Hi, how can I help you?'})
        
    def test_invalid_input(self):
        # Test chatbot response for invalid input
        user_input = ""
        response = self.client.post(reverse('get_response'), {'user_message': user_input})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'response': 'Sorry, I didn\'t understand that.'})

    def test_empty_response(self):
        # Test chatbot response for empty input
        user_input = "What is the weather like today?"
        response = self.client.post(reverse('get_response'), {'user_message': user_input})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'response': ''})

    def test_long_response(self):
        # Test chatbot response for a long input
        user_input = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        response = self.client.post(reverse('get_response'), {'user_message': user_input})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'response': 'Sorry, I can only process short messages.'})
