import numpy as np
import matplotlib.pyplot as plt  # Corrected import statement
from sklearn.datasets import fetch_openml
from sklearn
from sklearn.model_selection import train_test_split

# Fetch the Boston dataset
df_boston = fetch_openml(name="boston", as_frame=True)['frame']
print(df_boston.columns)

input_cols = ['CRIM', 'ZN', 'INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'TAX',
              'PTRATIO', 'B', 'LSTAT']

target = 'MEDV'

df_boston['constant'] = 1.0
x_train, x_test, y_train, y_test = train_test_split(df_boston[input_cols],  # Removed '*arrays:'
                                                    df_boston[target],
                                                    test_size=0.2,
                                                    shuffle=True,
                                                    random_state=10)

print(x_test.shape, x_train.shape)
print(y_test.shape, y_train.shape)

x_dot = np.dot(x_train.T, x_train)      ## transposed x bolon tuunii matrix-iig olon bolgoj huvirgav
x_inv = np.linalg.inv(x_dot)            ## X_dot-iig inverse hiih

y_dot = np.dot(x_train.T, y_train)
weight_parameters = np.dot(x_inv, y_dot) ## multipliction geneeeeee
print (weight_parameters)               ## reggression coefficients genee

### get fitted vallue

y_pred = np.dot(x_train, weight_parameters)

#plt.plot (y_train.values, label='actual value', color='black')
#plt.plot (y_pred, label='fitted value', color='red')
#plt.legend()
#plt.show()


### get reggression error###
print ('Train RMSE:', np.round(np.mean(np.sqrt((y_train.values-y_pred)**2)), 3))


### prediction on test set

y_pred_test = np.dot(x_test, weight_parameters)

print('Test RMSE', np.round(np.mean(np.sqrt((y_train.values-y_pred)**2)), 3))


plt.plot (y_test.values, label='actual value', color='black')
plt.plot (y_pred_test, label='fitted value', color='red')
plt.legend()
plt.show()