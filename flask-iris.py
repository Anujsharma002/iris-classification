from flask import Flask,render_template,request,redirect
import pickle
import numpy
app = Flask(__name__)
model = pickle.load(open("SVM.pickle",'rb'))
@app.route('/', methods=['GET','POST'] )
def home():
     return render_template('for.html',**locals())

@app.route('/for', methods=['GET','POST'] )
def predict():
     Sepal_length= float(request.form['sepal_length'])
     Sepal_width=  float(request.form['sepal_width'])
     Petal_length=  float(request.form['petal_length'])
     Petal_width = float(request.form['petal_width'])
     res =[[Sepal_length,Sepal_width,Petal_length,Petal_width]]
     result = model.predict(res)
     print(result)
     # return render_template()
     l = locals()
     print(l)
     return render_template('for.html',**l)

if __name__ == '__main__':
    app.run(debug=True)