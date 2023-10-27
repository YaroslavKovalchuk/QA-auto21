from sqlite3 import OperationalError
import pytest


@pytest.mark.database
def test_database_connection(database):
    database.test_connection()


@pytest.mark.database
def test_check_all_users(database):
    users = database.get_all_users()
    
    print(users)


@pytest.mark.database
def test_check_user_sergii(database):
    user = database.get_user_address_by_name('Sergii')
    
    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] == 'Ukraine'


@pytest.mark.database
def test_product_qnt_update(database):
    database.update_product_qnt_by_id(1,25)
    water_qnt = database.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25


@pytest.mark.database
def test_product_insert(database):
    database.insert_product(4,'печиво', 'солодке', 30)
    cookies_qnt = database.select_product_qnt_by_id(4)

    assert cookies_qnt[0][0] == 30


@pytest.mark.database
def test_product_delete(database):
    database.insert_product(99,'тестові', 'дані', 99)
    database.delete_product_by_id(99)
    qnt = database.select_product_qnt_by_id(99)

    assert len(qnt) == 0


@pytest.mark.database
def test_detailed_orders(database):
    orders = database.get_detailed_orders()

    assert len(orders) == 1

    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'


@pytest.mark.database
def test_product_insert_with_invalid_data_type_id(database):
      with pytest.raises(OperationalError):
          database.insert_product('id', 'морозиво', 'пломбір', 34)


@pytest.mark.database
def test_product_insert_with_invalid_data_type_qountity(database):
      with pytest.raises(OperationalError):
          database.insert_product(5, 'морозиво', 'пломбір', 'numbers')


@pytest.mark.database
def test_customer_insert_valid_data(database):
    database.insert_customer(12, 'Ivan', 'Zelena 4a', 'Lviv', 80067, 'Ukraine')
    customer = database.get_customer_by_id(12)

    assert len(customer) == 1

    assert customer[0][0] == 12
    assert customer[0][1] == 'Ivan'
    assert customer[0][2] == 'Zelena 4a'
    assert customer[0][3] == 'Lviv'
    assert customer[0][4] == '80067'
    assert customer[0][5] == 'Ukraine'


@pytest.mark.database
def test_customer_insert_with_invalid_data_type_id(database):
      with pytest.raises(OperationalError):
          database.insert_customer('id', 'Ivan', 'Zelena 4a', 'Lviv', 80067, 'Ukraine')


@pytest.mark.database
def test_customer_insert_with_invalid_data_type_postal_code(database):
      with pytest.raises(OperationalError):
          database.insert_customer(12, 'Ivan','Zelena 4a', 'Lviv', "post", 'Ukraine')