import os
import glob

def update_emails():
    html_files = glob.glob('email*.html')
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Change blue to red
        content = content.replace('#2E75B6', '#CC0000')
        
        # Insert logo
        logo_html = '\n<div style="text-align:center; margin-bottom:20px;"><img src="Logo.png" alt="All Clean Property Services Logo" style="max-width:200px; height:auto;"></div>\n'
        
        if '<tr><td style="padding:32px 40px;">' in content:
            content = content.replace('<tr><td style="padding:32px 40px;">', '<tr><td style="padding:32px 40px;">' + logo_html)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print(f"Updated {len(html_files)} HTML files.")

if __name__ == '__main__':
    update_emails()
