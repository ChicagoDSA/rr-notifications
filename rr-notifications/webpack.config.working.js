const path = require('path');
const fs = require('fs');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const NODE_ENV = process.env.NODE_ENV;

const setPath = function(folderName) {
  return path.join(__dirname, folderName);
}

const buildingForLocal = () => {
  return (NODE_ENV === 'development');
};

const setPublicPath = () => {
  let env = NODE_ENV;
  if (env === 'production') {
    return 'https://your-directory/production/';
  } else if (env === 'staging') {
    return 'https://your-directory/staging/';
  } else {
    return '/';
  }
};

// const extractHTML = new HtmlWebpackPlugin({
//   title: 'History Search',
//   filename: 'index.html',
//   inject: true,
//   template: setPath('/src/tpl/tpl.ejs'),
//   minify: {
//     removeAttributeQuotes: true,
//     collapseWhitespace: true,
//     html5: true,
//     minifyCSS: true,
//     removeComments: true,
//     removeEmptyAttributes: true
//   },
//   environment: process.env.NODE_ENV,
//   isLocalBuild: buildingForLocal(),
//   imgPath: (!buildingForLocal()) ? 'assets' : 'src/assets'
// });





module.exports = {
  mode: 'development',
  entry: [
    './assets/app.js'
  ],
  output: {
    // path: buildingForLocal() ? path.resolve(__dirname) : setPath('static'), //this one sets the path to serve
    path: path.resolve('./assets/webpack_bundles/'),
    // publicPath: setPublicPath(),
    filename: buildingForLocal() ? '[name]-[hash].js' : '[name]-[hash].js'
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader'
      }
    ]
  },
  plugins: [
    new BundleTracker({filename: './webpack-stats.json'})
  ]
};
