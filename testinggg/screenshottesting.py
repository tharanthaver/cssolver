from PIL import Image, ImageDraw, ImageFont
import io

def create_triangle_screenshot(rows):
    """
    Generates a right-angled triangle pattern using '*' and saves it to a PNG screenshot.
    """
    try:
        rows = int(rows)
        if rows <= 0:
            raise ValueError("Number of rows must be a positive integer.")

        pattern = ""
        for i in range(1, rows + 1):
            pattern += "*" * i + "\n"

        output_text = f"Right-angled triangle ({rows} rows):\n{pattern}"

        font = ImageFont.load_default()
        lines = output_text.splitlines()
        font_size = 24
        width = 400  # Adjust as needed
        height = len(lines) * font_size + 20

        image = Image.new('RGB', (width, height), color='white')
        draw = ImageDraw.Draw(image)
        y_offset = 10
        for line in lines:
            draw.text((10, y_offset), line, fill='black', font=font)
            y_offset += font_size

        screenshot_path = "triangle_screenshot.png"
        image.save(screenshot_path)
        print(f"Screenshot saved to: {screenshot_path}")

    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Get input
rows_str = input("Enter the number of rows for the triangle: ")
create_triangle_screenshot(rows_str)

