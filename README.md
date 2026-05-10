# Midland-Microfin-Risk-Tool
"A containerized machine learning solution to automate loan default prediction for rural microfinance segments."
The Goal: Automated the credit scoring process for small-ticket loans (₹1,000–₹2,000) using the Joint Liability Group (JLG) model.
The Impact: Reducing manual error and improving the "Portfolio at Risk" (PAR) by identifying high-risk borrowers before loan disbursement.
Model: Logistic Regression (Scikit-Learn) for high interpretability and regulatory transparency.
Interface: Streamlit for building a cross-functional web dashboard.
Deployment: Docker for environment consistency and "plug-and-play" deployment.
ROC-AUC Score:0.57 (Baseline model).
Key Insight: The model confirms core MFI philosophy—women and older borrowers significantly reduce the risk score in this dataset.
# 1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git
# 2. Build the Docker Image
docker built midland-risk-app.
# 3. Run the Container
docker run -p 8501:8501 midland-risk-app
