# AirBnB Console
Description
This is a command-line interpreter (CLI) for managing AirBnB-like objects. It is part of a larger project aimed at building an AirBnB clone. The purpose of this project is to implement a parent class (BaseModel) for object initialization, serialization, and deserialization, along with creating classes (User, State, City, Place, etc.) that inherit from BaseModel. The project also involves creating a simple flow for serialization/deserialization (Instance <-> Dictionary <-> JSON string <-> file), as well as the implementation of a file storage engine.

Command Interpreter
How to Start
To start the AirBnB console, ensure you have Python installed. Then follow these steps:

Clone the repository: git clone <repository-url>
Navigate to the project directory: cd <project-directory>
Run the console script: ./console.py
How to Use
Once the console is running, you will see the (hbnb) prompt. Here are some available commands:

Create: Creates a new instance of BaseModel, saves it, and prints its id.

Usage: create BaseModel
Example: create BaseModel
Show: Prints the string representation of an instance based on the class name and id.

Usage: show BaseModel <instance-id>
Example: show BaseModel 6770495a-3dee-4319-b885-f25a42c1fc44
Destroy: Deletes an instance based on the class name and id.

Usage: destroy BaseModel <instance-id>
Example: destroy BaseModel 6770495a-3dee-4319-b885-f25a42c1fc44
Update: Updates an instance based on the class name and id.

Usage: update BaseModel <instance-id> <attribute-name> "<attribute-value>"
Example: update BaseModel 6770495a-3dee-4319-b885-f25a42c1fc44 name "New Name"
All: Prints all string representations of all instances or those of a specific class.

Usage: all or all BaseModel
Examples:
all
all BaseModel
Quit: Exits the console.

Usage: quit
EOF: Handles EOF (Ctrl+D on Unix/Linux, Ctrl+Z on Windows) to exit the console.

Usage: Press Ctrl+D or Ctrl+Z
Examples
Here are some examples of using the commands:

Create an Instance

bash
Copy code
(hbnb) create BaseModel
Output:

Copy code
6770495a-3dee-4319-b885-f25a42c1fc44
Show Instance

bash
Copy code
(hbnb) show BaseModel 6770495a-3dee-4319-b885-f25a42c1fc44
Output:

csharp
Copy code
[BaseModel] (6770495a-3dee-4319-b885-f25a42c1fc44) {'id': '6770495a-3dee-4319-b885-f25a42c1fc44', 'created_at': '2024-03-02T21:46:50.015149', 'updated_at': '2024-03-02T21:46:50.015177', 'name': 'My_First_Model', 'my_number': 89}
Destroy Instance

bash
Copy code
(hbnb) destroy BaseModel 6770495a-3dee-4319-b885-f25a42c1fc44
Output:

scss
Copy code
(hbnb)
Update Instance

bash
Copy code
(hbnb) update BaseModel 1720fd62-dd41-455e-beff-6fc7afdff523 name "Updated Name"
Output:

scss
Copy code
(hbnb)
List All Instances

bash
Copy code
(hbnb) all
Output:

css
Copy code
["[BaseModel] (1720fd62-dd41-455e-beff-6fc7afdff523) {'id': '1720fd62-dd41-455e-beff-6fc7afdff523', 'created_at': '2024-03-02T21:46:55.263350', 'updated_at': '2024-03-02T21:46:55.263359', 'name': 'My_First_Model', 'my_number': 89}", "[BaseModel] (ada4587a-ff41-4fd6-a79a-7e7c56e140bb) {'id': 'ada4587a-ff41-4fd6-a79a-7e7c56e140bb', 'created_at': '2024-03-02T21:46:56.793235', 'updated_at': '2024-03-02T21:46:56.793242', 'name': 'My_First_Model', 'my_number': 89}"]
Info
This project is the first step towards building an AirBnB clone. It involves creating a command interpreter to manage AirBnB objects, implementing a parent class for object initialization and serialization (BaseModel), creating various classes (User, State, City, Place, etc.) that inherit from BaseModel, and developing a file storage engine for serialization/deserialization. Additionally, unit tests have been created to validate the functionality of the classes and storage engine.
