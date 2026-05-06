# Ýstanbul E-ticaret Lojistik Optimizasyonu

## 1. Real-World Problem Context
Ýstanbul'daki bir e-ticaret deposunun (Tuzla) çevre ilçelere en verimli þekilde ürün ulaþtýrmasý hedeflenmektedir.

## 2. Problem Definition
Amaç, depo ile hedef nokta arasýndaki en kýsa yolu (minimum mesafe) bularak yakýt ve zaman tasarrufu saðlamaktýr.

## 3. Network Model
Problem, ilçelerin 'düðüm', yollarýn ise 'kenar' olduðu bir 'Weighted Undirected Graph' modelidir.

## 4. Nodes and Edges
Düðümler: Tuzla, Maltepe, Kadýköy, Üsküdar, Beþiktaþ, Þiþli, Kaðýthane vb.
Kenarlar: Ýlçeler arasý baðlantý yollarý (KM cinsinden mesafeler).

## 5. Selected Algorithm
Dijkstra Algoritmasý kullanýlarak en kýsa yol hesaplanmýþtýr.

## 6. Python Implementation
Python 3 ve NetworkX kütüphanesi kullanýlmýþtýr. Veriler bir CSV dosyasýndan dinamik olarak okunur.

## 7. Results
Tuzla-Beþiktaþ arasý en kýsa rota baþarýyla hesaplanmýþ ve grafik olarak sonuç alýnmýþtýr.

## 8. Managerial Interpretation
Bu model sayesinde lojistik maliyetleri düþürülebilir ve teslimat süreleri tahmin edilebilir hale gelir.

## 9. How to Run the Code
`python src/solution.py` komutu ile çalýþtýrýlabilir.

## 10. References
NetworkX Documentation (https://networkx.org/)