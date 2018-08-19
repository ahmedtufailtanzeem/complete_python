import paramiko

session = paramiko.SSHClient()
session.set_missing_host_key_policy(paramiko.AutoAddPolicy)
session.connect("192.168.64.2", port=2222, username="parallels")
_, std_out, std_err = session.exec_command("date")
print(std_out.read())
print(std_err.read())
session.close()
