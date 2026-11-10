
/* =========================================
   TOTE STUDIO — ARTWORK CATALOGUE
   ========================================= */

// 1. HOW MANY IMAGES?
const BACKGROUNDS = 28;
const BORDERS = 7;
const STICKERS = 10;

// 2. DEFAULT FILE EXTENSIONS
const DEFAULT_EXTENSIONS = {
  backgrounds: "jpg",
  borders: "png",
  stickers: "png"
};

// 3. INDIVIDUAL FILE EXCEPTIONS
// Only list images that differ from the default.
// Examples:
// backgrounds: { 5: "png", 12: "webp" }
// borders: { 3: "jpg" }

const FILE_EXCEPTIONS = {
  backgrounds: {},
  borders: {},
  stickers: {}
};

// 4. GENERATE THE ARTWORK CATALOGUE
function makeArtwork(kind, count) {
  return Array.from({ length: count }, (_, i) => {
    const number = i + 1;

    const extension =
      FILE_EXCEPTIONS[kind][number] ||
      DEFAULT_EXTENSIONS[kind];

    return {
      id: `numbered-${kind}-${number}`,
      name: `${kind} ${number}`,
      category: "All",
      src: `assets/${kind}/${number}.${extension}`
    };
  });
}

window.TOTE_ASSETS = {
  backgrounds: makeArtwork("backgrounds", BACKGROUNDS),
  borders: makeArtwork("borders", BORDERS),
  stickers: makeArtwork("stickers", STICKERS)
};
