import cv2

def main():

    idx = 0
    cam = cv2.VideoCapture(idx)

    if cam is None or not cam.isOpened():
        print('Can´t open camera:', idx)

    else:
        while True:

            ret, img = cam.read()

            if ret == True:

                img = cv2.resize(img, (640, 480))
                cv2.imshow('Camera', img)

                key = cv2.waitKey(1) & 0xFF
                if key == ord("q"):
                    break
            else:
                cam = cv2.VideoCapture(idx)

        cam.release()
        cv2.destroyAllWindows()

    print("Camera closed")


if __name__ == "__main__":
   main()