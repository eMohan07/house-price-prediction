# 🏠 House Price Prediction — ML & DevOps CI/CD Pipeline

A complete end-to-end Machine Learning project that predicts residential house prices based on property features, integrated with a fully automated, production-grade **DevOps CI/CD Pipeline** using **Jenkins**, **Docker**, **Ansible**, and **Pytest**.

---

## 📌 Project Overview

This project predicts the selling price of a house using 13 property features:
- **Dimensions & Layout:** Bedrooms, Bathrooms, Living Area (`sqft_living`), Lot Area (`sqft_lot`), Floors, Above Ground Area (`sqft_above`), Basement Area (`sqft_basement`).
- **Condition & Ratings:** View Rating, Overall Condition, Waterfront status.
- **Timeline & Location:** Year Built, Year Renovated, City (20 King County municipalities).

The machine learning model uses a **Scikit-learn Pipeline** (with feature imputation and one-hot encoding) trained on Linear Regression, serialized via **Joblib**, and served interactively through a **Streamlit** web application.

---

## 🛠️ Technology Stack

| Domain | Technologies |
| :--- | :--- |
| **Machine Learning** | Python 3.11+, Scikit-learn, Pandas, NumPy, Joblib, Matplotlib |
| **Web Frontend** | Streamlit |
| **Testing & Quality** | Pytest, Flake8 |
| **Containerization** | Docker, Docker Desktop |
| **Configuration & CD** | Ansible Playbooks |
| **CI/CD Automation** | Jenkins Pipeline (`Jenkinsfile`), Git, GitHub |

---

## 📂 Project Directory Structure

```text
house-price-prediction/
│
├── .dockerignore                  # Docker build exclusions
├── Dockerfile                     # Multi-stage container specification with healthcheck
├── Jenkinsfile                    # 7-stage Declarative CI/CD pipeline definition
├── start-jenkins.bat              # 1-click script to launch Jenkins locally on Windows
├── app.py                         # Streamlit web application entrypoint
├── requirements.txt               # Application runtime dependencies
├── README.md                      # Project documentation
│
├── ansible/                       # Continuous Deployment infrastructure
│   ├── inventory.ini              # Ansible target host inventory
│   └── deploy.yml                 # Idempotent container deployment playbook
│
├── tests/                         # Automated test suite
│   ├── __init__.py
│   └── test_prediction.py         # Pytest unit, validation & regression tests
│
├── data/
│   └── Housing.csv                # Historical housing dataset
│
├── models/
│   ├── house_price_model.pkl      # Trained model weights
│   └── house_price_pipeline.pkl   # Serialized end-to-end scikit-learn pipeline
│
├── notebooks/                     # Research & data exploration
│   ├── exploration.ipynb
│   └── pipeline.ipynb
│
└── src/                           # Core source package
    ├── __init__.py
    ├── constants.py               # City categories & constants
    ├── predict.py                 # Pipeline loading & inference logic
    ├── train.py                   # Model persistence utility
    └── utils.py                   # Input dimension validation rules
```

---

## ⚙️ DevOps CI/CD Architecture

The automated delivery pipeline enforces a strict **fail-fast quality gate**: deployment only occurs if all unit tests, model assertions, syntax checks, and container builds succeed.

### 🔄 Pipeline Stages

```text
[ 1. Checkout ] 
       ⬇
[ 2. Dependency Installation ] 
       ⬇
[ 3. Code Validation (Flake8) ] 
       ⬇
[ 4. Automated Tests (Pytest) ] ➔ (Aborts on test failure)
       ⬇
[ 5. Docker Image Build ] 
       ⬇
[ 6. Ansible Deployment ] 
       ⬇
[ 7. Health Verification ] ➔ HTTP 200 at /_stcore/health
```

### Stage Breakdown

1. **Checkout:** Clones the target commit from the GitHub repository (`main` branch).
2. **Dependency Installation:** Automatically installs/upgrades pip, runtime dependencies, and testing tools (`pytest`, `flake8`).
3. **Code Validation:** Runs syntax compilation checks (`py_compile`) and linting (`flake8`) across application code and test suites.
4. **Automated Tests:** Executes 6 Pytest test cases covering input validation boundaries, pipeline serialization, deterministic price predictions, and cross-city inferences.
5. **Docker Image Build:** Builds a lightweight `python:3.11-slim` container, tagged with both `:BUILD_NUMBER` and `:latest`.
6. **Deployment through Ansible:** Executes `ansible/deploy.yml` (or Windows native container fallback) to idempotently stop older containers and run the new version on host port `8501`.
7. **Health Verification:** Actively probes `http://localhost:8501/_stcore/health` with retry intervals to confirm that the web app is live and healthy before marking the build as `SUCCESS`.

---

## 🚀 Quickstart: Running from Fresh Fork or Clone

### Prerequisites
- **Git**
- **Python 3.10+**
- **Docker Desktop** (running)
- **Java 21 LTS** (required to run Jenkins)

---

### Method 1: Local Development & Tests

```powershell
# 1. Clone repository
git clone https://github.com/eMohan07/house-price-prediction.git
cd house-price-prediction

# 2. Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt pytest flake8

# 3. Run automated test suite
python -m pytest tests/ -v

# 4. Launch Streamlit locally
streamlit run app.py
```
Application opens at: `http://localhost:8501`

---

### Method 2: Running with Docker Desktop

```powershell
# Build image
docker build -t house-price-predictor:latest .

# Run container
docker run -d --name house-price-predictor -p 8501:8501 --restart unless-stopped house-price-predictor:latest

# Check health endpoint
curl http://localhost:8501/_stcore/health
```
Application opens at: `http://localhost:8501`

---

### Method 3: Deploying via Ansible

```bash
ansible-playbook -i ansible/inventory.ini ansible/deploy.yml -e "image_tag=latest"
```

---

### Method 4: Automated CI/CD Pipeline with Jenkins

1. **Launch Docker Desktop.**
2. **Start Jenkins:** Double-click [`start-jenkins.bat`](./start-jenkins.bat) or run:
   ```powershell
   .\start-jenkins.bat
   ```
3. Open `http://localhost:8080` in your browser.
4. Retrieve the initial admin password:
   ```powershell
   Get-Content "$env:USERPROFILE\.jenkins\secrets\initialAdminPassword"
   ```
5. Install suggested plugins and create your admin account.
6. Click **New Item** ➔ Name: `house-price-prediction-pipeline` ➔ Select **Pipeline** ➔ Click **OK**.
7. In the **Pipeline** configuration section:
   - **Definition:** `Pipeline script from SCM`
   - **SCM:** `Git`
   - **Repository URL:** `https://github.com/eMohan07/house-price-prediction.git` (or your forked URL)
   - **Branch Specifier:** `*/main`
   - **Script Path:** `Jenkinsfile`
8. Click **Save** ➔ Click **Build Now**.
9. Observe all 7 stages turn **Green** in the **Pipeline Stage View**!

---

## 📊 Machine Learning Model Details

| Metric | Performance |
| :--- | :--- |
| **Model Type** | Linear Regression |
| **Preprocessing** | SimpleImputer + OneHotEncoder (`ColumnTransformer`) |
| **MAE** | 146,232 |
| **RMSE** | 238,736 |
| **R² Score** | 0.617 |

---

## 👨‍💻 Author

**Mohan E**
- **GitHub:** [https://github.com/eMohan07](https://github.com/eMohan07)
- **LinkedIn:** [https://www.linkedin.com/in/emohan/](https://www.linkedin.com/in/emohan/)

---

## ⭐ Contributing & Support
If this project helped you learn DevOps, ML pipelines, or Jenkins automation, please consider giving the repository a ⭐!
