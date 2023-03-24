import multiprocessing as mp
import subprocess
from time import sleep
import numpy as np

class Component:
    def __init__(self, name, mttf, mttr, ip_address, password, network_interface):
        self.name = name
        self.mttf = mttf
        self.mttr = mttr
        self.ip_address = ip_address
        self.password = password
        self.network_interface = network_interface

    def inject_fault(self):
        while True:
            random_mttf = np.random.exponential(float(self.mttf))
            # time is in second
            print("\n" + self.name, "is  UP, next FAULT will happen in:", random_mttf, "seconds")
            sleep(random_mttf)

            random_mttr = np.random.exponential(float(self.mttr))
            # to check the interface in ubuntu, type on terminal: ip addr
            ssh_command = "sshpass -p " \
                + self.password \
                + " ssh -f -o StrictHostKeyChecking=no " \
                + self.ip_address \
                + " -l root \"ip link set " + self.network_interface + " down && sleep " \
                + str(int(random_mttr)) + " && ip link set " + self.network_interface + " up &>/dev/null &\""
            '''
            OBS: we use the ssh_command is a command that deactivates and activates the network interface of the other computer.
                 This command is composed of two Linux commands with a interval between them, the interval is the random_ttr.
            '''
            subprocess.Popen(ssh_command, shell=True, stdout=subprocess.PIPE)

            print("\n" + self.name, "is DOWN, next REPAIR will finish in:", random_mttr, "seconds")
            sleep(random_mttr)

    def run(self):
        self.process = mp.Process(target=self.inject_fault)
        self.process.daemon = True
        self.process.start()

    def terminate(self):
        self.process.kill()
