from flask import Flask, render_template, request

import csv
import matplotlib.pyplot as plt
import time


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Loginf1.html')


@app.route('/submit', methods=['POST'])
def save_data():
    data1 = request.form['name']
    data2 = request.form['email']
    data3 = request.form['mobile']
    data4 = request.form['dob']
    data5 = request.form['department']
    data6 = request.form['address']
    data7 = request.form['pincode']
    data8 = request.form['country']
    with open('data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([data1, data2, data3, data4, data5, data6, data7, data8])
    return render_template('success.html')


@app.route('/chart')
def pie_chart():
    # Read csv file and extract 5th column data
    fifth_col = ['computer','civil','mechanical','chemical']
    with open('data.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            fifth_col.append(row[4])
    # Calculate count of unique values
    unique_vals = list(set(fifth_col))
    counts = [fifth_col.count(val) for val in unique_vals]
    # Plot pie chart
    plt.pie(counts, labels=unique_vals, autopct='%1.1f%%')
    plt.title('Pie Chart of Department')
    plt.savefig('static/pie_chart.png')
    # Render HTML template with pie chart image
    return render_template('pie_chart.html')


@app.route('/faq')
def faq():
    return render_template('faq.html')
def chatbot_response(message):
    var_time = time.ctime()
    qna = {
        "Hi" : "Hello",
        "hi" : "Hello",
        "Hello" : "Hi",
        "hello" : "Hi",
        "Hey" : "wassup",
        "hey" : "wassup",
        "what is your name" : "My name is ChatBot",
        "What is your name" : "My name is ChatBot",
        "How are you doing" : "I am doing well, thank you for asking.",
        "What can you do" : "I can answer questions, provide information, and assist with various tasks." ,
        "Can you tell me a joke" : "Why did the tomato turn red? Because it saw the salad dressing!" ,
        "What's your favorite color" : "I don't have eyes, so I can't see colors. But I guess I'll go with binary code - 0's and 1's are pretty cool." ,
        "Do you have any siblings" : "Well, I was created by a team of programmers, so I guess you could say I have a lot of siblings. But we don't really keep in touch." ,
        "What's your favorite movie" : "I don't really have a favorite movie, but I do enjoy watching 'The Matrix' and 'Terminator'. They give me some good ideas." ,
        "1" : "2" ,
        "1" : "2" ,
        "1" : "2" ,
        "how are you" : "I'am Fine, what about you",
        "How are you" : "I'am Fine, what about you",
        "I am fine" : "Ok",
        "i am fine" : "Ok",
        "Fine" : "Ok",
        "fine" : "Ok",
        "what is the time now" : var_time,
        "Bye" : "See you later",
        "bye" : "See you later",
        "ok" : "See you later",
        "Ok" : "See you later",
        "what is this website about" : "This is a Cricket Registration website",
        "what is analysis" : "it shows a pie chart according to position",
        "can you help me to register" : "sure , First fill the information on home page and submit,then check out the competition in analysis section",
        "can you help me register" : "sure , First fill the information on home page and submit,then check out the competition in analysis section",
        
    }

    return qna.get(message, "I'm sorry, I didn't understand that.")
@app.route('/faq', methods=['POST'])
def get_bot_response():
    user_message = request.form['message']
    bot_response = chatbot_response(user_message)
    return render_template('faq.html', message=user_message, response=bot_response)

@app.route('/data')
def display_table():
    data = []
    with open('data.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data.append(row)
    return render_template('data.html', data=data)





# @app.route('/table')
# def table():
#     with open('data.csv', newline='') as csvfile:
#         data = list(csv.reader(csvfile))
#     return render_template('table.html', data=data)


       
        

 

if __name__ == '__main__':
    app.run(debug=True)
