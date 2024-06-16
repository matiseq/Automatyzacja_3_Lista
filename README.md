# Automatyzacja Testów API

Ten skrypt automatyzuje testowanie endpointów API przy użyciu biblioteki requests. Wysyła żądania HTTP do wybranych publicznych API, sprawdza status odpowiedzi HTTP oraz weryfikuje obecność kluczowych elementów w odpowiedziach JSON.

## Jak używać

1. Upewnij się, że masz zainstalowany Python na swoim systemie.
2. Zainstaluj bibliotekę `requests`:
    ```sh
    pip install requests
    ```
3. Zapisz skrypt jako `api_test.py`.
4. Uruchom skrypt:
    ```sh
    python api_test.py
    ```

## Testowane Endpointy API

1. https://jsonplaceholder.typicode.com/posts/1
    - Sprawdzane klucze: `userId`, `id`, `title`, `body`
2. https://jsonplaceholder.typicode.com/users/1
    - Sprawdzane klucze: `id`, `name`, `username`, `email`
3. https://jsonplaceholder.typicode.com/comments/1
    - Sprawdzane klucze: `postId`, `id`, `name`, `email`, `body`

## Wyniki

Skrypt wyświetli wynik każdego testu w formacie:
- Test 1: PASSED
- Test 2: FAILED

## Zależności

- Python 3
- requests (biblioteka Python)

## Licencja

Projekt jest licencjonowany na warunkach licencji MIT.
