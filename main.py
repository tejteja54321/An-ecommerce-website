#importing libraries
from flask import *
from dbclass import *
import os
import pyotp
import smtplib
from email.message import EmailMessage
import datetime

app=Flask(__name__)
app.secret_key="Teja@531"
app.config["upload_folder"]="static/upload"

#----------------------------HOME-----------------------------------#
#Home Page URL
@app.route("/")
def project():
    return render_template("project.html")
@app.route("/project2")
def project2():
    id = session['cusid']
    sql = "select * from customer where cusid like '%s'" % (id)
    data = fetchall(sql)
    data=data[0]
    return render_template("project2.html", data=data)


#Register Page
@app.route("/register", methods=["POST", "GET"])
def register():
    print("you are in register page")
    msg = ""
    if request.method == "POST":
        print("hi")
        uname = request.form["username"]
        email = request.form["email"]
        pswd = request.form["password"]
        phno = request.form["phno"]
        phno = int(phno)
        print("phno: ", phno)
        file = request.files['file']
        file.save(os.path.join(app.config["upload_folder"], file.filename))
        sql = "SELECT * FROM customer WHERE email LIKE '%s' AND password LIKE '%s' OR phno LIKE '%s'" % (
        email, pswd, phno)
        data = fetchall(sql)
        if data:
            msg = "Already existed. You can login using your credentials."
        else:
            sql = "INSERT INTO customer (userid, email, password, phno, file) VALUES ('%s', '%s', '%s', '%s', '%s')" % (
            uname, email, pswd, phno, file.filename)
            excuteupdate(sql)
            msg = "Account created successfully"
    return render_template("project.html", msg=msg)

#Login Page
@app.route("/loginpage" ,methods=["POST","GET"])
def loginpage():
    print("login")
    msg=""
    if request.method=="POST":
        luser = request.form["Lusername"]
        lpswd = request.form["Lpassword"]
        sql="select * from customer where email like '%s' and password like '%s'"%(luser,lpswd)
        data = fetchall(sql)
        if (data):
            data = data[0]
            session['cusid'] = data[0]
            msg = "%s Now You Can Access Your Page Bro!!!"%(data[1].upper())
            print(data,msg)
            return render_template("project2.html", data=data, alert=msg)
        else:
            msg = "Please provide Valid details!!!"
        return render_template("project.html",alert=msg)

#Logout
@app.route("/logout")
def logout():
    session.clear()
    return render_template("project.html")

#--------------------------------------HOME END----------------------------------#

#-------------------------------------SHOPPING---------------------------------#

#SHOPPING PAGE
@app.route("/shoppingbag")
def shoppingbag():
    sql="Select * from products"
    data=fetchall(sql)
    return render_template("products.html",data2=data)

#SEARCH BAR
@app.route("/search", methods=["POST","GET"])
def search():
    if request.method=="POST":
        search_query = request.form["query"]
        print("hello",search_query)
        if search_query:
            search_query = search_query.lower()
            sql = sql = f"""
                            SELECT * 
                            FROM products 
                            WHERE LOWER(pname) LIKE '{search_query.lower()}%' 
                            OR LOWER(pcategory) LIKE '{search_query.lower()}%'
                        """
            filtered_data = fetchall(sql)  # Replace fetchall with your actual method
            print(filtered_data)
            if session['cusid']:
                id=session['cusid']
                sql = "select * from customer where cusid like '%s'" % (id)
                data = fetchall(sql)
                data = data[0]
                print("login:  ", data)
                return render_template("products2.html",data=data ,data2=filtered_data)
        else:
            sql="select * from products"
            data2=fetchall(sql)
            id = session['cusid']
            sql = "select * from customer where cusid like '%s'" % (id)
            data = fetchall(sql)
            data = data[0]
            return render_template("products2.html",data=data ,data2=data2)

#FILTER BAR
@app.route("/filter", methods=["POST","GET"])
def filter():
    if request.method=="POST":
        category = request.form["category"]
        if session['cusid']:
            id = session['cusid']
            sql = "select * from customer where cusid like '%s'" % (id)
            data = fetchall(sql)
            data = data[0]
            if category =="All":
                sql="select * from products"
                filtered_data = fetchall(sql)
                return render_template("products2.html", data=data,data2=filtered_data)
            else:
                sql = f"SELECT * FROM products WHERE pcategory = '{category}'"
                filtered_data = fetchall(sql)  # Replace fetchall with your actual method
                return render_template("products2.html",data=data ,data2=filtered_data)

#SEARCHBAR AFTER LOGIN
@app.route("/searchbeforlogin", methods=["POST", "GET"])
def searchbeforlogin():
    if request.method == "POST":
        search_query = request.form["query"]
        print("hellobeforelogin", search_query)
        if search_query:
            search_query = search_query.lower()
            sql = f"SELECT * FROM products WHERE LOWER(pname) LIKE '{search_query}%'"
            filtered_data = fetchall(sql)
            print(filtered_data)
            return render_template("products.html", data2=filtered_data)
        else:
            sql = "select * from products"
            data2 = fetchall(sql)
            return render_template("products.html", data2=data2)

#FILTERBAR AFTER LOGIN
@app.route("/filterbeforlogin", methods=["POST","GET"])
def filterbeforlogin():
    if request.method=="POST":
        category = request.form["category"]
        if category =="All":
            sql="select * from products"
            filtered_data = fetchall(sql)
            return render_template("products.html", data2=filtered_data)
        else:
            sql = f"SELECT * FROM products WHERE pcategory = '{category}'"
            filtered_data = fetchall(sql)
            return render_template("products.html", data2=filtered_data)

#SHAPPING PAGE AFTER LOGIN
@app.route("/shoppingbag2")
def shoppingbag2():
    id = session['cusid']
    sql = "select * from customer where cusid like '%s'" % (id)
    data = fetchall(sql)
    data = data[0]
    sql = "Select * from products"
    data2 = fetchall(sql)
    #print("helo : ", id)
    cart_sql="SELECT cart.cart_id,cart.customer_id,products.pid,products.pname,products.price,products.image,cart.quantity FROM cart INNER JOIN customer ON cart.customer_id = customer.cusid INNER JOIN products ON cart.pid = products.pid WHERE cart.customer_id ='%s'"%(id)
    cart_data=fetchall(cart_sql)
    #print("Cart DATA:  ",cart_data)
    #print("Cart DATA length:  ", len(cart_data))
    total=0
    for x in cart_data:
        total+=int(x[4]*x[6])
    return render_template("products2.html", data=data,data2=data2,cart=cart_data,
                           total=total,length=len(cart_data))

#---------------------------SHOPPING END------------------------------#

#---------------------------TRENDS PAGE------------------------------#

#TRENDS URL
@app.route("/trends")
def trends():
    return render_template("trends.html")

#TRENDS AFTER LOGIN
@app.route("/trends2")
def trends2():
    id = session['cusid']
    sql = "select * from customer where cusid like '%s'" % (id)
    data = fetchall(sql)
    data = data[0]
    return render_template("trends2.html", data=data)

#---------------------------TRENDS END------------------------------#

#---------------------------MEDIA PAGE------------------------------#

#MEDIA URL
@app.route("/media")
def media():
    return render_template("media.html")
#MEDIA AFTER LOGIN
@app.route("/media2")
def media2():
    id = session['cusid']
    sql = "select * from customer where cusid like '%s'" % (id)
    data = fetchall(sql)
    data=data[0]
    return render_template("media2.html", data=data)


@app.route("/media_ext")
def media_ext():
    return render_template("media_ext.html")
@app.route("/media_ext_2")
def media_ext_2():
    id = session['cusid']
    sql = "select * from customer where cusid like '%s'" % (id)
    data = fetchall(sql)
    data = data[0]
    return render_template("media_ext_2.html", data=data)


@app.route("/media_ext2")
def media_ext2():
    return render_template("media_ext2.html")
@app.route("/media_ext2_2")
def media_ext2_2():
    id = session['cusid']
    sql = "select * from customer where cusid like '%s'" % (id)
    data = fetchall(sql)
    data = data[0]
    return render_template("media_ext2_2.html", data=data)

#---------------------------MEDIA END------------------------------#

#---------------------------ABOUT PAGE------------------------------#

#ABOUT URL
@app.route("/about")
def about():
    return render_template("About.html")
#ABOUT AFTER LOGIN
@app.route("/about2")
def about2():
    id = session['cusid']
    sql = "select * from customer where cusid like '%s'" % (id)
    data = fetchall(sql)
    data = data[0]
    return render_template("About2.html", data=data)

#---------------------------ABOUT END------------------------------#


#---------------------------LOOKBOOK PAGE------------------------------#

#LOOKBOOK URL
@app.route("/lookbook")
def lookbook():
    return render_template("lookbook.html")

#LOOKBOOK AFTER LOGIN
@app.route("/lookbook2")
def lookbook2():
    id = session['cusid']
    sql = "select * from customer where cusid like '%s'" % (id)
    data = fetchall(sql)
    data = data[0]
    return render_template("lookbook2.html", data=data)

#---------------------------LOOKBOOK END------------------------------#

#---------------------------BOTIQUE PAGE------------------------------#
#BOTIQUE
@app.route("/botique")
def botique():
    return render_template("botique.html")

#BOTIQUE AFTER LOGIN
@app.route("/botique2")
def botique2():
    id = session['cusid']
    sql = "select * from customer where cusid like '%s'" % (id)
    data = fetchall(sql)
    data = data[0]
    return render_template("botique2.html", data=data)
#---------------------------BOTIQUE END------------------------------#


#---------------------------RENTAL PAGE------------------------------#

#RENTAL
@app.route("/rental")
def rental():
    return render_template("rental.html")

#RENTAL AFTER LOGIN
@app.route("/rental2")
def rental2():
    id = session['cusid']
    sql = "select * from customer where cusid like '%s'" % (id)
    data = fetchall(sql)
    data = data[0]
    return render_template("rental2.html", data=data)

#---------------------------RENTAL END------------------------------#

#---------------------------CREATE PAGE------------------------------#

#CREATE URL
@app.route("/Create")
def Create():
    return render_template("Create.html")

#CREATE AFTER LOGIN
@app.route("/Create2")
def Create2():
    id = session['cusid']
    sql = "select * from customer where cusid like '%s'" % (id)
    data = fetchall(sql)
    data = data[0]
    return render_template("Create2.html", data=data)

#INSERT INTO THE SQL TABLE FOR CREATING APPOINTMENT
@app.route("/insert",methods=["POST","GET"])
def insert():
    print("hello create")
    if request.method=="POST":
        id=session['cusid']
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        city = request.form["city"]
        if 'sessiontype' in request.form:
            sessiontype = request.form["sessiontype"]
        else:
            sessiontype = "No session type selected"
        date = request.form["date"]
        print("hello create",name,email,phone,city,sessiontype,date)
        sql="insert into Create_appointment(cust_id,name,email,contactno,address,session,doa) values('%s','%s','%s','%s','%s','%s','%s')"%(id,name,email,phone,city,sessiontype,date)
        excuteupdate(sql)
    return redirect(url_for("Create2"))

#---------------------------CREATE------------------------------#

#---------------------------FORGET PASSWORD PAGE------------------------------#

#OTP GENERATING FUNCTION
def generate_otp(email):
    otp = pyotp.TOTP(pyotp.random_base32()).now()
    session['otp'] = otp
    return otp

#FUNCTION FOR SENDING OTP THROUGH EMAIL
def send_email(email, otp):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'tejteja54321@gmail.com'
    password = 'ukqm kjfe pwqi ojwx'
    msg = EmailMessage()
    msg.set_content(f'Your OTP is: {otp}')
    msg['Subject'] = 'YOUR OWN FASHION SENT AN OTP FOR VERIFICATION'
    msg['From'] = sender_email
    msg['To'] = email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {e}")

#URL FOR FORGET PASSWORD
@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    return render_template('forgot_password.html')

#URL FOR SENDING OTP THROUGH EMAIL
@app.route("/enter_email", methods=['GET', 'POST'])
def enter_email():
    if request.method == 'POST':
        email = request.form.get('email')
        sql="select * from customer where email like '%s'"%(email)
        data=fetchall(sql)
        if (data):
            data = data[0]
            print(data)
            session['email'] = data[2]
            otp = generate_otp(data[2])
            print(otp)
            send_email(data[2], otp)
            return redirect(url_for('enter_otp'))
        else:
            return render_template('forgot_password.html', error='Email not found')
    return render_template('forgot_password.html', error=None)

#URL FOR ENTERING OTP THAT HAS BEEN SENT
@app.route("/send_otp",methods=["POST","GET"])
def enter_otp():
    return render_template("enter_otp.html")

#URL FOR VERIFYING OTP THAT HAS BEEN SUBMITTED
@app.route("/verify_otp",methods=["POST","GET"])
def verify_otp():
    if 'email' not in session:
        return redirect(url_for('forgot_password'))
    if request.method == 'POST':
        entered_otp = request.form.get('otp')
        print(entered_otp)
        stored_otp = session.get('otp')
        print(stored_otp)
        if entered_otp == stored_otp:
            return redirect(url_for('reset_password'))
        else:
            return render_template('enter_otp.html', error='Invalid OTP')
    return render_template('enter_otp.html', error=None)

#URL FOR RESETTING PASSWORD
@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if 'email' not in session:
        return redirect(url_for('forgot_password'))

    if request.method == 'POST':
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')

        if new_password != confirm_password:
            return render_template('reset_password.html', error='Passwords do not match')
        email=session['email']
        sql="update customer set password = '%s' where email ='%s'"%(new_password,email)
        excuteupdate(sql)
        del session['email']
        return 'Password reset successful<a href="/">HOME</a>'

    return render_template('reset_password.html', error=None)

#---------------------------FORGET PASSWORD END------------------------------#

#---------------------------ADMIN PAGE------------------------------#

#URL FOR ADMIN LOGIN
@app.route("/adminlogin",methods=["POST","GET"])
def adminlogin():
    if request.method=="POST":
        aemail=request.form["aemail"]
        apswd = request.form["apassword"]
        if(aemail=="tejteja54321@gmail.com" and apswd=="teja531@SVC"):
            sql="select * from customer"
            data=fetchall(sql)
            sql2="select * from products"
            products=fetchall(sql2)
            #print(products)
            sql3="select * from cart"
            cart=fetchall(sql3)
            sql4="select * from payment"
            payment=fetchall(sql4)
            print(payment)
            sql5="select * from create_appointment"
            appointment=fetchall(sql5)
            return render_template("admin_login.html",data=aemail,data2=data,products=products,cart=cart,payment=payment,appointment=appointment)
    return render_template("project.html")


#URL FOR ADMIN TO ADD PRODUCTS
@app.route("/addProduct",methods=["POST","GET"])
def addProduct():
    msg=""
    if request.method=="POST":
        pid=request.form["productId"]
        pname = request.form["productName"]
        pcategory = request.form["productCategory"]
        pprice = request.form["productPrice"]
        pfile = request.files['productImage']
        pfile.save(os.path.join(app.config["upload_folder"], pfile.filename))

        sql = "select * from products where pid like '%s' or pname like '%s' " % (pid,pname)
        data = fetchall(sql)
        if (data):
            msg = "The product Name or Id is already existed use another Id or Name"
        else:
            sql = "insert into products (pid,pname,pcategory,price,image) values('%s','%s','%s','%s','%s')" % (
            pid, pname, pcategory, pprice, pfile.filename)
            excuteupdate(sql)
            msg = "Product inserted successfully"
    return render_template("admin_login.html",msg=msg)

#URL FOR ADMIN TO DELETE PRODUCT
@app.route("/deleteproduct",methods=["POST","GET"])
def deleteproduct():
    try:
        pid = request.args["pid"]
        pid=int(pid)
        if pid:
            remove_from_cart(pid)
            delete_from_products(pid)
        return redirect(url_for("adminlogin"))
    except Exception as e:
        print("Exception: ",e)
    return render_template("admin_login.html")

def remove_from_cart(pid):
    sql="delete from cart where pid='%s'" % (pid)
    excuteupdate(sql)
def delete_from_products(pid):
    sql = "delete from products where pid='%s'" % (pid)
    excuteupdate(sql)





#URL FOR UPDATE PRODUCT PRICES
@app.route("/updateprice", methods=["POST"])
def updateprice():
    try:
        productId = request.form.get("productId")
        updatedPrice = request.form.get("updatedPrice")
        print(updatedPrice,productId)
        sql = "update products set price ='%s' where pid='%s'" % (updatedPrice, productId)
        excuteupdate(sql)

        return redirect(url_for("updateprice"))

    except Exception as e:
        print("Exception:", e)
        return jsonify({"error": str(e)})

#---------------------------ADMIN PAGE END------------------------------#



#URL FOR ADDING ITEMS TO CART
@app.route("/addtocart", methods=["POST", "GET"])
def addtocart():
    pid = request.args["pid"]
    id = session['cusid']
    sql = "select email from customer where cusid=%s" % (id)
    email = fetchall(sql)
    print("cust_email : ", email[0][0])
    print("cust_id : ", id)
    print("product id : ", pid)


    conn = mysql.connector.connect(user='root', password='', host='localhost', database='yourown', port=3307)
    cursor = conn.cursor()

    sql2 = "select cart_id, pid, quantity from cart where customer_id = %s" % (id)
    cursor.execute(sql2)
    cart_data = cursor.fetchall()
    print("Particular person car data: ", cart_data)

    search_item = int(pid)
    itemid = None
    item_quant = None
    for item in cart_data:
        print(item)
        if search_item == item[1]:
            itemid = item[0]
            item_quant = item[2]
            break

    if itemid is not None:
        sql3 = "update cart set quantity= '%s' where cart_id= '%s' " % (int(item_quant) + 1, itemid)
        cursor.execute(sql3)
        conn.commit()
    else:
        sql4 = "insert into cart(customer_id, email, pid, quantity) values('%s', '%s', '%s', '%s')" % (
            id, email[0][0], pid, '1')
        cursor.execute(sql4)
        conn.commit()


    cursor.close()
    conn.close()

    return redirect(url_for("shoppingbag2"))

#URL TO REMOVE ITEM FROM CART
@app.route("/removefromcart", methods=["POST","GET"])
def removefromcart():
    pid = request.args["pid"]
    id = session['cusid']
    sql="select quantity from cart where pid like '%s' and customer_id like '%s'"%(pid,id)
    quantity=fetchall(sql)
    quantity=int(quantity[0][0])
    print(quantity)
    if quantity>1:
        sql="update cart set quantity = '%s' where pid like '%s' and customer_id like '%s' "%(quantity-1,pid,id)
        excuteupdate(sql)
    else:
        sql="delete from cart where pid like '%s' and customer_id like '%s' "%(pid,id)
        excuteupdate(sql)
    return redirect(url_for("shoppingbag2"))

#URL FOR PAYMENT PAGE
@app.route("/payment")
def payment():
    id = session['cusid']
    sql="SELECT cart.cart_id, cart.quantity, products.pname, products.price,cart.quantity FROM cart INNER JOIN products ON cart.pid = products.pid WHERE cart.customer_id = %s"%(id)
    data=fetchall(sql)
    #print("In Payment: ",data)
    total = 0
    for x in data:
        total += int(x[3] * x[4])

    return render_template("payment.html",data=data,total=total)

#URL FOR CHECKOUT PAGE
@app.route("/checkout",methods=["POST","GET"])
def checkout():
    if request.method == "POST":
        fullname = request.form.get('fullname')
        address = request.form.get('address')
        payment_method = request.form.get('paymentmethod')
        id = session['cusid']
        sql = ("SELECT cart.cart_id, cart.quantity, products.pname, products.price, "
               "cart.quantity FROM cart INNER JOIN products ON cart.pid = products.pid WHERE cart.customer_id = %s") % (
            id)
        data = fetchall(sql)
        print("In checkout: ", data)
        list_items = []
        total = 0
        quantity = 0
        for x in data:
            total += int(x[3] * x[4])
            list_items.append(x[2])
            quantity += x[1]
        paydate = datetime.datetime.now().strftime('%Y-%m-%d')  # Format date as string

        print(list_items, total, quantity, paydate)
        print(payment_method, paydate)
        items_string = '_'.join(list_items)
        print(fullname,address)

        sql2 = ("INSERT INTO payment(cust_id, noofitems, amount, method, paymentdate, "
                "products,fullname,address) VALUES ('%s', '%s', '%s', '%s', '%s', '%s','%s','%s')")
        values = (id, quantity, total, payment_method, paydate, items_string,fullname,address)
        sql_with_values = sql2 % values  # Concatenate SQL query and values

        print(sql_with_values)

        excuteupdate(sql_with_values)

        return render_template("checkout.html")


#AFTER LOGIN COMMON HEADER
@app.route("/userheader")
def userheader():
    id=session['cusid']
    sql="select * from cart where customer_id = '%s'"%(id)
    data=fetchall(sql)
    length=None
    if len(data)>0:
        length=len(data)
    else:
        length=0
    print(length)

    sql = "select * from customer where cusid like '%s'" % (id)
    data = fetchall(sql)
    data = data[0]

    sql = "Select * from products"
    data2 = fetchall(sql)
    print("helo : ", id)
    cart_sql = "SELECT cart.cart_id,cart.customer_id,products.pid,products.pname,products.price,products.image,cart.quantity FROM cart INNER JOIN customer ON cart.customer_id = customer.cusid INNER JOIN products ON cart.pid = products.pid WHERE cart.customer_id ='%s'" % (id)
    cart_data = fetchall(cart_sql)
    print("Cart DATA:  ",cart_data)
    print("Cart DATA length:  ", len(cart_data))

    total = 0
    for x in cart_data:
        total += int(x[4] * x[6])

    return render_template("/userheader.html", data=data, data2=data2, cart=cart_data,
                           total=total, length=length)

#URL FOR UPDATE QUANTITY OF ITEMS IN CART
@app.route("/update_quantity")
def update_quantity():
    if request.method == 'POST':
        print("hello i'm changing")
        product_id = request.form.get('product_id')
        new_quantity = request.form.get('new_quantity')
        id=session['cusid']
        sql="update cart set quantity='%s' where pid='%s' and customer_id='%s' "%(new_quantity,product_id,id)
        return redirect(url_for("shoppingbag2"))



if __name__ == '__main__':
    app.run(debug=True)