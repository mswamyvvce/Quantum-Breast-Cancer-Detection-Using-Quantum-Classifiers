# QBreast-QC: Quantum Breast Cancer Detection Using Quantum Classifiers

## Overview

QBreast-QC is a Quantum Machine Learning (QML) framework for breast cancer detection and classification using quantum classifiers. The project leverages Variational Quantum Classifiers (VQC) and Quantum Support Vector Machines (QSVM) to classify breast cancer samples as benign or malignant using the Wisconsin Breast Cancer Dataset available in Scikit-learn.

The framework aims to explore the effectiveness of quantum-enhanced machine learning models in biomedical disease classification and compare their performance against classical machine learning approaches.

---

## Objectives

* Develop a quantum machine learning framework for breast cancer detection.
* Implement Variational Quantum Classifiers (VQC).
* Implement Quantum Support Vector Machines (QSVM).
* Compare quantum and classical classification performance.
* Evaluate model robustness using quantum simulation environments.
* Generate reproducible experimental results for biomedical quantum computing research.

---

## Dataset

This project uses the Wisconsin Breast Cancer Dataset provided by Scikit-learn.

### Dataset Characteristics

* Total Samples: 569
* Features: 30
* Classes: 2

#### Class Labels

| Label | Class     |
| ----- | --------- |
| 0     | Malignant |
| 1     | Benign    |

The dataset is loaded directly from Scikit-learn and does not require manual downloading.

---

## Methodology

### Data Preprocessing

* Feature normalization using Min-Max Scaling.
* Dimensionality reduction using Principal Component Analysis (PCA).
* Training and testing split.

### Classical Model

* Support Vector Machine (SVM)

### Quantum Models

#### Variational Quantum Classifier (VQC)

Components:

* ZZ Feature Map
* Real Amplitudes Ansatz
* SPSA Optimizer
* Aer Quantum Simulator

#### Quantum Support Vector Machine (QSVM)

Components:

* Quantum Kernel
* Fidelity Quantum Kernel
* Classical SVM Decision Function

---

## Project Structure

```text
QBreast-QC/
│
├── src/
│   ├── data_loader.py
│   ├── classical_svm.py
│   ├── vqc.py
│   ├── qsvm.py
│   └── main.py
│
├── results/
│   ├── confusion_matrix.png
│   ├── roc_curve.png
│   └── accuracy_comparison.png
│
├── README.md
├── requirements.txt
└── LICENSE
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/QBreast-QC.git
cd QBreast-QC
```

### Create Virtual Environment

```bash
python -m venv qenv
```

### Activate Environment

Windows:

```bash
qenv\Scripts\activate
```

Linux/macOS:

```bash
source qenv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Required Packages

* qiskit
* qiskit-machine-learning
* qiskit-aer
* numpy
* pandas
* scikit-learn
* matplotlib
* seaborn

---

## Running the Project

Execute:

```bash
python src/main.py
```

The program will:

1. Load and preprocess the dataset.
2. Train a classical SVM classifier.
3. Train a Variational Quantum Classifier.
4. Train a Quantum Support Vector Machine.
5. Evaluate classification performance.
6. Generate performance visualizations.

---

## Evaluation Metrics

The following metrics are reported:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* ROC Curve
* Training Time

---

## Expected Results

============================================================
Loading Breast Cancer Dataset
============================================================
Original Shape: (569, 30)
Reduced Shape: (569, 4)
Train Samples: 455
Test Samples : 114

======================================================================
BREAST CANCER DATASET
======================================================================
Original Shape : (569, 30)
Reduced Shape : (569, 4)
Training Samples : 455
Testing Samples  : 114

======================================================================
CLASSICAL SUPPORT VECTOR MACHINE
======================================================================
Accuracy : 96.49 %

Classification Report
              precision    recall  f1-score   support

           0       0.95      0.95      0.95        42
           1       0.97      0.97      0.97        72

    accuracy                           0.96       114
   macro avg       0.96      0.96      0.96       114
weighted avg       0.96      0.96      0.96       114



======================================================================
VARIATIONAL QUANTUM CLASSIFIER
======================================================================
Training VQC...
Accuracy : 70.18 %

Classification Report
              precision    recall  f1-score   support

           0       0.79      0.26      0.39        42
           1       0.69      0.96      0.80        72

    accuracy                           0.70       114
   macro avg       0.74      0.61      0.60       114
weighted avg       0.73      0.70      0.65       114



======================================================================
QUANTUM SUPPORT VECTOR MACHINE
======================================================================
Training QSVM...
Accuracy : 86.84 %

Classification Report
              precision    recall  f1-score   support

           0       0.86      0.76      0.81        42
           1       0.87      0.93      0.90        72

    accuracy                           0.87       114
   macro avg       0.87      0.85      0.85       114
weighted avg       0.87      0.87      0.87       114



======================================================================
MODEL COMPARISON
======================================================================
SVM  Accuracy : 0.9649
VQC  Accuracy : 0.7018
QSVM Accuracy : 0.8684

Results saved in results/ folder

Generated Files:
results/svm_confusion_matrix.png
results/vqc_confusion_matrix.png
results/qsvm_confusion_matrix.png
results/accuracy_comparison.png
results/model_accuracy.csv

Project Completed Successfully.

Results Saved Successfully.

## Applications

* Computer-Aided Diagnosis
* Biomedical Data Analytics
* Quantum Machine Learning Research
* Healthcare Decision Support Systems
* Quantum-Enhanced Disease Classification
---
## Future Enhancements

* Noise-aware quantum learning
* Adaptive quantum circuit optimization
* Explainable quantum classification
* Multi-class disease diagnosis
* Cross-simulator benchmarking using Qiskit, PennyLane, and Cirq
---
## Citation

If you use this work in your research, please cite:

```bibtex
@software{QBreastQC2026,
  title={QBreast-QC: Quantum Breast Cancer Detection Using Quantum Classifiers},
  author={Mahadevaswamy S},
  year={2026}
}
```
---
## License

This project is distributed under the MIT License.

---

## Author

Mahadevaswamy S

Department of Electronics and Communication Engineering

Vidyavardhaka College of Engineering, Mysuru, Karnataka, India
