
# Cookies and headers for scraping
 
COOKIES= {
    'bcookie': '"v=2&67d2c45c-eba4-4283-8f07-432653bc882d"',
    'li_sugr': '963f9f6d-8fd8-4525-9e1d-e3c19fd9de08',
    'bscookie': '"v=1&202407240924011b9e72e2-06d3-443c-839f-4dadd6c007e8AQGSJkk_T4KOUXknd4aD3KKNUNQWb0AH"',
    'li_rm': 'AQHJl2a77fCQMQAAAZFLo4PBWcUtDIxt_o2p2ppWLipyH-4ZOhDp6e_P88Lb3_pE9_eqIc0u8Df4a6k4vuCXo3C6DW_XgEl6FmZzZkMcosxxly5_pqp8qLAS',
    'li_theme': 'light',
    'li_theme_set': 'app',
    'dfpfpt': '89e2e6fe7b0e4fd58a501f7cbb624c94',
    'AMCV_14215E3D5995C57C0A495C55%40AdobeOrg': '-637568504%7CMCIDTS%7C19963%7CMCMID%7C63096030002651289443523443678346205394%7CMCAAMLH-1725344024%7C12%7CMCAAMB-1725344024%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1724746424s%7CNONE%7CvVersion%7C5.1.1%7CMCCIDH%7C-1652370584',
    'li_gc': 'MTswOzE3MjU2ODY5NTk7MjswMjECln3j/rWMxEnvcsGyIEJIH2soAeQ5c1L9lweWjxqHhg==',
    'timezone': 'Asia/Calcutta',
    'AnalyticsSyncHistory': 'AQK3OVWEGXvtTwAAAZSHRxrO8qvbd0cJ5A_yHZqd8Ro4h6EnYNB6usLKlITtOG8GGGqbKefojF4AUmou22f2Hg',
    'UserMatchHistory': 'AQIDHtaJErZCbgAAAZSR_rjhA5L5hc8MToy_Ko4aNEB59kHyOYOu5dlvRj6qj9k_HOwIJo3l3oG57w',
    'lms_ads': 'AQFxt1dfLU-gygAAAZSR_rn-qdJY6XX5LBoyezDUMbnpn-z-Sxi1uDpTShu3N4a0bBayjWBK9bfRdcrahvnDpbShZqDdd-Vk',
    'lms_analytics': 'AQFxt1dfLU-gygAAAZSR_rn-qdJY6XX5LBoyezDUMbnpn-z-Sxi1uDpTShu3N4a0bBayjWBK9bfRdcrahvnDpbShZqDdd-Vk',
    'visit': 'v=1&M',
    'lidc': '"b=VGST06:s=V:r=V:a=V:p=V:g=3168:u=1:x=1:i=1737616188:t=1737702588:v=2:sig=AQEqFuEkF7N2Hnq83CiKXAiLLthEwX1_"',
    'g_state': '{"i_p":1740035399473,"i_l":4}',
    'JSESSIONID': 'ajax:6512511520276752026',
    'lang': 'v=2&lang=en-us',
    'fid': 'AQFiaKZhkRXFIgAAAZSTx1iCRVde8CLJ1AIRA3RxLKFhObncK7wSC_HwwXb8sXCp3nI2FIpLC2Jxwg',
}


HEADERS= {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
}



TITEL_XPATH =  "//h1[contains(@class, 'top-card-layout__title')]//text()"
HEADING_XPATH ="//h2[contains(@class, 'top-card-layout__headline')]//text()"
ADDRESS_XPATH = "//div[contains(@class, 'profile-info-subheader')]//div[contains(@class,'not-first-middot')]//span//text()"
ABOUT_XPATH = "//section[contains(@data-section,'summary')]//text()"
COMPANY_NAME_XPATH = "//div[contains(@class,'top-card__links-container')]//div[contains(@data-section,'currentPositionsDetails')]//span[contains(@class,'top-card-link__description')]//text()"
EDUCATION_XPATH = "//div[contains(@class,'top-card__links-container')]//div[contains(@data-section,'educationsDetails')]//span[contains(@class,'top-card-link__description')]//text()"
EXPERIENCE_XPATH ="//div[contains(@class,'core-section-container__content')]//ul[contains(@class,'experience__list')]//li[contains(@class,'profile-section-card')]"
