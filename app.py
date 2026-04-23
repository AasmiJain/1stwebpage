
        from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template("index.html")

# Soil Info Page
@app.route('/soil')
def soil():
    return render_template("soil.html")

# Crop Info Page
@app.route('/crop')
def crop():
    return render_template("crop.html")

# Fruits Page
@app.route('/Fruits')
def fruits():
    return render_template('Fruits.html')

# Vegetables Page
@app.route('/Vegetables')
def vegetables():
    return render_template('Vegetables.html')

# Spices Page
@app.route('/Spices')
def spices():
    return render_template('Spices.html')
# oilseed page 
@app.route('/OilSeeds')
def OilSeeds():
    return render_template('OilSeeds.html')
# Grains page 
@app.route('/Grains')
def Grains():
    return render_template('Grains.html')
# Pulses page 
@app.route('/Pulses')
def Pulses():
    return render_template('Pulses.html')
# CommercialCrops page 
@app.route('/CommercialCrops')
def CommercialCrops():
    return render_template('CommercialCrops.html')

#Special crops page
@app.route('/SpecialCrops')
def SpecialCrops():
    return render_template('SpecialCrops.html')
# Recommendation Page
@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    result = None

    if request.method == 'POST':
        soil = int(request.form['soil'])
        temp = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        rainfall = float(request.form['rainfall'])

        # Simple Rule-Based Logic
        if soil == 0 and rainfall > 200:
            result = "Rice"
        elif soil == 1 and temp > 25:
            result = "Cotton"
        elif soil == 2 and humidity < 60:
            result = "Groundnut"
        elif soil == 3:
            result = "Tea"
        else:
            result = "Maize"

    return render_template("recommend.html", result=result)

# Run App
if __name__ == "__main__":
    app.run(debug=True)
