from datetime import datetime, timedelta
from interview.inventory.models import Inventory, InventoryLanguage, InventoryTag, InventoryType
from interview.order.models import Order, OrderTag


iso_langs = {
    "ab":{
        "name":"Abkhaz",
    },
    "aa":{
        "name":"Afar",
    },
    "af":{
        "name":"Afrikaans",
    },
    "ak":{
        "name":"Akan",
    },
    "sq":{
        "name":"Albanian",
    },
    "am":{
        "name":"Amharic",
    },
    "ar":{
        "name":"Arabic",
    },
    "an":{
        "name":"Aragonese",
    },
    "hy":{
        "name":"Armenian",
    },
    "as":{
        "name":"Assamese",
    },
    "av":{
        "name":"Avaric",
    },
    "ae":{
        "name":"Avestan",
    },
    "ay":{
        "name":"Aymara",
    },
    "az":{
        "name":"Azerbaijani",
    },
    "bm":{
        "name":"Bambara",
    },
    "ba":{
        "name":"Bashkir",
    },
    "eu":{
        "name":"Basque",
    },
    "be":{
        "name":"Belarusian",
    },
    "bn":{
        "name":"Bengali",
    },
    "bh":{
        "name":"Bihari",
    },
    "bi":{
        "name":"Bislama",
    },
    "bs":{
        "name":"Bosnian",
    },
    "br":{
        "name":"Breton",
    },
    "bg":{
        "name":"Bulgarian",
    },
    "my":{
        "name":"Burmese",
    },
    "ch":{
        "name":"Chamorro",
    },
    "ce":{
        "name":"Chechen",
    },
    "zh":{
        "name":"Chinese",
    },
    "cv":{
        "name":"Chuvash",
    },
    "kw":{
        "name":"Cornish",
    },
    "co":{
        "name":"Corsican",
    },
    "cr":{
        "name":"Cree",
    },
    "hr":{
        "name":"Croatian",
    },
    "cs":{
        "name":"Czech",
    },
    "da":{
        "name":"Danish",
    },
    "nl":{
        "name":"Dutch",
    },
    "en":{
        "name":"English",
    },
    "eo":{
        "name":"Esperanto",
    },
    "et":{
        "name":"Estonian",
    },
    "ee":{
        "name":"Ewe",
    },
    "fo":{
        "name":"Faroese",
    },
    "fj":{
        "name":"Fijian",
    },
    "fi":{
        "name":"Finnish",
    },
    "fr":{
        "name":"French",
    },
    "gl":{
        "name":"Galician",
    },
    "ka":{
        "name":"Georgian",
    },
    "de":{
        "name":"German",
    },
    "gn":{
        "name":"Guaraní",
    },
    "gu":{
        "name":"Gujarati",
    },
    "ha":{
        "name":"Hausa",
    },
    "he":{
        "name":"Hebrew",
    },
    "hz":{
        "name":"Herero",
    },
    "hi":{
        "name":"Hindi",
    },
    "ho":{
        "name":"Hiri Motu",
    },
    "hu":{
        "name":"Hungarian",
    },
    "ia":{
        "name":"Interlingua",
    },
    "id":{
        "name":"Indonesian",
    },
    "ie":{
        "name":"Interlingue",
    },
    "ga":{
        "name":"Irish",
    },
    "ig":{
        "name":"Igbo",
    },
    "ik":{
        "name":"Inupiaq",
    },
    "io":{
        "name":"Ido",
    },
    "is":{
        "name":"Icelandic",
    },
    "it":{
        "name":"Italian",
    },
    "iu":{
        "name":"Inuktitut",
    },
    "ja":{
        "name":"Japanese",
    },
    "jv":{
        "name":"Javanese",
    },
    "kn":{
        "name":"Kannada",
    },
    "kr":{
        "name":"Kanuri",
    },
    "ks":{
        "name":"Kashmiri",
    },
    "kk":{
        "name":"Kazakh",
    },
    "km":{
        "name":"Khmer",
    },
    "rw":{
        "name":"Kinyarwanda",
    },
    "kv":{
        "name":"Komi",
    },
    "kg":{
        "name":"Kongo",
    },
    "ko":{
        "name":"Korean",
    },
    "ku":{
        "name":"Kurdish",
    },
    "la":{
        "name":"Latin",
    },
    "lg":{
        "name":"Luganda",
    },
    "ln":{
        "name":"Lingala",
    },
    "lo":{
        "name":"Lao",
    },
    "lt":{
        "name":"Lithuanian",
    },
    "lu":{
        "name":"Luba-Katanga",
    },
    "lv":{
        "name":"Latvian",
    },
    "gv":{
        "name":"Manx",
    },
    "mk":{
        "name":"Macedonian",
    },
    "mg":{
        "name":"Malagasy",
    },
    "ms":{
        "name":"Malay",
    },
    "ml":{
        "name":"Malayalam",
    },
    "mt":{
        "name":"Maltese",
    },
    "mh":{
        "name":"Marshallese",
    },
    "mn":{
        "name":"Mongolian",
    },
    "na":{
        "name":"Nauru",
    },
    "nd":{
        "name":"North Ndebele",
    },
    "ne":{
        "name":"Nepali",
    },
    "ng":{
        "name":"Ndonga",
    },
    "nn":{
        "name":"Norwegian Nynorsk",
    },
    "no":{
        "name":"Norwegian",
    },
    "ii":{
        "name":"Nuosu",
    },
    "nr":{
        "name":"South Ndebele",
    },
    "oc":{
        "name":"Occitan",
    },
    "om":{
        "name":"Oromo",
    },
    "or":{
        "name":"Oriya",
    },
    "fa":{
        "name":"Persian",
    },
    "pl":{
        "name":"Polish",
    },
    "pt":{
        "name":"Portuguese",
    },
    "qu":{
        "name":"Quechua",
    },
    "rm":{
        "name":"Romansh",
    },
    "rn":{
        "name":"Kirundi",
    },
    "ru":{
        "name":"Russian",
    },
    "sc":{
        "name":"Sardinian",
    },
    "sd":{
        "name":"Sindhi",
    },
    "se":{
        "name":"Northern Sami",
    },
    "sm":{
        "name":"Samoan",
    },
    "sg":{
        "name":"Sango",
    },
    "sr":{
        "name":"Serbian",
    },
    "sn":{
        "name":"Shona",
    },
    "sk":{
        "name":"Slovak",
    },
    "sl":{
        "name":"Slovene",
    },
    "so":{
        "name":"Somali",
    },
    "st":{
        "name":"Southern Sotho",
    },
    "su":{
        "name":"Sundanese",
    },
    "sw":{
        "name":"Swahili",
    },
    "ss":{
        "name":"Swati",
    },
    "sv":{
        "name":"Swedish",
    },
    "ta":{
        "name":"Tamil",
    },
    "te":{
        "name":"Telugu",
    },
    "tg":{
        "name":"Tajik",
    },
    "th":{
        "name":"Thai",
    },
    "ti":{
        "name":"Tigrinya",
    },
    "tk":{
        "name":"Turkmen",
    },
    "tl":{
        "name":"Tagalog",
    },
    "tn":{
        "name":"Tswana",
    },
    "tr":{
        "name":"Turkish",
    },
    "ts":{
        "name":"Tsonga",
    },
    "tt":{
        "name":"Tatar",
    },
    "tw":{
        "name":"Twi",
    },
    "ty":{
        "name":"Tahitian",
    },
    "uk":{
        "name":"Ukrainian",
    },
    "ur":{
        "name":"Urdu",
    },
    "uz":{
        "name":"Uzbek",
    },
    "ve":{
        "name":"Venda",
    },
    "vi":{
        "name":"Vietnamese",
    },
    "wa":{
        "name":"Walloon",
    },
    "cy":{
        "name":"Welsh",
    },
    "wo":{
        "name":"Wolof",
    },
    "fy":{
        "name":"Western Frisian",
    },
    "xh":{
        "name":"Xhosa",
    },
    "yi":{
        "name":"Yiddish",
    },
    "yo":{
        "name":"Yoruba",
    },
}

for key, lang in iso_langs.items():
    InventoryLanguage.objects.create(name=lang['name'])
    
inventory_tags = [
    dict(
        name='Action',
    ),
    dict(
        name='Adventure',
    ),
    dict(
        name='Comedy',  
    ),
    dict(
        name='Drama',
    ),
    dict(
        name='Romance',
    ),
    dict(
        name='Sci-Fi',  
    ),
    dict(
        name='Thriller',
    ),
    dict(
        name='Crime',
    )
]

inventory_tag_dict = {}
for tag in inventory_tags:
    name = tag['name']
    inventory_tag_dict[name] = InventoryTag.objects.create(**tag)
    
    
inventory_types = ['Movie', 'Episode', 'Version']
inventory_type_objects = {}
for i, inv_type in enumerate(inventory_types):
    inventory_type_objects[inv_type] = InventoryType.objects.create(name=inv_type)
    
inventory_items = [
    [
        dict(
            name='The Matrix',
            language_id=1,
            type=inventory_type_objects['Version'],
            metadata=dict(
                year=1999,
                actors=['Keanu Reeves', 'Laurence Fishburne', 'Carrie-Anne Moss'],
                imdb_rating=8.7,
                rotten_tomatoes_rating=87,
            ),
        ),
        [inventory_tag_dict['Action']]
    ],
    [
        dict(
            name='The Matrix Reloaded',
            language_id=10,
            type=inventory_type_objects['Version'],
            metadata=dict(
                year=2003,
                actors=['Keanu Reeves', 'Laurence Fishburne', 'Carrie-Anne Moss'],
                imdb_rating=7.2,
                rotten_tomatoes_rating=73,
            )
        ),
        [inventory_tag_dict['Action']]
    ],
    [
        dict(
            name='The Matrix Revolutions',
            language_id=10,
            type=inventory_type_objects['Version'],
            metadata=dict(
                year=2003,
                actors=['Keanu Reeves', 'Laurence Fishburne', 'Carrie-Anne Moss'],
                imdb_rating=6.7,
                rotten_tomatoes_rating=59,
            )
        ),
        [inventory_tag_dict['Action']]
    ],
    [
        dict(
            name='Reqiuem for a Dream',
            language_id=12,
            type=inventory_type_objects['Version'],
            metadata=dict(
                year=2000,
                actors=['Ellen Burstyn', 'Jared Leto', 'Jennifer Connelly'],
                imdb_rating=8.3,
                rotten_tomatoes_rating=89,
            )
        ),
        [inventory_tag_dict['Drama']]
    ],
    [
        dict(
            name='The Lord of the Rings: The Fellowship of the Ring',
            language_id=37,
            type=inventory_type_objects['Movie'],
            metadata=dict(
                year=2001,
                actors=['Elijah Wood', 'Ian McKellen', 'Viggo Mortensen'],
                imdb_rating=8.8,
                rotten_toamtoes_rating=91,
            )
        ),
        [inventory_tag_dict['Adventure']]
    ],
    [
        dict(
            name='The Lord of the Rings: The Two Towers',
            language_id=37,
            type=inventory_type_objects['Movie'],
            metadata=dict(
                year=2002,
                actors=['Elijah Wood', 'Ian McKellen', 'Viggo Mortensen'],
                imdb_rating=8.7,
                rotten_tomatoes_rating=87,
            )
        ),
        [inventory_tag_dict['Adventure']]
    ],
    [
        dict(
            name='The Lord of the Rings: The Return of the King',
            language_id=37,
            type=inventory_type_objects['Movie'],
            metadata=dict(
                year=2003,
                actors=['Elijah Wood', 'Ian McKellen', 'Viggo Mortensen'],
                imdb_rating=8.9,
                rotten_tomatoes_rating=95,
            )
        ),
        [inventory_tag_dict['Adventure']]
    ],
    [
        dict(
            name='Titanic',
            language_id=37,
            type=inventory_type_objects['Movie'],
            metadata=dict(
                year=1997,
                actors=['Leonardo DiCaprio', 'Kate Winslet', 'Billy Zane'],
                imdb_rating=7.8,
                rotten_tomatoes_rating=89,
            )
        ),
        [inventory_tag_dict['Romance']]
    ],
    [
        dict(
            name='Crash',
            language_id=48,
            type=inventory_type_objects['Version'],
            metadata=dict(
                year=2004,
                actors=['Don Cheadle', 'Sandra Bullock', 'Matt Dillon'],
                imdb_rating=7.8,
                rotten_tomatoes_rating=89,
            )
        ),
        [inventory_tag_dict['Drama']]
    ],
    [
        dict(
            name='Seinfeld Season 1 Episode 1',
            language_id=37,
            type=inventory_type_objects['Episode'],
            metadata=dict(
                year=1990,
                actors=['Jerry Seinfeld', 'Julia Louis-Dreyfus', 'Michael Richards'],
                imdb_rating=8.8,
                rotten_tomatoes_rating=91,
            )
        ),
        [inventory_tag_dict['Comedy']]
    ],
    [
        dict(
            name='Seinfeld Season 1 Episode 2',
            language_id=37,
            type=inventory_type_objects['Episode'],
            metadata=dict(
                year=1990,
                actors=['Jerry Seinfeld', 'Julia Louis-Dreyfus', 'Michael Richards'],
                imdb_rating=8.8,
                rotten_tomatoes_rating=91,
            )
        ),
        [inventory_tag_dict['Comedy']]
    ],
    [
        dict(
            name='Seinfeld Season 1 Episode 3',
            language_id=37,
            type=inventory_type_objects['Episode'],
            metadata=dict(
                year=1990,
                actors=['Jerry Seinfeld', 'Julia Louis-Dreyfus', 'Michael Richards'],
                imdb_rating=8.8,
                rotten_tomatoes_rating=91,
            )
        ),
        [inventory_tag_dict['Comedy']]
    ],
    [
        dict(
            name='Seinfeld Season 1 Episode 4',
            language_id=37,
            type=inventory_type_objects['Episode'],
            metadata=dict(
                year=1990,
                actors=['Jerry Seinfeld', 'Julia Louis-Dreyfus', 'Michael Richards'],
                imdb_rating=8.8,
                rotten_tomatoes_rating=91,
            )
        ),
        [inventory_tag_dict['Comedy']]
    ],
    [  
        dict(
            name='Seinfeld Season 1 Episode 5',
            language_id=37,
            type=inventory_type_objects['Episode'],
            metadata=dict(
                year=1990,
                actors=['Jerry Seinfeld', 'Julia Louis-Dreyfus', 'Michael Richards'],
                imdb_rating=8.8,
                rotten_tomatoes_rating=91,
            )
        ),
        [inventory_tag_dict['Comedy']]
    ],
    [
        dict(
            name='Seinfeld Season 1 Episode 6',
            language_id=37,
            type=inventory_type_objects['Episode'],
            metadata=dict(
                year=1990,
                actors=['Jerry Seinfeld', 'Julia Louis-Dreyfus', 'Michael Richards'],
                imdb_rating=8.8,
                rotten_tomatoes_rating=91,
            )
        ),
        [inventory_tag_dict['Comedy']]
    ],
    [
        dict(
            name='Seinfeld Season 1 Episode 7',
            language_id=37,
            type=inventory_type_objects['Episode'],
            metadata=dict(
                year=1990,
                actors=['Jerry Seinfeld', 'Julia Louis-Dreyfus', 'Michael Richards'],
                imdb_rating=8.8,
                rotten_tomatoes_rating=91,
            )
        ),
        [inventory_tag_dict['Comedy']]
    ],
    [
        dict(
            name='Seinfeld Season 1 Episode 8',
            language_id=37,
            type=inventory_type_objects['Episode'],
            metadata=dict(
                year=1990,
                actors=['Jerry Seinfeld', 'Julia Louis-Dreyfus', 'Michael Richards'],
                imdb_rating=8.8,
                rotten_tomatoes_rating=91,
            )
        ),
        [inventory_tag_dict['Comedy']]
    ]
]

for item in inventory_items:
    inventory_item, tags = item
    Inventory.objects.create(**inventory_item).tags.add(*tags)

order_tags = [
    dict(
        name='San Antonio'
    ),
    dict(
        name='Austin'
    ),
    dict(
        name='Dallas'   
    ),
    dict(
        name='Houston'
    ),
    dict(
        name='El Paso'
    ),
    dict(
        name='Boston'
    ),
    dict(
        name='New York'
    ),
    dict(
        name='Chicago'
    ),
    dict(
        name='Los Angeles'
    ),
    dict(
        name='San Francisco'
    ),
    dict(
        name='Pending'
    ),
    dict(
        name='Delivered'
    ),
    dict(
        name='Cancelled'
    ),
    dict(
        name='On-hold'
    ),
    dict(
        name='Processing'
    ),
    dict(
        name='QC'
    ),
    dict(
        name='Dubbing'
    ),
    dict(
        name='Subbing'
    ),
    dict(
        name='Closed Captioning'
    ),
    dict(
        name='Transcription'
    ),
    dict(
        name='Transcoding'
    )
]
order_tag_dict = {}
for tag in order_tags:
    order_tag_dict[tag['name']] = OrderTag.objects.create(**tag)
    
orders = [
    [
        dict(
            inventory=Inventory.objects.get(name='The Lord of the Rings: The Fellowship of the Ring'),
            start_date=datetime.now(),
            embargo_date=datetime.now() + timedelta(days=30),
        ),
        [order_tag_dict['San Antonio'], order_tag_dict['Pending'], order_tag_dict['Dubbing']]
    ],
    [
        dict(
            inventory=Inventory.objects.get(name='The Lord of the Rings: The Two Towers'),
            start_date=datetime.now(),
            embargo_date=datetime.now() - timedelta(days=30),
        ),
        [order_tag_dict['Chicago'], order_tag_dict['Delivered'], order_tag_dict['Dubbing']]
    ],
    [
        dict(
            inventory=Inventory.objects.get(name='The Lord of the Rings: The Return of the King'),
            start_date=datetime.now() + timedelta(days=5),
            embargo_date=datetime.now() + timedelta(days=30),
        ),
        [order_tag_dict['Boston'], order_tag_dict['QC'], order_tag_dict['Subbing'], order_tag_dict['Transcription']]
    ],
    [
        dict(
            inventory=Inventory.objects.get(name='Crash'),
            start_date=datetime.now() + timedelta(days=15),
            embargo_date=datetime.now() + timedelta(days=30),
        ),
        [order_tag_dict['New York'], order_tag_dict['Processing'], order_tag_dict['Dubbing'], order_tag_dict['Transcoding']]
    ],
    [
        dict(
            inventory=Inventory.objects.get(name='The Matrix'),
            start_date=datetime.now() + timedelta(days=15),
            embargo_date=datetime.now() + timedelta(days=30),
            is_active=False
        ),
        [order_tag_dict['Los Angeles'], order_tag_dict['Cancelled'], order_tag_dict['Dubbing'], order_tag_dict['Transcoding']]
    ]
    
]

for order in orders:
    order_data, tags = order
    Order.objects.create(**order_data).tags.add(*tags)