import signal
from time import sleep

from utils.monitor import Monitor
from utils.component import Component

# Fault injection
IP_ADDRESS = "172.16.80.1"
PASSWORD = "adfadf"
NETWORK_INTERFACE = "wlan0"

# Monitor
MONITORING_INTERVAL = 10
MONITORING_FILE_NAME = "dados_monitoramento.txt"

def handler(signum, frame):
    res = input("\nCTRL + C was pressed. Do you really want to exit? y/n ")
    if res == 'y':
        exit(1)

signal.signal(signal.SIGINT, handler)


if __name__ == '__main__':
    monitor = Monitor(MONITORING_INTERVAL, MONITORING_FILE_NAME, IP_ADDRESS)
    components = []

    num_components = input("How many components? ")

    for i in range(int(num_components)):
        name = input("\nEnter the name of the component [" + str(i+1) + "]: ")
        mttf = input("Enter MTTF (FAIL) in seconds of the component [" + str(i+1) + "]: ")
        mttr = input("Enter MTTR (REPAIR) in seconds of the component [" + str(i+1) + "]: ")

        components.append(
            Component(
                name,
                mttf,
                mttr,
                IP_ADDRESS,
                PASSWORD,
                NETWORK_INTERFACE
            )
        )


    for component in components:
        component.run()


    monitor.start_monitor()

    print("Monitor and Fault injection RUNNING...")

