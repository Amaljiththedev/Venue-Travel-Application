Venue Travel App

Venue Travel App is an all-in-one travel planning solution designed to assist users in planning trips, 
managing itineraries, and receiving real-time travel updates. The app leverages several APIs to provide a seamless and integrated experience.

Features

- User Authentication: Sign in using Google accounts for a personalized experience.
- Mapping and Navigation: Utilize Google Maps for location search, route planning, and place information.
- Weather Updates: Get real-time weather information relevant to your travel plans.
- Flight Search: Search for flights, compare prices, and facilitate bookings.
- Hotel Search: Search for hotels, compare rates, and book accommodations.
- Travel Advice and Recommendations**: Receive travel advice, answer queries, and get personalized recommendations using AI.

 Technologies Used

- Backend: Django
- Frontend: JavaScript, HTML, CSS
- Authentication**: Google OAuth using `django-allauth`
- APIs:
  - Google Maps API (JavaScript API, Places API)
  - OpenWeather API
  - Skyscanner API
  - Booking.com API
  - OpenAI API (for AI-powered interactions)

Installation

1. Clone the repository:

   bash
   git clone https://github.com/Amaljiththedev/Venue-Travel-Application.git
   cd Venue-Travel-Application
   

2. Create and activate a virtual environment:

   bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables. Create a `.env` file in the project root with the following content:

   ```env
   SECRET_KEY=your_secret_key
   DEBUG=True
   ALLOWED_HOSTS=localhost, 127.0.0.1
   GOOGLE_CLIENT_SECRET=your_google_client_secret
   SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=your_google_client_id
   SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=your_google_client_secret
   ```

5. Apply migrations:

   bash
   python manage.py migrate
   

6. Run the development server:
   bash
   python manage.py runserver


Usage

1. Navigate to `http://127.0.0.1:8000` in your web browser.
2. Sign in using your Google account.
3. Start planning your trip by searching for locations, checking weather updates, finding flights, and booking hotels.

Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Contact

For support or any questions, please reach out to Amaljith at amaljith6430@gmail.com.


Feel free to adjust any part of this README to better fit your project's specifics.
