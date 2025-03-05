import xml.etree.ElementTree as ET
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Función para extraer el texto del abstract
def get_abstract(xml_data):
    # Parsear el XML
    tree = ET.ElementTree(ET.fromstring(xml_data))
    root = tree.getroot()

    # Espacios de nombres utilizados en el XML
    namespaces = {'tei': 'http://www.tei-c.org/ns/1.0'}

    # Buscar el elemento abstract dentro de profileDesc
    abstract = root.find('.//tei:teiHeader/tei:profileDesc/tei:abstract', namespaces)

    if abstract is not None:
        # Buscar el div dentro del abstract
        div = abstract.find('.//tei:div', namespaces)
        if div is not None:
            # Buscar los elementos <p> o <s> dentro del <div> y extraer el texto
            text_content = ""
            for element in div.findall('.//tei:p', namespaces):
                text_content += " " + (element.text or "")  # Añadir texto del <p>
            for element in div.findall('.//tei:s', namespaces):
                text_content += " " + (element.text or "")  # Añadir texto del <s>

            if text_content.strip():
                return text_content.strip()  # Retornar el texto limpio
            else:
                return "No text found in abstract"
        else:
            return "No div found in abstract"
    else:
        return "No abstract found"

# Leer el archivo XML
with open('335811.pdf.tei.xml', 'r') as xml_file:
    xml_data = xml_file.read()

# Extraer el abstract
abstract_text = get_abstract(xml_data)

# Verificar si se ha encontrado el abstract y luego generar la nube de palabras
if abstract_text != "No abstract found" and abstract_text != "No div found in abstract" and abstract_text != "No text found in abstract":
    # Crear la nube de palabras
    wordcloud = WordCloud(width=800, height=400).generate(abstract_text)

    # Mostrar la nube de palabras
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
else:
    print(abstract_text)
