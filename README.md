# Chimera Userbot

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Telegram-Userbot-blue.svg" alt="Telegram Userbot">
</p>

## 📌 О проекте

Chimera - это мощный и гибкий юзербот для Telegram, разработанный на Python с использованием библиотеки Pyrogram. Он позволяет автоматизировать различные действия в Telegram и расширять функциональность с помощью модулей.

## ✨ Особенности

- 🚀 Модульная архитектура для легкого расширения функциональности
- 🔌 Простая установка и настройка
- 📦 Возможность установки сторонних модулей из GitHub
- 🛠️ Удобное управление через команды в Telegram
- 🔒 Безопасное хранение учетных данных

## 🔧 Установка

```bash
# Клонирование репозитория
git clone https://github.com/yourusername/Chimera.git
cd Chimera

# Установка зависимостей
pip install -r requirements.txt

# Запуск юзербота
python main.py
```

## 📚 Использование

После запуска и авторизации, вы можете использовать следующие команды в Telegram:

- `.start` - Запуск бота и отображение приветственного сообщения
- `.help [название модуля]` - Список доступных команд бота
- `.modules` - Список установленных модулей
- `.install {ссылка github} as {название модуля}` - Установка модуля с GitHub
- `.uninstall {название модуля}` - Удаление выбранного модуля

## 🔄 Разработка модулей

Вы можете создавать собственные модули для расширения функциональности Chimera. Модули должны следовать определенной структуре:

```
module_name/
├── main.py         # Основной файл модуля с функцией launch
├── requirements.txt # Зависимости модуля
└── README.md       # Документация модуля
```

## 📄 Лицензия

Распространяется под лицензией MIT. См. файл `LICENSE` для получения дополнительной информации.

## 🔗 Ссылки

- [Telegram канал](https://t.me/chimera_ubot)
