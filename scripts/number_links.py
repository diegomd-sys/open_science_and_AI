import xml.etree.ElementTree as ET

# Function to extract links from each paper in the XML
def extract_links(xml_data):
    # Parse the XML data
    tree = ET.ElementTree(ET.fromstring(xml_data))
    root = tree.getroot()

    # Define the namespaces for the XML (adjust this based on your XML structure)
    namespaces = {'tei': 'http://www.tei-c.org/ns/1.0'}

    # Initialize a dictionary to store the paper titles and their respective links
    paper_links = {}

    # Find all <teiHeader> elements (each represents a paper)
    papers = root.findall('.//tei:teiHeader', namespaces)

    # Loop through each paper and extract the links
    for paper in papers:
        # Extract the title of the paper
        title = paper.find('.//tei:titleStmt/tei:title', namespaces)
        if title is not None:
            paper_title = title.text
        else:
            paper_title = "Unnamed Article"

        # Find all <link> tags with an 'href' attribute (links)
        links = paper.findall('.//tei:link', namespaces)
        
        # Extract the 'href' attribute for each link
        link_list = [link.attrib['href'] for link in links if 'href' in link.attrib]

        # Store the links for this paper in the dictionary
        paper_links[paper_title] = link_list

    return paper_links

# Example XML data (replace this with your actual XML data)
with open('388665934.pdf.tei.xml', 'r') as xml_file:
    xml_data = xml_file.read()

# Get the links for each paper
links_per_paper = extract_links(xml_data)

# Display the links for each paper
for paper_title, links in links_per_paper.items():
    print(f"Links for '{paper_title}':")
    for link in links:
        print(f"- {link}")
    print()
