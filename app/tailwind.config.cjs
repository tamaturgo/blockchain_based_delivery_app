/** @type {import('tailwindcss').Config}*/
const config = {
    content: ["./src/**/*.{html,js,svelte,ts}"],

    theme: {
        colors: {
            'background': '#ECECEC',
            'black-text': '#000',
            'blue-primary': '#01A0C7',
            'yellow-primary': '#FEC901'
        },
        extend: {},
    },

    plugins: [],
};

module.exports = config;
