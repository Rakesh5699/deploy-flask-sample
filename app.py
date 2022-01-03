from flask import Flask,render_template,request 
app = Flask(__name__) 
@app.route('/')
def home():
    return render_template('index.html')  

@app.route('/results', methods=['GET','POST'])
def calculation_results():
    if request.method == "POST":
        result = 0
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        operator = request.form["operator"] 
        if operator == "ADDITION":
            result = int(num1)+int(num2)
        elif operator == "SUBSTRACTION":
            result = (int(num1)) - (int(num2))
        elif operator == "MULTIPICATION":
            result = int(num1)*int(num2)
        elif operator == "DIVISION":
            result = int(num1)//int(num2)
    
    
    return render_template('index.html',result=result) 

if __name__=="__main__":
    app.run(debug=True)