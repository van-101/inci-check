from flask import Flask, render_template, request, redirect, url_for
from text_recog import ocr_image
app=Flask(__name__)

@app.route('/upload')
def upload():
   if request.method == 'POST':
       if request.files:
           file = request.files["file"]
           output = ocr_image(file)
           print(output)
           return render_template('index.html')
   return render_template('output.html')

@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'GET':
        if request.form.get('tryus')== 'Try Us!':
            return redirect(url_for('upload'))
   return render_template('index.html')

# @app.route('/at_work')
# def work_page():  
#    return render_template('output.html')

if __name__=='__main__':
    app.run(debug=True)