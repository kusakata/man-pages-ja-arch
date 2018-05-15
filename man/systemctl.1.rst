systemctl(1)
==================

名称
--------

systemctl - systemd システム・サービスマネージャを制御する

書式
--------

**systemctl** [OPTIONS...] COMMAND [UNIT...]

説明
-----------

**systemctl** を使うことで "systemd" システム・サービスマネージャの状態を調査・制御することができます。基本的な概念やこのツールで管理される機能については :doc:`systemd.1` を参照してください。

オプション
----------

以下のオプションを使うことができます:

.. option:: -t, --type=

   引数は **service** や **socket** などのユニットタイプをカンマで区切ったリストである必要があります。

   引数のどれかがユニットタイプの場合、指定したユニットタイプだけが表示されます。そうでない場合、全てのタイプのユニットが表示されます。

   特殊なケースとして、引数のどれかが **help** の場合、利用可能な値のリストが表示されてプログラムは終了します。

.. option:: --state=

   引数はユニットの状態の LOAD, SUB, ACTIVE をカンマで区切ったリストである必要があります。ユニットを一覧表示するときに、指定した状態のユニットだけが表示されるようになります。起動に失敗したユニットだけを表示したいときは **--state=failed** を使ってください。

   特殊なケースとして、引数のどれかが **help** の場合、利用可能な値のリストが表示されてプログラムは終了します。

.. option:: -p, --property=

   **show** コマンドでユニット・ジョブ・マネージャのプロパティを表示するときに、引数に指定したプロパティだけに表示を制限します。引数は "MainPID" などプロパティ名をカンマで区切ったリストである必要があります。指定しなかった場合、全ての既知のプロパティが表示されます。複数のプロパティを指定した場合、指定した名前の全てのプロパティが表示されます。プロパティ名はシェル補完が効きます。

   マネージャ自体については、:command:`systemctl show` で利用可能なプロパティが全て表示されます。プロパティについては :doc:`systemd-system.conf.5` で説明しています。

   ユニットのプロパティはユニットタイプによって変わるため、(存在しないユニットも含め) あらゆるユニットを表示してこのタイプに関するプロパティを一覧表示します。同じように、全てのジョブを表示することでジョブに関するプロパティが一覧表示されます。ユニットのプロパティについては :doc:`systemd.unit.5` で、あるいは :doc:`systemd.service.5` や :doc:`systemd.socket.5` など個別のユニットタイプのページで説明しています。

.. option:: -a, --all

   **list-units** でユニットを表示するときに、非活性なユニットと他のユニットに追従するユニットも表示します。ユニット・ジョブ・マネージャのプロパティを表示するときは、設定されているかどうかを問わずに全てのプロパティを表示します。

   ファイルシステムにインストールされているユニットを全て一覧したいときは、**list-unit-files** コマンドを使ってください。

   **list-dependencies** でユニットを一覧表示したときは、依存するユニットの全ての依存関係が表示されます (デフォルトでは指定したユニットの依存関係だけが表示されます)。

.. option:: -r, --recursive

   ユニットを一覧表示するときに、ローカルコンテナのユニットも表示します。ローカルコンテナのユニットにはコンテナの名前とコロン文字 (":") が前に付きます。

.. option:: --reverse

   **list-dependencies** でユニットの逆依存関係が表示されます。*Wants=* などではなく *WantedBy=*, *RequiredBy=*, *PartOf=*, *BoundBy=* タイプの依存を追従します。

.. option:: --after

   **list-dependencies** で指定したユニットより順番が前に来るユニットを表示します。つまり、*After=* の依存に従って再帰的にユニットを一覧表示します。

   *After=* の依存関係は自動的に複製されて *Before=* の依存が作成されるので注意してください。一時的な依存関係を明示的に指定することもできますが、*WantedBy=* ターゲットのユニットは依存関係が黙示的に作成されたり (:doc:`systemd.target.5` を参照)、他のディレクティブによって作成されることがあります (例: *RequiresMountsFor=*)。明示的・黙示的に定義された依存関係はどちらも **list-dependencies** で表示されます。

   **list-jobs** コマンドに指定した場合、各ジョブを待機するジョブが表示されます。**--before** と組み合わせることで各ジョブを待機するジョブだけでなく各ジョブが待機する全てのジョブも表示することが可能です。

.. option:: --before

   **list-dependencies** で指定したユニットよりも順番が後のユニットを表示します。つまり、*Before=* の依存に従って再帰的にユニットを一覧表示します。

   **list-jobs** コマンドに指定した場合、各ジョブから待機される他のジョブが表示されます。**--after** と組み合わせることで各ジョブから待機される他のジョブだけでなく各ジョブを待機するジョブも表示することが可能です。

.. option:: -l, --full

   ユニットの名前やプロセスツリーのエントリ、ジャーナルの出力を省略表示しません。さらに **status**, **list-units**, **list-jobs**, **list-timers** の出力におけるユニットの説明が切り詰められなくなります。

   また、**is-enabled** の出力でインストールターゲットが表示されます。

.. option:: --value

   **show** でプロパティを出力するときに、値だけを出力して、プロパティの名前や "=" を省きます。

.. option:: --show-types

   ソケットを表示するときに、ソケットのタイプを表示します。

.. option:: --job-mode=

   新しいジョブをキューに追加したときに、このオプションは既にキューに入っているジョブをどのように扱うのかを制御します。"fail", "replace", "replace-irreversibly", "isolate", "ignore-dependencies", "ignore-requirements", "flush" のどれかひとつを指定します。デフォルトは "replace" ですが、例外的に **isolate** コマンドを使う時だけは黙示的に "isolate" ジョブモードがデフォルトになります。

   "fail" が指定されると保留ジョブとリクエストした操作が競合する場合 (既に保留中の開始ジョブが停止ジョブになる、あるいはその逆)、操作は失敗するようになります。

   "replace" (デフォルト) が指定された場合、競合する保留ジョブは必要に応じて置き換えられます。

   "replace-irreversibly" が指定された場合、"replace" のように操作が行われますが、新しいジョブは不可逆になります。これによって今後は競合する操作によってジョブが置き換えられなくなります (あるいは不可逆のジョブが保留中の際はキューに入れられます)。不可逆ジョブは **cancel** コマンドを使って取り消すことができます。このジョブモードは shutdown.target を引き寄せる操作で使ってください。

   "isolate" は起動操作でのみ指定することができ、指定されたユニットが実行されたとき他のユニットは全て停止します。**isolate** コマンドを使用するときは常にこのモードが使われます。

   "flush" は新しいジョブがキューに入ったときにキューに入っている全てのジョブを取り消します。

   "ignore-dependencies" が指定された場合、新しいジョブではユニットの依存関係が全て無視され、操作は即座に実行されます。無視されたユニットから必要とされているユニットも無視され、順序の依存関係も考慮されません。このモードは管理者がデバッグや緊急ツールとして使うためのものであり、アプリケーションが使用するべきではありません。

   "ignore-requirements" は "ignore-dependencies" と似ていますが、必要の依存関係だけ無視され、順序の依存関係は遵守されます。

.. option:: --fail

   **--job-mode=**fail の省略形。

   **kill** コマンドと組み合わせて使用した場合、どのユニットも終了しなかったときは操作はエラーになります。

.. option:: -i, --ignore-inhibitors

   When system shutdown or a sleep state is requested, ignore inhibitor locks. Applications can establish inhibitor locks to avoid that certain important operations (such as CD burning or suchlike) are interrupted by system shutdown or a sleep state. Any user may take these locks and privileged users may override these locks. If any locks are taken, shutdown and sleep state requests will normally fail (regardless of whether privileged or not) and a list of active locks is printed. However, if --ignore-inhibitors is specified, the locks are ignored and not printed, and the operation attempted anyway, possibly requiring additional privileges.

.. option:: --dry-run

   Just print what would be done. Currently supported by verbs halt, poweroff, reboot, kexec, suspend, hibernate, hybrid-sleep, default, rescue, emergency, and exit.

.. option:: -q, --quiet

   Suppress printing of the results of various commands and also the hints about truncated log lines. This does not suppress output of commands for which the printed output is the only result (like show). Errors are always printed.

.. option:: --no-block

   Do not synchronously wait for the requested operation to finish. If this is not specified, the job will be verified, enqueued and systemctl will wait until the unit's start-up is completed. By passing this argument, it is only verified and enqueued. This option may not be combined with --wait.

.. option:: --wait

   Synchronously wait for started units to terminate again. This option may not be combined with --no-block. Note that this will wait forever if any given unit never terminates (by itself or by getting stopped explicitly); particularly services which use "RemainAfterExit=yes".

.. option:: --user

   Talk to the service manager of the calling user, rather than the service manager of the system.

.. option:: --system

   Talk to the service manager of the system. This is the implied default.

.. option:: --failed

   List units in failed state. This is equivalent to --state=failed.

.. option:: --no-wall

   Do not send wall message before halt, power-off and reboot.

.. option:: --global

   When used with enable and disable, operate on the global user configuration directory, thus enabling or disabling a unit file globally for all future logins of all users.

.. option:: --no-reload

   When used with enable and disable, do not implicitly reload daemon configuration after executing the changes.

.. option:: --no-ask-password

   When used with start and related commands, disables asking for passwords. Background services may require input of a password or passphrase string, for example to unlock system hard disks or cryptographic certificates. Unless this option is specified and the command is invoked from a terminal, systemctl will query the user on the terminal for the necessary secrets. Use this option to switch this behavior off. In this case, the password must be supplied by some other means (for example graphical password agents) or the service might fail. This also disables querying the user for authentication for privileged operations.

.. option:: --kill-who=

   When used with kill, choose which processes to send a signal to. Must be one of main, control or all to select whether to kill only the main process, the control process or all processes of the unit. The main process of the unit is the one that defines the life-time of it. A control process of a unit is one that is invoked by the manager to induce state changes of it. For example, all processes started due to the ExecStartPre=, ExecStop= or ExecReload= settings of service units are control processes. Note that there is only one control process per unit at a time, as only one state change is executed at a time. For services of type Type=forking, the initial process started by the manager for ExecStart= is a control process, while the process ultimately forked off by that one is then considered the main process of the unit (if it can be determined). This is different for service units of other types, where the process forked off by the manager for ExecStart= is always the main process itself. A service unit consists of zero or one main process, zero or one control process plus any number of additional processes. Not all unit types manage processes of these types however. For example, for mount units, control processes are defined (which are the invocations of /usr/bin/mount and /usr/bin/umount), but no main process is defined. If omitted, defaults to all.

.. option:: -s, --signal=

   When used with kill, choose which signal to send to selected processes. Must be one of the well-known signal specifiers such as SIGTERM, SIGINT or SIGSTOP. If omitted, defaults to SIGTERM.

.. option:: -f, --force

   When used with enable, overwrite any existing conflicting symlinks.

   When used with edit, create all of the specified units which do not already exist.

   When used with halt, poweroff, reboot or kexec, execute the selected operation without shutting down all units. However, all processes will be killed forcibly and all file systems are unmounted or remounted read-only. This is hence a drastic but relatively safe option to request an immediate reboot. If --force is specified twice for these operations (with the exception of kexec), they will be executed immediately, without terminating any processes or unmounting any file systems. Warning: specifying --force twice with any of these operations might result in data loss. Note that when --force is specified twice the selected operation is executed by systemctl itself, and the system manager is not contacted. This means the command should succeed even when the system manager has crashed.

.. option:: --message=

   When used with halt, poweroff or reboot, set a short message explaining the reason for the operation. The message will be logged together with the default shutdown message.

.. option:: --now

   When used with enable, the units will also be started. When used with disable or mask, the units will also be stopped. The start or stop operation is only carried out when the respective enable or disable operation has been successful.

.. option:: --root=

   When used with enable/disable/is-enabled (and related commands), use the specified root path when looking for unit files. If this option is present, systemctl will operate on the file system directly, instead of communicating with the systemd daemon to carry out changes.

.. option:: --runtime

   When used with enable, disable, edit, (and related commands), make changes only temporarily, so that they are lost on the next reboot. This will have the effect that changes are not made in subdirectories of /etc but in /run, with identical immediate effects, however, since the latter is lost on reboot, the changes are lost too.

   Similarly, when used with set-property, make changes only temporarily, so that they are lost on the next reboot.

.. option:: --preset-mode=

   Takes one of "full" (the default), "enable-only", "disable-only". When used with the preset or preset-all commands, controls whether units shall be disabled and enabled according to the preset rules, or only enabled, or only disabled.

.. option:: -n, --lines=

   When used with status, controls the number of journal lines to show, counting from the most recent ones. Takes a positive integer argument. Defaults to 10.

.. option:: -o, --output=

   When used with status, controls the formatting of the journal entries that are shown. For the available choices, see journalctl(1). Defaults to "short".

.. option:: --firmware-setup

   When used with the reboot command, indicate to the system's firmware to boot into setup mode. Note that this is currently only supported on some EFI systems and only if the system was booted in EFI mode.

.. option:: --plain

   When used with list-dependencies, list-units or list-machines, the output is printed as a list instead of a tree, and the bullet circles are omitted.

.. option:: -H, --host=

   Execute the operation remotely. Specify a hostname, or a username and hostname separated by "@", to connect to. The hostname may optionally be suffixed by a container name, separated by ":", which connects directly to a specific container on the specified host. This will use SSH to talk to the remote machine manager instance. Container names may be enumerated with machinectl -H HOST.

.. option:: -M, --machine=

   Execute operation on a local container. Specify a container name to connect to.

.. option:: --no-pager

   Do not pipe output into a pager.

.. option:: --no-legend

   Do not print the legend, i.e. column headers and the footer with hints.

.. option:: -h, --help

   短いヘルプテキストを表示して終了。

.. option:: --version

   短いバージョン文字列を表示して終了。

コマンド
-----------

以下のコマンドが使用できます:

ユニットコマンド
^^^^^^^^^^^^^^^^^

.. object:: list-units [PATTERN...]

   List units that systemd currently has in memory. This includes units that are either referenced directly or through a dependency, units that are pinned by applications programmatically, or units that were active in the past and have failed. By default only units which are active, have pending jobs, or have failed are shown; this can be changed with option --all. If one or more PATTERNs are specified, only units matching one of them are shown. The units that are shown are additionally filtered by --type= and --state= if those options are specified.

   This is the default command.

.. object:: list-sockets [PATTERN...]

   List socket units currently in memory, ordered by listening address. If one or more PATTERNs are specified, only socket units matching one of them are shown. Produces output similar to

      LISTEN           UNIT                        ACTIVATES
      /dev/initctl     systemd-initctl.socket      systemd-initctl.service
      ...
      [::]:22          sshd.socket                 sshd.service
      kobject-uevent 1 systemd-udevd-kernel.socket systemd-udevd.service

      5 sockets listed.

   Note: because the addresses might contains spaces, this output is not suitable for programmatic consumption.

   Also see --show-types, --all, and --state=.

.. object:: list-timers [PATTERN...]

   List timer units currently in memory, ordered by the time they elapse next. If one or more PATTERNs are specified, only units matching one of them are shown. Produces output similar to

      NEXT                         LEFT          LAST                         PASSED     UNIT                         ACTIVATES
      /a                          n/a           Thu 2017-02-23 13:40:29 EST  3 days ago ureadahead-stop.timer        ureadahead-stop.service
      Sun 2017-02-26 18:55:42 EST  1min 14s left Thu 2017-02-23 13:54:44 EST  3 days ago systemd-tmpfiles-clean.timer systemd-tmpfiles-clean.service
      Sun 2017-02-26 20:37:16 EST  1h 42min left Sun 2017-02-26 11:56:36 EST  6h ago     apt-daily.timer              apt-daily.service
      Sun 2017-02-26 20:57:49 EST  2h 3min left  Sun 2017-02-26 11:56:36 EST  6h ago     snapd.refresh.timer          snapd.refresh.service

   NEXT shows the next time the timer will run.

   LEFT shows how long till the next time the timer runs.

   LAST shows the last time the timer ran.

   PASSED shows has long as passed since the timer laset ran.

   UNIT shows the name of the timer

   ACTIVATES shows the name the service the timer activates when it runs.

   Also see --all and --state=.

.. object:: start PATTERN...

   Start (activate) one or more units specified on the command line.

   Note that glob patterns operate on the set of primary names of units currently in memory. Units which are not active and are not in a failed state usually are not in memory, and will not be matched by any pattern. In addition, in case of instantiated units, systemd is often unaware of the instance name until the instance has been started. Therefore, using glob patterns with start has limited usefulness. Also, secondary alias names of units are not considered.

.. object:: stop PATTERN...

   Stop (deactivate) one or more units specified on the command line.

.. object:: reload PATTERN...

   Asks all units listed on the command line to reload their configuration. Note that this will reload the service-specific configuration, not the unit configuration file of systemd. If you want systemd to reload the configuration file of a unit, use the daemon-reload command. In other words: for the example case of Apache, this will reload Apache's httpd.conf in the web server, not the apache.service systemd unit file.

   This command should not be confused with the daemon-reload command.

.. object:: restart PATTERN...

   Stop and then start one or more units specified on the command line. If the units are not running yet, they will be started.

   Note that restarting a unit with this command does not necessarily flush out all of the unit's resources before it is started again. For example, the per-service file descriptor storage facility (see FileDescriptoreStoreMax= in systemd.service(5)) will remain intact as long as the unit has a job pending, and is only cleared when the unit is fully stopped and no jobs are pending anymore. If it is intended that the file descriptor store is flushed out, too, during a restart operation an explicit systemctl stop command followed by systemctl start should be issued.

.. object:: try-restart PATTERN...

   Stop and then start one or more units specified on the command line if the units are running. This does nothing if units are not running.

.. object:: reload-or-restart PATTERN...

   Reload one or more units if they support it. If not, stop and then start them instead. If the units are not running yet, they will be started.

.. object:: try-reload-or-restart PATTERN...

   Reload one or more units if they support it. If not, stop and then start them instead. This does nothing if the units are not running.

.. object:: isolate UNIT

   Start the unit specified on the command line and its dependencies and stop all others, unless they have IgnoreOnIsolate=yes (see systemd.unit(5)). If a unit name with no extension is given, an extension of ".target" will be assumed.

   This is similar to changing the runlevel in a traditional init system. The isolate command will immediately stop processes that are not enabled in the new unit, possibly including the graphical environment or terminal you are currently using.

   Note that this is allowed only on units where AllowIsolate= is enabled. See systemd.unit(5) for details.

.. object:: kill PATTERN...

   Send a signal to one or more processes of the unit. Use --kill-who= to select which process to kill. Use --signal= to select the signal to send.

.. object:: is-active PATTERN...

   Check whether any of the specified units are active (i.e. running). Returns an exit code 0 if at least one is active, or non-zero otherwise. Unless --quiet is specified, this will also print the current unit state to standard output.

.. object:: is-failed PATTERN...

   Check whether any of the specified units are in a "failed" state. Returns an exit code 0 if at least one has failed, non-zero otherwise. Unless --quiet is specified, this will also print the current unit state to standard output.

.. object:: status [PATTERN...|PID...]

   Show terse runtime status information about one or more units, followed by most recent log data from the journal. If no units are specified, show system status. If combined with --all, also show the status of all units (subject to limitations specified with -t). If a PID is passed, show information about the unit the process belongs to.

   This function is intended to generate human-readable output. If you are looking for computer-parsable output, use show instead. By default, this function only shows 10 lines of output and ellipsizes lines to fit in the terminal window. This can be changed with --lines and --full, see above. In addition, journalctl --unit=NAME or journalctl --user-unit= NAME use a similar filter for messages and might be more convenient.

   systemd implicitly loads units as necessary, so just running the status will attempt to load a file. The command is thus not useful for determining if something was already loaded or not. The units may possibly also be quickly unloaded after the operation is completed if there's no reason to keep it in memory thereafter.

   **Example 1. Example output from systemctl status**

   .. code-block:: console

      $ systemctl status bluetooth
      ● bluetooth.service - Bluetooth service
         Loaded: loaded (/usr/lib/systemd/system/bluetooth.service; enabled; vendor preset: enabled)
         Active: active (running) since Wed 2017-01-04 13:54:04 EST; 1 weeks 0 days ago
           Docs: man:bluetoothd(8)
       Main PID: 930 (bluetoothd)
         Status: "Running"
          Tasks: 1
         Memory: 648.0K
            CPU: 435ms
         CGroup: /system.slice/bluetooth.service
                 └─930 /usr/lib/bluetooth/bluetoothd

      Jan 12 10:46:45 example.com bluetoothd[8900]: Not enough free handles to register service
      Jan 12 10:46:45 example.com bluetoothd[8900]: Current Time Service could not be registered
      Jan 12 10:46:45 example.com bluetoothd[8900]: gatt-time-server: Input/output error (5)

   The dot ("●") uses color on supported terminals to summarize the unit state at a glance. White indicates an "inactive" or "deactivating" state. Red indicates a "failed" or "error" state and green indicates an "active", "reloading" or "activating" state.

   The "Loaded:" line in the output will show "loaded" if the unit has been loaded into memory. Other possible values for "Loaded:" include: "error" if there was a problem loading it, "not-found", and "masked". Along with showing the path to the unit file, this line will also show the enablement state. Enabled commands start at boot. See the full table of possible enablement states — including the definition of "masked" — in the documentation for the is-enabled command.

   The "Active:" line shows active state. The value is usually "active" or "inactive". Active could mean started, bound, plugged in, etc depending on the unit type. The unit could also be in process of changing states, reporting a state of "activating" or "deactivating". A special "failed" state is entered when the service failed in some way, such as a crash, exiting with an error code or timing out. If the failed state is entered the cause will be logged for later reference.

.. object:: show [PATTERN...|JOB...]

   Show properties of one or more units, jobs, or the manager itself. If no argument is specified, properties of the manager will be shown. If a unit name is specified, properties of the unit are shown, and if a job ID is specified, properties of the job are shown. By default, empty properties are suppressed. Use --all to show those too. To select specific properties to show, use --property=. This command is intended to be used whenever computer-parsable output is required. Use status if you are looking for formatted human-readable output.

   Many properties shown by systemctl show map directly to configuration settings of the system and service manager and its unit files. Note that the properties shown by the command are generally more low-level, normalized versions of the original configuration settings and expose runtime state in addition to configuration. For example, properties shown for service units include the service's current main process identifier as "MainPID" (which is runtime state), and time settings are always exposed as properties ending in the "...USec" suffix even if a matching configuration options end in "...Sec", because microseconds is the normalized time unit used by the system and service manager.

.. object:: cat PATTERN...

   Show backing files of one or more units. Prints the "fragment" and "drop-ins" (source files) of units. Each file is preceded by a comment which includes the file name. Note that this shows the contents of the backing files on disk, which may not match the system manager's understanding of these units if any unit files were updated on disk and the daemon-reload command wasn't issued since.

.. object:: set-property UNIT PROPERTY= VALUE...

   Set the specified unit properties at runtime where this is supported. This allows changing configuration parameter properties such as resource control settings at runtime. Not all properties may be changed at runtime, but many resource control settings (primarily those in systemd.resource-control(5)) may. The changes are applied immediately, and stored on disk for future boots, unless --runtime is passed, in which case the settings only apply until the next reboot. The syntax of the property assignment follows closely the syntax of assignments in unit files.

   Example: systemctl set-property foobar.service CPUShares=777

   If the specified unit appears to be inactive, the changes will be only stored on disk as described previously hence they will be effective when the unit will be started.

   Note that this command allows changing multiple properties at the same time, which is preferable over setting them individually. Like with unit file configuration settings, assigning an empty list will reset the property.

.. object:: help PATTERN...|PID...

   Show manual pages for one or more units, if available. If a PID is given, the manual pages for the unit the process belongs to are shown.

.. object:: reset-failed [PATTERN...]

   Reset the "failed" state of the specified units, or if no unit name is passed, reset the state of all units. When a unit fails in some way (i.e. process exiting with non-zero error code, terminating abnormally or timing out), it will automatically enter the "failed" state and its exit code and status is recorded for introspection by the administrator until the service is stopped/re-started or reset with this command.

.. object:: list-dependencies [UNIT]

   Shows units required and wanted by the specified unit. This recursively lists units following the Requires=, Requisite=, ConsistsOf=, Wants=, BindsTo= dependencies. If no unit is specified, default.target is implied.

   By default, only target units are recursively expanded. When --all is passed, all other units are recursively expanded as well.

   Options --reverse, --after, --before may be used to change what types of dependencies are shown.

ユニットファイルコマンド
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. object:: list-unit-files [PATTERN...]

   List unit files installed on the system, in combination with their enablement state (as reported by is-enabled). If one or more PATTERNs are specified, only unit files whose name matches one of them are shown (patterns matching unit file system paths are not supported).

.. object:: enable UNIT..., enable PATH...

   Enable one or more units or unit instances. This will create a set of symlinks, as encoded in the "[Install]" sections of the indicated unit files. After the symlinks have been created, the system manager configuration is reloaded (in a way equivalent to daemon-reload), in order to ensure the changes are taken into account immediately. Note that this does not have the effect of also starting any of the units being enabled. If this is desired, combine this command with the --now switch, or invoke start with appropriate arguments later. Note that in case of unit instance enablement (i.e. enablement of units of the form foo@bar.service), symlinks named the same as instances are created in the unit configuration directory, however they point to the single template unit file they are instantiated from.

   This command expects either valid unit names (in which case various unit file directories are automatically searched for unit files with appropriate names), or absolute paths to unit files (in which case these files are read directly). If a specified unit file is located outside of the usual unit file directories, an additional symlink is created, linking it into the unit configuration path, thus ensuring it is found when requested by commands such as start. The file system where the linked unit files are located must be accessible when systemd is started (e.g. anything underneath /home or /var is not allowed, unless those directories are located on the root file system).

   This command will print the file system operations executed. This output may be suppressed by passing --quiet.

   Note that this operation creates only the symlinks suggested in the "[Install]" section of the unit files. While this command is the recommended way to manipulate the unit configuration directory, the administrator is free to make additional changes manually by placing or removing symlinks below this directory. This is particularly useful to create configurations that deviate from the suggested default installation. In this case, the administrator must make sure to invoke daemon-reload manually as necessary, in order to ensure the changes are taken into account.

   Enabling units should not be confused with starting (activating) units, as done by the start command. Enabling and starting units is orthogonal: units may be enabled without being started and started without being enabled. Enabling simply hooks the unit into various suggested places (for example, so that the unit is automatically started on boot or when a particular kind of hardware is plugged in). Starting actually spawns the daemon process (in case of service units), or binds the socket (in case of socket units), and so on.

   Depending on whether --system, --user, --runtime, or --global is specified, this enables the unit for the system, for the calling user only, for only this boot of the system, or for all future logins of all users. Note that in the last case, no systemd daemon configuration is reloaded.

   Using enable on masked units is not supported and results in an error.

.. object:: disable UNIT...

   Disables one or more units. This removes all symlinks to the unit files backing the specified units from the unit configuration directory, and hence undoes any changes made by enable or link. Note that this removes all symlinks to matching unit files, including manually created symlinks, and not just those actually created by enable or link. Note that while disable undoes the effect of enable, the two commands are otherwise not symmetric, as disable may remove more symlinks than a prior enable invocation of the same unit created.

   This command expects valid unit names only, it does not accept paths to unit files.

   In addition to the units specified as arguments, all units are disabled that are listed in the Also= setting contained in the "[Install]" section of any of the unit files being operated on.

   This command implicitly reloads the system manager configuration after completing the operation. Note that this command does not implicitly stop the units that are being disabled. If this is desired, either combine this command with the --now switch, or invoke the stop command with appropriate arguments later.

   This command will print information about the file system operations (symlink removals) executed. This output may be suppressed by passing --quiet.

   This command honors --system, --user, --runtime and --global in a similar way as enable.

.. object:: reenable UNIT...

   Reenable one or more units, as specified on the command line. This is a combination of disable and enable and is useful to reset the symlinks a unit file is enabled with to the defaults configured in its "[Install]" section. This command expects a unit name only, it does not accept paths to unit files.

.. object:: preset UNIT...

   Reset the enable/disable status one or more unit files, as specified on the command line, to the defaults configured in the preset policy files. This has the same effect as disable or enable, depending how the unit is listed in the preset files.

   Use --preset-mode= to control whether units shall be enabled and disabled, or only enabled, or only disabled.

   If the unit carries no install information, it will be silently ignored by this command. UNIT must be the real unit name, any alias names are ignored silently.

   For more information on the preset policy format, see systemd.preset(5). For more information on the concept of presets, please consult the Preset [#]_ document.

.. object:: preset-all

   Resets all installed unit files to the defaults configured in the preset policy file (see above).

   Use --preset-mode= to control whether units shall be enabled and disabled, or only enabled, or only disabled.

.. object:: is-enabled UNIT...

   Checks whether any of the specified unit files are enabled (as with enable). Returns an exit code of 0 if at least one is enabled, non-zero otherwise. Prints the current enable status (see table). To suppress this output, use --quiet. To show installation targets, use --full.

   **Table 1.  is-enabled output**

   Name	Description	Exit Code
   "enabled"	Enabled via .wants/, .requires/ or Alias= symlinks (permanently in /etc/systemd/system/, or transiently in /run/systemd/system/).	0
   "enabled-runtime"		
   "linked"	Made available through one or more symlinks to the unit file (permanently in /etc/systemd/system/ or transiently in /run/systemd/system/), even though the unit file might reside outside of the unit file search path.	> 0
   "linked-runtime"		
   "masked"	Completely disabled, so that any start operation on it fails (permanently in /etc/systemd/system/ or transiently in /run/systemd/systemd/).	> 0
   "masked-runtime"		
   "static"	The unit file is not enabled, and has no provisions for enabling in the "[Install]" unit file section.	0
   "indirect"	The unit file itself is not enabled, but it has a non-empty Also= setting in the "[Install]" unit file section, listing other unit files that might be enabled, or it has an alias under a different name through a symlink that is not specified in Also=. For template unit file, an instance different than the one specified in DefaultInstance= is enabled.	0
   "disabled"	The unit file is not enabled, but contains an "[Install]" section with installation instructions.	> 0
   "generated"	The unit file was generated dynamically via a generator tool. See systemd.generator(7). Generated unit files may not be enabled, they are enabled implicitly by their generator.	0
   "transient"	The unit file has been created dynamically with the runtime API. Transient units may not be enabled.	0
   "bad"	The unit file is invalid or another error occurred. Note that is-enabled will not actually return this state, but print an error message instead. However the unit file listing printed by list-unit-files might show it.	> 0

.. object:: mask UNIT...

   Mask one or more units, as specified on the command line. This will link these unit files to /dev/null, making it impossible to start them. This is a stronger version of disable, since it prohibits all kinds of activation of the unit, including enablement and manual activation. Use this option with care. This honors the --runtime option to only mask temporarily until the next reboot of the system. The --now option may be used to ensure that the units are also stopped. This command expects valid unit names only, it does not accept unit file paths.

.. object:: unmask UNIT...

   Unmask one or more unit files, as specified on the command line. This will undo the effect of mask. This command expects valid unit names only, it does not accept unit file paths.

.. object:: link PATH...

   Link a unit file that is not in the unit file search paths into the unit file search path. This command expects an absolute path to a unit file. The effect of this may be undone with disable. The effect of this command is that a unit file is made available for commands such as start, even though it is not installed directly in the unit search path. The file system where the linked unit files are located must be accessible when systemd is started (e.g. anything underneath /home or /var is not allowed, unless those directories are located on the root file system).

.. object:: revert UNIT...

   Revert one or more unit files to their vendor versions. This command removes drop-in configuration files that modify the specified units, as well as any user-configured unit file that overrides a matching vendor supplied unit file. Specifically, for a unit "foo.service" the matching directories "foo.service.d/" with all their contained files are removed, both below the persistent and runtime configuration directories (i.e. below /etc/systemd/system and /run/systemd/system); if the unit file has a vendor-supplied version (i.e. a unit file located below /usr) any matching persistent or runtime unit file that overrides it is removed, too. Note that if a unit file has no vendor-supplied version (i.e. is only defined below /etc/systemd/system or /run/systemd/system, but not in a unit file stored below /usr), then it is not removed. Also, if a unit is masked, it is unmasked.

   Effectively, this command may be used to undo all changes made with systemctl edit, systemctl set-property and systemctl mask and puts the original unit file with its settings back in effect.

.. object:: add-wants TARGET UNIT..., add-requires TARGET UNIT...

   Adds "Wants=" or "Requires=" dependencies, respectively, to the specified TARGET for one or more units.

   This command honors --system, --user, --runtime and --global in a way similar to enable.

.. object:: edit UNIT...

   Edit a drop-in snippet or a whole replacement file if --full is specified, to extend or override the specified unit.

   Depending on whether --system (the default), --user, or --global is specified, this command creates a drop-in file for each unit either for the system, for the calling user, or for all futures logins of all users. Then, the editor (see the "Environment" section below) is invoked on temporary files which will be written to the real location if the editor exits successfully.

   If --full is specified, this will copy the original units instead of creating drop-in files.

   If --force is specified and any units do not already exist, new unit files will be opened for editing.

   If --runtime is specified, the changes will be made temporarily in /run and they will be lost on the next reboot.

   If the temporary file is empty upon exit, the modification of the related unit is canceled.

   After the units have been edited, systemd configuration is reloaded (in a way that is equivalent to daemon-reload).

   Note that this command cannot be used to remotely edit units and that you cannot temporarily edit units which are in /etc, since they take precedence over /run.

.. object:: get-default

   Return the default target to boot into. This returns the target unit name default.target is aliased (symlinked) to.

.. object:: set-default TARGET

   Set the default target to boot into. This sets (symlinks) the default.target alias to the given target unit.

マシンコマンド
^^^^^^^^^^^^^^^^^

.. object:: list-machines [PATTERN...]

   List the host and all running local containers with their state. If one or more PATTERNs are specified, only containers matching one of them are shown.

ジョブコマンド
^^^^^^^^^^^^^^^^^

.. object:: list-jobs [PATTERN...]

   List jobs that are in progress. If one or more PATTERNs are specified, only jobs for units matching one of them are shown.

   When combined with --after or --before the list is augmented with information on which other job each job is waiting for, and which other jobs are waiting for it, see above.

.. object:: cancel JOB...

   Cancel one or more jobs specified on the command line by their numeric job IDs. If no job ID is specified, cancel all pending jobs.

環境コマンド
^^^^^^^^^^^^^^^

.. object:: show-environment

   Dump the systemd manager environment block. This is the environment block that is passed to all processes the manager spawns. The environment block will be dumped in straight-forward form suitable for sourcing into most shells. If no special characters or whitespace is present in the variable values, no escaping is performed, and the assignments have the form "VARIABLE=value". If whitespace or characters which have special meaning to the shell are present, dollar-single-quote escaping is used, and assignments have the form "VARIABLE=$'value'". This syntax is known to be supported by bash(1), zsh(1), ksh(1), and busybox(1)'s ash(1), but not dash(1) or fish(1).

.. object:: set-environment VARIABLE=VALUE...

   Set one or more systemd manager environment variables, as specified on the command line.

.. object:: unset-environment VARIABLE...

   Unset one or more systemd manager environment variables. If only a variable name is specified, it will be removed regardless of its value. If a variable and a value are specified, the variable is only removed if it has the specified value.

.. object:: import-environment [VARIABLE...]

   Import all, one or more environment variables set on the client into the systemd manager environment block. If no arguments are passed, the entire environment block is imported. Otherwise, a list of one or more environment variable names should be passed, whose client-side values are then imported into the manager's environment block.

マネージャライフサイクルコマンド
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. object:: daemon-reload

   Reload the systemd manager configuration. This will rerun all generators (see systemd.generator(7)), reload all unit files, and recreate the entire dependency tree. While the daemon is being reloaded, all sockets systemd listens on behalf of user configuration will stay accessible.

   This command should not be confused with the reload command.

.. object:: daemon-reexec

   Reexecute the systemd manager. This will serialize the manager state, reexecute the process and deserialize the state again. This command is of little use except for debugging and package upgrades. Sometimes, it might be helpful as a heavy-weight daemon-reload. While the daemon is being reexecuted, all sockets systemd listening on behalf of user configuration will stay accessible.

システムコマンド
^^^^^^^^^^^^^^^^^^^

.. object:: is-system-running

   Checks whether the system is operational. This returns success (exit code 0) when the system is fully up and running, specifically not in startup, shutdown or maintenance mode, and with no failed services. Failure is returned otherwise (exit code non-zero). In addition, the current state is printed in a short string to standard output, see the table below. Use --quiet to suppress this output.

   **Table 2. is-system-running output**

   Name	Description	Exit Code
   initializing	Early bootup, before basic.target is reached or the maintenance state entered.	> 0
   starting	Late bootup, before the job queue becomes idle for the first time, or one of the rescue targets are reached.	> 0
   running	The system is fully operational.	0
   degraded	The system is operational but one or more units failed.	> 0
   maintenance	The rescue or emergency target is active.	> 0
   stopping	The manager is shutting down.	> 0
   offline	The manager is not running. Specifically, this is the operational state if an incompatible program is running as system manager (PID 1).	> 0
   unknown	The operational state could not be determined, due to lack of resources or another error cause.	> 0

.. object:: default

   Enter default mode. This is equivalent to systemctl isolate default.target. This operation is blocking by default, use --no-block to request asynchronous behavior.

.. object:: rescue

   Enter rescue mode. This is equivalent to systemctl isolate rescue.target. This operation is blocking by default, use --no-block to request asynchronous behavior.

.. object:: emergency

   Enter emergency mode. This is equivalent to systemctl isolate emergency.target. This operation is blocking by default, use --no-block to request asynchronous behavior.

.. object:: halt

   Shut down and halt the system. This is mostly equivalent to systemctl start halt.target --job-mode=replace-irreversibly --no-block, but also prints a wall message to all users. This command is asynchronous; it will return after the halt operation is enqueued, without waiting for it to complete. Note that this operation will simply halt the OS kernel after shutting down, leaving the hardware powered on. Use systemctl poweroff for powering off the system (see below).

   If combined with --force, shutdown of all running services is skipped, however all processes are killed and all file systems are unmounted or mounted read-only, immediately followed by the system halt. If --force is specified twice, the operation is immediately executed without terminating any processes or unmounting any file systems. This may result in data loss. Note that when --force is specified twice the halt operation is executed by systemctl itself, and the system manager is not contacted. This means the command should succeed even when the system manager has crashed.

.. object:: poweroff

   Shut down and power-off the system. This is mostly equivalent to systemctl start poweroff.target --job-mode=replace-irreversibly --no-block, but also prints a wall message to all users. This command is asynchronous; it will return after the power-off operation is enqueued, without waiting for it to complete.

   If combined with --force, shutdown of all running services is skipped, however all processes are killed and all file systems are unmounted or mounted read-only, immediately followed by the powering off. If --force is specified twice, the operation is immediately executed without terminating any processes or unmounting any file systems. This may result in data loss. Note that when --force is specified twice the power-off operation is executed by systemctl itself, and the system manager is not contacted. This means the command should succeed even when the system manager has crashed.

.. object:: reboot [arg]

   Shut down and reboot the system. This is mostly equivalent to systemctl start reboot.target --job-mode=replace-irreversibly --no-block, but also prints a wall message to all users. This command is asynchronous; it will return after the reboot operation is enqueued, without waiting for it to complete.

   If combined with --force, shutdown of all running services is skipped, however all processes are killed and all file systems are unmounted or mounted read-only, immediately followed by the reboot. If --force is specified twice, the operation is immediately executed without terminating any processes or unmounting any file systems. This may result in data loss. Note that when --force is specified twice the reboot operation is executed by systemctl itself, and the system manager is not contacted. This means the command should succeed even when the system manager has crashed.

   If the optional argument arg is given, it will be passed as the optional argument to the reboot(2) system call. The value is architecture and firmware specific. As an example, "recovery" might be used to trigger system recovery, and "fota" might be used to trigger a “firmware over the air” update.

.. object:: kexec

   Shut down and reboot the system via kexec. This is equivalent to systemctl start kexec.target --job-mode=replace-irreversibly --no-block. This command is asynchronous; it will return after the reboot operation is enqueued, without waiting for it to complete.

   If combined with --force, shutdown of all running services is skipped, however all processes are killed and all file systems are unmounted or mounted read-only, immediately followed by the reboot.

.. object:: exit [EXIT_CODE]

   Ask the service manager to quit. This is only supported for user service managers (i.e. in conjunction with the --user option) or in containers and is equivalent to poweroff otherwise. This command is asynchronous; it will return after the exit operation is enqueued, without waiting for it to complete.

   The service manager will exit with the specified exit code, if EXIT_CODE is passed.

.. object:: switch-root ROOT [INIT]

   Switches to a different root directory and executes a new system manager process below it. This is intended for usage in initial RAM disks ("initrd"), and will transition from the initrd's system manager process (a.k.a. "init" process) to the main system manager process which is loaded from the actual host volume. This call takes two arguments: the directory that is to become the new root directory, and the path to the new system manager binary below it to execute as PID 1. If the latter is omitted or the empty string, a systemd binary will automatically be searched for and used as init. If the system manager path is omitted, equal to the empty string or identical to the path to the systemd binary, the state of the initrd's system manager process is passed to the main system manager, which allows later introspection of the state of the services involved in the initrd boot phase.

.. object:: suspend

   Suspend the system. This will trigger activation of the special target unit suspend.target. This command is asynchronous, and will return after the suspend operation is successfully enqueued. It will not wait for the suspend/resume cycle to complete.

.. object:: hibernate

   Hibernate the system. This will trigger activation of the special target unit hibernate.target. This command is asynchronous, and will return after the hibernation operation is successfully enqueued. It will not wait for the hibernate/thaw cycle to complete.

.. object:: hybrid-sleep

   Hibernate and suspend the system. This will trigger activation of the special target unit hybrid-sleep.target. This command is asynchronous, and will return after the hybrid sleep operation is successfully enqueued. It will not wait for the sleep/wake-up cycle to complete.

パラメータ構文
^^^^^^^^^^^^^^^^

   Unit commands listed above take either a single unit name (designated as UNIT), or multiple unit specifications (designated as PATTERN...). In the first case, the unit name with or without a suffix must be given. If the suffix is not specified (unit name is "abbreviated"), systemctl will append a suitable suffix, ".service" by default, and a type-specific suffix in case of commands which operate only on specific unit types. For example,

   .. code-block:: console

      # systemctl start sshd

   and

   .. code-block:: console

      # systemctl start sshd.service

   are equivalent, as are

   .. code-block:: console

      # systemctl isolate default

   and

   .. code-block:: console

      # systemctl isolate default.target

   Note that (absolute) paths to device nodes are automatically converted to device unit names, and other (absolute) paths to mount unit names.

   .. code-block:: console

      # systemctl status /dev/sda
      # systemctl status /home

   are equivalent to:

   .. code-block:: console

      # systemctl status dev-sda.device
      # systemctl status home.mount

   In the second case, shell-style globs will be matched against the primary names of all units currently in memory; literal unit names, with or without a suffix, will be treated as in the first case. This means that literal unit names always refer to exactly one unit, but globs may match zero units and this is not considered an error.

   Glob patterns use fnmatch(3), so normal shell-style globbing rules are used, and "*", "?", "[]" may be used. See glob(7) for more details. The patterns are matched against the primary names of units currently in memory, and patterns which do not match anything are silently skipped. For example:

   .. code-block:: console

      # systemctl stop sshd@*.service

   will stop all sshd@.service instances. Note that alias names of units, and units that aren't in memory are not considered for glob expansion.

   For unit file commands, the specified UNIT should be the name of the unit file (possibly abbreviated, see above), or the absolute path to the unit file:

   .. code-block:: console

      # systemctl enable foo.service

   or

   .. code-block:: console

      # systemctl link /path/to/foo.service

終了ステータス
---------------

成功時は 0 が返り、失敗時はゼロ以外のコードが返ります。

環境変数
----------

.. envvar:: $SYSTEMD_EDITOR

   ユニットを編集するときに使用数するエディタを指定します。*$EDITOR* と *$VISUAL* を上書きします。*$SYSTEMD_EDITOR*, *$EDITOR*, *$VISUAL* のいずれもが設定されていない場合や空文字に設定されている場合、あるいはコマンドの実行に失敗した場合、systemctl は有名なエディタを次の順番で実行できないか試行します: :doc:`editor.1`, :doc:`nano.1`, :doc:`vim.1`, :doc:`vi.1`。

.. envvar:: $SYSTEMD_PAGER

   Pager to use when --no-pager is not given; overrides $PAGER. If neither $SYSTEMD_PAGER nor $PAGER are set, a set of well-known pager implementations are tried in turn, including less(1) and more(1), until one is found. If no pager implementation is discovered no pager is invoked. Setting this environment variable to an empty string or the value "cat" is equivalent to passing --no-pager.

.. envvar:: $SYSTEMD_LESS

   Override the options passed to less (by default "FRSXMK").

.. envvar:: $SYSTEMD_LESSCHARSET

   Override the charset passed to less (by default "utf-8", if the invoking terminal is determined to be UTF-8 compatible).

関連項目
--------

:doc:`systemd.1`,
:doc:`journalctl.1`,
:doc:`loginctl.1`,
:doc:`machinectl.1`,
:doc:`systemd.unit.5`,
:doc:`systemd.resource-control.5`,
:doc:`systemd.special.7`,
:doc:`wall.1`,
:doc:`systemd.preset.5`,
:doc:`systemd.generator.7`,
:doc:`glob.7`

注釈
-------

.. [#] https://www.freedesktop.org/wiki/Software/systemd/Preset
