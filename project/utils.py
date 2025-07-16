from datetime import datetime
import pytz

def convert_to_timezone(dt_string, from_tz, to_tz):
    from_zone = pytz.timezone(from_tz)
    to_zone = pytz.timezone(to_tz)
    dt = datetime.fromisoformat(dt_string)
    dt = from_zone.localize(dt)
    return dt.astimezone(to_zone)

def validate_booking(data, classes, bookings):
    # Add basic validation logic (e.g., checking if class exists and has slots)
    for cls in classes:
        if cls['id'] == data['class_id']:
            if cls['available_slots'] <= 0:
                return False, "No available slots"
            break
    else:
        return False, "Class not found"
    
    # Optional: check if user already booked
    for b in bookings:
        if b['class_id'] == data['class_id'] and b['client_email'] == data['client_email']:
            return False, "User already booked this class"
    
    return True, "Valid"
