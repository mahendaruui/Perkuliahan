import os
import re

LIGHT_ALGO_CSS = """  <style>
    :root {
      --bg-page: #f8fafc;
      --card-bg: #ffffff;
      --card-subtle: #f8fafc;
      --card-border: #e2e8f0;
      --card-border-strong: #cbd5e1;
      --primary: #0284c7; /* Sky 600 */
      --primary-hover: #0369a1;
      --primary-light: #e0f2fe;
      --secondary: #6366f1; /* Indigo 500 */
      --accent-purple: #9333ea;
      --accent-emerald: #059669;
      --accent-amber: #d97706;
      --accent-rose: #e11d48;
      --text-main: #0f172a;
      --text-muted: #475569;
      --font-code: 'Fira Code', 'JetBrains Mono', monospace;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
      background: var(--bg-page);
      color: var(--text-main);
      overflow: hidden;
      height: 100vh;
      width: 100vw;
      display: flex;
      flex-direction: column;
      user-select: none;
    }

    header {
      padding: 12px 28px;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(16px);
      border-bottom: 1px solid var(--card-border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 100;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
    }

    .brand { display: flex; align-items: center; gap: 12px; }
    .brand-logo { height: 32px; width: auto; border-radius: 6px; }
    .brand-text { font-size: 0.95rem; font-weight: 800; letter-spacing: -0.02em; color: #0f172a; }
    .brand-text span { color: var(--primary); }
    .brand-sub { font-size: 0.72rem; color: var(--text-muted); font-weight: 500; }

    .header-controls { display: flex; align-items: center; gap: 10px; }
    
    .timer-badge {
      background: #f1f5f9;
      border: 1px solid var(--card-border-strong);
      color: #0f172a;
      padding: 5px 12px;
      border-radius: 20px;
      font-size: 0.82rem;
      font-weight: 700;
      font-family: var(--font-code);
      display: inline-flex;
      align-items: center;
      gap: 6px;
      cursor: pointer;
      user-select: none;
      transition: all 0.2s ease;
    }
    .timer-badge:hover {
      background: #e2e8f0;
      border-color: #94a3b8;
    }
    .timer-badge.paused {
      color: #e11d48;
      border-color: #fda4af;
      background: #fff1f2;
    }

    .btn-icon {
      background: #ffffff;
      border: 1px solid var(--card-border-strong);
      color: var(--text-main);
      padding: 6px 14px;
      border-radius: 8px;
      cursor: pointer;
      font-size: 0.82rem;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: all 0.2s cubic-bezier(0.16, 1, 0.3, 1);
      font-family: inherit;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
    }
    .btn-icon:hover {
      background: #f1f5f9;
      border-color: #94a3b8;
    }

    #slide-viewport {
      flex: 1;
      position: relative;
      overflow: hidden;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 20px 28px;
    }

    .slide {
      position: absolute;
      width: min(1140px, 94vw);
      height: min(640px, 84vh);
      background: #ffffff;
      border-radius: 24px;
      border: 1px solid var(--card-border);
      box-shadow: 0 20px 40px -15px rgba(0, 0, 0, 0.07), 0 0 1px 1px rgba(0, 0, 0, 0.03);
      padding: 36px 44px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      opacity: 0;
      transform: translateY(20px) scale(0.98);
      pointer-events: none;
      transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .slide.active {
      opacity: 1;
      transform: translateY(0) scale(1);
      pointer-events: auto;
      z-index: 10;
    }

    .slide.prev {
      opacity: 0;
      transform: translateY(-20px) scale(0.98);
    }

    .slide-tag {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      font-size: 0.75rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      padding: 4px 12px;
      border-radius: 99px;
      background: #e0f2fe;
      border: 1px solid #bae6fd;
      color: #0369a1;
      margin-bottom: 8px;
    }

    .slide-title {
      font-size: 1.85rem;
      font-weight: 800;
      letter-spacing: -0.03em;
      color: #0f172a;
      line-height: 1.25;
      margin-bottom: 4px;
    }

    .slide-subtitle {
      font-size: 0.95rem;
      color: var(--text-muted);
      font-weight: 500;
      margin-bottom: 16px;
    }

    .slide-body {
      flex: 1;
      overflow-y: auto;
      padding-right: 6px;
    }
    .slide-body::-webkit-scrollbar { width: 5px; }
    .slide-body::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }

    footer {
      padding: 12px 28px;
      background: rgba(255, 255, 255, 0.94);
      backdrop-filter: blur(16px);
      border-top: 1px solid var(--card-border);
      display: flex;
      justify-content: space-between;
      align-items: center;
      z-index: 100;
      box-shadow: 0 -1px 3px rgba(0, 0, 0, 0.03);
    }

    .progress-track {
      flex: 1;
      max-width: 440px;
      height: 6px;
      background: #e2e8f0;
      border-radius: 99px;
      overflow: hidden;
      margin: 0 20px;
    }

    .progress-fill {
      height: 100%;
      background: linear-gradient(90deg, #0284c7 0%, #6366f1 50%, #9333ea 100%);
      width: 0%;
      border-radius: 99px;
      transition: width 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .nav-btn-group { display: flex; align-items: center; gap: 8px; }
    .btn-nav {
      background: #ffffff;
      border: 1px solid var(--card-border-strong);
      color: var(--text-main);
      width: 36px;
      height: 36px;
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-weight: 700;
      transition: all 0.2s;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04);
    }
    .btn-nav:hover:not(:disabled) {
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
    }
    .btn-nav:disabled { opacity: 0.35; cursor: not-allowed; }

    .slide-counter {
      font-size: 0.85rem;
      font-weight: 700;
      color: #334155;
      min-width: 70px;
      text-align: center;
      font-family: var(--font-code);
      background: #f1f5f9;
      padding: 4px 10px;
      border-radius: 20px;
      border: 1px solid var(--card-border);
    }

    .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
    .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; }
    .grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; }

    .card {
      background: #f8fafc;
      border: 1px solid var(--card-border);
      border-radius: 14px;
      padding: 16px;
      position: relative;
      overflow: hidden;
      transition: all 0.2s ease;
    }
    .card:hover {
      box-shadow: 0 8px 20px -4px rgba(0, 0, 0, 0.06);
      transform: translateY(-2px);
    }
    .card-cyan { border-left: 4px solid var(--primary); background: #f0f9ff; }
    .card-emerald { border-left: 4px solid var(--accent-emerald); background: #ecfdf5; }
    .card-amber { border-left: 4px solid var(--accent-amber); background: #fffbeb; }
    .card-purple { border-left: 4px solid var(--accent-purple); background: #faf5ff; }
    .card-rose { border-left: 4px solid var(--accent-rose); background: #fff1f2; }

    .card h4 { font-size: 0.95rem; font-weight: 700; margin-bottom: 6px; color: #0f172a; display: flex; align-items: center; gap: 6px; }
    .card p, .card li { font-size: 0.84rem; color: #334155; line-height: 1.55; }

    .quote-box {
      background: #eef2ff;
      border: 1px solid #c7d2fe;
      border-radius: 14px;
      padding: 14px 18px;
      margin-top: 10px;
    }
    .quote-title { font-size: 0.75rem; font-weight: 800; text-transform: uppercase; color: #4338ca; letter-spacing: 0.08em; margin-bottom: 4px; }
    .quote-text { font-size: 0.85rem; color: #1e1b4b; font-style: italic; line-height: 1.5; }
    .quote-author { font-size: 0.75rem; color: #6366f1; margin-top: 4px; text-align: right; font-weight: 600; }

    pre {
      background: #0f172a;
      color: #38bdf8;
      border: 1px solid #1e293b;
      padding: 14px;
      border-radius: 12px;
      font-family: var(--font-code);
      font-size: 0.82rem;
      line-height: 1.55;
      overflow-x: auto;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
    }

    table.slide-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.84rem;
      margin-top: 6px;
      border-radius: 10px;
      overflow: hidden;
      border: 1px solid var(--card-border);
    }
    table.slide-table th, table.slide-table td {
      padding: 10px 14px;
      border: 1px solid var(--card-border);
      text-align: left;
    }
    table.slide-table th {
      background: #f1f5f9;
      font-weight: 700;
      color: #0f172a;
      border-bottom: 2px solid var(--card-border-strong);
    }
    table.slide-table td {
      color: #334155;
      background: #ffffff;
    }
    table.slide-table tr:hover td {
      background: #f8fafc;
    }

    .hero-slide { text-align: center; display: flex; flex-direction: column; justify-content: center; align-items: center; height: 100%; }
    .hero-title { font-size: 2.4rem; font-weight: 800; letter-spacing: -0.03em; color: #0f172a; margin-bottom: 12px; line-height: 1.2; }
    .hero-title span { color: var(--primary); }
    .hero-meta { display: flex; gap: 12px; margin-top: 24px; flex-wrap: wrap; justify-content: center; }
    .hero-pill { background: #f1f5f9; border: 1px solid var(--card-border-strong); padding: 8px 16px; border-radius: 99px; font-size: 0.84rem; font-weight: 600; color: #334155; box-shadow: 0 1px 2px rgba(0, 0, 0, 0.04); }
  </style>"""

CLEAN_ALGO_SCRIPT = """  <script>
    let currentSlide = 0;
    const slides = document.querySelectorAll('.slide');
    const totalSlides = slides.length;
    const slideNum = document.getElementById('slide-num');
    const progressBar = document.getElementById('progress-bar');
    const btnPrev = document.getElementById('btn-prev');
    const btnNext = document.getElementById('btn-next');

    // Presentation Timer (Global Scope - Continuous)
    let timerSeconds = 0;
    let timerInterval = null;
    let timerRunning = true;
    const timerElement = document.getElementById('presentationTimer');

    function formatTime(totalSec) {
      const mins = Math.floor(totalSec / 60);
      const secs = totalSec % 60;
      return `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
    }

    function startTimer() {
      if (timerInterval) clearInterval(timerInterval);
      timerInterval = setInterval(() => {
        if (timerRunning) {
          timerSeconds++;
          if (timerElement) {
            timerElement.textContent = `⏱️ ${formatTime(timerSeconds)}`;
          }
        }
      }, 1000);
    }

    function toggleTimer() {
      timerRunning = !timerRunning;
      if (timerElement) {
        if (!timerRunning) {
          timerElement.classList.add('paused');
          timerElement.title = "Timer Dijeda (Klik: Lanjut, Dobel Klik: Reset)";
        } else {
          timerElement.classList.remove('paused');
          timerElement.title = "Timer Berjalan (Klik: Jeda, Dobel Klik: Reset)";
        }
      }
    }

    function resetTimer() {
      timerSeconds = 0;
      timerRunning = true;
      if (timerElement) {
        timerElement.classList.remove('paused');
        timerElement.textContent = `⏱️ 00:00`;
      }
    }

    if (timerElement) {
      timerElement.addEventListener('click', toggleTimer);
      timerElement.addEventListener('dblclick', resetTimer);
    }

    function updateSlide() {
      slides.forEach((s, idx) => {
        s.classList.remove('active', 'prev');
        if (idx === currentSlide) {
          s.classList.add('active');
        } else if (idx < currentSlide) {
          s.classList.add('prev');
        }
      });

      slideNum.textContent = (currentSlide + 1) + ' / ' + totalSlides;
      progressBar.style.width = (((currentSlide + 1) / totalSlides) * 100) + '%';
      btnPrev.disabled = currentSlide === 0;
      btnNext.disabled = currentSlide === totalSlides - 1;
    }

    function nextSlide() { if (currentSlide < totalSlides - 1) { currentSlide++; updateSlide(); } }
    function prevSlide() { if (currentSlide > 0) { currentSlide--; updateSlide(); } }

    function toggleFullScreen() {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(err => console.error(err));
      } else {
        if (document.exitFullscreen) document.exitFullscreen();
      }
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') nextSlide();
      else if (e.key === 'ArrowLeft' || e.key === 'PageUp') prevSlide();
      else if (e.key === 'f' || e.key === 'F') toggleFullScreen();
      else if (e.key === 'Home') { currentSlide = 0; updateSlide(); }
      else if (e.key === 'End') { currentSlide = totalSlides - 1; updateSlide(); }
    });

    // Touch Navigation
    let touchStartX = 0;
    let touchEndX = 0;
    document.addEventListener('touchstart', e => { touchStartX = e.changedTouches[0].screenX; });
    document.addEventListener('touchend', e => {
      touchEndX = e.changedTouches[0].screenX;
      if (touchStartX - touchEndX > 50) nextSlide();
      if (touchEndX - touchStartX > 50) prevSlide();
    });

    updateSlide();
    startTimer();
  </script>"""

def process_algo_presentation(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace <style> block
    content = re.sub(r'<style>.*?</style>', LIGHT_ALGO_CSS, content, flags=re.DOTALL)

    # Add timer in header if missing
    if 'id="presentationTimer"' not in content:
        content = content.replace('<div class="header-controls">', '<div class="header-controls">\n      <span class="timer-badge" id="presentationTimer" title="Timer Presentasi (Klik: Jeda/Lanjut, Dobel Klik: Reset)">⏱️ 00:00</span>')

    # Replace <script> block
    content = re.sub(r'<script>.*?</script>', CLEAN_ALGO_SCRIPT, content, flags=re.DOTALL)

    # Polish inline dark elements
    content = content.replace('color: #ffffff;', 'color: #0f172a;')
    content = content.replace('color: #94a3b8;', 'color: #475569;')
    content = content.replace('color: #cbd5e1;', 'color: #334155;')
    content = content.replace('color: #e2e8f0;', 'color: #1e293b;')
    content = content.replace('background: #090d16;', 'background: #0f172a;')
    content = content.replace('background: rgba(30, 41, 59, 0.8);', 'background: #f1f5f9;')
    content = content.replace('background: rgba(30,41,59,0.8);', 'background: #f1f5f9;')
    content = content.replace('border: 1px solid var(--card-border);', 'border: 1px solid var(--card-border-strong);')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Upgraded Algoritma slide to Light Mode: {filepath}")

# Update all algoritma slides in docs/public/presentasi/
pub_dir = '/Users/mac/code/Perkuliahan/docs/public/presentasi'
for filename in os.listdir(pub_dir):
    if 'algoritma' in filename and filename.endswith('.html'):
        process_algo_presentation(os.path.join(pub_dir, filename))
