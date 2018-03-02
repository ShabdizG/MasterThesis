import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import *
from sklearn.metrics import classification as metrics
from pprint import pprint
from data.constants import *
from sklearn.model_selection import cross_val_score
from datetime import datetime as datetime
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

names = ["Nearest Neighbors",
         # "Linear SVM",
         # "RBF SVM",
         # "Gaussian Process",
         "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
         "Naive Bayes"
         #"QDA"
         ]

classifiers = [
    KNeighborsClassifier(3),
    # SVC(kernel="linear", C=0.025), takes too long
    # SVC(gamma=2, C=1), takes too long
    # GaussianProcessClassifier(1.0 * RBF(1.0), n_jobs=-1), # needs too much memory
    DecisionTreeClassifier(),   # max_depth=5
    # n_jobs = -1 : number of processor cores
    RandomForestClassifier(n_jobs=-1),  # max_depth=5, n_estimators=10, max_features=1,
    MLPClassifier(alpha=1),
    AdaBoostClassifier(),
    GaussianNB()
    # QuadraticDiscriminantAnalysis()
]

engine = create_engine('mysql+pymysql://root:Milch4321@localhost:3306/leaguestats', encoding='latin1',
                       echo=False)
item_names = {key: value for (key, value) in list(engine.execute('SELECT * FROM itemkeys'))}

collection = db.jhin_training_set
data = list(collection.find())
keys = data[1].keys()
frame = pd.DataFrame(data, columns=keys)

platform_fact, platform_keys = pd.factorize(frame.platformId)
frame['platform_fact'] = platform_fact

item_fact, item_keys = pd.factorize(frame.itemId)
frame['item_fact'] = item_fact

type_fact, type_key = pd.factorize(frame.type)
frame['type_fact'] = type_fact

frame['is_train'] = np.random.uniform(0, 1, len(frame)) <= .9
train, test = frame[frame['is_train']], frame[~frame['is_train']]

features = frame.columns.difference(['_id', 'gameId', 'itemId', 'is_train', 'platformId', 'type', 'item_fact'])
# pprint(train[[x for x in frame.columns if x in features]].head())

for name, clf in zip(names, classifiers):
    start = datetime.now()
    pprint("Start Processing: " + name)

    #clf: RandomForestClassifier = RandomForestClassifier(n_jobs=-1)
    clf.fit(train[[x for x in frame.columns if x in features]], train['item_fact'])

    preds = item_keys[clf.predict(test[[x for x in frame.columns if x in features]])]

    precision = metrics.accuracy_score(test['itemId'], preds)
    pprint("Accuracy: " + str(precision))

    actual = pd.Series([item_names[i] for i in test['itemId']])
    predicted = pd.Series([item_names[p] for p in preds])

    # crosstab = pd.crosstab(test['itemId'], preds, rownames=['actual'], colnames=['preds'])
    crosstab = pd.crosstab(actual, predicted, rownames=['actual'], colnames=['predicted'])
    crosstab.to_csv("output/" + name + "_crosstab.csv", sep=";")
    # cnf_matrix = metrics.confusion_matrix(test['itemId'], preds, labels=item_keys)
    cnf_matrix = metrics.confusion_matrix(actual, predicted, labels=[item_names[i] for i in item_keys])

    # Plot non-normalized confusion matrix
    df_cm = pd.DataFrame(cnf_matrix, index=[item_names[i] for i in item_keys],
                         columns=[item_names[i] for i in item_keys])
    df_cm.to_csv("output/" + name + "_confusion_matrix.csv", sep=";")
    plt.figure(figsize=(10, 7))
    sns.set(font_scale=0.25)
    sns_plot = sns.heatmap(df_cm).get_figure()
    sns_plot.savefig("output/confusion_matrix_" + name + ".pdf", format='pdf')
    # plt.savefig("output/confusion_matrix_" + name + ".pdf", format='pdf')

    time = (datetime.now() - start).seconds
    pprint("Finished " + name + " after " + str(time) + " seconds.")
