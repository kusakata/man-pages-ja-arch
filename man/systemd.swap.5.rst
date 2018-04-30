systemd.swap(5)
==================

名称
--------

systemd.swap - スワップユニットの設定

書式
--------

*swap*.swap

説明
-----------

名前の末尾が ".swap" のユニット設定ファイルはスワップデバイスやスワップファイルの情報をエンコードします。systemd によってメモリページの制御や管理に使われます。

この man ページではスワップユニットタイプの設定オプションについて記述しています。全てのユニット設定ファイルで共通のオプションについては :manpage:`systemd.unit(5)` を参照してください。共通の設定アイテムは一般的な [Unit] と [Install] セクションで設定します。スワップユニットの設定オプションは [Swap] セクションで設定します。

:manpage:`systemd.exec(5)` には :manpage:`swapon(8)` プログラムが実行されたときの環境変数を定義するオプションが、:doc:`systemd.kill.5` にはプロセスを終了する方法を定義するオプションが、:manpage:`systemd.resource-control(5)` にはユニットのプロセスのリソース制御を設定するオプションについて記述されています。

スワップユニットの名前は制御するスワップデバイスやスワップファイルの名前と合わせる必要があります。例: スワップデバイス /dev/sda5 はユニットファイル dev-sda5.swap で設定してください。ファイルシステムのパスをユニットの前に変換するときにエスケープを行う方法については :manpage:`systemd.unit(5)` を参照してください。スワップユニットはテンプレート化することができません。シンボリックリンクを作成してスワップユニットに複数の名前を追加することも不可能です。

オプション
----------

スワップファイルには [Swap] セクションが必要です。管理するスワップデバイスについての情報を記述します。[Swap] セクションで使用するオプションの中には他のユニットタイプでも使えるものがあります。そのようなオプションは :manpage:`systemd.exec(5)` や :doc:`systemd.kill.5` で説明しています。スワップユニットでしか使えない [Swap] セクションのオプションは以下の通りです:

.. option:: What=

   ページングに使用するデバイスノードあるいはファイルの絶対パスを指定します。詳しくは :manpage:`swapon(8)` を見てください。

.. option:: Priority=

   スワップデバイスやスワップファイルを有効化するときのスワップの優先順位です。整数を指定します。この設定は任意であり、Options= キーで pri= を使って優先度が設定されていた場合は無視されます。

他のオプションについては :manpage:`systemd.exec(5)` や :doc:`systemd.kill.5` を参照してください。

関連項目
--------

:manpage:`systemd(1)`,
:manpage:`systemctl(1)`,
:manpage:`systemd.unit(5)`,
:manpage:`systemd.exec(5)`,
:doc:`systemd.kill.5`,
:manpage:`systemd.resource-control(5)`,
:manpage:`systemd.device(5)`,
:manpage:`systemd.mount(5)`,
:manpage:`swapon(8)`,
:manpage:`systemd-fstab-generator(8)`,
:manpage:`systemd.directives(7)`
