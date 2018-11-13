import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_phpcs_is_installed(host):
    f = host.file('/usr/local/bin/phpcs')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_phpcbf_is_installed(host):
    f = host.file('/usr/local/bin/phpcbf')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
