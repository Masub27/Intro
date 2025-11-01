**Task:** Create two complete beginner‑friendly LiaScript lessons.

1. **`Teaching-Workflow/lessons/example-lesson.md`** – a new “Introduction to Artificial Intelligence” lesson built from the teaching guide and lesson template.  
2. **`Teaching-Workflow/lessons/03_Data_Science_Basics.md`** – a full “Data Science Basics” lesson with introduction, objectives, sections, three quizzes, reflection, and summary.

---

### 1. `Teaching-Workflow/lessons/example-lesson.md` – Introduction to Artificial Intelligence
*Added a full LiaScript lesson structure, filled every section with beginner‑level explanations, and included three interactive quizzes.*

```markdown Teaching-Workflow/lessons/example-lesson.md
# Introduction to Artificial Intelligence

## Introduction
Artificial Intelligence (AI) is the field of computer science that aims to create machines capable of performing tasks that normally require human intelligence. From voice assistants to recommendation systems, AI is becoming part of everyday life.

## Learning Objectives
- Define **Artificial Intelligence** and differentiate it from related terms.
- Identify the main sub‑fields of AI (Machine Learning, NLP, Computer Vision, etc.).
- Understand simple AI concepts such as **training data**, **models**, and **inference**.
- Recognize common real‑world AI applications.

## Section 1 – What Is AI?
AI refers to systems that can **perceive**, **reason**, **learn**, and **act**. Traditional programs follow explicit rules; AI systems instead learn patterns from data.

### Key Concepts
- **Agent** – an entity that perceives its environment and takes actions.
- **Intelligence** – the ability to achieve goals in a wide range of environments.
- **Rule‑based vs. Learning‑based** – contrast hand‑crafted logic with data‑driven models.

## Section 2 – A Brief History
| Era | Milestone |
|-----|-----------|
| 1950s | Alan Turing’s “Computing Machinery and Intelligence” |
| 1956 | Dartmouth Workshop – birth of AI as a field |
| 1980s | Expert systems dominate industry |
| 1997 | IBM Deep Blue defeats world chess champion |
| 2012 | Deep learning breakthrough with ImageNet |
| 2020s | Generative AI (ChatGPT, DALL·E) |

## Section 3 – Core Sub‑fields
- **Machine Learning (ML)** – algorithms that improve from data.
- **Natural Language Processing (NLP)** – understanding and generating human language.
- **Computer Vision** – interpreting visual information.
- **Robotics** – physical agents that act in the world.

## Section 4 – Simple AI Example: Spam Detection
1. **Collect data** – a set of emails labeled “spam” or “not spam”.
2. **Extract features** – word frequencies, presence of links, etc.
3. **Train a model** – e.g., a Naïve Bayes classifier.
4. **Inference** – the model predicts whether a new email is spam.

## Quiz 1 – Multiple Choice
?Which of the following best describes an AI **agent**?
- [ ] A piece of hardware that stores data
- [x] An entity that perceives its environment and takes actions
- [ ] A programming language
- [ ] A database management system

## Quiz 2 – True/False
?Deep learning is a subset of Machine Learning.  
- [x] True  
- [ ] False

## Quiz 3 – Fill‑in‑the‑Blank
?The 1956 conference at Dartmouth College is considered the **____** of AI.  
`Dartmouth Workshop`

## Reflection
Think about a daily task you perform (e.g., searching the web, using a map). How might AI be helping you without you noticing? Write a short paragraph in your notebook.

## Summary
Artificial Intelligence enables computers to perform tasks that normally require human intelligence. By learning from data, AI systems can adapt, improve, and solve complex problems across many domains. This lesson introduced the definition, history, sub‑fields, and a simple example to ground your understanding.

--- 

### 2. `Teaching-Workflow/lessons/03_Data_Science_Basics.md` – Data Science Basics
*Populated the file with a complete LiaScript lesson covering introduction, objectives, detailed sections, three quizzes, a reflection prompt, and a concise summary.*

```markdown Teaching-Workflow/lessons/03_Data_Science_Basics.md
# Data Science Basics

## Introduction
Data Science is the interdisciplinary practice of extracting knowledge and insights from data using statistics, programming, and domain expertise. It powers everything from business analytics to scientific discovery.

## Learning Objectives
- Explain what **Data Science** is and why it matters.
- Identify the typical **data science workflow** (collect → clean → explore → model → communicate).
- Understand basic concepts: **datasets**, **variables**, **features**, **labels**.
- Perform simple exploratory data analysis (EDA) with visualizations.
- Recognize common tools (Python, pandas, Jupyter, matplotlib).

## Section 1 – What Is Data Science?
Data Science combines:
- **Statistics** – to infer patterns.
- **Computer Science** – to process large datasets.
- **Domain Knowledge** – to ask the right questions.

### Real‑World Example
A retailer wants to predict next month’s sales. Data scientists gather historical sales, clean the data, explore trends, build a predictive model, and present actionable recommendations.

## Section 2 – The Data Science Workflow
1. **Data Collection** – APIs, databases, web scraping.
2. **Data Cleaning** – handling missing values, correcting errors.
3. **Exploratory Data Analysis (EDA)** – summary statistics, plots.
4. **Modeling** – regression, classification, clustering.
5. **Communication** – dashboards, reports, storytelling.

## Section 3 – Core Concepts
- **Dataset** – a table of rows (observations) and columns (features).
- **Feature** – an individual measurable property (e.g., age, price).
- **Label/Target** – the outcome we want to predict (e.g., churn).
- **Training vs. Test Set** – split data to evaluate model performance.

## Section 4 – Simple EDA in Python (pseudocode)
```python
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('sales.csv')

# Summary statistics
print(df.describe())

# Histogram of sales
plt.hist(df['sales'], bins=20)
plt.title('Sales Distribution')
plt.show()
```

## Quiz 1 – Multiple Choice
?Which step comes **first** in the data science workflow?
- [x] Data Collection
- [ ] Modeling
- [ ] Communication
- [ ] Data Cleaning

## Quiz 2 – True/False
?The **test set** should be used to train the model.  
- [ ] True  
- [x] False

## Quiz 3 – Short Answer
?Name one common Python library used for data manipulation.  
`pandas`

## Reflection
Identify a dataset you have access to (e.g., personal fitness tracker, public COVID‑19 data). Write down three questions you could answer with that data and how you would start the workflow.

## Summary
Data Science turns raw data into actionable insights through a systematic workflow. By mastering data collection, cleaning, exploration, modeling, and communication, you can solve real‑world problems across any domain. This lesson laid the groundwork for you to begin your own data‑driven projects.

--- 

### Summary of Key Edits
1. **Created a full AI lesson** in `example-lesson.md` with intro, objectives, four content sections, three quizzes, reflection, and summary.  
2. **Populated `03_Data_Science_Basics.md`** with a complete Data Science Basics lesson, covering workflow, core concepts, sample code, three quizzes, reflection, and summary.  
3. Ensured each file follows LiaScript markdown conventions and includes interactive quiz syntax for immediate learner feedback.