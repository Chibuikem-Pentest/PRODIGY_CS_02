import os
import numpy as np
from PIL import Image
import random

class PixelMorphCipher:
    def __init__(self, seed: int):
        """Initialise the cipher with a random seed."""
        self.seed = seed

    def encrypt_image(self, input_path: str, output_path: str):
        """Encrypts an image by applying pixel transformations."""
        img = Image.open(input_path).convert('RGB')
        img_array = np.array(img)

        # Generate a random matrix for pixel modification
        key_matrix = self._generate_key(img_array.shape)

        # Add the key matrix and perform modulo operation for encryption
        encrypted_array = (img_array + key_matrix) % 256

        # Save the encrypted image
        encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
        encrypted_img.save(output_path)
        print("Image successfully encrypted and saved at:", output_path)

    def decrypt_image(self, encrypted_path: str, output_path: str):
        """Decrypts an image by reversing the pixel transformations."""
        img = Image.open(encrypted_path).convert('RGB')
        img_array = np.array(img)

        # Regenerate the key matrix
        key_matrix = self._generate_key(img_array.shape)

        # Subtract the key matrix and perform modulo operation for decryption
        decrypted_array = (img_array - key_matrix) % 256

        # Save the decrypted image
        decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
        decrypted_img.save(output_path)
        print("Image successfully decrypted and saved at:", output_path)

    def _generate_key(self, shape):
        """Generate a consistent random key matrix based on the seed."""
        rng = np.random.default_rng(self.seed)  # Use a seeded random generator
        return rng.integers(0, 256, size=shape, dtype=np.uint8)


# Implementation:
if __name__ == "__main__":
    cipher = PixelMorphCipher(seed=42)  # Use a consistent seed for encryption/decryption

    # Prompt the user for the input image path
    input_image_path = input("Enter the path to the input image: ").strip()

    # Automatically determine paths for encrypted and decrypted images
    input_dir, input_file = os.path.split(input_image_path)
    input_name, _ = os.path.splitext(input_file)

    encrypted_image_path = os.path.join(input_dir, f"{input_name}_encrypted.png")
    decrypted_image_path = os.path.join(input_dir, f"{input_name}_decrypted.png")

    # Encrypt and decrypt the image
    cipher.encrypt_image(input_image_path, encrypted_image_path)
    cipher.decrypt_image(encrypted_image_path, decrypted_image_path)
