# Sahyog – Cultural E-commerce Platform

Sahyog is a Django-based e-commerce web application designed to promote **Indian handicrafts and cultural products** globally.
The platform connects rural artisans with customers, helping preserve traditional craftsmanship while supporting livelihoods.

---------------------------------------

## 🌟 Features

* 🏠 Beautiful homepage with intro + product slider
* 🛍️ Product listing page
* 🔍 Product detail page (full description, image, price)
* 🛒 Add to Cart functionality
* ➕ Increase / ➖ Decrease quantity
* ❌ Remove items from cart
* ⚡ Buy Now option
* 🔔 Toast message (item added to cart)
* 👤 User Authentication (Register / Login / Logout)
* 📱 Responsive UI

---------------------------------------

## 🛠️ Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLite
* **Media Handling:** Pillow

---------------------------------------

## 📂 Project Structure

```
Sahyog/
│── core/              # Main project settings
│── store/             # App (products, cart, views)
│── templates/         # HTML templates
│── static/            # CSS files
│── media/             # Uploaded product images
│── manage.py
```

---------------------------------------

## ⚙️ Installation & Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/sahyog.git
cd sahyog
```

2. Create virtual environment:

```bash
python -m venv env
env\Scripts\activate   # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create superuser:

```bash
python manage.py createsuperuser
```

6. Run server:

```bash
python manage.py runserver
```

7. Open in browser:

```
http://127.0.0.1:8000/
```

---------------------------------------

## 🔑 Admin Panel

Access admin panel at:

```
http://127.0.0.1:8000/admin/
```

Use it to:

* Add products
* Upload images
* Manage data

---------------------------------------

## 📸 Screenshots (Add Later)

* Homepage
* Products Page
* Product Detail Page
* Cart Page

---------------------------------------

## 🎯 Future Improvements

* 💳 Payment integration (Razorpay/Stripe)
* 📦 Order management system
* ⭐ Product reviews & ratings
* 🔍 Search & filter functionality
* 📊 Admin dashboard

---------------------------------------

## 🤝 Contribution

Contributions are welcome!
Feel free to fork this repo and submit a pull request.

---------------------------------------

## 📧 Contact

* Email: sahyog.admin@gmail.com
* Location: Bhopal, India

---------------------------------------

## ❤️ Vision

Sahyog aims to empower rural artisans by giving them a digital platform to showcase their work and reach a global audience.
Every purchase supports culture, tradition, and livelihoods.
~ Shiwani Jha

---------------------------------------

⭐ If you like this project, give it a star!
