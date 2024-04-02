const PLAYLIST_SYMBOLS_MAP = {"daily": "M64 128H0V64V0H64H128V64V128H64Z", "dejavu": "M0 0H128V128H107H86H65H0V63V42V21V0Z", "premiere": "M128 128H0V63V0H65H128V21V42V64V128Z", "stash": "M128 0H0V128H128V0Z"}

async function getIcon(name) {
  return { path: PLAYLIST_SYMBOLS_MAP[name.replace(/_/g,'-')] };
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
