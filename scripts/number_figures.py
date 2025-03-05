import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# Function to count the number of figures in each article
def count_figures_in_article(xml_data):
    # Parse the XML data
    tree = ET.ElementTree(ET.fromstring(xml_data))
    root = tree.getroot()

    # Define namespaces for the XML
    namespaces = {'tei': 'http://www.tei-c.org/ns/1.0'}

    # Initialize a dictionary to store article titles and their respective figure counts
    figure_counts = {}

    # Find all articles (assuming each article is structured with <teiHeader> and <fileDesc>)
    # You can adjust this based on how articles are structured in your XML files
    articles = root.findall('.//tei:teiHeader', namespaces)

    # Loop through each article and count the number of <figure> elements
    for article in articles:
        # Extract the title of the article
        title = article.find('.//tei:titleStmt/tei:title', namespaces)
        if title is not None:
            article_title = title.text
        else:
            article_title = "Unnamed Article"

        # Count the number of <figure> elements in this article
        figures = article.findall('.//tei:figure', namespaces)
        figure_count = len(figures)

        # Add the count to the dictionary
        figure_counts[article_title] = figure_count

    return figure_counts

# Example XML data (replace this with your XML data)
with open('1396969.pdf.tei.xml', 'r') as xml_file:
    xml_data = xml_file.read()

# Get the figure counts per article
figure_counts = count_figures_in_article(xml_data)

# Extract article titles and figure counts for visualization
article_titles = list(figure_counts.keys())
figure_counts_values = list(figure_counts.values())

# Create a bar chart to visualize the number of figures per article
plt.figure(figsize=(10, 6))
plt.barh(article_titles, figure_counts_values, color='skyblue')
plt.xlabel('Number of Figures')
plt.title('Number of Figures per Article')
plt.tight_layout()

# Show the plot
plt.show()
