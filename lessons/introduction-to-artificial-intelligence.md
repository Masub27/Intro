````chatmode
# Introduction to Artificial Intelligence

## 🎯 Learning Objectives
- Explain what Artificial Intelligence (AI) is and why it matters.
- Identify common examples of AI in everyday life.
- Describe the basic machine learning workflow: data → model → training → inference.
- Apply a simple, hands-on example by implementing a tiny k-nearest neighbors (k-NN) classifier from scratch.
- Reflect on the limits and ethical considerations of AI systems.

## 📘 Introduction
Artificial Intelligence (AI) is a field of computer science that builds systems that can perform tasks that normally require human intelligence. These tasks include recognizing images, understanding language, and making decisions. AI is important because it helps us automate repetitive tasks, find patterns in large amounts of data, and create useful tools for medicine, education, transportation, and more.

Key context for beginners:
- AI often learns from examples called a dataset. A dataset contains features (the input) and sometimes labels (the correct answer).
- "Model" is a computer program that learns patterns from data. "Training" is the process of teaching a model from data. "Inference" (or prediction) is when the trained model is used to make decisions on new data.

## 🧠 Main Content
1. What is AI — short definition and example
   - Definition: AI means machines performing tasks that usually need human thinking.
   - Example: A smartphone camera that recognizes faces and focuses automatically.

2. Machine Learning (ML) — a common way to build AI
   - Definition: Machine Learning is a set of techniques where computers learn patterns from data instead of being explicitly programmed.
   - Supervised learning: model learns from labeled examples (e.g., emails labeled "spam" or "not spam").
   - Unsupervised learning: model finds patterns without labels (e.g., grouping similar customers).

3. Data, features, and labels — the building blocks
   - Dataset: a collection of examples (rows). Each example has features (inputs) and optionally a label (the desired output).
   - Feature: a measurable property (e.g., temperature, image pixels, word counts).
   - Label: the correct answer used for training (e.g., cat/dog, price value).

4. Training vs Inference
   - Training: adjusting a model's internal settings using labeled data so it can make correct predictions.
   - Inference: using the trained model to predict labels for new data.

5. Common AI tasks (short list)
   - Classification: choose a category (e.g., disease vs healthy).
   - Regression: predict a continuous value (e.g., house price).
   - Clustering: group similar items (e.g., customer segments).

6. Simple algorithm example — k-Nearest Neighbors (k-NN)
   - Intuition: To guess the label for a new example, look at the k closest examples in the dataset and use their labels.
   - Key idea: distance (how similar examples are) determines closeness.

## 🧩 Guided Activity / Example
```text
Task: Implement a tiny k-NN classifier from scratch in Python (no libraries required) and use it on the small dataset provided below.

Dataset (toy): each example is [feature1, feature2] and a label.
- [1, 2] -> A
- [2, 1] -> A
- [4, 4] -> B
- [5, 5] -> B

Steps:
1. Write a function to compute Euclidean distance between two points.
2. For a new point, find the k nearest points from the dataset.
3. Return the most common label among the neighbors.

Expected outcome: A short Python script that predicts the label for at least two new points and prints the results.

---

### Code (paste into a file `knn_simple.py` and run with `python knn_simple.py`):
```python
# Simple k-NN from scratch (toy example)
from collections import Counter
import math

# Training data: list of (features, label)
data = [([1, 2], 'A'), ([2, 1], 'A'), ([4, 4], 'B'), ([5, 5], 'B')]

def euclidean(a, b):
    """Compute Euclidean distance between two numeric vectors a and b."""
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))

def predict_knn(point, data, k=3):
    """Predict label for point using k nearest neighbors from data.

    Args:
        point: list of numeric features for the new example.
        data: list of (features, label) training examples.
        k: number of neighbors to consider.

    Returns:
        predicted label (most common among k nearest).
    """
    # compute distances to all training examples
    distances = [(euclidean(point, features), label) for features, label in data]
    # sort by distance
    distances.sort(key=lambda x: x[0])
    # take k nearest labels
    k_labels = [label for _, label in distances[:k]]
    # majority vote
    most_common = Counter(k_labels).most_common(1)[0][0]
    return most_common

if __name__ == '__main__':
    new_points = [[1.5, 1.5], [4.5, 4.2]]
    for p in new_points:
        label = predict_knn(p, data, k=3)
        print(f"Point {p} -> predicted label: {label}")

# What this teaches:
# - How a very simple classifier uses distances (similarity) to decide labels.
# - The difference between training data (examples) and predicting on new data (inference).
```

## Quiz / Reflection (5 items)
1. What is Artificial Intelligence (short answer)?
# Introduction to Artificial Intelligence

## 🎯 Learning Objectives
- Explain what Artificial Intelligence (AI) is and why it matters.
- Identify common examples of AI in everyday life.
- Describe the basic machine learning workflow: data → model → training → inference.
- Apply a simple, hands-on example by running a tiny k-nearest neighbors (k-NN) classifier from scratch.
- Reflect on the limits and ethical considerations of AI systems.

## 📘 Introduction
Artificial Intelligence (AI) is a field of computer science that builds systems that can perform tasks that normally require human intelligence. These tasks include recognizing images, understanding language, and making decisions. AI is important because it helps us automate repetitive tasks, find patterns in large amounts of data, and create useful tools for medicine, education, transportation, and more.

Key context for beginners:
- AI often learns from examples called a dataset. A dataset contains features (the input) and sometimes labels (the correct answer).
- "Model" is a computer program that learns patterns from data. "Training" is the process of teaching a model from data. "Inference" (or prediction) is when the trained model is used to make decisions on new data.

## 🧠 Main Content
1. What is AI — short definition and example
   - Definition: AI means machines performing tasks that usually need human thinking.
   - Example: A smartphone camera that recognizes faces and focuses automatically.

2. Machine Learning (ML) — a common way to build AI
   - Definition: Machine Learning is a set of techniques where computers learn patterns from data instead of being explicitly programmed.
   - Supervised learning: model learns from labeled examples (e.g., emails labeled "spam" or "not spam").
   - Unsupervised learning: model finds patterns without labels (e.g., grouping similar customers).

3. Data, features, and labels — the building blocks
   - Dataset: a collection of examples (rows). Each example has features (inputs) and optionally a label (the desired output).
   - Feature: a measurable property (e.g., temperature, image pixels, word counts).
   - Label: the correct answer used for training (e.g., cat/dog, price value).

4. Training vs Inference
   - Training: adjusting a model's internal settings using labeled data so it can make correct predictions.
   - Inference: using the trained model to predict labels for new data.

5. Common AI tasks (short list)
   - Classification: choose a category (e.g., disease vs healthy).
   - Regression: predict a continuous value (e.g., house price).
   - Clustering: group similar items (e.g., customer segments).

6. Simple algorithm example — k-Nearest Neighbors (k-NN)
   - Intuition: To guess the label for a new example, look at the k closest examples in the dataset and use their labels.
   - Key idea: distance (how similar examples are) determines closeness.

## 🧩 Guided Activity / Example
Task: Implement or run a tiny k-NN classifier from scratch in Python (no libraries required) and use it on the small dataset provided below.

Dataset (toy): each example is [feature1, feature2] and a label.
- [1, 2] -> A
- [2, 1] -> A
- [4, 4] -> B
- [5, 5] -> B

Steps:
1. Write or open the provided `exercises/knn_simple.py` script.
2. Run it with Python and observe the printed predictions for two new points.
3. Try changing the value of k and different new points to see how predictions change.

Expected outcome: A short Python script prints predicted labels for new points and helps illustrate the idea of "similarity-based" classification.

---

### Code
Save and run the script at `exercises/knn_simple.py` (created alongside this lesson). Example:

```powershell
python exercises\knn_simple.py
```

The script prints something like:

```
Point [1.5, 1.5] -> predicted label: A
Point [4.5, 4.2] -> predicted label: B
```

## Quiz / Reflection (5 items)
1. What is Artificial Intelligence (short answer)?
2. Name two real-world examples of AI you have used.
3. True/False: In supervised learning, the model learns from labeled examples. (Answer: True)
4. Short: What is the difference between training and inference?
5. Multiple choice: Which of these is an example of an AI task?
   A) Sorting a list using a fixed algorithm
   B) Predicting house prices from historical data
   C) Writing a letter by hand
   (Correct answer: B)

Answer key (for instructors):
1. AI is the field of building systems that can perform tasks requiring human-like intelligence (recognizing, reasoning, decision-making).
2. Example answers: voice assistants (Siri), recommendation systems (Netflix), spam filters.
3. True
4. Training adjusts a model's parameters using data; inference uses the trained model to make predictions on new data.
5. B

## ✅ Summary
- AI builds systems that can perform tasks that normally need human intelligence.
- Machine Learning is a common approach where models learn from data.
- Key concepts: dataset, features, labels, training, and inference.
- Simple algorithms like k-NN show the idea of "learn from examples" using similarity.
- Always consider limits and ethics: AI can make mistakes and learn wrong patterns from biased data.

## Further reading & next steps
- Try the guided activity with different values of k and different datasets.
- Read about neural networks and supervised learning when comfortable with these basics.
- Discuss ethics: how bias in data can affect predictions and why diverse data matters.
