# QSVM-Classification-Model Documentation

## Overview

This repository implements a **Quantum Support Vector Machine (QSVM)** and a classical SVM model for the classification of breast cancer subtypes *LumA* vs. *LumB*. The main workflow consists of **data preprocessing**, **dimensionality reduction using PCA**, **training/testing classical and quantum models**, and **evaluation**. The code relies on both **Scikit-learn** for classical machine learning and the **Qiskit** framework for quantum machine learning.

---

## Directory Contents

- **Dataset Generator.py**: Generates and shuffles the dataset from feather format files for use by both classical and quantum models.
- **Classical SVM.ipynb**: Jupyter notebook for running a traditional SVM using dimensionality-reduced data, benchmarking via accuracy metrics.
- **LumAB_with_QSVM - Ameya.ipynb** and **QSVM_LumA_v_LumB.ipynb**: Notebooks implementing and testing a Quantum SVM using Qiskit and reduced features.
- **test.csv, train.csv, test.npy, train.npy**: Preprocessed data files.
- **README.md**: Brief description and literature reference.

---

## Workflow Summary

1. **Data Preparation**
    - Merges training and test feather files into one DataFrame.
    - Shuffles and saves combined dataset for downstream usage.

2. **Preprocessing and Dimensionality Reduction**
    - Reads in the merged dataset.
    - Binarizes labels for binary classification.
    - Reduces feature space to the top 10 principal components via PCA (Principal Component Analysis).

3. **Classical SVM**
    - Trains an SVM classifier on reduced training data.
    - Performs repeated splits for cross-validation.
    - Reports accuracy statistics.

4. **Quantum SVM (QSVM)**
    - Utilizes Qiskit's deprecated `aqua` module to construct a QSVM using a ZZFeatureMap.
    - Trains and tests on PCA-reduced data.
    - Evaluates quantum classification accuracy.

---

## Assumptions & Disclaimer

> **Code Assumptions:**
> - The feather-format dataset files are present and correctly named in the expected locations.
> - The code is run in an environment with the correct versions of all required packages (notably, Qiskit Aqua—which is now deprecated).
> - The code structure and scripts assume usage in Jupyter/Google Colab, and file paths may require adjustment for different environments.
> - PCA component count does not exceed the minimum dimension among features/samples.

> **Important Disclaimer:**
> - **Deprecation:** The quantum code depends on Qiskit’s `aqua` module, which is no longer supported or installed in recent Qiskit versions; you may encounter import or API errors if using a modern setup.
> - **Hardcoded Filenames/Paths:** The code expects very specific file names and directory structures. You must ensure your data and directories match or modify the code accordingly.
> - **Minimal Error Handling:** The scripts lack detailed exception handling. Non-existent files, wrong data shapes, or package incompatibilities will produce runtime errors.
> - **Outdated Methods:** Certain pandas and DataFrame methods (`append`, some feather usage) are deprecated and should be replaced in production.
> - **Environment Dependency:** Some code chunks (notably, those depending on `/content/drive/...`) assume an interactive Google Colab environment with Google Drive mounted.
> - **Not Plug-and-Play:** You may need to update, refactor, or fix the code for it to work with your environment and latest package versions.
> 
> **Please review and adapt the code for your own environment and software stack.**

---

## References

- Quantum Support Vector Machine (QSVM) based classifier for LumA vs. LumB breast cancer  
  [arXiv:1909.06206 [pdf]](https://arxiv.org/pdf/1909.06206.pdf)


https://arxiv.org/pdf/1909.06206.pdf
