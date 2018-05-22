systemd-timesyncd.service(8)
================================

名称
--------

systemd-timesyncd.service, systemd-timesyncd - ネットワーク時刻同期

書式
--------

| systemd-timesyncd.service
| /usr/lib/systemd/systemd-timesyncd

説明
-----------

systemd-timesyncd はリモートの Network Time Protocol サーバーを使ってローカルのシステム時刻を同期するシステムサービスです。また、時刻が同期されるたびにローカル時刻がディスクに保存されるため、システムにバッテリー内蔵の RTC チップが搭載されていなくてもシステムのリアルタイムクロックが再起動後も確実に進めることができるようになっています。

systemd-timesyncd サービスは仕様的には SNTP のみを実装しています。このミニマルなサービスは時刻の差分が大きいときはシステム時刻を設定して、差分が小さいときはゆっくりと調整します。より複雑なユースケースは systemd-timesyncd では想定されていません。

接続する NTP サーバーは :doc:`timesyncd.conf.5` のグローバル設定、.network ファイルのリンク別の静的設定、DHCP によって受信されるリンク別の動的設定から決まります。詳しくは :doc:`systemd.network.5` を見てください。

このサービスを起動・有効化・無効化・停止するときは :doc:`timedatectl.1` の **set-ntp** コマンドを使います。

ファイル
----------

.. describe:: /var/lib/systemd/timesync/clock

   このファイルには最後に同期が成功した時のタイムスタンプが保存されます。

関連項目
--------

:doc:`systemd.1`,
:doc:`timesyncd.conf.5`,
:doc:`systemd.network.5`,
:doc:`systemd-networkd.service.8`,
:doc:`timedatectl.1`,
:doc:`localtime.5`,
:doc:`hwclock.8`
