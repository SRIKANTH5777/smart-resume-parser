# Smart Resume Parser 🧠📄

> A lightweight and powerful resume parser built with Python and NLP — designed to extract key candidate information from PDF and DOCX resumes in seconds.

---

[![GitHub stars](https://img.shields.io/github/stars/SRIKANTH5777/smart-resume-parser.svg)](https://github.com/SRIKANTH5777/smart-resume-parser/stargazers)
[![License](https://img.shields.io/github/license/SRIKANTH5777/smart-resume-parser.svg)](https://github.com/SRIKANTH5777/smart-resume-parser/blob/main/LICENSE)
[![Python Version](https://img.shields.io/pypi/pyversions/Django.svg)](https://python.org)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#)

---

### ✨ Key Features

- Extracts:
  - ✅ Full Name
  - ✅ Email Address
  - ✅ Phone Number
  - ✅ Skills
  - ✅ Experience
  - ✅ Degree
  - ✅ College Name
  - ✅ Designation
  - ✅ Company Names
- Supports `.pdf` and `.docx` files
- CLI tool for batch parsing resumes

---

### ⚙️ Installation

Make sure you have Python 3.6+ installed.

```bash
pip install -r requirements.txt

Install required language models for NLP:

bash
Copy
Edit
python -m spacy download en_core_web_sm
python -m nltk.downloader stopwords
python -m nltk.downloader words

---
Quick Start
python
Copy
Edit
from pyresparser import ResumeParser

data = ResumeParser("path/to/resume.pdf").get_extracted_data()
print(data)

Supported File Formats
.pdf and .docx are supported by default

To use .doc files, install textract

