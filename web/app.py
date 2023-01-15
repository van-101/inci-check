from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def main_page():
   # return render_template('index.html')
   return render_template('result.html')

# @app.route('/at_work')
# def work_page():  
#    return render_template('output.html')

if __name__=='__main__':
    app.run(debug=True)