📚 Class Booking API
This is a simple Flask-based web API that lets users:

View available classes (GET /classes)

Book a class (POST /book)

View their bookings (GET /bookings)

🚀 How to Run This App
1. Clone or Download the Project
bash
Copy
Edit
git clone https://your-repo-url.git
cd your-project-folder
2. Install Required Packages
Make sure Python (preferably 3.7 or later) is installed on your system.

Then install the required Python libraries:

bash
Copy
Edit
pip install flask
If your project uses other packages (e.g. pytz, etc.), you can install them using:

bash
Copy
Edit
pip install -r requirements.txt
If you don’t have a requirements.txt, create one and add packages like:

txt
Copy
Edit
flask
pytz
3. Check Required Files
Make sure you have these Python files in the same folder:

app.py – the main Flask app (your script)

models.py – contains load_classes, load_bookings, save_classes, save_bookings functions

utils.py – contains convert_to_timezone and validate_booking functions

data/ folder or JSON files (like classes and bookings data)

4. Start the Server
Run the Flask app using:

bash
Copy
Edit
python app.py
You should see:

nginx
Copy
Edit
Starting Flask server...
 * Running on http://127.0.0.1:5000
🛠 API Endpoints
✅ GET /classes
Description: Get a list of available classes.
Optional query parameter: timezone (e.g. Asia/Kolkata, UTC, etc.)

Example:

bash
Copy
Edit
curl "http://localhost:5000/classes?timezone=UTC"
📝 POST /book
Description: Book a class.

Required JSON body:

json
Copy
Edit
{
  "class_id": "abc123",
  "client_name": "John Doe",
  "client_email": "john@example.com"
}
Example:

bash
Copy
Edit
curl -X POST http://localhost:5000/book \
     -H "Content-Type: application/json" \
     -d '{"class_id": "abc123", "client_name": "John Doe", "client_email": "john@example.com"}'
📬 GET /bookings
Description: Get all bookings for a given email.

Query parameter: email

Example:

bash
Copy
Edit
curl "http://localhost:5000/bookings?email=john@example.com"
📂 File Structure Example
pgsql
Copy
Edit
your-project/
├── app.py
├── models.py
├── utils.py
├── data/
│   ├── classes.json
│   └── bookings.json
└── requirements.txt
