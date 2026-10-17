# OXIS & OXEV — Corporate Profile Documentation

## Overview

This repository contains the documentation and profile-generation resources for **OXIS and OXEV**. It includes HTML-based corporate profiles, PDF documents, Python scripts for document generation, and supporting image assets.

## Features

- **Corporate Profile:** HTML-based profile pages for OXIS and OXEV.
- **PDF Generation:** Generate PDF documents from profile content.
- **HTML Embedding:** Python utilities for embedding content and generating profile documents.
- **Asset Management:** Organized image resources for use in profile pages.
- **Reusable Scripts:** Separate Python scripts for document generation and related tasks.

## Project Structure

```text
oxis_docu/
├── images/
├── .gitignore
├── embed_and_generate.py
├── generate_pdf.py
├── profile.html
├── profile.pdf
├── profile_final.html
└── README.md
```

## Technologies Used

- **HTML** — Profile structure and content
- **Python** — Document processing and generation
- **PDF** — Exported corporate profile documents

## Getting Started

### Prerequisites

- Python 3.x
- Required Python packages used by the scripts
- Any additional dependencies specified in the source code

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/juhisakshisurin/oxis_docu.git
   ```

2. Navigate to the project directory:

   ```bash
   cd oxis_docu
   ```

3. Install the required dependencies, if applicable:

   ```bash
   pip install -r requirements.txt
   ```

   If a `requirements.txt` file is not present, install the dependencies required by the Python scripts.

### Usage

Run the relevant Python script from the project directory:

```bash
python generate_pdf.py
```

For the embedding and profile-generation workflow:

```bash
python embed_and_generate.py
```

The generated output depends on the script configuration and available input files.

## Output

The repository includes HTML profile documents and a PDF profile. Running the scripts can generate or update documents according to their implementation.

## Website

Visit the official OXIS website: https://oxis.in/

## Repository

GitHub: https://github.com/juhisakshisurin/oxis_docu

## License

No license has been specified for this repository. Please contact the repository owner for permission before reusing or distributing its contents.

---

*Maintained as part of the OXIS and OXEV corporate profile documentation project.*
