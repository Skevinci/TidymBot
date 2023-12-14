import socket
import struct
import json
import numpy as np
import cv2
import apriltag
import time

HOST = "sled-whistler.eecs.umich.edu"
PORT = 12345

class Capture():
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3, 640)
        self.cap.set(4, 480)
        self.detector = apriltag.Detector()
        
    def show(self):
        while True:
            ret, frame = self.cap.read()
            frame = cv2.flip(frame, 0)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        self.cap.release()
        cv2.destroyAllWindows()
        
    def debugImg(self):
        i = 0
        while True:
            ret, frame = self.cap.read()
            # frame = cv2.flip(frame, 0)
            cv2.imshow('frame', frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            print(i)
            if self.detector.detect(gray):
                detections = self.detector.detect(gray, return_image=True)
                print(detections)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            time.sleep(1)
            i += 1
        
        self.cap.release()
        cv2.destroyAllWindows()
        
    def checkDir(self, obj):
        ret, frame = self.cap.read()
        # frame = cv2.flip(frame, 0)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if not self.detector.detect(gray):
            return False
        else:
            detections = self.detector.detect(gray)
            # print(detections)
            goal_id = self.obj2tagid(obj)
            print("==========", detections[0].tag_id)
            print("==========", detections[0].center[0])
            
            if goal_id != detections[0].tag_id:
                return False
            else:
                if goal_id < 5:
                    if detections[0].center[0] > 310 and detections[0].center[0] < 340:
                        print("============See the center!================")
                        return True
                    else:
                        return False
                else:
                    if detections[0].center[0] > 270 and detections[0].center[0] < 400:
                        print("============See the center!================")
                        return True
                    else:
                        return False
        
        
    def checkDis(self, obj):
        ret, frame = self.cap.read()
        # frame = cv2.flip(frame, 0)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if self.detector.detect(gray):
            detections = self.detector.detect(gray)
            goal_id = self.obj2tagid(obj)
            
            if goal_id != detections[0].tag_id:
                return False
            else:
                edge = abs(detections[0].corners[0][1] - detections[0].corners[3][1])
                print("Edge length: ", edge)
                if goal_id >= 6:
                    if edge > 90:
                        time.sleep(1.8)
                        return True
                    else:
                        return False
                elif goal_id == 5:
                    if edge > 6:
                        time.sleep(1.8)
                        return True
                    else:
                        return False
                else:
                    if edge > 50: # the parameters need to be tuned
                        time.sleep(2.3)
                        return True 
                    else:
                        return False
        else:
            return False
        
        
    def obj2tagid(self, obj):
        if obj == "blue":
            print("===object===", 0)
            return 0
        elif obj == "red":
            print("===object===", 1)
            return 1
        elif obj == "green":
            print("===object===", 2)
            return 2
        elif obj == "upper left":
            print("===object===", 5)
            return 5
        elif obj == "upper right":
            print("===object===", 6)
            return 6
        elif obj == "lower left":
            print("===object===", 7)
            return 7
        elif obj == "lower right":
            print("===object===", 8)
            return 8
        else:
            return 11
        
def videoCap():
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)
    detector = apriltag.Detector()
    while True:
        ret, frame = cap.read()
        # frame = cv2.flip(frame, 1)
        # cv2.imshow('frame', frame)
        # cv2.imwrite('frame.png', frame)
        # img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)
        results = detector.detect(gray)
        print(results)
        
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        
        time.sleep(3)
        
    #     time.sleep(1)
    
    cap.release()
    cv2.destroyAllWindows()
    
def tagDetector():
    img_path = "/home/pi/TidymBot/server/tag.png"
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    detector = apriltag.Detector()
    results = detector.detect(img)
    print(results)
    
def communicate(request):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))
        print("Connect to Server...")
        
        client_socket.sendall(request.encode('utf-8'))
        
        response = client_socket.recv(1024).decode('utf-8')
        response = json.loads(response)
        if response:
            print(f"Received response from side B: {response}")
            
            client_socket.close()
            return response
        return
    
if __name__ == '__main__':
    # communicate("Hello")
    videoCap()
    # tagDetector()