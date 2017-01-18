Summary: Web page with summary of ABRT services
Name: abrt-server
Version: 1.1
Release: 1%{?dist}
License: GPLv3+
Group: Applications/Internet
URL: https://github.com/marusak/Abrt-server
Source0: abrt-server-1.0.tar.gz

BuildArch: noarch

BuildRequires: intltool
BuildRequires: libtool
BuildRequires: texinfo
BuildRequires: asciidoc
BuildRequires: xmlto

Requires: python-flask >= 0.10
Requires: httpd
Requires: mod_wsgi

%define _unpackaged_files_terminate_build 0 

%description
Web page for use as front page of ABRT servers. Contains information about
ABRT's products.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/%{python_sitelib}/Abrt-server/static
mkdir -p ${RPM_BUILD_ROOT}/%{python_sitelib}/Abrt-server/static/js
mkdir -p ${RPM_BUILD_ROOT}/%{python_sitelib}/Abrt-server/static/css
mkdir -p ${RPM_BUILD_ROOT}/%{python_sitelib}/Abrt-server/static/fonts
mkdir -p ${RPM_BUILD_ROOT}/%{python_sitelib}/Abrt-server/templates
mkdir -p ${RPM_BUILD_ROOT}/%{_sysconfdir}/httpd/conf.d
install -m 644  abrt-server-1.0/abrt_server.py ${RPM_BUILD_ROOT}/%{python_sitelib}/Abrt-server
install -m 644 abrt-server-1.0/abrt_server.wsgi ${RPM_BUILD_ROOT}/%{python_sitelib}/Abrt-server
install -m 644 abrt-server-1.0/config.py ${RPM_BUILD_ROOT}/%{python_sitelib}/Abrt-server
install -m 644 abrt-server-1.0/config/abrt-server.conf ${RPM_BUILD_ROOT}/%{_sysconfdir}/httpd/conf.d
install -m 644 abrt-server-1.0/templates/index.html ${RPM_BUILD_ROOT}/%{python_sitelib}/Abrt-server/templates
install -m 644 abrt-server-1.0/static/fonts/* ${RPM_BUILD_ROOT}/%{python_sitelib}/Abrt-server/static/fonts
install -m 644 abrt-server-1.0/static/css/* ${RPM_BUILD_ROOT}/%{python_sitelib}/Abrt-server/static/css
install -m 644 abrt-server-1.0/static/js/* ${RPM_BUILD_ROOT}/%{python_sitelib}/Abrt-server/static/js
install -m 644 abrt-server-1.0/static/abrt-logo.png ${RPM_BUILD_ROOT}/%{python_sitelib}/Abrt-server/static/abrt-logo.png

%post
/sbin/install-info %{_infodir}/%{name} %{_infodir}/dir 2> /dev/null || :

%preun
if [ "$1" = 0 ]
then
    /sbin/install-info --delete %{_infodir}/%{name} %{_infodir}/dir 2> /dev/null || :
fi

%files
%config(noreplace) %{_sysconfdir}/httpd/conf.d/abrt-server.conf

%dir %{python_sitelib}/Abrt-server
%{python_sitelib}/Abrt-server/abrt_server.py
%{python_sitelib}/Abrt-server/abrt_server.wsgi
%{python_sitelib}/Abrt-server/config.py

%dir %{python_sitelib}/Abrt-server/templates
%{python_sitelib}/Abrt-server/templates/index.html

%dir %{python_sitelib}/Abrt-server/static
%dir %{python_sitelib}/Abrt-server/static/js
%dir %{python_sitelib}/Abrt-server/static/css
%dir %{python_sitelib}/Abrt-server/static/fonts
%{python_sitelib}/Abrt-server/static/fonts/*.otf
%{python_sitelib}/Abrt-server/static/fonts/*.woff
%{python_sitelib}/Abrt-server/static/fonts/*.eot
%{python_sitelib}/Abrt-server/static/fonts/*.svg
%{python_sitelib}/Abrt-server/static/fonts/*.ttf
%{python_sitelib}/Abrt-server/static/css/*.css
%{python_sitelib}/Abrt-server/static/js/*.js
%{python_sitelib}/Abrt-server/static/abrt-logo.png

%changelog
* Wed Jan 18 2017 Matej Marusak <mmarusak@redhat.com> 1.0-1
- Initial version of the package
