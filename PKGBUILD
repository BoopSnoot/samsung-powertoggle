# Maintainer: Dmitry Grebenin <grebenin.dmitry@gmail.com>

_name=samsung_powertoggle
pkgname=python-samsungpowertoggle
pkgver=1.0.0
pkgrel=1
pkgdesc='Samsung Smart TV power toggle'
url='https://github.com/BoopSnoot/samsung-wakeonlan'
arch=('any')
license=('LGPL-3.0')
depends=('python>=3.10' 'python-samsungtvws' 'python-requests')
makedepends=('python-build' 'python-installer' 'python-wheel')
source=("$url/releases/download/v$pkgver/v$pkgver.tar.gz")
sha256sums=('')

build() {
	cd $_name-$pkgver
	python -m build --wheel --no-isolation
}

package() {
	cd $_name-$pkgver
	python -m installer --destdir="$pkgdir" dist/*.whl
	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
