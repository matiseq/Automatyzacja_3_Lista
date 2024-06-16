# Automatyzacja procesów z wykorzystaniem Makefile

Ten projekt demonstruje automatyzację procesów testowania i uruchamiania aplikacji za pomocą Makefile.

## Struktura projektu

- `app.py`: Prosta aplikacja z funkcją dodawania dwóch liczb.
- `test_app.py`: Testy jednostkowe dla aplikacji.
- `Makefile`: Plik Makefile automatyzujący procesy.
- `requirements.txt`: Plik z zależnościami (w naszym przypadku pusty).

## Jak używać

1. Instalacja zależności:
    ```sh
    make install
    ```

2. Uruchamianie testów jednostkowych:
    ```sh
    make test
    ```

3. Uruchamianie aplikacji:
    ```sh
    make run
    ```

## Zależności

- Python 3
- unittest (standardowa biblioteka Pythona)

## Licencja

Projekt jest licencjonowany na warunkach licencji MIT.
