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

この man ページではスワップユニットタイプの設定オプションについて記述しています。全てのユニット設定ファイルで共通のオプションについては :doc:`systemd.unit.5` を参照してください。共通の設定アイテムは一般的な [Unit] と [Install] セクションで設定します。スワップユニットの設定オプションは [Swap] セクションで設定します。

:doc:`systemd.exec.5` には :doc:`swapon.8` プログラムが実行されたときの環境変数を定義するオプションが、:doc:`systemd.kill.5` にはプロセスを終了する方法を定義するオプションが、:doc:`systemd.resource-control.5` にはユニットのプロセスのリソース制御を設定するオプションについて記述されています。

スワップユニットの名前は制御するスワップデバイスやスワップファイルの名前と合わせる必要があります。例: スワップデバイス /dev/sda5 はユニットファイル dev-sda5.swap で設定してください。ファイルシステムのパスをユニットの前に変換するときにエスケープを行う方法については :doc:`systemd.unit.5` を参照してください。スワップユニットはテンプレート化することができません。シンボリックリンクを作成してスワップユニットに複数の名前を追加することも不可能です。

黙示的な依存関係
-----------------
以下の依存関係が黙示的に追加されます:

   全てのスワップユニットは有効化するデバイスユニットやファイルのマウントユニットが自動的に *BindsTo=* と *After=* に設定されます。

:doc:`systemd.exec.5` や :doc:`systemd.kill.5` で説明されているように実行やリソース制御のパラメータの結果として黙示的な依存関係が追加されることがあります。

デフォルトの依存関係
---------------------

*DefaultDependencies=no* を設定しない場合、以下の依存関係が設定されます:

   スワップユニットは自動的に *Conflicts=* と *Before=* が umount.target に設定され、*Before=swap.target* と同様にシャットダウン時に無効化されます。

FSTAB
------

スワップユニットはユニットファイルと /etc/fstab のどちらかで設定できます (詳しくは :doc:`fstab.5` を参照)。/etc/fstab に列挙されたスワップは起動時およびシステムマネージャのリロード時に動的にネイティブのユニットに変換されます。変換について詳しくは :doc:`systemd-fstab-generator.8` を参照してください。

スワップデバイスおよびスワップファイルを /etc/fstab とユニットファイルの両方で設定した場合、後者が優先されます。

/etc/fstab の読み込み時、スワップユニットを作成するときの依存関係に影響を与える特殊なオプションが存在します。

**noauto**, **auto**

   **noauto** が設定されている場合、スワップユニットは swap.target の依存ユニットとしては追加されません。起動時に自動的に有効化されなくなり、他のユニットから必要とされたときに初めて有効化されます。**auto** は **noauto** の逆であり、デフォルト設定です。

**nofail**

   **nofail** が設定されている場合、スワップユニットは swap.target から require ではなく want で有効化されます。スワップデバイスの有効化が失敗してもブートが続行するようになります。

オプション
----------

スワップファイルには [Swap] セクションが必要です。管理するスワップデバイスについての情報を記述します。[Swap] セクションで使用するオプションの中には他のユニットタイプでも使えるものがあります。そのようなオプションは :doc:`systemd.exec.5` や :doc:`systemd.kill.5` で説明しています。スワップユニットでしか使えない [Swap] セクションのオプションは以下の通りです:

.. option:: What=

   ページングに使用するデバイスノードあるいはファイルの絶対パスを指定します。詳しくは :doc:`swapon.8` を見てください。デバイスノードを指定した場合、該当するデバイスユニットの依存関係が自動的に作成されます (詳しくは :doc:`systemd.device.5` を参照)。ファイルを指定した場合、該当するマウントユニットの依存関係が自動的に作成されます (詳しくは :doc:`systemd.mount.5` を参照)。このオプションは必須です。この設定では通常の記述子拡張が適用されるため、パーセント記号は "%%" と書く必要があります。

.. option:: Priority=

   スワップデバイスやスワップファイルを有効化するときのスワップの優先順位です。整数を指定します。この設定は任意であり、*Options=* キーで pri= を使って優先度が設定されていた場合は無視されます。

.. option:: Options=

   スワップデバイスのオプション文字列を指定できます。スワップバッキングデバイスが discard や trim 操作をサポートしている場合に discard オプションを制御するのに使うことができます (詳しくは :doc:`swapon.8` を参照)。この設定では通常の記述子拡張が適用されるため、パーセント記号は "%%" と書く必要があります。

.. option:: TimeoutSec=

   swapon コマンドが完了するまで待機する時間を設定します。設定した時間以内にコマンドが終了しなかった場合、スワップが失敗したと判断されシャットダウンされます。実行中のコマンドは全て **SIGTERM** で強制終了され、一定時間後に **SIGKILL** が送信されます (:doc:`systemd.kill.5` の **KillMode=** を参照)。単位を省略して秒単位で指定するか、"5min 20s" のように時間を指定します。"0" を指定するとタイムアウトが無効になります。デフォルトではマネージャ設定ファイルの *DefaultTimeoutStartSec=* が使われます (:doc:`systemd-system.conf.5` を参照)。

他のオプションについては :doc:`systemd.exec.5` や :doc:`systemd.kill.5` を参照してください。

関連項目
--------

:doc:`systemd.1`,
:doc:`systemctl.1`,
:doc:`systemd.unit.5`,
:doc:`systemd.exec.5`,
:doc:`systemd.kill.5`,
:doc:`systemd.resource-control.5`,
:doc:`systemd.device.5`,
:doc:`systemd.mount.5`,
:doc:`swapon.8`,
:doc:`systemd-fstab-generator.8`,
:doc:`systemd.directives.7`
