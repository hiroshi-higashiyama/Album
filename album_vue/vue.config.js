module.exports = {
    //ここで指定した場所で展開する
    outputDir: '../album_django',
    //サーバーを起動した時のルートパス
    publicPath: '/',
    //outputDir起点でindex.htmlを格納する場所を指定
    indexPath: 'post/templates/index.html',
    //outputDir起点でstaticファイルを格納する場所を指定
    assetsDir: 'staticfiles'
}
