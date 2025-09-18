# Project Title: IoT Smart Lock

## Objective
This project simulates a smart lock system using Python and Tkinter. It allows users to monitor and control a lock through a GUI, with GPIO mocked for testing on laptops and full hardware support on Raspberry Pi.

---

## Tools & Technologies

- **Language**: Python 3.x
- **Framework**: Tkinter for GUI
- **Simulator**: Custom GUI (Tkinter) with mock GPIO
- **Dependencies**: None required for mock GUI; optional real GPIO on Raspberry Pi (`RPi.GPIO`)
- **Extensions / Tools**: VS Code, Git, Python virtual environment

---

## Setup Instructions

### 1. Clone the Repository
git clone https://github.com/marthanjoel/IoT-Smart-Lock.git
cd IoT-Smart-Lock/python
2. Create Virtual Environment (Optional)
bash
Copy code
python3 -m venv venv
source venv/bin/activate
3. Install Dependencies (Optional for Raspberry Pi)
bash
Copy code
pip install -r requirements.txt
# or for Raspberry Pi:
sudo apt install python3-rpi.gpio
4. Run the Project
bash
Copy code
python3 lock.py
Simulation Details
Sensor Emulated: Lock state (OPEN / CLOSED)

Actuator Emulated: LED indicator on GUI represents lock status

Logic: Clicking "Toggle Lock" switches lock state and LED color (green=open, red=closed)


--

##Screenshots
Screenshot 1:<img width="1255" height="731" alt="Screenshot from 2025-09-18 09-01-32" src="https://github.com/user-attachments/assets/0e09df3f-53e1-41d9-9be9-4f43316515fa" />

Screenshot 2: <img width="1255" height="731" alt="Screenshot from 2025-09-18 09-02-19" src="https://github.com/user-attachments/assets/b6cebd85-37e1-4a7b-b09c-dd3748ee17c9" />




--
##Observations
GUI loads correctly on laptop with mock GPIO

Lock status updates properly when toggled

LED indicator changes color based on lock state

Can integrate with real GPIO when deployed on Raspberry Pi


---
##Future Improvements
Add cloud logging for lock events

Integrate voice control or mobile app interface

Replace mock GPIO with real hardware control

Add security features like PIN validation


--
##Files & Structure
bash
Copy code
IoT-Smart-Lock/
├── python/
│   ├── lock.py       
│   ├── main.py
│   ├── Lock.py      
│   ├── move.py
│   ├── state.py      
│   ├── connection.py 
├── README_custom.md  # Project documentation
├── requirements.txt  # Optional dependencies
