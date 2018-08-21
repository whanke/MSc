"""
scikit-learn word2vec

kleines Beispiel mit einfachen Sätzen 

Quelle: Sebastian Raschka, Machine Learning mit Python, Frechen 2017, S. 240
"""

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

count = CountVectorizer()
docs = np.array([
		'der hase läuft auf dem feld',
		'der fuchs frisst die gans',
		'zuhause ist es ruhig'
		])

bag = count.fit_transform(docs)

print(count.vocabulary_)

print(bag.toarray())
