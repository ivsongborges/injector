from time import sleep
import subprocess

class Monitor:
    def __init__(self, interval, file_name, ip_address):
        self.interval = interval
        self.file_name = file_name
        self.ip_address = ip_address

    def start_monitor(self):
        while True:
            command = "ping -w 1 " \
                +  self.ip_address \
                + " | grep received | awk '{print $4}'"
            output = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read().rstrip()
            
            if output.decode('UTF-8')=='0':
                with open(self.file_name, "a") as myfile:
                    print("\n[MONITOR] system is DOWN")
                    myfile.write("DOWN" + "\n")

            elif output.decode('UTF-8')=='1':
                with open(self.file_name, "a") as myfile:
                    print("\n[MONITOR] system is UP")
                    myfile.write("UP" + "\n")

            else:
                print("output is not known")

            sleep(self.interval)
