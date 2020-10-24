import pandas as pd
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
import pprint
import urllib.request
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing import sequence
from tqdm import tqdm
from prettytable import PrettyTable
import tensorflow as tf

random_seed = 18

np.random.seed(random_seed)

print("Phishtank Online Valid Dataset")

#Combining multiple online-valid datasets from different days to get more unique samples.
online_valid_df_1 = pd.read_csv("online-valid_2020-10-08.csv")
online_valid_df_1.set_index("phish_id", inplace=True)
online_valid_df_2 = pd.read_csv("online-valid_2020-10-19.csv")
online_valid_df_2.set_index("phish_id", inplace=True)
online_valid_df_3 = pd.read_csv("online-valid_2020-10-20.csv")
online_valid_df_3.set_index("phish_id", inplace=True)
online_valid_df_4 = pd.read_csv("online-valid_2020-10-21.csv")
online_valid_df_4.set_index("phish_id", inplace=True)
online_valid_df_5 = pd.read_csv("online-valid_2020-10-21_2.csv")
online_valid_df_5.set_index("phish_id", inplace=True)
online_valid_df_6 = pd.read_csv("online-valid_2020-10-22_1.csv")
online_valid_df_6.set_index("phish_id", inplace=True)
online_valid_df_7 = pd.read_csv("online-valid_2020-10-22_2.csv")
online_valid_df_7.set_index("phish_id", inplace=True)
online_valid_df_8 = pd.read_csv("online-valid_2020-10-23_1.csv")
online_valid_df_8.set_index("phish_id", inplace=True)
online_valid_df_9 = pd.read_csv("online-valid_2020-10-24.csv")
online_valid_df_9.set_index("phish_id", inplace=True)

online_valid_df = online_valid_df_1.merge(online_valid_df_2, how="outer")
online_valid_df = online_valid_df.merge(online_valid_df_3, how="outer")
online_valid_df = online_valid_df.merge(online_valid_df_4, how="outer")
online_valid_df = online_valid_df.merge(online_valid_df_5, how="outer")
online_valid_df = online_valid_df.merge(online_valid_df_6, how="outer")
online_valid_df = online_valid_df.merge(online_valid_df_7, how="outer")
online_valid_df = online_valid_df.merge(online_valid_df_8, how="outer")
online_valid_df = online_valid_df.merge(online_valid_df_9, how="outer")

online_valid_df.to_csv("combined_online_valid.csv")

# Extracting tld and domain name.
tld_count = defaultdict(lambda: 0)
domain_names = []
for index, row in online_valid_df.iterrows():
    # Extracting the tld from the url
    domain_name = row["url"].replace("https://","").replace("http://","").split("/")[0]
    domain_names.append(domain_name)
    tld = domain_name.split(".")[-1]
    tld_count[tld] += 1

tld_df = pd.Series(dict(tld_count))
tld_df.sort_values(ascending=False, inplace=True)

show_top_n = 20

tld_print = tld_df.iloc[:show_top_n]
tld_print["OTHERS"] = tld_df.iloc[show_top_n:].sum()

online_valid_df["domain_names"] = domain_names


whitelist_file_alexa = "top-1m_alexa.csv"
whitelist_file_umbrella = "top-1m_umbrella.csv"
alexa_whitelist_df = pd.read_csv(whitelist_file_umbrella, header=None, names=["rank", "domain_names"])

# Finding if there are any domains that are also in the whitelist.
domains_in_whitelist = np.intersect1d(online_valid_df["domain_names"], alexa_whitelist_df["domain_names"])
# Tagging the whitelisted domains as such.
online_valid_df["in_whitelist"] = np.in1d(online_valid_df["domain_names"], domains_in_whitelist)

print(online_valid_df.shape[0], "rows")
print(online_valid_df.head(20))
print(tld_print.to_frame(name="TLD Count").transpose().to_string())
print(f"Percentage of top {show_top_n} tlds: {np.round(100*tld_df.iloc[:show_top_n].sum()/tld_df.sum(), decimals=2)} %")


print()
print(whitelist_file_umbrella)

print(alexa_whitelist_df.shape[0], "rows")
print(alexa_whitelist_df.head(20))

print()
print("Number of urls that have domains which are in the whilelist:", online_valid_df["in_whitelist"].sum())


# For the dataset, excluding all where the domain name is in the whitelist.

online_valid_df_without_intersection = online_valid_df.loc[online_valid_df['in_whitelist'] == False]
alexa_whitelist_df_without_intersection = alexa_whitelist_df.loc[np.invert(alexa_whitelist_df['domain_names'].isin(domains_in_whitelist))]

oversampling_rate = 1 # Set this to 1 to have the positive samples match the phishing samples. Set to greater than 1 to use more negative samples.

phishing_domains = online_valid_df_without_intersection["domain_names"].values
whitelist_domains = np.random.choice(alexa_whitelist_df_without_intersection["domain_names"].values, size=int(oversampling_rate*len(phishing_domains)), replace=False)

# Calling a phishing url 1 and a benign url 0.
# Using character encoding as the vocabulary.
# Feeding the url as the sequence.

print()
print("Selected Data Examples:")
print("Phishing domains:", phishing_domains, len(phishing_domains))
print("Benign domains:", whitelist_domains, len(whitelist_domains))

# Creating the samples array and the label array
print()
X = list(phishing_domains) + list(whitelist_domains)
y = [1]*len(phishing_domains) + [0]*len(whitelist_domains)
sample_weights = [1]*len(phishing_domains) + [1/oversampling_rate]*len(whitelist_domains)


vocab = sorted(set("".join(X)), reverse=True)
# Inserting a space at index 0, since it is not used in url and will be used for padding the examples.
vocab.insert(0, " ")
vocab_size = len(vocab)

print()
print(f"Encoding Vocabulary ({vocab_size}) used:")
print(vocab)
# Creating a mapping from unique characters to indices
char2idx = {u:i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)

def text_to_int(text):
  return np.array([char2idx[c] for c in text])

print("Encoding example:")
print(text_to_int(phishing_domains[0]))

def int_to_text(ints):
  try:
    ints = ints.numpy()
  except:
    pass
  return ''.join(idx2char[ints])

print(int_to_text(text_to_int(phishing_domains[0])))


# Investigating the domain name length for the combined domain names:
X_elem_len = [len(domain_name) for domain_name in X]
print("Longest domain name:", np.max(X_elem_len))

plt.hist(X_elem_len, bins = 100)
plt.savefig("domain_name_length_histogram.png")

print(sorted(X_elem_len, reverse=True)[:show_top_n])
# Only 10 urls are longer than 100 characters. So going with that for sequence length.
max_seq_len = 50
print((np.array(X_elem_len) > max_seq_len).sum(), "URLs longer than the cutoff length", max_seq_len)

# Creating test and training datasets
print()

X_train, X_test, y_train, y_test, sample_weights_train, sample_weights_test = train_test_split(np.array(X), np.array(y), np.array(sample_weights), test_size=0.15, random_state=random_seed)

show_top_n = 5
print(f"Training and testing data: (showing first {show_top_n})")
print(f"Train data {len(X_train)} samples")
print(list(zip(X_train[:show_top_n], y_train[:show_top_n], sample_weights_train[:show_top_n])))
print(f"Test data {len(X_test)} samples")
print(list(zip(X_test[:show_top_n], y_test[:show_top_n], sample_weights_test[:show_top_n])))

# Encoding the domain names using the vocabulary

X_train_encoded = [text_to_int(domain_name) for domain_name in X_train]
X_test_encoded = [text_to_int(domain_name) for domain_name in X_test]
print()
print(f"Encoded data: (showing first {show_top_n})")
print(f"Train data {len(X_train_encoded)} samples, encoded")
print(list(zip(X_train_encoded[:show_top_n], y_train[:show_top_n])))
print(f"Test data {len(X_test_encoded)} samples, encoded")
print(list(zip(X_test_encoded[:show_top_n], y_test[:show_top_n])))

# Padding to the right sequence length.
X_train_encoded_padded = sequence.pad_sequences(X_train_encoded, max_seq_len)
X_test_encoded_padded = sequence.pad_sequences(X_test_encoded, max_seq_len)
print()
print(f"Encoded and padded data: (showing first {show_top_n})")
print(f"Train data {len(X_train_encoded_padded)} samples, encoded")
print(list(zip(X_train_encoded_padded[:show_top_n], y_train[:show_top_n])))
print(f"Test data {len(X_test_encoded_padded)} samples, encoded")
print(list(zip(X_test_encoded_padded[:show_top_n], y_test[:show_top_n])))



# Creating the recurrent model for the predictions:
print("\n---------------Tensorflow magic------------------\n")
# print(tf.config.list_physical_devices('GPU'))
# For some reason needed so the code runs properly on the gpu.
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    print('gpu', gpu)
    tf.config.experimental.set_memory_growth(gpu, True)
    print('memory growth:' , tf.config.experimental.get_memory_growth(gpu))

# https://www.tensorflow.org/api_docs/python/tf/keras/layers/LSTM
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, 64),
    # tf.keras.layers.LSTM(512, return_sequences=True),
    tf.keras.layers.LSTM(512),
    # tf.keras.layers.LSTM(128, go_backwards=True),
    # tf.keras.layers.Dense(512),
    # tf.keras.layers.Dense(128,activation="tanh"),
    # tf.keras.layers.Dense(128),
    tf.keras.layers.Dense(512,activation="tanh"),
    # tf.keras.layers.Dense(512,activation="tanh"),
    # tf.keras.layers.Dense(512,activation="tanh"),
    # tf.keras.layers.Dense(512,activation="tanh"),
    # tf.keras.layers.Dense(32,activation="sigmoid"),
    # tf.keras.layers.Dense(32),
    # tf.keras.layers.Dense(16),
    tf.keras.layers.Dense(1, activation="sigmoid")
])


# Compiling the model
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=['acc'])
print(model.summary())

# Training the model
history = model.fit(X_train_encoded_padded, y_train, epochs=10, validation_data=(X_test_encoded_padded, y_test), sample_weight=sample_weights_train)

#Evaluating the model


def evaluate_nn_model(X, y, threshold=0.5):
    """
    Custom nn evaluation to get the TP, TN, FP, FN rates.
    Anything below threshold is considered not phishing.
    Anything above threshold is considered phishing.

    """
    print()
    predictions = model.predict(X_test_encoded_padded).flatten()
    mean_prediction = np.mean(predictions)
    print(f"Calculated {len(predictions)} predictions with a mean value of {mean_prediction}")
    print(f"Evaluating using threshold {threshold}")
    # Turning the predictions into 0 and 1 by checking the threshold. (0 safe, 1 phishing)
    predictions_boolean = predictions > threshold
    predictions_binary = predictions_boolean.astype(np.int)
    print(f"Cut-off threshold: {np.round(threshold, decimals=4)}")
    statistics_table_printer(predictions_binary, y)
    return mean_prediction

def statistics_table_printer(predictions_binary, y_binary, decimals=3):
    # Concattenating the strings of the binary value of the prediction and the truth.
    # First value is the prediction, second the actual label
    # Hypothesis is: is phishing -> positive: yes phishing, negative: no phishing
    # Then 00 would be a TN, 01 is a FP, 10 is a FN, 11 is a TP. 
    # Converting the binary outcomes to integer: 0 TN, 1 FP, 2 FN, 3 TP
    hypothesis_tests = [int(str(label)+str(prediction), 2) for prediction, label in zip(predictions_binary, y_binary)]
    # Counting the number of times each unique value in the tests is returned.
    unique_elements, counts_elements = np.unique(hypothesis_tests, return_counts=True)
    counts_elements = dict(zip(unique_elements, counts_elements))
    outcome_labels = ["TN", "FP", "FN", "TP"]
    evaluation_ratios_counts = dict(zip(outcome_labels, [counts_elements.get(0, 0), counts_elements.get(1, 0), counts_elements.get(2, 0), counts_elements.get(3, 0)]))
    print("Evaluation counts:", evaluation_ratios_counts)
    try:
        positive_predictive_value = evaluation_ratios_counts["TP"]/(evaluation_ratios_counts["TP"]+evaluation_ratios_counts["FP"])
    except:
        positive_predictive_value = 0
    try:
        true_positive_rate = evaluation_ratios_counts["TP"]/(evaluation_ratios_counts["TP"]+evaluation_ratios_counts["FN"])
    except:
        true_positive_rate = 0
    try:
        false_discovery_rate = evaluation_ratios_counts["FP"]/(evaluation_ratios_counts["TP"]+evaluation_ratios_counts["FP"])
    except:
        false_discovery_rate = 0
    try:
        false_positive_rate = evaluation_ratios_counts["FP"]/(evaluation_ratios_counts["FP"]+evaluation_ratios_counts["TN"])
    except:
        false_positive_rate = 0
    try:
        false_omission_rate = evaluation_ratios_counts["FN"]/(evaluation_ratios_counts["TN"]+evaluation_ratios_counts["FN"])
    except:
        false_omission_rate = 0
    try:
        false_negative_rate = evaluation_ratios_counts["FN"]/(evaluation_ratios_counts["TP"]+evaluation_ratios_counts["FN"])
    except:
        false_negative_rate = 0
    try:
        negative_predictive_value = evaluation_ratios_counts["TN"]/(evaluation_ratios_counts["TN"]+evaluation_ratios_counts["FN"])
    except:
        negative_predictive_value = 0
    try:
        true_negative_rate = evaluation_ratios_counts["TN"]/(evaluation_ratios_counts["TN"]+evaluation_ratios_counts["FP"])
    except:
        true_negative_rate = 0

    t = PrettyTable(["", 'Is phishing', "Not phishing"])
    t.add_row(['Predicted phishing', "TP: {TP}".format(**evaluation_ratios_counts), "FP: {FP}".format(**evaluation_ratios_counts)])
    t.add_row(['', f"PPV: {np.round(positive_predictive_value*100, decimals=decimals)}%", f"FDR: {np.round(false_discovery_rate*100, decimals=decimals)}%"])
    t.add_row(['', f"TPR: {np.round(true_positive_rate*100, decimals=decimals)}%", f"FPR: {np.round(false_positive_rate*100, decimals=decimals)}%"])
    t.add_row(['Predicted safe', "FN: {FN}".format(**evaluation_ratios_counts), "TN: {TN}".format(**evaluation_ratios_counts)])
    t.add_row(['', f"FOR: {np.round(false_omission_rate*100, decimals=decimals)}%", f"NPV: {np.round(negative_predictive_value*100, decimals=decimals)}%"])
    t.add_row(['', f"FNR: {np.round(false_negative_rate*100, decimals=decimals)}%", f"TNR: {np.round(true_negative_rate*100, decimals=decimals)}%"])
    print(t)

    

results = model.evaluate(X_test_encoded_padded, y_test)
print(results)

mean_prediction = evaluate_nn_model(X_test_encoded_padded, y_test, threshold=0.5)
mean_prediction = evaluate_nn_model(X_test_encoded_padded, y_test, threshold=mean_prediction)
evaluate_nn_model(X_test_encoded_padded, y_test, threshold=1-(1/(oversampling_rate+1)))


# Making a prediction on a url using the model:
print()
show_top_n = 10
print(f"Predicting the first {show_top_n} examples from the test data:")

first_n_predictions = model.predict(X_test_encoded_padded[:show_top_n])
print(first_n_predictions.flatten())

prediction_df = pd.DataFrame(data={"domain_names": X_test[:show_top_n], "predictions": first_n_predictions.flatten(), "truth": y_test[:show_top_n]})
print(prediction_df)

def predict_url(url):
    encoded_text = sequence.pad_sequences([text_to_int(url)], max_seq_len)
    result = model.predict(encoded_text) 
    print("Prediction on url:", url, result[0][0])

print("\nPhishing ULR examples:")
predict_url("frgcxtmjzfjpdcusge.top")
predict_url("evilmadeupurl.phish")
predict_url("evil.madeupurl.phish")


print("\nSafe URL examples:")
predict_url("sharelatex.cryptobro.eu")
predict_url("sharelatex.cryptobro.eu:5000")

predict_url("google.com")
predict_url("www.google.com")
predict_url("gmail.google.com")
predict_url("mail.google.com")

predict_url("tudelft.nl")

predict_url("brightspace.tudelft.nl")

predict_url("colab.research.google.com")

predict_url("00-gayrettepe-t3-8---00-gayrettepe-xrs-t2-1.statik.turktelekom.com.tr")