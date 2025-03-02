<div align="center">

# Chimera Userbot

<p>
  <img src="https://img.shields.io/badge/Python-3.7+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License">
  <img src="https://img.shields.io/badge/Telegram-Userbot-blue.svg" alt="Telegram Userbot">
</p>

**English** | [Русский](README_RU.md)

</div>

## 📌 About

Chimera is a powerful and flexible Telegram userbot developed in Python using the Pyrogram library. It allows you to automate various actions in Telegram and extend functionality through modules.

## ✨ Features

- Modular architecture for easy functionality extension
- Simple installation and configuration
- Ability to install third-party modules from GitHub
- Convenient management through Telegram commands
- Secure credential storage
- Hot module reloading
- Performance monitoring
- Multi-language support

## 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/Ladvix/Chimera.git
cd Chimera

# Install dependencies
pip install -r requirements.txt

# Run the userbot
python main.py
```

## 📚 Usage

After launching and authorizing, you can use the following commands in Telegram:

- `.start` - Start the bot and display a welcome message
- `.help { module name }` - List available bot commands
- `.modules` - List installed modules
- `.install { github link } as { module name }` - Install a module from GitHub
- `.uninstall { module name }` - Remove a selected module

## 🛠️ Configuration

Chimera can be configured through the `config.py` file. You can customize various settings such as:

- API credentials
- Proxy settings
- Module behavior
- UI preferences

## 🔍 Troubleshooting

If you encounter any issues:

1. Check the logs for error messages
2. Ensure all dependencies are correctly installed
3. Verify your API credentials
4. Join our Telegram support channel for assistance

## 📄 License

Distributed under [the MIT License](https://github.com/Ladvix/Chimera/blob/main/LICENSE).

## 🔗 Links

- <a href="https://t.me/chimera_ubot"><img src="https://img.shields.io/badge/Telegram-2CA5E0?style=flat&logo=telegram&logoColor=white" alt="Telegram Channel"></a>