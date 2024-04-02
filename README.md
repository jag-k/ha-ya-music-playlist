[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg?style=for-the-badge)](https://github.com/hacs/integration)

# Yandex.Music Playlist Icons
Old-style icons of Yandex.Music Playlist in svg format HomeAssistant

## Инструкции
Чтобы добавить эти иконки в Home Assistant, нужно выполнить простые шаги:

1. Найти и установить в HACS **Yandex.Music Playlist Icons**
2. Добавьте этот код в configuration.yaml:

```yaml
frontend:
  extra_module_url:
    - /hacsfiles/ha-ya-music-playlist/ya-music-playlist.js
```
Или так:
```yaml
lovelace:
  resources:
    - url: /local/community/ha-ya-music-playlist/ya-music-playlist.js
      type: module  
```
Или так:
```yaml
lovelace:
  resources:
    - url: /hacsfiles/ha-ya-music-playlist/ya-music-playlist.js
      type: module  
```


А также можно через UI Home Assistant в ресурсах Lovelace

[![Open your Home Assistant instance and show your Lovelace resources.](https://my.home-assistant.io/badges/lovelace_resources.svg)](https://my.home-assistant.io/redirect/lovelace_resources/)
