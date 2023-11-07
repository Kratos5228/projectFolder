from flask import Flask, render_template, request

app = Flask(__name__)

# Make Homepage
@app.route('/')
def homepage():
    return render_template('base.html')

@app.route('/hello')
def hello(Name1=None):
    # listOfNames = [Name1]
    if request.method == 'POST':
        Name1=request.form['Name1']
    return render_template('name2.html', Name1 = Name1)

@app.route('/form', methods=['GET', 'POST'])
def formDemo(name=None):
    if request.method == 'POST':
        name=request.form['name']
    return render_template('form.html', name=name)

@app.route('/teams')
def teams():
    return render_template('teams.html')
    
# return render_template('name.html', context = {'name' = name})
#<!-- <p> Hello there, {{ context.name }}!</p>  -->

# Add the option to run this file directly
if __name__ == '__main__':
    app.run(debug=True)