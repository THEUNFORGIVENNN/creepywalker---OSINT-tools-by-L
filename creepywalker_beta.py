import requests
from colorama import Fore, Style, init
import argparse
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyfiglet  # Import pyfiglet for banner

# Banner CREEPYWALKER
def print_banner():
    banner = pyfiglet.figlet_format("CREEPYWALKER", font="slant")
    print(Fore.MAGENTA + banner + Style.RESET_ALL)
    print(Fore.YELLOW + "OSINT TOOLS BY L (use --help)" + Style.RESET_ALL)  # Add additional text below the banner

# 1. GeoIP Lookup
def get_geo_from_ip(ip):
    try:
        res = requests.get(f"http://ip-api.com/json/{ip}").json()
        if res['status'] == 'success':
            return {
                'ip': res['query'],
                'country': res['country'],
                'region': res['regionName'],
                'city': res['city'],
                'zip': res['zip'],
                'lat': res['lat'],
                'lon': res['lon'],
                'isp': res['isp']
            }
        else:
            return {'error': res.get('message', 'Unknown error')}
    except Exception as e:
        return {'error': str(e)}

# 2. Phone Number Lookup

init(autoreset=True)

def phone_lookup(phone_number, api_key):
    url = f"http://apilayer.net/api/validate?access_key={api_key}&number={phone_number}"
    response = requests.get(url).json()
    
    # Output dengan warna yang menarik
    if response.get('valid'):
        print(f"{Fore.GREEN}{Style.BRIGHT}Phone Lookup for {Fore.CYAN}{phone_number}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'Valid'}: {Fore.GREEN}{response['valid']}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'Number'}: {Fore.CYAN}{response['number']}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'Local Format'}: {Fore.CYAN}{response['local_format']}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'International Format'}: {Fore.CYAN}{response['international_format']}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'Country Prefix'}: {Fore.CYAN}{response['country_prefix']}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'Country Code'}: {Fore.CYAN}{response['country_code']}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'Country Name'}: {Fore.CYAN}{response['country_name']}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'Location'}: {Fore.CYAN}{response.get('location', 'N/A')}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'Carrier'}: {Fore.CYAN}{response['carrier']}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{'Line Type'}: {Fore.CYAN}{response['line_type']}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}{Style.BRIGHT}Invalid phone number or failed lookup.{Style.RESET_ALL}")

# 3. Image EXIF Analyzer
def get_exif_data(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()
    if exif_data is None:
        return {'error': 'No EXIF data found'}
    
    exif = {}
    for tag, value in exif_data.items():
        tag_name = TAGS.get(tag, tag)
        exif[tag_name] = value
    
    # If GPS data exists
    gps_info = exif.get('GPSInfo', {})
    if gps_info:
        gps_coordinates = gps_info.get(2)
        if gps_coordinates:
            lat = gps_coordinates[0] + (gps_coordinates[1] / 60.0) + (gps_coordinates[2] / 3600.0)
            lon = gps_coordinates[3] + (gps_coordinates[4] / 60.0) + (gps_coordinates[5] / 3600.0)
            exif['GPS'] = {'latitude': lat, 'longitude': lon}
    
    return exif

# 4. Reverse Geocoding
def reverse_geocode(lat, lon):
    try:
        url = f"https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json"
        headers = {"User-Agent": "creepywalker/1.0"}
        res = requests.get(url, headers=headers).json()
        address = res.get("address", {})
        return {
            "country": address.get("country"),
            "state": address.get("state"),
            "city": address.get("city", address.get("town", address.get("village"))),
            "postcode": address.get("postcode")
        }
    except Exception as e:
        return {'error': str(e)}

# 5. Dorking / Crawler
def google_dork(query):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    
    url = f"https://www.google.com/search?q={query}"
    driver.get(url)
    time.sleep(3)
    
    results = driver.find_elements(By.XPATH, "//h3")
    dork_results = []
    for result in results:
        dork_results.append(result.text)
    
    driver.quit()
    return dork_results

# 6. Subdomain + Vulnerability Scanner
def check_subdomains(domain):
    subdomains = ["www", "blog", "shop", "dev"]
    subdomain_results = []
    
    for sub in subdomains:
        subdomain_url = f"http://{sub}.{domain}"
        try:
            res = requests.get(subdomain_url)
            if res.status_code == 200:
                subdomain_results.append(subdomain_url)
        except requests.exceptions.RequestException as e:
            continue
    
    return subdomain_results

# Main function to handle command-line arguments
def main():
    print_banner()  # Display banner
    parser = argparse.ArgumentParser(description="CreepyWalker - A tool for various reconnaissance tasks")
    
    # Arguments
    parser.add_argument('--geo', type=str, help='IP address to perform GeoIP lookup')
    parser.add_argument('--phone', type=str, help='Phone number to look up(usage +country code)')
    parser.add_argument('--image', type=str, help='Image file path to analyze EXIF data')
    parser.add_argument('--dork', type=str, help='Google Dork query')
    parser.add_argument('--domain', type=str, help='Domain to check subdomains')
    parser.add_argument('--apikey', type=str, help='API Key just for phone lookup')

    args = parser.parse_args()

    # Handle different commands
    if args.geo:
        print(f"GeoIP Lookup for {args.geo}:")
        print(get_geo_from_ip(args.geo))
    
    if args.phone:
        if not args.apikey:
            print("Error: API Key required for phone lookup")
        else:
            print(f"Phone Lookup for {args.phone}:")
            print(phone_lookup(args.phone, args.apikey))
    
    if args.image:
        print(f"EXIF Data for image {args.image}:")
        print(get_exif_data(args.image))
    
    if args.lat and args.lon:
        print(f"Reverse Geocoding for Latitude: {args.lat}, Longitude: {args.lon}:")
        print(reverse_geocode(args.lat, args.lon))
    
    if args.dork:
        print(f"Google Dork Results for query: {args.dork}")
        print(google_dork(args.dork))
    
    if args.domain:
        print(f"Checking subdomains for domain: {args.domain}")
        print(check_subdomains(args.domain))

if __name__ == '__main__':
    main()
