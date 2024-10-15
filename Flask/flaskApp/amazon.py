from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')

def home():
    datas = [
        {"url":"https://images-eu.ssl-images-amazon.com/images/G/31/img23/Softlines_JWL_SH_GW_Assets/2024/QC/Sept11/PCQC_New_sports_low._SY116_CB563244637_.jpg","text":"Sports shoes"},
        {"url":"https://images-eu.ssl-images-amazon.com/images/G/31/img23/Softlines_JWL_SH_GW_Assets/2024/QC/Sept11/pcqc_shoes_low._SY116_CB563244637_.jpg","text":"Sports shoes"},
        {"url":"https://images-eu.ssl-images-amazon.com/images/G/31/img23/Softlines_JWL_SH_GW_Assets/2024/QC/Sept11/pcqc_heels_low._SY116_CB563244637_.jpg","text":"Sports shoes"},
        {"url":"https://images-eu.ssl-images-amazon.com/images/G/31/img23/Softlines_JWL_SH_GW_Assets/2024/QC/Sept11/PCQC_HB_Low._SY116_CB563244637_.jpg","text":"Sports shoes"},
    ]
    return render_template('amazon.html',datas=datas)


if __name__ == '__main__':
    app.run(debug=True)