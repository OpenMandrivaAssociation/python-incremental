Summary:	Library for versioning Python projects
Name:		python-incremental
Version:	21.3.0
Release:	2
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/incremental/
Source0:	https://files.pythonhosted.org/packages/4f/c5/430765c697afc217c8491785de321a21fa4d983dda14bcd82feb965b0593/incremental-21.3.0.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-setuptools
BuildArch:	noarch

%description
Library for versioning Python projects

%package -n python2-incremental
Summary:	Library for versioning Python 2.x projects
Group:		Development/Python

%description -n python2-incremental
Library for versioning Python 2.x projects

%prep
%setup -qn incremental-%{version}
%autopatch -p1

mkdir python2
mv `ls |grep -v python2` python2
cp -a python2 python3

%build
cd python2
python2 setup.py build

cd ../python3
python setup.py build

%install
cd python2
python2 setup.py install --root=%{buildroot}

cd ../python3
python setup.py install --root=%{buildroot}

%files
%defattr(0644,root,root,0755)
%{py_sitedir}/incremental
%{py_sitedir}/*.egg-info

%files -n python2-incremental
%{py2_puresitedir}/incremental
%{py2_puresitedir}/*.egg-info
