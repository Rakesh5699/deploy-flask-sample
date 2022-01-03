from flask import Flask,render_template,request 
app = Flask(__name__) 
@app.route('/')
def home():
    return render_template('index.html')  

@app.route('/results', methods=['GET','POST'])
def calculation_results():
    if request.method == "POST":
        result = "Nothing to get"
        num1 = request.form["num1"]
        num2 = request.form["num2"]
        operator = request.form["operator"] 
        if operator == "ADDITION":
            val = int(num1)+int(num2) 
            result = "THE "+ operator +" OF "+str(num1) + " and " + str(num2) +" is " + str(val)
            return render_template('index.html',result=result) 
        elif operator == "SUBSTRACTION":
            val = (int(num1)) - (int(num2))
            result = "THE "+ operator +" OF "+str(num1) + " and " + str(num2) +" is " + str(val)
            return render_template('index.html',result=result)
        elif operator == "MULTIPICATION":
            val = int(num1)*int(num2)
            result = "THE "+ operator +" OF "+str(num1) + " and " + str(num2) +" is " + str(val)
            return render_template('index.html',result=result)
        elif operator == "DIVISION":
            val = int(num1)//int(num2)
            result = "THE "+ operator +" OF "+str(num1) + " and " + str(num2) +" is " + str(val)
            return render_template('index.html',result=result)
    
    return render_template('index.html',result=result) 

if __name__=="__main__":
    app.run(debug=True)