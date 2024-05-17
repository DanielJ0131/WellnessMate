# WellnessMate
Project for the Agile Development Methods Course

by Daniel, Patrick, Tony, André, Elina


## Contents
- [Introduction](#introduction)
- [Requirements](#requirements)
- [Installation](#Installation)
- [Usage](#usage)
- [How to contribute to the project](#how-to-contribute-to-the-project) 

## Introduction

### Product Vision
WellnessMate is an application for individuals looking to improve their mental health and well-being, who struggle to find effective tools for cultivating good habits. It is a wellness computer application that provides easy access to habit tracking, personalization and instead of using complex and time-consuming apps - gives users a simple and easy-to-use habit tracker app that provides personalized recommendations and goals, an app that offers reminders and motivational features to help users stay on track. WellnessMate focuses on making the user experience personal.

## Requirements
Before running this application, ensure that you have the following prerequisites installed:

- A package manager:
  - Brew for Mac and Linux: https://brew.sh/
  - Chocolatey for Windows: https://docs.chocolatey.org/en-us/choco/setup
- Python interpreter [version 3.3 or superior].
  - To check if you have Python installed, open the terminal and execute the command 
```bash
python --version
python3 --version
```
  - To install the latest version of Python with a package manager (Brew or Chocolatey) use 
```bash
choco install python #for Windows
brew install python #for Mac/Linux
```
- Make tool. 
  - If needed, intall with: 
```bash
choco install make #for Windows
brew install make #for Mac/Linux
```
- MySQL Workbench:
  - MySQL Workbench is a unified visual tool for database architects, developers, and DBAs. It provides data modeling, SQL development, and comprehensive administration tools for server configuration, user administration, and more.
  - To install MySQL Workbench, visit the official download page: https://www.mysql.com/products/workbench/
  - Or install it using a package manager:
```bash
choco install mysql.workbench  # for Windows
brew install --cask mysqlworkbench  # for Mac
```

By ensuring you have these prerequisites installed, you will be able to set up and run the application smoothly.

## Installation
Make sure you follow these steps to install WellnessMate locally:

### Step 1:
Clone the repository to your local machine using the terminal provided by Git Bash: 
```bash
git clone https://github.com/DanielJ0131/WellnessMate.git
```

### Step 2: 
Navigate to the project directory.
Open a new terminal at the root folder.
  - If you use python3, you need to update the file called makefile and replace `python` with `python3` in the following line: 
```bash
PYTHON ?= python # python3 py
```
  - If you have a different host or password for MySQL Workbench modify them accordingly.

### Step 3:
Create and activate a virtual environment by running the comands:
```bash
make venv
. .venv/Scripts/activate #for Windows
. .venv/bin/activate #for Mac/Linux
```

Notice that the command line will start with a `(.venv)` after activation.

### Step 4:
Install dependencies specified in the requirements.txt file by running the comand:
```bash
make install
```

To see installed dependencies, run: 
```bash
make installed
```

To exit the virtual enviroment, run: 
```bash
deactivate
```

## Usage
To run WellnessMate App: 
1. Launch MySQL Workbench and ensure it's running in the background.
2. Execute the following command in the terminal:
```bash
make run
```

## How to contribute to the project
