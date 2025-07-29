# app/services/image_compression.py
import io
from PIL import Image

def compress_image(image_bytes: bytes, max_size_bytes: int = 1000000) -> io.BytesIO:
    """
    Compresses an image from bytes, reducing its quality until its size is below
    a specified maximum size (default 1MB) or a minimum quality is reached.

    Args:
        image_bytes (bytes): The raw bytes content of the image.
        max_size_bytes (int): The maximum target size for the compressed image in bytes.
                              Defaults to 1,000,000 bytes (1MB).

    Returns:
        io.BytesIO: An in-memory binary stream containing the compressed image in PNG format.
                    The stream's position is reset to the beginning for easy reading.
    Raises:
        ValueError: If the input bytes cannot be opened as an image.
        Exception: For other unexpected image processing errors.
    """
    try:
        # Read the image into an in-memory BytesIO object
        img_buffer = io.BytesIO(image_bytes)
        img = Image.open(img_buffer)

        # Ensure the image is in a format that can be saved as PNG (e.g., convert from JPEG)
        # PNG supports transparency (RGBA) which is often desired.
        if img.mode != 'RGBA' and img.mode != 'RGB':
            img = img.convert('RGBA')

        output_buffer = io.BytesIO()
        quality = 90  # Starting quality, can be adjusted
        min_quality = 10 # Minimum acceptable quality

        # Loop to compress until size is below max_size_bytes or quality is too low
        while True:
            output_buffer.seek(0)    # Reset buffer position for writing
            output_buffer.truncate(0) # Clear buffer content

            # Save with current quality. 'optimize=True' is good for PNG.
            # Using PNG format as per your original Node.js code's output.
            img.save(output_buffer, format='PNG', optimize=True, quality=quality)
            
            # Get the size of the compressed image
            compressed_size = len(output_buffer.getvalue())

            # If size is within limit or quality is at its minimum, break the loop
            if compressed_size <= max_size_bytes or quality <= min_quality:
                break
            
            # Reduce quality for the next iteration
            quality -= 10
            # Ensure quality does not fall below the minimum
            if quality < min_quality:
                quality = min_quality

        # Reset buffer position to the beginning before returning
        output_buffer.seek(0)
        return output_buffer

    except Image.UnidentifiedImageError:
        raise ValueError("Invalid image file: The provided bytes do not represent a recognizable image.")
    except Exception as e:
        # Catch any other potential errors during image processing
        raise Exception(f"Failed to compress image: {e}")
