from flask import Flask, render_template
from sniffer import *

app = Flask(__name__)


@app.route('/')
def main_page():
    gen_1_engine_rpm = sniffer()
    return render_template('main_page.html', GEN_1='ДГУ №1', GEN_2='ДГУ №2', GEN_3='ДГУ №3', GEN_4='ДГУ №4',
                             Engine_RPM="Число оборотов", GEN_1_Engine_RPM=gen_1_engine_rpm, GEN_2_Engine_RPM=0, GEN_3_Engine_RPM=0,GEN_4_Engine_RPM=0)

if __name__ == "__main__":
    app.run()