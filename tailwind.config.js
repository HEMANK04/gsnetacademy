/** Tailwind build config — see BUILD-CSS.txt for how to regenerate the CSS. */
module.exports = {
  content: ["./*.html", "./js/**/*.js"],
  theme: {
    extend: {
      colors: {
        navy: { 50:"#eef2f9",100:"#d6e0ef",200:"#adc0df",300:"#7893c4",400:"#456aa8",500:"#1f4585",600:"#143166",700:"#0f2551",800:"#0b1c3f",900:"#08152f",950:"#050d1e" },
        gold: { 50:"#fff9ec",100:"#fff0cd",200:"#ffdf95",300:"#ffc85c",400:"#ffb020",500:"#f59e0b",600:"#d97b06",700:"#b45a09",800:"#92460e",900:"#783a0f" },
        cream: "#fdfaf3",
        brick: "#b4232a",
      },
      fontFamily: {
        sans: ['"Plus Jakarta Sans"', '"Tiro Devanagari Hindi"', "system-ui", "sans-serif"],
        display: ['"Barlow Condensed"', '"Tiro Devanagari Hindi"', "sans-serif"],
      },
      boxShadow: {
        card: "0 1px 2px rgba(8,21,47,.05), 0 8px 24px -12px rgba(8,21,47,.18)",
        lift: "0 24px 48px -24px rgba(8,21,47,.35)",
      },
      opacity: { 6:".06",7:".07",8:".08",12:".12",15:".15",45:".45",65:".65",85:".85",92:".92" },
    },
  },
  plugins: [],
};
