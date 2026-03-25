import os

# Контент страниц
pages = {
    "index.html": {
        "title": "Вихоревка | Сердце Сибири",
        "header": "Вихоревка",
        "content": """
            <section class="hero" data-aos="fade-in">
                <div class="hero-inner">
                    <h1 class="animate__animated animate__backInDown">Вихоревка</h1>
                    <p class="animate__animated animate__fadeInUp animate__delay-1s">Город железных дорог и бескрайней тайги</p>
                    <div class="hero-btns animate__animated animate__fadeInUp animate__delay-2s">
                        <a href="history.html" class="btn-glass">Открыть историю</a>
                        <a href="gallery.html" class="btn-glass secondary">Галерея</a>
                    </div>
                </div>
            </section>
            <div class="container">
                <div class="glass-card" data-aos="fade-up">
                    <h2>Добро пожаловать</h2>
                    <p>Вихоревка — это уникальное сочетание индустриальной мощи и суровой северной красоты. Основанный как ключевой узел БАМа, город продолжает жить в ритме стука колес и шелеста сосен.</p>
                    <img src="https://unsplash.com" class="rounded-img">
                </div>
            </div>
        """
    },
    "history.html": {
        "title": "История города",
        "header": "Наша История",
        "content": """
            <div class="container section">
                <div class="glass-card" data-aos="zoom-in">
                    <h1>Путь сквозь века</h1>
                    <div class="timeline">
                        <div class="step"><strong>1630:</strong> Вихор Савин закладывает имя этим землям.</div>
                        <div class="step"><strong>1947:</strong> Начало великой стройки железной дороги.</div>
                        <div class="step"><strong>1966:</strong> Вихоревка официально становится городом.</div>
                    </div>
                    <p>Каждый кирпич здесь пропитан духом первопроходцев и энтузиазмом строителей магистрали.</p>
                    <a href="index.html" class="btn-glass">На главную</a>
                </div>
            </div>
        """
    },
    "gallery.html": {
        "title": "Галерея Вихоревки",
        "header": "Фотоархив",
        "content": """
            <div class="container section">
                <h1 align="center" data-aos="fade-down">Красота Севера</h1>
                <div class="grid-gallery">
                    <div class="gallery-item" data-aos="flip-left"><img src="https://unsplash.com"></div>
                    <div class="gallery-item" data-aos="flip-up"><img src="https://unsplash.com"></div>
                    <div class="gallery-item" data-aos="flip-right"><img src="https://unsplash.com"></div>
                </div>
            </div>
        """
    }
}

css_content = """
:root {
    --primary: #6366f1; --bg: #f0f2f5; --text: #1e293b; --glass: rgba(255, 255, 255, 0.7);
    --grad: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
}
[data-theme="dark"] {
    --bg: #0f172a; --text: #f8fafc; --glass: rgba(30, 41, 59, 0.7);
}

body { 
    margin: 0; font-family: 'Inter', system-ui; background: var(--bg); color: var(--text); 
    transition: 0.5s cubic-bezier(0.4, 0, 0.2, 1); overflow-x: hidden;
}

.container { max-width: 1100px; margin: 0 auto; padding: 40px 20px; }

/* Навигация */
nav {
    position: sticky; top: 0; background: var(--glass); backdrop-filter: blur(15px);
    z-index: 1000; padding: 15px 0; border-bottom: 1px solid rgba(255,255,255,0.1);
}
.nav-box { display: flex; justify-content: space-between; align-items: center; }
.nav-links a { color: var(--text); text-decoration: none; margin-right: 20px; font-weight: 600; transition: 0.3s; }
.nav-links a:hover { color: var(--primary); transform: translateY(-2px); }

/* Hero секция */
.hero {
    height: 80vh; background: var(--grad); display: flex; align-items: center; justify-content: center;
    color: white; text-align: center; clip-path: ellipse(150% 100% at 50% 0%);
}
.hero h1 { font-size: 5rem; margin: 0; text-shadow: 0 10px 20px rgba(0,0,0,0.2); }

/* Кнопки и карточки */
.btn-glass {
    padding: 12px 30px; border-radius: 50px; background: white; color: var(--primary);
    text-decoration: none; font-weight: bold; transition: 0.3s; display: inline-block;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}
.btn-glass:hover { transform: scale(1.05); box-shadow: 0 8px 25px rgba(0,0,0,0.2); }
.btn-glass.secondary { background: transparent; border: 2px solid white; color: white; margin-left: 15px; }

.glass-card {
    background: var(--glass); backdrop-filter: blur(10px); padding: 40px;
    border-radius: 30px; border: 1px solid rgba(255,255,255,0.2);
    box-shadow: 0 20px 40px rgba(0,0,0,0.1); margin-top: -100px;
}

.rounded-img { width: 100%; border-radius: 20px; margin-top: 20px; transition: 0.5s; }
.rounded-img:hover { transform: scale(1.02); }

/* Сетка галереи */
.grid-gallery { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }
.gallery-item img { width: 100%; height: 250px; object-fit: cover; border-radius: 20px; transition: 0.3s; }
.gallery-item:hover img { transform: rotate(2deg) scale(1.05); }

/* Переключатель темы */
#theme-btn {
    border: none; background: var(--grad); color: white; padding: 10px 20px;
    border-radius: 50px; cursor: pointer; font-weight: bold;
}
"""

script_content = """
const btn = document.getElementById('theme-btn');
const body = document.documentElement;

btn.onclick = () => {
    const isDark = body.getAttribute('data-theme') === 'dark';
    const newTheme = isDark ? 'light' : 'dark';
    body.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    btn.innerHTML = newTheme === 'dark' ? '☀️ Свет' : '🌙 Тьма';
};

// Загрузка темы
const saved = localStorage.getItem('theme') || 'light';
body.setAttribute('data-theme', saved);
btn.innerHTML = saved === 'dark' ? '☀️ Свет' : '🌙 Тьма';

// Инициализация AOS (анимация при скролле)
AOS.init({ duration: 1000, once: true });
"""


def generate():
    with open("style.css", "w", encoding="utf-8") as f: f.write(css_content)

    for name, data in pages.items():
        html = f"""
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <title>{data['title']}</title>
            <link rel="stylesheet" href="style.css">
            <link rel="stylesheet" href="https://cloudflare.com"/>
            <link rel="stylesheet" href="https://unpkg.com" />
        </head>
        <body>
            <nav>
                <div class="container nav-box" style="padding:0 20px">
                    <div class="nav-links">
                        <a href="index.html">Главная</a>
                        <a href="history.html">История</a>
                        <a href="gallery.html">Галерея</a>
                    </div>
                    <button id="theme-btn">🌙 Тьма</button>
                </div>
            </nav>
            {data['content']}
            <script src="https://unpkg.com"></script>
            <script>{script_content}</script>
        </body>
        </html>
        """
        with open(name, "w", encoding="utf-8") as f: f.write(html)
    print("✨ Сайт Вихоревки создан с премиум дизайном!")


if __name__ == "__main__": generate()
