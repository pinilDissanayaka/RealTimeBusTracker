# Real-Time Bus Tracker Application

This repository contains a real-time bus tracker application that allows users to track buses in real-time on a map. The system uses the NEO-6M GPS Module connected to an ESP32 device to collect GPS data, which is transmitted to AWS IoT. The application processes this data using Apache Kafka and PyKafka to stream GPS data to a Flask web application for real-time display.

## Features
- Real-time bus tracking using GPS data.
- Flask-based web interface to display bus locations on a map.
- GPS data streaming using Apache Kafka and PyKafka.
- IoT integration with AWS IoT and EC2 for data processing.
- Data visualization in real-time using a web-based map.

## Technologies Used
- ESP32: A microcontroller with Wi-Fi and Bluetooth capabilities.
- NEO-6M GPS Module: Provides real-time GPS data.
- AWS IoT: Cloud service to connect and manage IoT devices.
- Apache Kafka: Distributed streaming platform for handling real-time data.
- PyKafka: Python client for Apache Kafka.
- Flask: Lightweight web framework for building the real-time web application.
- AWS EC2: Virtual server to host the Flask application.


## Setup and Installation

### Prerequisites
- Python 3.x installed on your machine.
- AWS Account: Set up AWS IoT Core and EC2.
- Apache Kafka: Install Kafka and set up a broker.
- Flask: Install Flask for the web interface.
- ESP32 Board: Set up with NEO-6M GPS Module.

1. Set up the ESP32 Device
i. Install the required libraries for the ESP32, including the GPS library.
ii. Upload the code from the /device/esp32_gps.py to the ESP32 board.
iii. Configure the device to connect to the AWS IoT Core using the credentials provided in your AWS account.

2. Set up Apache Kafka
i. Install Kafka on your local machine or use a managed Kafka service.
ii. Create a Kafka topic for bus location data.
iii. Run the Kafka broker.

3. Set up AWS IoT Core
i. Create an IoT thing on AWS IoT Core.
ii. Attach a certificate and policy for communication between the ESP32 and AWS IoT.
iii. Ensure your IoT device is properly connected and able to publish GPS data to AWS.

4. Set up the Flask Web Application
i. Install Flask and required dependencies:
```
pip install flask pykafka
```

ii. Run the Flask app:
```
python server/server.py
```

iii. Open your browser and go to http://localhost:5001 to see the real-time bus tracking interface.

5. Set up Kafka Producer and Consumer
i. Run the Kafka producer to send data from ESP32 to Kafka topic:
```
python kafka/producer.py
```

ii. Run the Kafka consumer to process data and pass it to Flask:
```
python kafka/consumer.py
```

## Usage
- The ESP32 device will send GPS data to AWS IoT Core.
- The data will be processed by the Kafka producer and consumer system.
- The processed GPS data will be sent to the Flask app for real-time visualization.
- The Flask app will display the bus locations on a map.

## License
This project is licensed under the MIT License.

## Acknowledgments
- ESP32 and NEO-6M GPS Module for hardware components.
- AWS IoT for managing IoT devices and real-time communication.
- Apache Kafka for streaming and processing the GPS data.
- Flask for building the real-time web application.
