hostname(5)
==================

名称
--------

hostname - ローカルホストネーム設定ファイル

書式
--------

/etc/hostname

説明
-----------

/etc/hostname ファイルは :doc:`sethostname.2` システムコールを使って起動時にローカルシステムの名前を設定します。ファイルには改行で終わるホストネーム文字列が記述されている必要があります。コメント ('#' から始まる行) は無視されます。ホストネームは64文字以内で自由に付けることができますが、7ビットの ASCII 小文字だけで指定して空白やドットを入れないことを推奨します。絶対に必須というわけではありませんが、DNS のドメイン名ラベルとしても使える名前に限定したほうが良いでしょう。

コマンドラインから :doc:`hostnamectl.1` を使うことでファイルの値を変更することができます。マウントされているシステムイメージ (起動はしていない) でホストネームを初期化したいときは :doc:`systemd-firstboot.1` を使ってください。

歴史
----------

/etc/hostname のシンプルな設定ファイルフォーマットは Debian GNU/Linux から由来しています。


関連項目
--------

:doc:`systemd.1`,
:doc:`sethostname.2`,
:doc:`hostname.1`,
:doc:`hostname.7`,
:doc:`machine-id.5`,
:doc:`machine-info.5`,
:doc:`hostnamectl.1`,
:doc:`systemd-hostnamed.service.8`,
:doc:`systemd-firstboot.1`
