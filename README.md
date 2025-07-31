# 🛡️ NSAP Eligibility Prediction using Machine Learning

This project predicts eligibility for **National Social Assistance Programme (NSAP)** schemes using Machine Learning. It leverages historical welfare data to build and deploy a model that can assist in identifying potential beneficiaries with greater speed, transparency, and accuracy.



---

## 🧠 Project Objective

To automate the eligibility prediction process for NSAP schemes such as:
- **IGNOAPS** – Indira Gandhi National Old Age Pension Scheme  
- **IGNWPS** – Indira Gandhi National Widow Pension Scheme  
- **IGNDPS** – Indira Gandhi National Disability Pension Scheme  

By analyzing scheme-level and regional-level data, this project helps ensure fair and efficient distribution of government welfare benefits.

---
## 🔗 Live Model Deployment

The final model — a **Snap AutoAI Random Forest Classifier** — is deployed and accessible via IBM watsonx.ai as an online endpoint.

### 🛰️ Deployment Details

- **Platform**: IBM watsonx.ai Studio  
- **Model**: AutoAI - Random Forest  
- **Deployment Name**: `NSAP_Prediction`  
- **Deployment Type**: Online  
- **API Type**: Multiclass Classification  
- **Prediction Categories**: `IGNOAPS`, `IGNWPS`, `IGNDPS`    
- **Region**: Sydney  
- **Status**: ✅ Deployed

---

## 📡 API Access

### 📍 Endpoints
> You can call these endpoints using your IAM token.

- **Public Endpoint**: https://au-syd.ml.cloud.ibm.com/ml/v4/deployments/2277dd73-3170-4327-8238-2d7c7db760fa/predictions?version=2021-05-01
- ## 🔐 API Authorization & Usage

The deployed model is accessible via a secure endpoint on IBM watsonx.ai. You will need to generate an **IAM Token** for authorization.

### 🔑 Authorization
- **Type**: Bearer Token (`IAM`)
- **Headers Required**:
  - Content-Type: application/json
  - Authorization: Bearer <IAM_TOKEN>

---

### 🧪 Example Input Format

```json
{
  "input_data": [
    {
      "fields": ["finyear", "lgdstatecode", "statename", "lgddistrictcode", "districtname", "totalbeneficiaries", "totalmale", "totalfemale"],
      "values": [
        ["2025-2026", 1, "JAMMU AND KASHMIR", 10, "POONCH", 310, 211, 99]
      ]
    }
  ]
}
````

✅ Sample Prediction Output

| Prediction | Confidence |
| ---------- | ---------- |
| IGNOAPS    | 100%       |





## 📊 Dataset Overview

Collected from multiple Indian states and union territories, the dataset includes scheme performance indicators like:

### 🔑 Key Features:
- `finyear`: Financial Year  
- `lgdstatecode`, `statename`  
- `lgddistrictcode`, `districtname`  
- `schemename`: NSAP Scheme Name  
- `total_applicants`, `eligible_count`, `ineligible_count`  
- `aadhar_seeded`, `rejected`, `pending`  
- `total_disbursed`, `total_target`

> The dataset has been cleaned, preprocessed, and extended with new entries to improve model generalization.

---

## 🛠️ Tools & Technologies

- **Python 3.11**
- **Pandas**, **NumPy** – Data Handling
- **Matplotlib**, **Seaborn** – Data Visualization
- **Scikit-learn** – Machine Learning Models
- **Jupyter Notebook** – Analysis & Prototyping
- **GitHub** – Version Control
- **IBM Watsonx.ai Studio** – Model Deployment

---

## 📌 ML Workflow

### 1. Data Preprocessing
- Null value imputation
- Encoding categorical variables
- Normalization and scaling

### 2. Exploratory Data Analysis (EDA)
- Scheme-wise trend analysis
- State and district-level visualization
- Correlation analysis

### 3. Model Building
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier ✅
- Support Vector Machine (SVM)

### 4. Evaluation Metrics
- Accuracy, Precision, Recall
- Confusion Matrix
- Cross-Validation Scores

---

## 📈 Model Performance

| Model               | Accuracy |
|--------------------|----------|
| Logistic Regression| 84.3%    |
| Decision Tree      | 87.1%    |
| Random Forest      | 94.8% ✅ |
| SVM                | 85.7%    |

> Random Forest achieved the best accuracy and generalization.


## 🔮 Future Scope

- Integration with a user-facing web portal for eligibility checking
- Include socio-economic variables: occupation, income, health, caste, etc.
- Regional disparity analysis using geospatial data
- Mobile dashboard for local administrators

---

## ✅ Conclusion

- NSAP datasets provide rich potential for machine learning applications
- Automation boosts accuracy and transparency in welfare delivery
- Technology can empower better governance and inclusion

---

## 🏅 Internship & Acknowledgments

This project was developed during my internship with **Edunet Foundation** via **IBM SkillsBuild** program.

### Tools Provided:
- IBM Cloud and Watsonx.ai Studio  
- Agentic AI Tools  
- AutoAI for model building and comparison  

🎓 **Credly Certificate**: _Getting Started with AI and Cloud_

---

## 📚 References

- [NSAP Official Website](https://nsap.nic.in)
- [Open Government Data Platform India](https://data.gov.in)
- [Scikit-learn Documentation](https://scikit-learn.org)
- IBM SkillsBuild & Edunet Foundation Materials

---
## 👤 Author

**Akash Kumar Singh**  
B.Tech Student, AKGEC  
Intern at Edunet Foundation (IBM SkillsBuild Program)  
🔗 [GitHub Profile](https://github.com/Aakash4518)  
📧 Email: akash2310016-d@akgec.ac.in


