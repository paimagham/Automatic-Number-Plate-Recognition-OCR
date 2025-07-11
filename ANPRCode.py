import cv2
import pytesseract

# Load the image
img = cv2.imread('images/car1.jpg')

# Check if the image was loaded successfully
if img is None:
    print("Error: Could not load image.")
else:
    # Display original image
    print("Original Image:")
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    cv2.imshow("Original Image", img)
    cv2.waitKey(2000)  # waits for 2 seconds
    cv2.destroyAllWindows()


    # Converting to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Display grayscale image
    print("Grayscale Image:")
    cv2.imshow("Grayscale Image", gray)
    cv2.waitKey(2000)  # waits for 2 seconds
    cv2.destroyAllWindows()



    # Reducing the noise
    gray_filtered = cv2.bilateralFilter(gray, 12, 18, 18)
    print("Smoothned Image:")
    cv2.imshow("Smoothened Image", gray_filtered)
    cv2.waitKey(2000)  # waits for 2 seconds
    cv2.destroyAllWindows()



    # Detect the edges
    edged = cv2.Canny(gray_filtered, 40, 300)
    print("Edged Image:")
    cv2.imshow("Edged Image", edged)
    cv2.waitKey(2000)  # waits for 2 seconds
    cv2.destroyAllWindows()


    # Recognizing the image's contours from its edges
    cnts, new = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    img1 = img.copy()
    cv2.drawContours(img1, cnts, -1, (0, 255, 0), 3)
    print("Contours:")
    cv2.imshow("Contours", img1)
    cv2.waitKey(2000)  # waits for 2 seconds
    cv2.destroyAllWindows()



    # Sorting out the known contours
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:30]
    screenCnt = None
    img2 = img.copy()
    cv2.drawContours(img2, cnts, -1, (0, 255, 0), 3)
    print("Top 30 contours:")
    cv2.imshow("Top 30 contours", img2)
    cv2.waitKey(2000)  # waits for 2 seconds
    cv2.destroyAllWindows()



    # Locating the four-sided contour
    i = 7
    for c in cnts:
          perimeter = cv2.arcLength(c, True)
          approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
          if len(approx) == 4:
                screenCnt = approx
                x, y, w, h = cv2.boundingRect(c)
                new_img = img[y:y + h, x:x + w]
                cv2.imwrite('./' + str(i) + '.png', new_img)
                i += 1
                break

    # Drawing the chosen contour on the original image
    if screenCnt is not None:
        cv2.drawContours(img, [screenCnt], -1, (0, 255, 0), 3)
        print("Image with detected license plate:")
        cv2.imshow("Image with Detected License Plate", img)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()



        # Obtaining text from the license plate's cropped image
        Cropped_loc = './7.png'
        print("Cropped image:")
        cropped_img = cv2.imread(Cropped_loc)
        cv2.imshow("Cropped License Plate", cropped_img)
        cv2.waitKey(2000)
        cv2.destroyAllWindows()


        # Using pytesseract to read text
        plate = pytesseract.image_to_string(cropped_img)
        print("Number plate is:", plate)
    else:
        print("No quadrilateral contour found.")
