# ISAssgnment
Internet Security Assignment

## **Instructions on how to run the programs:**

### Open two command prompt windows:

#### On the first command prompt window:
1.	git clone https://github.com/jp7chaiban/ISAssgnment.git
2.	Go to project directory
3.	py -m pip install --user virtualenv (install virtualenv)
4.	py -m venv venv (create a virtual environment and call it “venv”)
5.	.\venv\Scripts\activate (activate virtual environment)
6.	pip install scapy (install scapy package)
7.	pip install Flask (install Flask package)
8.	Go to “BlueTeam” directory (cd BlueTeam)
9.	Two servers are available, one vulnerable to the attack and the other with counter measures:

    a. To run the vulnerable server use : py VulnerableFlask.py (run VulnerableFlask.py)

    b. To run the updated server use: py ImmuneFlask.py (run ImmuneFlask.py)

#### On the second command prompt window:
1.	Go to project directory
2.	.\venv\Scripts\activate (activate virtual environment)
3.	Go to “RedTeam” directory (cd RedTeam)
4.	py SampleDOS.py (run SampleDOS.py)
