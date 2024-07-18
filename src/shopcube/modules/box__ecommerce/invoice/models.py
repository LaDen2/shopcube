from datetime import datetime
from init import db

class Invoice(db.Model):
    __tablename__ = "invoices"

    id = db.Column(db.Integer, primary_key=True)
    invoice_number = db.Column(db.String(100), unique=True, nullable=True)
    invoice_date = db.Column(db.DateTime, default=datetime.now, nullable=True)
    due_date = db.Column(db.DateTime, nullable=True)

    # Company Info
    company_name = db.Column(db.String(100), nullable=True)
    company_address = db.Column(db.String(300), nullable=True)
    company_contact = db.Column(db.String(100), nullable=True)

    # Customer Information
    customer_name = db.Column(db.String(100), nullable=True)
    customer_address = db.Column(db.String(300), nullable=True)
    customer_contact = db.Column(db.String(100), nullable=True)

    # Transaction Details
    transaction_id = db.Column(db.Integer, db.ForeignKey('transactions.id'), nullable=True)
    #transaction = db.relationship('Transaction', back_populates='invoice', lazy=True)

    # Pricing Summary
    subtotal = db.Column(db.Float, nullable=True)
    discount = db.Column(db.Float, nullable=True, default=0.0)
    taxes = db.Column(db.Float, nullable=True, default=0.0)
    shipping = db.Column(db.Float, nullable=True, default=0.0)
    total_amount = db.Column(db.Float, nullable=True)

    # Payment Information
    payment_method = db.Column(db.String(50), nullable=True)
    payment_status = db.Column(db.String(50), nullable=True)
    payment_reference_number = db.Column(db.String(100), nullable=True)

    # Additional Information
    terms_and_conditions = db.Column(db.Text, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    return_policy = db.Column(db.Text, nullable=True)
    po_number = db.Column(db.String(100), nullable=True)

    def add(self):
        db.session.add(self)

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
