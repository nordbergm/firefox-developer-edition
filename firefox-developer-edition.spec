Name:           firefox-developer-edition
Version:        74.0b9
Release:        1%{?dist}
Summary:        Firefox Developer Edition
License:        Mozilla Public License, GPL
URL:            https://www.mozilla.org/en-US/firefox/

Source0:        https://download-installer.cdn.mozilla.net/pub/devedition/releases/%{version}/linux-x86_64/en-US/firefox-%{version}.tar.bz2
Source1:        firefox-developer-edition.desktop

%description
Firefox Developer Edition

%install
install -d %{buildroot}/opt/%{name}
tar -xvf %{SOURCE0}
cp -r firefox/* %{buildroot}/opt/%{name}/
install -d -m 0755 %{buildroot}%{_datadir}/applications
install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
/opt/%{name}/
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Mar 4 2020 Mattias Nordberg <mattias.nordberg@gmail.com> - 74.0b9-1
- Bump to version 74.0b9

* Fri Dec 20 2019 Josh Locash <locashjosh@gmail.com> - 72.0b9-1
- Bump to version 72.0b9

* Wed Dec 18 2019 Josh Locash <locashjosh@gmail.com> - 72.0b8-1
- Bump to version 72.0b8

* Mon Dec 16 2019 Josh Locash <locashjosh@gmail.com> - 72.0b7-1
- Bump to version 72.0b7

* Fri Dec 13 2019 Josh Locash <locashjosh@gmail.com> - 72.0b6-1
- Bump to version 72.0b6

* Wed Dec 11 2019 Josh Locash <locashjosh@gmail.com> - 72.0b5-1
- Bump to version 72.0b5

* Tue Dec 10 2019 Josh Locash <locashjosh@gmail.com> - 72.0b4-1
- Initial RPM release
