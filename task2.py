from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.units import cm

def create_receipt(filename, customer_details, items):
    pdf = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    title_style = ParagraphStyle(name='Title', fontSize=24, leading=28, alignment=1, textColor=colors.green, fontName='Helvetica-Bold')

    address_style = ParagraphStyle(name='Address', fontSize=12, leading=14, alignment=1, textColor=colors.black, fontName='Helvetica')
    normal_style = styles['Normal']
    normal_style.fontSize = 10

    # Title
    title = Paragraph("Indian Tech", title_style)
    elements.append(title)

    # Address
    address = Paragraph("Cape Town 19-144-A/36, Beside clock tower", address_style)
    elements.append(address)
    elements.append(Spacer(1, 20))

    # Header details (Date, Customer Name, Invoice No, Mobile No, Payment Method)
    header_data = [
        ["Date:", customer_details['Date']],
        ["Customer Name:", customer_details['Customer Name']],
        ["Invoice No:", customer_details['Invoice No']],
        ["Mobile No:", customer_details['Mobile No']],
        ["Payment Method:", customer_details['Payment Method']]
    ]

    header_table = Table(header_data, colWidths=[100, 400])
    header_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'), ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, -1), 10), ('BOTTOMPADDING', (0, 0), (-1, -1), 6), ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    elements.append(header_table)
    elements.append(Spacer(1, 20))

    payment_details_header = Paragraph("Payment Details:", normal_style)
    elements.append(payment_details_header)
    elements.append(Spacer(1, 12))

    payment_details_data = [["Item", "Quantity", "Unit Price", "Total Price"]]
    total_amount = 0

    for item, details in items.items():
        quantity, unit_price = details
        total_price = quantity * unit_price
        payment_details_data.append([item, str(quantity), f"Rs. {unit_price:.2f}", f"Rs. {total_price:.2f}"])
        total_amount += total_price

    payment_details_table = Table(payment_details_data, colWidths=[220, 80, 100, 100])
    payment_details_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#E8E8E8')),  # Light grey background for header
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('ALIGN', (1, 1), (3, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 6),
        ('TOPPADDING', (0, 0), (-1, 0), 6),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(payment_details_table)
    elements.append(Spacer(1, 20))

    summary_data = [
        ["Subtotal:", f"Rs. {total_amount:.2f}"],
        ["Discount:", "Rs. 0.00"],
        ["Total:", f"Rs. {total_amount:.2f}"]
    ]

    summary_table = Table(summary_data, colWidths=[220, 100])
    summary_table.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'RIGHT'), ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, -1), 10), ('BOTTOMPADDING', (0, 0), (-1, -1), 6), ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    elements.append(summary_table)
    pdf.build(elements)

customer_details = {
    "Date": input("Enter the date (DD-MM-YYYY): "),
    "Customer Name": input("Enter the customer name: "),
    "Invoice No": input("Enter the invoice number: "),
    "Mobile No": input("Enter the mobile number: "),
    "Payment Method": input("Enter the payment method: ")
}

num_items = int(input("Enter the number of items purchased: "))
items = {}
for i in range(num_items):
    item_name = input(f"Enter item {i+1} name: ")
    quantity = int(input(f"Enter item {i+1} quantity: "))
    unit_price = float(input(f"Enter item {i+1} unit price: "))
    items[item_name] = (quantity, unit_price)

create_receipt("receipt.pdf", customer_details, items)
print("Receipt generated and saved as receipt.pdf")