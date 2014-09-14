#
# Conditional build:
%bcond_without	mysql		# mysql support
%bcond_without	pgsql		# PostgreSQL support
%bcond_without	odbc		# ODBC support
%bcond_without	radius		# radius support
%bcond_without	carrierroute	# carrierroute support
%bcond_without	ldap		# LDAP support
%bcond_with	osp		# ETSI OSP VoIP Peering support
%bcond_without	geoip		# GeoIP
%bcond_without	json		# json support
%bcond_without	memcached	# memcached support
%bcond_without	microhttpd	# httpd support
%bcond_without	redis		# Redis support

Summary:	SIP proxy, redirect and registrar server
Summary(pl.UTF-8):	Serwer SIP rejestrujący, przekierowujący i robiący proxy
Name:		opensips
Version:	1.8.3
Release:	2
License:	GPL v2
Group:		Networking/Daemons
Source0:	http://opensips.org/pub/opensips/%{version}/src/%{name}-%{version}_src.tar.gz
# Source0-md5:	ead8637ce2b4865418991f5c9564c3ed
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Patch0:		%{name}-curses.patch
URL:		http://www.opensips.org/
%{?with_geoip:BuildRequires:	GeoIP-devel}
%{?with_osp:BuildRequires:	OSPToolkit}
BuildRequires:	bison
BuildRequires:	curl-devel
BuildRequires:	expat-devel
BuildRequires:	flex
%{?with_redis:BuildRequires:	hiredis-devel}
%{?with_json:BuildRequires:	json-c-devel}
%{?with_carrierroute:BuildRequires:	libconfuse-devel}
%{?with_memcached:BuildRequires:	libmemcached-devel}
%{?with_microhttpd:BuildRequires:	libmicrohttpd-devel}
%{?with_pgsql:BuildRequires:	libpqxx-devel}
BuildRequires:	libxml2-devel
BuildRequires:	libxslt-progs
#BuildRequires:	lynx
%{?with_mysql:BuildRequires:	mysql-devel}
BuildRequires:	net-snmp-devel
%{?with_ldap:BuildRequires:	openldap-devel}
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	perl-devel
BuildRequires:	perl-tools-devel
%{?with_radius:BuildRequires:	radiusclient-ng-devel}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.268
#BuildRequires:	subversion
%{?with_odbc:BuildRequires:	unixODBC-devel}
BuildRequires:	which
#BuildRequires:	xmlrpc-c-devel >= 1.10.0
BuildRequires:	zlib-devel
Requires(post,preun):	/sbin/chkconfig
Requires:	rc-scripts
Suggests:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# mi_xmlrpc requires xmlrpc-c-devel in version 1.9 only
# event_rabbitmq requires 'amqp.h'
# cachedb_cassandra requires 'protocol/TBinaryProtocol.h'
# lua: lua.h
%define	exclude_modules	mi_xmlrpc db_oracle event_rabbitmq cachedb_cassandra lua

%description
OpenSIPS (Open SIP Server) is a mature Open Source implementation of a
SIP server. OpenSIPS is more than a SIP proxy/router as it includes
application-level functionalities. OpenSIPS, as a SIP server, is the
core component of any SIP-based VoIP solution. With a very flexible
and customizable routing engine, OpenSIPS 'unifies voice, video, IM
and presence services in a highly efficient way, thanks to its
scalable (modular) design.

%package mysql
Summary:	openSIPS MySQL module
Summary(pl.UTF-8):	Moduł MySQL do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description mysql
MySQL module for openSIPS.

%description mysql -l pl.UTF-8
Moduł MySQL do openSIPS.

%package postgres
Summary:	openSIPS PostgreSQL module
Summary(pl.UTF-8):	Moduł PostgreSQL do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description postgres
PostgreSQL module for openSIPS.

%description postgres -l pl.UTF-8
Moduł PostgreSQL do openSIPS.

%package json
Summary:	openSIPS JSON module
Summary(pl.UTF-8):	Moduł JSON do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description json
JSON module for openSIPS.

%description json -l pl.UTF-8
Moduł JSON do openSIPS.

%package memcached
Summary:	openSIPS memcached module
Summary(pl.UTF-8):	Moduł memcached do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description memcached
Memcached module for openSIPS.

%description memcached -l pl.UTF-8
Moduł memcached do openSIPS.

%package radius
Summary:	openSIPS Radius module
Summary(pl.UTF-8):	Moduł Radius do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description radius
Radius module for openSIPS.

%description radius -l pl.UTF-8
Moduł Radius do openSIPS.

%package odbc
Summary:	openSIPS ODBC module
Summary(pl.UTF-8):	Moduł ODBC do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description odbc
ODBC module for openSIPS.

%description odbc -l pl.UTF-8
Moduł ODBC do openSIPS.

%package perl
Summary:	openSIPS perl and perlvdb modules
Summary(pl.UTF-8):	Moduły perl i perlvdb do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description perl
Perl modules (perl & perlvdb) for openSIPS.

%description perl -l pl.UTF-8
Moduły perl i perlvdb do openSIPS.

%package xmpp
Summary:	openSIPS XMPP/Jabber modules
Summary(pl.UTF-8):	Moduły XMPP/Jabber do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}
Obsoletes:	opensips-jabber

%description xmpp
XMPP/Jabber modules for openSIPS.

%description xmpp -l pl.UTF-8
Moduły XMPP/Jabber do openSIPS.

%package ldap
Summary:	openSIPS LDAP and H350 modules
Summary(pl.UTF-8):	Moduły LDAP i H350 do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description ldap
LDAP and H350 modules for openSIPS.

%description ldap -l pl.UTF-8
Moduły LDAP i H350 do openSIPS.

%package carrierroute
Summary:	openSIPS Carrierroute module
Summary(pl.UTF-8):	Moduł Carrierroute do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description carrierroute
Carrierroute module for openSIPS.

%description carrierroute -l pl.UTF-8
Moduł Carrierroute do openSIPS.

%package osp
Summary:	openSIPS OSP module
Summary(pl.UTF-8):	Moduł OSP do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description osp
OSP module for openSIPS.

%description osp -l pl.UTF-8
Moduł OSP do openSIPS.

%package mmgeoip
Summary:	openSIPS MaxMind GeoIP module
Summary(pl.UTF-8):	Moduł MaxMind GeoIP do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description mmgeoip
MaxMind GeoIP module for openSIPS.

%description mmgeoip -l pl.UTF-8
Moduł MaxMind GeoIP do openSIPS.

%package snmpstats
Summary:	openSIPS SNMP statistics module
Summary(pl.UTF-8):	Moduł do statystyk SNMP do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description snmpstats
openSIPS SNMP statistics module.

%description snmpstats -l pl.UTF-8
Moduł do statystyk SNMP do openSIPS.

%package -n mibs-%{name}
Summary:	MIBs for openSIPS
Summary(pl.UTF-8):	MIB-y dla openSIPS
Group:		Applications/System
Requires:	mibs-dirs
Requires:	mibs-net-snmp
Obsoletes:	opensips-mibs

%description -n mibs-%{name}
MIBs for openSIPS.

%description -n mibs-%{name} -l pl.UTF-8
MIB-y dla openSIPS.

%package redis
Summary:	Redis interface for openSIPS
Summary(pl.UTF-8):	Moduł Redis do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description redis
Redis interface for openSIPS.

%description redis -l pl.UTF-8
Moduł Redis do openSIPS.

%package httpd
Summary:	HTTP interface to openSIPS
Summary(pl.UTF-8):	Interfejs HTTP do openSIPS
Group:		Networking/Daemons
Requires:	%{name} = %{version}-%{release}

%description httpd
HTTP interface to openSIPS.

%description httpd -l pl.UTF-8
Interfejs HTTP do openSIPS.

%prep
%setup -q -n %{name}-%{version}-tls
%patch0 -p1

%build
exclude_modules="%{exclude_modules}"
%if %{without redis}
exclude_modules="$exclude_modules cachedb_redis"
%endif
%if %{without ldap}
exclude_modules="$exclude_modules h350 ldap"
%endif
%if %{without carrierroute}
exclude_modules="$exclude_modules carrierroute"
%endif
%if %{without osp}
exclude_modules="$exclude_modules osp"
%endif
%if %{without microhttpd}
exclude_modules="$exclude_modules httpd"
%endif
%if %{without mysql}
exclude_modules="$exclude_modules db_mysql"
%endif
%if %{without pgsql}
exclude_modules="$exclude_modules db_postgres"
%endif
%if %{without odbc}
exclude_modules="$exclude_modules db_unixodbc"
%endif
%if %{without geoip}
exclude_modules="$exclude_modules mmgeoip"
%endif
%if %{without radius}
exclude_modules="$exclude_modules aaa_radius"
%endif
%if %{without json}
exclude_modules="$exclude_modules json"
%endif
%if %{without memcached}
exclude_modules="$exclude_modules cachedb_memcached"
%endif
echo "$exclude_modules" > exclude_modules
%{__make} all \
	exclude_modules="$exclude_modules" \
	prefix="%{_prefix}" \
	cfg-prefix=$RPM_BUILD_ROOT \
	cfg-target=/etc/opensips/ \
	CC="%{__cc}" \
	PREFIX="%{_prefix}" \
	CFLAGS="%{rpmcflags} -Wcast-align -fPIC" \
	TLS=1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{ser,sysconfig,rc.d/init.d}

exclude_modules="$(cat exclude_modules)"
%{__make} install -j1 \
	exclude_modules="$exclude_modules" \
	prefix="%{_prefix}" \
	basedir=$RPM_BUILD_ROOT \
	cfg-prefix=$RPM_BUILD_ROOT \
	cfg-target=/etc/opensips/ \
	INSTALLMIBDIR=$RPM_BUILD_ROOT%{_datadir}/mibs

for i in modules/*; do \
	i=$(basename $i)
	[ -f modules/$i/README ] && cp -f modules/$i/README README.$i; \
done

# contains the same files we install in %doc
%{__rm} -r  $RPM_BUILD_ROOT%{_docdir}/%{name}

#cd doc/serdev
#docbook2html serdev.sgml
#rm -f serdev.sgml
#cd ../seruser
#docbook2html seruser.sgml
#rm -f seruser.sgml
#cd ../..

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/opensips
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/opensips

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add opensips
%service opensips restart "SIP Daemon"

%preun
if [ "$1" = "0" ]; then
	%service opensips stop
	/sbin/chkconfig --del opensips
fi

%files
%defattr(644,root,root,755)
%doc README* AUTHORS CREDITS ChangeLog INSTALL NEWS scripts examples
%attr(755,root,root) %{_sbindir}/*
%dir %{_sysconfdir}/opensips
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/opensips/opensips.cfg
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/opensips/opensipsctlrc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/opensips/osipsconsolerc
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/opensips
%attr(754,root,root) /etc/rc.d/init.d/opensips
%dir %{_libdir}/opensips
%dir %{_libdir}/opensips/opensipsctl
%{_libdir}/opensips/opensipsctl/*.*
%dir %{_libdir}/opensips/opensipsctl/dbtextdb
%attr(755,root,root) %{_libdir}/opensips/opensipsctl/dbtextdb/dbtextdb.py
%dir %{_libdir}/opensips/modules
# explict list here, no globs please (to avoid mistakes)
%attr(755,root,root) %{_libdir}/opensips/modules/acc.so
%attr(755,root,root) %{_libdir}/opensips/modules/alias_db.so
%attr(755,root,root) %{_libdir}/opensips/modules/auth.so
%attr(755,root,root) %{_libdir}/opensips/modules/auth_aaa.so
%attr(755,root,root) %{_libdir}/opensips/modules/auth_db.so
%attr(755,root,root) %{_libdir}/opensips/modules/auth_diameter.so
%attr(755,root,root) %{_libdir}/opensips/modules/avpops.so
%attr(755,root,root) %{_libdir}/opensips/modules/b2b_entities.so
%attr(755,root,root) %{_libdir}/opensips/modules/b2b_logic.so
%attr(755,root,root) %{_libdir}/opensips/modules/benchmark.so
%attr(755,root,root) %{_libdir}/opensips/modules/cachedb_local.so
%attr(755,root,root) %{_libdir}/opensips/modules/call_control.so
%attr(755,root,root) %{_libdir}/opensips/modules/cfgutils.so
%attr(755,root,root) %{_libdir}/opensips/modules/closeddial.so
%attr(755,root,root) %{_libdir}/opensips/modules/cpl-c.so
%attr(755,root,root) %{_libdir}/opensips/modules/db_berkeley.so
%attr(755,root,root) %{_libdir}/opensips/modules/db_flatstore.so
%attr(755,root,root) %{_libdir}/opensips/modules/db_http.so
%attr(755,root,root) %{_libdir}/opensips/modules/db_text.so
%attr(755,root,root) %{_libdir}/opensips/modules/db_virtual.so
%attr(755,root,root) %{_libdir}/opensips/modules/dialog.so
%attr(755,root,root) %{_libdir}/opensips/modules/dialplan.so
%attr(755,root,root) %{_libdir}/opensips/modules/dispatcher.so
%attr(755,root,root) %{_libdir}/opensips/modules/diversion.so
%attr(755,root,root) %{_libdir}/opensips/modules/dns_cache.so
%attr(755,root,root) %{_libdir}/opensips/modules/domain.so
%attr(755,root,root) %{_libdir}/opensips/modules/domainpolicy.so
%attr(755,root,root) %{_libdir}/opensips/modules/drouting.so
%attr(755,root,root) %{_libdir}/opensips/modules/enum.so
%attr(755,root,root) %{_libdir}/opensips/modules/event_datagram.so
%attr(755,root,root) %{_libdir}/opensips/modules/exec.so
%attr(755,root,root) %{_libdir}/opensips/modules/gflags.so
%attr(755,root,root) %{_libdir}/opensips/modules/group.so
%attr(755,root,root) %{_libdir}/opensips/modules/identity.so
%attr(755,root,root) %{_libdir}/opensips/modules/imc.so
%attr(755,root,root) %{_libdir}/opensips/modules/load_balancer.so
%attr(755,root,root) %{_libdir}/opensips/modules/mangler.so
%attr(755,root,root) %{_libdir}/opensips/modules/maxfwd.so
%attr(755,root,root) %{_libdir}/opensips/modules/mediaproxy.so
%attr(755,root,root) %{_libdir}/opensips/modules/mi_datagram.so
%attr(755,root,root) %{_libdir}/opensips/modules/mi_fifo.so
%attr(755,root,root) %{_libdir}/opensips/modules/msilo.so
%attr(755,root,root) %{_libdir}/opensips/modules/nat_traversal.so
%attr(755,root,root) %{_libdir}/opensips/modules/nathelper.so
%attr(755,root,root) %{_libdir}/opensips/modules/options.so
%attr(755,root,root) %{_libdir}/opensips/modules/path.so
%attr(755,root,root) %{_libdir}/opensips/modules/pdt.so
%attr(755,root,root) %{_libdir}/opensips/modules/peering.so
%attr(755,root,root) %{_libdir}/opensips/modules/permissions.so
%attr(755,root,root) %{_libdir}/opensips/modules/pike.so
%attr(755,root,root) %{_libdir}/opensips/modules/presence.so
%attr(755,root,root) %{_libdir}/opensips/modules/presence_callinfo.so
%attr(755,root,root) %{_libdir}/opensips/modules/presence_dialoginfo.so
%attr(755,root,root) %{_libdir}/opensips/modules/presence_mwi.so
%attr(755,root,root) %{_libdir}/opensips/modules/presence_xcapdiff.so
%attr(755,root,root) %{_libdir}/opensips/modules/presence_xml.so
%attr(755,root,root) %{_libdir}/opensips/modules/pua.so
%attr(755,root,root) %{_libdir}/opensips/modules/pua_bla.so
%attr(755,root,root) %{_libdir}/opensips/modules/pua_dialoginfo.so
%attr(755,root,root) %{_libdir}/opensips/modules/pua_mi.so
%attr(755,root,root) %{_libdir}/opensips/modules/pua_usrloc.so
%attr(755,root,root) %{_libdir}/opensips/modules/python.so
%attr(755,root,root) %{_libdir}/opensips/modules/qos.so
%attr(755,root,root) %{_libdir}/opensips/modules/ratelimit.so
%attr(755,root,root) %{_libdir}/opensips/modules/regex.so
%attr(755,root,root) %{_libdir}/opensips/modules/registrar.so
%attr(755,root,root) %{_libdir}/opensips/modules/rls.so
%attr(755,root,root) %{_libdir}/opensips/modules/rr.so
%attr(755,root,root) %{_libdir}/opensips/modules/rtpproxy.so
%attr(755,root,root) %{_libdir}/opensips/modules/seas.so
%attr(755,root,root) %{_libdir}/opensips/modules/signaling.so
%attr(755,root,root) %{_libdir}/opensips/modules/sipcapture.so
%attr(755,root,root) %{_libdir}/opensips/modules/sipmsgops.so
%attr(755,root,root) %{_libdir}/opensips/modules/siptrace.so
%attr(755,root,root) %{_libdir}/opensips/modules/sl.so
%attr(755,root,root) %{_libdir}/opensips/modules/sms.so
%attr(755,root,root) %{_libdir}/opensips/modules/speeddial.so
%attr(755,root,root) %{_libdir}/opensips/modules/sst.so
%attr(755,root,root) %{_libdir}/opensips/modules/statistics.so
%attr(755,root,root) %{_libdir}/opensips/modules/stun.so
%attr(755,root,root) %{_libdir}/opensips/modules/textops.so
%attr(755,root,root) %{_libdir}/opensips/modules/tlsops.so
%attr(755,root,root) %{_libdir}/opensips/modules/tm.so
%attr(755,root,root) %{_libdir}/opensips/modules/uac.so
%attr(755,root,root) %{_libdir}/opensips/modules/uac_auth.so
%attr(755,root,root) %{_libdir}/opensips/modules/uac_redirect.so
%attr(755,root,root) %{_libdir}/opensips/modules/uac_registrant.so
%attr(755,root,root) %{_libdir}/opensips/modules/uri.so
%attr(755,root,root) %{_libdir}/opensips/modules/userblacklist.so
%attr(755,root,root) %{_libdir}/opensips/modules/usrloc.so
%attr(755,root,root) %{_libdir}/opensips/modules/xcap_client.so
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/db_berkeley
%{_datadir}/%{name}/dbtext
%{_datadir}/%{name}/menuconfig_templates
%{_mandir}/man*/*

%files xmpp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/jabber.so
%attr(755,root,root) %{_libdir}/opensips/modules/xmpp.so
%attr(755,root,root) %{_libdir}/opensips/modules/pua_xmpp.so

%if %{with mysql}
%files mysql
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/db_mysql.so
%{_datadir}/%{name}/mysql
%endif

%if %{with pgsql}
%files postgres
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/db_postgres.so
%{_datadir}/%{name}/postgres
%endif

%if %{with json}
%files json
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/json.so
%endif

%if %{with memcached}
%files memcached
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/cachedb_memcached.so
%endif

%if %{with radius}
%files radius
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/opensips/dictionary.opensips
%attr(755,root,root) %{_libdir}/opensips/modules/aaa_radius.so
%endif

%if %{with odbc}
%files odbc
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/db_unixodbc.so
%endif

%if %{with geoip}
%files mmgeoip
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/mmgeoip.so
%endif

%if %{with ldap}
%files ldap
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/h350.so
%attr(755,root,root) %{_libdir}/opensips/modules/ldap.so
%endif

%if %{with carrierroute}
%files carrierroute
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/carrierroute.so
%endif

%if %{with osp}
%files osp
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/osp.so
%endif

%files snmpstats
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/snmpstats.so

%files perl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/perl.so
%attr(755,root,root) %{_libdir}/opensips/modules/perlvdb.so

%files -n mibs-%{name}
%defattr(644,root,root,755)
%{_datadir}/mibs/*

%if %{with redis}
%files redis
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/cachedb_redis.so
%endif

%if %{with microhttpd}
%files httpd
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/opensips/modules/httpd.so
%attr(755,root,root) %{_libdir}/opensips/modules/mi_http.so
%endif
