# Secret Notes Uygulaması

Bu uygulama, kullanıcıların başlık ve gizli notlarını şifreleyerek saklamalarına ve daha sonra bu notları çözmelerine olanak tanır.

## Gereksinimler

- Python 3.x kurulu olmalıdır.
- Gerekli kütüphaneler (`tkinter`, `PIL`, `cryptography`) yüklü olmalıdır.

## Kurulum

1. Depoyu klonlayın veya dosyaları indirin.
2. Python ortamınızı hazırlayın.
3. Uygulamayı başlatmak için `python secret_notes.py` komutunu kullanın.

## Kullanım

- **Enter Your Title**: Şifrelenmiş notunuz için bir başlık girin.
- **Enter Your Secret**: Gizli notunuzu yazın.
- **Enter Master Key**: Şifreleme ve çözme için bir anahtar girin.
- **Save and Encrypt** düğmesine basarak notunuzu şifreleyin ve kaydedin.
- **Decrypt** düğmesine basarak şifreli notunuzu (şifrelenmiş not textbox'a yazılmış olmalıdır) çözün.

## Önemli Notlar

- Her notun şifresini çözmek için doğru anahtar gerekir.
- Anahtarların güvenliğinden emin olun; kaybolması notlarınızın kalıcı olarak kaybolmasına neden olabilir.
