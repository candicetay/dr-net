#%%
# import methods defined in the other files
from OCREngine import OCREngine
from FeatureEngine import FeatureEngine
from Invoice import Invoice
from Token import Token
from Classifier import Classifier
from util import features_to_use

print("Starting...")
invoices = FeatureEngine.load_invoices_and_map_labels(
    "/Users/suenwailun/Sync Documents/University/Y4S1/BT3101 Business Analytics Capstone Project/Training data",
    autoload=False,
    verbose=True,
)
#%%
print("\nCreating training and testing data...")
data = Classifier.create_train_and_test_packet(invoices, features_to_use)

#%%
classifier = Classifier()
print("Training classifier with features of dimension", len(data["train_data"][0]))
classifier.train("Neural Network", data["train_data"], data["train_labels"])
predictions = classifier.predict_token_classifications(
    data["test_data"], "Neural Network"
)
classifier.prediction_summary(predictions=predictions, labels=data["test_labels"])


#%%
import json

invoices_perf = classifier.sort_invoices_by_predictive_accuracy(
    invoices, "Neural Network"
)
with open("invoice scores.json", "w") as f:
    f.write(json.dumps(invoices_perf))
print("Worst 20 performers:")
for invoice in invoices_perf[:20]:
    print(
        f"Name of invoice: {invoice['name']}     Accuracy: {invoice['overall_accuracy']}"
    )

#%%
