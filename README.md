# FPGA Project

## Using the YOLOv3 Model

This project utilizes FPGA technology for object detection using the YOLOv3 model. Below are the instructions for setting up the environment and running the model.

### Prerequisites
- Ensure that you have the `imageai` library installed.
- Place the `yolov3.pt` file in the `Models` directory.

### Running the Object Detection
1. Make sure the input image is placed in the `Input` directory.
2. Run the `object_detection.py` script:
   ```bash
   python object_detection.py
   ```
3. The output will be saved in the `Output` directory, and the console will display the detected objects along with their confidence levels.

This project utilizes FPGA technology for object detection using the YOLOv3 model. The following instructions will guide you through setting up the environment and running the model.

## Installation Instructions

To set up the environment for this project, install the required dependencies by running the following commands:

- **PyTorch and ImageAI:**

  ```bash
  pip install torch torchvision torchaudio imageai
  ```

- **PyBvision:**

  ```bash
  pip install pybvision
  ```

**Note:** If you encounter issues related to OpenGL, you may need to install the `libgl1` package:

```bash
sudo apt-get update && sudo apt-get install -y libgl1
```

## Dependencies

- `torch` (PyTorch)
- `torchvision`
- `torchaudio`
- `imageai`
- `pybvision`

Ensure all dependencies are installed using the commands provided above.

## Model Usage

The model `Models/yolov3.pt` is used for object detection. To set up and use the model:

1. **Download the YOLOv3 Model:**

   Download the YOLOv3 model file and place it in the `Models` directory:

   ```bash
   wget -P ./Models https://github.com/OlafenwaMoses/ImageAI/releases/download/3.0.0-pretrained/yolov3.pt
   ```

2. **Prepare Input Images:**

   Place your input images in the `Input` directory.

3. **Run the Model:**

   Ensure you have the YOLOv3 model file located at `Models/yolov3.pt` for object detection functionality. Use the appropriate script or command to run the model on your input images.

**Note:** Replace the placeholder script or command with the actual command used to run the model, as it is not specified in the provided information.

By following these steps, you will set up the environment and run the object detection model successfully.
