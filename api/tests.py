from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product, Supplier, Shipment, Route

class ModelTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Test Product", category="Electronics")
        self.supplier = Supplier.objects.create(name="Test Supplier", supplier_type="Company", location="NY")
        self.shipment = Shipment.objects.create(origin="NY", destination="LA", status="Pending")
        self.route = Route.objects.create(source="NY", destination="LA", distance_km=4000)

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Test Product")
        self.assertEqual(str(self.product), "Test Product")

    def test_supplier_creation(self):
        self.assertEqual(self.supplier.name, "Test Supplier")
        self.assertEqual(str(self.supplier), "Test Supplier")

    def test_shipment_creation(self):
        self.assertEqual(self.shipment.status, "Pending")
        self.assertEqual(str(self.shipment), "NY -> LA (Pending)")

    def test_route_creation(self):
        self.assertEqual(self.route.distance_km, 4000)
        self.assertEqual(str(self.route), "NY to LA")

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(name="API Product", category="Software")

    def test_get_products(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_product(self):
        data = {'name': 'New Product', 'category': 'Hardware'}
        response = self.client.post('/api/products/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)
