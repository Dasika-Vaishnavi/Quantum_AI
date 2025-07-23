# Quantum_AI Repository 
Welcome to the **Quantum_AI** repository—a comprehensive, hands-on exploration of **Quantum Computing** and **Quantum Artificial Intelligence**. This documentation is designed to guide advanced learners and professionals through the codebase, providing technical clarity and actionable context at each step.
From Vaishnavi Dasika <3

## 📦 Repository Structure

```
Quantum_AI/
│
├── Installing_Qiskit_and_Dependancies.ipynb
├── Complex_Arithmetic.ipynb
├── QML_Exploring_quantum_states.ipynb
├── QuantumKeyDistribution.ipynb
├── Deutsch_Jozsa_Algorithm.ipynb
├── Simons_Algorithm.ipynb
├── Quantum_error_correction.ipynb
├── Quantum_data.ipynb
├── Titanic_data_QML.ipynb
├── gradients.ipynb
├── hello_many_worlds.ipynb
├── QCNN.ipynb
├── q_KNN.ipynb
├── vqe_advanced_options.ipynb
├── VQE_Qiskit_introduction.ipynb
├── QSVM-Classification-Model-master/
│   ├── Classical SVM.ipynb
│   ├── Dataset Generator.py
│   ├── LumAB_with_QSVM - Ameya.ipynb
│   ├── QSVM_LumA_v_LumB.ipynb
│   ├── README.md
├── Data/
│   └── (project datasets)
└── README.md
```

## 📚 Lesson-by-Lesson Documentation

### 1. Installing_Qiskit_and_Dependancies.ipynb

**Purpose:** Establishes the quantum computing environment.  
**Content:** Comprehensive instructions for installing Qiskit using pip/conda, verifying successful setup, and troubleshooting import/test errors.  
**Technical Focus:** Ensures your Python ecosystem is configured for quantum code execution.  
**Reference:** [Qiskit Getting Started](https://qiskit.org/documentation/getting_started.html)

```
[Anaconda/Miniconda or Python] --pip/conda--> [Qiskit Packages] --> [Quantum Development Environment]
```

### 2. Complex_Arithmetic.ipynb

**Purpose:** Acts as a mathematical bridge between classical and quantum computation using Python (NumPy).

- Covers:  
  - Complex number manipulation (addition, multiplication)
  - Matrix operations  
  - Essentials for quantum state descriptions

**Sample Table: Quantum Arithmetic**

| Operation   | Symbol | Python Example                   | Output   |
|-------------|--------|----------------------------------|----------|
| Addition    | +      | 4 + 3j + 2                       | (6+3j)   |
| Multiplic.  | *      | (1+2j) * 3                       | (3+6j)   |
| Dot Prod.   | @      | np.array() @ np.array()| 2        |

### 3. QML_Exploring_quantum_states.ipynb

**Purpose:** Construction, manipulation, and visualization of quantum states using Qiskit.  
**Core Ideas:**
- Dirac (bra-ket) notation
- Superposition principles
- Multi-qubit entanglement

**Visual:**

![Bloch Sphere](https://upload.wikimedia.org/wikipedia/commons/6/6b/Bloch_Spherech sphere is essential for visualizing single-qubit quantum states.*

**Reference:** [Qiskit Bloch Sphere](https://qiskit.org/textbook/ch-states/representing-qubit-states.html)

### 4. QuantumKeyDistribution.ipynb

**Purpose:** Implements quantum key distribution protocols (e.g., BB84).

- Explains:  
  - Qubit preparation and measurement  
  - Classical channel basis comparison  
  - Secure key postprocessing

**Protocol Flow:**
```
Alice (bits/bases)
      |
[Qubits sent (BB84 protocol)]
      v
Bob (random basis, measure)
      |
[Classical basis comparison]
      v
Key agreement, error analysis
```

**Reference:** [BB84 (Wikipedia)](https://en.wikipedia.org/wiki/BB84)

### 5. Deutsch_Jozsa_Algorithm.ipynb

**Purpose:** Demonstrates the Deutsch-Jozsa algorithm, showcasing quantum advantage for function types (constant/balanced).

**Circuit:**

![Deutsch-Jozsa Circuit](https://qiskit.org/textbook/_images/deutsch:** [Qiskit Deutsch-Jozsa](https://qiskit.org/textbook/ch-algorithms/deutsch-jozsa.html)

### 6. Simons_Algorithm.ipynb

**Purpose:** Introduction to Simon’s algorithm—a precursor to Shor’s algorithm for quantum period-finding.  
Covers use of oracles, entanglement, and measurement.

### 7. Quantum_error_correction.ipynb

**Purpose:** Teaches error correction concepts essential for scalable quantum computation.

- Bit-flip & phase-flip codes
- Logical vs. physical qubits
- Encoding/decoding circuits

**Reference:** [Qiskit Textbook: Error Correction](https://qiskit.org/textbook/ch-quantum-hardware/error-correction-repetition-code.html)

### 8. Quantum_data.ipynb

**Purpose:** Prepares classical datasets (e.g., MNIST) for quantum ingestion.

**Techniques:**  
- Normalization  
- Feature mapping (angle-based)  
- Conversion to circuit parameters

### 9. Titanic_data_QML.ipynb

**Purpose:** Blend of classical and quantum ML pipelines on the Titanic dataset.

**Processing Table:**

| Step        | Classical    | Quantum                 |
|-------------|--------------|------------------------|
| Normalize   | Yes          | Yes (for encoding)     |
| Format      | 1D vector    | Circuit params         |
| Input       | float        | gate/rotation          |

### 10. gradients.ipynb

**Purpose:** Details hybrid gradient calculation essential for optimization in quantum-classical algorithms.

- **Focus:**  
  - Parameter-shift rule  
  - Qiskit & PyTorch bridges for autodiff

### 11. hello_many_worlds.ipynb

**Purpose:** Explores quantum calibration under the many-worlds interpretation, linking theory to practice.

**Reference:** [Many-Worlds Interpretation](https://en.wikipedia.org/wiki/Many-worlds_interpretation)

### 12. QCNN.ipynb

**Purpose:** End-to-end implementation of a **Quantum Convolutional Neural Network**.

- Quantum circuit convolution
- Pooling operations
- Pipeline for quantum deep learning

### 13. q_KNN.ipynb

**Purpose:** Implements quantum-enhanced k-nearest neighbors leveraging quantum feature space search.

- Parallel distance computations
- Quantum speedup in classification

### 14. vqe_advanced_options.ipynb & VQE_Qiskit_introduction.ipynb

**Purpose:** Advanced coverage of the **Variational Quantum Eigensolver (VQE)** for quantum chemistry and optimization.

**Workflow Diagram:**
```
[Params θ] → [Quantum Circuit] → [Measurement/Cost]
      ↑                             |
      +-----------------------------+
          Classical Optimization Loop
```

**Reference:** [Qiskit VQE](https://qiskit.org/textbook/ch-applications/vqe-molecules.html)

### 15. QSVM-Classification-Model-master/

A dedicated folder for breast cancer subtype classification (LumA vs. LumB) using both classical and quantum SVM approaches.

**Contents:**  
- `Dataset Generator.py` – Data preparation, transformation  
- `Classical SVM.ipynb` – Baseline comparison  
- `QSVM_LumA_v_LumB.ipynb` – Quantum SVM training and evaluation  
- `README.md`  
- `LumAB_with_QSVM - Ameya.ipynb` – Annotated workflow and results

**Pipeline Table:**

| Phase     | Script                 | Quantum?      |
|-----------|------------------------|---------------|
| Data prep | Dataset Generator.py   | No            |
| SVM       | Classical SVM.ipynb    | No            |
| QSVM      | QSVM_LumA_v_LumB.ipynb | Yes           |
| Compare   | README, Notebooks      | Yes/No        |

**Flow Schematic:**
```
Raw Data → Preprocessing → PCA → [SVM] & [QSVM] → Accuracy Analysis
```

**Reference:** [Quantum SVM Paper](https://arxiv.org/pdf/1909.06206.pdf)

### 16. Data/

**Purpose:** Contains all datasets (CSV, NPY, etc.) for experimentation and practice.

## 📊 Summary Table

| Notebook/Project                  | Main Topic                | Core Algorithm/Concept      |
|-----------------------------------|---------------------------|-----------------------------|
| Installing_Qiskit...              | Setup                     | Qiskit, Environment         |
| Complex_Arithmetic                | Python, Math              | Complex, Linear Algebra     |
| QML_Exploring_quantum_states      | Quantum State, Circuit    | Bloch Sphere, Gates         |
| QuantumKeyDistribution            | Quantum Crypto            | BB84, Secure Channel        |
| Deutsch_Jozsa_Algorithm           | Quantum Alg.              | Deutsch-Jozsa               |
| Simons_Algorithm                  | Quantum Period Finding    | Simon's Algorithm           |
| Quantum_error_correction          | Error Correction          | Bit/phase-flip Codes        |
| Quantum_data                      | Data for Quantum ML       | Scaling, Encoding           |
| Titanic_data_QML                  | Applied ML/QML            | SVM, Quantum Classification |
| gradients                         | Quantum Gradients         | Parameter-shift, Hybrid     |
| hello_many_worlds                 | Theory + ML               | Calibration, Simulation     |
| QCNN                              | Quantum Deep Learning     | Quantum CNN                 |
| q_KNN                             | Quantum kNN               | Quantum Distance            |
| vqe_advanced_options, VQE_intro   | Hybrid VQE                | Quantum Ground State        |
| QSVM-Classification-Model-master  | End-to-End QML            | SVM, Quantum SVM            |
| Data/                             | Dataset Storage           | CSV, NPY, feather           |

## 📈 Visual Roadmap

![Learning Path Timeline](https://cdn.qiskit.org/textbook/ch-appendix/images/learning learning path illustrates a structured progression from quantum foundations to advanced quantum machine learning projects, adapted from the [Qiskit Textbook](https://qiskit.org/textbook/).*

## 📚 Further Resources

- [Qiskit Textbook](https://qiskit.org/textbook/)
- [Qiskit Tutorials](https://qiskit.org/documentation/tutorials/)
- [ArXiv: Quantum SVM](https://arxiv.org/pdf/1909.06206.pdf)
