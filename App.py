from flask import Flask, render_template, flash, request, session

import mysql.connector
import sys

app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route("/")
def homepage():

    return render_template('index.html')


@app.route("/Home")
def Home():
    return render_template('index.html')


@app.route("/AdminLogin")
def DoctorLogin():
    return render_template('AdminLogin.html')


@app.route("/NewEmployee")
def NewEmployee():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM employeetb ")
    data = cur.fetchall()
    return render_template('NewEmployee.html', data=data)


@app.route("/EmployeeLogin")
def EmployeeLogin():
    return render_template('EmployeeLogin.html')


@app.route("/UserLogin")
def UserLogin():
    return render_template('UserLogin.html')


@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')


@app.route("/NewProduct")
def NewProduct():
    return render_template('NewProduct.html')


@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb  ")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)


@app.route("/AProductInfo")
def AProductInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM packagetb   ")
    data = cur.fetchall()

    return render_template('AProductInfo.html', data=data)





@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        if request.form['uname'] == 'admin' or request.form['password'] == 'admin':

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb ")
            data = cur.fetchall()
            flash("Login successfully")
            return render_template('AdminHome.html', data=data)

        else:
            flash("UserName Or Password Incorrect!")
            return render_template('AdminLogin.html')


@app.route("/newemp", methods=['GET', 'POST'])
def newemp():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        mobile = request.form['mobile']

        email = request.form['email']

        address = request.form['address']

        uname = request.form['uname']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO employeetb VALUES ('" + name + "','" + email + "','" + mobile + "','" + address + "','" + uname + "','" + password + "','" + gender + "')")
        conn.commit()
        conn.close()
        flash('Employee Info Register Successfully')

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        # cursor = conn.cursor()
        cur = conn.cursor()
        cur.execute("SELECT * FROM employeetb ")
        data = cur.fetchall()
        return render_template('NewEmployee.html', data=data)


@app.route("/RARemove")
def RARemove():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cursor = conn.cursor()
    cursor.execute(
        "delete from roomtb where id='" + id + "'")
    conn.commit()
    conn.close()

    flash('Room  info Remove Successfully!')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM roomtb  ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb  ")
    data1 = cur.fetchall()

    return render_template('AProductInfo.html', data=data, data1=data1)

@app.route("/FARemove")
def FARemove():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cursor = conn.cursor()
    cursor.execute(
        "delete from protb where id='" + id + "'")
    conn.commit()
    conn.close()

    flash('Food  info Remove Successfully!')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM roomtb  ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb  ")
    data1 = cur.fetchall()


    return render_template('AProductInfo.html', data=data,data1=data1)




@app.route("/emplogin", methods=['GET', 'POST'])
def emplogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['ename'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from employeetb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('EmployeeLogin.html', data=data)
        else:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
            cur = conn.cursor()
            cur.execute("SELECT * FROM employeetb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()
            flash("Login successfully")
            return render_template('EmployeeHome.html', data=data)


@app.route("/EmployeeHome")
def EmployeeHome():
    username = session['ename']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM employeetb where username='" + username + "' ")
    data = cur.fetchall()
    return render_template('EmployeeHome.html', data=data)


@app.route("/NewRoom")
def NewRoom():
    return render_template('NewRoom.html')



@app.route("/newroom", methods=['GET', 'POST'])
def newroom():
    if request.method == 'POST':
        PackageName = request.form['PackageName']
        ptype = request.form['ptype']
        price = request.form['price']
        mperson = request.form['mperson']
        info = request.form['info']
        Source   = request.form['Source']
        Destination = request.form['Destination']

        import random
        file = request.files['file']
        fnew = random.randint(1111, 9999)
        savename = str(fnew) + ".png"
        file.save("static/upload/" + savename)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO  packagetb VALUES ('','" + PackageName + "','" + ptype + "','" + price + "','"+ mperson +"','" +
            info + "','" + savename + "','"+ Source +"','"+  Destination +"')")
        conn.commit()
        conn.close()

    flash('Package Info Register successfully')
    return render_template('NewRoom.html')






@app.route("/Remove")
def Remove():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cursor = conn.cursor()
    cursor.execute(
        "delete from protb where id='" + id + "'")
    conn.commit()
    conn.close()

    flash('Product  info Remove Successfully!')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb  ")
    data = cur.fetchall()
    return render_template('EProductInfo.html', data=data)


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        mobile = request.form['mobile']

        email = request.form['email']

        address = request.form['address']

        uname = request.form['uname']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO regtb VALUES ('" + name + "','" + email + "','" + mobile + "','" + address + "','" + uname + "','" + password + "','" + gender + "')")
        conn.commit()
        conn.close()
        flash('User Register successfully')

    return render_template('UserLogin.html')


@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('UserLogin.html')
        else:

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()
            flash("Login successfully")

            return render_template('UserHome.html', data=data)


@app.route("/Search")
def Search():
    import datetime
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    print(date)
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb ")
    data = cur.fetchall()

    return render_template('Search.html', data=data)

@app.route("/SearchRoom")
def SearchRoom():
    import datetime
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    print(date)
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM roomtb ")
    data = cur.fetchall()
    return render_template('SearchRoom.html', data=data)



@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        ptype = request.form['ptype']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM protb where  ProductType ='" + ptype + "'")
        data = cur.fetchall()
        return render_template('Search.html', data=data)


@app.route("/rsearch", methods=['GET', 'POST'])
def rsearch():
    if request.method == 'POST':
        ptype = request.form['ptype']
        import datetime

        date = datetime.datetime.now().strftime('%Y-%m-%d')
        print(date)
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM roomtb  where  RoomType ='" + ptype + "'")
        data = cur.fetchall()

        return render_template('SearchRoom.html', data=data)


@app.route("/search1", methods=['GET', 'POST'])
def search1():
    if request.method == 'POST':
        ptype = request.form['ptype']
        import datetime

        date = datetime.datetime.now().strftime('%Y-%m-%d')
        print(date)
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM protb where  ProductType ='" + ptype + "'")
        data = cur.fetchall()

        return render_template('index.html', data=data)


@app.route("/UserHome")
def UserHome():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM  regtb where username='" + uname + "'  ")
    data = cur.fetchall()

    return render_template('UserHome.html', data=data)


@app.route("/Add")
def Add():
    id = request.args.get('id')
    session['pid'] = id
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb  where id='" + id + "' ")
    data = cur.fetchall()
    return render_template('AddCart.html', data=data)


@app.route("/Add1")
def Add1():
    id = request.args.get('id')
    session['pid'] = id
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM roomtb  where id='" + id + "' ")
    data = cur.fetchall()
    return render_template('RoomBook.html', data=data)

@app.route("/add")
def add():
    flash('Please Login!')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb   ")
    data = cur.fetchall()
    return render_template('index.html', data=data)


@app.route("/addcart", methods=['GET', 'POST'])
def addcart():
    if request.method == 'POST':
        import datetime
        date = request.form['Date']
        pid = session['pid']
        uname = session['uname']
        qty = request.form['qty']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM protb  where  id='" + pid + "'")
        data = cursor.fetchone()

        if data:
            ProductName = data[1]
            Producttype = data[2]
            price = data[3]


            Image = data[5]

        else:
            return 'No Record Found!'


        payamt = float(qty) + float(price)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO carttb VALUES ('','" + uname + "','" + ProductName + "','" + Producttype + "','" + str(
                price) + "','" + str(qty) + "','" + str(payamt) + "','" +
            Image + "','" + date + "','0','')")
        conn.commit()
        conn.close()

        flash('Add To Cart  Successfully')

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM protb  where id='" + pid + "' ")
        data = cur.fetchall()
        return render_template('AddCart.html', data=data)




@app.route("/addcart1", methods=['GET', 'POST'])
def addcart1():
    if request.method == 'POST':
        import datetime
        date = request.form['Date']
        pid = session['pid']
        uname = session['uname']
        cname = request.form['cname']
        cno = request.form['cno']


        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM roomtb  where  id='" + pid + "'")
        data = cursor.fetchone()

        if data:
            ProductName = data[1]
            Producttype = data[2]
            price = data[3]


            Image = data[6]

        else:
            return 'No Record Found!'




        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO roombooktb VALUES ('','" + uname + "','" + ProductName + "','" + Producttype + "','" + str(
                price) + "','" +
            Image + "','" + date + "','"+ cname +"','"+ cno +"')")
        conn.commit()
        conn.close()

        flash('Room  Book   Successfully')

        return render_template('RoomBook.html')




@app.route("/Cart")
def Cart():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  carttb where UserName='" + uname + "' and Status='0' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT  sum(Qty) as qty ,sum(Tprice) as Tprice   FROM  carttb where UserName='" + uname + "' and Status='0' ")
    data1 = cursor.fetchone()
    if data1:
        tqty = data1[0]
        tprice = data1[1]
    else:
        return 'No Record Found!'

    return render_template('Cart.html', data=data, tqty=tqty, tprice=tprice)


@app.route("/RemoveCart")
def RemoveCart():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM carttb  where  id='" + id + "'")
    data1 = cursor.fetchone()

    if data1:
        ProductName = data1[2]
        cQty1 = data1[5]

    else:
        return 'No Record Found!'

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM protb  where  ProductName='" + ProductName + "'")
    data2 = cursor.fetchone()

    if data2:
        cQty = data2[4]

    else:
        return 'No Record Found!'

    total = float(cQty1) + float(cQty)

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cursor = conn.cursor()
    cursor.execute(
        "update protb set Qty='" + str(total) + "' where  ProductName='" + ProductName + "' ")
    conn.commit()
    conn.close()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cursor = conn.cursor()
    cursor.execute(
        "delete from carttb where id='" + id + "'")
    conn.commit()
    conn.close()

    flash('Product Remove Successfully!')

    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  carttb where UserName='" + uname + "' and Status='0' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT  sum(Qty) as qty ,sum(Tprice) as Tprice   FROM  carttb where UserName='" + uname + "' and Status='0' ")
    data1 = cursor.fetchone()
    if data1:
        tqty = data1[0]
        tprice = data1[1]

    return render_template('Cart.html', data=data, tqty=tqty, tprice=tprice)


@app.route("/payment", methods=['GET', 'POST'])
def payment():
    if request.method == 'POST':
        import datetime
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        uname = session['uname']
        cname = request.form['cname']
        Cardno = request.form['cno']
        Cvno = request.form['cvno']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT  sum(Qty) as qty ,sum(Tprice) as Tprice   FROM  carttb where UserName='" + uname + "' and Status='0' ")
        data1 = cursor.fetchone()
        if data1:
            tqty = data1[0]
            tprice = data1[1]

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        cursor = conn.cursor()
        cursor.execute(
            "SELECT  count(*) As count  FROM booktb ")
        data = cursor.fetchone()
        if data:
            bookno = data[0]
            print(bookno)

            if bookno == 'Null' or bookno == 0:
                bookno = 1
            else:
                bookno += 1

        else:
            return 'Incorrect username / password !'

        bookno = 'BOOKID' + str(bookno)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        cursor = conn.cursor()
        cursor.execute(
            "update   carttb set status='1',Bookid='" + bookno + "' where UserName='" + uname + "' and Status='0' ")
        conn.commit()
        conn.close()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO booktb VALUES ('','" + uname + "','" + bookno + "','" + str(tqty) + "','" + str(
                tprice) + "','" + cname + "','" + Cardno + "','" + Cvno + "','" + date + "')")
        conn.commit()
        conn.close()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  carttb where UserName='" + uname + "' and Status='1' ")
        data1 = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  booktb where username='" + uname + "'")
        data2 = cur.fetchall()

    return render_template('UserBook.html', data1=data1, data2=data2)


@app.route("/BookInfo")
def BookInfo():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  carttb where UserName='" + uname + "' and Status='1' ")
    data1 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  booktb where username='" + uname + "'")
    data2 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  roombooktb where username='" + uname + "'")
    data3 = cur.fetchall()


    return render_template('UserBook.html', data1=data1, data2=data2,data3 =data3)


@app.route("/ASalesInfo")
def ASalesInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  carttb where Status='1' ")
    data1 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  booktb ")
    data2 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT distinct username FROM  booktb ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  roombooktb ")
    data3 = cur.fetchall()

    return render_template('ASalesInfo.html', data1=data1, data2=data2, data=data,data3=data3)


@app.route("/ESalesInfo")
def ESalesInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  carttb where  Status='1' ")
    data1 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  booktb")
    data2 = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  roombooktb")
    data3 = cur.fetchall()



    return render_template('ESalesInfo.html', data1=data1, data2=data2,data3=data3)


@app.route("/asale", methods=['GET', 'POST'])
def asale():
    if request.method == 'POST':
        uname = request.form['username']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  carttb where UserName='" + uname + "' and Status='1' ")
        data1 = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  booktb where username='" + uname + "'")
        data2 = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        cur = conn.cursor()
        cur.execute("SELECT distinct username FROM  booktb ")
        data = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  roombooktb where username='" + uname + "' ")
        data3 = cur.fetchall()

        return render_template('ASalesInfo.html', data1=data1, data2=data2, data=data,data3=data3)


@app.route("/Update")
def Update():
    uid = request.args.get('uid')
    session["uid"] = uid

    return render_template('Update.html')


@app.route("/update", methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        price = request.form['price']
        Qty = request.form['qty']
        date = request.form['date']
        mdate = request.form['date']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2traveldbpy')
        cursor = conn.cursor()
        cursor.execute(
            "update protb set price='" + price + "',Qty='" + Qty + "',exdate='" + date + "',Mdate ='" + mdate + "' where id='" +
            session[
                'uid'] + "' ")
        conn.commit()
        conn.close()

        flash('Product Info Update')

        return render_template('AProductInfo.html')
def sendmsg(Mailid, message):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders

    fromaddr = "sampletest685@gmail.com"
    toaddr = Mailid

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Alert"

    # string to store the body of the mail
    body = message

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "hneucvnontsuwgpj")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
