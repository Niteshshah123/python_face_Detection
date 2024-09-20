import requests

# URLs of the files to download
prototxt_url = "https://github.com/opencv/opencv/raw/master/samples/dnn/face_detector/deploy.prototxt"
caffemodel_url = "https://github.com/opencv/opencv_3rdparty/raw/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel"

# Download deploy.prototxt.txt
print("Downloading deploy.prototxt...")
prototxt_response = requests.get(prototxt_url)
with open("deploy.prototxt.txt", "wb") as f:
    f.write(prototxt_response.content)

# Download res10_300x300_ssd_iter_140000.caffemodel
print("Downloading res10_300x300_ssd_iter_140000.caffemodel...")
caffemodel_response = requests.get(caffemodel_url)
with open("res10_300x300_ssd_iter_140000.caffemodel", "wb") as f:
    f.write(caffemodel_response.content)

print("Download completed.")
