# NSAP Eligibility Prediction using Machine Learning

This project aims to **predict eligibility for schemes under the National Social Assistance Programme (NSAP)** using Machine Learning techniques. The NSAP is a flagship welfare initiative by the Government of India that provides financial assistance to the elderly, widows, and persons with disabilities living below the poverty line (BPL).

## 🧠 Project Objective

The main goal is to build a model that can predict whether a person or household is eligible for various NSAP schemes based on historical data. This helps automate and optimize the targeting process for welfare schemes.

---

## 📊 Dataset

The dataset includes records from multiple Indian states and union territories across various schemes such as:
- IGNOAPS (Old Age Pension)
- IGNWPS (Widow Pension)
- IGNDPS (Disability Pension)

### Sample Features:
- `finyear`: Financial Year
- `lgdstatecode`: State Code
- `statename`: State Name
- `lgddistrictcode`: District Code
- `districtname`: District Name
- `schemename`: NSAP Scheme Name
- `total_applicants`: Number of Applicants
- `eligible_count`: Eligible People
- `ineligible_count`: Not Eligible
- `aadhar_seeded`: Aadhaar Seeded Accounts
- `rejected`: Rejected Applications
- `pending`: Pending Applications
- `total_disbursed`: Total Benefits Disbursed
- `total_target`: Total Target Beneficiaries

The dataset has been cleaned, preprocessed, and augmented with additional inputs from various regions for better generalization.

---

## 🧪 Tech Stack Used

- **Python 3.11**
- **Pandas** & **NumPy** for Data Manipulation
- **Matplotlib** & **Seaborn** for Data Visualization
- **Scikit-learn** for ML Modeling
- **Jupyter Notebook** for Analysis
- **GitHub** for Version Control
- **IBM Cloud Services** (during Edunet Foundation Internship)

---

## 🛠️ Features & Steps

### 1. Data Preprocessing
- Handling missing values
- Feature encoding and normalization
- Outlier detection and correction

### 2. Exploratory Data Analysis
- Scheme-wise distribution across states
- Eligibility trend visualization
- Correlation matrix to identify key indicators

### 3. Model Building
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Machines (SVM)

### 4. Model Evaluation
- Accuracy, Precision, Recall
- Confusion Matrix
- Cross-validation scores

### 5. Final Output
- Predict eligibility using new input data
- Generate reports with graphical summaries

---

## 📈 Results

| Model               | Accuracy |
|--------------------|----------|
| Logistic Regression| 84.3%    |
| Decision Tree      | 87.1%    |
| Random Forest      | 94.8%    |
| SVM                | 85.7%    |

The **Random Forest Classifier** outperformed others in terms of overall accuracy and generalization.

---

## 🔮 Future Scope

- Integrate with a web portal for real-time eligibility check.
- Include socio-economic attributes such as occupation, health status, and caste category.
- Use geospatial data to analyze regional disparities.
- Build a mobile-friendly dashboard for scheme administrators.

---

## 📌 Conclusion

- NSAP data has rich potential for ML-based prediction systems.
- Automation can enhance the accuracy and speed of benefit disbursement.
- Ensures fair and transparent allocation of welfare schemes.

---

## 🏅 Internship & Acknowledgment

This project was developed as part of my internship under the **Edunet Foundation** via **IBM SkillsBuild**. I had access to:
- IBM Cloud and Watsonx.ai
- Agentic AI Tools
- AutoAI for model experimentation

**Credly Certificate**: _Getting Started with AI and Cloud_ ✅

---

## 📚 References

- [NSAP Official Website](https://nsap.nic.in)
- [Open Government Data (OGD) Platform India](https://data.gov.in)
- IBM SkillsBuild & Edunet Foundation Resources
- Scikit-learn Documentation

---

## 📦 How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/Aakash4518/PREDICTING-ELIGIBILITY-FOR-NSAP-SCHEMES-USING-MACHINE-LEARNING.git
   cd PREDICTING-ELIGIBILITY-FOR-NSAP-SCHEMES-USING-MACHINE-LEARNING
