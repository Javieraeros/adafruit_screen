import subprocess
from paramiko import SSHClient

class Command:

    error = None

    def __init__(self, computer):
        if computer != "":
            self.client = SSHClient()
            self.client.load_system_host_keys()
            splited = computer.split('@')
            self.host = splited[1]
            try:
                self.client.connect(self.host, username=splited[0])
            except:
                self.error = "Cannot connect to {}".format(self.host)
                pass
        else:
            self.client = None

    def result(self, cmd):
        if self.client != None:
            try:
                ssh_stdin, ssh_stdout, ssh_stderr = self.client.exec_command(cmd)
                result = ssh_stdout.read().decode("utf-8")
            except:
                result = "No connection to {}".format(self.host)
        elif self.error != None:
            result = self.error
        else:
            result = subprocess.check_output(cmd, shell=True).decode("utf-8")
        return result

    def hostname(self):
        cmd = "hostname"
        hostname = self.result(cmd)
    
        return "Hostname: {}".format(hostname).replace("\n", "")
    
    def cpuload(self):
        cmd = "uptime | sed 's/.*average://'"
        loadaverage = self.result(cmd)
        return "Load:{}".format(loadaverage).replace("\n", "")
    
    def memory(self):
        cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%s MB  %.2f%%\", $3,$2,$3*100/$2 }'"
        memory = self.result(cmd)
        return memory
    
    def disk(self):
        cmd = 'df -h | awk \'$NF=="/"{printf "Disk: %d/%d GB  %s", $3,$2,$5}\''
        disk = self.result(cmd)
        return disk
    
    def temperatura(self):
        cmd = "cat /sys/class/thermal/thermal_zone0/temp |  awk '{printf \"CPU Temp: %.1f C\", $(NF-0) /     1000}'"
        temp = self.result(cmd)
        return temp

    def end(self):
        if self.client != None:
            self.client.close()

