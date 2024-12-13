# PixelMorphCipher

## Overview
PixelMorphCipher is a Python-based tool for encrypting and decrypting images using pixel transformations. It generates a consistent random key matrix based on a seed for reversible encryption.

## Features
- **Image Encryption:** Transforms image pixel values for secure storage.
- **Image Decryption:** Reverses encryption to restore the original image.
- **Automatic Path Management:** Saves encrypted and decrypted images alongside the original file.
- **Custom Seed:** Ensures consistent encryption and decryption with a specified seed.

## Requirements
- Python 3.6 or later
- Libraries: `numpy`, `Pillow`

## Installation
Install the required libraries:
```bash
pip install numpy pillow
```

## Usage
1. Save the script as `PixelMorphCipher.py`.
2. Run the program:
   ```bash
   python PixelMorphCipher.py
   ```
3. Enter the path to an image when prompted.
4. The encrypted and decrypted images are saved in the same directory as the original image, with `_encrypted` and `_decrypted` appended to the file name.

## Note
Use this tool for educational or authorised purposes only. Ensure proper handling of encrypted and original images.
