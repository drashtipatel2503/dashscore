# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 09:35:56 2021

@author: DRASHTI
"""
from flask import send_file
import matplotlib.pyplot as plt
import io
import numpy as np
import numpy
import hashlib
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from flask import Flask, render_template,request, redirect, session, json, make_response

from flask_mysqldb import MySQL
import pickle

mysql=MySQL()
app=Flask(__name__)

app.config['MySQL_USER']='root'
app.config['MYSQL_PASSWORD']='drashti'
app.config['MYSQL_DB']='dashscore'
app.config['MYSQL_HOST']='localhost'

mysql.init_app(app)
app.secret_key=hashlib.sha1('abcdef'.encode()).hexdigest()
msg=""
model=pickle.load(open('feedbacklr.sav','rb')) 
@app.route('/')
def main():
    return render_template('home.html')
@app.route('/home')
def home():
    return render_template('home.html')
  

@app.route('/success')
def success():
    return render_template('dataadded.html')
   

'''
@app.route('/plot/temp')
def plot_temp():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)
    axis.set_title("Temperature [°C]")
    axis.set_xlabel("Samples")
    axis.grid(True)
    
    a=[5,4,5,3]
    b=[2001,2002,2003,2004]
    axis.plot(a, b)
        
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response

'''
@app.route('/plot/pvs')
def pvs():
    fig = Figure()
    hist = fig.add_subplot(1, 1, 1)
    hist.set_title("Production - Sales")
    hist.set_xlabel("Months")
    
    #hist.grid(True)
    
    a=session['p']
    
    b=['jan','feb','mar','apr','may','jun','july','aug','sep','oct','nov', 'dec']
    hist.plot(b,a)
    c=session['s']
    hist.plot(b,c, color="green")
    hist.legend(labels=('production','sales'), loc='upper right')
        
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response



@app.route('/plot/pvt')
def pvt():
    fig = Figure()
    hist = fig.add_subplot(1, 1, 1)
    hist.set_title("Production - Sales")
    hist.set_xlabel("Months")
    
    #hist.grid(True)
    
    a=session['p']
    
    b=['jan','feb','mar','apr','may','jun','july','aug','sep','oct','nov', 'dec']
    hist.plot(b,a)
    c=session['t']
    hist.plot(b,c, color="cyan")
    hist.legend(labels=('production','sales'), loc='upper right')
        
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response



@app.route('/plot/nc')
def nc():
    fig = Figure()
    plt = fig.add_subplot(1, 1, 1)
    plt.set_title("Expenditure Distribution")
    plt.set_xlabel("Worth")
    
    c=session['nc']
    X=np.array(4)
    w=0.25
    
    b=['raw goods', 'hr', 'tax', 'marketing', 'techn-cost']
    
    
    plt.pie(c,labels=b)
        
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response
@app.route('/plot/b')
def b():
    fig = Figure()
    plt = fig.add_subplot(1, 1, 1)
    plt.set_title("Allocated budget")
    
    c=session['e']
    X=np.array(4)
    w=0.25
    
    b=['raw goods', 'hr', 'tax', 'marketing', 'techn-cost']
    
    
    plt.pie(c,labels=b)
        
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response
@app.route('/plot/csl')
def csl():
    fig = Figure()
    plt = fig.add_subplot(1, 1, 1)
    plt.set_title("Allocated budget")
    
    c=session['cs']
    X=np.array(4)
    w=0.25
    
    b=['satisfied customers' , 'unsatisfied']
    
    
    plt.bar(b,c, color="green", width=0.1)
        
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response

@app.route('/plot/eb')
def eb():
    fig = Figure()
    plt = fig.add_subplot(1, 1, 1)
    plt.set_title("Expenditure - allocation")
    plt.set_xlabel("Worth")
    a=session['e']
    c=session['nc']
    a=np.arange(len(a))
    w=0.25
    c=[x + w for x in a]
    print(c)
    print(a)
    b=['raw goods', 'hr', 'tax', 'marketing', 'techn-cost']
    
    plt.barh(b,a, color="yellow", height=0.25)
    
   
    plt.barh(b,c, color="green", height=0.25)
        
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response
@app.route('/plot/eb1')
def eb1():
    fig = Figure()
    plt=fig.subplots()
    #plt = fig.add_subplot(1, 1, 1)
    plt.set_title("Expenditure - allocation")
    plt.set_xlabel("Worth")
    a=session['e']
    c=session['nc']
    a=np.arange(len(a))
    w=0.25
    c=[x + w for x in a]
    print(c)
    print(a)
    b=['raw goods', 'hr', 'tax', 'marketing', 'techn-cost']
    b1=np.arange(len(a))
    b2=[x + w for x in b1]
    plt.bar(b1,a, color="yellow", width=0.25, label="allocation")
    
   
    plt.bar(b2,c,  color="green", width=0.25, label="expenditure")
        
    canvas = FigureCanvas(fig)
    output = io.BytesIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response

@app.route('/setsale')
def setsale():
    return render_template('setsale.html')

@app.route('/generatereport')
def generatereport():
        try:
        
        id1=session['id']
        
        budget=session['budget']
        exp=session['exp']
       
        cur=mysql.connection.cursor()
        cur.execute("Select * from review where `id` like %s",[id1])
        cr=cur.fetchone()
        cr=list(cr)
        session['cs']=cr[1:]
        cr=cr[1]
        
        cur.execute("Select * from sales where `id` like %s",[id1])
        #s=list(s)
        s=cur.fetchone()
        s=list(s)
        s=s[1:]
        ys=sum(s)
        session['s']=s
        
        
        cur.execute("Select * from targets where `id` like %s",[id1])
    
        s=cur.fetchone()
        s=list(s)
        s=s[1:-1]
        ys=sum(s)
        session['t']=s
        
        cur.execute("Select * from production where `id` like %s",[id1])
        #s=list(s)
        s=cur.fetchone()
        s=list(s)
        p=s[1:]
        yp=sum(p)
        session['p']=p
        
        cur.execute("Select * from estimate where `id` like %s",[id1])
    
        s=cur.fetchone()
        s=list(s)
        e=s[1:]
        budget=sum(e)
        session['e']=e
        
        
        cur.execute("Select * from netcost where `id` like %s",[id1])
    
        s=cur.fetchone()
        s=list(s)
        nc=s[1:]
        exp=sum(nc)
        session['nc']=nc
        
    
        return render_template('report.html',yp=yp, ys=ys, exp=exp, budget=budget, cs=cr)
    except:
        return render_template('alldetail.html')
        
        
        
        
@app.route('/settarget')
def settarget():
    return render_template('settarget.html')
@app.route('/enterprise')
def enterprise():
    name=session['name']
    return render_template('enterprise.html', name=name)

@app.route('/estimatesale')
def estimatesale():
    return render_template('estimatesale.html')


@app.route('/manageresource')
def manageresource():
    return render_template('manageresource.html')

@app.route('/viewsale')
def viewsale():
    return render_template('viewsale.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')
@app.route('/setbudget')
def setbudget():
    return render_template('setbudget.html')
@app.route('/addnetcost')
def addnetcost():
    return render_template('addnetcost.html')
 
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/reviewed')
def reviewed():
    return render_template('reviewed.html')
@app.route('/feeddetail', methods=["POST"])
def feeddetail():
    a=request.form["rnr"]
    id1=session['id']
    
    p=model.predict([a])
    print(p)
    if p==1:
        msg="Customer is satisfied...Cheers!!"
        icon="thumbs-up"
        cur=mysql.connection.cursor()
        cur.execute("Update review SET pos = pos +1 where id Like %s",[id1])
        mysql.connection.commit()
        cur.close()
                
    else:
        msg="Li'll disatisfaction"
        icon="thumbs-down"
        cur=mysql.connection.cursor()
            
        cur.execute("UPDATE review SET neg=neg+1 where id Like %s",[id1])
        mysql.connection.commit()
        cur.close()
    return render_template('reviewed.html', ans=msg, icon=icon)
    

@app.route('/registeruser', methods=["POST"])
def registeruser():
    
        name=request.form["name"]
        password=request.form["password"]
        
        cpassword=request.form["cpassword"]
        email=request.form["email"]
    
        
        session['name']=name 
        location=request.form["location"]
        
        if cpassword==password:
            cur=mysql.connection.cursor()
            
            
            cur.execute("SELECT * from user WHERE `email` LIKE %s",[email])
            q=cur.fetchall()
            if len(q)>0:
               return  render_template('register.html', msg="Email already registered")
                
            else:  
                    
                cur.execute("Insert into user (`name`, `email`, `password`, `location`) values(%s, %s, %s,%s)", (name, email, password,location));
                p=cur.lastrowid
                session['id']=p 
                a=0
                cur.execute("Insert into review (`id`, `pos`, `neg`) value (%s,%s, %s)",(p,a,a))
                mysql.connection.commit()
                cur.close()
                return redirect('enterprise')
        else:
            msg="Password and Confirm Password does not match"
            return render_template('register.html' , msg=msg)
                  

@app.route('/loginuser', methods=["POST"])
def loginuser():
        password=request.form["password"]
       
        email=request.form["email"]
        cur=mysql.connection.cursor()
        
        
        cur.execute("SELECT * from user WHERE `email` LIKE %s",[email])
        q=cur.fetchone()
        if q!=0:
    
            if (q[4])==password:
                print(q)
                session['id']=q[0]
                session['name']=q[1]
                name=q[1]
                print(name)
                cur.close()
                return render_template('enterprise.html', name=name)
            else:
                cur.close()
                msg="Please try again"
                return render_template('login.html', msg=msg)
        else:
            msg="This Id is not registered"
            return render_template('login.html', msg=msg)
        

@app.route('/settargetdetails', methods=["POST"])
def settargetdetails():
                
                yp=request.form["yp"]
                jan=request.form["jan"]
                feb=request.form["feb"]
                mar=request.form["mar"]
                apr=request.form["apr"]
                may=request.form["may"]
                jun=request.form["jun"]
                jul=request.form["jul"]
                aug=request.form["aug"]
                sep=request.form["sep"]
                oct1=request.form["oct"]
                nov=request.form["nov"]
                dc=request.form["dec"]
                id1=session['id']
                
                cur=mysql.connection.cursor()
                
                
                cur.execute("SELECT * from targets WHERE `id` LIKE %s",[id1])
                
                q=cur.fetchall()
                if q!=0:
                    
                    cur.execute("DELETE * from targets WHERE `id` LIKE %s",[id1])
                    mysql.connection.commit()
                    cur.close()
                
                cur=mysql.connection.cursor()
             
                        
                cur.execute("Insert into targets (`id`, `jan`, `feb`, `mar`, `apr`, `may`, `jun`, `jul`, `aug`, `sep`, `oct`, `nov`, `dec`, `yearly_production`) values(%s, %s, %s,%s,%s, %s, %s,%s,%s, %s, %s,%s,%s,%s)", (id1,jan,feb,mar,apr,may,jun,jul,aug,sep,oct1,nov,dc,yp));
                mysql.connection.commit()
                cur.close()
                return redirect('success')


@app.route('/setbudgetdetails', methods=["POST"])
def setbudgetdetails():
                id1=session['id']
                rm=request.form['rm']
                hr=request.form['hr']
                market=request.form['market']
                techcost=request.form['techcost']
                tax=request.form['tax']
                session['budget']=float(rm)+float(hr)+float(market)+float(tax)+float(techcost)
                cur=mysql.connection.cursor()
             
                        
                cur.execute("Insert into estimate (`id`, `rawmaterial`, `hr`, `tax`, `marketing`, `techcost`) values( %s, %s,%s,%s,%s,%s)", (id1,rm,hr,tax,market,techcost));
                mysql.connection.commit()
                cur.close()
                return redirect('success')
@app.route('/addnetcostdetails', methods=["POST"])
def addnetcostdetails():
                id1=session['id']
                rm=request.form['rm']
                hr=request.form['hr']
                market=request.form['market']
                techcost=request.form['techcost']
                tax=request.form['tax']
                
                session['exp']=float(rm)+float(hr)+float(market)+float(tax)+float(techcost)
                cur=mysql.connection.cursor()
             
                        
                cur.execute("Insert into netcost (`id`, `rawmaterial`, `hr`, `tax`, `marketing`, `techcost`) values( %s, %s,%s,%s,%s,%s)", (id1,rm,hr,tax,market,techcost));
                mysql.connection.commit()
                cur.close()
                return redirect('success')
     
@app.route('/setsaledetails', methods=["POST"])
def setsaledetails():
                yp=request.form["yp"]
                
                
                ys=request.form["ys"]
                
                jan=request.form["janp"]
                feb=request.form["febp"]
                mar=request.form["marp"]
                apr=request.form["aprp"]
                may=request.form["mayp"]
                jun=request.form["junp"]
                jul=request.form["julp"]
                aug=request.form["augp"]
                sep=request.form["sepp"]
                oct1=request.form["octp"]
                nov=request.form["novp"]
                dc=request.form["decp"]
                id1=session['id']
                session['yp']=jan+feb+mar+apr+may+jun+jul+aug+sep+oct1+nov+dc
                
                cur=mysql.connection.cursor()
                
                
                
                cur.execute("SELECT * from production WHERE `id` LIKE %s",[id1])
                
                q=cur.fetchall()
                if q!=0:
                    
                    cur.execute("DELETE * from production WHERE `id` LIKE %s",[id1])
                    mysql.connection.commit()
                    cur.close()
                
                cur=mysql.connection.cursor()       
                cur.execute("Insert into production (`id`, `jan`, `feb`, `mar`, `apr`, `may`, `jun`, `jul`, `aug`, `sep`, `oct`, `nov`, `decm` ) values(%s, %s, %s,%s,%s, %s, %s,%s,%s, %s, %s,%s,%s)", (id1,jan,feb,mar,apr,may,jun,jul,aug,sep,oct1,nov,dc));
                mysql.connection.commit()
                cur.close()

                jan=request.form["jans"]
                feb=request.form["febs"]
                mar=request.form["mars"]
                apr=request.form["aprs"]
                may=request.form["mays"]
                jun=request.form["juns"]
                jul=request.form["juls"]
                aug=request.form["augs"]
                sep=request.form["seps"]
                oct1=request.form["octs"]
                nov=request.form["novs"]
                dc=request.form["decs"]
                id1=session['id']
                
                session['ys']=jan+feb+mar+apr+may+jun+jul+aug+sep+oct1+nov+dc
                cur=mysql.connection.cursor()
                
                
                
                cur.execute("SELECT * from sales WHERE `id` LIKE %s",[id1])
                
                q=cur.fetchall()
                if q!=0:
                    
                    cur.execute("DELETE * from sales WHERE `id` LIKE %s",[id1])
                    mysql.connection.commit()
                    cur.close()
                
                
                cur=mysql.connection.cursor()
             
                        
                cur.execute("Insert into sales (`id`, `jan`, `feb`, `mar`, `apr`, `may`, `jun`, `jul`, `aug`, `sep`, `oct`, `nov`, `decm`) values(%s, %s, %s,%s,%s, %s, %s,%s,%s, %s, %s,%s,%s)", (id1,jan,feb,mar,apr,may,jun,jul,aug,sep,oct1,nov,dc));
                mysql.connection.commit()
                cur.close()


                return redirect('success')
    
    
if __name__=='__main__':
    app.run(debug=False)
    
 