# SQL Alchemy - Materialize Example

## Run the example

1. Install requirements in a virtual environment.

    ```
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. Create a `.env` file to connect to Materialize. Here is an example:

    ```
    export MZ_HOST=<id>.<region>.aws.materialize.cloud
    export MZ_USER=chuck@materialize.com
    export MZ_PASSWORD=<app password>
    export MZ_PORT=6875
    export MZ_DB=materialize
    export MZ_CLUSTER=chuck
    export MZ_SCHEMA=public
    export MZ_TRANSACTION_ISOLATION=serializable
    ```

3. Create a table in Materialize (e.g. from the Console SQL Shell).

    ```
    create table t (id int, content text);
    insert into t values (1, 'hi'), (2, 'hello');
    ```

4. Run the application.

    ```
    python app.py
    ```
    Output:
    ```
    ID: 1
    Content: 'hi'


    ID: 2
    Content: 'hello'
    ```