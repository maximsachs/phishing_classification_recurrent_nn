import pandas as pd
import numpy as np
from collections import defaultdict
import matplotlib.pyplot as plt
import pprint
import urllib.request
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing import sequence
from tqdm import tqdm
import tensorflow as tf

random_seed = 59

np.random.seed(random_seed)

print(tf.config.list_physical_devices('GPU'))
# For some reason needed so the code runs properly on the gpu.
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    print('gpu', gpu)
    tf.config.experimental.set_memory_growth(gpu, True)
    print('memory growth:' , tf.config.experimental.get_memory_growth(gpu))

print("Phishtank Online Valid Dataset")
online_valid_df = pd.read_csv("online-valid.csv")

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


alexa_whitelist_df = pd.read_csv("top-1m.csv", header=None, names=["rank", "domain_names"])

# Finding if there are any domains that are also in the whitelist.
domains_in_whitelist = np.intersect1d(online_valid_df["domain_names"], alexa_whitelist_df["domain_names"])
# Tagging the whitelisted domains as such.
online_valid_df["in_whitelist"] = np.in1d(online_valid_df["domain_names"], domains_in_whitelist)

print(online_valid_df.shape[0], "rows")
print(online_valid_df.head(20))
print(tld_print.to_frame(name="TLD Count").transpose().to_string())
print(f"Percentage of top {show_top_n} tlds: {np.round(100*tld_df.iloc[:show_top_n].sum()/tld_df.sum(), decimals=2)} %")


print()
print("Alexa whitelist top 500k")

print(alexa_whitelist_df.shape[0], "rows")
print(alexa_whitelist_df.head(20))

print()
print("Number of urls that have domains which are in the whilelist:", online_valid_df["in_whitelist"].sum())


# For the dataset, excluding all where the domain name is in the whitelist.

online_valid_df_without_intersection = online_valid_df.loc[online_valid_df['in_whitelist'] == False]
alexa_whitelist_df_without_intersection = alexa_whitelist_df.loc[np.invert(alexa_whitelist_df['domain_names'].isin(domains_in_whitelist))]

phishing_domains = online_valid_df_without_intersection["domain_names"].values
whitelist_domains = np.random.choice(alexa_whitelist_df_without_intersection["domain_names"].values, size=len(phishing_domains))

# Calling a phishing url 1 and a benign url 0.
# Using character encoding as the vocabulary.
# Feeding the url as the sequence.

print()
print("Selected Data Examples:")
print("Phishing domains:", phishing_domains, len(phishing_domains))
print("Benign domains:", whitelist_domains, len(whitelist_domains))


vocab = sorted(set("".join(phishing_domains+whitelist_domains)), reverse=True)
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

# Creating the samples array and the label array
print()
X = list(phishing_domains) + list(whitelist_domains)
y = [1]*len(phishing_domains) + [0]*len(whitelist_domains)

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

X_train, X_test, y_train, y_test = train_test_split(np.array(X), np.array(y), test_size=0.15, random_state=random_seed)

show_top_n = 5
print(f"Training and testing data: (showing first {show_top_n})")
print(f"Train data {len(X_train)} samples")
print(list(zip(X_train[:show_top_n], y_train[:show_top_n])))
print(f"Test data {len(X_test)} samples")
print(list(zip(X_test[:show_top_n], y_test[:show_top_n])))

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
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, 64),
    # tf.keras.layers.LSTM(32, return_sequences=True),
    tf.keras.layers.LSTM(32),
    tf.keras.layers.Dense(1, activation="sigmoid")
])


# Compiling the model
model.compile(loss="binary_crossentropy", optimizer="rmsprop", metrics=['acc'])
print(model.summary())

# Training the model
history = model.fit(X_train_encoded_padded, y_train, epochs=3, validation_data=(X_test_encoded_padded, y_test))

#Evaluating the model
results = model.evaluate(X_test_encoded_padded, y_test)
print(results)


# Making a prediction on a url using the model:
print()
show_top_n = 10
print(f"Predicting the first {show_top_n} examples from the test data:")

first_n_predicitons = model.predict(X_test_encoded_padded[:show_top_n])
print(first_n_predicitons.flatten())

prediction_df = pd.DataFrame(data={"domain_names": X_test[:show_top_n], "predicitons": first_n_predicitons.flatten(), "truth": y_test[:show_top_n]})
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