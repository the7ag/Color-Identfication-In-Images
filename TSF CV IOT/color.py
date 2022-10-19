######### Made By : Mohamed Ali Bayoumi #######################




import cv2 #include computer vision lib
import pandas as pd #include the pandas lib

img = cv2.imread("test.jpg") #the image that we can detect color in

clicked = False #Double click stat initally false
r = g = b = x_pos = y_pos = 0 #mouse position and rgb values

index = ["color", "color_name", "hex", "R", "G", "B"] #list to traverser through the csv file
csv = pd.read_csv("colors.csv", names=index, header=None)#Panda object def

##this function gets the color closest in range for colors of the csv file
def get_color_name(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

##This fucntion detect the mouse x y pos and in return will show the color that the mouse double clicked on
def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)

#showing the window
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function) #calling the function on the double click event
#the main program that shows the rectangle with color in it and the name of the color
while True:

    cv2.imshow("image", img)
    if clicked:

        cv2.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)

        text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()
