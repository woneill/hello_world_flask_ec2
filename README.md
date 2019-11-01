# Hello World

A simple flask app that returns the private IPv4 DNS hostname of the EC2 instance it's running on.

If it can't determine the value from the ec2 metadata endpoint it assumes it isn't running on an EC2 instance and returns that information instead.

## Installation

```
PIPENV_VENV_IN_PROJECT=1 pipenv install
pipenv run gunicorn -w 4 helloworld:app
```

### Installation when pipenv isn't available
Alternatively, if `pipenv` is problematic to install you can use `requirements.txt` that was generated via `pipenv lock -r > requirements.txt`

```
python -m venv helloword_env
source helloword_env/bin/activate
pip install -r requirements.txt
gunicorn -w 4 helloworld:app
```

### CentOS 7 python3 setup

```
yum install centos-release-scl
yum install rh-python36
scl enable rh-python36 bash
```