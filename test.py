import pickle

with open('stock_pred_model.pkl', 'rb') as pickle_file:
    stock_pred_model = pickle.load(pickle_file)

sample_data = [[12.0, 11.0, 1, 0.1, 0.1, 5.0]]
pred_1 = stock_pred_model.predict_proba(sample_data)[:, 1]
print(pred_1)