import os
import re

TIMER_CSS = """
    .timer-badge {
      background: #f1f5f9;
      border: 1px solid var(--border-dark);
      color: #0f172a;
      padding: 4px 12px;
      border-radius: 20px;
      font-size: 0.82rem;
      font-weight: 700;
      font-family: 'Fira Code', monospace;
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
"""

TIMER_HTML = '<span class="timer-badge" id="presentationTimer" title="Timer Presentasi (Klik: Jeda/Lanjut, Dobel Klik: Reset)">⏱️ 00:00</span>\n      <span class="slide-badge"'

TIMER_JS = """
    // Presentation Timer
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
          timerElement.title = "Timer Dijeda (Klik untuk Lanjut, Dobel Klik untuk Reset)";
        } else {
          timerElement.classList.remove('paused');
          timerElement.title = "Timer Berjalan (Klik untuk Jeda, Dobel Klik untuk Reset)";
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

    startTimer();
"""

def update_presentation_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Add timer CSS if not present
    if '.timer-badge' not in content:
        content = content.replace('.slide-badge {', TIMER_CSS + '\n    .slide-badge {')

    # 2. Add timer HTML in header controls if not present
    if 'id="presentationTimer"' not in content:
        content = content.replace('<span class="slide-badge"', TIMER_HTML)

    # 3. Add timer JS if not present
    if 'presentationTimer' not in content or 'let timerSeconds' not in content:
        content = content.replace('updateSlide();', 'updateSlide();\n' + TIMER_JS)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Added Timer to: {filepath}")

# Process files
pres_dir = '/Users/mac/code/Perkuliahan/Presentasi'
for filename in os.listdir(pres_dir):
    if filename.endswith('.html'):
        update_presentation_file(os.path.join(pres_dir, filename))
