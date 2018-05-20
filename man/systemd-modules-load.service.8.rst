systemd-modules-load.service(8)
================================

名称
--------

systemd-modules-load.service, systemd-modules-load - 起動時にカーネルモジュールをロード

書式
--------

| systemd-modules-load.service
| /usr/lib/systemd/systemd-modules-load

説明
-----------

systemd-modules-load.service は静的設定に基づいて起動の初期段階でカーネルモジュールをロードするサービスです。

サービスの設定については :doc:`modules-load.d.5` を参照してください。

カーネルコマンドライン
--------------------------

systemd-modules-load.service は以下のカーネルコマンドラインパラメータを認識します:

.. option:: modules_load=, rd.modules_load=

   起動初期段階で静的にロードするカーネルモジュールをカンマで区切ったリストを指定します。前に "rd." が付くオプションは初期 RAM ディスクでのみ読み込まれます。

関連項目
--------

:doc:`systemd.1`,
:doc:`modules-load.d.5`