const path = require('path')
const BundleTracker = require('webpack-bundle-tracker')

const DEPLOYMENT_PATH = '/frontend/dist/'

module.exports = {
  publicPath: DEPLOYMENT_PATH,
  runtimeCompiler: true, // See: https://vuejs.org/v2/guide/installation.html#Runtime-Compiler-vs-Runtime-only
  devServer: {
      writeToDisk: true, // Write files to disk in dev mode, so Django can serve the assets
      headers: {
        'Access-Control-Allow-Origin': '*',
      },
    },
  transpileDependencies: [
    'vuetify'
  ],
  configureWebpack: {
    plugins: [
        new BundleTracker({ path: __dirname, filename: 'webpack-stats.json' }),
    ],
  }
}
