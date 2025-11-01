"""Very small k-NN example used by the lesson `Introduction to Artificial Intelligence`.

Run: python exercises/knn_simple.py

What this teaches:
- How a very simple classifier uses distances (similarity) to decide labels.
- The difference between training data (examples) and predicting on new data (inference).
"""
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
