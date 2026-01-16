# 🎨 Pallet-Extracter

A user-friendly graphical application that extracts dominant colors from images and displays them with their hex codes and usage proportions.

## 📋 Description

The Color Palette Extraction Tool is built with Python's Tkinter library and uses advanced color analysis algorithms. It allows users to select an image file, extract the top 10 dominant colors, and display them in an organized interface with hex codes and their proportions in the image.

Perfect for designers, developers, and anyone who needs to work with color palettes from existing images.

## 🚀 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AnandkumarMall/Pallet-Extracter.git
   cd Pallet-Extracter
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Usage

1. **Launch the application:**
   ```bash
   python main.py
   ```

2. **Extract colors:**
   - Click the "Open Image" button to select an image file
   - The tool will analyze and extract the top 10 dominant colors from your image
   - Colors, their hex codes, and proportions will be displayed in a table

3. **Copy color codes:**
   - Click on any color in the display to automatically copy its hex code to your clipboard
   - Paste the hex code wherever you need it (design tools, code editors, etc.)

## ✨ Features

- 🎯 **Extract Dominant Colors**: Automatically identify and extract the top 10 dominant colors from any image
- 🎨 **Visual Display**: See each color with a visual preview
- 📊 **Detailed Information**: View hex codes and color proportions at a glance
- 📋 **One-Click Copy**: Copy hex codes to clipboard with a single click
- 🖼️ **Multiple Formats**: Supports PNG, JPEG, and GIF image formats
- 💾 **Easy to Use**: Simple and intuitive graphical interface

## 🛠️ Technologies Used

- **Python** - Programming language
- **Tkinter** - GUI framework for the user interface
- **colorgram.py** - Color extraction algorithm
- **Pillow** - Image processing library
- **pyperclip** - Clipboard management

## 📦 Requirements

See `requirements.txt` for all dependencies:
- colorgram.py==1.2.0
- Pillow>=3.3.1
- pyperclip>=1.8.1


