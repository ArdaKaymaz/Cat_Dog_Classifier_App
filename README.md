# Cat-Dog Classifier App


![meow_or_woof](https://github.com/ArdaKaymaz/Cat_Dog_Classifier_App/assets/146623362/46059f6b-e563-4486-b8d4-515676b51a61)


<strong>Project Summary:</strong> Cat and Dog Image Classification

This project focuses on developing an image classification system to distinguish between images of cats and dogs. The workflow involves image preprocessing, model training, and creating app with the best model.

<strong>Image Preprocessing:</strong> To handle the dataset efficiently, the ImageDataGenerator and flow_from_directory functions were utilized for preprocessing and loading the images, reducing computational strain.

<strong>Model Selection and Fine-tuning:</strong> Transfer learning was employed with MobileNet, VGG16 and ResNet50 pre-trained models as the base architecture. Fine-tuning was performed using the dataset to enhance performance on the specific task.

![model](https://github.com/ArdaKaymaz/cat_dog_classifier_mobilenet/assets/146623362/c63eb873-2d79-4eb2-9027-9612028b09ee)

<strong>Experiment Tracking with MLflow:</strong> MLflow was employed to monitor the training process, log metrics, and register the best-performing models, enabling efficient experiment management.

![mlflow](https://github.com/ArdaKaymaz/cat_dog_classifier_mobilenet/assets/146623362/dbe4b7b1-8f57-49e5-a52a-c9fb49d968cd)

<strong>Model Evaluation:</strong> Various performance metrics were used for model evaluation. According to these metrics, VGG16 was chosen for its accuracy on validation data, model size, and prediction duration. While the training duration of VGG16 was the highest among all the models, its advantages are promising in the long run.

![tensorboard](https://github.com/ArdaKaymaz/cat_dog_classifier_mobilenet/assets/146623362/b6e24c46-f6fb-4881-8073-300bbc0005d6)

<strong>Model Deployment:</strong> All the three models were registered to an MLflow server, allowing access via an endpoint. The best model, VGG16, was chosen for production stage and integrated to Streamlit application.

![test](https://github.com/ArdaKaymaz/cat_dog_classifier_mobilenet/assets/146623362/f1fc342d-92c5-4f2f-bcb9-3ba89d20c03e)

This structured approach enabled the development of a robust image classification system for distinguishing between cats and dogs, with the ability to track experiments, deploy models, and make predictions in real-world scenarios.
