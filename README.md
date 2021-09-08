# 128T Application pack Module for ~ 150 Applications

This AppID module will identify traffic associated with ca. 150 Applications. adding this module to your system will identify the all new application-name with various names which can then be prioritized using service-policy, service-route handling, etc.

Please reference this in the `application-name` field of the service you create.
In order to identify application name go to Authority -> Routers -> <Router name> -> Applications seen
The name must be copied exactly in the `application-name` field.


## Installing AppID Module

yum -i install git
cd /etc/128technology/application-modules/
git clone 
chmod +x application-pack.py

## Configuring your 128T to use the Module

Each of the 128T application modules in this repository uses a specific NAME (the naming convention in these modules will use ALL CAPS) that needs to be configured within a `service` definition on your 128T. This NAME will be referenced in the `application-name` field in the configuration. For example:

```
admin@labsystem# show config running authority service ZOOM

config

    authority

        service  ZOOM
            name                  ZOOM

            description           "Zoom meetings"
            scope                 private
            application-name      ZOOM

            access-policy         trusted
                source      trusted
                permission  allow
            exit
            service-policy        voip-video
            share-service-routes  false
        exit
    exit
exit
```

In the case of the Zoom plugin, the `application-name` is ZOOM. The README.md file for each of the modules will indicate its `application-name`.

After configuring the service, don't forget to configure a `service-route` following the basic principles of 128T configuration design. For more information, [review our documentation](https://docs.128technology.com/docs/concepts_glossary/#service-routes).





Current list of applications:
Auth
BGP
Biff
BitTorrent
CC-MAIL
CMD
CMIP-Agent
CMIP-MAN
CORBA-IIOP
CORBA-IIOP-SSL
CYBERCASH
CharGen
Chat
Citrix
Citrix DataCollect
Citrix ICA
Citrix IMA Client
Citrix MGMT Console
DHCP-Client
DHCP-Server
DHCPv6
Direct Connect
ECHO
eDonkey
EXEC
ExoSee
EyeBall
FINGER
FTP
FTP-DATA
FTPS
FTPS-DATA
FireChat
Flash Media
GOPHER
Gnutella
H.323
H323HOSTCALLSC
HTTP-Proxy
Hotline
ICQ - Other
ICQ Chat
IKE
IMAP2
IMAP3
IMAPS
IPXOIP
IRC
IRC SSL
Jabber
KaZaA
KuGoo
LDAP
LDAPS
LOTUS-NOTES
Local MGMT
MGCP
MS Exchange
MS-RDP-CLIENT
MS-SQL-SERVER
MSN - Other
MYTH
Madster-AIMSTER
Manolito
Mute
NETBIOS-IP
NETWARE-IP
NFS
NNTP
NNTP SSL
NPP
NTP
Napster
Net2Phone
NetShow
ORACLE-COAUTHOR
ORACLE-EM1
ORACLE-EM2
ORACLE-NET8CMAN
ORACLE-NET8CMAN-ADMIN
ORACLE-ORASRV
ORACLE-REMOTE-DATABASE
ORACLE-TLISRV
ORACLE-VP1
ORACLE-VP2
ORACLENAMES
Oracle
Other Games
PHILIPS-VC
POP2
POP3
POP3 SSL
PPTP
PRINT-SRV
PRINTER
PcAnywhere
QNext
RADIUS
RADIUS-ACCT
RCP
RIP
RLOGIN
RMON
RTELNET
RTSP
SAP
SAP-DIALOGSERVICE
SAP-INFOSERVICE
SAP-ROUTER
SAP-TO-ADABAS
SAP-TO-INFORMIX
SIP
SMB
SMTP
SNMP
SNMP-TRAP
SQL-NET
SQLSERV
SQLSERVICE
SSH
SUGP
SUNRPC
SYSLOG
Scydo
Skinny
Skype
Soribada
SoulSeek
Starcraft II
T.120
TACACS
Talkdesk
TELNETS
TFTP
TIME
TIMESERVER
Tango
Telnet
Thunder
VOCALTEC-IPHONE
WHO
WHOIS
Waste
WinMX
X11
XFire
Yahoo Chat


# 128T AppID Modules

This repository contains scripts for use with your 128T *Session Smart Router*, to extend its application identification capability. For more information on the 128T's Application Identification behavior, and how to configure AppID modules, refer to our [user documentation](https://docs.128technology.com/docs/concepts_appid#appid-using-modules).

## About AppID Modules

Generally, AppID modules are scripts placed on the 128T's filesystem that generate JSON output to `/var/run/128technology/application-modules/`. This JSON output is dynamically, and periodically ingested by the 128T to create FIB entries for a designated `service` within the 128T's configuration.

Each module can specify its time to live; after this TTL expires, the 128T will re-execute the AppID script and (re)generate the JSON file.

## Installing AppID Modules

Copy the script (e.g., `zoom.py`) to `/etc/128technology/application-modules` on the target router. Ensure the permissions are correct using the command `chmod +x zoom.py`. You can test that the script is executable and functioning properly by running it manually: `./zoom.py`. You should see it create a file named `/var/run/128technology/application-modules/zoom.json`, with a number of prefixes contained in it.

## Configuring your 128T to use the Module

Each of the 128T application modules in this repository uses a specific NAME (the naming convention in these modules will use ALL CAPS) that needs to be configured within a `service` definition on your 128T. This NAME will be referenced in the `application-name` field in the configuration. For example:

```
admin@labsystem1.fiedler# show config running authority service ZOOM

config

    authority

        service  ZOOM
            name                  ZOOM

            description           "Zoom meetings"
            scope                 private
            application-name      ZOOM

            access-policy         trusted
                source      trusted
                permission  allow
            exit
            service-policy        voip-video
            share-service-routes  false
        exit
    exit
exit
```

In the case of the Zoom plugin, the `application-name` is ZOOM. The README.md file for each of the modules will indicate its `application-name`.

After configuring the service, don't forget to configure a `service-route` following the basic principles of 128T configuration design. For more information, [review our documentation](https://docs.128technology.com/docs/concepts_glossary/#service-routes).
