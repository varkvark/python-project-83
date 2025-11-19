### Hexlet tests and linter status:
[![Actions Status](https://github.com/varkvark/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/varkvark/python-project-83/actions)

[![Python CI](https://github.com/varkvark/python-project-83/actions/workflows/PyCI.yml/badge.svg)](https://github.com/varkvark/python-project-83/actions/workflows/PyCI.yml)

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=varkvark_python-project-83&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=varkvark_python-project-83)

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=varkvark_python-project-83&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=varkvark_python-project-83)

# Page Analyzer

Page Analyzer is a Flask application that allows users to analyze web pages for SEO effectiveness.

Application is available by the link:
[Page Analyzer Application](https://python-project-83-naaz.onrender.com/)


## Technologies used

- Python
- Flask
- PostgreSQL
- HTML/CSS
- Bootstrap
- UV package manager


## Installation and launching

Make sure you have Python, UV and PostgreSQL installed.

Use the `Makefile` to simplify the installation and start the process:

```bash
git clone https://github.com/varkvark/python-project-83.git
cd python-project-83

# Configuration
Before running the application, you need to set up your environment variables. Create the `.env` file. Then, modify it with your actual data for the following variables:
- `SECRET_KEY`: a secret key for your application.
- `DATABASE_URL`: the connection string for your PostgreSQL database, formatted as `postgresql://username:password@localhost:5432/database_name`.

# Install dependencies
make install

# Run the local development server
make dev

# Run the production server
make start
```
