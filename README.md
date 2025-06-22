# Offline Conversion Tracking for Google Ads

   This project demonstrates a system to track offline conversions from Google Ads by capturing the Google Click ID (GCLID), storing lead data, and uploading conversions to Google Ads when a deal is closed in a CRM. It’s built as a proof-of-concept for attributing offline sales to online ad campaigns.

   ## Features
   - Captures GCLID from URL parameters on a landing page.
   - Stores lead data (name, email, GCLID) in an SQLite database.
   - Simulates CRM integration by updating conversion status via an API endpoint.
   - Mocks Google Ads API calls to upload offline conversions.

   ## Tech Stack
   - **Backend**: Python (Flask)
   - **Database**: SQLite
   - **Frontend**: HTML, CSS
   - **APIs**: Google Ads API (mocked), Google Tag Manager (GTM) for GCLID capture
   - **CRM**: Simulated (HubSpot-compatible webhook endpoint)

   ## Setup Instructions
   1. **Clone the repository**:
      ```bash
      git clone https://github.com/your-username/offline-conversion-tracking.git
      cd offline-conversion-tracking
      ```
   2. **Install dependencies**:
      ```bash
      pip install -r requirements.txt
      ```
   3. **Run the application**:
      ```bash
      python app.py
      ```
      Access the landing page at `http://localhost:5000/?gclid=test_gclid_123`.
   4. **Simulate a conversion**:
      - Submit a lead via the form.
      - Use a tool like Postman to send a POST request to `http://localhost:5000/update_conversion/<lead_id>`.

   ## Usage
   - Visit the landing page with a `?gclid=...` parameter to simulate a Google Ads click.
   - Submit the form to store lead data.
   - Trigger a conversion by updating a lead’s status to "closed" via the `/update_conversion` endpoint.
   - The app logs a mock Google Ads API call to upload the conversion.

   ## Notes
   - The Google Ads API is mocked due to credential requirements. For production, configure OAuth2 and a conversion action in Google Ads.
   - GTM setup is documented but not implemented in the frontend. Add GTM scripts to `index.html` for dynamic GCLID capture.
   - For CRM integration, configure webhooks (e.g., HubSpot) to trigger the `/update_conversion` endpoint.

   ## Future Improvements
   - Implement real Google Ads API integration.
   - Add input validation and error handling.
   - Deploy to a cloud platform (e.g., Heroku, AWS).
   - Enhance UI with a dashboard to view leads and conversions.

   ## License
   MIT License
