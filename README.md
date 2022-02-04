# Relational-NER
A Python code for enhancing the output of multilingual named entity recognition based on Wikidata relations

**To Cite the Work:** Turki, H., Priskorn, D., Hadj Taieb, M. A., Ben Aouicha, M., & Piad-Morffis, A. (2022). Enhancing Multilingual Named Entity Recognition using Wikidata Semantic Relations. In *[Wiki Workshop 2022](https://wikiworkshop.org/2022/)* (Forthcoming).
## Description
This project proposes a novel approach that enriches the named entity recognition (NER) of a given class of entities through the use of semantic relations in open knowledge graphs, particularly Wikidata. For the sake of our research work, we have chosen drugs as the considered class for the original NER to be enriched using our approach.
## Files
The repository provides four source codes implemented in Python 3.9 and four datasets for the assessment of our proposed approach.
* **Source:**
 * *Drug-NER.py*: Algorithm for the named entity recognition of drug items in the titles of scholarly publications
 * *RelationBasedNER.py*: Algorithm for the enrichment of the output of drug NER with the annotation of drug-related Wikidata items as revealed by the Wikidata Knowledge Graph.
* **Output:**
 * *dataset.csv*: Dataset of the titles of biomedical scholarly publications about drugs as extracted using the ItemSubjector tool.
 * *drugNER.txt*: Output of the named entity recognition of drugs.
 * *drugs.tsv*: List of drug names used for drug NER and extracted using SPARQL from the Wikidata Knowledge Graph.
 * *relatedNER.txt*: 
## Dependencies
* Langdetect 1.0.9
* Wikibaseintegrator 0.12.0
## Team
* Houcemeddine Turki, Data Engineering and Semantics Research Unit, University of Sfax, Tunisia
* Dennis Priskorn, Mid Sweden University, Sweden
* Mohamed Ali Hadj Taieb, Data Engineering and Semantics Research Unit, University of Sfax, Tunisia
* Mohamed Ben Aouicha, Data Engineering and Semantics Research Unit, University of Sfax, Tunisia
* Alejandro Piad-Morffis, School of Math and Computer Science, University of Havana, Cuba
