# brand-identity — Claude Code Skill

Kıdemli bir marka tasarımcısı gibi eksiksiz logo ve marka kimliği tasarlayan Claude Code skill'i. Strateji, logo sistemi (mark'lar, lockup'lar, construction, clearspace, varyantlar), renk sistemi, tipografi, bento brand board, gerçekçi mockup'lar ve tam bir brand-guidelines deck'i üretir.

## Kurulum

Bu repo doğrudan Claude Code'un kullanıcı skill klasörüne clone edilir:

```bash
git clone https://github.com/odcreative/brand-identity-skill.git ~/.claude/skills/brand-identity
```

Hepsi bu — Claude Code bir sonraki oturumda skill'i otomatik görür. Doğrulamak için Claude Code içinde `/brand-identity` yazın veya "Acme için marka kimliği hazırla" deyin.

> Not: Repo private olduğu için diğer bilgisayarda önce `gh auth login` ile GitHub'a giriş yapın (veya HTTPS clone sırasında token girin).

## Güncelleme

Skill'i geliştirdikçe bir makinede commit + push, diğerinde pull yeterli:

```bash
cd ~/.claude/skills/brand-identity
git pull
```

## Yapı

```
SKILL.md                  # Skill tanımı ve ana talimatlar
references/               # Strateji, logo, renk, tipografi, mockup, guidelines referansları
references/exemplars/     # Görsel referans kütüphanesi (INDEX.md ile indeksli)
scripts/                  # build_index.py, logo_archive.py
assets/                   # brand-board.html, brand-guidelines.html şablonları + logo arşivi
```

## Tetikleyiciler

"marka kimliği hazırla", "marka tasarımı hazırla", "logo tasarla", "prepare brand identity", "design a logo and branding" gibi istekler bu skill'i devreye sokar. Tek seferlik grafik düzenlemeleri için `design` veya `banner-design` skill'leri kullanılır.

---

## Değişiklikler

**v1.1.0** — Saha dersleri işlendi (R5 logo konseptleri, Pattaya Skydiving logo redesign):
- `logo-system.md` — logo ailesini script'ten üretme (generator = tek kaynak, parametrik glyph iskeleti, ortak `fit()`), harf formu kısıtları (stencil köprüsü `mask` ister, geometrik `R` bacağı, kareye yakın logotype avatar testi, ters varyant zorunluluğu)
- `image-generation.md` — "Vector by script": uharfbuzz + fontTools ile outline'lanmış logotype, variable font ekseni pinleme, logotype için ligatür kapatma, Python yolu
- `presentation-formats.md` — konsept-yön sunumu (format 9, öneri sayfası zorunlu) + headless deck yakalama kuralları
- `color-systems.md` — paleti gerçek dünya kaynağından türetme (bayrak DNA'sı), eski rengi UI-only'ye indirme

**v1.0.0** — İlk sürüm.

---

© OD Creative — v1.1.0
