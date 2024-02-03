import unittest
from modules import generative_ai

class TestGenerativeAI(unittest.TestCase):
    def test_get_gemini_response(self):
        # Define a simple input
        input = "Hello, world!"

        # Call the function with the test input
        response = generative_ai.get_gemini_response(input)

        # Check that the response is a string (replace this with your own checks)
        self.assertIsInstance(response, str)

if __name__ == '__main__':
    unittest.main()
