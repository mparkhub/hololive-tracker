# Holostrider

Holostrider is a Django web app that displays upcoming and ongoing livestreams from Hololive talents.

---

## Features

- Displays live and scheduled livestreams from Hololive talents (upcoming)
- Filtering by talent (upcoming)

---

## Installation and Setup

1. Clone the repository:
```bash
git clone https://github.com/mparkhub/hololive-tracker.git
cd hololive-tracker
```
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Run migrations:
```bash
python manage.py migrate
```
5. Start the server:
```bash
python manage.py runserver
```
6. Navigate to the server:

Visit http://127.0.0.1:8000/ in your browser.