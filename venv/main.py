from flask import Flask,request,render_template


app=Flask(__name__)
#creating routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/blog')
def blog():
    return render_template('blog.html')
@app.route('/developer')
def diagnosis():
    return render_template('diagnosis.html')
# python main
if __name__=="__main__":
    app.run(debug=True)

