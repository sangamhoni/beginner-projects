# Program to take screenshot
import pyscreenshot

print("Sangam")
# To capture the screen
image = pyscreenshot.grab()

# To display the captured screenshot
image.show()

# To save the screenshot
image.save("Screenshot.png")
