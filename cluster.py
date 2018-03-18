#testing file onyl not for production


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score

documents = ["VIT", "Vellore", "VIT", "Vellore", "VIT", "Vellore",]

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

true_k = 2
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1)
model.fit(X)

print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(true_k):
    print ("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print (' %s' % terms[ind]),
    print

print('\n')
print("Prediction")

Y = vectorizer.transform["VIT"]
prediction = model.predict(Y)
print (prediction)