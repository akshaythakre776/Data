# import docx2txt
# my_text = docx2txt.process("test.docx")
# print(my_text)

from imageai.Prediction import ImagePrediction
import os
execution_path = os.getcwd()
prediction = ImagePrediction()
prediction.setModelTypeAsResNet()
prediction.setModelPath( execution_path + "\resnet50_weights_tf_dim_ordering_tf_kernels.h5")
prediction.loadModel()


predictions, percentage_probabilities = prediction.predictImage("C:\Users\athakre\Downloads\sample.jpeg", result_count=5)
for index in range(len(predictions)):
print(predictions)