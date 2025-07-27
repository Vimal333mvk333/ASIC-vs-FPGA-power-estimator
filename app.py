from flask import Flask, render_template, request
from estimator import estimate_power

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        gate_type = request.form['gate_type']
        num_gates = int(request.form['num_gates'])
        frequency = float(request.form['frequency'])
        voltage = float(request.form['voltage'])

        asic_power, fpga_power = estimate_power(gate_type, num_gates, frequency, voltage)
        return render_template('result.html', asic_power=asic_power, fpga_power=fpga_power)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
