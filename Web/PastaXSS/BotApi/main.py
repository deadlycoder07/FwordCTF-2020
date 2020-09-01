from flask import Flask,request,make_response
import re,subprocess,shlex,requests,time,os
app=Flask(__name__)

@app.route("/",methods=["GET"])
def visitBot():
    url=request.args.get("url")
    if url is None:
        return "error, url parameter not specified"
    if re.search("^http:\/\/web1.fword.wtf\/jutsu\/\d*$",url) is not None:
        with requests.Session() as s:
            data={"username":"kahlaFtw","password":"Th1sP@ssWorDwiLLneVerB3GueeSS3dK4hlA"}
            s.post("http://localhost:8000/login",data=data)
            session=s.cookies.values()[0].strip()
            result=subprocess.check_output("export OPENSSL_CONF=/etc/ssl/; phantomjs xss-bot.js "+shlex.quote(url)+" "+session,shell=True,timeout=30)
            print(result)
        if b"success" in result:
            resp=make_response("success\n")
            resp.headers["Content-Type"]="text/plain; charset=utf-8"
            return resp
        else:
            return "Failed, contact admin if you are using this legitimately"
    else:
        return "Please only the specified form is accepted"

if __name__=="__main__":
    app.run("0.0.0.0")
