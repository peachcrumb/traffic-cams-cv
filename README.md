# traffic-cams-cv

## Steps for Using traffic-cams-cv Files

1. Save repo contents to target destination
* You will likely need cloud computing for these tasks – it is not recommended to run on your local machine or without a virtual environment.


2. Create and activate virtual environment
* In your command line prompt at the target location, it is recommended you run the following: 
```
     python3 -m venv ~/venv
     source ~/venv/bin/activate
     pip install ultralytics # this is for step 5, in order to run yolov11 in the script
```


3. Obtain Data from Relevant Sources
Some options to collect data:

* Image Scraping: Use web scraping tools or APIs to collect images from online sources.
    * For [pySNAPSHOT_GoAkamai_ALL.py](https://github.com/peachcrumb/traffic-cams-cv/blob/main/pySNAPSHOT_GoAkamai_ALL.py), you can run it once from its location using `python3 pySNAPSHOT_GoAkamai_ALL.py` or set up an automation to scrape every x minutes:
    * In the command lne, enter `crontab -e` and paste the following at the bottom in an uncommented line: `*/10 * * * * cd /media/volume/test_Data && /usr/bin/python3 pySNAPSHOT_GoAkamai_ALL.py >> /media/volume/test_Data/log_file.log 2>&1` 
    * You may need to edit the path or filenames in the python script and/or crontab editor to point to where to store the images.

* Roboflow: A popular platform to find and annotate datasets for tasks like object detection.
    * You'll likely need to create a Roboflow account to use its features or export any public datasets. This repository assumes you will use the [y11model.py](https://github.com/peachcrumb/traffic-cams-cv/blob/main/y11model.py) script, so only data is relevant from the site, not necessarily available models.


4. Prepare to train model on dataset
Since the `y11model.py` script uses an image classification model, the data path structure should look like:  

folder-name-/  
|-- train/  
|   |-- airplane/  
|   |-- automobile/  
|   |-- bird/  
|   ...  
|-- test/  
|   |-- airplane/  
|   |-- automobile/  
|   |-- bird/  
|   ...  
|-- val/ (optional)  
|   |-- airplane/  
|   |-- automobile/  
|   |-- bird/  
|   ...  

With the relevant images sorted into each label class.


5. Initiate the Training Phase  
Assuming the virtual environment is activated and the `ultralytics` library was installed successfully,
* Check the path or filenames in the `y11model.py` script to ensure the model grabs from the right dataset folder & path
* Be sure to configure the right hyperparameters (learning rate, batch size, epochs, etc.) in the script
* Once the above is completed, run `python3 y11model.py`


6. Check Model Outputs
Once training begins, frequently check your model’s outputs on validation data to assess its performance. This might include visual checks (e.g., does the model accurately detect objects or classify images?) and numerical metrics like accuracy, precision, recall, or loss.
If the results are unsatisfactory, go back and adjust your model or data and monitor the training process for any issues, such as overfitting or underfitting.


9. Make Changes as Needed  
Based on the performance of your model, you may need to:
* Increase the dataset size: Gather more data or use data augmentation to ensure your model can generalize well.
* Tweak parameters: Adjust learning rates, batch sizes, or other model hyperparameters.
* Use transfer learning: Fine-tune a pre-trained model with your own data to improve performance on a specific task.
9. Prepare for Deployment
Once your model has reached an acceptable level of accuracy and performance, it’s time to prepare for deployment. This may involve:
* Model Optimization: Reduce the model's size and complexity for faster inference (e.g., using techniques like quantization or pruning).
* API Integration: Set up an API to allow others to interact with your model in real-time.
* Deploy to Cloud: Deploy your model to a cloud service (e.g., AWS, Azure, or Google Cloud) for scalability and accessibility.
Finally, test your deployed model to ensure it performs well in a production environment, making any final adjustments if necessary.

## References

[Ultralytics YOLO Documentation](https://docs.ultralytics.com/datasets/classify/)

