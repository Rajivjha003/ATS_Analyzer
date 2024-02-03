import unittest
from modules import pdf_processing

class TestPDFProcessing(unittest.TestCase):
    def test_input_pdf_text(self):
        # For this test, you'll need a sample PDF file. 
        # Replace 'sample.pdf' with the path to your sample PDF.
        uploaded_file = open('sample.pdf', 'rb')

        # Call the function with the test input
        text = pdf_processing.input_pdf_text(uploaded_file)

        # Check that the response is a string (replace this with your own checks)
        self.assertIsInstance(text, str)

        # Don't forget to close the file
        uploaded_file.close()

if __name__ == '__main__':
    unittest.main()
