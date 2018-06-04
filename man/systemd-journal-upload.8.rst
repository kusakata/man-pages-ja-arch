systemd-journal-upload(8)
==========================

名称
--------

systemd-journal-upload - ネットワークを越えてジャーナルメッセージを送信

書式
--------

**systemd-journal-upload** [OPTIONS...] [-u/--url= *URL*] [SOURCES...]

説明
-----------

**systemd-journal-upload** は **--url** で指定した URL にジャーナルのエントリをアップロードします。以下のオプションのどれかを使って制限しないかぎり、プログラムを実行しているユーザーがアクセスできる全てのジャーナルエントリが送信されます。そしてプログラムは待機を行って新しいエントリを送信します。

オプション
-----------

.. object:: -u, --url=[https://]URL, --url=[http://] URL

   指定したアドレスにアップロードします。*URL* はホストネームだけ、あるいはプロトコルとホストネームの両方で指定できます。デフォルトは **https** です。

.. object:: --system, --user

   システムサービスとカーネルからのエントリ、あるいは現在のユーザーのサービスからのエントリだけをアップロードするようにします。:doc:`journalctl.1` における **--system** や **--user** オプションと同じ意味を持ちます。何も指定しなかった場合、全てのエントリがアップロードされます。

.. object:: -m, --merge

   他のマシンを含むあらゆるジャーナルからインターリーブされたエントリをアップロードします。:doc:`journalctl.1` における **--merge** オプションと同じ意味を持ちます。

.. object:: -D, --directory=DIR

   ディレクトリのパスを引数として指定します。デフォルトのランタイム・システムジャーナルパスの代わりに指定したジャーナルディレクトリ *DIR* のエントリをアップロードします。:doc:`journalctl.1` における **--directory** オプションと同じ意味を持ちます。

.. object:: --file=GLOB

   ファイル glob を引数として指定します。デフォルトのランタイム・システムジャーナルパスの代わりに *GLOB* にマッチするジャーナルファイルのエントリをアップロードします。複数回指定することができ、その場合はファイルは適当にインターリーブされます。:doc:`journalctl.1` における **--file** オプションと同じ意味を持ちます。

.. object:: --cursor=

   カーソルで指定したジャーナルの場所からエントリをアップロードします。:doc:`journalctl.1` における **--cursor** オプションと同じ意味を持ちます。

.. object:: --after-cursor=

   カーソルで指定したジャーナルの場所の後からエントリをアップロードします。:doc:`journalctl.1` における **--after-cursor** オプションと同じ意味を持ちます。

.. object:: --save-state[=PATH]

   *PATH* のファイル (デフォルトは /var/lib/systemd/journal-upload/state) に保存されたカーソルで指定されたジャーナルの場所の後からエントリをアップロードします。エントリのアップロードが成功すると、このファイルはエントリのカーソルで更新されます。

.. object:: --follow[=BOOL]

   yes に設定した場合、**systemd-journal-upload** は入力を待機します。

.. object:: --key=

   PEM 形式の SSL 鍵ファイルのパスを指定します。デフォルトは /etc/ssl/private/journal-upload.pem。

.. object:: --cert=

   PEM 形式の SSL 証明書ファイルのパスを指定します。デフォルトは /etc/ssl/certs/journal-upload.pem。

.. object:: --trust=

   PEM 形式の SSL CA 証明書ファイルのパス、あるいは **all** を指定します。**all** に設定した場合、証明書のチェックが無効になります。デフォルトは /etc/ssl/ca/trusted.pem です。

.. object:: -h, --help

   短いヘルプテキストを出力して終了します。

.. object:: --version

   短いバージョン文字列を出力して終了します。

終了ステータス
---------------

成功時は 0 が返り、失敗時はゼロ以外のコードが返ります。

サンプル
----------

**例 1. 認証用の証明書を設定**

アップロードされたメッセージが正しいかどうか検証するために認証局によって署名された証明書が使われます。

証明書は **openssl** を使って生成することができます:

.. code-block:: console

   openssl req -newkey rsa:2048 -days 3650 -x509 -nodes \
         -out ca.pem -keyout ca.key -subj '/CN=Certificate authority/'

   cat >ca.conf <<EOF
   [ ca ]
   default_ca = this

   [ this ]
   new_certs_dir = .
   certificate = ca.pem
   database = ./index
   private_key = ca.key
   serial = ./serial
   default_days = 3650
   default_md = default
   policy = policy_anything

   [ policy_anything ]
   countryName             = optional
   stateOrProvinceName     = optional
   localityName            = optional
   organizationName        = optional
   organizationalUnitName  = optional
   commonName              = supplied
   emailAddress            = optional
   EOF

   touch index
   echo 0001 >serial

   SERVER=server
   CLIENT=client

   openssl req -newkey rsa:2048 -nodes -out $SERVER.csr -keyout $SERVER.key -subj "/CN=$SERVER/"
   openssl ca -batch -config ca.conf -notext -in $SERVER.csr -out $SERVER.pem

   openssl req -newkey rsa:2048 -nodes -out $CLIENT.csr -keyout $CLIENT.key -subj "/CN=$CLIENT/"
   openssl ca -batch -config ca.conf -notext -in $CLIENT.csr -out $CLIENT.pem

生成されたファイル ca.pem, server.pem, server.key はサーバーにインストールしてください。ca.pem, client.pem, client.key はクライアントにインストールしてください。これらのファイルのパスは /etc/systemd/journal-remote.conf (サーバー側) と /etc/systemd/journal-upload.conf (クライアント側) の *TrustedCertificateFile=*, *ServerCertificateFile=*, *ServerKeyFile=* で指定できます。デフォルトのパスは **systemd-journal-remote --help** と **systemd-journal-upload --help** で確認することができます。

関連項目
--------

:doc:`systemd-journal-remote.8`,
:doc:`journalctl.1`,
:doc:`systemd-journald.service.8`,
:doc:`systemd-journal-gatewayd.service.8`
