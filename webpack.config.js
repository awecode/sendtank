const webpack = require('webpack');
const ExtractTextPlugin = require("extract-text-webpack-plugin");

const path = require('path');
const resolve = path.resolve.bind(path, __dirname);
const dev_path = resolve('static/dist_dev/');
const prod_path = resolve('static/dist/');
let output;

output = {
  path: dev_path,
  filename: 'js/[name].js',
  publicPath: '/static/dist/'
};

if (process.env.NODE_ENV === 'production') {
  output['path'] = prod_path;
  output['publicPath'] = 'https://cdn.awecode.com/sendtank/dist/';
}

let commonsPlugin = new webpack.optimize.CommonsChunkPlugin({name: 'common', filename: 'js/common.js'});

module.exports = {
  entry: {
    // landing: "./src/landing.js",
    app: "./src/main.js",
    // dashboard: "./src/dashboard.js",
  },
  output: output,
  module: {
    rules: [
      {
        test: /\.s?css$/,
        use: ExtractTextPlugin.extract({
          fallback: "style-loader",
          use: "css-loader!sass-loader"
        })
      },
      {test: /\.woff(2)?(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: "url-loader?limit=10000&mimetype=application/font-woff"},
      {test: /\.(ttf|eot|svg)(\?v=[0-9]\.[0-9]\.[0-9])?$/, loader: "file-loader"}
    ]
  },
  plugins: [
    commonsPlugin,
    new ExtractTextPlugin({filename: 'css/[name].css', allChunks: true}),
  ]
};