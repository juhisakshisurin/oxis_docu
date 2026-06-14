"""
embed_and_generate.py
Embeds gallery images as base64 data URIs into profile.html, writes
a self-contained profile_final.html, then compiles to profile.pdf.
"""
import subprocess, os, time, base64, re

BASE = os.path.dirname(os.path.abspath(__file__))

# ── 1. Read source HTML ────────────────────────────────────────────────────────
with open(os.path.join(BASE, "profile.html"), "r", encoding="utf-8") as f:
    html = f.read()

# ── 2. Replace image src references with base64 data URIs ─────────────────────
IMAGE_MAP = {
    "images/hackathon.png": os.path.join(BASE, "images", "hackathon.png"),
    "images/dashboard.png": os.path.join(BASE, "images", "dashboard.png"),
    "images/networking.png": os.path.join(BASE, "images", "networking.png"),
}

for rel_path, abs_path in IMAGE_MAP.items():
    if not os.path.exists(abs_path):
        print(f"  WARNING: {abs_path} not found — skipping")
        continue
    with open(abs_path, "rb") as img_f:
        b64 = base64.b64encode(img_f.read()).decode("utf-8")
    data_uri = f"data:image/png;base64,{b64}"
    html = html.replace(f'src="{rel_path}"', f'src="{data_uri}"')
    print(f"  Embedded {rel_path} ({len(b64)//1024} KB base64)")

# ── 3. Write self-contained HTML ───────────────────────────────────────────────
final_html = os.path.join(BASE, "profile_final.html")
with open(final_html, "w", encoding="utf-8") as f:
    f.write(html)
print(f"\nSelf-contained HTML written to: {final_html}")

# ── 4. Locate Chrome ──────────────────────────────────────────────────────────
chrome_paths = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    os.path.expandvars(r"%LocalAppData%\Google\Chrome\Application\chrome.exe"),
]
chrome = next((p for p in chrome_paths if os.path.exists(p)), None)
if not chrome:
    raise RuntimeError("Chrome not found")

# ── 5. Compile PDF ────────────────────────────────────────────────────────────
pdf_path = os.path.join(BASE, "profile.pdf")
cmd = [
    chrome,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    "--no-pdf-header-footer",
    "--disable-pdf-tagging",
    f"--print-to-pdf={pdf_path}",
    final_html,
]
print("\nGenerating PDF...")
result = subprocess.run(cmd, capture_output=True, text=True)
print(f"Return code: {result.returncode}")
if result.stderr:
    print(f"Stderr: {result.stderr[:300]}")

time.sleep(1.5)
if os.path.exists(pdf_path):
    size_kb = os.path.getsize(pdf_path) / 1024
    print(f"\n[OK] PDF ready: {pdf_path}")
    print(f"  Size: {size_kb:.1f} KB ({size_kb/1024:.2f} MB)")
else:
    print("\n[FAIL] PDF generation failed.")
