// Code sourced from "Unleashing the Power of React.js for Chrome Extension Development"
// Article by Integri Solutions: https://dev.to/integridsolutions/unleashing-the-power-of-reactjs-for-chrome-extension-development-3kij
//modified for my needs

const path = require("path");
const CopyPlugin = require("copy-webpack-plugin");
const HtmlPlugin = require("html-webpack-plugin");
// const tailwindcss = require("tailwindcss");
const autoprefixer = require("autoprefixer");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const Dotenv = require('dotenv-webpack');

module.exports = {
  entry: {
    popup: path.resolve("src/popup/index.js")
},

  mode: "production",
  module: {
    rules: [
      {
        test: /\.js?$/,
        use: [
          {
            loader: "babel-loader",
            options: {
                presets: ["@babel/preset-env", "@babel/preset-react"],
            },
          },
        ],
        exclude: /node_modules/,
      },
      {
        test: /\.css$/i,
        use: [
            "style-loader",
            {
                loader: "css-loader",
                options: {
                    importLoaders: 1,
                }
            }]
          }
      
    ],
  },    
  plugins: [
    // new Dotenv(),
    new CleanWebpackPlugin({
        cleanStaleWebpackAssets: false,
    }),
    new CopyPlugin({
        patterns: [
            {
                from: path.resolve("src/static"),
                to: path.resolve("dist"),
            },
        ],
    }),
    ...getHtmlPlugins(["popup"]),
],
  
  resolve: {
    extensions: [".tsx", ".ts", ".js"],
  },
  output: {
    filename: "[name].js",
    path: path.resolve(__dirname,  "dist"),
  },
};




function getHtmlPlugins(chunks) {
    return chunks.map(
        (chunk) =>
            new HtmlPlugin({
                title: "Chrome Extension with ReactJs",
                filename: `${chunk}.html`,
                chunks: [chunk],
            })
    );
}