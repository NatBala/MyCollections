import keras
from sklearn.metrics import roc_auc_score


class TestCallback(keras.callbacks.Callback):
    def __init__(self, test_data):
        self.test_data = test_data

    def on_train_begin(self, logs={}):
        self.aucs = []

    def on_epoch_end(self, epoch, logs={}):
        x, y = self.test_data
        loss, acc = self.model.evaluate(x, y, verbose=0)
        #y_pred = self.model.predict(x)
        #self.aucs.append(roc_auc_score(y, y_pred))
        return
#
# class Histories(keras.callbacks.Callback):
#     def on_train_begin(self, logs={}):
#         self.aucs = []
#         self.losses = []
#
#     def on_train_end(self, logs={}):
#         return
#
#     def on_epoch_begin(self, epoch, logs={}):
#         return
#
#     def on_epoch_end(self, epoch, logs={}):
#         self.losses.append(logs.get('loss'))
#         y_pred = self.model.predict(self.model.validation_data[0])
#         self.aucs.append(roc_auc_score(self.model.validation_data[1], y_pred))
#         return
#
#     def on_batch_begin(self, batch, logs={}):
#         return
#
#     def on_batch_end(self, batch, logs={}):
#         return
