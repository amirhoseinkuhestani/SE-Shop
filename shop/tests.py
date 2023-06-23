from django.test import TestCase
from .models import Category, Product

class ProductTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(title="Electronics", is_active=True)
        self.product = Product.objects.create(
            title="Laptop",
            thumbnail="path/to/thumbnail.jpg",
            category=self.category,
            quantity=10,
            price=1500,
            weight=2,
            note="Sample laptop",
            discount=10,
            colors="B",
            slug="laptop",
            is_active=True,
        )

    def test_product_creation(self):
        product = self.product
        self.assertEqual(product.title, "Laptop")
        self.assertEqual(product.category, self.category)
        self.assertEqual(product.quantity, 10)
        self.assertEqual(product.price, 1500)
        self.assertEqual(product.weight, 2)
        self.assertEqual(product.note, "Sample laptop")
        self.assertEqual(product.discount, 10)
        self.assertEqual(product.colors, "B")
        self.assertEqual(product.slug, "laptop")
        self.assertTrue(product.is_active)

    def test_discount_price_calculation(self):
        product = self.product
        discount_price = product.price - (product.price * product.discount) / 100
        self.assertEqual(product.discount_price, discount_price)

    def test_str_representation(self):
        product = self.product
        self.assertEqual(str(product), "Laptop")

    def test_default_is_active_value(self):
        product = Product.objects.create(
            title="Keyboard",
            thumbnail="path/to/thumbnail.jpg",
            category=self.category,
            quantity=5,
            price=50,
            weight=1,
            note="Sample keyboard",
            discount=0,
            colors="B",
            slug="keyboard",
        )
        self.assertTrue(product.is_active)