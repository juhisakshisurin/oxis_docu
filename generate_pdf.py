import subprocess
import os
import time

# Paths
chrome_search_paths = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LocalAppData%\Google\Chrome\Application\chrome.exe")
]

# Select Chrome path
chrome_path = None
for path in chrome_search_paths:
    if os.path.exists(path):
        chrome_path = path
        break

if not chrome_path:
    print("Error: Google Chrome executable not found in standard paths.")
    exit(1)

print(f"Using Chrome executable at: {chrome_path}")

current_dir = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(current_dir, "profile.html")
pdf_path = os.path.join(current_dir, "profile.pdf")

# Arguments for headless Chrome print to PDF
cmd = [
    chrome_path,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    "--disable-pdf-tagging",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    html_path
]

print("Executing PDF generation command...")
result = subprocess.run(cmd, capture_output=True, text=True)

print(f"Process return code: {result.returncode}")
if result.stdout:
    print(f"Stdout: {result.stdout}")
if result.stderr:
    print(f"Stderr: {result.stderr}")

time.sleep(1.5)

if os.path.exists(pdf_path):
    size_kb = os.path.getsize(pdf_path) / 1024
    print(f"Success! PDF generated at: {pdf_path}")
    print(f"File Size: {size_kb:.2f} KB")
else:
    print("Error: PDF file was not generated.")
    exit(1)
