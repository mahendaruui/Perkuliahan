import os
import re

LIGHT_CSS = """  <style>
    :root {
      --primary: #4f46e5;
      --primary-hover: #4338ca;
      --primary-light: #e0e7ff;
      --secondary: #0284c7;
      --bg-page: #f8fafc;
      --card-bg: #ffffff;
      --card-subtle: #f8fafc;
      --text-main: #0f172a;
      --text-muted: #64748b;
      --border: #e2e8f0;
      --border-dark: #cbd5e1;
      --accent-green: #059669;
      --accent-amber: #d97706;
      --accent-purple: #9333ea;
      --accent-pink: #db2777;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg-page);
      color: var(--text-main);
      overflow: hidden;
      height: 100vh;
      width: 100vw;
      display: flex;
      flex-direction: column;
      user-select: none;
    }

    /* Top Navigation Bar */
    header {
      padding: 12px 24px;
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 100;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
    }

    .brand {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .brand-logo {
      height: 32px;
      width: auto;
      border-radius: 4px;
    }

    .brand-text {
      font-size: 0.95rem;
      font-weight: 700;
      letter-spacing: -0.02em;
      color: #0f172a;
    }

    .brand-text span {
      color: #4f46e5;
    }

    .brand-sub {
      font-size: 0.75rem;
      color: var(--text-muted);
      font-weight: 500;
    }

    .header-controls {
      display: flex;
      align-items: center;
      gap: 10px;
    }

    .btn-icon {
      background: #ffffff;
      border: 1px solid var(--border-dark);
      color: var(--text-main);
      padding: 6px 12px;
      border-radius: 8px;
      cursor: pointer;
      font-size: 0.85rem;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s ease;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
    }

    .btn-icon:hover {
      background: #f1f5f9;
      border-color: #94a3b8;
    }

    .slide-badge {
      background: #eef2ff;
      border: 1px solid #c7d2fe;
      color: #4338ca;
      padding: 4px 10px;
      border-radius: 20px;
      font-size: 0.8rem;
      font-weight: 700;
      font-family: 'Fira Code', monospace;
    }

    /* Presentation Main Stage */
    main {
      flex: 1;
      position: relative;
      overflow: hidden;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }

    .slide {
      position: absolute;
      width: 92%;
      max-width: 1200px;
      height: 85%;
      background: #ffffff;
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 48px;
      display: flex;
      flex-direction: column;
      justify-content: center;
      opacity: 0;
      transform: scale(0.95) translateY(20px);
      pointer-events: none;
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
      box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.07), 0 0 1px 1px rgba(0, 0, 0, 0.03);
      overflow-y: auto;
    }

    .slide.active {
      opacity: 1;
      transform: scale(1) translateY(0);
      pointer-events: auto;
      z-index: 10;
    }

    /* Slide Content Typography */
    .slide-tag {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.85rem;
      font-weight: 700;
      color: #4f46e5;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 12px;
    }

    h1.slide-title {
      font-size: 2.5rem;
      font-weight: 800;
      line-height: 1.15;
      letter-spacing: -0.03em;
      margin-bottom: 16px;
      color: #0f172a;
      background: none;
      -webkit-text-fill-color: initial;
    }

    h2.slide-subtitle {
      font-size: 1.25rem;
      font-weight: 500;
      color: var(--text-muted);
      margin-bottom: 32px;
      line-height: 1.5;
    }

    /* Grid Layouts */
    .grid-2 {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 24px;
      margin-top: 16px;
    }

    .grid-3 {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 20px;
      margin-top: 16px;
    }

    .grid-4 {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 16px;
      margin-top: 16px;
    }

    /* Card Box */
    .card-box {
      background: #f8fafc;
      border: 1px solid var(--border);
      border-radius: 14px;
      padding: 24px;
      transition: all 0.3s ease;
    }

    .card-box:hover {
      border-color: #818cf8;
      box-shadow: 0 10px 25px -5px rgba(79, 70, 229, 0.08);
      transform: translateY(-2px);
    }

    .card-icon {
      font-size: 2rem;
      margin-bottom: 12px;
    }

    .card-title {
      font-size: 1.15rem;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 8px;
    }

    .card-desc {
      font-size: 0.9rem;
      color: #475569;
      line-height: 1.6;
    }

    /* Custom Badges */
    .badge {
      display: inline-block;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.75rem;
      font-weight: 700;
      margin-bottom: 8px;
    }
    .badge-php { background: #e0e7ff; color: #3730a3; border: 1px solid #c7d2fe; }
    .badge-blue { background: #e0f2fe; color: #0369a1; }
    .badge-green { background: #d1fae5; color: #047857; }
    .badge-purple { background: #f3e8ff; color: #7e22ce; }
    .badge-amber { background: #fef3c7; color: #b45309; }
    .badge-pink { background: #fce7f3; color: #be185d; }

    /* Tables */
    .custom-table {
      width: 100%;
      border-collapse: collapse;
      margin-top: 16px;
      border-radius: 10px;
      overflow: hidden;
      border: 1px solid var(--border);
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.03);
    }

    .custom-table th {
      background: #f1f5f9;
      color: #0f172a;
      padding: 12px 16px;
      font-size: 0.9rem;
      text-align: left;
      font-weight: 700;
      border-bottom: 2px solid var(--border-dark);
    }

    .custom-table td {
      padding: 12px 16px;
      font-size: 0.88rem;
      color: #334155;
      border-bottom: 1px solid var(--border);
      background: #ffffff;
    }

    .custom-table tr:hover td {
      background: #f8fafc;
    }

    /* Code Block (High contrast syntax block) */
    pre {
      background: #0f172a;
      border: 1px solid #1e293b;
      border-radius: 12px;
      padding: 18px;
      overflow-x: auto;
      font-family: 'Fira Code', monospace;
      font-size: 0.88rem;
      line-height: 1.6;
      color: #f8fafc;
      margin-top: 12px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }

    .code-keyword { color: #fb7185; font-weight: 600; }
    .code-class { color: #38bdf8; font-weight: 600; }
    .code-func { color: #c084fc; }
    .code-str { color: #4ade80; }
    .code-var { color: #fde047; }
    .code-num { color: #fb923c; }
    .code-comment { color: #94a3b8; font-style: italic; }

    /* Footer & Controls */
    footer {
      padding: 14px 24px;
      background: rgba(255, 255, 255, 0.92);
      backdrop-filter: blur(12px);
      border-top: 1px solid var(--border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 100;
      box-shadow: 0 -1px 3px rgba(0, 0, 0, 0.03);
    }

    .progress-container {
      flex: 1;
      max-width: 400px;
      height: 6px;
      background: #e2e8f0;
      border-radius: 3px;
      overflow: hidden;
      margin: 0 20px;
    }

    .progress-bar {
      height: 100%;
      width: 0%;
      background: linear-gradient(90deg, #4f46e5, #6366f1);
      transition: width 0.3s ease;
    }

    .nav-buttons {
      display: flex;
      gap: 12px;
    }

    .btn-nav {
      background: var(--primary);
      color: white;
      border: none;
      padding: 8px 18px;
      border-radius: 8px;
      font-weight: 700;
      font-size: 0.9rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: all 0.2s ease;
      box-shadow: 0 2px 4px rgba(79, 70, 229, 0.2);
    }

    .btn-nav:hover {
      background: var(--primary-hover);
      transform: scale(1.02);
    }

    .btn-nav.secondary {
      background: #ffffff;
      border: 1px solid var(--border-dark);
      color: var(--text-main);
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
    }

    .btn-nav.secondary:hover {
      background: #f8fafc;
    }

    .btn-nav:disabled {
      opacity: 0.4;
      cursor: not-allowed;
      transform: none;
    }

    .key-hint {
      font-size: 0.75rem;
      color: var(--text-muted);
      font-family: 'Fira Code', monospace;
    }

    /* Cover Slide */
    .cover-slide {
      text-align: center;
      align-items: center;
      justify-content: center;
    }

    .cover-badge {
      background: #eef2ff;
      border: 1px solid #c7d2fe;
      color: #4338ca;
      padding: 6px 16px;
      border-radius: 30px;
      font-weight: 700;
      font-size: 0.9rem;
      margin-bottom: 20px;
      display: inline-block;
    }

    .avatar-box {
      margin-top: 32px;
      display: flex;
      align-items: center;
      gap: 16px;
      background: #f8fafc;
      padding: 12px 24px;
      border-radius: 50px;
      border: 1px solid var(--border-dark);
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
    }

    .avatar-img {
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: linear-gradient(135deg, #4f46e5, #6366f1);
      color: #ffffff;
      display: flex;
      align-items: center;
      justify-content: center;
      font-weight: 800;
      font-size: 1.2rem;
    }

    .author-info {
      text-align: left;
    }
    .author-name {
      font-weight: 700;
      font-size: 1rem;
      color: #0f172a;
    }
    .author-role {
      font-size: 0.8rem;
      color: var(--text-muted);
    }
  </style>"""

def process_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace <style>...</style> block
    content = re.sub(r'<style>.*?</style>', LIGHT_CSS, content, flags=re.DOTALL)

    # Replace inline dark styles in body
    content = content.replace('background: rgba(15, 23, 42, 0.8);', 'background: #f1f5f9;')
    content = content.replace('background: rgba(15, 23, 42, 0.7);', 'background: #f8fafc;')
    content = content.replace('background: rgba(15, 23, 42, 0.6);', 'background: #f8fafc;')
    content = content.replace('background: rgba(30, 41, 59, 0.8);', 'background: #f1f5f9;')
    content = content.replace('background: rgba(99, 102, 241, 0.2);', 'background: #eef2ff;')
    content = content.replace('background: rgba(16, 185, 129, 0.15);', 'background: #ecfdf5;')
    content = content.replace('background: rgba(14, 165, 233, 0.15);', 'background: #f0f9ff;')
    content = content.replace('color: #c7d2fe;', 'color: #3730a3;')
    content = content.replace('color: #a7f3d0;', 'color: #065f46;')
    content = content.replace('color: #bae6fd;', 'color: #075985;')
    content = content.replace('var(--dark-muted)', 'var(--text-muted)')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated HTML: {filepath}")

def process_md_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace('background-color: #0f172a;', 'background-color: #f8fafc;')
    content = content.replace('color: #f8fafc;', 'color: #0f172a;')
    content = content.replace('color: #818cf8;', 'color: #4f46e5;')
    content = content.replace('color: #94a3b8;', 'color: #475569;')
    content = content.replace('background-color: #1e293b;', 'background-color: #e2e8f0;')
    content = content.replace('color: #ffffff;', 'color: #0f172a;')
    content = content.replace('color: #cbd5e1;', 'color: #334155;')
    content = content.replace('color: #a5b4fc;', 'color: #4338ca;')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated MD: {filepath}")

# Process files
pres_dir = '/Users/mac/code/Perkuliahan/Presentasi'
for filename in os.listdir(pres_dir):
    full_path = os.path.join(pres_dir, filename)
    if filename.endswith('.html'):
        process_html_file(full_path)
    elif filename.endswith('.md'):
        process_md_file(full_path)
