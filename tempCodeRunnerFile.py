     data_dir = "D:\Projects\data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert('L')  # grey scale image
            imgNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imgNp)
            ids.append(id)
            cv2.imshow('Training', imgNp)
            cv2.waitKey(1)
        ids = np.array(ids)

        # ============================Training========
        clf = cv2.createLBPHFaceRecognizer()  # Alternative method that should work for both OpenCV 3.x and 4.x
        clf.train(faces, ids)
        clf.write('Classifier.xml')
        cv2.destroyAllWindows()
        messagebox.showinfo('Results', 'Data Training Completed')
