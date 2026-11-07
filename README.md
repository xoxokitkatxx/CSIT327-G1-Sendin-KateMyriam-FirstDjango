# CampusConnect
- **Author:** Kate Myriam B. Sendin
- **Course:** CSIT327 - G1

## Setup and Run Instructions
1. **Clone the repository:**
   ```bash
   git clone https://github.com/xoxokitkatxx/CSIT327-G1-Sendin-KateMyriam-FirstDjango.git
   cd CSIT327-G1-Sendin-KateMyriam-FirstDjango
   ```
2. **Create and activate a virtual environment:**
   - **Windows:**
     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```
   - **Mac/Linux:**
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Create a superuser (optional, for testing admin access):**
   ```bash
   python manage.py createsuperuser
   ```
6. **Start the development server:**
   ```bash
   python manage.py runserver
   ```
7. Open `http://127.0.0.1:8000/` in your browser.