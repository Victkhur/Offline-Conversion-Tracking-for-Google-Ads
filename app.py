# Offline Conversion Tracking for Google Ads
   # Captures GCLID from Google Ads, stores lead data, and simulates offline conversion uploads
   from flask import Flask, request, render_template
   import sqlite3
   import uuid
   import requests
   from datetime import datetime

   app = Flask(__name__)

   # Initialize SQLite database
   def init_db():
       with sqlite3.connect('leads.db') as conn:
           cursor = conn.cursor()
           cursor.execute('''
               CREATE TABLE IF NOT EXISTS leads (
                   id TEXT PRIMARY KEY,
                   name TEXT,
                   email TEXT,
                   gclid TEXT,
                   conversion_status TEXT,
                   created_at TIMESTAMP
               )
           ''')
           conn.commit()

   # Route for landing page with lead form
   @app.route('/')
   def landing_page():
       gclid = request.args.get('gclid', '')
       return render_template('index.html', gclid=gclid)

   # Route to handle form submission
   @app.route('/submit', methods=['POST'])
   def submit_lead():
       name = request.form.get('name')
       email = request.form.get('email')
       gclid = request.form.get('gclid')
       
       lead_id = str(uuid.uuid4())
       
       with sqlite3.connect('leads.db') as conn:
           cursor = conn.cursor()
           cursor.execute('''
               INSERT INTO leads (id, name, email, gclid, conversion_status, created_at)
               VALUES (?, ?, ?, ?, ?, ?)
           ''', (lead_id, name, email, gclid, 'pending', datetime.now()))
           conn.commit()
       
       return 'Lead submitted successfully!'

   # Route to simulate CRM marking deal as "Closed"
   @app.route('/update_conversion/<lead_id>', methods=['POST'])
   def update_conversion(lead_id):
       with sqlite3.connect('leads.db') as conn:
           cursor = conn.cursor()
           cursor.execute('''
               UPDATE leads SET conversion_status = ? WHERE id = ?
           ''', ('closed', lead_id))
           conn.commit()
           
           cursor.execute('SELECT gclid FROM leads WHERE id = ?', (lead_id,))
           result = cursor.fetchone()
           if result:
               gclid = result[0]
               upload_conversion(gclid, lead_id)
       
       return 'Conversion updated and uploaded!'

   # Mock function to simulate Google Ads API conversion upload
   def upload_conversion(gclid, lead_id):
       try:
           conversion_data = {
               'gclid': gclid,
               'conversion_action_id': 'YOUR_CONVERSION_ACTION_ID',
               'conversion_date_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
               'conversion_value': 100.0,
               'currency_code': 'USD'
           }
           print(f"Simulating conversion upload for GCLID: {gclid}, Lead ID: {lead_id}")
           return True
       except Exception as e:
           print(f"Error uploading conversion: {str(e)}")
           return False

   if __name__ == '__main__':
       init_db()
       app.run(debug=True)
