# Information Theory for Biological Sequence Classification: A Novel Feature Extraction Technique based on Tsallis Entropy

In recent years, there has been an exponential growth of sequencing projects due to accelerated technological advances, leading to a significant increase in the amount of data, and resulting in new challenges for biological sequence analysis. Consequently, the use of techniques capable of analyzing large amounts of data has been explored, such as Machine Learning (ML) algorithms. ML algorithms are being used to analyze and classify biological sequences, despite the intrinsic difficulty in extracting and finding representative biological sequence methods suitable for them. Moreover, extracting numerical features to represent sequences makes it statistically feasible to use universal concepts from Information Theory, such as Tsallis and Shannon entropy.
Thereby, in this study, we propose a novel Tsallis entropy-based feature extractor to provide useful information to classify biological sequences. To assess its relevance, we prepared four cases studies: (1) An analysis of the effect of the entropic index q; (2) Performance testing of the best entropic
indices on new datasets; (3) A comparison made with Shannon Entropy; (4) An investigation of the Tsallis entropy in the context of dimensionality reduction. As a result, our proposal proved to be effective, being superior to Shannon entropy and robust in terms of generalization, and also
potentially representative for collecting information in fewer dimensions compared to methods such as Singular Value Decomposition and Uniform Manifold Approximation and Projection.

## Authors

* Robson Parmezan Bonidia, Anderson P. Avila Santos, Breno L. S. de Almeida, Peter F. Stadler, Ulisses N. da Rocha, Danilo S. Sanches and André C.P.L.F. de Carvalho.

* **Correspondence:** rpbonidia@gmail.com or bonidia@usp.br


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
$ git clone https://github.com/Bonidia/TsallisEntropy.git TsallisEntropy

$ cd TsallisEntropy

$ pip3 install -r requirements.txt
```

## Usage and Examples


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
