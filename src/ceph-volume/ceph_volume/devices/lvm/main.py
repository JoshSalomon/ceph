import argparse
from textwrap import dedent
from ceph_volume import terminal
from . import activate
from . import deactivate
from . import prepare
from . import create
from . import trigger
from . import listing
from . import zap
from . import batch


class LVM(object):

    help = 'Use LVM and LVM-based technologies to deploy OSDs'

    _help = dedent("""
    Use LVM and LVM-based technologies to deploy OSDs

    {sub_help}
    """)

    mapper = {
        'activate': activate.Activate,
        'deactivate': deactivate.Deactivate,
        'batch': batch.Batch,
        'prepare': prepare.Prepare,
        'create': create.Create,
        'trigger': trigger.Trigger,
        'list': listing.List,
        'zap': zap.Zap,
    }

    def __init__(self, argv):
        self.argv = argv

    def print_help(self, sub_help):
        return self._help.format(sub_help=sub_help)

    def main(self):
        terminal.dispatch(self.mapper, self.argv)
        parser = argparse.ArgumentParser(
            prog='ceph-volume lvm',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=self.print_help(terminal.subhelp(self.mapper)),
        )
        parser.parse_args(self.argv)
        if len(self.argv) <= 1:
            return parser.print_help()
