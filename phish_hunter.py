#!venv/bin/python
# -*- coding: utf-8 -*-
import sys
from libs.predictor import Predictor
from libs.features import FeatureExtraction
import argparse
from time import sleep

p = Predictor()

links = [
    'https://www.google.com',
    'https://www.youtube.com',
    'https://www.twitter.com',
    'https://www.pkobp.pl/',
    'https://www.dskdirect.bg/page/default.aspx?xml_id=/bg-BG/.login',
    'https://mobilephotokiosk.app:443/view/1337',
    'https://podrozklienta.online/#/app/accept-invitation/emilia.sliwoska@pkobp.pl/1733303090/3xQuib5rvnf_IgW6EvXmVEjNKO4GgvOKapilH9bwAOw~7hCMWXlKgRrv6QPjpqmsyz5P_4RWBKN1mJgtPJiUNRA~',
    'https://wordpress.com/support/domains/',
    'https://lbpiaccess.com',
    'https://104.208.244.222/',
    'https://eniplenitude.com/my-eni',
    'https://ebio.gg/@meandyouxq',
    'https://explorer.walletconnect.com/',
    'https://www.autenticacao.gov.pt/',
    'https://ebanking.itauprivatebank.com/',
    'https://cloudflare-ipfs.org',
    'https://www.economist.com/',
    'https://www.nabtrade.com.au/',
    'https://paypay.ne.jp:443/',
    'https://www.truist.com/fraud-and-security',
    'https://releases.jquery.com/',
    'http://0000000000000000000000000.findyourjacket.com',
    'http://00000000000000000000000.fielty.mx',
    'http://00000000000000000update.emy.ba',
    'http://0000000000c0.x9xcax2a.workers.dev',
    'http://00000000883838383992929292222.ratingandreviews.in',
    'http://00000002.c1.biz',
    'http://0.00000.life/paypal/login.html',
    'http://0000-1t8.pages.dev',
    'http://0.0.0.0forum.cryptonight.net',
    'http://0.0.0.0mailgate.cryptonight.net',
    'http://0.0.0.0ns10.cryptonight.net',
    'http://0.0.0.0ssl.cryptonight.net',
    'http://0001.353527440.workers.dev',
    'http://0001home.webflow.io',
    'http://0007854.atwebpages.com/desk/index.html',
    'http://000811893962007154932393170597959432.hanefra7bikiemta.com',
    'http://0.0.0assets.cryptonight.net',
    'http://000chgojhd78jhvbwreuvk.webnode.com',
    'http://0.0.0dbs.cryptonight.net',
    'http://000f9e-48.myshopify.com/bigi2001',
    'http://000ficohs99onli22.125mb.com',
    'http://0.0.0fileserver.cryptonight.net'

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
            fe.append_dataset(filename=args.append_dataset,
                              new_row=feature_array)

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
                fe.append_dataset(filename=args.append_dataset,
                                  new_row=feature_array)

            count += 1
            sleep(.5)

    else:
        parser.print_help()
        sys.exit(0)
