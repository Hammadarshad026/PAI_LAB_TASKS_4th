import cv2
import numpy as np

def draw_circle(image_path):
    # Read the image
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Unable to load image. Check the file path.")
        return
    
    # Define the center and radius of the circle
    center_coordinates = (200, 200)
    radius = 100
    color = (0, 0, 255)  # Red color in BGR
    thickness = 3  # Circle outline thickness (-1 for filled circle)
    
    # Draw the circle on the image
    cv2.circle(img, center_coordinates, radius, color, thickness)
    
    # Display the result
    cv2.imshow('Image with Circle', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Call function with image path
draw_circle("D:/University/BSAI-4th semester/Programming for AI (Lab)/Assignments/Lab 5 task/Circle.png")