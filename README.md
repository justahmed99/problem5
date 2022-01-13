# Petunjuk Penggunaan dan Dokumentasi Software Swiching Vendor API (Problem 2)

## Dibuat oleh :
Ahmad Mujahid Abdurrahman (ahmadm.abdurrahman@gmail.com)

## Penginstalan Environment dan Dependensi
- Pastikan bahwa Python 3 dan pip sudah terinstal terlebih dahulu.
- Masukkan terminal / cmd pada root path dari folder project
- Untuk membuat environment, gunakan perintah berikut :
    ```bash
    python -m venv env
    ``` 
- Jika sudah terdapat folder **env** pada folder project, artinya environment telah berhasil dibuat.
- Untuk mengaktifkan environment, gunakan perintah :
    - Pada Windows, gunakan perintah :
        ```powershell
        .\env\Script\activate 
        ```
    - Pada Linux / Mac, gunakan perintah :
        ```bash
        source env/bin/activate
        ```
- Untuk menginstal dependensi, gunakan perintah :
    ```bash
    pip install -r requirement.txt
    ```
- Untuk menonaktifkan environment setelah selesai simulasi, gunakan perintah :
    ```bash
    deactivate
    ```

## Catatan Tentang Vendor dan File Konfigurasinya

### Penjelasan Tentang Vendor
File konfigurasi vendor pada project ini terdapat pada script **app/config.toml**.

Vendor yang digunakan pada simulasi ini adalah Twilio. Terdapat 2 vendor yang dideskripsikan, yaitu :
- Twilio 1
- Twilio 2

Keterbatasan dari simulasi ini adalah tidak dapat menambahkan kontak dikarenakan menggunakan akun Twilio Trial. Jika penguji ingin menambahkan akun Twilio berbayar, penguji dapat menambahkannya di file **app/config.toml**.

### Cara Menambahhkan Vendor
Untuk menambahkan vendor pada file **app/config.toml**, Anda dapat menggunakan format :
```toml
[[vendor]]
    id = "{id_vendor}" # input sesuai keinginan untuk pembeda antar vendor
    name = "{nama_vendor}" # input sesuai keinginan untuk pembeda antar vendor 
    twilio_sid = "{twilio_account_sid}"
    twilio_auth_token = "{twilio_auth_token}"
    twilio_number = "{twilio_number}"
```
**Contoh** pengaturan vendor pada file **app/config.toml**:
```toml
[[vendor]]
    id = "twilio1"
    name = "Twilio 1"
    twilio_sid = "{twilio_account_sid}"
    twilio_auth_token = "{twilio_auth_token}"
    twilio_number = "{twilio_number}"
[[vendor]]
    id = "twilio2"
    name = "Twilio 2"
    twilio_sid = "{twilio_account_sid}"
    twilio_auth_token = "{twilio_auth_token}"
    twilio_number = "{twilio_number}"
```

## Menjalankan program
- Untuk menjalankan program, gunakan perintah :
    ```bash
    python app/app.py
    ```

## Dokumentasi Project
Untuk mendapatkan daftar dan dokumentasi dari API project ini, kita dapat melihatnya pada halaman Swagger UI dengan URL :

http://localhost:5000/swagger atau http://127.0.0.1:5000/swagger

Terdapat 4 buah API pada project ini, yaitu :
- POST http://localhost:5000/send atau http://127.0.0.1:5000/send (digunakan untuk percobaan pengiriman pesan).
- POST http://localhost:5000/register atau http://127.0.0.1:5000/register (digunakan untuk menambakan kontak baru) **NOTE : Premium Twilio account only**.
- POST http://localhost:5000/switch atau http://127.0.0.1:5000/switch (digunakan untuk mengubah vendor yang digunakan).

Untuk mendapatkan Postman collection, dapat dengan menimport file **Problem 5.postman_collection.json** atau melalui link https://documenter.getpostman.com/view/6648039/UVXhqGkQ.

## Unit Test

Ada beberapa langkah yang perlu dilakukan untuk melakukan unit test, yaitu :
- Pastikan program utama sudah berjalan.
- Script yang digunakan untuk melakukan unit test adalah **app/app_test.py**.
- Untuk menjalankan script, gunakan perintah :
    - Jika prompt terminal / CMD berada di root path project :
        ```
        python unittest -m app.app_test
        ```
    - Jika prompt terminal / CMD  berada dalam folder **app** :
        ```
        python unittest -m app.app_test
        ```

## Catatan Penting dalam Menajalankan Program

Jika Anda menggunakan sistem operasi Linux atau Mac, mungkin Anda akan mendapatkan **error** ketika mengeksekusi perintah **python** pada terminal. Gunakan perintah **python3** jika mendapatkan error pada saat menjalankan program.

Hal ini dikarenakan umumnya pada Linux ata Mac, perintah untuk menjalankan script program Python 3 dieksekusi melalui perintah **python3**.

## Hasil Simulasi Vendor

### Dengan menggunakan Twilio
![Twilio Image](./src/twilio.jpeg)
