# Simple Vector Database in Python

This repository contains a basic implementation of a vector database in Python, as described in the blog post "Vector Databases Demystified Part 2: Building a Simple Vector Database in Python". This simple example is designed to illustrate the core concepts of vector databases and is not intended for large-scale or real-world applications.

For additional context, see also Part 1:

The vector database supports inserting vectors, searching for similar vectors, and retrieving vectors. It uses cosine similarity as a measure of similarity between vectors.

## Setup and Installation
To set up and run the example, follow these steps:

1. Clone this repository: `git clone https://github.com/yourusername/simple-vector-database.git`
2. Navigate to the project directory: `cd simple-vector-database`
3. Create a virtual environment: for Python 3.6 and above: `python -m venv venv`
4. Activate the virtual environment:
- For Windows: `venv\Scripts\activate`
- For macOS/Linux: `source venv/bin/activate`
5. Install the required libraries: `pip install -r requirements.txt`
6. Run `main.py` to see a demonstration of the vector database in action: `python main.py`

To exit the virtual environment, type `deactivate` in the terminal.

Note: The virtual environment and requirements installation steps are optional but recommended to ensure compatibility and avoid conflicts with other Python packages you may have installed.

## Contents
- `main.py`: Contains the implementation of the VectorDatabase class and a simple example of its usage
- `requirements.txt`: Lists the required libraries for this project
- `README.md`: Provides instructions for setting up and running the example, and explains the contents of the repository
- `.gitignore`: A simple Git configuration file to ignore the virtual environment directory

## License
This project is licensed under the MIT License.
