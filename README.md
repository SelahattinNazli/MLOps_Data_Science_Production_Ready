# MLOps_Data_Science_Production_Ready

This project demonstrates an end-to-end MLOps workflow, including data processing, model development, deployment, and monitoring. It provides a production-ready template for deploying machine learning models with containerization, CI/CD, and database integration.

## Features

- End-to-end machine learning pipeline
- API deployment using FastAPI
- MongoDB integration for data storage
- Dockerized application for easy deployment
- CI/CD workflow with GitHub Actions
- Jupyter notebooks for EDA and model development

## Project Structure
```bash
MLOps_Data_Science_Production_Ready/
├── .github/workflows/ # CI/CD GitHub Actions workflows
├── config/ # Configuration files (DB, app settings)
├── notebook/ # Data exploration and model notebooks
├── static/ # Static files (CSS)
├── templates/ # HTML templates
├── app.py # FastAPI application
├── demo.py # Demo script for testing API
├── Dockerfile # Docker image configuration
├── requirements.txt # Python dependencies
├── setup.py # Package setup
└── README.md # Project documentation
```

## Installation

**1. Clone the repository:**

```bash
git clone https://github.com/SelahattinNazli/MLOps_Data_Science_Production_Ready.git
cd MLOps_Data_Science_Production_Ready
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```
**Running with Docker**

Build and run the Docker container:
```bash
docker-compose up --build
```
**Access the API at http://localhost:8000**
.

## MongoDB Configuration

The project uses MongoDB to store and retrieve data. Update the connection URI in config/db_config.py (or the relevant config file) before running the application.

**Example:**
```bash
MONGO_URI = "mongodb://username:password@localhost:27017/db_name"
```
**Usage**
```bash
Start the API server: python app.py

Run the demo script: python demo.py (interacts with the API)
```
## Contributing

**Fork the repository**

**Create a new branch:**
```bash
git checkout -b feature-xyz
```
**Commit your changes:**
```bash
git commit -m "Add feature xyz"
```
**Push the branch:**
```bash
git push origin feature-xyz
```
**Open a pull request**

## License

**MIT License**
