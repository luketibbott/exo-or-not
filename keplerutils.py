# This is a utility file for modeling on Exoplanet classification data
# Project 3, October 2018


def encode_response(x):
    if x == 'CONFIRMED':
        return 1
    else:
        return 0

def split_and_upsample(df):
    '''
        Does a train test split on response and features, uses SMOTE to upsample imputed values
        from minority class to achieve 1:1 ratio of classes, returns the upsampled training response
        and features.
        ----Parameters----
        df: Pandas dataframe with response in 0th column, features in rest of columns
        ----Returns----
        X_train_res: upsampled imputed features
        y_train_res: upsampled imputed response
        X_test: unchanged test features
        y_test: unchanged test response
    '''
    
    y = df.iloc[:, 0]
    X = df.iloc[:, 1:]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
    
    sm = SMOTE()
    
    X_train_res, y_train_res = sm.fit_sample(X_train, y_train.ravel())
    
    return X_train_res, X_test, y_train_res, y_test