### Run the server locally
* Run `pip install django`
* Run `python manage.py runserver`
* The server will be available in http://localhost:8000

### Steps to consume the endpoints
* **Register User** : `POST` 
   >JSON data format:
   ```
    {
        "name":"your_name",
        "email":"your_email@example.com",
        "password":"your_password"
    }
    ```
    
     Send JSON data to http://127.0.0.1:8000/api/user/register/

* **Login User** : `POST`
    >JSON data format:
   ```
    {
        "name":"your_name",
        "email":"your_email@example.com",
        "password":"your_password"
    }
    ```
    
     Send JSON data to http://127.0.0.1:8000/api/user/login/

* **Add Items** : `POST`
    >JSON data format:
   ```
    {
        "SKU":"",
        "name":"",
        "tags":"",
        "category":"",
        "inStock":"",
        "availableStock":""
    }
    ```
    
     Send JSON data to http://127.0.0.1:8000/api/item/addItem/

* **Get All Items for authenticated User** : `GET`
    
     Call this end point  http://127.0.0.1:8000/api/item/getItem/ <br>
        this will return data in JSON format.
    >JSON data format:
   ```
    {
        "SKU":"",
        "name":"",
        "tags":"",
        "category":"",
        "inStock":"",
        "availableStock":"",
        "created_at":""
    }
    ```


* **Filter Item for authenticated User** : `GET`
    
    Call this end point http://127.0.0.1:8000/api/item/getItem/?"field_name"__gt="min_value"&"write_field_name"__lt="max_value"&filter=1 <br>
        this will return data in JSON format.
    >JSON data format:
   ```
    {
        "SKU":"",
        "name":"",
        "tags":"",
        "category":"",
        "inStock":"",
        "availableStock":"",
        "created_at":""
    }
    ```


* **Search Item for authenticated User** : `GET`

    Call this end point http://127.0.0.1:8000/api/item/getItem/?"field_name"="value_to_be_searched"&filter=1 <br>
        this will return data in JSON format.
    >JSON data format:
   ```
    {
        "SKU":"",
        "name":"",
        "tags":"",
        "category":"",
        "inStock":"",
        "availableStock":"",
        "created_at":""
    }
    ```
    

* **Sort Item for authenticated User** : `GET`

    Call this end point http://127.0.0.1:8000/api/item/getItem/?ordering="field_name"&filter=1 <br>
        this will return data in JSON format.
    >JSON data format:
   ```
    {
        "SKU":"",
        "name":"",
        "tags":"",
        "category":"",
        "inStock":"",
        "availableStock":"",
        "created_at":""
    }
    ```

#
