import sys
from flask import Flask, render_template, request, redirect, url_for, session
from text_recog import ocr_image
import json


app=Flask(__name__)
app.config["SECRET_KEY"] = "kinmin_apps_co"
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"


@app.route('/results', methods=['GET', 'POST'])
def results(output = None):
   #  output = ocr_image(file)
   json_data = session['json_data']
   json_data = json.loads(json_data)
   rep = json_data['repeated']
   inci_list = ", ".join(list(json_data['inci_not']))
   if inci_list == "":
      inci = "Yes"
   else:
      inci = "No"
   aqua = json_data['aqua']
   pres = json_data['preservatives']
   print(json_data, file=sys.stdout)
   return render_template('result.html', rep = rep, inci_list = inci_list,
                          inci=inci, aqua = aqua, pres = pres)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
   if request.method == 'POST':
       if request.files:
           file = request.files["file"]
           json_data = ocr_image(file)
           session['json_data'] = json_data
           return redirect(url_for('results'))
   return render_template('output.html')


@app.route('/', methods=['GET', 'POST'])
def index():
   # if request.method == 'GET':
   #      if request.form.get('tryus')== 'Try Us!':
   #          return redirect(url_for('upload'))
   return render_template('index.html')

# @app.route('/at_work')
# def work_page():  
#    return render_template('output.html')

if __name__=='__main__':
    app.run(debug=True)