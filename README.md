# Phish Hunter AI

Phish Hunter is a Machine Learning Artificial Intelligence application
developed to analyze URLs, obtain various datapoints and make a prediction
to if it is a valid Phishing website or not.

Phish Hunter follows the "Phishing Websites Features" outlined and documented by
Rami M. Mohammad, Fadi Thabtah and Lee McCluskey.

The dataset used in this version has been changed from the original to remove the
page_rank, google_index ,links_pointing_to_page, and statistical_report datapoints
as there is some complications obtaining that data due to situations like Google
blocking users from making search request from code.

Though these data points have been removed, this new design and trained data model
still holds a 95% prediction success rate.

My goal is too add additional datapoints to counter the removal of the 4 mentioned
above, but this may take some time as it will require me to build a new and
custom dataset for training purposes since the original URLs used to build the 
original training dataset were not included in any of the publications
that I was able to locate.

Furthermore, while this project could be expanded with a Flask interface for allowing
users to make requests via a provided web service, I have decided to write this
project in a way that will make it usable by many projects and so that you 
can "import" it into your own Python applications to create Internet crawlers,
web services, and tools to protect your corporate employees and clients.

For the dataset, saved pickle, and website features outline please see the 
original_publications/* directory. With some modifications, and new functions in
the libs/features.py you could bring the original version back should you have
the desire to do so.

Enjoy

## Getting Started
Install instructions and all the cool shit goes here....


## Use cases

If you haven't already, make sure you are in your environment.

```bash
$ source venv/bin/activate
```


## Train the AI Model

```bash
$ python train_phish_hunter.py
usage: analyze_url [-h] [-d DATASET] [-o DOT] [-m MATRIX]

Analyze a URL for debugging the Phish Hunter ML AI

options:
  -h, --help            show this help message and exit
  -d DATASET, --dataset DATASET
  -o DOT, --dot DOT
  -m MATRIX, --matrix MATRIX


```

Unless you have renamed the dataset, the command below will work right off the rip of a git clone of this repository.

```bash
$ python train_phish_hunter.py -d new_dataset.csv -o tree.dot -m confusion_matrix.png


#################################################################################################
[+] Staring Phish Hunter AI Training Mode...
[+] Splitting data into Train and Test data...
[+] Creating Model Decision Tree Classifier...
[+] Fitting data and training the Model...
[+] Making predictions with Xtest...

              precision    recall  f1-score   support

          -1       0.93      0.96      0.95      1209
           1       0.97      0.94      0.96      1555

    accuracy                           0.95      2764
   macro avg       0.95      0.95      0.95      2764
weighted avg       0.95      0.95      0.95      2764

Accuracy Score: 95.0 %

[+] Saving Confusion Matrix...
[+] Saving dot file...
[+] Converting dot file to image...
[+] Saving the model to file for later use...
[+] DONE!
```


## Analyze a URL

I would like to circle back and break down each point so you can understand the
datapoint that determined the result like I did with the Length, but
I will come back to this. For now, here is a starting point.

```bash
$ python analyze_url.py
usage: analyze_url [-h] [-u URL]

Analyze a URL for debugging the Phish Hunter ML AI

options:
  -h, --help         show this help message and exit
  -u URL, --url URL
```

```bash
python analyze_url.py -u https://welcome-doc-exodus.github.io/en-us/
Length of URL: 43 : https://welcome-doc-exodus.github.io/en-us/
{
    "having_IP_Address": -1,
    "URL_Length": -1,
    "Shortining_Service": -1,
    "having_At_Symbol": -1,
    "double_slash_redirecting": -1,
    "Prefix_Suffix": 1,
    "having_Sub_Domain": -1,
    "SSLFinal_State": -1,
    "Domain_registeration_length": 1,
    "Favicon": 1,
    "port": -1,
    "HTTPS_token": -1,
    "Request_URL": -1,
    "URL_of_Anchor": -1,
    "Links_in_tags": -1,
    "SFH": -1,
    "Submitting_to_email": -1,
    "Abnormal_URL": -1,
    "Redirect": -1,
    "on_mouseover": -1,
    "RightClick": -1,
    "popUpWidnow": -1,
    "Iframe": 1,
    "age_of_domain": 1,
    "DNSRecord": -1,
    "web_traffic": 1
}
```