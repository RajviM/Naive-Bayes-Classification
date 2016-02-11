# Naive-Bayes-Classification
A Naive Bayes Classifier to detect positive and negative , truthful and deceptive hotel reviews

Word Tokens are used as features
#Programs

Two programs are written. nblearn.py will learn a naive Bayes model from the training data and nbclassify.py will use the model to classify new data. The program will learn a naive Bayes model, and write the model parameters to a file called nbmodel.txt. 
The results to a text file called nboutput.txt in the following format:

label_a label_b path1
label_a label_b path2 
⋮

In the above format, label_a is either “truthful” or “deceptive”, label_b is either “positive” or “negative”, and pathn is the path of the text file being classified.

#Data

op_spam_train was used as training data.

A top-level directory with two sub-directories, one for positive reviews and another for negative reviews  
Each of the subdirectories contains two sub-directories, one with truthful reviews and one with deceptive reviews. 
Each of these subdirectories contains four subdirectories, called “folds”.  
Each of the folds contains 80 text files with English text (one review per file).  

