from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

# CSV file path
DATA_FILE = 'data/applications.csv'

# Ensure directory and CSV file exists
if not os.path.exists('data'):
    os.makedirs('data')

if not os.path.isfile(DATA_FILE):
    with open(DATA_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Phone', 'Address', 'Description', 'Service Type'])

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/apply', methods=['POST'])
def apply():
    name = request.form['name']
    phone = request.form['phone']
    address = request.form['address']
    description = request.form.get('description', '')
    service_type = request.form['service_type']

    # Save form data to CSV
    with open(DATA_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, address, description, service_type])

    return redirect('/')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
