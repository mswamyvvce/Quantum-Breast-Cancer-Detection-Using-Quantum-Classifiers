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

| Model         | Expected Accuracy |
| ------------- | ----------------- |
| Classical SVM | 94–98%            |
| VQC           | 90–97%            |
| QSVM          | 95–98%            |

Actual results may vary depending on simulator settings and preprocessing parameters.

---

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

Vidyavardhaka College of Engineering, Mysuru, India
