# 💰 crypto_bot

> Get cryptocurrency prices on demand

A lightweight Telegram bot that scrapes cryptocurrency prices from CoinMarketCap in real-time.

## ✨ Features

- **Real-time pricing** — Fetch current crypto prices instantly
- **Easy lookup** — Send coin name or symbol to get price
- **Web scraping** — Uses CoinMarketCap for price data
- **Quick response** — Sub-second price lookups
- **Predefined buttons** — Quick access to Bitcoin, Ethereum, Dogecoin

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- Telegram Bot Token

### Installation

```bash
git clone https://github.com/w1cee/crypto_bot.git
cd crypto_bot
pip install -r requirements.txt
```

### Setup

1. Replace the bot token in `main.py` (line 8):

```python
TOKEN = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(TOKEN)
```

2. Run the bot:

```bash
python main.py
```

## 💻 How to Use

1. Start the bot: `/start`
2. Choose from predefined buttons or send any cryptocurrency name
3. Get the price instantly

### Example

```
User: /start
Bot: [Buttons: Bitcoin | Ethereum | Dogecoin]
     Hello, send me the name of any cryptocurrency and I will send you the price!

User: bitcoin
Bot: 1 bitcoin = $45,230

User: ethereum
Bot: 1 ethereum = $2,480
```

## 🛠️ Tech Stack

- **Language**: Python 3.7+
- **Bot Framework**: pyTelegramBotAPI (telebot)
- **Web Scraping**: BeautifulSoup4, requests
- **Parsing**: Regular expressions (regex)
- **Data Source**: CoinMarketCap

## 📚 Code Structure

The bot has two main handlers:

### 1. Start Handler (`/start`)
```python
@bot.message_handler(commands=['start'])
def start(message):
    buttons = telebot.types.ReplyKeyboardMarkup(True)
    buttons.row('Bitcoin', 'Ethereum', 'Dogecoin')
    bot.send_message(message.chat.id, '...', reply_markup=buttons)
```

Creates a keyboard with quick access to popular cryptocurrencies.

### 2. Price Handler (Coin Lookup)
```python
@bot.message_handler(content_types=['text'])
def get_price(message):
    user_input = message.text  # e.g., "bitcoin"
    name_of_crypto = user_input.replace(' ', '-')  # Convert to URL format
    
    url = f'https://coinmarketcap.com/currencies/{name_of_crypto.lower()}/'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        block = soup.find_all('div', class_='priceValue')
        element = str(block)
        price = re.findall(r'[$][\d]*[,]?[\d]*[.]?[\d]*', element)
        price = price.pop(0)
        bot.send_message(message.chat.id, f'1 {name_of_crypto} = {price}')
```

## 🔌 Data Source: CoinMarketCap

The bot scrapes price data from CoinMarketCap:

```python
# URL format
url = f'https://coinmarketcap.com/currencies/{coin_name.lower()}/'

# Example URLs
https://coinmarketcap.com/currencies/bitcoin/
https://coinmarketcap.com/currencies/ethereum/
https://coinmarketcap.com/currencies/dogecoin/
```

### Web Scraping Process

1. **Fetch page**: `requests.get(url)`
2. **Parse HTML**: `BeautifulSoup(response.text, 'lxml')`
3. **Find price element**: `soup.find_all('div', class_='priceValue')`
4. **Extract price with regex**: `re.findall(r'[$][\d]*[,]?[\d]*[.]?[\d]*', element)`
5. **Send to user**: `bot.send_message(chat_id, f'1 {coin} = {price}')`

## 📊 Price Format

The bot extracts prices in the format:
- `$XX,XXX.XX` — Full price with commas and decimals
- Examples:
  - `$45,230.50`
  - `$2,480.75`
  - `$0.08`

## 🐛 Troubleshooting

### Bot not responding
- Verify bot token is correct
- Check internet connection
- Ensure Telegram Bot API is accessible

### Coin not found (404 error)
```
User sends: some_random_coin
Bot: Are you sure this cryptocurrency exists?
```
- Verify cryptocurrency name is correct
- Try with full name instead of symbol
- Check if coin exists on CoinMarketCap

### Website errors
```
Bot: Something went wrong..
```
- CoinMarketCap website might be down
- HTML structure might have changed (requires code update)
- Check internet connection

### Parser errors
- If prices stop showing, CoinMarketCap HTML structure may have changed
- May need to update the CSS class name: `priceValue`
- Update regex pattern if price format changed

## 📝 Requirements File

```
pyTelegramBotAPI
beautifulsoup4
requests
lxml
```

## 🔄 Workflow

```
User sends coin name (e.g., "bitcoin")
        ↓
Bot replaces spaces with hyphens ("bitcoin")
        ↓
Construct CoinMarketCap URL
        ↓
Fetch webpage with requests library
        ↓
Parse HTML with BeautifulSoup
        ↓
Find all price divs (class="priceValue")
        ↓
Extract price with regex pattern: [$][\d]*[,]?[\d]*[.]?[\d]*
        ↓
Send formatted response: "1 bitcoin = $45,230"
        ↓
Bot waits for next message
```

## ⚠️ Important Notes

- **Web Scraping**: This bot scrapes CoinMarketCap. Check their Terms of Service.
- **Rate Limiting**: Avoid sending too many requests too quickly
- **HTML Changes**: If CoinMarketCap updates their website structure, the parser may break
- **Alternative**: Consider using a proper cryptocurrency API (CoinGecko, Binance) for production

## 📄 License

MIT License - See LICENSE file

## 👨‍💻 Author

**w1cee** — Backend Developer | Systems Builder  
💬 [GitHub](https://github.com/w1cee)

---

**Building things that work while I sleep** 📈
