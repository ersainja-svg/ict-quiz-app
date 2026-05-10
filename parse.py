import json
import re

raw_text = """Theme 1: The role of ICT in key sectors of development and standards in the field
of ICT
1. Which of the following is considered a key sector where ICT plays a crucial
role?
A) Agriculture
B) Education
C) Healthcare
D) Finance
E) All of the above
2. ICT contributes to society by:
A) Increasing communication efficiency
B) Reducing access to information
C) Limiting technological development
D) Increasing manual paperwork
E) Decreasing manual paperwork
3. What does the acronym ICT stand for?
A) Information and Communication Training
B) Internet and Computing Technology
C) Information and Communication Technology
D) Interactive Computing Tools
E) Intelligent Communication Techniques
4. Which standard ensures interoperability of computer networks globally?
A) ISO 9001
B) IEEE 802
C) TCP/IP
D) HTML
E) COBOL
5. Which of the following is a benefit of ICT in healthcare?
A) Manual record keeping
B) Increased treatment errors
C) Delayed communication
D) Telemedicine and electronic health records
E) Reduced patient access to services
6. In the context of ICT standards, ISO primarily deals with:
A) Network hardware design
B) Software programming languages
C) International standardization of processes and technology
D) Database query optimization
E) Cloud storage pricing
7. A major challenge in applying ICT across sectors is:
A) Rapid technological adoption
B) Reduced data generation
C) Lack of skilled workforce and digital divide
D) High literacy levels
E) Decreased automation
8. Which ICT application is critical in modern education?
A) Blackboard and Learning Management Systems
B) Typewriters
C) Fax machines
D) Online collaborative platforms and e-learning tools
E) Printed textbooks only
9. How does ICT affect economic development?
A) By limiting trade opportunities
B) By reducing productivity
C) By increasing efficiency, innovation, and access to markets
D) By eliminating digital communication
E) By increasing production costs only
10.Which of the following is a correct example of ICT standards in software?
A) JPEG for images
B) HTML for web content
C) PDF for documents
D) MP3 for audio
E) TCP for email
Theme 2: Introduction to computer systems and architecture of computer systems
1. The main components of a computer system include:
A) CPU, RAM, HDD
B) Keyboard, Monitor, Printer
C) Operating System, Software, Applications
D) Software, Applications
2. The CPU is responsible for:
A) Storing data permanently
B) Executing instructions and processing data
C) Displaying images on screen
D) Managing network connections
E) Processing data
3. Which of the following is considered primary memory?
A) Hard Disk Drive
B) Flash Drive
C) RAM
D) Optical Disk
E) Cloud Storage
4. What is the function of the motherboard?
A) Connects CPU, memory, and peripherals
B) Stores permanent files
C) Provides network access
D) Displays output to the user
E) Stores user information
5. Which type of architecture separates memory and processing units?
A) Von Neumann
B) Harvard
C) ARM
D) RISC
E) Bit
6. The control unit in a CPU is responsible for:
A) Performing arithmetic operations
B) Managing execution of instructions
C) Storing programs permanently
D) Controlling internet access
E) Storing accesses
7. Which is an example of input devices?
A) Monitor, Printer
B) Keyboard, Mouse
C) CPU, RAM
D) USB Drive
E) Speakers
8. Cache memory is:
A) Slower than RAM
B) Used to store long-term data
C) High-speed memory between CPU and RAM
D) Part of the hard disk
E) A type of network memory
9. In a computer system, the bus is:
A) A type of memory
B) A communication pathway between components
C) The storage drive
D) The CPU core
E) The display device
10.Which architecture uses a single memory for instructions and data?
A) Harvard
B) ARM
C) Von Neumann
D) RISC
E) x86
Theme 3: Software and operating systems
1. Which of the following is system software?
A) Microsoft Word
B) Photoshop
C) Operating System
D) Chrome
E) AutoCAD
2. The primary function of an operating system is:
A) Running only games
B) Managing hardware and software resources
C) Writing code
D) Browsing internet
E) Creating documents
3. Which OS is open-source?
A) Windows
B) macOS
C) Linux
D) iOS
E) None of the above
4. Device drivers are used to:
A) Increase internet speed
B) Improve software graphics
C) Allow OS to communicate with hardware
D) Control keyboard only
E) Store files
5. GUI stands for:
A) General User Interface
B) Graphical Unit Integration
C) Graphical User Interface
D) Guided User Installation
E) None of the above
6. Multitasking in an OS means:
A) Running multiple hardware
B) Running multiple software simultaneously
C) Using multiple GPUs
D) Running background apps only
E) Using multiple CPUs
7. Which OS is used for smartphones?
A) Linux
B) Windows 95
C) Android
D) DOS
E) UNIX
8. Utility software is used for:
A) Gaming
B) System maintenance and optimization
C) Writing documents
D) Browsing
E) Video editing
9. The kernel of an OS is:
A) User interface
B) Core component managing resources
C) Applications
D) Network card
E) None of the above
10.Virtual memory is:
A) Extra RAM installed physically
B) Part of storage used as RAM
C) Cache memory
D) Cloud storage
E) CPU cache
Theme 4: Human-computer interaction (HCI)
1. HCI stands for:
A) High-level Computing Interface
B) Hardware Control Integration
C) Human-Computer Interaction
D) Human Communication Internet
E) None of the above
2. GUI is important in HCI because:
A) Increases hardware cost
B) Makes software user-friendly
C) Reduces user interaction
D) Slows processing
E) None of the above
3. Which is a direct input device?
A) Printer
B) Keyboard
C) Monitor
D) Speaker
E) RAM
4. HCI studies:
A) Only hardware
B) Only software
C) Interaction between humans and computers
D) Programming languages
E) Cloud computing
5. Usability in HCI refers to:
A) Speed of CPU
B) Memory size
C) Ease of use for the user
D) Graphics quality
E) Internet speed
6. Touch screens are an example of:
A) Output device
B) Input device
C) Storage device
D) Network device
E) None of the above
7. Ergonomics in HCI is concerned with:
A) Keyboard shortcuts
B) User comfort and efficiency
C) Cloud storage
D) Database design
E) Network security
8. Voice recognition is an example of:
A) Software tool
B) Hardware device
C) Natural user interface
D) Cloud computing
E) Database system
9. A bad HCI design may result in:
A) Faster processing
B) User errors and low productivity
C) Better usability
D) High security
E) Improved performance
10.In HCI, accessibility ensures:
A) Software runs on all devices
B) Only advanced users can operate
C) Software is usable by people with disabilities
D) Faster internet
E) Better graphics
Theme 5: Database systems
1. A database is:
A) A type of operating system
B) A storage device
C) An organized collection of data
D) A programming language
E) A network protocol
2. SQL stands for:
A) Standard Query Language
B) Structured Query Language
C) Structured Query Language
D) Simple Query Language
E) System Quality Level
3. Primary key is:
A) Duplicate value in a table
B) Unique identifier for each record
C) Password for the database
D) Type of query
E) Storage location
4. Normalization is:
A) Data encryption method
B) Process to reduce redundancy in a database
C) Backup process
D) Query optimization
E) Table formatting
5. A foreign key:
A) Is the main key in the table
B) Links one table to another
C) Encrypts data
D) Deletes records
E) Stores backup
6. Which of the following is a relational database?
A) MongoDB
B) MySQL
C) Redis
D) Cassandra
E) Hadoop
7. ACID properties stand for:
A) Atomicity, Consistency, Isolation, Durability
B) Accuracy, Control, Integrity, Database
C) Atomicity, Consistency, Isolation, Durability
D) Access, Control, Internet, Data
E) Analytics, Consistency, Index, Database
8. Which command is used to retrieve data in SQL?
A) GET
B) SELECT
C) SELECT
D) RETRIEVE
E) FETCH
9. Index in a database is:
A) A file type
B) A data structure to speed up retrieval
C) Query statement
D) Database user
E) Table name
10.Which is a non-relational database?
A) MySQL
B) PostgreSQL
C) Oracle
D) MongoDB
E) SQL Server
Theme 6: Data analysis and data management
1. Data analysis is:
A) Storing files
B) Inspecting and modeling data to extract useful information
C) Sending emails
D) Installing software
E) Backing up databases
2. Big data refers to:
A) Small datasets
B) Large and complex datasets requiring special tools
C) Encrypted files
D) Cloud storage only
E) Text files
3. ETL in data management stands for:
A) Extract, Transform, Load
B) Encrypt, Transfer, Log
C) Extract, Transform, Load
D) Evaluate, Track, Link
E) Execute, Test, Log
4. Data cleaning is:
A) Process of correcting or removing inaccurate data
B) Encrypting files
C) Data backup
D) File formatting
E) Data transmission
5. Dashboard in analytics is:
A) A car panel
B) Visual interface summarizing key metrics
C) SQL query
D) Database table
E) Memory storage
6. Which tool is used for data analysis?
A) Excel
B) Tableau
C) Python
D) All of the above
E) None of the above
7. Data visualization helps to:
A) Encrypt data
B) Delete data
C) Understand and communicate data insights
D) Store data
E) Increase memory
8. Structured data is:
A) Data in random format
B) Organized in rows and columns
C) Images only
D) Audio files only
E) Cloud storage
9. A challenge in data management is:
A) Easy storage
B) Low volume of data
C) Data security and integrity
D) No processing tools
E) None
10.Data warehouse is:
A) A storage device
B) Central repository for integrating multiple data sources
C) Software
D) Programming language
E) Cloud only
Theme 7: Networks and Telecommunications
1. LAN stands for:
A) Large Area Network
B) Local Area Network
C) Long Access Network
D) Logical Area Network
E) Linked Access Node
2. WAN connects:
A) Devices in the same room
B) Multiple LANs over a large distance
C) Only computers in one office
D) Internet servers only
E) Printers only
3. The Internet Protocol (IP) is used for:
A) Storing files
B) Addressing and routing data packets
C) Encrypting emails
D) Programming
E) Connecting USB devices
4. Which device connects multiple networks?
A) Switch
B) Hub
C) Router
D) Modem
E) Firewall
5. TCP/IP stands for:
A) Transmission Control Protocol / Internet Protocol
B) Transfer Communication Process / Internet Protocol
C) Transmission Control Protocol / Internet Protocol
D) Transfer Control Process / Internal Protocol
E) Transport Communication Program / Internet Process
6. Wi-Fi is:
A) Wired connection
B) Wireless local area network
C) Satellite system
D) Bluetooth only
E) Network cable
7. Bandwidth measures:
A) Processor speed
B) Data transfer capacity
C) Memory usage
D) Screen resolution
E) File size
8. Ping command is used to:
A) Open a website
B) Test connectivity between devices
C) Encrypt messages
D) Transfer files
E) Backup data
9. A firewall is used to:
A) Increase bandwidth
B) Protect networks from unauthorized access
C) Store files
D) Print documents
E) Control CPU usage
10.A VPN allows:
A) Faster CPU
B) Secure remote network access
C) More memory
D) Wireless printing
E) Cloud storage only
Theme 8: Cybersecurity
1. Cybersecurity is:
A) Programming network software
B) Protecting computer systems from threats
C) Creating hardware
D) Managing databases
E) Designing websites
2. Phishing is:
A) Data storage
B) Fraudulent attempt to obtain sensitive information
C) Software installation
D) Network cabling
E) Encryption method
3. Malware is:
A) Safe software
B) Malicious software intended to harm systems
C) Database tool
D) Cloud storage
E) Programming language
4. A strong password should include:
A) Only letters
B) Only numbers
C) Letters, numbers, and symbols
D) Only symbols
E) Only spaces
5. Two-factor authentication requires:
A) Password only
B) Email verification only
C) Password + another verification method
D) Fingerprint only
E) Security software only
6. Firewall protects against:
A) Data loss
B) Unauthorized network access
C) Power failure
D) Disk corruption
E) Slow CPU
7. Encryption is:
A) Data deletion
B) Transforming data to prevent unauthorized access
C) Network configuration
D) Database backup
E) Software installation
8. Antivirus software:
A) Creates files
B) Detects and removes malware
C) Increases bandwidth
D) Monitors CPU only
E) Compiles code
9. A common cybersecurity risk in emails is:
A) High memory
B) Phishing attacks
C) Network cabling
D) Slow processor
E) Disk fragmentation
10.Social engineering attacks target:
A) Hardware only
B) Human behavior and trust
C) Cloud storage
D) CPU speed
E) Memory usage
Theme 9: Internet technologies
1. HTTP stands for:
A) Hypertext Transfer Protocol
B) Hypertext Transfer Protocol
C) Hyperlink Transfer Protocol
D) Hyper Text Transmission Program
E) None
2. HTTPS differs from HTTP by:
A) Faster speed
B) Encryption for secure communication
C) Lower bandwidth
D) Only used in browsers
E) Only for images
3. URL stands for:
A) Unified Resource Location
B) Uniform Resource Locator
C) Uniform Resource Locator
D) Universal Resource Link
E) None
4. HTML is used to:
A) Store files
B) Create and structure web pages
C) Program databases
D) Encrypt emails
E) Configure network
5. CSS is used to:
A) Create database
B) Style HTML web pages
C) Encrypt data
D) Test connectivity
E) Run scripts
6. JavaScript is:
A) A database tool
B) Programming language for web interactivity
C) Styling language
D) Networking protocol
E) Hardware driver
7. A web server:
A) Stores and delivers web content
B) Stores and delivers web content
C) Compiles software
D) Monitors CPU
E) Encrypts emails
8. Cookies in web technology are:
A) Edible
B) Data stored on user device to remember information
C) Network cables
D) CPU storage
E) Disk format
9. DNS is used to:
A) Translate domain names to IP addresses
B) Encrypt data
C) Translate domain names to IP addresses
D) Monitor networks
E) Store cookies
10.Cloud hosting allows:
A) Only local access
B) Access to services and storage via the internet
C) USB storage
D) Only database storage
E) Offline software
Theme 10: Cloud and mobile technologies
1. Cloud computing allows:
A) Local only access
B) Remote access to computing resources over the internet
C) Faster CPU
D) Local storage only
E) Standalone software
2. SaaS stands for:
A) Storage as a Service
B) Software as a Service
C) Security as a Service
D) System as a Service
E) Server as a Service
3. PaaS provides:
A) Hardware only
B) Platform for developers to build applications
C) Network only
D) Storage only
E) CPU resources only
4. IaaS is:
A) Internet and Application Service
B) Infrastructure as a Service
C) Internal as a Service
D) Input as a Service
E) None
5. Mobile apps are installed on:
A) Desktop only
B) Smartphones and tablets
C) Routers
D) Servers only
E) Network switches
6. Cloud storage examples include:
A) Google Drive
B) Dropbox
C) OneDrive
D) All of the above
E) None
7. Hybrid cloud means:
A) Public cloud only
B) Private cloud only
C) Combination of public and private cloud
D) Cloud offline
E) Cloud storage only
8. Mobile operating systems include:
A) Windows 95
B) DOS
C) Android and iOS
D) Ubuntu only
E) Linux desktop
9. Benefits of cloud computing include:
A) Scalability
B) Cost efficiency
C) Accessibility
D) All of the above
E) None
10.Risks of cloud computing include:
A) Data security
B) Service downtime
C) Compliance issues
D) All of the above
E) None
Theme 11: Multimedia technologies
1. Multimedia combines:
A) Text only
B) Images only
C) Text, images, audio, video, and animation
D) Audio only
E) None
2. Video editing software examples include:
A) Adobe Premiere
B) Final Cut Pro
C) Both A and B
D) Word
E) Excel
3. Audio file formats include:
A) JPG
B) MP3
C) MP3
D) TXT
E) PNG
4. Animation in multimedia is:
A) Still images
B) Creating motion graphics
C) Text files
D) Audio tracks only
E) Video playback
5. Multimedia presentations include:
A) PowerPoint
B) Prezi
C) Both A and B
D) PDF only
E) Word only
6. Which is a benefit of multimedia?
A) Engages audience
B) Enhances learning
C) Visual communication
D) All of the above
E) None
7. Editing images in multimedia uses software like:
A) Adobe Photoshop
B) Excel
C) Word
D) Notepad
E) Paint only
8. Streaming media requires:
A) Local playback
B) Internet connection
C) CD-ROM only
D) DVD drive only
E) Printer
9. Compression of multimedia files is used to:
A) Increase file size
B) Reduce storage space and bandwidth
C) Delete content
D) Encrypt files
E) Improve CPU speed
10.Interactive multimedia allows:
A) Passive viewing
B) User interaction with content
C) Only audio playback
D) Text editing
E) File transfer only
Theme 12: Smart technology
1. Smart technology is characterized by:
A) High cost only
B) Automation and connectivity
C) Manual operation
D) Desktop only
E) None
2. IoT stands for:
A) Internet of Transmission
B) Internet of Things
C) Integration of Technology
D) International Online Tools
E) None
3. Smart homes can include:
A) Smart lighting
B) Smart thermostats
C) Security systems
D) All of the above
E) None
4. Wearable devices include:
A) Smartwatch
B) Fitness tracker
C) Both A and B
D) Desktop PC
E) None
5. Smart cities use ICT for:
A) Traffic management
B) Waste management
C) Energy efficiency
D) All of the above
E) None
6. AI integration in smart technology allows:
A) Automated decision-making
B) Predictive analytics
C) Both A and B
D) None
E) Manual control only
7. Security challenge in smart devices is:
A) Unauthorized access
B) High RAM
C) CPU speed
D) Storage only
E) Internet speed
8. A smart appliance example is:
A) Oven
B) Washing machine
C) Wi-Fi enabled washing machine
D) Laptop
E) None
9. Energy monitoring in smart technology helps:
A) Reduce electricity usage
B) Monitor consumption
C) Optimize devices
D) All of the above
E) None
10.Connectivity of smart devices is mostly via:
A) USB only
B) Wi-Fi, Bluetooth, Zigbee
C) VGA
D) HDMI
E) Ethernet only
Theme 13: E-technology, electronic business, e-learning, and e-government
1. Which tool allows instructors to track student progress in e-learning?
A) PDF files
B) YouTube videos
C) Learning Management System (LMS)
D) Blog posts
E) Social media
2. Which is a key security requirement for online payment in e-business?
A) Using open Wi-Fi
B) Weak passwords
C) SSL encryption and multi-factor authentication
D) Disabling firewalls
E) None
3. A primary benefit of e-government is:
A) Manual record keeping
B) Increased paperwork
C) Online submission of forms
D) In-person queues
E) Printing extra documents
4. Mobile learning (m-learning) is defined as:
A) Learning on desktop computers
B) Learning using smartphones and tablets
C) Traditional classroom-only learning
D) Only video lectures
E) Printed materials
5. What is the biggest barrier to e-learning adoption in developing countries?
A) Teacher training and digital literacy
B) Internet speed
C) Device availability
D) Cultural resistance to online learning
E) None
6. Which activity is typically performed by e-business analytics?
A) Tracking warehouse temperature
B) Monitoring customer behavior online
C) Encrypting devices
D) Printing invoices
E) Sending paper mail
7. Which technology enhances accessibility for students with disabilities in elearning?
A) Keyboard shortcuts
B) Screen readers
C) LMS platforms
D) Video playback
E) PDF downloads
8. Digital identity verification in e-government ensures:
A) Faster printing
B) Secure access to public services
C) Higher bandwidth
D) More storage
E) None
9. An example of an m-learning platform is:
A) Moodle
B) Coursera
C) Udemy
D) None of the above individually
E) None
10.Efficiency in e-government is improved mainly by:
A) Automated service delivery
B) Printing forms
C) Increased queues
D) Reducing paperwork
E) None
Theme 14: Information technologies in professional and industrial ICT
1. Which ICT tool is primarily used for industrial process automation?
A) Microsoft Word
B) CAD software
C) SCADA systems
D) LMS
E) None
2. IoT in manufacturing mainly helps with:
A) Marketing campaigns
B) Real-time monitoring of production lines
C) Email management
D) Cloud storage only
E) None
3. Industrial robots are primarily used to:
A) Replace all humans
B) Increase paperwork
C) Perform repetitive and precise tasks
D) Reduce automation
E) None
4. ERP systems are used for:
A) Editing videos
B) Social media management
C) Managing enterprise resources like finance, HR, and supply chain
D) Writing reports only
E) None
5. A primary cybersecurity risk when integrating IoT devices in industrial ICT
is:
A) Device overheating
B) Unauthorized access to production systems
C) High electricity use
D) Printing errors
E) None
6. Data analytics in industrial ICT helps:
A) Decision-making
B) Process optimization
C) Forecasting production needs
D) All of the above
E) None
7. A common challenge in adopting industrial ICT is:
A) Cheap technology
B) Employee training and integration with legacy systems
C) No internet
D) Excess storage
E) None
8. SCADA systems are used to:
A) Post social media updates
B) Control and monitor industrial processes
C) Manage emails
D) Cloud storage only
E) None
9. IoT devices improve industrial ICT by:
A) Increasing downtime
B) Enhancing efficiency and predictive maintenance
C) Reducing automation
D) Increasing manual error
E) None
10.Automation in industrial ICT primarily reduces:
A) Internet usage
B) Human error and production time
C) Software updates
D) Marketing expenses
E) None
Theme 15: Prospects of development of ICT
1. Which emerging technology is expected to have the largest impact on future
ICT?
A) AI
B) Blockchain
C) Quantum computing
D) All of the above
E) None
2. AI can assist ICT development by:
A) Automating routine tasks
B) Printing documents
C) Only storing files
D) Monitoring hardware only
E) None
3. 5G networks primarily provide:
A) Low-speed internet
B) High-speed connectivity with low latency
C) More power consumption
D) Only mobile apps
E) None
4. Quantum computing impacts ICT by:
A) Enabling faster data processing and new encryption methods
B) Reducing internet speed
C) Printing invoices faster
D) Increasing storage size only
E) None
5. A major ethical challenge in ICT is:
A) AI decision-making without transparency
B) Slow internet
C) Outdated software
D) Cloud storage cost
E) None
6. Green ICT focuses on:
A) Energy-efficient and sustainable computing
B) Faster processors only
C) Cloud storage only
D) AI only
E) None
7. Edge computing allows:
A) Data processing near the source
B) Faster real-time analytics
C) Only data backup
D) Printing output
E) None
8. IoT in smart cities helps with:
A) Only traffic lights
B) Traffic management, energy optimization, and environmental monitoring
C) Just email services
D) Printing forms
E) None
9. Blockchain improves ICT by:
A) Enabling secure and transparent transactions
B) Increasing storage only
C) Reducing bandwidth
D) Monitoring hardware
E) None
10.The biggest global ICT adoption challenge is:
A) Digital divide and unequal access to technology
B) Printing issues
C) Local networks only
D) Keyboard speed
E) None
"""

themes = []
current_theme = None
current_question = None

lines = raw_text.strip().split('\n')
for line in lines:
    line = line.strip()
    if not line:
        continue
    
    if line.startswith("Theme"):
        if current_question:
            current_theme["questions"].append(current_question)
            current_question = None
        if current_theme:
            themes.append(current_theme)
        current_theme = {
            "title": line,
            "questions": []
        }
    elif re.match(r'^\d+\.', line):
        if current_question:
            current_theme["questions"].append(current_question)
        current_question = {
            "text": line,
            "options": []
        }
    elif re.match(r'^[A-E]\)', line):
        if current_question:
            current_question["options"].append(line)
    else:
        # continuation of text
        if current_question and len(current_question["options"]) == 0:
            current_question["text"] += " " + line
        elif current_theme and not current_question:
            current_theme["title"] += " " + line

if current_question:
    current_theme["questions"].append(current_question)
if current_theme:
    themes.append(current_theme)

with open("questions.json", "w", encoding="utf-8") as f:
    json.dump(themes, f, indent=4, ensure_ascii=False)
