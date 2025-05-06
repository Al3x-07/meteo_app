[app]

# Nome dell'applicazione
title = MeteoApp

# Nome del pacchetto (deve essere tutto minuscolo, senza spazi)
package.name = meteoapp

# Dominio (può essere anche org.tuinome, importante è che sia unico)
package.domain = org.barra

# Cartella dove si trova il tuo codice
source.dir = .

# File da includere nel pacchetto
source.include_exts = py,png,jpg,kv,atlas

# Versione dell'app
version = 1.0

# Orientamento dello schermo (portrait = verticale)
orientation = portrait

# Icona dell'app (facoltativa, puoi usare anche logo.png se vuoi)
# icon.filename = %(source.dir)s/logo.png

# Moduli Python richiesti
requirements = python3,kivy,requests,plyer

# Entry point dell'app
entrypoint = main.py

# Se vuoi testare su dispositivo USB
android.logcat_filters = *:S python:D

# Architettura Android (non toccare)
android.archs = armeabi-v7a, arm64-v8a

# Firma dell'app in debug
android.debug = 1

# Permessi richiesti per accedere al GPS e internet
android.permissions = INTERNET, ACCESS_COARSE_LOCATION, ACCESS_FINE_LOCATION

# Abilita il supporto al multitouch (consigliato)
android.features = android.hardware.touchscreen

# SDK minimo richiesto
android.minapi = 21

# SDK target (puoi alzarlo se vuoi)
android.target = 33

# SDK massimo (non impostato)
# android.maxapi =

# Disabilita la compilazione di codice Java (opzionale)
# android.disable_compile_time_resource_compression = 1

# Lingua predefinita
# presplash.filename = %(source.dir)s/logo.png

# Eventuali risorse extra da includere
# (qui puoi aggiungere altri file come immagini o suoni se servono)
# android.add_resources = assets/suono.wav

# (non toccare se non sai cosa fai)
[buildozer]
log_level = 2
warn_on_root = 1
