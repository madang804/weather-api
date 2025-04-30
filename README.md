# Weather API

![License](https://img.shields.io/badge/license-MIT-blue.svg)  
A simple web API built with Python and Flask that provides weather-related information. This service is designed to allow other web applications to connect and retrieve random weather data for a given location.

---

## Table of Contents
1. [About the Project](#about-the-project)
2. [Endpoints](#endpoints)
3. [Getting Started](#getting-started)
4. [Deploying to AWS Elastic Beanstalk](#deploying-to-aws-elastic-beanstalk)
5. [Reference](#reference)
6. [License](#license)

---

## About the Project
This Flask-based web API provides three endpoints for weather-related information:
- `weather`
- `temperature`
- `wind speed and direction`

The API is designed to simulate weather data for a given location.

---

## Endpoints

### 1. Weather
- **Endpoint:** `/weather`
- **Method:** `GET`
- **Query Parameters:**
  - `location` (required): The location for which weather data is requested.
- **Response:** A random weather description (e.g., sunny, cloudy, rainy).

### 2. Temperature
- **Endpoint:** `/temperature`
- **Method:** `GET`
- **Query Parameters:**
  - `location` (required): The location for which temperature data is requested.
- **Response:** A random temperature in Celsius.

### 3. Wind Speed and Direction
- **Endpoint:** `/wind`
- **Method:** `GET`
- **Query Parameters:**
  - `location` (required): The location for which wind speed and direction data is requested.
- **Response:** A random wind speed (e.g., 15 kts) and direction (e.g., 45 deg).

---

## Getting Started

### Select your OS

<details>
<summary>Windows</summary>

### Prerequisites
- Python and pip installed.
- Git installed.

1. Clone the repository:
   ```cmd
   git clone https://github.com/madang804/weather-api.git
   ```
2. Navigate to project directory:
   ```cmd
   cd weather-api
   ```
3. Create a virtual environment:
   ```cmd
   python -m venv venv
   ```
4. Activate virtual environment:
   ```cmd
   venv\Scripts\activate
   ```
5. Install dependencies:
   ```cmd
   pip install -r requirements.txt
   ```
6. Run Flask app:
   ```cmd
   flask --app application run
   ```
7. Open a browser and visit `http://127.0.0.1:5000` to test the API locally.
8. Deactivate virtual environment:
   ```cmd
   deactivate
   ```
</details>

<details>
<summary>MacOS</summary>

### Prerequisites
- Python and pip installed.
- Git installed.

1. Clone the repository:
   ```bash
   git clone https://github.com/madang804/weather-api.git
   ```
2. Navigate to project directory:
   ```bash
   cd weather-api
   ```
3. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
4. Activate virtual environment:
   ```bash
   source venv/bin/activate
   ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Run Flask app:
   ```bash
   flask --app application run
   ```
7. Open a browser and visit `http://127.0.0.1:5000` to test the API locally.
8. Deactivate virtual environment:
   ```bash
   deactivate
   ```
</details>

<details>
<summary>Linux</summary>

### Prerequisites
- Python and pip installed.
- Git installed.

1. Clone the repository:
   ```bash
   git clone https://github.com/madang804/weather-api.git
   ```
2. Navigate to project directory:
   ```bash
   cd weather-api
   ```
3. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```
4. Activate virtual environment:
   ```bash
   source venv/bin/activate
   ```
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Run Flask app:
   ```bash
   flask --app application run
   ```
7. Open a browser and visit `http://127.0.0.1:5000` to test the API locally.
8. Deactivate virtual environment:
   ```bash
   deactivate
   ```
</details>

## Deploying to AWS Elastic Beanstalk

<details>
<summary>AWS Console</summary>

The Flask app is deployed to AWS Elastic Beanstalk via the AWS Console. Below is a step-by-step guide.

### Step-by-Step Guide

#### 1. Zip Application Files
- Create a `.zip` file that includes `application.py` and `requirements.txt`.

<details>
<summary>Windows</summary>

### Prerequisites
- 7-Zip installed.

  ```cmd
  "C:\Program Files\7-Zip\7z.exe" a -tzip application.zip application.py requirements.txt
  ```
</details>

<details>
<summary>MacOS</summary>

### Prerequisites
- Zip installed.

  ```bash
  "zip application.zip application.py requirements.txt
  ```
</details>

<details>
<summary>Linux</summary>

### Prerequisites
- Zip installed.

  ```bash
  "zip application.zip application.py requirements.txt
  ```
</details>

#### 2. Log In to AWS Management Console
1. Go to the [AWS Elastic Beanstalk Console](https://console.aws.amazon.com/elasticbeanstalk).
2. Click **Create Application**.

#### 3. Create a New Elastic Beanstalk Application
1. Under **Application information** name the application (e.g., `WeatherAPI`).
2. Under **Environment information**:
   - Choose a domain prefix (e.g., `weather-api`) and check availability.
   - Leave blank to auto-generate.
3. Under **Platform**:
   - Select **Python** and the appropriate **Platform Branch**.

#### 4. Upload Flask Application
1. Under **Application code**:
   - Select **Upload your code**
   - Set **Version label** to v1.0
   - Upload `.zip` file created earlier.
2. Click **Next**.
3. Under **Service access**:
   - Choose an **EC2 instance profile** from dropdown list.
   - If none listed, create a new IAM role with these policies:
     - AWSElasticBeanstalkWebTier
     - AWSElasticBeanstalkWorkerTier
     - AWSElasticBeanstalkMulticontainerDocker
   - Click `Refresh` to refresh the dropdown list to find the new IAM role .
4. Click **Skip to Review** or **Next** to continue through additional settings.
5. Click **Submit** to deploy.

#### 5. Monitor Deployment
- Wait until you see **Environment successfully launched**. App is now live.

  ![eb-console.png](./png/eb-console.png)

#### 6. Test API
1. Copy app URL (e.g., `http://weather-api.eu-west-2.elasticbeanstalk.com`).

   ![main.png](./png/main.png)

2. Test endpoints in a browser.

   ![weather.png](./png/weather.png)

   ![temperature.png](./png/temperature.png)

   ![wind.png](./png/wind.png)

3. Test endpoints using curl (optional).

   ![curl-weather.png](./png/curl-weather.png)

   ![curl-temperature.png](./png/curl-temperature.png)

   ![curl-wind.png](./png/curl-wind.png)

</details>

<details>
<summary>Terraform</summary>

### Prerequisites
- aws CLI installed.
- curl installed.
- jq installed (optional)
 
1. Change to terraform directory
   ```bash
   cd terraform/
   ```
1. Ensure `zip_app.sh` is executable.
   ```bash
   chmod +x zip_app.sh
   ```
2. Run these Terraform commands to deploy Flask app to AWS Elastic Beanstalk.
   ```bash
   terraform init
   terraform plan
   terraform apply -auto-approve
   ```
3. Test API
   ```bash
   curl -s http://weather-api.eu-west-2.elasticbeanstalk.com/api/v1.0/weather?location=london | jq .
   ```
   ```bash
   curl -s http://weather-api.eu-west-2.elasticbeanstalk.com/api/v1.0/temperature?location=london | jq .
   ```
   ```bash
   curl -s http://weather-api.eu-west-2.elasticbeanstalk.com/api/v1.0/wind?location=london | jq .
   ```
4. Run this command to destroy deployed AWS resources.
   ```bash
   terraform destroy -auto-approve
   ```
5. NOTE: AWS Elastic Beanstalk automatically creates an S3 bucket which is not managed by Terraform code. AWS recommends to manually delete the bucket.
   ```bash
   aws s3 rm s3://elasticbeanstalk-<region>-<account-id> --recursive
   aws s3api delete-bucket --bucket elasticbeanstalk-<region>-<account-id>
   ```
  
</details>

---

## Reference

- https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html
- https://flask.palletsprojects.com
- https://www.python.org

---

## License
This project is licensed under the MIT License. See [LICENSE](./LICENSE) for more details.

---






