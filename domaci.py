from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)


#Pomoćna funkcija za povezivanje sa bazom
def connect_db():
    return sqlite3.connect('football_team.db')

#Kreiranje tabele u bazi podataka
def create_table():
    conn = connect_db()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS players (
                 id INTEGER PRIMARY KEY,
                 name TEXT NOT NULL,
                 position TEXT NOT NULL,
                 age INTEGER NOT NULL,
                 nationality TEXT NOT NULL)''')
    conn.commit()
    conn.close()

#Dodavanje novog igrača u bazu podataka
@app.route('/players', methods=['POST'])
def add_player():
    data = request.get_json()
    name = data['name']
    position = data['position']
    age = data['age']
    nationality = data['nationality']
    
    conn = connect_db()
    c = conn.cursor()
    c.execute("INSERT INTO players (name, position, age, nationality) VALUES (?, ?, ?, ?)", (name, position, age, nationality))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Player added successfully"})

#Prikazivanje svih igrača iz baze podataka
@app.route('/players', methods=['GET'])
def get_players():
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM players")
    players = c.fetchall()
    conn.close()
    
    players_list = []
    for player in players:
        player_dict = {
            "id": player[0],
            "name": player[1],
            "position": player[2],
            "age": player[3],
            "nationality": player[4]
        }
        players_list.append(player_dict)
    
    return jsonify(players_list)

#Brisanje igrača iz baze podataka
@app.route('/players/<int:id>', methods=['DELETE'])
def delete_player(id):
    conn = connect_db()
    c = conn.cursor()
    c.execute("DELETE FROM players WHERE id=?", (id,))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Player deleted successfully"})

if __name__ == '__main__':
    create_table()
    app.run(debug=True)

#Prikazivanje detalja određenog igrača na osnovu ID-ja
@app.route('/players/<int:id>', methods=['GET'])
def get_player(id):
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM players WHERE id=?", (id,))
    player = c.fetchone()
    conn.close()

    if player:
        player_dict = {
            "id": player[0],
            "name": player[1],
            "position": player[2],
            "age": player[3],
            "nationality": player[4]
        }
        return jsonify(player_dict)
    else:
        return jsonify({"message": "Player not found"}), 404

#Ažuriranje informacija o određenom igraču
@app.route('/players/<int:id>', methods=['PUT'])
def update_player(id):
    data = request.get_json()
    name = data.get('name')
    position = data.get('position')
    age = data.get('age')
    nationality = data.get('nationality')

    conn = connect_db()
    c = conn.cursor()
    c.execute("UPDATE players SET name=?, position=?, age=?, nationality=? WHERE id=?", (name, position, age, nationality, id))
    conn.commit()
    conn.close()

    return jsonify({"message": "Player updated successfully"})

#Prikazivanje igrača na osnovu pozicije
@app.route('/players/position/<position>', methods=['GET'])
def get_players_by_position(position):
    conn = connect_db()
    c = conn.cursor()
    c.execute("SELECT * FROM players WHERE position=?", (position,))
    players = c.fetchall()
    conn.close()

    players_list = []
    for player in players:
        player_dict = {
            "id": player[0],
            "name": player[1],
            "position": player[2],
            "age": player[3],
            "nationality": player[4]
        }
        players_list.append(player_dict)

    return jsonify(players_list)

