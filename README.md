
---

# Travel Buddy Project

## Overview

The Travel Buddy project is designed to help users explore travel destinations, book trips, and access travel resources efficiently. It leverages Python for backend development, SQL for robust data storage, WampServer for managing the database server, and PyCharm as the integrated development environment.

## Features

- **Destination Exploration:** Browse detailed information and images for various travel destinations.
- **Booking System:** Simplified booking process for flights, hotels, and travel packages.
- **Responsive Design:** Optimized for a variety of devices to ensure a smooth user experience.
- **User Reviews:** Allows users to leave and read reviews for destinations and services.
- **Interactive Maps:** Integration with map services for location exploration.

## Technologies & Tools Used

- **Programming Language:** Python
- **Backend Framework:** Flask/Django (choose one)
- **Database:** SQL (using WampServer for managing MySQL/MariaDB)
- **Frontend:** HTML, CSS, JavaScript, Bootstrap
- **APIs:** Integration with third-party APIs for flight and hotel data
- **Development Environment:** PyCharm, WampServer

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/varshan-ms/travel-buddy.git

   ```

2. **Create and Activate Virtual Environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install and Set Up WampServer:**
   - Download and install WampServer from [here](https://www.wampserver.com/en/).
   - Start WampServer and make sure the services are running.

5. **Create a Database:**
   - Open phpMyAdmin (usually at `http://localhost/phpmyadmin`).
   - Create a new database for the project.

6. **Set Up Environment Variables:**
   Create a `.env` file in the root directory and add your environment variables (e.g., database connection strings, API keys).
   
   ```

7. **Run the Application:**
   ```bash
   
   python app.py runserver  # 
   ```

8. **Access the Website:**
   Open your browser and navigate to `http://localhost:5000` (for Flask) or `http://localhost:8000` (for Django) to view the website.

## Usage

1. **Browse Destinations:** Explore various travel destinations, view images, and read descriptions.
2. **Book Trips:** Use the booking system to search for and book flights, hotels, and travel packages.
3. **User Reviews:** Read and submit reviews for different destinations and services.
4. **Interactive Maps:** Explore locations using the integrated map feature.


## Contributing

Contributions are welcome! Please fork this repository and submit a pull request for any improvements or bug fixes.

## Contact

For any inquiries or questions, feel free to reach out:

- Email: your-varshan07@gmail.com
- LinkedIn: [varshanms](https://www.linkedin.com/in/msvarshan)

---
