import textract
import os
import argparse

def convert_to_txt(file_path, output_path):
    # extract text from the file
    text = textract.process(file_path)

    # Create a text file and write the extracted content to it
    with open(os.path.join(output_path, 'output.txt'), 'wb') as output_file:
        output_file.write(text)

def main():
    parser = argparse.ArgumentParser(description='Process some files.')
    parser.add_argument('--input', type=str, help='Input file path')
    parser.add_argument('--output', type=str, help='Output directory path')

    args = parser.parse_args()

    convert_to_txt(args.input, args.output)

if __name__ == "__main__":
    main()