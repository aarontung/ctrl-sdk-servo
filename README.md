# ctrl-sdk-servo

## Native SDK

### Installation
```
git clone https://github.com/aarontung/ctrl-sdk-servo.git
cd ctrl-sdk-servo
pip install -r requirements.txt
```

### Preparation
- Connect the robotic arm controller to a power source and connect it to the computer via USB.
- Modify the ```DEVICENAME``` in the test example ```tests/sync_read.py``` based on your operating system.
  (e.g. Windows: "COM1"   Linux: "/dev/ttyUSB0" Mac: "/dev/tty.usbserial-*")

### Run the Example
```
cd tests
python sync_read.py
```
The program will read the current angles of the servo motors numbered 1-7 on the robotic arm (with numbers assigned from the base to the end, i.e., the base servo motor is number 1, and the gripper is number 7). The range of the values is from 0 to 4095.

## RTC SDK
- Supported Linux versions:
  - Ubuntu 22.04 LTS and above

- Python version:
  - Python 3.10 and above

### Installation
```
apt install python3 python3-pip git -y
git clone https://github.com/aarontung/ctrl-sdk-servo.git
cd ctrl-sdk-servo/rtc_sdk
pip install .
```

### Run the Example
```
cd tests
python3 rtc_recv.py --room_id <your room id> --secret_id <your secret id> --secret_key <your secret key>
```
Go to [https://rtcrobot.com/](https://rtcrobot.com/), enter the same `secret_id`/`secret_key` and `room_id`, access the teleoperation webpage, select your controller device, and the test example will receive joint angle data.
```
{"angles":[3128,1520,3418,3785,3284,3950,2236],"timestamp":1739112070124}
```
