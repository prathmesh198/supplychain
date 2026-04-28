import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from api.models import Product, Supplier, Shipment, Route

def seed():
    # Clear existing
    Product.objects.all().delete()
    Supplier.objects.all().delete()
    Shipment.objects.all().delete()
    Route.objects.all().delete()

    # Products
    Product.objects.create(name="Paracetamol", category="Pharmaceutical")
    Product.objects.create(name="Mobile Chip", category="Electronics")
    Product.objects.create(name="Iron Ore", category="Raw Material")
    Product.objects.create(name="Steel Rod", category="Finished Product")

    # Suppliers
    Supplier.objects.create(name="Global Pharma Supply", supplier_type="Company", location="Mumbai", contact="gps@example.com")
    Supplier.objects.create(name="Tech Components Inc.", supplier_type="Company", location="Shenzhen", contact="techcomp@example.com")
    Supplier.objects.create(name="National Miners", supplier_type="Company", location="Odisha", contact="miners@example.com")

    # Shipments
    Shipment.objects.create(origin="Nagpur", destination="Mumbai", status="In Transit")
    Shipment.objects.create(origin="Delhi", destination="Bangalore", status="Delivered")
    Shipment.objects.create(origin="Shenzhen", destination="Chennai", status="Pending")

    # Routes
    Route.objects.create(source="Nagpur", destination="Mumbai", distance_km=800)
    Route.objects.create(source="Delhi", destination="Bangalore", distance_km=2100)
    Route.objects.create(source="Shenzhen", destination="Chennai", distance_km=4500)

    print("Seed data successfully added!")

if __name__ == '__main__':
    seed()
