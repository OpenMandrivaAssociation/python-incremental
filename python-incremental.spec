Summary:	Library for versioning Python projects
Name:		python-incremental
Version:	16.10.1
Release:	2
License:	MIT
Group:		Development/Python
Url:		https://pypi.org/project/incremental/
Source0:	https://files.pythonhosted.org/packages/da/b0/32233c9e84b0d44b39015fba8fec03e88053723c1b455925081dc6ccd9e7/incremental-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python)
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
%apply_patches

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
