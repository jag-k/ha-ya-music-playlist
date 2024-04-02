const PLAYLIST_SYMBOLS_MAP = require('./ya-music-playlist.min.json')

async function getIcon(name) {
  return {
    path: PLAYLIST_SYMBOLS_MAP[name.replace(/_/g,'-')],
    viewBox: "0 0 132 132"
  };
}

async function getIconList() {
  return Object.keys(PLAYLIST_SYMBOLS_MAP).map(icon => ({name: icon}));
}

if (!window.frontendVersion || window.frontendVersion <= 20211027.0){
  window.customIconsets = window.customIconsets || {};
  window.customIconsets["ya-music-playlist"] = getIcon;
} else {
  window.customIcons = window.customIcons || {};
  window.customIcons["ya-music-playlist"] = { getIcon, getIconList };
}
