
class Percent(object):
    def __init__(self, x, precision=1):
        self.x = x
        self.precision = precision

    def __str__(self):
        return ('{:.' + str(self.precision) + '%}').format(self.x)

    @property
    def verb(self):
        return 'increased' if self.x > 0 else 'decreased'

# from http://www.iso.org/iso/country_names_and_code_elements_txt
COUNTRIES = {
"AF": u"Afghanistan",
"AX": u"\xc5land Islands",
"AL": u"Albania",
"DZ": u"Algeria",
"AS": u"American Samoa",
"AD": u"Andorra",
"AO": u"Angola",
"AI": u"Anguilla",
"AQ": u"Antarctica",
"AG": u"Antigua And Barbuda",
"AR": u"Argentina",
"AM": u"Armenia",
"AW": u"Aruba",
"AU": u"Australia",
"AT": u"Austria",
"AZ": u"Azerbaijan",
"BS": u"Bahamas",
"BH": u"Bahrain",
"BD": u"Bangladesh",
"BB": u"Barbados",
"BY": u"Belarus",
"BE": u"Belgium",
"BZ": u"Belize",
"BJ": u"Benin",
"BM": u"Bermuda",
"BT": u"Bhutan",
"BO": u"Bolivia, Plurinational State Of",
"BQ": u"Bonaire, Sint Eustatius And Saba",
"BA": u"Bosnia And Herzegovina",
"BW": u"Botswana",
"BV": u"Bouvet Island",
"BR": u"Brazil",
"IO": u"British Indian Ocean Territory",
"BN": u"Brunei Darussalam",
"BG": u"Bulgaria",
"BF": u"Burkina Faso",
"BI": u"Burundi",
"KH": u"Cambodia",
"CM": u"Cameroon",
"CA": u"Canada",
"CV": u"Cape Verde",
"KY": u"Cayman Islands",
"CF": u"Central African Republic",
"TD": u"Chad",
"CL": u"Chile",
"CN": u"China",
"CX": u"Christmas Island",
"CC": u"Cocos (keeling) Islands",
"CO": u"Colombia",
"KM": u"Comoros",
"CG": u"Congo",
"CD": u"Congo, The Democratic Republic Of The",
"CK": u"Cook Islands",
"CR": u"Costa Rica",
"CI": u"C\xf4te D'ivoire",
"HR": u"Croatia",
"CU": u"Cuba",
"CW": u"Cura\xe7ao",
"CY": u"Cyprus",
"CZ": u"Czech Republic",
"DK": u"Denmark",
"DJ": u"Djibouti",
"DM": u"Dominica",
"DO": u"Dominican Republic",
"EC": u"Ecuador",
"EG": u"Egypt",
"SV": u"El Salvador",
"GQ": u"Equatorial Guinea",
"ER": u"Eritrea",
"EE": u"Estonia",
"ET": u"Ethiopia",
"FK": u"Falkland Islands (malvinas)",
"FO": u"Faroe Islands",
"FJ": u"Fiji",
"FI": u"Finland",
"FR": u"France",
"GF": u"French Guiana",
"PF": u"French Polynesia",
"TF": u"French Southern Territories",
"GA": u"Gabon",
"GM": u"Gambia",
"GE": u"Georgia",
"DE": u"Germany",
"GH": u"Ghana",
"GI": u"Gibraltar",
"GR": u"Greece",
"GL": u"Greenland",
"GD": u"Grenada",
"GP": u"Guadeloupe",
"GU": u"Guam",
"GT": u"Guatemala",
"GG": u"Guernsey",
"GN": u"Guinea",
"GW": u"Guinea-bissau",
"GY": u"Guyana",
"HT": u"Haiti",
"HM": u"Heard Island And Mcdonald Islands",
"VA": u"Holy See (vatican City State)",
"HN": u"Honduras",
"HK": u"Hong Kong",
"HU": u"Hungary",
"IS": u"Iceland",
"IN": u"India",
"ID": u"Indonesia",
"IR": u"Iran, Islamic Republic Of",
"IQ": u"Iraq",
"IE": u"Ireland",
"IM": u"Isle Of Man",
"IL": u"Israel",
"IT": u"Italy",
"JM": u"Jamaica",
"JP": u"Japan",
"JE": u"Jersey",
"JO": u"Jordan",
"KZ": u"Kazakhstan",
"KE": u"Kenya",
"KI": u"Kiribati",
"KP": u"Korea, Democratic People's Republic Of",
"KR": u"Korea, Republic Of",
"KW": u"Kuwait",
"KG": u"Kyrgyzstan",
"LA": u"Lao People's Democratic Republic",
"LV": u"Latvia",
"LB": u"Lebanon",
"LS": u"Lesotho",
"LR": u"Liberia",
"LY": u"Libya",
"LI": u"Liechtenstein",
"LT": u"Lithuania",
"LU": u"Luxembourg",
"MO": u"Macao",
"MK": u"Macedonia, The Former Yugoslav Republic Of",
"MG": u"Madagascar",
"MW": u"Malawi",
"MY": u"Malaysia",
"MV": u"Maldives",
"ML": u"Mali",
"MT": u"Malta",
"MH": u"Marshall Islands",
"MQ": u"Martinique",
"MR": u"Mauritania",
"MU": u"Mauritius",
"YT": u"Mayotte",
"MX": u"Mexico",
"FM": u"Micronesia, Federated States Of",
"MD": u"Moldova, Republic Of",
"MC": u"Monaco",
"MN": u"Mongolia",
"ME": u"Montenegro",
"MS": u"Montserrat",
"MA": u"Morocco",
"MZ": u"Mozambique",
"MM": u"Myanmar",
"NA": u"Namibia",
"NR": u"Nauru",
"NP": u"Nepal",
"NL": u"Netherlands",
"NC": u"New Caledonia",
"NZ": u"New Zealand",
"NI": u"Nicaragua",
"NE": u"Niger",
"NG": u"Nigeria",
"NU": u"Niue",
"NF": u"Norfolk Island",
"MP": u"Northern Mariana Islands",
"NO": u"Norway",
"OM": u"Oman",
"PK": u"Pakistan",
"PW": u"Palau",
"PS": u"Palestinian Territory, Occupied",
"PA": u"Panama",
"PG": u"Papua New Guinea",
"PY": u"Paraguay",
"PE": u"Peru",
"PH": u"Philippines",
"PN": u"Pitcairn",
"PL": u"Poland",
"PT": u"Portugal",
"PR": u"Puerto Rico",
"QA": u"Qatar",
"RE": u"R\xe9union",
"RO": u"Romania",
"RU": u"Russian Federation",
"RW": u"Rwanda",
"BL": u"Saint Barth\xe9lemy",
"SH": u"Saint Helena, Ascension And Tristan Da Cunha",
"KN": u"Saint Kitts And Nevis",
"LC": u"Saint Lucia",
"MF": u"Saint Martin (french Part)",
"PM": u"Saint Pierre And Miquelon",
"VC": u"Saint Vincent And The Grenadines",
"WS": u"Samoa",
"SM": u"San Marino",
"ST": u"Sao Tome And Principe",
"SA": u"Saudi Arabia",
"SN": u"Senegal",
"RS": u"Serbia",
"SC": u"Seychelles",
"SL": u"Sierra Leone",
"SG": u"Singapore",
"SX": u"Sint Maarten (dutch Part)",
"SK": u"Slovakia",
"SI": u"Slovenia",
"SB": u"Solomon Islands",
"SO": u"Somalia",
"ZA": u"South Africa",
"GS": u"South Georgia And The South Sandwich Islands",
"SS": u"South Sudan",
"ES": u"Spain",
"LK": u"Sri Lanka",
"SD": u"Sudan",
"SR": u"Suriname",
"SJ": u"Svalbard And Jan Mayen",
"SZ": u"Swaziland",
"SE": u"Sweden",
"CH": u"Switzerland",
"SY": u"Syrian Arab Republic",
"TW": u"Taiwan, Province Of China",
"TJ": u"Tajikistan",
"TZ": u"Tanzania, United Republic Of",
"TH": u"Thailand",
"TL": u"Timor-leste",
"TG": u"Togo",
"TK": u"Tokelau",
"TO": u"Tonga",
"TT": u"Trinidad And Tobago",
"TN": u"Tunisia",
"TR": u"Turkey",
"TM": u"Turkmenistan",
"TC": u"Turks And Caicos Islands",
"TV": u"Tuvalu",
"UG": u"Uganda",
"UA": u"Ukraine",
"AE": u"United Arab Emirates",
"GB": u"United Kingdom",
"US": u"United States",
"UM": u"United States Minor Outlying Islands",
"UY": u"Uruguay",
"UZ": u"Uzbekistan",
"VU": u"Vanuatu",
"VE": u"Venezuela, Bolivarian Republic Of",
"VN": u"Viet Nam",
"VG": u"Virgin Islands, British",
"VI": u"Virgin Islands, U.s.",
"WF": u"Wallis And Futuna",
"EH": u"Western Sahara",
"YE": u"Yemen",
"ZM": u"Zambia",
"ZW": u"Zimbabwe"
}

def country_name(code):
    return COUNTRIES.get(code, code)
