from flask import Flask, request, jsonify
from models import load_classes, load_bookings, save_classes, save_bookings
from utils import convert_to_timezone, validate_booking
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# GET /classes
@app.route('/classes', methods=['GET'])
def get_classes():
    try:
        target_timezone = request.args.get("timezone", "Asia/Kolkata")
        app.logger.info(f"Requested timezone: {target_timezone}")

        classes = load_classes()
        app.logger.info(f"Loaded {len(classes)} classes")

        for cls in classes:
            original_dt = cls.get('datetime')
            from_tz = cls.get('timezone')

            app.logger.info(f"Class ID {cls.get('id')} original datetime: {original_dt} [{from_tz}]")

            converted = convert_to_timezone(original_dt, from_tz, target_timezone)
            cls['datetime'] = converted.isoformat() if hasattr(converted, 'isoformat') else str(converted)

        return jsonify(classes)

    except Exception as e:
        app.logger.error("Error in /classes route", exc_info=True)
        return jsonify({"error": "Internal Server Error"}), 500


# POST /book
@app.route('/book', methods=['POST'])
def book_class():
    data = request.get_json()
    required_fields = ['class_id', 'client_name', 'client_email']

    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing Fields"}), 400

    classes = load_classes()
    bookings = load_bookings()

    valid, message = validate_booking(data, classes, bookings)
    if not valid:
        return jsonify({"error": message}), 400

    bookings.append({
        "class_id": data['class_id'],
        "client_name": data['client_name'],
        "client_email": data['client_email']
    })

    for cls in classes:
        if cls['id'] == data['class_id']:
            cls['available_slots'] -= 1
            break

    save_bookings(bookings)
    save_classes(classes)

    return jsonify({"message": "Booking Successful"}), 201


# GET /bookings
@app.route('/bookings', methods=['GET'])
def get_bookings():
    email = request.args.get("email")
    if not email:
        return jsonify({"error": "Missing email parameter"}), 400

    bookings = load_bookings()
    user_bookings = [b for b in bookings if b['client_email'].lower() == email.lower()]
    return jsonify(user_bookings)


# Run the Flask app
if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(port=5000, debug=True)
