from imageai.Detection import ObjectDetection
import os

def setup_paths():
    # Create directories if they don't exist
    for dir_name in ['Models', 'Input', 'Output']:
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

def main():
    setup_paths()
    
    # instantiating the class
    recognizer = ObjectDetection()
    
    # defining the paths
    path_model = "./Models/yolov3.pt"
    path_input = "./Input/images.jpeg"
    path_output = "./Output/newimage.jpeg"
    
    # using the setModelTypeAsYOLOv3() function for PyTorch
    recognizer.setModelTypeAsYOLOv3()
    
    # setting the path to the pre-trained PyTorch Model
    recognizer.setModelPath(path_model)
    
    # loading the model
    recognizer.loadModel()
    
    # calling the detectObjectsFromImage() function
    recognition = recognizer.detectObjectsFromImage(
        input_image=path_input,
        output_image_path=path_output
    )
    
    # iterating through the items found in the image
    for eachItem in recognition:
        print(eachItem["name"], " : ", eachItem["percentage_probability"])

if __name__ == "__main__":
    main()
