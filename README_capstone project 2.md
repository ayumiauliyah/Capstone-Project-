# Capstone Project 2 : Analisis Airbnb Bangkok

## Latar Belakang
Thailand menempati daftar destinasi internasional yang menawarkan pengalaman lengkap mulai dari budaya, alam dan suasananya. Oleh karena itu, Airbnb memiliki peran penting untuk mendukung pelayanan akomodasi yang nyaman dan terjangkau. Bagaimanapun, seiring bertumbuhnya listings di Bangkok, perlu adanya analisis agar listings dapat mengoptimalisasi dalam meningkatkan occupancy rate dan pendapatan. Analisis ini akan meliputi beberapa faktor seperti area listings (neighbourhood), tipe kamar, keyword fasilitas serta transportasi, seasonal trend, persyaratan minimum dalam menginap, dan bahasa yang ditampilkan pada listings.

## Business Stakeholders
Airbnb Host atau pemiliki properti yang menyewakan akomodasi melalu Airbnb dan bertanggung jawab atas kenyamanan tamu

## Masalah yang akan dianalisis
Strategi peningkatan occupancy rate listing Airbnb Bangkok. Oleh karena itu, berikut beberapa hal yang akan dianalisis:

1. Area Listings : Bagaimana cara agar harga listings dapat bersaing dan memberikan harga wajar dibanding dengan listing lainnya?

2. Tipe Kamar : Apa tipe kamar yang diminati oleh wisatawan? 

3. Keyword Fasilitas dan Transportasi : Jenis fasilitas dan transportasi apa yang meninggalkan kesan bagi wisatawan dan bagaimana dampaknya terhadap occupancy rate?

4. Seasonal Trend : Kapan banyaknya wisatawan berkunjung ke Bangkok (high season dan low season)?

5. Minimum Nights Required :  Bagaimana preferensi wisatawan Bangkok (short-term stay atau long-term stay)?

6. Bahasa yang ditampilkan : Bagaimana dampak bahasa yang ditampilkan di listings terhadap occupancy rate dan kesan wisatawan?

## Pemahaman Data
Dataset ini berisi informasi terkait Airbnb Listings di Bangkok. Ada 17 kolom dalam dataset Airbnb Listings Bangkok, yaitu:

- id : kode unik listing Airbnb
- name : nama listing
- host_id : kode unik untuk host Airbnb
- host_name : nama host. biasa hanya ditulis nama depan
- neighbourhood : nama daerah di Bangkok
- latitude : garis lintang yang diukur menggunakan proyeksi sistem geodetic dunia (WGS84)
- longitude: garis bujur yang diukur menggunakan proyeksi sistem geodetic dunia (WGS84)
- room_type : tipe kamar yang ada pada listing Bangkok
- price : harga listing Airbnb perhari (Thai bhat)
- minimum_nights : jumlah minimum malam untuk menginap di listing tersebut
- number_of_reviews : banyaknya review yang dimiliki oleh listing
- last_review : tanggal review terbaru
- reviews_per_month : review per bulan
- calculated_host_listings_count : Jumlah listing yang dimiliki host dalam geografi kota/wilayah
- availability_365 : Jumlah hari daftar tersedia dalam 365 hari ke depan
- number_of_reviews_ltm : banyaknya review yang dimiliki oleh listing (12 bulan terakhir)
- occupancy_rate : tingkat occupancy rate listing dalam persen

## Kesimpulan dan Rekomendasi
**Area** 

Kesimpulan:
1. Area dengan kepadatan wisatawan yang lebih tinggi (higher occupancy rate) memiliki tantangan dalam mempertahankan performa listings dengan menawarkan harga yang baik (tidak overprice atau underprice). Listings harus memiliki fitur menarik seperti pengalaman yang unik maupun fasilitas yang ditingkatkan untuk menarik wisatawan.

2. Area dengan occupancy rate yang lebih rendah memiliki kesempatan lebih untuk meningkatkan performa melalui penawaran harga yang terjangkau dengan lingkungan yang dapat menjadi daya tarik dalam berwisata. Area ini dapat menjangkau segmen low-budget traveler di Bangkok.

Rekomendasi:

Host dapat mengkaji ulang harga, baik melihat rata - rata harga area sendiri maupun rata - rata harga area lain (termasuk seberapa dekat dengan area wisata) agar dapat menawarkan harga yang kompetitif

**Tipe Kamar**

Kesimpulan:

Bagi group traveler:

1. Tipe kamar yang paling diminati oleh wisatawan adalah entire home/apt. Kemungkinan besar wisatawan yang pergi ke Bangkok adalah grup sehingga entire home/apt menjadi pilihan akomodasi yang pas. Selain itu, entire home/apt juga memiliki beberapa variasi penginapan dalam persyaratan minimum nights sehingga group-traveler dengan short-term maupun long-term terakomodasi dengan baik. Oleh karena itu, jika entire home/apt dapat tetap pada standar rata - rata harga yang ada, akan terus menjadi akomodasi unggulan bagi wisatawan bangkok.

Bagi solo-traveler:

2. Pilihan akomodasi bagi solo traveler adalah hotel room, private room, dan shared room (berdasarkan persyaratan maksimal person pada umumnya). Dalam hal ini, hotel room memiliki rata - rata harga yang lebih rendah dengan fleksibilitas persyaratan minimum nights (1-3 hari) dibandingkan dengan private room sehingga mencapai occupancy rate yang lebih tinggi.

3. Shared room merupakan akomodasi yang linear antara rata - rata harga yang jauh lebih rendah dengan occupancy rate yang rendah pula. Hal ini disebabkan oleh segmentasi wisatawan solo traveler, khususnya backpacker yang mau bersosialisasi dengan wisatawan lainnya. Akomodasi ini memiliki keunggulan dan pasar tertentu dibandingkan jenis akomodasi lainnya.

Rekomendasi:

Berdasarkan analisis tipe kamar ini, maka harga dan fleksibilitas dalam memilih minimum malam inap merupakan hal yang harus diperhatikan untuk meningkatkan occupancy rate di keempat tipe kamar.

**Keyword**

Kesimpulan:

1. Berdasarkan grafik, rata - rata harga listings akan meningkat jika ada keyword MRT, wifi, kitchen, dan breakfast

2. Kesan dalam pengalaman tamu yang menginap paling tinggi ditunjukkan jika listings memiliki kata kunci pools atau kolam renang. Lalu kata kunci yang linear terhadap rata - rata harga yang lebih tinggi adalah MRT, wifi, dan kitchen. Lalu, untuk kesan lainnya diberikan pada penginapan dengan keyword airport, BTS, boat, station, AC, dan spa.

3. Occupancy rate yang lebih tinggi ditujukan pada penginapan yang memiliki key word MRT dan wifi meskipun dengan rata - rata yang lebih tinggi pula. Selain itu, BTS, SRT, trains, bus, buses, dan public transport juga memiliki occupancy rate yang lebih tinggi dibandingkan listings yang tidak menampilkan keyword tersebut. Keyword fasilitas seperti gym, beach, dan pools juga berperan penting dalam meningkatkan occupancy rate.

Jadi,
- Keyword MRT dan wifi adalah hal yang paling signifikan dalam meningkatkan occupancy rate meskipun dengan rata - rata harga yang lebih tinggi
- Wisatawan memerhatikan kenyamanan dalam bertransportasi di Bangkok seiring meningkatkanya occupancy rate pada penginapan yang memiliki keyword transportasi umum
- Keyword pools atau kolam renang mendapatkan banyak kesan bagi wisatawan yang juga terbukti pada tingkat occupancy rate lebih tinggi dibandingkan yang tidak memiliki keyword tersebut

Rekomendasi:

Listings dapat menambahkan keyword fasilitas yang ada dan transportasi umum yang relevan guna meningkatkan occupancy rate

**Seasonal trend**

Kesimpulan:

1. Banyaknya tamu meningkat dimulai di bulan November dan mengalami peak season di bulan Desember. Hal ini disebabkan oleh libur akhir tahun sehingga wisatawan banyak datang berkunjung. Sedangkan, low season terjadi di Bulan Januari - September.
2. Rata - rata harga listings terlihat fluktuatif di setiap bulannya dengan harga paling tinggi berada pada bulan Februari, diikuti oleh bulan September.

Rekomendasi:

- Pada bulan peak season, occupancy rate memiliki kemungkinan lebih besar untuk meningkat seiring jumlah wisatawan yang tinggi. Listings dapat meningkatkan harga yang lebih tinggi dan kompetitif karena demand meningkat. 
- Pada bulan low season, dengan sedikitnya wisatawan yang berkunjung, maka daya tarik listings akan dilihat dengan penawaran harga dan promosi yang menarik, seperti diskon harga, diskon lebih ketika menginap lebih lama, free-breakfast, dan service lainnya. 
- Host harus mengevaluasi dan menyesuaikan dengan kondisi season yang berubah - ubah untuk meningkatkan occupancy rate

**Minimum Nights Required**

Kesimpulan:

1. Berdasarkan banyaknya minimum nights yang disyaratkan oleh host, occupancy rate tertinggi berada pada 1-2 bulan untuk short-term stay dan 2 weeks untuk long-term stay
2. Short-term stay traveler memilih 2 weeks karena memiliki harga lebih rendah dibandingkan listings dengan persyaratan minimum 1 week atau 3 weeks
3. Grafik juga menunjukkan long-term stay traveler lebih memilih untuk book listings dengan minimum persyaratan 1-2 bulan dibandingkan dengan listings dengan minimum 3-4 bulan atau 4 bulan lebih karena harga yang lebih rendah. Walaupun 3 bulan memiliki harga lebih rendah dibandingkan listing long-term stay lainnya, occupancy rate tidak lebih tinggi. Oleh karena itu, informasi yang dapat disimpulkan adalah pada saat ini traveler dominan untuk tinggal di listings yang sama 1-2 bulan. 

Rekomendasi:

- Host perlu mengevaluasi harga penginapan untuk short-term stay listing agar lebih kompetitif dan bisa meningkatkan occupancy rate
- Host perlu mengevaluasi minimum nights required untuk long-term stay listing agar wisatawan lebih fleksibel dan bisa meningkatkan occupancy rate

**Bahasa yang digunakan**

Kesimpulan:

1. Nama listings yang menggunakan bahasa Inggris lebih banyak dibandingkan dengan bahasa non-inggris. Rata - rata jumlah review nama listings yang menggunakan bahasa Inggris juga lebih banyak
2. Rata - rata harga dan rata - rata occupancy rate nama listings yang tidak menggunakan bahasa inggris lebih tinggi sehingga nama listings yang menggunakan bahasa Inggris tidak selalu lebih ramai dibandingkan nama listings yang digunakan dengan bahasa non-Inggris. 

Rekomendasi:

- Host dapat memberikan keterangan yang lengkap baik bahasa inggris maupun bahasa lokal untuk menjangkau pasar internasional dan domestik yang lebih luas
- Meskipun nama listings tidak sepenuhnya menggunakan bahasa Inggris, dapat dilihat bahwa banyak listings tetap mengkombinasikannya dengan bahasa Ingrris sehingga masih dapat dimengerti banyak orang. banyak listings keterangan dan dokumen pendukung seperti foto listings juga menjadi daya tarik tersendiri bagi wisatawan untuk memutuskan menginap

Note:

Link Tableau Public : https://public.tableau.com/views/AirbnbBangkokAnalysis_17645148705180/Dashboard2?:language=en-GB&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link

Link Canva : https://www.canva.com/design/DAG5-S0-JIE/hp_fE3q8pXm7R4-onwHUjQ/edit?utm_content=DAG5-S0-JIE&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
