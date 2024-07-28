import phonenumbers
from phonenumbers import geocoder
import requests

def locate_location(phone_number):
    try:
        # Validate and parse the phone number
        parsed_number = phonenumbers.parse(phone_number, None)
        location = geocoder.description_for_number(parsed_number, "en")
        
        # Get IP geolocation data
        ip_api_url = "http://ip-api.com/json"
        response = requests.get(ip_api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        ip_data = response.json()
        
        # Extract location data
        ip_location = {
            "city": ip_data.get("city", "N/A"),
            "region": ip_data.get("region", "N/A"),
            "country": ip_data.get("country", "N/A"),
            "latitude": ip_data.get("lat", "N/A"),
            "longitude": ip_data.get("lon", "N/A"),
        }
        
        return location, ip_location
    
    except phonenumbers.phonenumberutil.NumberParseException:
        return "Invalid phone number", None
    except requests.RequestException as e:
        return f"Error fetching IP geolocation data: {str(e)}", None

# Example usage
phone_number = "+91xxxxxxxxxx"  # Replace with the desired phone number
location, ip_location = locate_location(phone_number)

print(f"Phone Number Location: {location}")
if ip_location:
    print("IP Geolocation:")
    print(f"  City: {ip_location['city']}")
    print(f"  Region: {ip_location['region']}")
    print(f"  Country: {ip_location['country']}")
    print(f"  Latitude: {ip_location['latitude']}")
    print(f"  Longitude: {ip_location['longitude']}")
else:
    print("Could not determine the IP geolocation.")