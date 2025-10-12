🏠 Affordable Housing Tracker

A Django-powered web app to help users discover affordable housing options with ease. Built for transparency, accessibility, and real-world impact.
![sample image](./portfolio.jpg)  
---

## 🔍 Features

- 🗺️ **Interactive Listings**: Browse housing options with images and location details.
- 📦 **SQLite Backend**: Lightweight database for quick setup and local testing.
- 🛠️ **Admin Dashboard**: Manage listings and media through Django’s built-in admin panel.
- 📁 **Modular Structure**: Clean separation of concerns for easy scaling and maintenance.

---

## 🚀 Tech Stack

| Layer        | Tools Used                          |
|--------------|-------------------------------------|
| Backend      | Django, SQLite                      |
| Frontend     | HTML, CSS (via Django templates)    |
| Media        | Static image hosting                |
| Environment  | Python 3.x, Virtualenv              |

---

## 🧰 Setup Instructions

1. **Clone the repo**  
   ```bash
   git clone https://github.com/sudharshan59/affordable-housing-tracker.git
   cd affordable-housing-tracker
Create and activate virtual environment

bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
Install dependencies

bash
pip install -r requirements.txt
Run migrations

bash
python manage.py migrate
Start the server

bash
python manage.py runserver
Access the app Visit http://127.0.0.1:8000/ in your browser.

🖼️ Media & Assets
All housing images are stored in media/houses/

Static files are managed via Django’s default configuration

🛡️ Privacy & Local Deployment
This project is designed with local-first principles—no external APIs or cloud dependencies. Ideal for internal use or secure deployment in resource-constrained environments.

📌 Project Structure
Code
affordable-housing-tracker/
├── affordable_housing/       # Main Django app
├── housing/                  # Housing listings logic
├── media/houses/             # Uploaded images
├── venv/                     # Virtual environment
├── db.sqlite3                # Local database
└── manage.py                 # Django CLI entrypoint
👤 Author
Made with ❤️ by Sudharshanmonith 🔗 GitHub Profile

📬 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

📄 License
This project is open-source under the MIT License.
