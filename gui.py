import streamlit as st
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')
st.set_page_config(layout="wide") 

model = pickle.load(open('modelSVC.pkl','rb'))

st.markdown("**<h1 style='text-align: center'> CROP RECOMMENDATION SYSTEM**</h1>", unsafe_allow_html=True)
Nitrogen = st.slider('**N(Nitrogen):**',0.0,150.0)
Phosphorous = st.slider('**P(Phosphorous):**',0.0,150.0)
Potassium = st.slider('**K(Potassium):**',0.0,210.0)
Temperature = st.slider('**Temperature:**',5.0,50.0)
Humidity = st.slider('**Humidity:**',5.0,110.0)
pH = st.slider('**pH:**',6.0,8.0)
Rainfall = st.slider('**Amount of Rainfall:**',0.0, 1500.0)
submit = st.button("Submit")

LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'he': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'or': 'odia',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'ug': 'uyghur',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu'
}
from deep_translator import GoogleTranslator
#from google_trans_new import google_translator

#translator = google_translator()

selected_language = st.selectbox("Select Language", list(LANGUAGES.values()))

def translate_app_content(text):
    return translate_text(text, selected_language)

# def detect_language(text):
#     detect_language_data = translator.detect(text)
#     lang = detect_language_data.lang
#     confidence = detect_language_data.confidence
#     return lang, confidence

from deep_translator.exceptions import LanguageNotSupportedException

def translate_text(text, dest):
    try:
        translated_text = GoogleTranslator(source='auto', target=dest).translate(text)
        return translated_text
    except LanguageNotSupportedException:
        return f"Translation to {dest} is not supported."

st.markdown("""
<style>
.big-font {
    font-size: 20px !important;
}
</style>
""", unsafe_allow_html=True)

p = [[Nitrogen, Phosphorous, Potassium, Temperature, Humidity, pH, Rainfall]]
crop = model.predict(p)

if submit:
    st.write(translate_app_content(f'**<p class="big-font">Recommended Crop is -** {crop[0]} </p>'), unsafe_allow_html=True)

    if(crop == 'rice'):
        st.markdown(translate_app_content('**<p class="big-font">Do\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Water Management:** Maintain proper water levels in the paddy fields.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content(' **<p class="big-font">Soil Conditions:** Choose well-drained clayey soils for cultivation.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content(' **<p class="big-font">Temperature:** Rice thrives in warm temperatures, so ensure the right climate.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Fertilization:** Apply nitrogenous fertilizers appropriately. </p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Overwatering:** Avoid excessive water as it may lead to diseases.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Poor Drainage:** Do not cultivate in poorly drained soils.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Late Planting:** Avoid late planting, as it may affect yield.</p>'), unsafe_allow_html=True)

    elif crop == 'maize':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Sunlight:** Maize requires full sunlight, so choose a sunny location</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Spacing:** Plant seeds at the recommended spacing.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Soil:** Well-drained loamy soils are ideal.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Fertilization:** Provide adequate nutrients, especially nitrogen.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Overcrowding:** Avoid planting too closely; give enough space between plants.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Waterlogging:** Maize doesn\'t tolerate waterlogged conditions.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Poor Soil:** Avoid poorly-drained or acidic soils.</p>'), unsafe_allow_html=True)

    elif crop == 'Soyabeans':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Crop Rotation:** Practice crop rotation for better yield</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Inoculation:** Use nitrogen-fixing bacteria for soil inoculation.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Planting Time:**  Plant during the recommended season.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Weed Control:**  Implement effective weed control measures.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Overcrowding:** Plant at recommended spacing to prevent overcrowding.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Late Planting:** Avoid late planting; soybeans are sensitive to day length.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Poor Drainage:** Soybeans prefer well-drained soils.</p>'), unsafe_allow_html=True)

    elif crop == 'beans':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Support:** Provide support for climbing varieties.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Watering:** Maintain consistent soil moisture.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Spacing:** Plant seeds at the recommended spacing.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Fertilization:** Apply balanced fertilizers.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Overwatering:** Beans are susceptible to waterlogging; avoid overwatering.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Late Planting:** Plant on time for optimal yield.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Neglecting Weeds:** Ensure proper weed control.</p>'), unsafe_allow_html=True)

    elif crop == 'peas':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Support:** Use supports for climbing varieties.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Cool Season:** Plant during cool seasons.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Well-Drained Soil:** Peas prefer well-drained soil.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Mulching:** Mulch to retain soil moisture.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Overwatering:** Peas are sensitive to waterlogging; avoid excessive watering.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Hot Weather:** Avoid planting during hot weather.</p>'), unsafe_allow_html=True)

    elif crop == 'groundnut':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**'),unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Sandy Loam Soil:** Groundnuts prefer well-drained sandy loam soil.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Planting Depth:** Plant seeds at the right depth.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Rotation:** Practice crop rotation for disease control.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Fertilization:** Apply phosphorus-rich fertilizers.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Waterlogging:** Avoid waterlogged conditions.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Overcrowding:** Plant at recommended spacing.</p>'), unsafe_allow_html=True)

    elif crop == 'cowpeas':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Warm Season:** Plant during warm seasons.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Well-Drained Soil:** Cowpeas prefer well-drained soil.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Fertilization:** Apply organic matter or balanced fertilizers.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Watering:** Maintain consistent soil moisture.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Overwatering:** Avoid overwatering; cowpeas tolerate drought better than waterlogging.</p>'), unsafe_allow_html=True)

    elif crop == 'banana':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Sunlight:** Requires full sunlight.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Watering:** Provide consistent moisture.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Well-Drained Soil:** Plant in well-drained, fertile soil.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Mulching:** Mulch to retain soil moisture.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Waterlogging:** Avoid waterlogged conditions.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Poor Drainage:** Planting in poorly drained soil.</p>'), unsafe_allow_html=True)

    elif crop == 'mango':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Warm Climate:** Mangoes thrive in warm climates.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Well-Drained Soil:** Plant in well-drained sandy loam.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Pruning:** Prune regularly for proper shape and size.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Overwatering:** Avoid excessive watering once established.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Waterlogging:** Mango trees don\'t tolerate waterlogged conditions.</p>'), unsafe_allow_html=True)

    elif crop == 'grapes':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Sunlight:** Grapes need full sunlight.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Training:** Proper training and pruning.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Fertilization:** Apply balanced fertilizers.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Disease Control:** Implement disease control measures.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Overwatering:** Grapes are susceptible to root rot; avoid overwatering.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Poor Drainage:** Ensure well-drained soil.</p>'), unsafe_allow_html=True)

    elif crop == 'watermelon':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Sandy Soil:** Watermelons prefer sandy, well-drained soil.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Watering:** Consistent watering during the growing season.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Spacing:** Provide enough space between plants.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**'),unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Overwatering:**  Watermelons are sensitive to waterlogging.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Late Planting:** Plant on time for proper fruit development.</p>'), unsafe_allow_html=True)

    elif crop == 'apple':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Chill Hours:** Choose apple varieties suited to your region\'s chill hours.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Pruning:** Regular pruning for shape and size control.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Well-Drained Soil:** Plant in well-drained soil.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Overcrowding:** Provide adequate spacing between apple trees.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Waterlogging:** Apples don\'t tolerate waterlogged conditions.</p>'), unsafe_allow_html=True)

    elif crop == 'orange':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Warm Climate:** Oranges thrive in warm climates.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Fertilization:** Apply balanced fertilizers.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Well-Drained Soil:** Plant in well-drained soil.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Overwatering:** Provide adequate, but not excessive, water.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Waterlogging:** Avoid waterlogged conditions.</p>'), unsafe_allow_html=True)

    elif crop == 'cotton':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Spacing:** Plant seeds at the recommended spacing.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Pest Control:** Implement pest control measures.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Well-Drained Soil:** Cotton prefers well-drained loamy soil.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Overwatering:** Cotton is sensitive to waterlogging.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Late Planting:** Plant on time for optimal yield.</p>'), unsafe_allow_html=True)

    elif crop == 'coffee':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Altitude:** Choose the right altitude for coffee cultivation.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Shade:** Provide shade for young coffee plants.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Fertilization:** Apply organic fertilizers</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Pest Control:** Monitor and control pests.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Overwatering:** Maintain proper soil moisture without overwatering.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Waterlogging:** Coffee plants are sensitive to waterlogged conditions.</p>'), unsafe_allow_html=True)

    elif crop == 'chickpea':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Well-Drained Soil:** Chickpeas prefer well-drained soil with a slightly acidic to neutral pH.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Sunlight:** Provide sufficient sunlight for optimal growth.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Crop Rotation:** Practice crop rotation to prevent diseases and maintain soil fertility.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Over-fertilization:** Avoid excessive use of nitrogen-rich fertilizers.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Waterlogging:** Avoid waterlogged conditions as chickpeas are sensitive to excessive moisture.Coffee plants are sensitive to waterlogged conditions.</p>'), unsafe_allow_html=True)

    elif crop == 'kidneybeans':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Support Structure:** Provide support structures for climbing varieties.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Regular Watering:** Maintain consistent soil moisture, especially during flowering and pod development.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Crop Rotation:** Practice crop rotation to prevent diseases and maintain soil fertility.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Overcrowding:**  Avoid overcrowding plants; provide adequate spacing for air circulation.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Water Stress:** Avoid water stress during critical growth stages.</p>'), unsafe_allow_html=True)

    elif crop == 'jute':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Well-Drained Soil:**  Jute grows well in well-drained, fertile soil.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Regular Watering:** Keep the soil consistently moist.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Crop Rotation:** Practice crop rotation to prevent diseases and maintain soil fertility.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Over-fertilization:** Use fertilizers judiciously.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Waterlogging:** Avoid waterlogged conditions.</p>'), unsafe_allow_html=True)

    elif crop == 'coconut':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Well-Drained Soil:** Coconut palms prefer well-drained sandy soils.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Regular Watering:** Keep the soil consistently moist.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Fertilization:** Apply balanced fertilizers.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Over-fertilization:** Avoid excessive use of fertilizers.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Water Stress:** Avoid water stress, especially during dry periods.</p>'), unsafe_allow_html=True)

    elif crop == 'papaya':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Well-Drained Soil:** Plant in well-drained soil with organic matter.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Regular Pruning:** Prune to control height and encourage lateral branching.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Irrigation:** Provide consistent and adequate water.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Over-fertilization:**Avoid excessive use of nitrogen.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Waterlogging:** Avoid waterlogged conditions.</p>'), unsafe_allow_html=True)

    elif crop == 'muskmelon':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Warm Climate:** Muskmelons thrive in warm climates.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Proper Spacing:** Plant seeds or seedlings with adequate spacing.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Mulching:** Use mulch to retain soil moisture.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Overwatering:**  Avoid excessive water, especially during fruiting</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Late Planting:** Plant on time for optimal yield.</p>'), unsafe_allow_html=True)

    elif crop == 'pomegranate':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Well-Drained Soil:**  Pomegranates prefer well-drained, loamy soil.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Pruning:** Regular pruning for shape and size control.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Irrigation:**  Provide adequate and consistent irrigation.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Over-pruning:** Avoid excessive pruning, especially of young trees.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Waterlogging:** Avoid waterlogged conditions.</p>'), unsafe_allow_html=True)

    elif crop == 'lentil':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Cool Climate:** Lentils thrive in cool climates.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Sunlight:** Provide full sunlight for optimal growth.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Crop Rotation:** Practice crop rotation to prevent diseases and maintain soil fertility.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Over-fertilization:** Use fertilizers judiciously.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Waterlogging:** Avoid waterlogged conditions.</p>'), unsafe_allow_html=True)

    elif crop == 'jute':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Well-Drained Soil:** Plant in well-drained soil.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Regular Watering:** Keep the soil consistently moist.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Crop Rotation:** Practice crop rotation to prevent diseases and maintain soil fertility.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Over-fertilization:** Avoid excessive use of nitrogen-rich fertilizers.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Water Stress:** Avoid water stress during critical growth stages.</p>'), unsafe_allow_html=True)

    elif crop == 'mungbeans':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Warm Climate** Moth beans thrive in warm climates.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Regular Watering:** Keep the soil consistently moist.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Mulching:** Use mulch to retain soil moisture.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Late Planting:** Plant on time for optimal growth.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Waterlogging:** Avoid waterlogged conditions.</p>'), unsafe_allow_html=True)

    elif crop == 'pigeonpeas':
        st.write(translate_app_content('**<p class="big-font">Do\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Well-Drained Soil:** Plant in well-drained, sandy loam soil.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Sunlight:** Pigeon peas thrive in full sunlight.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Pruning:** Prune to encourage branching and improve pod production.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Dont\'s:**</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Over-pruning:** Avoid excessive pruning, especially during flowering.</p>'), unsafe_allow_html=True)
        st.write(translate_app_content('**<p class="big-font">Waterlogging:** Avoid waterlogged conditions.</p>'), unsafe_allow_html=True)

import base64

def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:image/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_background("farming2.jpg")

