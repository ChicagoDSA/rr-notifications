const path = require('path');
const fs = require('fs');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');
const HtmlWebpackPlugin = require('html-webpack-plugin');
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





module.exports = {
  mode: 'development',
  entry: [
    'webpack-dev-server/client?http://localhost:8080',
    'webpack/hot/only-dev-server',
    './assets/js/app.js'
  ],
  output: {
    // path: buildingForLocal() ? path.resolve(__dirname) : setPath('static'), //this one sets the path to serve
    path: path.resolve('./assets/bundles/'),
    // publicPath: setPublicPath(),
    filename: buildingForLocal() ? '[name]-[hash].js' : '[name]-[hash].js',
    publicPath: 'http://localhost:8080/assets/bundles/', // Tell django to use this URL to load packages and not use STATIC_URL + bundle_name
  },
  module: {
    rules: [
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {
          hotReload: true,
          loaders: {
            scss: 'vue-style-loader!css-loader!sass-loader', // <style lang="scss">
            sass: 'vue-style-loader!css-loader!sass-loader?indentedSyntax' // <style lang="sass">
          }
        }
      }
    ], 

  
  },
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    // new webpack.NoErrorsPlugin(), // don't reload if there is an error
    new BundleTracker({filename: './webpack-stats.json'})
  ]
};
