# Vehicle Type Recognition using CNN and ElasticNet
---

## Project Background
In daily life, road traffic is filled with different types of vehicles such as cars, trucks, buses, and motorcycles. However, identifying and distinguishing these vehicle types from images can be a complicated task, especially in scenarios such as traffic monitoring or vehicle density analysis. With the advancement of machine learning technology, we have the opportunity to develop solutions that can aid automation in vehicle type recognition.

## Project Dataset
Dataset name : `Vehicle-dataset`

Dataset source : [Kaggle - Vehicle Type Recognition](https://www.kaggle.com/datasets/kaggleashwin/vehicle-type-recognition)

This is a vehicle image classification dataset containing images of four different types of vehicles: Car, Truck, Bus, and Motorcycle. The dataset is curated to help learners to develop and evaluate image classification models for identifying various vehicle types from images.

## Objective
The main objective of this project is to build a machine learning model that can distinguish between four categories of vehicles: cars, trucks, buses, and motorcycles using Convolutional Neural Networks (CNN) and ElasticNet.

## Result
- Accuracy Score Model CNN : **56%**
- Acuracy Score Model ElasticNet : **94%**

## Conclusion
Based on our test results above between the model we have built and the model with transfer learning, we can conclude that:

- In terms of accuracy, the model with transfer learning is much more accurate than the simple model we have built. This is proven by the Accuracy Score between the two models.

- Although the transfer learning model has good accuracy, it also has weaknesses. The model is good for recognizing vehicles with clear images or focus on 1 object image, but weak if the object image is small or out of focus. This is proven during the Inference Model.

- In both models, the training time is also long. This also needs to be considered when building real-time models.

- In business, the model with ElasticNet can help recognize the type of vehicle accurately on the condition that the image must be clear and expose the object. With these advantages, the model with ElasticNet is suitable for parking management, traffic analysis, market analysis and public facility security.

## Suggestions for Improvement

- Model Architecture Exploration: You can try exploring different model architectures, such as changing or adding layers to your model. You can also try better preprocessing models to extract better features from images.

- Hyperparameter Tuning: You can adjust the training hyperparameters, such as the learning rate or batch size. These adjustments can help speed up model convergence and improve performance.

- Data Augmentation: Adding data variations by augmentation (e.g. rotation, cropping, or shifting) can help the model learn a wide variety of images. This can help improve the accuracy of the model.

- Regularization: Applying regularization techniques such as dropout or weight decay can help reduce overfitting if needed.

- Further Data Collection: If possible, collecting more training data can help improve model performance. The more variety of data a model has, the better it is at generalizing knowledge.

- Testing with New Data: Once you have updated your model, make sure to test the model with data that it has never seen before (test data) to get a better estimate of its performance in the real world.

- Hardware Optimization: If you have access to more powerful hardware (for example, a faster GPU), this can help speed up training.
