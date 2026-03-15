# DevNet REST API Automation Project

## Author
Klaudia

## Description
This project demonstrates basic network automation using Python and REST APIs.

The Python script sends an HTTP request to an API endpoint, processes JSON data
and prints the response from the server.

The goal of this project is to show how network devices or services can be
configured automatically using APIs.

## Technologies
- Python
- REST API
- JSON
- Ubuntu Linux
- Git
- GitHub

## Project Structure
devnet-restconf-project
│
├── restconf.py
└── README.md

## How it works
1. The Python script sends a REST API request.
2. The server processes the request.
3. The response is returned in JSON format.
4. The script prints the response in the terminal.

## Example architecture

Python Script
      │
      ▼
   REST API
      │
      ▼
 Network Service
      │
      ▼
  JSON Response

## How to run the project

Clone the repository:

git clone https://github.com/klaudia946/devnet-restconf-project.git

Go to the project directory:

cd devnet-restconf-project

Run the script:

python3 restconf.py

