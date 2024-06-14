from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.units import cm

def create_receipt(filename):
    # Create document
    pdf = SimpleDocTemplate(filename, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    # Custom styles
    title_style = ParagraphStyle(
        name='Title',
        fontSize=24,
        leading=28,
        alignment=1,  # Center alignment
        textColor=colors.green,  # Green color for the title
        fontName='Helvetica-Bold'
    )

    address_style = ParagraphStyle(
        name='Address',
        fontSize=12,
        leading=14,
        alignment=1,  # Center alignment
        textColor=colors.black,
        fontName='Helvetica'
    )

    normal_style = styles['Normal']
    normal_style.fontSize = 10

    # Title
    title = Paragraph("Hackx Electrics", title_style)
    elements.append(title)

    # Address
    address = Paragraph("Cape Town 19-144-A/36, Beside clock tower", address_style)
    elements.append(address)

    # Spacer
    elements.append(Spacer(1, 20))

    # Header details (Date, Customer Name, Invoice No, Mobile No, Payment Method)
    header_data = [
        ["Date:", "28-05-2024"],
        ["Customer Name:", "John Sena"],
        ["Invoice No:", "097756210"],
        ["Mobile No:", "7786390500"],
        ["Payment Method:", "Credit Card"]
    ]

    header_table = Table(header_data, colWidths=[100, 400])
    header_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))
    elements.append(header_table)

    # Spacer
    elements.append(Spacer(1, 20))

    # Payment Details Header
    payment_details_header = Paragraph("Payment Details:", normal_style)
    elements.append(payment_details_header)

    # Spacer
    elements.append(Spacer(1, 12))

    # Payment Details Table
    payment_details_data = [
        ["Item", "Quantity", "Unit Price", "Total Price"],
        ["LED Bulb", "10", "Rs. 50.00", "Rs. 500.00"],
        ["Switch", "5", "Rs. 30.00", "Rs. 150.00"],
        ["Wiring Cable", "2", "Rs. 200.00", "Rs. 400.00"],
        ["Socket", "8", "Rs. 25.00", "Rs. 200.00"],
        ["Fan", "1", "Rs. 1500.00", "Rs. 1500.00"],
    ]

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

    # Spacer
    elements.append(Spacer(1, 20))

    # Subtotal, Discount, and Total Table
    summary_data = [
        ["Subtotal:", "Rs. 2750.00"],
        ["Discount:", "Rs. 250.00"],
        ["Total:", "Rs. 2500.00"]
    ]

    summary_table = Table(summary_data, colWidths=[220, 100])
    summary_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'RIGHT'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
    ]))

    elements.append(summary_table)

    # Build PDF
    pdf.build(elements)

# Generate the PDF
create_receipt("receipt.pdf")