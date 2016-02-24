import click
from lib import generate_records_from_fastq, wrapper


def main_routine(forward, reverse, barcode):
    wrapper(forward, reverse, barcode)


@click.command(
    context_settings=dict(help_option_names=['-h', '--help']),
    help=('Pretty straight forward demultiplexing algorithm.'
    )
)
@click.option(
    '-f', '--forward', required=True,
    help='Path to forward read file.', type=click.File()
)
@click.option(
    '-r', '--reverse', required=True, help='Path to reverse read file.',
    type=click.File()
)
@click.option(
    '-b', '--barcode', required=True, help='Path to barcode read file.',
    type=click.File()
)
def demultiplex(forward, reverse, barcode):
    main_routine(forward, reverse, barcode)


if __name__ == "__main__":
    demultiplex()