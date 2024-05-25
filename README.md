# HR Analytics - Employee Attrition Prediction

## Description
This project leverages HR data analytics to interpret organizational data, uncover people-related trends, and predict employee attrition using machine learning models. The insights from this analysis help HR departments take proactive steps to retain valuable employees, thus maintaining the organization's smooth and profitable operation.

## Table of Contents
- [Introduction](#introduction)
- [Business Significance](#business-significance)
- [Project Overview](#project-overview)
- [Analytics Overview](#analytics-overview)
- [Dashboard Overview](#dashboard-overview)
- [Limitations & Potential Improvements](#limitations--potential-improvements)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [Authors and Acknowledgments](#authors-and-acknowledgments)
- [Contact Information](#contact-information)
- [Additional Documentation](#additional-documentation)

## Introduction
Employee attrition is a significant challenge for HR departments and people managers. By using machine learning models, we can predict potential attrition cases and enable HR personnel to take proactive measures to retain employees.

## Business Significance
1. **Cost Reduction**: Minimize recruitment and training costs by retaining employees.
2. **Employee Satisfaction**: Enhance satisfaction and productivity by understanding retention factors.
3. **Strategic Workforce Planning**: Improve workforce planning and talent management.
4. **Competitive Advantage**: Boost overall organizational success and stability.

## Project Overview
- **Dataset**: HR Analytics dataset.
- **Tools**:
  - **Dashboard**: Created using Power BI.
  - **ETL Process**: Data cleaning conducted using Python.
  - **Version Control**: Collaboration facilitated through GIT.
  - **Analytics Techniques**: Employed Correlation Matrix and Logistic Regression for predictive analytics.

## Analytics Overview
The analytics portion involves examining various factors that contribute to employee attrition. This includes using statistical techniques like correlation matrices to identify relationships between different variables and employing logistic regression models to predict the likelihood of employee turnover.

## Dashboard Overview
The Power BI dashboard is designed to provide an interactive and visual representation of the insights derived from the HR data. Key elements of the dashboard include:
- Attrition rates segmented by department, role, and tenure.
- Identification of key factors influencing attrition.
- Predictive analytics highlighting employees at high risk of leaving.
- Trend analysis over time.

## Limitations & Potential Improvements
While the project offers significant insights, there are limitations such as the quality and completeness of the data, the complexity of accurately predicting human behavior, and the need for continuous model improvement. Future improvements could involve incorporating more diverse datasets, refining the machine learning models, and expanding the dashboard features.

## Installation
To run this project locally, follow these steps:
1. Clone the repository: `git clone https://github.com/theabandonedpluto/DSConsProject`
2. Navigate to the project directory: `cd DSConsProject`
3. Create a virtual environment (optional but recommended): `python -m venv env`
4. Activate the virtual environment:
   - On Windows: `env\Scripts\activate`
   - On macOS/Linux: `source env/bin/activate`
5. Install the required dependencies: `pip install -r requirements.txt`
6. Open the Power BI dashboard file: `HR_Analytics_Final.pbix`

## Usage
1. **Data Cleaning**: Run the `data_cleaning.py` script to preprocess the HR data.
2. **Model Training**: Execute the `train_model.py` script to train and evaluate the machine learning model.
3. **Dashboard**: Open the Power BI dashboard to interact with the visualizations.

## Features
- **Predictive Analytics**: Machine learning models to predict employee attrition.
- **Data Visualization**: Interactive Power BI dashboard for data insights.
- **Data Cleaning Scripts**: Automated scripts for preprocessing HR data.

## Contributing
We welcome contributions from the community. Please follow these guidelines:
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit them: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-branch`
5. Submit a pull request.

## Authors and Acknowledgments
- **Authors**: Pearly Tantra, Yamini Kuntal
- **Acknowledgments**: We thank the contributors and the community for their valuable feedback and support.

## Contact Information
For any queries or support, please contact:
- Pearly Tantra - [pearly.tantra@student.uw.edu.pl](mailto:pearly.tantra@example.com)
- Yamini Kuntal - [yamini.kuntal@student.uw.edu.pl](mailto:yamini.kuntal@example.com)

## Additional Documentation
- [Power BI Documentation](https://docs.microsoft.com/en-us/power-bi/)
- [Machine Learning with Python](https://scikit-learn.org/stable/user_guide.html)
- [HR Analytics Best Practices](https://www.forbes.com/advisor/business/hr-analytics/)
  
---

For more details, visit the project repository on [GitHub](https://github.com/theabandonedpluto/DSConsProject).
