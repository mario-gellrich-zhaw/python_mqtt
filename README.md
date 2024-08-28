# MQTT Example with Raspberry Pi

This repository contains an example project that demonstrates how to use the MQTT protocol with a Raspberry Pi. The project utilizes the `mosquitto` MQTT broker and the `paho-mqtt` Python client library to send and receive messages.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Understanding MQTT](#understanding-mqtt)


## Introduction

Message Queuing Telemetry Transport (MQTT) is a lightweight messaging protocol designed for devices that require a small code footprint or have limited network bandwidth. It is widely used in IoT (Internet of Things) devices due to its efficiency and simplicity.

This project showcases how to set up an MQTT broker on a Raspberry Pi using `mosquitto` and how to create a simple Python client using `paho-mqtt` to send and receive messages.

## Requirements

Before you begin, ensure you have the following hardware and software:

- **Hardware:**
  - Raspberry Pi (I use Pi Model B with 4 GB RAM)
  - Sense Hat
  - Internet connection
  
- **Software:**
  - Raspbian OS installed on Raspberry Pi
  - Mosquitto MQTT broker
  - Python 3.x
  - paho-mqtt Python library
  - sense-hat Python library

## Installation

Follow these steps to set up your Raspberry Pi and install the necessary software.

### 1. Install Mosquitto Broker on Raspberry Pi

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install mosquitto mosquitto-clients
sudo systemctl enable mosquitto
sudo systemctl start mosquitto
```

### 2. Install the required Python Libraries on Raspberry Pi and your client PC

```bash
# Raspberry Pi
pip install sense-hat
pip install paho-mqtt

# Client PC
pip install paho-mqtt
```

### Usage
Make sure that the Raspberry Pi and your client PC are in the same network.

In VS Code on your PC, open a Terminal and cd into the folder where app.py is located.

Run the following Python command in your VS Code Terminal.

```bash
python app.py
```

## Understanding MQTT

**What is MQTT?**  
MQTT stands for Message Queuing Telemetry Transport. It is a publish/subscribe messaging protocol that works on top of the TCP/IP protocol. MQTT is designed to be lightweight, making it ideal for use in constrained environments such as IoT devices.

**How MQTT Works**
Broker: The central server that receives all messages from the clients and routes them to the appropriate subscribers.
Client: Any device or application that connects to the broker to send (publish) or receive (subscribe) messages.
Topic: The routing information for the broker to send the message to the correct clients. Topics are organized hierarchically using slashes (e.g., house/sensor1).

**Why Use MQTT?** 
Efficiency: MQTT minimizes network bandwidth and device resource requirements, making it ideal for low-power devices.
Simplicity: The publish/subscribe model is easy to understand and implement.
Reliability: MQTT can ensure messages are delivered at least once, exactly once, or at most once.