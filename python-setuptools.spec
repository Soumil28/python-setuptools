Name:           python-setuptools
Version:        67.6.1
Release:        1%{?dist}
Summary:        Easily download, build, install, upgrade, and uninstall Python packages

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        MIT
URL:            https://github.com/pypa/setuptools
Source:         %{pypi_source setuptools}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'setuptools' generated automatically by pyp2spec.}


%description %_description

%package -n     python3-setuptools
Summary:        %{summary}

%description -n python3-setuptools %_description


%prep
%autosetup -p1 -n setuptools-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%pyproject_check_import


%files -n python3-setuptools -f %{pyproject_files}


%changelog
* Sun Apr 09 2023 Soumil Kadam - 67.6.1-1
- Initial package