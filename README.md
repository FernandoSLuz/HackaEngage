# HackaEngage - Campus Party Experience - 1st Place

This is a Python/Flask solution created to engage the over 4000 employees who work at the Parque Dom Pedro mall. The solution harmonizes with IntranetMall’s API and encourages logistics to sign up for the existing employee access control system. It develops an automated system that checks and sends news, announcements, and store promotions using WhatsApp.

The project won first place at the HackaEngage hackathon, held in September 2019.

## Repository

https://github.com/FernandoSLuz/HackaEngage

## Main Scripts

The main scripts of this solution are the following:

1. [app.py](https://github.com/FernandoSLuz/HackaEngage/blob/master/app.py): The main Flask application file.
2. [update.py](https://github.com/FernandoSLuz/HackaEngage/blob/master/routes/update.py): Handles the `/update` and `/submitupdate` routes.
3. [bd.py](https://github.com/FernandoSLuz/HackaEngage/blob/master/bd.py): Defines the database schema and CRUD operations.
4. [registers.py](https://github.com/FernandoSLuz/HackaEngage/blob/master/registers.py): Handles the `/registers` route.
5. [requirements.txt](https://github.com/FernandoSLuz/HackaEngage/blob/master/requirements.txt): Lists the required libraries and their versions for this project.
6. [webhook.py](https://github.com/FernandoSLuz/HackaEngage/blob/master/webhook.py): Processes incoming webhook events and sends messages based on user actions.

## Technologies Used

- WhatsApp
- Wassenger
- Twilio
- Python
- Flask
- MySQL
- Google Cloud VM

## Installation

1. Clone the repository:

```bash
git clone https://github.com/FernandoSLuz/HackaEngage.git
```

2. Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Set up your database and configure the credentials in the `bd.py` file.

## Running the Application

1. Set the Flask environment variables:

```bash
export FLASK_APP=app.py
```

2. Run the application:

```bash
flask run
```

Visit `http://127.0.0.1:5000/` to access the application in your browser.

## License

This project is licensed under the MIT License.
