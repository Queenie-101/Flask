from flask import Flask, render_template #load html files
#initialize the flask app
app=Flask(__name__)
#open the home page
@app.route('/')
#function to render the home page
def home():
    #dispaly the contents of index.html
    return render_template('index.html')
#run the app
if __name__=='__main__':
    app.run(debug=True)