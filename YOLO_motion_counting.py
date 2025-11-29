#Detection on every 10th(say) frame and tracking in between is proven to be the best 
#approach rather than detection on each frame which is slow and inefficient

import cv2
from ultralytics import YOLO

# Loading video
cap = cv2.VideoCapture("traffic_vdo.mp4")

# Loading model
model = YOLO("yolov8n.pt")

# Defining counting line
y_line = 300
offset = 0 #Tolerance for crossing
count = 0
# Storing position of each tracked object
prev_positions = {}
array = []
while True:
    ret, frame = cap.read()
    if not ret:
        break
    # Run YOLO tracking
    results = model.track(frame[:, 150:], persist=True)  # persist=True keeps IDs
    frame = frame[:, 150:]
    if results[0].boxes is not None:
       for box in results[0].boxes:
          track_id = int(box.id[0]) #unique object ID
          cls = int(box.cls[0]) #class
          x1, y1, x2, y2 = box.xyxy[0]

         # Usint object center for crossing logic
          cx = int((x1+x2)/2)
          cy = int((y1+y2)/2)
          #print(cy)

         # Draw tracking ID + box
          cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0,255,0), 2)
          cv2.putText(frame, f"ID {track_id}", (int(x1), int(y1)-5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)

          if cls == 2:
             if track_id not in array:
              if cy > y_line - offset :
                count += 1
                print(count)
                array.append(track_id)

    # Drawing the counting line and putting text
    cv2.line(frame, (0, y_line), (frame.shape[1], y_line), (0,255,0), 2)
    cv2.putText(frame, f"Count: {count}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Motion-Based Counting", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
       break
        
cap.release()
cv2.destroyAllWindows()