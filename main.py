from flask import Flask, jsonify, render_template, request
from baseAPI import create_app

app = create_app()


if __name__ == '__main__':
    app.run(debug=True)
