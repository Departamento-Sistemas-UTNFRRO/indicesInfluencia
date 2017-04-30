
import warnings
import os 
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA as sklearnPCA
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt; plt.rcdefaults()
import plotly.plotly as py

# Ask for name for the csv file to read
# Pide el nombre del archivo csv a leer
def fileNameInput():
	filename = input('Ingrese el nombre del archivo csv a leer: ')
	return (filename + '.csv')

# Ask for name for the csv file to save the results
# Pide el nombre del archivo csv para guardar los resultados
def fileNameOutput():
	filename = input('Elija un nombre para el archivo csv con los resultados: ')
	return (filename + '.csv')


# Save tweets from csv file in a dataset
# Almacena en un data set los tweets del archivo cv
def loadCsvIntoDataSet():
	data_path = ''
	tweets_csv = pd.read_csv(os.path.join(os.path.dirname(__file__), 'data', fileNameInput()), header=0, sep=';', quotechar='"', encoding = "ISO-8859-1")
	return tweets_csv.values

# Obtiene las variables númericas que servirán de entrada para el acp
# Get numeric variables that will be the input for the pca
def getNumericVariables(tweets):
	indexes = [0,2,3,4,5,6,7,8,9,10,
	11,12,13,14,15,16,17,18,
	22,23,24,25,26,27,29,
	30,31,32,33,34,35,36,37,38,39,
	40,41]
	numericVariables = np.delete(tweets,indexes,1)
	return numericVariables
	

# Standardize tweets (mean = 0, variance = 1)
# Estandariza tweets (media = 0, varianza = 1)
def standardizeTweetsData(numericVariables):
	return scale(numericVariables)

# Create and train pca model, calculate number of components that explain at least
# 75% of variance
# Crea y entrena el modelo acp, calculando el número de componentes que explican
# al menos el 75% de la varianza
def doPCA(standardized_tweets):
	number_of_components = 1
	total_explained_variance_ratio = 0
	
	while not total_explained_variance_ratio >= 0.75:
		pca = PCA(n_components=number_of_components)
		pca.fit(standardized_tweets)
		total_explained_variance_ratio = 0
		
		for i in range(0,number_of_components):
			total_explained_variance_ratio+= pca.explained_variance_ratio_[i]
		if total_explained_variance_ratio < 0.75:
			number_of_components+=1

	return pca

# Apply dimension reduction to tweets
# Aplicar la reducción dimensional a los tweets
def transformTweets(standardized_tweets, pca):
	return pca.transform(standardized_tweets)

# Calculate scores
# Calcula los índices de influencia
def calculateScores(transformed_tweets, pca):
	scores = []
	for i in range(0, len(transformed_tweets)):
		score = 0
		for j in range(0, len(pca.components_)):
			score+= pca.explained_variance_ratio_[j] * transformed_tweets[i][j]
		scores.append(float("{0:.2f}".format(score)))
	return scores 

# Add score to tweet data
# Agrega el índice de influencia a los datos del tweet
def addIdentifiers(scores, tweetsDataSet):
	tweetsWithScore = tweetsDataSet.tolist()

	for i in range(0, len(scores)):
		tweetsWithScore[i].insert(0,scores[i])

	return tweetsWithScore

# Sort by score in descending order
# Ordena por índice en orden descendente
def sortByScore(tweetsWithScore):
	return sorted(tweetsWithScore,key=lambda x: x[0], reverse=True)


# Returns the top 1% percentile
# Devuelve el 1% percentil superior
def percentile(tweetsSorted):
	values = []
	for i in range(0, len(tweetsSorted)):
		values.append(tweetsSorted[i][0])
	percentileValue = np.percentile(values,99)
	scoresRank = []
	for i in range(0, len(tweetsSorted)):
		if tweetsSorted[i][0] > percentileValue:
			scoresRank.append(tweetsSorted[i])

	return scoresRank


# Save results in csv
# Almacena los resultados en un csv
def saveInCsv(tweetsFinal):
	fileName = fileNameOutput()
	files_present = os.path.isfile(os.path.join(os.path.dirname(__file__), 'results', fileName))
	tweetsFinal = np.asarray(tweetsFinal)

	if (not files_present):

		columns = ['indice_influencia','text', 'retweet_count','created_at','location','statuses_count',
		'followers_count', 'favourites_count', 'name', 'friends_count', 'screen_name', 'expanded_url']

		df = pd.DataFrame(data=tweetsFinal[0:,[0,1,2,9,15,20,21,22,25,29,30,41]],
	                  columns=columns)
		
		df.to_csv(os.path.join(os.path.dirname(__file__), 'results', fileName), index=False, columns= columns, sep=';')
		print("El archivo csv fue almacenado en la carpeta results.")
	else:
		print("El archivo ya existe. Por favor, elija otro nombre.\n")
		saveInCsv(tweetsFinal)


# Main program
def main():
	warnings.filterwarnings("ignore")
	try:
		tweetsDataSet = loadCsvIntoDataSet()
	except FileNotFoundError:
		print("El archivo no existe.\n")
		main()
	else:
		numericVariables = getNumericVariables(tweetsDataSet)
		standardized_tweets = standardizeTweetsData(numericVariables)
		pca = doPCA(standardized_tweets)
		transformed_tweets = transformTweets(standardized_tweets, pca)
		scores = calculateScores(transformed_tweets, pca)
		tweetsWithScore = addIdentifiers(scores, tweetsDataSet)
		tweetsSorted = sortByScore(tweetsWithScore)
		tweetsRanked = percentile(tweetsSorted)
		saveInCsv(tweetsRanked)

main() 

