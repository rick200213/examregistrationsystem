from flask import Flask,render_template,request,redirect
import pymysql,re
sign=Flask(__name__)
@sign.route('/')
def initialfuction():
    return render_template('signin.html')
@sign.route('/<string:page_request>')
def pagerequest(page_request):
    return render_template(page_request)
@sign.route('/submit_form',methods=['POST','GET'])
def signup():
    if request.method=='POST':
        data=request.form.to_dict()
        print(data)
        name=data["name"]
        email=data["email"]
        username=data["username"]
        password=data["password"]
        print(data)
        try:
           #Connect to MySQL database
           con = pymysql.connect(host='localhost', user='root', passwd='Account1start', database='webdevsignup')
           print('connection sucessful')
           cur=con.cursor()
           str="insert into users values('%s','%s','%s','%s')"
           args=(name,email,username,password)
           cur.execute(str%args)
           con.commit()
           print('1 row inserted')
        except:
            print('Insertion Failed')
            con.rollback()
        finally:
            cur.close()
            con.close()
        return redirect('/')
    else:
        return "Something went wrong"
@sign.route('/login_form',methods=['POST','GET'])
def login():
    name=None
    if request.method=='POST':
        data=request.form.to_dict()
        print(data)
        username = data["username"]
        password = data["password"]
        print(data)
        try:
           #Connect to MySQL database
           con = pymysql.connect(host='localhost', user='root', passwd='Account1start', database='webdevsignup')
           print('connection sucessful')
           result = re.match(r'\S+@\S+', username)
           print(result)
           cur=con.cursor()
           if result is None:
               str="select username from users where username='%s' and password='%s'"
           else:
               str = "select username from users where email='%s' and password='%s'"
           args=(username,password)
           cur.execute(str%args)
           n=cur.fetchone()

           if n is None:
               return "User Id or passWord invalid"

           print(n)
        except:
            print('Insertion Failed')
            con.rollback()
        finally:
            cur.close()
            con.close()
        return render_template('home.html',name=n[0])
    else:
        return "Something went wrong"
@sign.route('/registration',methods=['POST','GET'])
def registration():
    if request.method=='POST':
        data=request.form.to_dict()
        name=request.form.get('name')
        midname=request.form.get('middlename')
        lastname =request.form.get('lastname')
        dob=request.form.get('dob')
        fathername=request.form.get('fname')
        mothername=request.form.get('mname')
        gender=request.form.get('gender')
        apply=request.form.getlist('apply')
        schoolname=request.form.get('school')
        address=request.form.get('address')
        city=request.form.get('city')
        state=request.form.get('state')
        pincode=request.form.get('pincode')
        print(data)
        print(name)
        print(gender)
        print(apply[0])
        print(pincode)
        try:
           #Connect to MySQL database
           con = pymysql.connect(host='localhost', user='root', passwd='Account1start', database='webdevsignup')
           print('connection sucessful')
           cur=con.cursor()
           str="insert into student1 values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
           args=(name,midname,lastname,dob,fathername,mothername,gender,apply[0],apply[1],schoolname,address,city,state,pincode)
           cur.execute(str%args)
           con.commit()
           print('1 row inserted')
        except:
            print('Insertion Failed')
            con.rollback()
        finally:
            cur.close()
            con.close()

        return redirect('/')
    else:
        return "Something went wrong"

@sign.route('/genadmit',methods=['POST','GET'])
def genadmit():
    fathername=request.form.get('fathername')
    con = pymysql.connect(host='localhost', user='root', passwd='Account1start', database='webdevsignup')
    cur=con.cursor()
    str="select * from student1 where fathername='%s'"
    args=(fathername)

    cur.execute(str%args)
    data=cur.fetchone()
    print(data)
    return render_template('admitcard.html',student=data)


