from pypdf import PdfReader


def extract_text_from_pdf(file):
    try:
        reader = PdfReader(file)

        text_parts = []

        for page in reader.pages:
            page_text = page.extract_text()

            if page_text:
                text_parts.append(page_text)

        return "\n".join(text_parts).strip()

    except Exception as e:
        raise Exception(f"Unable to extract text from PDF: {e}")