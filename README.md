# fault-injection-simulator

This repository contains a Fault Injection Simulator to accelerate the failure process in components. It also collects data to evaluate availability of a service.


## Setting the virtual environment

Before running the fault-injection simulator, create a Python virtual environment. This step is important because you have to install some packages to run the fault-injection simulator. By creating a virtual environment, you will install all dependencies only on the virtual environment, which means that your system's Python installation will not be modify.


The following commands help to create the virtual environment (venv) and activate it. Make sure you are in the ```fault-injection-simulator``` directory.

**NOTE:** ```foo@foo:~$``` is not part of the command, it is and example of what you terminal shows when you open it up.

```bash
foo@foo:~$ python -m venv vevn --prompt=fault-injection-simulator
```

The previous command will create a ```venv``` directory, which represents the virtual environment. After that, you have to activate the virtual environment. The following command activates the virtual environment.

```bash
foo@foo:~$ source venv/bin/activate
```

Now you should see you terminal showing:

```bash
(fault-injection-simulator) foo@foo:~$
```

It means that you virtual environment is activated.

To finish, with the virtual environment activated, update the ```pip``` (package installer for Python). The following command will update the ```pip```version.

```bash
(fault-injection-simulator) foo@foo:~$ pip install pip --upgrade
```

## Installing requirements

Once you have the virtual environment activated, you have to install the packages that are used by the fault-injection simulator. All dependencies are listed in the requirements.txt.

To install all dependecies, run the following command:

```bash
(fault-injection-simulator) foo@foo:~$ pip install -r requirements.txt
```

Now you are all set to run the fault-injection simulator.


## Running the fault-injection simulator

Open the ```main.py``` file to set the following variables:

- **IP_ADDRESS** is the variable that will store the ip address of the server which the faults will be injected to. We use this address to connect via ssh;
- **PASSWORD** is the variable that will store the password of the server, in order to connect via ssh;
- **NETWORK_INTERFACE** is the variable that will store the network interface that will be up and down during the fault injection;
- **MONITORING_INTERVAL** is the variable that will store the monitoring interval. The monitor will collect data about the service every amount of seconds that is set in this variable;
- **MONITORING_FILE_NAME** is the variable that will store the file name. This file will store the collected data about the server.

For instance:

```bash
IP_ADDRESS = "172.16.80.1"
PASSWORD = "adfadf"
NETWORK_INTERFACE = "wlan0"

MONITORING_INTERVAL = 10
MONITORING_FILE_NAME = "dados_monitoramento.txt"
```

After you performed the previous steps, you are good to go, and now you can run the fault-injection simulator. The following command will start the fault-injection simulator.

```bash
(fault-injection-simulator) foo@foo:~$ python simulator/main.py
```

**NOTE:** the mttf and mttr will be set in seconds.


## Other informations

To stop the fault-injection simulator, press ```CTRL + C```, and the following message will appear in the terminal:

```bash
CTRL + C was pressed. Do you really want to exit? y/n
```

Then you press ```y``` and it will finish the simulator execution.

To deactivate the virtual environment, you only need to run the ```deactivate``` command.

```bash
(fault-injection-simulator) foo@foo:~$ deactivate
```

Your terminal will be back:

```bash
foo@foo:~$
```
