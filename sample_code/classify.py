#!/usr/bin/env python3

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

import os
import cv2
import numpy
import string
import random
import argparse
import tflite as tfl
from tflite_runtime.interpreter import Interpreter



def decode(characters, y):
    # y = numpy.argmax(numpy.array(y), axis=2)[:,0]
    y = numpy.argmax(numpy.array(y), axis=1)
    return ''.join([characters[x] for x in y])

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model-name', help='Model name to use for classification', type=str)
    parser.add_argument('--captcha-dir', help='Where to read the captchas to break', type=str)
    parser.add_argument('--output', help='File where the classifications should be saved', type=str)
    parser.add_argument('--symbols', help='File with the symbols to use in captchas', type=str)
    args = parser.parse_args()

    if args.model_name is None:
        print("Please specify the CNN model to use")
        exit(1)

    if args.captcha_dir is None:
        print("Please specify the directory with captchas to break")
        exit(1)

    if args.output is None:
        print("Please specify the path to the output file")
        exit(1)

    if args.symbols is None:
        print("Please specify the captcha symbols file")
        exit(1)

    symbols_file = open(args.symbols, 'r')
    captcha_symbols = symbols_file.readline().strip()
    print(captcha_symbols)
    symbols_file.close()

    print("Classifying captchas with symbol set {" + captcha_symbols + "}")
    with open(args.output, 'w') as output_file:
        output_file.write("shelkem\n")
        interpreter = Interpreter('converted_model.tflite')
        interpreter.allocate_tensors()
        input = interpreter.get_input_details()
        print(input)
        output = interpreter.get_output_details()
        print(output)

        img_list = os.listdir(args.captcha_dir)
        img_list.sort()
        print(img_list)
        for x in img_list:
            # load image and preprocess it
            raw_data = cv2.imread(os.path.join(args.captcha_dir, x))
            rgb_data = cv2.cvtColor(raw_data, cv2.COLOR_BGR2RGB)
            image = numpy.array(rgb_data, dtype=numpy.float32) / 255.0
            (c, h, w) = image.shape
            image = image.reshape([-1, c, h, w])
            print(input[0]['index'])
            interpreter.set_tensor(input[0]['index'], image)
            interpreter.invoke()
            output_dt = interpreter.get_tensor(output[0]['index'])
            print("decoded")
            # print(decode(captcha_symbols,output_dt))
            decoded_captcha = ''.join(decode('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                             interpreter.get_tensor(x["index"])) for x in output)

            output_file.write(x + "," + decoded_captcha + "\n")

            print('Classified ' + x)
if __name__ == '__main__':
    main()
