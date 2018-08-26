systemd-portabled.service(8)
=============================

名称
--------

systemd-portabled.service, systemd-portabled - ポータブルサービスマネージャ

書式
--------

| systemd-portabled.service
| /usr/lib/systemd/systemd-portabled

説明
-----------

**systemd-portabled** はポータブルサービスイメージをアタッチ・デタッチ・調査するためのシステムサービスです。

**systemd-portabled** のほとんどの機能は :doc:`portablectl.1` コマンドからアクセスすることができます。

このサービスの実装コンセプトについて詳しくは **Portable Services Documentation** [1]_ を参照してください。

関連項目
--------

:doc:`systemd.1`,
:doc:`portablectl.1`

注釈
-------

.. [1] https://github.com/systemd/systemd/blob/master/doc/PORTABLE_SERVICES.md
