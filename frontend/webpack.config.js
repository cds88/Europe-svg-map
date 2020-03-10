
const path = require('path');
const HtmlWebpackPlugin = require("html-webpack-plugin");



module.exports = {
    entry: {
        Index: './src/Index.tsx'
    },
    watch: true,
    devtool: false,
    //'source-map',
    output: { 
        filename: '[name].js',
        path: path.resolve(__dirname, './public/')
    },
    cache: true,
    mode: 'development',
    plugins:[
        new HtmlWebpackPlugin({
            template: './index.html'
        })
    ],


    module: {
        rules: [

            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            },
            {
                test: /\.ts(x?)$/,
                exclude: /node_modules/,
                use: {
                    loader: "ts-loader"
                }
            },
            {
                test: /\.css$/i,
                use: ['style-loader', 'css-loader'],
            },
            {
                test: /\.s[ac]ss$/i,
                use: ['style-loader', 'css-loader', 'sass-loader'],
            },
            {
                test: /\.(png|jpe?g|gif|eot|ttf|woff|svg)$/i,
                use: [
                    {
                        loader: 'file-loader',
                    },
                ],
            }


        ]



    },
    resolve: {
        extensions: [
            '.tsx', '.ts', '.js'
        ]
    },
    devServer:{
        contentBase: path.join(__dirname, 'src'),
        compress: true,
        port : 4800
    }

}
