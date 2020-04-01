from flask import Flask, render_template
from flask_cors import CORS
import connexion

app = connexion.App(__name__, specification_dir='./')
CORS(app.app)
app.add_api("api.yml")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)