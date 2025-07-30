from flask import Flask, request, jsonify
import random

app = Flask(__name__)

tree_facts = [
    "Trees produce oxygen and reduce carbon dioxide.",
    "The tallest tree in the world is a redwood named Hyperion.",
    "Baobab trees can store thousands of liters of water.",
    "Some trees can live for thousands of years."
]

@app.route('/')
def home():
    return "🌳 welcome to vishvendar panwar!"

@app.route('/tree', methods=['GET'])
def get_random_fact():
    return jsonify({"tree_fact": random.choice(tree_facts)})

@app.route('/trees', methods=['GET'])
def get_all_facts():
    return jsonify({"all_facts": tree_facts})

@app.route('/tree', methods=['POST'])
def add_tree_fact():
    data = request.get_json()
    fact = data.get("fact")
    if fact:
        tree_facts.append(fact)
        return jsonify({"message": "Fact added!", "fact": fact}), 201
    else:
        return jsonify({"error": "No fact provided"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
