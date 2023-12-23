#https://sourabhbajaj.com/mac-setup/Python/virtualenv.html
# Total 358.22 calories burned for 60.0 min. of training

import pandas as pd 
#import matplotlib.pyplot as plt
from scipy import stats
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/prediction', methods=['GET', 'POST'])
def cardio():
    numberofcalories = None
    data = pd.read_csv('cardio.csv')
    #print(data.info())
    #features = ['Duration', 'Average_Pulse', 'Max_Pulse']
    x = data["Duration"]

    y = data["Calorie_Burnage"]
    slope, intercept, r, p, std_err = stats.linregress(x, y)
    def myfunc(x):
        return slope * x + intercept
 
    duration = float( request.form['duration'])
    numberofcalories = round(myfunc(duration),2)
    print(numberofcalories)
    return render_template('prediction.html', numberofcalories=numberofcalories, duration=duration )    

if __name__ == '__main__':
    app.run()

'''
plt.bar(x, y)
plt.xlabel("Duration")
plt.ylabel ("Calorie_Burnage")
plt.show()

print(data.corr())
'''