from flask import *
import pymysql

import pymysql.cursors
# step 8 - on add product function
import os


# create a flask
app=Flask(__name__)
app.config['UPLOAD_FOLDER']='static/images'

# create the route of the api / endpoint
@app.route("/api/signup", methods=['POST'])

# Create a function to handle the signup process
def signup():

    if request.method=="POST":
        username: str=request.form["username"]
        email=request.form['email']
        passwrd=request.form['passwrd']
        phone=request.form['phone']

        # connect to the database for data storeage
        connection=pymysql.connect(host='localhost', user='root', password='', database='SokoGarden')

        # insert the data to the database
        # cursor - allows run sql queries in python
        cursor=connection.cursor()
        cursor.execute('insert into users(username, email, passwrd, phone) values(%s,%s,%s,%s)',(username, passwrd, email, phone))


        # cursor the save or commits the changes to the database
        connection.commit()

        return jsonify({
            "success" : "log"
        })
    
# create a function to handle the signin

# step 1 - define the route
@app.route('/api/signin', methods=['POST'])

# step 2 - create a function 
def signin():
    # extract POST data step -3
    email=request.form['email']
    passwrd=request.form["passwrd"]

    # 3 Step 4- connect to the DB
    connection=pymysql.connect(host='localhost', user='root',password='',database='SokoGarden')

    # create a cursor to return results a dictionary, initialize connection
    cursor=connection.cursor(pymysql.cursors.DictCursor)

    # STEP -6 SQL query to select from the users table email passwrd
    sql="select * from users where email=%s and passwrd=%s"

    # step - 7 prepare the data to replace the placeholders %s  
    data=(email, passwrd)

    # step -9 use the cursor to execute the sql providing the data to replace the placeholders
    cursor.execute(sql,data)

    # step 9 check how rows are found
    count=cursor.rowcount

    # step - 10 count if rows are zero,invalid credentials- no user found
    if count == 0:
        return jsonify({
            'message' : 'Login Failed'
        })
    else:
        # else there is a user, return a message to say login success and all user details, fetchone to get all user login details
        user=cursor.fetchone()

        # step return the login success message with user details as a dictionary
        return jsonify({
            'Message' : 'Login success',
            'user' : user
        })
    

# Add products function    
# step 1 - Define the route
@app.route("/api/add_product", methods=['POST'])

# step 2 - create a function to perform the act of adding products
def add_product():
    if request.method =="POST":

        # STEP 3 - Extract the data
        product_name=request.form['product_name'] 
        product_description=request.form.get('product_description')
        product_cost=request.form['product_cost']

        # product_photo=request.form['product_photo']
        # extract the image data
        photo=request.files['product_photo']

        # get the image file name
        filename=photo.filename

        # specify where the image will be saved (in static folder) - image path
        photo_path=os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # save the image
        photo.save(photo_path)




        # step 4 - connect to the database
        connection=pymysql.connect(host='localhost', user='root', password='', database='SokoGarden')

        # step 5 - prepare and execute query to insert data intoour database
        cursor=connection.cursor()

        cursor.execute('INSERT INTO product_details(product_name, product_description, product_cost, product_photo) VALUES(%s, %s, %s, %s)', (product_name, product_description, product_cost, filename))

        # step 6 - commit / save the changes
        connection.commit()

        # step 6 - return the success message
        return jsonify({
            'success' : 'product successfully'
        })



# get product function

# define the route
@app.route("/api/get_products", methods=["GET"])
def get_product_details():

    # connect to the database with Dict cursor for direct dictionary results
    connection=pymysql.connect(host="localhost", user="root", password="", database="SokoGarden")

    # Create the cursor object and fetch all data from the product details table
    cursor=connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM product_details")
    product_details=cursor.fetchall()

    # close the database connection
    connection.close()

    # return the fetched the products
    return product_details


# Mpesa Payment Route/Endpoint 
import requests
import datetime
import base64
from requests.auth import HTTPBasicAuth

@app.route('/api/mpesa_payment', methods=['POST'])
def mpesa_payment():
    if request.method == 'POST':
        amount = request.form['amount']
        phone = request.form['phone']
        # GENERATING THE ACCESS TOKEN
        # create an account on safaricom daraja
        consumer_key = "GTWADFxIpUfDoNikNGqq1C3023evM6UH"
        consumer_secret = "amFbAoUByPV2rM5A"

        api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"  # AUTH URL
        r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        data = r.json()
        access_token = "Bearer" + ' ' + data['access_token']

        #  GETTING THE PASSWORD
        timestamp = datetime.datetime.today().strftime('%Y%m%d%H%M%S')
        passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
        business_short_code = "174379"
        data = business_short_code + passkey + timestamp
        encoded = base64.b64encode(data.encode())
        password = encoded.decode('utf-8')

        # BODY OR PAYLOAD
        payload = {
            "BusinessShortCode": "174379",
            "Password": "{}".format(password),
            "Timestamp": "{}".format(timestamp),
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,  # use amount when testing
            "PartyA": phone,  # change to your number
            "PartyB": "174379",
            "PhoneNumber": phone,
            "CallBackURL": "https://modcom.co.ke/api/confirmation.php",
            "AccountReference": "account",
            "TransactionDesc": "account"
        }

        # POPULAING THE HTTP HEADER
        headers = {
            "Authorization": access_token,
            "Content-Type": "application/json"
        }

        url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"  # C2B URL

        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        return jsonify({"message": "Please Complete Payment in Your Phone and we will deliver in minutes"})
    
















# run the app
if __name__ =='__main__':
 app.run(debug=True)


