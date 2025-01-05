from tests.conftest import product1, product2, product3


def test_init(Product_test):
    assert Product_test.name == "Samsung Galaxy S23 Ultra"
    assert Product_test.description == "256GB, Серый цвет, 200MP камера"
    assert Product_test.price == 180000.0
    assert Product_test.quantity == 5


def test_initt(Category_test):
    assert Category_test.name == "Смартфоны"
    assert (
        Category_test.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert Category_test.products == (
        [
            product1,
            product2,
            product3,
        ]
    )
    assert Category_test.category_count == 1
    assert Category_test.product_count == 3
