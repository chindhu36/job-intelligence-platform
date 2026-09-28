from flask import Blueprint, request, jsonify

from app.services.cv_parser import extract_text_from_pdf

cv_bp = Blueprint("cv", __name__)


@cv_bp.route("/upload", methods=["POST"])
def upload_cv():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    if not file.filename.lower().endswith(".pdf"):
        return jsonify({"error": "Only PDF files are supported"}), 400

    try:
        extracted_text = extract_text_from_pdf(file)

        if not extracted_text:
            return jsonify({"error": "No text could be extracted from the PDF"}), 400

        return jsonify({
            "filename": file.filename,
            "extracted_text": extracted_text,
        }), 200

    except Exception as e:
        return jsonify({
            "error": "Unable to process CV",
            "details": str(e),
        }), 500