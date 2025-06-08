CreepyWalker - OSINT Tools by L
Description:
CreepyWalker is a collection of OSINT (Open Source Intelligence) tools designed for various social engineering and data analysis purposes, such as:

GeoIP Lookup: Find geographic information based on an IP address.

Phone Lookup: Find information related to a phone number.

Image EXIF Analyzer: Analyze the EXIF data embedded in images.

Reverse Geocoding: Convert GPS coordinates into a physical address.

Google Dorking: Perform searches using Google Dorking techniques.

Subdomain & Vulnerability Scanner: Check subdomains and their vulnerabilities.

This tool leverages external APIs and browser automation via Selenium, and outputs results in a colorful, easy-to-read format using colorama.

Setup and Running CreepyWalker from Scratch

1.) Download the Project
a. Clone the Repository from GitHub
If you have Git installed, you can clone the CreepyWalker repository by running the following command:

    git clone https://github.com/username/creepywalker.git

2.) Install Dependencies

a. Create a Virtual Environment (Optional but Recommended)
It is recommended to use a virtual environment to isolate dependencies.

  Create a virtual environment:

    python -m venv venv
Activate the virtual environment:

  On Windows:

    venv\Scripts\activate
  On macOS/Linux:
  
    source venv/bin/activate
  b. Install Dependencies
Once the virtual environment is activated, install the required dependencies by running:

    pip install -r requirements.txt

The requirements.txt file includes libraries such as requests, colorama, Pillow, and selenium.

3. Running CreepyWalker

a. Run GeoIP Lookup
To perform a GeoIP lookup, use the following command:

    python creepywalker_beta.py --geo <IP_ADDRESS>
Replace <IP_ADDRESS> with the IP address you want to check

b. Run Phone Lookup
To look up information about a phone number, run the following command:

    python creepywalker_beta.py --phone <PHONE_NUMBER> --apikey <API_KEY>
Replace <PHONE_NUMBER> with the phone number you want to search for, and <API_KEY> with the API key you obtained from apilayer.

c. Run EXIF Analyzer (For Images)
To analyze the EXIF data of an image, use the following command:

    python creepywalker_beta.py --image <IMAGE_PATH>
Replace <IMAGE_PATH> with the path to the image file you want to analyze.

d. Run Reverse Geocoding (Get Address from Coordinates)
To perform reverse geocoding based on latitude and longitude:

    python creepywalker_beta.py --lat <LATITUDE> --lon <LONGITUDE>
Replace <LATITUDE> and <LONGITUDE> with the appropriate coordinates.

e. Run Google Dorking
To use Google Dorking, you can provide a search query like this:

    python creepywalker_beta.py --dork "<QUERY>"
Replace <QUERY> with the search query you want to perform using Google Dorking techniques.

f. Run Subdomain & Vulnerability Scanner
To check subdomains and their vulnerabilities for a given domain, use the following command:


    python creepywalker_beta.py --domain <DOMAIN>
Replace <DOMAIN> with the domain you want to check.

4. Using the Output
Whenever you run one of the above commands, the results will be displayed in your terminal with color-coded output for readability. For example, for the GeoIP lookup results, you'll see information such as country, city, and ISP displayed with different colors for clarity.

5. Getting an API Key for Phone Lookup
For the Phone Lookup feature, you'll need an API key from apilayer:

Visit the apilayer Phone Lookup API.

Sign up and obtain your API Key.

Use your API Key with the --apikey parameter when running the script.

6. Troubleshooting
If you run into any issues, here are some things to try:

Ensure Python and dependencies are correctly installed.
Check by running python --version and ensure all dependencies in requirements.txt are installed.

Verify API Credentials.
If you get an error related to APIs, ensure that you've correctly entered the API Key.

Check Your Internet Connection.
Some features require internet access to fetch data from external services (e.g., GeoIP lookup, phone lookup).

Good luck and feel free to ask if you encounter any issues or have further questions!



## ☕ Support Me on Ko-fi
[![ko-fi](https://ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/N4N61G430Z)
