import os
import re

CLEAN_SCRIPT = """  <script>
    const slides = document.querySelectorAll('.slide');
    const slideIndicator = document.getElementById('slideIndicator');
    const progressBar = document.getElementById('progressBar');
    const prevBtn = document.getElementById('prevBtn');
    const nextBtn = document.getElementById('nextBtn');

    let currentSlide = 0;
    const totalSlides = slides.length;

    // Presentation Timer (Global Scope - Persists across slide transitions)
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
      slides.forEach((slide, index) => {
        slide.classList.remove('active');
        if (index === currentSlide) {
          slide.classList.add('active');
        }
      });

      // Update indicator & progress
      slideIndicator.textContent = `SLIDE ${currentSlide + 1} / ${totalSlides}`;
      const progressPercent = ((currentSlide + 1) / totalSlides) * 100;
      progressBar.style.width = `${progressPercent}%`;

      // Update button states
      prevBtn.disabled = currentSlide === 0;
      nextBtn.disabled = currentSlide === totalSlides - 1;
      nextBtn.textContent = (currentSlide === totalSlides - 1) ? 'Selesai 🏁' : 'Selanjutnya ▶';
    }

    function nextSlide() {
      if (currentSlide < totalSlides - 1) {
        currentSlide++;
        updateSlide();
      }
    }

    function prevSlide() {
      if (currentSlide > 0) {
        currentSlide--;
        updateSlide();
      }
    }

    function toggleFullscreen() {
      if (!document.fullscreenElement) {
        document.documentElement.requestFullscreen().catch(err => {
          alert(`Error fullscreen: ${err.message}`);
        });
      } else {
        if (document.exitFullscreen) {
          document.exitFullscreen();
        }
      }
    }

    // Keyboard navigation
    document.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
        e.preventDefault();
        nextSlide();
      } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
        e.preventDefault();
        prevSlide();
      } else if (e.key === 'f' || e.key === 'F') {
        e.preventDefault();
        toggleFullscreen();
      } else if (e.key === 'Home') {
        currentSlide = 0;
        updateSlide();
      } else if (e.key === 'End') {
        currentSlide = totalSlides - 1;
        updateSlide();
      }
    });

    // Touch navigation for mobile/tablet
    let touchStartX = 0;
    let touchEndX = 0;

    document.addEventListener('touchstart', e => {
      touchStartX = e.changedTouches[0].screenX;
    });

    document.addEventListener('touchend', e => {
      touchEndX = e.changedTouches[0].screenX;
      if (touchStartX - touchEndX > 50) {
        nextSlide();
      }
      if (touchEndX - touchStartX > 50) {
        prevSlide();
      }
    });

    // Initial render & timer start
    updateSlide();
    startTimer();
  </script>"""

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace <script>...</script>
    content = re.sub(r'<script>.*?</script>', CLEAN_SCRIPT, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed script in: {filepath}")

pres_dir = '/Users/mac/code/Perkuliahan/Presentasi'
for filename in os.listdir(pres_dir):
    if filename.endswith('.html'):
        fix_file(os.path.join(pres_dir, filename))
