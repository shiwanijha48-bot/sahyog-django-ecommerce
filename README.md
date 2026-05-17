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
## ✅ Current Modules

| Module | Status |
|---|---|
| User Authentication | ✅ Completed |
| Product Management | ✅ Completed |
| Cart System | ✅ Completed |
| Checkout System | ✅ Completed |
| Order Tracking | ✅ Completed |
| Artisan Application System | ✅ Completed |
| Admin Approval Workflow | ✅ Completed |
| Artisan Dashboard | ✅ Completed |
| Responsive UI | ✅ Completed |
| Media Upload System | ✅ Completed |

---------------------------------------

## 🔐 Demo Credentials

### Admin Login
Username: sahyog.admin
Password: sahyog1234

### Artisan Login
Username: Arif Hussain
Password: a1234

### User
Username: Anu
Password: a1234

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

## 🔄 Application Workflow

1. User registers/login
2. User browses products
3. User adds items to cart
4. User places order via checkout
5. Orders stored in database
6. Users can track orders

### Artisan Workflow
1. User applies as artisan
2. Admin reviews application
3. Approved application converts into Artisan
4. Artisan gets dashboard access
5. Artisan uploads products
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

---------------------------------------
## 🚀 NEW UPDATES (Latest Features Added)
## 🧑‍🎨 Artisan Ecosystem (Major Upgrade)

## Sahyog now includes a complete artisan onboarding system:

* 📝 Artisan Application System (users can apply as artisans)
* ✅ Admin Approval Workflow
* 🔄 Approved applications automatically convert into Artisans
* ❌ Rejected applications handled separately
* 👤 Artisan linked directly with user accounts
* 🛠️ Admin Enhancements

---------------------------------------

## The admin panel has been upgraded into a full control system:

* 📋 Artisan application review dashboard
* ✔️ Approve / Reject artisan requests
* 🧾 Product management improvements
* 👨‍🎨 Artisan Dashboard (New Module)

---------------------------------------

## Each approved artisan gets their own dashboard:

* 📤 Add new products
* 🧩 Backend Improvements
* ⚙️ Added context_processors.py for global data handling
* 🧾 Added forms.py for structured form handling
* 🗂️ New migrations for:
** Artisan applications
** User linking system

---------------------------------------

## Order system
* 🔄 Improved model relationships between User, Artisan, Products, Orders
* 🛒 Checkout System (New)
* 🧾 Dedicated checkout page added
* 📦 Order placement system introduced
* 🔄 Cart → Order conversion flow implemented
* 🎨 UI Improvements
* 📱 Better structured templates:
-artisan_dashboard.html
-admin_dashboard.html
-add_product.html
-checkout.html

---------------------------------------

## 🎯 Improved user experience flow across cart → checkout → order
* 🔮 Upcoming Enhancements
* 💳 Payment Gateway Integration (Razorpay)
* 📬 Email notifications for orders & approvals
* 📊 Advanced analytics dashboard
* 🔍 Product search & filtering system
* ⭐ Ratings & reviews system
  
---------------------------------------

 ## 👩‍💻 Developer

Developed with dedication by **Shiwani Jha**

---------------------------------------
