# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. 

### Permasalahan Bisnis
Dibalik dari semua keindahan yang ada pada Jaya Jaya Institute, terdapat masalah seperti terdapat beberapa siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. 

### Cakupan Proyek
1. Menganalisis faktor penyebab dropout siswa.
2. Membuat model machine learning yang dapat digunakan untuk prediksi sederhana yang dapat di akses online.
3. Membangun dashboard menggunakan metabase untuk analisis penyebab terjadinya dropout

### Persiapan

Sumber data: [students_performance](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

Setup environment:
```
pip install -r requirements.txt
```
*menginstall library yang diperlukan*

```
streamlit run app.py
```
*menjalankan model menggunakan streamlit*





## Business Dashboard
![Dashboard Image](https://github.com/rezaafaisal/dropout-classification/raw/main/dashboard.png "Dashboard")

Dashboard yang dibuat merupakan salah satu solusi untuk mengatasi tingginya jumlah dropout pada Jaya Jaya Institute, dengan menampilkan data yang memiliki korelasi terhadap dropout siswa seperti :
- Rata-rata nilai siswa setiap semester
- Siswa termasuk penerima beasiswa atau tidak
- Apakah biaya kuliah sesuai dengan keadaan saat ini
- Apakah siswa termasuk orang yang mengungsi
- Apakah jurusan mempengaruhi tingkat dropout

Pada bagian atas terdapat data kuantitatif terkait massa siswa yang dropout dan berapa persetanasenya, siswa yang lulus, dan siswa yang sedang berlangsung belajar mengajarnya 

Dibawahnya terdapat grafik bar yang menunjukkan bahwa nilai rata-rata siswa sangat mempengaruhi tingkat dropout siswa, dan nilai yang lebih tinggi cenderung akan selesai atau lulus.

Disampingnya terdapat grafik donat yang menampilkan persentase siswa yang mendapatkan beasiswa antara yang dropout, yang lulus maupun yang sedang bersekolah dan terlihat jelas jika dibandingkan antara yang lulus dan dropout, sisawa yang mendapatkan beasiswa kemungkinan besar tidak ada dropout.

Sedangkan dibawahnya lagi terdapat 2 grafik donat yang menunjukan apakah siswa yang tidak mendapatkan biaya kuliah sesuai dengan keadaan saat ini dan siswa yang tidak mengungsi cenderung dropout.

Grafik bar horizontal yang mnunjukakan daftar jurusan dan persentase dropout siswanya dengan peringkat pertama diduduki oleh Biofuel Production Technologies kemudian selanjutnya.


## Menjalankan Sistem Machine Learning


```

```

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
