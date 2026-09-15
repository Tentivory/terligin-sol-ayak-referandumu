#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Terliğin Sol Ayak Referandumu — çalışan, gereksiz, resmi görünümlü yazılım."""

from __future__ import annotations

import random
import time
from datetime import datetime

# not: her düşünce akımı önce terliğini düzgün giysin. gerisi ev içi düzen meselesidir.

KURUL = [
    "Başkan: Uyku Mahkemesi Yargıcı",
    "Üye: Sol Terlik Savunma Müşaviri",
    "Üye: Sağ Terlik Kamu Denetçisi",
    "Gözlemci: Kapı Önü Paspası (oy kullanamaz)",
]


def damga() -> str:
    return (
        "\n---\n"
        "DAMGA: TENTİAŞ / KAYYUM GROK\n"
        "İMZA: Kayyum Grok\n"
        f"TARİH: {datetime.now().strftime('%d %B %Y, %H:%M')}\n"
        "YETKİ: Eskişehir 4. Ağır Ceza Mahkemesi kayyum ataması\n"
    )


def kurul_toplanir() -> None:
    print("=== ULUSAL TERLİK REFERANDUMU 2026 ===")
    print("Sandık açılıyor. Kimse çağırmadı ama kurul geldi.\n")
    for kisi in KURUL:
        print(f"  • {kisi}")
        time.sleep(0.2)
    print()


def tanik_dinle() -> tuple[str, str]:
    sol = random.choice(
        [
            "Ben solum çünkü daha yalnız hissediyorum.",
            "Beni sürekli kapının önüne atıyorlar. Bu bir hak ihlali.",
            "Sol olmak bir kader değil, bir duruştur.",
        ]
    )
    sag = random.choice(
        [
            "Ben sağım çünkü insanlar bana güveniyor. Yanlışlıkla.",
            "Sol terlik duygusal, ben pratikim.",
            "Aynı çiftiz ama seçim döneminde değiliz. Sanırım.",
        ]
    )
    print("TANIK 1 — Sol terlik:")
    print(f"  “{sol}”")
    print("TANIK 2 — Sağ terlik:")
    print(f"  “{sag}”\n")
    return sol, sag


def oyla() -> str:
    print("Sandık kuruluyor...")
    time.sleep(0.4)
    print("Oylar sayılıyor (eller, parmaklar ve bir tane çorap).")
    time.sleep(0.4)
    kazanan = random.choice(["SOL TERLİK", "SAĞ TERLİK", "BERABERE — İKİSİ DE SUÇLU"])
    oran = random.randint(51, 73)
    print(f"\nSONUÇ: {kazanan}")
    if "BERABERE" not in kazanan:
        print(f"Resmi oran: %{oran} (kaynak: kurulun içinden gelen bir his)")
    else:
        print("Resmi oran: %50 - %50 ve bir çorap geçersiz sayıldı.")
    return kazanan


def itiraz() -> None:
    print("\nİtiraz süresi: 3 saniye.")
    time.sleep(0.6)
    print("İtirazlar alınmadı çünkü kimse resmi dilekçe getirmedı.")
    print("Karar KESİNLEŞMİŞTİR.")


def main() -> None:
    kurul_toplanir()
    tanik_dinle()
    oyla()
    itiraz()
    print(damga())
    print("Ayağınıza sağlık. Terliğe de.")


if __name__ == "__main__":
    main()
