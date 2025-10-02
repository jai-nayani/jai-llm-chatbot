"""
Script to download resumes from Google Drive
Run this script first to download all resume PDFs
"""

import os
import requests
from pathlib import Path

# Google Drive file IDs (extract from sharing links)
RESUME_FILES = {
    "AdithyaJai_Resume_Reference.pdf": "REPLACE_WITH_FILE_ID",
    "AdithyaNayani_Resume_May.pdf": "REPLACE_WITH_FILE_ID",
    "Jai_Final.pdf": "REPLACE_WITH_FILE_ID",
    "Jai_ML.pdf": "REPLACE_WITH_FILE_ID",
    "JaiAdityaN_SDE.pdf": "REPLACE_WITH_FILE_ID",
    "JaiNayani_AI_SDE.pdf": "REPLACE_WITH_FILE_ID",
    "JaiNayani_SDE.pdf": "REPLACE_WITH_FILE_ID",
    "JaiNayani_SDE2.pdf": "REPLACE_WITH_FILE_ID",
}

def download_from_gdrive(file_id, destination):
    """Download file from Google Drive"""
    URL = "https://docs.google.com/uc?export=download"
    
    session = requests.Session()
    response = session.get(URL, params={'id': file_id}, stream=True)
    
    # Save file
    with open(destination, 'wb') as f:
        for chunk in response.iter_content(32768):
            if chunk:
                f.write(chunk)
    
    print(f"Downloaded: {destination}")

def main():
    """Download all resumes"""
    data_dir = Path(__file__).parent
    data_dir.mkdir(exist_ok=True)
    
    print("Downloading resumes from Google Drive...")
    print("\nNOTE: Please manually download PDFs from:")
    print("https://drive.google.com/drive/folders/1E08mYzQwVpu9jvJ08nV4D8_HMwOHl9ZJ")
    print("\nAnd place them in the 'data/' directory\n")
    
    # For now, just create placeholder
    for filename in RESUME_FILES.keys():
        filepath = data_dir / filename
        if not filepath.exists():
            print(f"❌ Missing: {filename}")
        else:
            print(f"✅ Found: {filename}")

if __name__ == "__main__":
    main()

