%if %{mdvver} >= 201200
%define __noautoprov 'engine.so'
%else
%define _provides_exceptions engine.so
%endif

Name:		samuel
Version:	0.1.8
Release:	%mkrel 1
Summary:	A Draughts Program
Group:		Games/Boards
License:	GPLv3+
URL:		http://www.johncheetham.com/projects/samuel/
Source:		http://www.johncheetham.com/projects/samuel/%{name}-%{version}.tar.gz
BuildRequires:	imagemagick
BuildRequires:	python-devel
Requires:	pygtk2

%description
A Draughts program for Linux written in Python, GTK, C++.
Derived from the windows program guicheckers.

%prep
%setup -q
%__chmod 644 README

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root %{buildroot}

# icons
for N in 16 32 48 64 128; do convert %{name}.png -resize ${N}x${N} $N.png; done
%__install -D 16.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png
%__install -D 32.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
%__install -D 48.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
%__install -D 64.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
%__install -D 128.png %{buildroot}%{_iconsdir}/hicolor/128x128/apps/%{name}.png

# overwrite the default .desktop file
%__mkdir_p  %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Type=Application
Name=Samuel
Comment=Draughts Game
Comment[ru]=Шахматы
Icon=samuel
Exec=samuel
Terminal=false
Categories=Game;BoardGame;
EOF

%__rm -rf %{buildroot}%{_defaultdocdir}/%{name}-%{version}

%clean
%__rm -rf %{buildroot}

%files
%doc LICENSE README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}*.egg-info
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_iconsdir}/hicolor/*/apps/%{name}.png

