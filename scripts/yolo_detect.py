from ultralytics import YOLO
import cv2

model = YOLO("weights/best.pt")
vid_path = "sample2.mp4"
cap = cv2.VideoCapture(vid_path)
output_path = "annotated_sample2.mp4"
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
fps = cap.get(cv2.CAP_PROP_FPS)
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

while cap.isOpened():
    success, frame = cap.read()
    if success:
        results = model(frame, conf=0.20)
        annotated_frame = results[0].plot()
        cv2.imshow("YOLO inference", annotated_frame)
        out.write(annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
