
# Yet Another License Plate Detector 

Yet Another License Plate Detector using the state of the art YOLO model trained on the Roboflow dataset to detect, well, license plates!
## Demo
You can watch the model prediction demo video `demo/annotated_video.mp4`. The input video is `demo/test_video.mp4`.

## Features

- Real-time detection of license plates using YOLO
- Configurable confidence threshold for detection accuracy
- Visual feedback with bounding boxes and extracted text displayed on images
- OCR-based text extraction from detected license plates (future integration)

## Libraries Used
- YOLO
- OpencV

## How to use?

Clone this repo:

```bash
git clone https://github.com/Forenche/yalpd.git
```
Install required dependencies with:
```bash
pip install -r requirements.txt
```
Open `scripts/yolo_detect.py` and change the `vid_path` and `output_path`. After that save the file(important) and run using `python scripts/yolo_detect.py`. You may exit the window using `q`.

## Script and Jupyter Notebook Details
The YOLO model was trained with the `license_plate.ipynb` and the results were visualized using `yolo_detect.py`. The python script reads in a video and outputs the number of license plates detected in the terminal while OpenCV is used to display the annotated frames on the input image in real time and writes the annotated video to your local machine.

## Future Plans

- Integrate Keras OCR to read license plate text
- Track vehicles in real time
- Mix in more vehicles and license plates in the dataset
- Deploy the model to use in real time
