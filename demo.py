from flask import Flask, render_template
import helper
app = Flask(__name__)
app.config.from_object( 'config' ) #导入配置文件config.py

print(app.config["FLASKDEBUG"])
print(app.config["DEBUG"])

@app.route("/baidu")
def baidu():
    return "www.baidu.com"

@app.route("/book/search/<q>/<page>")
def search(q,page):
    """
        q:关键字或者是ISBN
        page:
    """
    isbn_or_key = helper.is_isbn_or_key(q)

@app.route("/index")
def index():
    return "Hello world flask!"

@app.route("/flask")
def flask01():
    x = 1/0 
    x = x+ 1
    return  x+"flask hejj口jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj!"

@app.route("/login/",methods=["GET","POST"])
def login():
    print("请求来了！显示longin.html页面！")
    return render_template("login.html")

app.add_url_rule("/disk/",view_func=login)

app.add_url_rule("/disk_disk",view_func= index)

def main():
    """
    docstring
    """
    print("aaaaa!")
    app.run("0.0.0.0",8848,debug = app.config["FLASKDEBUG"] )



if __name__ == "__main__" :
    main()
