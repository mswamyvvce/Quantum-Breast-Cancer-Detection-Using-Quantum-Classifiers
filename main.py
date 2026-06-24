import warnings
warnings.filterwarnings("ignore")

# ==========================
# IMPORTS
# ==========================
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split

from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# Qiskit Imports
from qiskit.circuit.library import ZZFeatureMap, RealAmplitudes
from qiskit_algorithms.optimizers import SPSA
from qiskit_machine_learning.algorithms import VQC


# ==========================
# LOAD DATASET
# ==========================
print("=" * 60)
print("Loading Breast Cancer Dataset")
print("=" * 60)

data = load_breast_cancer()

X = data.data
y = data.target

print("Original Shape:", X.shape)

# ==========================
# NORMALIZATION
# ==========================
scaler = MinMaxScaler()

X = scaler.fit_transform(X)

# ==========================
# PCA REDUCTION
# ==========================
pca = PCA(n_components=4)

X = pca.fit_transform(X)

print("Reduced Shape:", X.shape)

# ==========================
# TRAIN TEST SPLIT
# ==========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("Train Samples:", len(X_train))
print("Test Samples :", len(X_test))

# ======================================================
# CLASSICAL SVM
# ======================================================
print("\n")
print("=" * 60)
print("CLASSICAL SVM")
print("=" * 60)

svm = SVC()

svm.fit(X_train, y_train)

svm_pred = svm.predict(X_test)

svm_acc = accuracy_score(y_test, svm_pred)

print("SVM Accuracy:", round(svm_acc * 100, 2), "%")

print("\nClassification Report")
print(classification_report(y_test, svm_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, svm_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=data.target_names
)

disp.plot()

plt.title("Classical SVM")
plt.savefig("svm_confusion_matrix.png")
plt.close()

# ======================================================
# QUANTUM VQC
# ======================================================
print("\n")
print("=" * 60)
print("VARIATIONAL QUANTUM CLASSIFIER")
print("=" * 60)

feature_map = ZZFeatureMap(
    feature_dimension=4,
    reps=2
)

ansatz = RealAmplitudes(
    num_qubits=4,
    reps=2
)

optimizer = SPSA(
    maxiter=50
)

vqc = VQC(
    feature_map=feature_map,
    ansatz=ansatz,
    optimizer=optimizer
)

print("Training VQC...")

vqc.fit(X_train, y_train)

vqc_pred = vqc.predict(X_test)

vqc_acc = accuracy_score(y_test, vqc_pred)

print("VQC Accuracy:", round(vqc_acc * 100, 2), "%")

print("\nClassification Report")
print(classification_report(y_test, vqc_pred))

cm_q = confusion_matrix(y_test, vqc_pred)

disp_q = ConfusionMatrixDisplay(
    confusion_matrix=cm_q,
    display_labels=data.target_names
)

disp_q.plot()

plt.title("Quantum VQC")
plt.savefig("vqc_confusion_matrix.png")
plt.close()

# ======================================================
# COMPARISON
# ======================================================
print("\n")
print("=" * 60)
print("MODEL COMPARISON")
print("=" * 60)

print(f"SVM Accuracy : {svm_acc:.4f}")
print(f"VQC Accuracy : {vqc_acc:.4f}")

plt.figure(figsize=(6,4))

models = ["SVM", "VQC"]
scores = [svm_acc, vqc_acc]

plt.bar(models, scores)

plt.ylabel("Accuracy")
plt.title("Accuracy Comparison")

plt.savefig("accuracy_comparison.png")

plt.show()

print("\nResults Saved Successfully.")
