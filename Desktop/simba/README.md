# Second Hand Commodities Website

A Flask-based web application for second-hand commodities marketplace in Kiambu and Nairobi areas.

## Features

- Users can post items for sale.
- Admin (you) approves/rejects posts.
- Buyers view approved items and contact admin for purchases.
- Admin acts as intermediary between buyers and sellers.

## Setup

1. Install Python 3.12 from https://www.python.org/downloads/ or Microsoft Store.
2. Install Flask: `pip install flask`
3. Run the app: `python app.py`
4. Open http://127.0.0.1:5000 in your browser.

## Usage

- Home: View approved items.
- Post Item: Submit a new item (requires admin approval).
- Admin: Approve or reject pending items.

Database: marketplace.db (SQLite) will be created automatically.