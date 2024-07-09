# VAry
 VAry, Diversify, VAry app(Android) And more..


enjoy.


## diversify

**A Seamless, Stealthy, and Reliable Remote Access and Control Tool for Windows**

This project presents a suite of tools designed for subtle remote access and control of Windows machines. It functions on a client-server model, with the server component (**dvrfy**) prioritizing stealth and dependability. Client components, offered as a Kivy-based mobile app and a desktop application (**UTXTool**), provide various ways to interact with a compromised system.

### Project Focus

* **Smooth and Seamless Operation:** diversify integrates smoothly into the target system, avoiding disruptive behavior and minimizing its presence.
* **Stealth and Evasion:** The server component is crafted to evade detection by most antivirus software through techniques like hiding its executable, securing file permissions, and utilizing encrypted communication. It stays dormant unless activated by a client, further reducing its visibility. Note that highly sophisticated heuristic-based antivirus solutions might still flag certain behaviors. 
* **Reliability:** The tools are meticulously engineered for robust performance and consistent functionality, ensuring a stable remote access experience.

### Core Components

#### dvrfy (Server)

dvrfy resides on the target Windows machine, operating silently by default. It executes commands only upon receiving validated instructions from a connected client.

**Functionality:**

* **Dormant State:** dvrfy maintains a low profile, remaining inactive unless instructed by a client. Its default actions are limited to self-preservation, such as adding itself to the startup folder and applying restrictive permissions to its file.
* **Encrypted Communication:** It utilizes AES encryption for all communication with clients, securing both commands and data transmission.
* **Client-Activated Operations:** Upon receiving and authenticating commands from a connected client, dvrfy springs into action. The range of commands includes:
    * **System Manipulation:** Opening websites, interacting with the mouse and keyboard, playing sounds, manipulating the display (including blacking out the screen and rotating it),  and more.
    * **Process Management:** Terminating or freezing selected processes.
    * **Security Feature Manipulation:** Disabling the firewall, User Account Control (UAC), or Windows Defender.
    * **Network Interaction:** Scanning the local network for other "diversify" devices and sending commands to them.
    * **Self-Modification:** Updating itself, renaming itself, moving itself to a different folder, and even self-destructing.
* **Optimized Screen Sharing:** It features a screen-sharing module designed for efficiency and discretion.  By transmitting only the changes between screen frames, it minimizes network traffic, making it less noticeable to network monitoring software. 

#### Kivy-based Mobile App (Client)

The mobile app provides an intuitive interface for controlling dvrfy on remote hosts. It's designed for user-friendliness, allowing for effortless command execution and interaction with the compromised system.

**Key Features:**

* **Comprehensive Command Set:**  Offers a broad range of commands, encompassing basic system interactions, powerful system manipulation, and self-modification options.
* **Intuitive Touch-Based UI:**  Features a streamlined interface optimized for touch interactions on mobile devices.
* **Integrated Network Scanner:**  Simplifies the process of discovering and connecting to available dvrfy hosts on the local network.

#### UTXTool (Desktop Client)

UTXTool is a work-in-progress desktop client, envisioned to provide a more comprehensive user interface for accessing the full range of dvrfy's capabilities. Currently, its primary focus is on creating a sleek and feature-rich experience for remote desktop control.


#### builder.py

builder.py  is a Flask application with a web UI that simplifies the building process for UTXTool and dvrfy using PyInstaller. It allows users to configure build options, including output directories and additional dependencies, and offers real-time feedback by displaying console output during the build. 

### Legacy Components

These components are from previous iterations of the server and are kept for historical context.

* **cdwn.exe:**  Monitored and restarted the legacy **rb.exe** server in case of crashes and managed its updates.
* **rb.exe:** The initial server component, now replaced by the more advanced and stealthy **dvrfy**.
* **tbl.exe:** A discontinued project aiming to merge the functionality of **cdwn.exe** and **rb.exe**, ultimately abandoned for the more modular approach used in **dvrfy**.

### Communication and Security

All communication between clients and the dvrfy server is secured using AES encryption, requiring a pre-shared key for authentication. A keep-alive mechanism is in development to enhance connection reliability and verify host availability. 

### Disclaimer

This project is for educational and ethical purposes only. Misusing these tools for illegal activities is strictly prohibited and can result in severe legal consequences. Unauthorized access and control of computer systems are criminal offenses with serious repercussions. 
