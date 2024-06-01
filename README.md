# Cat-Dog Classifier with MobileNet


![Meow or Woof](https://github.com/ArdaKaymaz/cat_dog_classifier_mobilenet/assets/146623362/cd87745a-8167-4c3a-8bfb-46c4ab340445)


<strong>Project Summary:</strong> Cat and Dog Image Classification

This project focuses on developing an image classification system to distinguish between images of cats and dogs. The workflow involves data collection, preprocessing, model training, and deployment techniques.

<strong>Data Collection:</strong> Cat and dog images were obtained using the Bing Image Downloader tool.

<strong>Data Preprocessing:</strong> To handle the dataset efficiently, the ImageDataGenerator and flow_from_directory functions were utilized for preprocessing and loading the images, reducing computational strain.

<strong>Model Selection and Fine-tuning:</strong> Transfer learning was employed with the MobileNet pre-trained model as the base architecture. Fine-tuning was performed using the dataset to enhance performance on the specific task.

![model](https://github.com/ArdaKaymaz/cat_dog_classifier_mobilenet/assets/146623362/c63eb873-2d79-4eb2-9027-9612028b09ee)

<strong>Experiment Tracking with MLflow:</strong> MLflow was employed to monitor the training process, log metrics, and register the best-performing model, enabling efficient experiment management.

![mlflow](https://github.com/ArdaKaymaz/cat_dog_classifier_mobilenet/assets/146623362/dbe4b7b1-8f57-49e5-a52a-c9fb49d968cd)

<strong>Model Evaluation:</strong> Performance evaluation was conducted by making predictions on a validation set. The highest achieved validation accuracy was <strong>77.55%<strong>, with the best-performing model selected for deployment.

![tensorboard](https://github.com/ArdaKaymaz/cat_dog_classifier_mobilenet/assets/146623362/b6e24c46-f6fb-4881-8073-300bbc0005d6)

<strong>Model Deployment:</strong> The chosen model was deployed to an MLflow server, allowing access via an endpoint. Interaction with the deployed model and predictions on new unseen data were facilitated using requests.

![test](https://github.com/ArdaKaymaz/cat_dog_classifier_mobilenet/assets/146623362/f1fc342d-92c5-4f2f-bcb9-3ba89d20c03e)

This structured approach enabled the development of a robust image classification system for distinguishing between cats and dogs, with the ability to track experiments, deploy models, and make predictions in real-world scenarios.
