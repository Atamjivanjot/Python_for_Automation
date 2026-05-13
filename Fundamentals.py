#Lists
servers = ["web1","web2","web3"]
print(servers[1])

#dictionary
server = {
    "name": "web1",
    "ip": "10.0.0.1",
    "status": "running"
}
print(server["ip"])

#conditions
cpu = 50
if cpu > 80:
    print("High CPU")
else:
    print("Normal")

#loops
servers = ["web1","web2","web3"]
for server in servers:
    print(server)


#function
def check_server(name):
    print(f"Checking {name}")
check_server("web1")

#practice
servers = ["web1","web2","web3"]
def restart(server):
    print(f"{server} restarting")
for server in servers:
    restart(server)

#write : this will overwrite the content of the file
with open(r"C:\Users\delln\OneDrive\Desktop\projects\python-automation\logs.txt", "w")as file:
    file.write("Server status OK")

#read
with open(r"C:\Users\delln\OneDrive\Desktop\projects\python-automation\logs.txt", "r")as file:
   data = file.read()
print(data)


#read file line-wise
with open("logs.txt", "r") as file:
    for line in file:
        print(line)



