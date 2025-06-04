# CyberBullyingDetection-PRANEETHA SAI
Detecting hate comments using Hybrid RNN LSTM and deploying it using render
email-spraneethasai2006@gmail.com


# CyberBullyingDetection

Detecting hate comments using a Hybrid RNN-LSTM model and deploying it using Render.

## 📌 Overview

This project focuses on identifying hate comments in social media platforms by leveraging a hybrid Recurrent Neural Network (RNN) and Long Short-Term Memory (LSTM) model. The model is trained on labeled datasets to classify comments as cyberbullying or not. The application is deployed using [Render](https://render.com/), providing a user-friendly interface for real-time detection.

## 🧠 Features

* **Hybrid RNN-LSTM Model**: Combines the strengths of RNN and LSTM architectures for effective sequence modeling.
* **Pre-trained Models**: Includes Logistic Regression and Support Vector Machine (SVM) models for comparison.
* **Web Interface**: User-friendly interface for inputting comments and viewing predictions.
* **Deployment**: Hosted on Render for easy accessibility.

## 📁 Project Structure

```
CyberBullyingDetection/
├── Data/                   # Contains datasets used for training and testing
├── Models/                 # Saved machine learning models
├── PPT and docs/           # Project documentation and presentation files
├── templates/              # HTML templates for the web interface
├── lr_model.joblib         # Pre-trained Logistic Regression model
├── svm_model.joblib        # Pre-trained SVM model
├── vectorizer.joblib       # Text vectorizer used for feature extraction
├── untitled3.py            # Main application script
├── webscraping.ipynb       # Jupyter notebook for data collection via web scraping
├── requirements.txt        # Python dependencies
├── LICENSE                 # MIT License
└── README.md               # Project documentation
```

## 🚀 Getting Started

### Prerequisites

* Python 3.6 or higher
* pip (Python package installer)

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/preyi/CyberBullyingDetection.git
   cd CyberBullyingDetection
   ```

2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

1. **Start the application:**

   ```bash
   python untitled3.py
   ```

2. **Access the web interface:**

   Open your browser and navigate to `http://localhost:5000` to use the application.

## 🛠️ Deployment

The application is deployed using [Render](https://render.com/). To deploy your own instance:

1. **Create a new web service on Render:**

   * Connect your GitHub repository.
   * Set the build and start commands:

     * **Build Command:** `pip install -r requirements.txt`
     * **Start Command:** `python untitled3.py`

2. **Configure environment variables (if any):**

   Ensure any necessary environment variables are set in the Render dashboard.

3. **Deploy:**

   Render will automatically build and deploy your application.

## 📊 Model Details

* **Hybrid RNN-LSTM Model:** Combines RNN's ability to handle sequential data with LSTM's capability to manage long-term dependencies.
* **Pre-trained Models:**

  * `lr_model.joblib`: Logistic Regression model.
  * `svm_model.joblib`: Support Vector Machine model.
* **Vectorizer:**

  * `vectorizer.joblib`: Used for transforming text data into numerical features.

## 📈 Performance

The hybrid RNN-LSTM model demonstrates superior performance in detecting hate comments compared to traditional machine learning models like Logistic Regression and SVM. Detailed evaluation metrics and comparisons are available in the `PPT and docs/` directory.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📬 Contact

For any inquiries or feedback, please contact:

* **Name:** Praneetha Sai
* **Email:** [spraneethasai2006@gmail.com](mailto:spraneethasai2006@gmail.com)

---
