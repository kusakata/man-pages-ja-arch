chroot(1)
==================

名称
--------

chroot - 特定のルートディレクトリでコマンドあるいはインタラクティブシェルを実行

書式
--------

**chroot** [*OPTION*] *NEWROOT* [*COMMAND* [*ARG*]..]

説明
-----------

ルートディレクトリを NEWROOT に設定して COMMAND を実行します。

.. option:: --groups=G_LIST

   g1,g2,..,gN と追加グループを指定します。

.. option:: --userspec=USER:GROUP

   使用するユーザーとグループ (ID または名前) を指定します。

.. option:: --skip-chdir

   作業ディレクトリを '/' に変更しません。

.. option:: --help

   このヘルプを表示して終了します。

.. option:: --version

   バージョン情報を出力して終了します。

コマンドを指定しなかった場合、`"$SHELL" -i` (デフォルト: `/bin/sh -i`) が実行されます。

著者
-------

Roland McGrath によって書かれました。

バグの報告
------------

GNU coreutils オンラインヘルプ: <https://www.gnu.org/software/coreutils/>

chroot の翻訳についてのバグの報告: <https://translationproject.org/team/>

著作権
-------

Copyright © 2017 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.

This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.

関連項目
--------

:doc:`chroot.2`

完全なドキュメントは <https://www.gnu.org/software/coreutils/chroot> にあります。もしくはローカルで: info '(coreutils) chroot invocation'
