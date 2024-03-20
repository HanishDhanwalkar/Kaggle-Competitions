import pandas as pd


def gender_filter(string):
    if string == 'male':
        return 0
    else:
        return 1

def em2idx(string):
    # One hot encoding for Embarked col
    # arr_Embarked = df['Embarked'].unique()
    dic_Embarked = {'S': 0, 'C': 1, 'Q': 2, 'nan': 4}
    return dic_Embarked[f'{string}']

def pre_process(df):
    df = df.set_index('PassengerId')
    df = df.drop(columns = ['Name', 'Ticket', 'Fare', 'Cabin'])

    # gender one hot encoding
    df['Sex'] = df['Sex'].apply(gender_filter)



    # one hot encoding for Embarked
    df['Embarked'] = df['Embarked'].apply(em2idx)

        # Fill Nan
    for col in df.columns:
        mean_value = df[f'{col}'].mean()
        # print(mean_value)
        df[f'{col}'].fillna(value=mean_value, inplace=True)
        # print(df.head())

    return df

# # USAGE:
# train_file = "../data/" + "train.csv"
# train_df = pd.read_csv(train_file)

# print(pre_process(train_df).head())