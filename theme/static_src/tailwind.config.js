module.exports = {
  content: [
    "../templates/**/*.html",
    "../../**/*.html",
    "../../**/*.py",
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('daisyui'),
  ],
}
