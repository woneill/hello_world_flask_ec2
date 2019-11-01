"""The heart of the application"""
from ec2_metadata import ec2_metadata
from flask import Flask
app = Flask(__name__)  # pylint: disable=invalid-name


@app.route('/')
@app.route('/index')
def index():
    """Return an indicator of which host we're running on"""
    try:
        hostname = ec2_metadata.private_hostname
    except Exception:  # pylint: disable=broad-except
        hostname = f"not running in EC2"

    return f"Hello, World! I'm {hostname}"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
