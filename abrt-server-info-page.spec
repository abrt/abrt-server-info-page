Summary: Web page with summary of ABRT services
Name: abrt-server-info-page
Version: 1.5
Release: 1%{?dist}
License: GPLv3+
URL: https://github.com/marusak/abrt-server-info-page
# source is created by:
# git clone
# cd abrt-server-info-page; tito build --tgz
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch

BuildRequires: python2-devel

%if 0%{?rhel} > 7 || 0%{?fedora} > 27
Requires: python2-flask >= 0.10
Requires: python2-mod_wsgi
%else
Requires: python-flask >= 0.10
Requires: mod_wsgi
%endif
Requires: httpd
Requires(post): systemd

%description
Web page for use as front page of ABRT servers. Contains information about
ABRT's products.

%prep
%setup -q

%install
mkdir -p %{buildroot}
mkdir -p %{buildroot}/%{python_sitelib}/abrt-server-info-page/static
mkdir -p %{buildroot}/%{python_sitelib}/abrt-server-info-page/static/js
mkdir -p %{buildroot}/%{python_sitelib}/abrt-server-info-page/static/css
mkdir -p %{buildroot}/%{python_sitelib}/abrt-server-info-page/static/fonts
mkdir -p %{buildroot}/%{python_sitelib}/abrt-server-info-page/templates
mkdir -p %{buildroot}/%{_sysconfdir}/httpd/conf.d
cp -a abrt_server_info_page.py %{buildroot}/%{python_sitelib}/abrt-server-info-page
cp -a abrt_server_info_page.wsgi %{buildroot}/%{python_sitelib}/abrt-server-info-page
cp -a config.py %{buildroot}/%{python_sitelib}/abrt-server-info-page
cp -a config/abrt-server-info-page.conf %{buildroot}/%{_sysconfdir}/httpd/conf.d/
cp -a templates/index.html %{buildroot}/%{python_sitelib}/abrt-server-info-page/templates
cp -a static/* %{buildroot}/%{python_sitelib}/abrt-server-info-page/static

%files
%config(noreplace) %{_sysconfdir}/httpd/conf.d/abrt-server-info-page.conf
%{python_sitelib}/abrt-server-info-page
%license LICENSE

%post
systemctl condrestart httpd

%changelog
* Wed Mar 21 2018 Miroslav Suchý <msuchy@redhat.com> 1.5-1
- require systemd
- Update Python 2 dependency declarations to new packaging standards
  (mmarusak@redhat.com)

* Thu Jan 11 2018 Martin Kutlak <mkutlak@redhat.com> 1.4-1
- swap links (msuchy@redhat.com)

* Wed Apr 12 2017 Miroslav Suchý <msuchy@redhat.com> 1.3-1
- add link to wiki (msuchy@redhat.com)
- add missing quotes (msuchy@redhat.com)
- Add retrace server's disclaimer (mmarusak@redhat.com)

* Sat Feb 04 2017 Matej Marusak <marusak.matej@gmail.com> 1.2-1
- Add license into specfile (marusak.matej@gmail.com)
- Add BuildRequires into specfile (marusak.matej@gmail.com)
- Create LICENSE (marusak.matej@gmail.com)
- Fix wrong command in specfile (mmarusak@redhat.com)
- Add README (marusak.matej@gmail.com)
- Remove unused BuildRequires from specfile (marusak.matej@gmail.com)
* Thu Jan 19 2017 Matej Marusak <mmarusak@redhat.com> 1.1-1
- Initial package

