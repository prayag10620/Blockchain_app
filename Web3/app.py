from flask import Flask, render_template, request , jsonify
from service import get_block_by_hash , get_block_by_num , get_trasaction_data


app = Flask(__name__)

app.config['SECRET_KEY'] = "MySecureSecretKey"
#app.config['MAIL_SERVER'] = "smtp-mail.outlook.com"
#app.config['MAIL_PORT'] = 587
#app.config['MAIL_USE_TLS'] = True
#app.config['MAIL_USE_SSL'] = False
#app.config['MAIL_USERNAME'] = mail_username
#app.config['MAIL_PASSWORD'] = mail_password
#mail = Mail(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/form")
def search():
    return render_template('blockchain.html')


@app.route("/blockchain" , methods = ['POST'])
def get_block_data():
    if request.method == 'POST':
        block_num = request.form['block_number']
        block_hash = request.form['block_hash']

        if block_hash:
            block_data = get_block_by_hash(block_hash)

        elif block_num:
            block_data = get_block_by_num(block_num)

        
        return jsonify(block_data)
        return render_template('result.html' , blockdata = block_data)
    
@app.route('/transaction_form')
def transaction():
    return render_template('transaction.html')

@app.route("/transaction" , methods = ['POST'])
def get_transaction():
    if request.method == 'POST':
        tx_hash = request.form['transaction_hash']     

        if tx_hash:
            tx_data = get_trasaction_data(tx_hash)

        
        return jsonify(tx_data)
        return render_template('result.html' , blockdata = tx_data)  
    
    else:
        return render_template('transaction.html')
        
    
    


       
if __name__ == "__main__":
    app.run(debug=True)
