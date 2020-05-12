# Information Theory for Biological Sequences Classification: A Novel Feature Descriptor based on Tsallis Entropy

Over the years, with the accelerated technological advance came the exponential growth of sequencing projects, generating a significant increase in the amount of data. Consequently, resulting in new challenges for biological sequence analysis. Moreover, with this large amount of sequences, new methods are needed. In this way, machine learning approaches are being used for the analysis and classification of biological sequences. The development of effective methods for data analysis, through machine learning, benefits the mathematical understanding of the structure of sequences. However, analyzing sequences with machine learning presents a central problem, Feature Extraction, where is challenging generating representative and informative numeric features. Considering this, the need to extract numerical features to represent sequences makes it statistically feasible to apply universal concepts from Information Theory. Therefore, we present a Tsallis entropy-based feature extraction approach, to classify biological sequences. We investigate five classification algorithms like Naive Bayes, Random Forest, Bagging, Multi-layer Perceptron, and CatBoost. Moreover, the proposed approach was compared with Shannon entropy. As a result, our proposal proved to be effective, being superior to Shannon entropy and robust in terms of generalization.

## Authors

* Robson Parmezan Bonidia and Anderson Paulo Ávila Santos.

* **Correspondence:** robservidor@gmail.com or bonidia@usp.br


## Publication

If you use this code in a scientific publication, we would appreciate citations to the following paper:

Submitted


## List of files

 - **Examples:** Datasets of Example

 - **README:** Documentation;

 - **Requirements:** List of items to be installed using pip install;

 - **TsallisEntropy** Main File - Python;

 - **machineLearningEntropy** Main File - Python.


## Dependencies

- Python (>=3.7)
- NumPy 
- Pandas
- Biopython
- Scikit-learn
- Catboost


## Installing our tool

```sh
$ pip3 install -r requirements.txt

$ git clone https://github.com/Bonidia/TsallisEntropy.git TsallisEntropy
```

## Usange and Examples


```sh
Access folder: $ cd TsallisEntropy
 
To run the feature extraction tool (Example): $ python3.7 TsallisEntropy.py -i examples/1rna.fasta -o example_dataset.csv -l RNA -k 24 -q 2.3

Where:

-h = help

-i = Input - Fasta format file, e.g., sequences.fasta

-o = output - CSV format file, e.g., dataset.csv

-l = Label - Dataset Label, e.g., lncRNA, mRNA, sncRNA

-k = kmer - Range of k-mer, E.g., 1-mer (1) or 2-mer (1, 2) ...

-q = Tsallis - q parameter

This example will generate a csv file with the extracted features.
```

```sh
Access folder: $ cd TsallisEntropy
 
To analyze the data set with machine learning algorithms (example): $ python3.7 machineLearningEntropy.py -i dataset.csv -o results.csv

Where:

-i = Input - CSV format file, e.g., dataset.csv

-o = output - CSV format file, e.g., results.csv

This example will generate a csv file with the performance of the classifiers.
```

**Note** Input sequences for feature extraction must be in fasta format.

## About

If you use this code in a scientific publication, we would appreciate citations to the following paper:

Submitted