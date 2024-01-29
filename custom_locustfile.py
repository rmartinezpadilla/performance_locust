# master.conf in current directory
locustfile = test/locustfile.py
headless = true
master = true
expect-workers = 5
host = https://reqres.in/
users = 100
spawn-rate = 10
run-time = 10m