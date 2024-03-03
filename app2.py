from flask import Flask, render_template
import pymysql
import serial

app = Flask('__name__')
ser = serial.Serial('/dev/ttyACM0',115200)



@app.route('/')
def hello_world():
    return 'Hello World!'



#def get_table_data():
#    connection=pymysql.connect(host='localhost', user='root', password='1234', db='humididb', charset='utf8')
#    try :
#        with connection.cursor() as cursor:
#            cursor.execute("SELECT * FROM humi")
#            table_data=cursor.fetchall()
#            return table_data
#    finally:
#        conn.close()



def update_servo(a):
    connection=pymysql.connect(host='localhost', user='root', password='1234', db='servodb', charset='utf8')
    with connection.cursor() as cursor:
        cursor.execute("UPDATE servo SET angle" +a)
        connection.commit()
        connection.close()
         
@app.route('/cal')
def index2():
    return render_template("index2.html")

@app.route('/humidity')
def humidity():
    if(ser.isOpen()==False):
        ser.open()
    readline = ser.readline().decode('utf-8')
    
    data_list = []
    if "temperature" in readline and "humidity" in readline:
        datas = (readline.split(','))
        data_list.append(datas[0].split(':')[1])
        data_list.append(datas[1].split(':')[1])

    else:
        pass
    ser.close()

    return render_template("humidity.html", item=data_list)










@app.route('/humidity1')
def humidity_desc():
    item = get_humidity_data()
    return render_template("humidity.html", item=data_list)



@app.route('/servo')
def test():
    if(ser.isOpen()==False):
        ser.open()
    data = ser.readline().decode('utf-8')


    list=[]
    datas=data.split(',')
    list.append(datas[0])
    update_servo(datas[0])

    ser.close()

    return render_template("servo.html",item=list)



if __name__=='__main__':
    app.run(host='localhost',port=5023)

