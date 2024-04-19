# Flask Football players Management API

This is a simple Flask API for managing players in football team. It allows you to perform CRUD (Create, Read, Update, Delete) operations on players data stored in a SQLite database.
Each player has an id, name, position (Defender, Midfielder, Forward), age and nationality.


## Installation

1. Make sure you have Python installed on your computer. If not, you can download and install it from the [official Python website](https://www.python.org/).

2. Install Flask and SQLite3 libraries using pip:
    ```
    pip install flask
    ```

3. Clone this repository to your local machine:
    ```
    git clone https://github.com/ab20200286/Domaci-1.git
    ```

4. Navigate to the project directory:
    ```
    cd Domaci-1
    ```

5. Run the Flask application:
    ```
    python domaci.py
    ```

6. Access the API at `http://127.0.0.1:5000/` in your web browser or using tools like Postman.

## API Endpoints

- `POST /players`: Add a new player
- `GET /players`: Get all players
- `DELETE /players/<id>`: Delete player by ID
- `GET /players/<id>`: Get player by ID
- `PUT /players/<id>`: Update player by ID
- `GET /players/position/<position>`: Get player by position

## Database

The SQLite database (`football_team.db`) contains a single table `players` with columns `id`, `name`, `position`, `age` and `nationality` . 
You can use SQLite browser tools to interact with the database.

## Usage

You can use tools like Postman to interact with the API endpoints. Here are some example requests:

- To add a new player: `POST http://127.0.0.1:5000/players` with JSON body `{"name": "Lionel Messi", "position": "Forward", "age": 20, "nationality": "Argentina"}`
- To get all players: `GET http://127.0.0.1:5000/players`
- To delete a player: `DELETE http://127.0.0.1:5000/players/<id>`
- To get a player by id: `GET http://127.0.0.1:5000/players/<id>`
- To update a player by id: `PUT http://127.0.0.1:5000/players/<id>` with JSON body `{"name": "Lionel Messi", "position": "Midfielder", "age": 38, "nationality": "Argentina"}`
- To get all player by position: `GET http://127.0.0.1:5000/players/<position>`


## Author

[Aleksa](https://github.com/ab20200286/)
[Marko](https://github.com/mm20200041/)

## License

This project is licensed under the [MIT License](LICENSE).
