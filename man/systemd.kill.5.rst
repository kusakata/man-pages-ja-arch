systemd.kill(5)
==================

.. _name:

名称
--------

systemd.kill - プロセス終了方法の設定

.. _synopsis:

書式
--------

*service*.service, *socket*.socket, *mount*.mount, *swap*.swap, *scope*.scope

.. _description:

説明
-----------

サービス・ソケット・マウントポイント・スワップデバイス・スコープのユニット設定ファイルは、ユニットに属するプロセスの終了方法を定義する設定オプションが共通しています。

この man ページでは上記5つのユニットタイプで共通する設定オプションについて説明しています。全てのユニット設定ファイルで共通のオプションについては :doc:`systemd.unit.5` を参照してください。個別のユニットタイプでしか使えない設定オプションについては :doc:`systemd.service.5`, :doc:`systemd.socket.5`, :doc:`systemd.swap.5`, :doc:`systemd.mount.5`, :doc:`systemd.scope.5` を参照してください。

終了方法の設定オプションはユニットタイプにあわせて [Service], [Socket], [Mount], [Swap] セクションのどれかに設定します。

.. _options:

オプション
----------

.. option:: KillMode=

   ユニットのプロセスを終了する方法を指定します。**control-group**, **process**, **mixed**, **none** のどれかになります。

   **control-group** に設定した場合、ユニットの停止時にユニットのコントロールグループの全てのプロセスが終了します (サービスの場合: *ExecStop=* で設定されているように停止コマンドが実行された後)。**process** に設定した場合、メインプロセスだけが終了します。**mixed** に設定した場合、**SIGTERM** シグナル (下を参照) がメインプロセスに送信され、ユニットのコントロールグループのプロセスには **SIGKILL** シグナル (下を参照) が送信されます。**none** に設定した場合、プロセスは終了しません。その場合、ユニットの停止時に停止コマンドは実行されますが、プロセスは終了しません。停止後も生きているプロセスはコントロールグループに残り、コントロールグループが空になるまでコントロールグループは停止後も存在し続けます。

   (*KillSignal=* で送信コマンドが変更されていないかぎり) プロセスは最初に **SIGTERM** で終了します。任意で、その後すぐに **SIGHUP** を送信することができます (*SendSIGHUP=* で有効化した場合)。一定時間後もプロセスが終了しない場合 (時間は *TimeoutStopSec=* オプションで設定できます)、**SIGKILL** シグナルで繰り返し終了リクエストが送信されます (*SendSIGKILL=* オプションで無効化できます)。詳しくは :doc:`kill.2` を見てください。

   デフォルトは **control-group** です。

.. option:: KillSignal=

   サービスの終了時にどのシグナルを使用するか指定します。ユニットのシャットダウン時に最初に送信されるシグナルを制御します (上を参照)。通常はその後に **SIGKILL** が送信されます (上と下を参照)。利用可能なシグナルのリストは :doc:`signal.7` を参照してください。デフォルトは **SIGTERM** です。

   この設定でシグナルが送信された後、systemd は常に **SIGCONT** を送信するので注意してください。停止したタスクが正しく終了されることを保証するためです。

.. option:: SendSIGHUP=

   *KillSignal=* で設定したシグナルを送信した後に残っているプロセスに **SIGHUP** を送信するかどうか指定します。接続が切断したシェルやシェルライクなプログラムで有用です。論理値で指定します。デフォルトは "no" です。

.. option:: SendSIGKILL=

   通常のシャットダウンを行ってもサービスのプロセスが消えない場合、タイムアウト後に残っているプロセスに **SIGKILL** を送信するかどうか指定します。論理値で指定します。デフォルトは "yes" です。

.. _see-also:

関連項目
--------

:doc:`systemd.1`,
:doc:`systemctl.1`,
:doc:`journalctl.8`,
:doc:`systemd.unit.5`,
:doc:`systemd.service.5`,
:doc:`systemd.socket.5`,
:doc:`systemd.swap.5`,
:doc:`systemd.mount.5`,
:doc:`systemd.exec.5`,
:doc:`systemd.directives.7`,
:doc:`kill.2`,
:doc:`signal.7`
