# OSPublic
## Octa Semester Public
- This repository contains eight semester practicals/ experiments

## DC Practical 3
*To establish group communication between N servers*
### Step 1: Getting config port numbers
**Run init.py on any one of the N servers (run only once)**

**N = number of servers/nodes**

`python init.py --nodes N`

You will get two txt files `all_ins.txt` and `all_config.txt`
### Step 2: Setting up port numbers and IP addresses of the servers
Create `in.txt` file and paste port numbers for your server depending upon the decided name (Server A, Server B etc)

Create `config.txt` file and paste port numbers for your server depending upon the decided name (Server A, Server B etc)

The `config.txt` should contain IP addresses of the other servers except your own IP address and the port numbers generated in  `all_config.txt` file

**Example**: 

`192.168.25.85:6502` 

`192.168.65.203:6120`

`192.168.49.165:8562` 

`192.168.30.193:7508`

### Step 3: Set own IP
Open `server.py` file and edit `host="YOUR_SERVER_IP_ADDRESS"`

### Step 4: Run `server.py` file on all the servers simultaneously

### Step 5: Communicate with servers
`python client_helper.py --ip DESTINATION_IP_ADDRESS --port DESTINATION_SERVER_PORT`

**Note: DESTINATION_SERVER_PORT should be present in `in.txt` file of the DESTINATION_SERVER**