# Breakout Denemem

Python ve Pygame ile geliştirilmiş tek oyunculu Breakout (tuğla kırma) oyunu.

## Özellikler
- Çubuk kontrolü (Ok tuşları veya WASD)
- Çarpışma tespiti (top-çubuk, top-tuğla, top-duvar)
- Kazanma/kaybetme durumu
- R tuşu ile yeniden başlatma

## Nasıl çalıştırılır
1. Python ve Pygame kurulu olmalı: `pip install pygame`
2. `python breakout.py` ile çalıştır

## Kontroller
- Sol/Sağ ok veya A/D: Çubuğu hareket ettir
- R: Yeniden başlat

## Kullanılan kavramlar
- Game loop (event kontrolü → güncelleme → çizim → framerate sınırlama)
- Pygame Rect ve collision detection (`colliderect`)
- Klavye girdisi yönetimi (`pygame.key.get_pressed()`, `KEYDOWN` olayları)
- Liste yönetimi (tuğlaların dinamik olarak oluşturulması/kaldırılması)
- Koşullu durum yönetimi (oyun bitti/kazandı/kaybetti mantığı)
- Font render etme ve metin konumlandırma