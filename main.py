from flask import Flask, render_template,request,jsonify
import openai
import sqlite3
openai.api_key = 'YOUR_OPEN_AI_API_KEY'
MODEL= "gpt-3.5-turbo"

def create_table():
    connection = sqlite3.connect('manager.db')
    cursor = connection.cursor()  
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS qa_table (
            QUESTION TEXT,
            ANSWER TEXT
        )
    ''')

    connection.commit()
    connection.close()

create_table()

def insert_into_database(question, answer):
    connection = sqlite3.connect('manager.db')

    cursor = connection.cursor()
    cursor.execute('INSERT INTO qa_table (QUESTION, ANSWER) VALUES (?, ?)', (question, answer))
    connection.commit()
    connection.close()

def fetch_from_database(question):
    connection = sqlite3.connect('manager.db')
    cursor = connection.cursor()
    cursor.execute('SELECT ANSWER FROM qa_table WHERE QUESTION = ?', (question,))
    result = cursor.fetchone()
    connection.close()
    return result[0] if result else None

def fetchQuestion():
    connection = sqlite3.connect('manager.db')
    cursor = connection.cursor()

    cursor.execute('SELECT QUESTION FROM qa_table')
    questions = [row[0] for row in cursor.fetchall()]

    connection.close()

    return questions

app = Flask(__name__)

@app.route("/")
def home():
    try:
        chats=fetchQuestion()
        myChats=[chat for chat in chats]
        return render_template("index.html",myChats=myChats)
    except:
        return render_template("index.html")
    
@app.route("/api",methods=["GET","POST"])




def qa():
    if request.method=="POST":
        question=request.json.get("question")
        chats=fetchQuestion()
        if question in chats:
            Answer=fetch_from_database(question)
            print("Answer")
            data={"result":Answer}
            return jsonify(data)
        else:
            try:
                que=question
                print(que)
                response = openai.ChatCompletion.create(
                    model=MODEL,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content":que},
                    ],
                    temperature=0,
                )
                print(response['choices'][0]['message']['content'])
                Answer=response['choices'][0]['message']['content']
                print(que)
                insert_into_database(question,Answer)
                
                data={"result":f"Answer of {Answer}"}
                return jsonify(data)
            except:
                data="Sorry please try again"
                return jsonify(data)
    data = {"result": "Thank you! I'm just a machine learning model designed to respond to questions and generate text based on my training data. Is there anything specific you'd like to ask or discuss? "}
    return jsonify(data)
    # return render_template("index.html")


app.run(debug=True)
