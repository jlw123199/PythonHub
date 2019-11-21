# Inputs: X – features, y - target
import numpy as np
from sklearn.metrics import roc_auc_score
from sklearn.svm import SVC
# grid of (gamma, C) values to try
from sklearn.tests.test_discriminant_analysis import y

gam_vec, cost_vec = np.meshgrid(np.linspace(0.01, 10., 11),
np.linspace(1., 10., 11))
AUC_all = []
# set up cross-validation folds
N = len(y)
K = 10
folds = np.random.randint(0, K, size=N)
# search over every value of the grid
for param_ind in np.arange(len(gam_vec.ravel())):
    # initialize cross-validation predictions
    y_cv_pred = np.empty(N)
    # loop through the cross-validation folds
    for ii in np.arange(K):
        # break your data into training and testing subsets
        X_train = X.ix[folds != ii,:]
        y_train = y.ix[folds != ii]
        X_test = X.ix[folds == ii,:]
        # build a model on the training set
        model = SVC(gamma=gam_vec.ravel()[param_ind], C=cost_vec.ravel()[param_ind])
    model.fit(X_train, y_train)
    # generate and store model predictions on the testing set
    y_cv_pred[folds == ii] = model.predict(X_test)
# evaluate the AUC of the predictions
AUC_all.append(roc_auc_score(y, y_cv_pred))

indmax = np.argmax(AUC_all)
print ("Maximum = %.3f" % (np.max(AUC_all)))
print ("Tuning Parameters: (gamma = %f, C = %f)" % (gam_vec.ravel()[indmax],cost_vec.ravel()[indmax]))