from libs.predictor import Predictor
from libs.features import FeatureExtraction
from time import sleep

p = Predictor()

links = [
         'https://mondialrelaylivraison.net/', # valid
         'https://verif0785portal.info/purduefeds', # valid
         'https://www.irs.gov.tax-sioe.com/', # valid
         'https://rebrand.ly/gpdpcxz', # valid
         'https://gt.membersitogo.4pu.com/plan', # valid
         'http://allegrolokalnie.pl-4637347.icu', # valid
         #'https://mintrabajo.gob.gt@tinyurl.com/', # valid, fails due to socket issues
         'https://serve.tigo-gt.top/gt?hWK=RyR4orilLs', # valid
         'http://allegrolokalnie.pl-oferta9431404.cfd', # valid
         'http://d0pd.841518.cfd/', # valid
         'https://welcome-doc-exodus.github.io/en-us/', # valid
         'https://s-push-erneuerung.com/', # valid
         'https://bigalmechanical.com/-/dbag/', # valid
         'https://package-expressdh.com/captcha/captcha.php', #valid
         'https://docs.google.com/presentation/d/e/2PACX-1vTr4Eb70TIUMSkdwL9Q2twDWru9LVq6C_4dj2g_xQ_12QoHrbeH-p9Fw9eJ2vGUFKiP64-eTSb1r1hS/pub?start=false&loop=false&delayms=3000', # valid
         'https://f6d19e18.outh-sam20.pages.dev/', # valid
         'https://e025441b.currentllyy.pages.dev/', # valid
         'https://metanetfixx.pages.dev/connect', # valid
         'https://package-expressdh.com/captcha/captcha.php', # valid
         'http://vz2wssfi.r.us-east-1.awstrack.me/L0/9uy8t76dytxcvyubhijpohikgnytrgwsdtyuigohojigu.pages.dev%2F%3FD5kcy5grsNUHE0gZ4sKOUP4jkHyJXMDitQmieP5mgGRvzlGSgmUwAl/1/01000194dd66b512-c7ca596e-9acd-4604-8b07-178de31095b1-000000/CuLVPdOnU5xiffpFq3V-MyrkJAc=412', # valid
         'http://itauresgatedepontos.dynv6.net/', # valid
         'https://disponivelparavoce.dynv6.net/cliente/cadrastro.php?codigo=XIHl7gXN4LkHDgTmq2xJu6ZWU-pFJCfIKE0oMWT3YFdKF', # valid
         'https://duxyy3sx96.com/index/login/login/token/e116e1304ce834694c37f2c53778894d.html', # valid
         'https://z7r7433fo3.vip/index/login/login/token/e116e1304ce834694c37f2c53778894d.html', # valid
         'https://duxyy3sx96.vip/index/login/login/token/e116e1304ce834694c37f2c53778894d.html', # valid
         'https://rzs6ji6bq0.vip/index/login/login/token/e116e1304ce834694c37f2c53778894d.html', # valid
         'https://tldbrrqcmj.vip/index/login/login/token/e116e1304ce834694c37f2c53778894d.html', # valid
         'https://slgndocline.onlxtg.com/87300038978/', # valid
         'https://viaoceanica.com/jpd/index.htm', # valid
         'http://sjfqvcxbee.cfolks.pl/ab/ar', # valid
         'https://pay.shopeeprodutos.site/lDW0ZaKOBaQgN7E?utm_source=organic&utm_campaign=&utm_medium=&utm_content=&utm_term=&subid=&sid2=&subid2=&subid3=&subid4=&subid5=&xcod=&sck=', # valid
         'https://pay.pagmenos.site/YEwR3ADR7dogdKy?utm_source=organic&utm_campaign=rKm-km-rKm&utm_medium=&utm_content=&utm_term=&xcod=jLj67a1f0eef317b016cee2cca3hQwK21wXxRrKm-km-rKmhQwK21wXxRhQwK21wXxRhQwK21wXxR&sck=jLj67a1f0eef317b016cee2cca3hQwK21wXxRrKm-km-rKmhQwK21wXxRhQwK21wXxRhQwK21wXxR', # valid
         'https://f6d19e18.outh-sam20.pages.dev/?id=ev7BHk51p2', # valid
         ]

count = 1
for link in links:
    note = False

    fe = FeatureExtraction(link)

    prediction = p.make_prediction(data=fe.getFeaturesArray())

    if prediction is True:
        print(f"[*] {count} - {link} is PHISH: {prediction}")
    else:
        print(f"[-] {count} - {link} is PHISH: {prediction}")

    count += 1
    sleep(.5)
