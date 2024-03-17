# Import the necessary modules
import json
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

# Define your document's header details
company_name = "<b>Company XYZ</b>"
company_contact_info = "1234 Business Rd., Business City | +123 456 7890 | contact@companyxyz.com"
document_title = "Price Quote / Proposal for Exterior Renovation"
quote_number = "<b>Quote No:</b> 123456"
customer_name = "<b>Customer Name:</b> John Doe"
object_address = "<b>Object Address:</b> 1234 Main St, Anytown"
quote_date = "<b>Quote Date:</b> 2023-02-02"

# Load your data from 'proposal.json'
with open('proposal.json', 'r') as file:
    data = json.load(file)

# Initialize the PDF document
pdf_file = "Renovation_Proposal_123456.pdf"
doc = SimpleDocTemplate(pdf_file, pagesize=A4)
elements = []

# Custom styles
styles = getSampleStyleSheet()
custom_style = ParagraphStyle('CustomStyle', parent=styles['Normal'], fontSize=10, leading=12)
header_style = ParagraphStyle('HeaderStyle', parent=styles['Normal'], fontSize=12, leading=14)

# Add company and document details
elements.append(Paragraph(company_name, header_style))
elements.append(Paragraph(company_contact_info, custom_style))
elements.append(Spacer(1, 6))
elements.append(Paragraph(document_title, header_style))
elements.append(Paragraph(quote_number, custom_style))
elements.append(Spacer(1, 12))

# Add customer and project details
elements.append(Paragraph(customer_name, custom_style))
elements.append(Paragraph(object_address, custom_style))
elements.append(Paragraph(quote_date, custom_style))
elements.append(Spacer(1, 12))

# Generate table data from the JSON
table_data = [['Description', 'Quantity', 'Unit', 'Unit Price', 'Total Cost']]
for item in data['costItems']:
    row = [item['description'], item['quantity'], item['unit'], item['totalUnitPrice'], item['totalCost']]
    table_data.append(row)

# Append the total cost information with merging setup
table_data.append(['Total Cost Excl. VAT:', '', '', '', data['totalCostExclVAT']])
table_data.append(['VAT (22%):', '', '', '', data['VAT']])
table_data.append(['Total Cost:', '', '', '', data['totalCost']])

# Create and style the table
table = Table(table_data)
table_style = TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('ALIGN', (0, 1), (0, -4), 'LEFT'),  # Align the description column text to the left for all but the last 3 rows
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -4), colors.lightgrey),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    # Merge cells for the last three rows
    ('SPAN', (0, -3), (-2, -3)),  # Merge description cells for "Total Cost Excl. VAT:"
    ('SPAN', (0, -2), (-2, -2)),  # Merge description cells for "VAT (22%):"
    ('SPAN', (0, -1), (-2, -1)),  # Merge description cells for "Total Cost:"
    ('ALIGN', (0, -3), (-1, -1), 'RIGHT'),  # Ensure right alignment for the last 3 rows
])
table.setStyle(table_style)
elements.append(table)

# Footer information
footer_elements = [
    Paragraph("Thank you for considering our services. We look forward to the opportunity to work with you.", custom_style),
    Spacer(1, 12),
    Paragraph("For any questions or further information, please do not hesitate to contact us.", custom_style),
    Paragraph("This proposal is valid for 30 days from the date of issuance.", custom_style)
]
# Add footer elements
elements.extend(footer_elements)
# Build the PDF
doc.build(elements)
