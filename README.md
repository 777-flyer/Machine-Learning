# Machine Learning: Implementations and Explorations

A comprehensive collection of machine learning algorithms implemented from scratch as part of CSE427: Machine Learning coursework. This repository demonstrates fundamental ML concepts through hands-on implementations, exploratory data analysis, and practical applications.

## Overview

This repository contains implementations of core machine learning algorithms built from the ground up, emphasizing understanding of underlying mathematical principles and algorithmic mechanics. Each implementation includes detailed exploratory data analysis (EDA), visualization, and evaluation metrics.

## Repository Structure

### Core Implementations

#### **AdaBoost Classification**

Implementation of the Adaptive Boosting ensemble method for binary and multi-class classification problems.

- `AdaBoost_Classification.ipynb` - Jupyter notebook with detailed analysis
- `adaboost_classification.py`
- `classwork dataset.csv` - Training dataset

#### **Decision Tree & Random Forest**

From-scratch implementations of decision tree algorithms and ensemble-based random forest classifiers.

- `DecisionTree_&_RandomForest.ipynb` - Comprehensive notebook
- `decisiontree_&_randomforest.py`
- `titanic.csv` - Titanic dataset for survival prediction

#### **K-Nearest Neighbors (KNN)**

Implementation of the KNN algorithm for classification and regression tasks.

- `KNN.ipynb`
- `KNN.py`

#### **Library Essentials**

Foundational data manipulation and visualization techniques using essential Python libraries.

- `LibraryEssentials.py`
- `LibraryEssentialsPy.ipynb` - Tutorial-style notebook
- `subject_scores.csv` - Sample dataset

#### **Logistic Regression**

Binary and multi-class logistic regression implementation with gradient descent optimization.

- `Logistic_Regression.ipynb` - Complete analysis workflow
- `logistic_regression.py`
- `cell_samples.csv` - Dataset

#### **Multilayer Perceptrons (MLP)**

Neural network implementation featuring backpropagation and configurable architectures.

- `MLP.ipynb` - Training and evaluation notebook
- `MLP.py` -

### Additional Materials

#### **Lab Exercises (MISC/LAB_01)**

Supplementary lab work and experimental implementations.

- `CSE427_Lab_1_Codes.ipynb` - Lab assignment solutions
- `cse427_lab_1_codes.py` - Supporting scripts
- `iris.csv` - Iris dataset for classification

## Technologies & Tools

- **Python 3.x**
- **NumPy** - Numerical computations
- **Pandas** - Data manipulation
- **Matplotlib/Seaborn** - Visualization
- **Scikit-learn** - Benchmarking and validation (where applicable)
- **Jupyter Notebook** - Interactive development

## Key Features

- **From-Scratch Implementations**: All algorithms coded without relying on high-level ML libraries
- **Comprehensive EDA**: Thorough exploratory data analysis for each dataset
- **Dual Format**: Both notebook (`.ipynb`) and script (`.py`) versions for flexibility
- **Clear Documentation**: Well-commented code with explanations of methodology

## Getting Started

### Prerequisites

```bash
pip install numpy pandas matplotlib seaborn jupyter scikit-learn
```

### Running the Notebooks

```bash
jupyter notebook
```

Navigate to the desired algorithm folder and open the `.ipynb` file.

### Running Python Scripts

```bash
python <algorithm_folder>/<script_name>.py
```

## Acknowledgments

Developed as part of the undergraduate Machine Learning curriculum at BRAC University. The implementations draw from classical ML literature and course materials, adapted and extended through hands-on experimentation.

## License

This repository is maintained for educational purposes. Feel free to explore and learn.

## Contact

For questions, discussions - please feel free to reach out or open an issue in this repository.
