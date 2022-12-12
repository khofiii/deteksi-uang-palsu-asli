# deteksi-uang-palsu-asli
mendeteksi uang asli atau uang palsu dengan yolov4 

Untuk menjalankan nya siapkan aplikasi anconda dan vsc
setelah di download buka anaconda prompt
ketik code ni:
code .

setelah itu akan langsung masuk ke aplikasi vsc setelah di vsc 
1. klik terminal (buat terminal baru dengan format cmd)
2. setelah itu buat environment baru dengan code:
   conda create -n "deteksi" python==3.9
3. nanti akan akan ada pilihan [y/n]
   ketik saja y terus enter
4. aktifkan environtment yang tadi sudah di baut dengan cara ketikan code ini:
   conda activate deteksi
5. setelah itu instal opencv,flask, dan numpy dengan cara ketikan code:
   pip install opencv-python
   pip install flask
   pip install numpy
6. setelah itu jalankan programnya dengan cara ketikan code ini :
   pyhton app.py
7. setelah itu cari tulisan "http://127.0.0.1:5000"
   salin tulisan tersebut, setelah itu paste ke browser. Untuk berhenti klik Ctrl+C 
selamat program sudah di jalankan.

Bonus: 
di folder ada folder bernama real_time_yolo.py
silahkan klik file tersebut setelah itu run dengan python dan jangan lupa untuk menginstall opencv serta flask.
codingan ini bisa mendeteksi uang asli dan uang palsu secara live. Kelemahan nya adalah fps nya masih kecil jadi harus menunggu.
