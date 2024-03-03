from flask import Flask, render_template
import serial

app = Flask(__name__)
ser = serial.Serial('/dev/ttyACM0',115200)

@app.route('/1')
def hello():
    return 'Hello!'

@app.route('/2')
def calender():
    return render_template("calender.html")


@app.route('/humi')
def humidity():
    if(ser.isOpen()==False):
        ser.open()
    readline = ser.readline().decode('utf-8')
    
    data_list = []
    if "Temperature" in readline and "Humidity" in readline:
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




if __name__ == '__main__':
    app.run(host='localhost',port=5013)
