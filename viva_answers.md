# Possible Viva Questions – ML Hackathon & Company Questions

## A. Dataset Loading & Understanding

**1. What is the objective of your machine learning problem?**
The objective is to analyze a user's skills and provide job role recommendations while identifying skill gaps and readiness levels. This helps candidates understand what missing skills they need to acquire to become job-ready for a specific role.

**2. What is the target variable in your dataset?**
Depending on the specific predictive model, the target variable is typically `readiness_level` (e.g., Job Ready, Intermediate, Developing) or `target_role` (e.g., Frontend Developer, Data Engineer).

**3. Is your problem classification, regression, or clustering? Why?**
It is primarily a **Classification** problem because we are predicting categorical variables, such as recommending a discrete job role (`target_role`) or classifying a candidate into specific readiness tiers (`readiness_level`). Job recommendation can also be framed as a similarity/ranking problem, but predicting discrete outcomes makes it classification.

**4. How many records and features are present in the dataset?**
The dataset contains 10,000 records (rows) and 13 features (columns), representing different skill scores, match percentages, and categorized levels.

**5. Which features are numerical and which are categorical?**
- **Numerical:** `technical_skills_score`, `programming_skills_score`, `problem_solving_score`, `projects_score`, `communication_score`, `education_score`, `experience_score`, `skill_match_percentage`, `job_readiness_percentage`.
- **Categorical:** `target_role`, `readiness_level`, `strongest_skill`, `missing_skill`.

**6. How did you identify missing values?**
Missing values were identified using Pandas functions like `df.isnull().sum()` or `df.isna().sum()`, which return the count of null values in each column. Visual tools like `missingno` can also be used.

**7. What data-quality issues did you observe?**
Issues commonly observed include missing data (e.g., users not entering education), inconsistent formatting in text fields, outliers in scores, and class imbalance in `target_role`.

**8. Why is understanding the dataset important before model building?**
Understanding the dataset (Exploratory Data Analysis) is crucial to uncover patterns, identify anomalies/outliers, understand feature relationships, and determine the correct preprocessing steps required. Feeding garbage data to a model results in garbage output (GIGO).

**9. Which feature appears to have the strongest relationship with the target?**
For predicting `readiness_level`, features like `job_readiness_percentage`, `technical_skills_score`, and `skill_match_percentage` generally have the strongest correlation.

**10. Did you identify any duplicate records or irrelevant columns?**
Duplicates can be checked using `df.duplicated().sum()`. Columns that act as unique identifiers (like user IDs or random hashes) are irrelevant for training and should be dropped.

---

## B. Data Preprocessing

**11. How did you handle missing values?**
Missing numerical values were imputed using the median or mean, while missing categorical values (like `missing_skill`) were imputed with the mode or a placeholder like "Unknown".

**12. Why did you choose mean/median/mode imputation or another technique?**
Mean is used for normally distributed numerical data. Median is preferred when data has outliers (as it's robust to them). Mode is the standard central tendency measure for categorical data.

**13. How did you handle categorical variables?**
Categorical variables (like `target_role` and `strongest_skill`) were converted to numerical formats using techniques like One-Hot Encoding (for nominal data) or Label Encoding (for ordinal data like `readiness_level`).

**14. What is the difference between Label Encoding and One-Hot Encoding?**
- **Label Encoding** assigns an integer to each category (e.g., 0, 1, 2). It is useful for ordinal data where order matters.
- **One-Hot Encoding** creates a new binary column for each category. It is used for nominal data to prevent the model from falsely assuming a natural ordering.

**15. Why is feature scaling required for some ML algorithms?**
Algorithms that compute distances (like KNN, SVM) or use gradient descent (like Neural Networks, Logistic Regression) are sensitive to the scale of features. Scaling ensures that features with larger numeric ranges don't disproportionately dominate the learning process.

**16. Which scaling technique did you use and why?**
StandardScaler (Z-score normalization) or MinMaxScaler. StandardScaler is generally preferred when features follow a normal distribution or when using models like SVM/Logistic Regression.

**17. How did you detect and handle outliers?**
Outliers can be detected using Boxplots, Scatter plots, or the IQR (Interquartile Range) method. They can be handled by capping/flooring values at percentiles or using robust algorithms (like Random Forests) that are not heavily affected by them.

**18. What is data leakage? Did your preprocessing introduce any leakage?**
Data leakage occurs when information from the test dataset is used to train the model, resulting in overly optimistic performance. To prevent this, preprocessing steps (like scaling and imputation) must be `fit` ONLY on the training data and then `transformed` on the test data.

**19. Why should preprocessing be fitted only on the training data?**
Fitting on the entire dataset incorporates information from the testing set into the scaling/imputation parameters (like global mean/variance), which causes data leakage and invalidates the test set.

**20. How did you divide the data into training and testing sets?**
Using `train_test_split` from `sklearn.model_selection`, typically with an 80-20 or 70-30 split. Stratified sampling can be used to ensure both sets have the same proportion of target classes.

---

## C. Feature Engineering & Selection

**21. Why did you select these particular features?**
Features like skill scores, education, and experience directly reflect a candidate's competency. Extracted skills directly impact the job matching process, making them highly predictive for our classification objective.

**22. What is feature selection?**
It is the process of selecting a subset of the most relevant features (variables) for use in model construction, discarding irrelevant or redundant ones to simplify the model and reduce overfitting.

**23. What is the difference between feature selection and feature extraction?**
- **Feature Selection:** Keeps a subset of the original features without changing them (e.g., dropping `communication_score`).
- **Feature Extraction:** Transforms the original features into a new, lower-dimensional space (e.g., PCA creating Principal Components from existing features).

**24. How can irrelevant features affect model performance?**
They introduce "noise," which can cause models to overfit (learning patterns that don't exist), increase computational training time, and degrade overall accuracy.

**25. What is correlation, and how did you use it in your project?**
Correlation measures the linear relationship between two variables. A correlation matrix/heatmap is used to identify highly correlated independent variables (multicollinearity) or features strongly correlated with the target variable.

**26. Did you remove highly correlated features? Why?**
Yes (if applicable). If two features (e.g., `skill_match_percentage` and `job_readiness_percentage`) have a >0.9 correlation, they provide redundant information. Removing one reduces multicollinearity, making the model more stable and interpretable.

**27. What is dimensionality reduction?**
It is the process of reducing the number of input variables in a dataset, which can be done via feature selection or feature extraction.

**28. Why might reducing the number of features improve a model?**
It mitigates the "Curse of Dimensionality", reduces training time, makes the model simpler, and helps prevent overfitting by removing noisy or redundant data.

**29. In PCA, what does explained variance mean?**
Explained variance is the amount of variance (information or spread) in the original dataset that is captured by a principal component. We typically select enough components to explain 90-95% of the total variance.

**30. Why is scaling particularly important before applying PCA?**
PCA seeks to maximize variance. If features are not scaled, variables with larger absolute scales will artificially dominate the principal components simply due to their magnitude.

---

## D. Model Implementation

**31. Why did you select your particular machine learning algorithm?**
Assuming Random Forest/XGBoost for this dataset: Random Forests handle both categorical and numerical data well, are robust against outliers, capture non-linear relationships between skills and job readiness, and are less prone to overfitting compared to single decision trees.

**32. How does your selected algorithm work at a high level?**
- **Decision Tree:** Splits data based on feature thresholds to maximize information gain until a decision is reached.
- **Random Forest:** An ensemble method that trains multiple decision trees on random subsets of data and features, then outputs the majority vote (classification) or average (regression).

**33. What are the major assumptions or limitations of your model?**
Tree-based models don't assume linear relationships or normally distributed data. However, they can be a black box (hard to interpret compared to linear models) and can struggle with extrapolation (predicting values outside the training range).

**34. What is the difference between training data and testing data?**
Training data is the subset used to build and train the model. Testing data is a separate, unseen subset used to evaluate the model's generalization capabilities.

**35. What is overfitting?**
Overfitting occurs when a model learns the training data *too* well, memorizing noise and specific details rather than general patterns. It performs exceptionally well on training data but poorly on unseen test data.

**36. What is underfitting?**
Underfitting occurs when a model is too simple to capture the underlying patterns in the data. It performs poorly on both training and test data.

**37. How can you reduce overfitting?**
- Get more training data.
- Reduce model complexity (e.g., limit tree depth).
- Apply Regularization (L1/L2).
- Use cross-validation.
- Remove redundant features.

**38. What is the purpose of hyperparameter tuning?**
To find the optimal set of hyperparameters (e.g., max_depth, learning rate) that maximize the model's performance and generalization on unseen data. Methods include Grid Search or Random Search.

**39. What is the difference between a parameter and a hyperparameter?**
- **Parameter:** Learned automatically by the model during training (e.g., split points in a tree).
- **Hyperparameter:** Set manually by the developer *before* training begins (e.g., number of trees in a forest).

**40. Why might an ensemble model perform better than a single model?**
Ensemble models combine the predictions of multiple weak models to reduce variance and bias. By aggregating results, they cancel out individual errors and yield more robust predictions.

---

## E. Evaluation & Interpretation

**41. Which evaluation metric did you use and why?**
For an imbalanced classification problem, **F1-Score** or **ROC-AUC** is preferred over Accuracy. F1-Score balances Precision and Recall, which is vital if falsely predicting someone is "Job Ready" is costly.

**42. What is a confusion matrix?**
A table used to describe the performance of a classification model. It shows True Positives (TP), True Negatives (TN), False Positives (FP), and False Negatives (FN).

**43. Explain TP, TN, FP, and FN in your problem.**
Predicting if someone is "Job Ready" (Positive):
- **TP:** Model predicts Job Ready, and they actually are Job Ready.
- **TN:** Model predicts Not Ready, and they actually are Not Ready.
- **FP (Type I Error):** Model predicts Job Ready, but they are NOT (risky for hiring).
- **FN (Type II Error):** Model predicts Not Ready, but they ARE Job Ready (missed opportunity).

**44. What is the difference between precision and recall?**
- **Precision:** Out of all positive *predictions*, how many were actually correct? (TP / (TP + FP))
- **Recall (Sensitivity):** Out of all *actual* positives, how many did the model find? (TP / (TP + FN))

**45. When would recall be more important than precision?**
When missing a positive case is highly dangerous or costly (e.g., cancer detection—you want high recall to catch every sick person, even if it means some false alarms).

**46. When would precision be more important than recall?**
When false positives are very costly (e.g., spam filtering—you demand high precision before labeling an important email as spam).

**47. What is the F1-score?**
The harmonic mean of Precision and Recall. It ranges from 0 to 1 and is a good single metric when you need a balance between Precision and Recall.

**48. Why can accuracy be misleading for an imbalanced dataset?**
If 95% of candidates are "Developing" and 5% are "Job Ready", a dumb model predicting "Developing" for everyone will have 95% accuracy, but it completely fails at identifying "Job Ready" candidates.

**49. How did you compare different models?**
By evaluating them on the same test set using cross-validation and comparing metrics like F1-score, Precision, Recall, and overall training/inference speed.

**50. If your model performs poorly after deployment, what would you investigate first?**
I would check for **Data Drift** (did the real-world input data change?), investigate data pipelines for bugs, check if preprocessing steps match training, and evaluate if the business environment changed.

---

## Company Specific Viva Questions

### Data Engineering
**What is Apache Kafka and how is it used in data pipelines? (Akaike Technologies)**
Apache Kafka is a distributed event streaming platform used to handle high-throughput, real-time data feeds. In data pipelines, it acts as a buffer/message broker that reliably ingests, stores, and routes massive streams of data from producers to consumers in real-time.

**What is Apache Airflow and how is it used for workflow orchestration? (Akaike Technologies)**
Apache Airflow is an open-source platform to programmatically author, schedule, and monitor workflows as Directed Acyclic Graphs (DAGs). It automates ETL pipelines, ensuring tasks execute in the correct order, handling retries and alerts.

**How do you design a data ingestion pipeline and file storage architecture in the cloud? (Akaike Technologies)**
1. **Ingestion:** API gateways/streaming tools (Kafka/Kinesis) for real-time, batch tools for bulk data.
2. **Storage:** Raw data in object storage (AWS S3, GCS).
3. **Processing:** Spark/Airflow processes raw data.
4. **Data Warehouse:** Cleaned data is loaded into Snowflake or BigQuery for ML consumption.

### Deep Learning
**How do you evaluate a deep learning model using accuracy, F1-score, and confusion matrix? (Big Vision, Akaike Technologies)**
Compare test set predictions to ground truth labels. The Confusion Matrix visualizes TP, TN, FP, FN. Accuracy gives a general overview, while the F1-score provides a reliable metric across classes, especially useful for class imbalance.

**What is backpropagation and how are gradients computed during model training? (Big Vision)**
Backpropagation calculates the gradient of the loss function with respect to each weight using the chain rule of calculus. It iterates backward from the output layer to the input layer, distributing the error so the optimizer can update weights to minimize loss.

**How do you build an LSTM/GRU-based deep learning model for multi-class text classification? (Akaike Technologies)**
1. **Preprocessing:** Tokenize, remove stop words, pad sequences.
2. **Embedding:** Convert words to dense vectors.
3. **RNN Layer:** Add LSTM/GRU layer to capture sequential context.
4. **Dense Layer:** Add fully connected layer with a Softmax activation.
5. **Compile:** Use `categorical_crossentropy` loss and Adam optimizer.

**What is ResNet and how is it used for tumor detection or similar computer vision tasks? (Akaike Technologies)**
ResNet uses "skip connections" to bypass some layers, solving the vanishing gradient problem and allowing very deep networks. In tumor detection, a pre-trained ResNet extracts complex features from medical scans, followed by a custom layer to classify tumor presence.

### Machine Learning
**What is bagging and boosting and what is the difference between them? (Akaike Technologies)**
- **Bagging:** Trains multiple independent models in parallel on random subsets of data (e.g., Random Forest) to reduce variance.
- **Boosting:** Trains models sequentially, where each new model corrects errors made by the previous ones (e.g., XGBoost) to reduce bias.

**What are ensemble techniques and how do they improve model performance? (Akaike Technologies)**
Ensemble techniques combine predictions of multiple baseline models to produce a single, stronger prediction. They improve performance by minimizing individual biases, reducing variance, and avoiding overfitting.

**What are model evaluation metrics such as accuracy, precision, recall, F1-score, and confusion matrix? (Akaike Technologies)**
*(Refer to questions 42-47).* These metrics quantify how well a supervised learning model generalizes to new data, helping engineers select the best model based on the business problem.

**What is supervised learning and how does it differ from unsupervised learning? (Klyonix)**
Supervised learning uses labeled data to train a model to predict outputs for new inputs. Unsupervised learning uses unlabeled data to discover hidden patterns or groupings.

**What are the different types of machine learning: supervised, unsupervised, and reinforcement learning? (Finastra, Klyonix)**
- **Supervised:** Learning from labeled data (Regression, Classification).
- **Unsupervised:** Finding patterns in unlabeled data (Clustering).
- **Reinforcement Learning:** An agent learns to make decisions by taking actions to maximize cumulative rewards (e.g., autonomous driving).

**What is a Decision Tree and how does it work? (Akaike Technologies)**
A Decision Tree splits the dataset into smaller subsets based on the feature that provides the highest Information Gain. This recursive splitting continues until a stopping criterion is met, culminating in "leaf nodes" representing the final prediction.
