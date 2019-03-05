from flask import Flask, jsonify

app = Flask(__name__)

my_dairy = [
    {
        'id': 1,
        'pageTitle': 'My first Day at School',
        'description': 'I really cannt imagine talking about it because it is hillarious',
        'done': False
    },
    {
        'id': 2,
        'pageTitle': 'How I used my first lunch coin',
        'description': 'How ,else apart form a rolex',
        'done': False
    }
]
@app.route('/diary/api/v1/mydiary', methods=['GET'])
def get_tasks():
    return jsonify({'my_dairy': my_dairy})


if __name__ == '__main__':
    app.run(debug=True)