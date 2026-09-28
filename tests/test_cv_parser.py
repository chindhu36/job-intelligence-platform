from app.services import cv_parser


def test_extract_text_from_pdf(monkeypatch):
    # Simulate a PDF containing two pages of text
    class MockPage:
        def __init__(self, text):
            self.text = text

        def extract_text(self):
            return self.text

    class MockPdfReader:
        def __init__(self, file):
            self.pages = [
                MockPage("Python Developer with 4 years of experience."),
                MockPage("Skills: Python, SQL, Flask and Azure."),
            ]

    # Replace PdfReader with our mock
    monkeypatch.setattr(cv_parser, "PdfReader", MockPdfReader)

    result = cv_parser.extract_text_from_pdf("mock_cv.pdf")

    assert "Python Developer with 4 years of experience." in result
    assert "Skills: Python, SQL, Flask and Azure." in result
    assert "\n" in result