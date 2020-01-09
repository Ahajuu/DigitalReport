import cv2
import numpy as np
import requests

url=''



while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, -1)
    cv2.imshow("AndroidCam",img)
    if cv2.waitKey(1) == 27:
        break
