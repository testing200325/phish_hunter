import sys
from libs.predictor import Predictor
from libs.features import FeatureExtraction
import json
import argparse

parser = argparse.ArgumentParser(
                    prog='analyze_url',
                    description='Analyze a URL for debugging the Phish Hunter ML AI')

parser.add_argument('-u', '--url')      # option that takes a value

args = parser.parse_args()

if args.url is None:
    parser.print_help()
    sys.exit(1)

p = Predictor()

links = [
         args.url
         ]

count = 1
for link in links:
    print(f"Length of URL: {len(link)} : {link}")
    fe = FeatureExtraction(link)
    print(json.dumps(fe.getFeaturesDict(), indent=4))

