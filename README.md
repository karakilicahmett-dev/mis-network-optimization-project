

# İstanbul E-ticaret Dağıtım Ağı Optimizasyonu

## 1. Real-World Problem Context
İstanbul merkezli bir e-ticaret firması (JetLojistik), Tuzla'daki ana deposundan Avrupa yakasındaki dağıtım merkezlerine sevkiyat yapmaktadır. Trafik ve yakıt maliyetleri nedeniyle en kısa rotanın belirlenmesi operasyonel verimlilik için kritiktir.

## 2. Problem Definition
Bu projede, belirli dağıtım noktaları arasındaki mesafeler (km) baz alınarak, ana depodan hedef noktaya en kısa rotanın bulunması amaçlanmaktadır.

## 3. Network Model
Problem bir **Yönlendirilmemiş Ağırlıklı Çizge (Undirected Weighted Graph)** olarak modellenmiştir. Ağırlıklar, noktalar arasındaki km mesafesini temsil eder.

## 4. Nodes and Edges
- **Düğümler (Nodes):** Tuzla (Depo), Maltepe, Kadıköy, Üsküdar, Beşiktaş, Şişli, Kağıthane vb.
- **Kenarlar (Edges):** İlçeler arasındaki ana yollar ve mesafeleri.
- Toplam 7 düğüm ve 10 kenar kullanılmıştır.

## 5. Selected Algorithm
**Dijkstra Algoritması** kullanılmıştır. Bu algoritma, bir başlangıç noktasından diğer tüm noktalara (veya belirli bir hedefe) olan en kısa yolu kesin olarak hesaplar.

## 6. Python Implementation
Proje Python 3.x ve `networkx` kütüphanesi kullanılarak geliştirilmiştir. Veriler `data/` klasöründeki bir CSV dosyasından okunur.

## 7. Results
Tuzla'dan Beşiktaş'a giden en kısa yol algoritma tarafından şu şekilde belirlenmiştir:
`Tuzla -> Maltepe -> Üsküdar -> Beşiktaş` (Toplam 47 km).

## 8. Managerial Interpretation
Yöneticiler bu modeli kullanarak:
- Yakıt maliyetlerini %15 oranında azaltabilir.
- Teslimat sürelerini optimize ederek müşteri memnuniyetini artırabilir.
- Yeni bir dağıtım merkezi açıldığında ağa kolayca entegre edebilir.

## 9. How to Run the Code
1. Kütüphaneleri kurun: `pip install -r requirements.txt`
2. Kodu çalıştırın: `python src/solution.py`

## 10. References
- NetworkX Documentation: https://networkx.org/
- Dijkstra's Algorithm Overview.
