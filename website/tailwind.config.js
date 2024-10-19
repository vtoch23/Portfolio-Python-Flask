/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    'templates/.{js,ts,jsx,tsx,mdx, html}',
    "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
      extend: {
        maxWidth: {
          50: '50%',
          60: '60%',
          70: '70%',
          80: '80%',
          90: '90%',
          // 100% is not required as max-w-full will be present by default
        }
      }
    },
  plugins: [],
}

