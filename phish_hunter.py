#!venv/bin/python
# -*- coding: utf-8 -*-
import sys
from libs.predictor import Predictor
from libs.features import FeatureExtraction
import argparse
from time import sleep

p = Predictor()

links = [
         'https://eocodaswallet.godaddysites.com/',
         'https://mondialrelay-transit-fr.com/pac/calcul.php'
         ]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='phish_hunter',
        description='Analyze a URL to determine if it may be a Phishing site')

    parser.add_argument('-u', '--url')
    parser.add_argument('-r', '--run_internal_links', action='store_true')
    parser.add_argument('-a', '--append_dataset')

    args = parser.parse_args()

    if args.url is None and args.run_internal_links is None:
        parser.print_help()
        sys.exit(1)

    if args.url and not args.run_internal_links:
        fe = FeatureExtraction(args.url)

        feature_array = fe.getFeaturesArray()

        prediction = p.make_prediction(data=feature_array)

        result = None

        if prediction is True:
            print(f"[*] {count} - {args.url} is PHISH: {prediction}")
            result = 1
        else:
            print(f"[-] {count} - {args.url} is PHISH: {prediction}")
            result = -1

        # If requested : add new data to the dataset for future training purposes
        if args.append_dataset:
            feature_array.append(result)
            fe.append_dataset(filename=args.append_dataset, new_row=feature_array)

    elif args.run_internal_links:
        # If no URL was passed and we got the run_internal_links switch
        # then process all the links in the array above
        count = 1
        for link in links:
            fe = FeatureExtraction(link)

            feature_array = fe.getFeaturesArray()

            prediction = p.make_prediction(data=feature_array)

            result = None

            if prediction is True:
                print(f"[*] {count} - {link} is PHISH: {prediction}")
                result = 1
            else:
                print(f"[-] {count} - {link} is PHISH: {prediction}")
                result = -1

            # If requested : add new data to the dataset for future training purposes
            if args.append_dataset:
                feature_array.append(result)
                fe.append_dataset(filename=args.append_dataset, new_row=feature_array)

            count += 1
            sleep(.5)

    else:
        parser.print_help()
        sys.exit(0)
