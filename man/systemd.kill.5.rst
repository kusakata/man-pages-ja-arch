systemd.kill(5)
==================

名称
--------

systemd.kill - プロセス終了方法の設定

書式
--------

*service*.service, *socket*.socket, *mount*.mount, *swap*.swap, *scope*.scope

説明
-----------

サービス・ソケット・マウントポイント・スワップデバイス・スコープのユニット設定ファイルは、ユニットに属するプロセスの終了方法を定義する設定オプションが共通しています。

この man ページでは上記5つのユニットタイプで共通する設定オプションについて説明しています。全てのユニット設定ファイルで共通のオプションについては :manpage:`systemd.unit(5)` を参照してください。個別のユニットタイプでしか使えない設定オプションについては :manpage:`systemd.service(5)`, :manpage:`systemd.socket(5)`, :doc:`systemd.swap.5`, :manpage:`systemd.mount(5)`, :manpage:`systemd.scope(5)` を参照してください。

終了方法の設定オプションはユニットタイプにあわせて [Service], [Socket], [Mount], [Swap] セクションのどれかに設定します。

オプション
----------

.. option:: KillMode=

   ユニットのプロセスを終了する方法を指定します。**control-group**, **process**, **mixed**, **none** のどれかになります。

関連項目
--------

:manpage:`systemd(1)`,
:manpage:`systemctl(1)`,
:manpage:`journalctl(8)`,
:manpage:`systemd.unit(5)`,
:manpage:`systemd.service(5)`,
:manpage:`systemd.socket(5)`,
:manpage:`systemd.swap(5)`,
:manpage:`systemd.mount(5)`,
:manpage:`systemd.exec(5)`,
:manpage:`systemd.directives(7)`,
:manpage:`kill(2)`,
:manpage:`signal(7)`
