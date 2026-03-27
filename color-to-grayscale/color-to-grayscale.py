def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    # Write code here
    height = len(image)
    width = len(image[0])
    grayscale = []
    for i in range(height):
        row = []
        for j in range(width):
            r, g, b = image[i][j]
            gray = 0.299 * r + 0.587 * g + 0.114 * b
            row.append(gray)
        grayscale.append(row)
    return grayscale
             
                 
        
