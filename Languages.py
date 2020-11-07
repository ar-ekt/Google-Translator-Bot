from Consts import *

languages = {
    "af":    ("Afrikaans",             AFRIKAANS_FLAG_EMOJI),
    "sq":    ("Albanian",              ALBANIAN_FLAG_EMOJI),
    "am":    ("Amharic",               AMHARIC_FLAG_EMOJI),
    "ar":    ("Arabic",                ARABIC_FLAG_EMOJI),
    "hy":    ("Armenian",              ARMENIAN_FLAG_EMOJI),
    "az":    ("Azerbaijani",           AZERBAIJANI_FLAG_EMOJI),
    
#     "eu":    ("Basque",                BASQUE_FLAG_EMOJI),
    "be":    ("Belarusian",            BELARUSIAN_FLAG_EMOJI),
    "bn":    ("Bengali",               BENGALI_FLAG_EMOJI),
    "bs":    ("Bosnian",               BOSNIAN_FLAG_EMOJI),
    "bg":    ("Bulgarian",             BULGARIAN_FLAG_EMOJI),
    
    "ca":    ("Catalan",               CATALAN_FLAG_EMOJI),
    "ceb":   ("Cebuano",               CEBUANO_FLAG_EMOJI),
#     "ny":    ("Chichewa",              CHICHEWA_FLAG_EMOJI),
    "zh-cn": ("Chinese (Simplified)",  CHINESE_SIMPLIFIED_FLAG_EMOJI),
    "zh-tw": ("Chinese (Traditional)", CHINESE_TRADITIONAL_FLAG_EMOJI),
    "co":    ("Corsican",              CORSICAN_FLAG_EMOJI),
    "hr":    ("Croatian",              CROATIAN_FLAG_EMOJI),
    "cs":    ("Czech",                 CZECH_FLAG_EMOJI),
    
    "da":    ("Danish",                DANISH_FLAG_EMOJI),
    "nl":    ("Dutch",                 DUTCH_FLAG_EMOJI),
    
    "en":    ("English",               ENGLISH_FLAG_EMOJI),
    "eo":    ("Esperanto",             ESPERANTO_FLAG_EMOJI),
    "et":    ("Estonian",              ESTONIAN_FLAG_EMOJI),
    
    "tl":    ("Filipino",              FILIPINO_FLAG_EMOJI),
    "fi":    ("Finnish",               FINNISH_FLAG_EMOJI),
    "fr":    ("French",                FRENCH_FLAG_EMOJI),
    "fy":    ("Frisian",               FRISIAN_FLAG_EMOJI),
    
    "gl":    ("Galician",              GALICIAN_FLAG_EMOJI),
    "ka":    ("Georgian",              GEORGIAN_FLAG_EMOJI),
    "de":    ("German",                GERMAN_FLAG_EMOJI),
    "el":    ("Greek",                 GREEK_FLAG_EMOJI),
    "gu":    ("Gujarati",              GUJARATI_FLAG_EMOJI),
    
    "ht":    ("Haitian Creole",        HAITIAN_CREOLE_FLAG_EMOJI),
    "ha":    ("Hausa",                 HAUSA_FLAG_EMOJI),
    "haw":   ("Hawaiian",              HAWAIIAN_FLAG_EMOJI),
    "iw":    ("Hebrew",                HEBREW_FLAG_EMOJI),
    "hi":    ("Hindi",                 HINDI_FLAG_EMOJI),
    "hmn":   ("Hmong",                 HMONG_FLAG_EMOJI),
    "hu":    ("Hungarian",             HUNGARIAN_FLAG_EMOJI),
    
    "is":    ("Icelandic",             ICELANDIC_FLAG_EMOJI),
    "ig":    ("Igbo",                  IGBO_FLAG_EMOJI),
    "id":    ("Indonesian",            INDONESIAN_FLAG_EMOJI),
    "ga":    ("Irish",                 IRISH_FLAG_EMOJI),
    "it":    ("Italian",               ITALIAN_FLAG_EMOJI),
    
    "ja":    ("Japanese",              JAPANESE_FLAG_EMOJI),
    "jw":    ("Javanese",              JAVANESE_FLAG_EMOJI),
    
    "kn":    ("Kannada",               KANNADA_FLAG_EMOJI),
    "kk":    ("Kazakh",                KAZAKH_FLAG_EMOJI),
    "km":    ("Khmer",                 KHMER_FLAG_EMOJI),
    "ko":    ("Korean",                KOREAN_FLAG_EMOJI),
    "ku":    ("Kurdish (Kurmanji)",    KURDISH_KURMANJI_FLAG_EMOJI),
    "ky":    ("Kyrgyz",                KYRGYZ_FLAG_EMOJI),
    
    "lo":    ("Lao",                   LAO_FLAG_EMOJI),
    "la":    ("Latin",                 LATIN_FLAG_EMOJI),
    "lv":    ("Latvian",               LATVIAN_FLAG_EMOJI),
    "lt":    ("Lithuanian",            LITHUANIAN_FLAG_EMOJI),
    "lb":    ("Luxembourgish",         LUXEMBOURGISH_FLAG_EMOJI),
    
    "mk":    ("Macedonian",            MACEDONIAN_FLAG_EMOJI),
    "mg":    ("Malagasy",              MALAGASY_FLAG_EMOJI),
    "ms":    ("Malay",                 MALAY_FLAG_EMOJI),
    "ml":    ("Malayalam",             MALAYALAM_FLAG_EMOJI),
    "mt":    ("Maltese",               MALTESE_FLAG_EMOJI),
    "mi":    ("Maori",                 MAORI_FLAG_EMOJI),
    "mr":    ("Marathi",               MARATHI_FLAG_EMOJI),
    "mn":    ("Mongolian",             MONGOLIAN_FLAG_EMOJI),
#     "my":    ("Myanmar (Burmese)",     MYANMAR_BURMESE_FLAG_EMOJI),
    
    "ne":    ("Nepali",                NEPALI_FLAG_EMOJI),
    "no":    ("Norwegian",             NORWEGIAN_FLAG_EMOJI),
    
    "or":    ("Odia",                  ODIA_FLAG_EMOJI),
    
    "ps":    ("Pashto",                PASHTO_FLAG_EMOJI),
    "fa":    ("Persian",               PERSIAN_FLAG_EMOJI),
    "pl":    ("Polish",                POLISH_FLAG_EMOJI),
    "pt":    ("Portuguese",            PORTUGUESE_FLAG_EMOJI),
    "pa":    ("Punjabi",               PUNJABI_FLAG_EMOJI),
    
    "ro":    ("Romanian",              ROMANIAN_FLAG_EMOJI),
    "ru":    ("Russian",               RUSSIAN_FLAG_EMOJI),
    
    "sm":    ("Samoan",                SAMOAN_FLAG_EMOJI),
    "gd":    ("Scots Gaelic",          SCOTS_GAELIC_FLAG_EMOJI),
    "sr":    ("Serbian",               SERBIAN_FLAG_EMOJI),
    "sn":    ("Shona",                 SHONA_FLAG_EMOJI),
    "sd":    ("Sindhi",                SINDHI_FLAG_EMOJI),
    "si":    ("Sinhala",               SINHALA_FLAG_EMOJI),
    "sk":    ("Slovak",                SLOVAK_FLAG_EMOJI),
    "sl":    ("Slovenian",             SLOVENIAN_FLAG_EMOJI),
    "so":    ("Somali",                SOMALI_FLAG_EMOJI),
    "es":    ("Spanish",               SPANISH_FLAG_EMOJI),
    "su":    ("Sundanese",             SUNDANESE_FLAG_EMOJI),
    "sw":    ("Swahili",               SWAHILI_FLAG_EMOJI),
    "sv":    ("Swedish",               SWEDISH_FLAG_EMOJI),
    
    "tg":    ("Tajik",                 TAJIK_FLAG_EMOJI),
    "ta":    ("Tamil",                 TAMIL_FLAG_EMOJI),
    "te":    ("Telugu",                TELUGU_FLAG_EMOJI),
    "th":    ("Thai",                  THAI_FLAG_EMOJI),
    "tr":    ("Turkish",               TURKISH_FLAG_EMOJI),
    
    "uk":    ("Ukrainian",             UKRAINIAN_FLAG_EMOJI),
    "ur":    ("Urdu",                  URDU_FLAG_EMOJI),
#     "ug":    ("Uyghur",                UYGHUR_FLAG_EMOJI),
    "uz":    ("Uzbek",                 UZBEK_FLAG_EMOJI),
    
    "vi":    ("Vietnamese",            VIETNAMESE_FLAG_EMOJI),
    
    "cy":    ("Welsh",                 WELSH_FLAG_EMOJI),
    
#     "xh":    ("Xhosa",                 XHOSA_FLAG_EMOJI),
    
    "yi":    ("Yiddish",               YIDDISH_FLAG_EMOJI),
    "yo":    ("Yoruba",                YORUBA_FLAG_EMOJI),
    
    "zu":    ("Zulu",                  ZULU_FLAG_EMOJI)
}