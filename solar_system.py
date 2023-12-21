import cv2

img = cv2.imread("solar_system.jpg")

cv2.putText(img,
            "Sol",
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0 0 10)
            )

cv2.putText(img,
            "Mercurio",
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0 0 20)
            )

cv2.putText(img,
            "Venus",
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0 0 30)
            )

cv2.putText(img,
            "Tierra",
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0 0 40)
            )

cv2.putText(img,
            "Júpiter",
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0 0 50)
            )

cv2.putText(img,
            "Saturno",
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0 0 60)
            )

cv2.putText(img,
            "Urano",
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0 0 70)
            )

cv2.putText(img,
            "Neptuno",
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0 0 80)
            )

cv2.imshow("Output", img)

print(img)

cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg", img)
