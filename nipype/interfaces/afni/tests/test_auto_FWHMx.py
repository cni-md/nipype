# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import FWHMx


def test_FWHMx_inputs():
    input_map = dict(
        acf=dict(
            argstr='-acf',
            usedefault=True,
        ),
        args=dict(argstr='%s', ),
        arith=dict(
            argstr='-arith',
            xor=['geom'],
        ),
        automask=dict(
            argstr='-automask',
            usedefault=True,
        ),
        combine=dict(argstr='-combine', ),
        compat=dict(argstr='-compat', ),
        demed=dict(
            argstr='-demed',
            xor=['detrend'],
        ),
        detrend=dict(
            argstr='-detrend',
            usedefault=True,
            xor=['demed'],
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        geom=dict(
            argstr='-geom',
            xor=['arith'],
        ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='-input %s',
            mandatory=True,
        ),
        mask=dict(argstr='-mask %s', ),
        out_detrend=dict(
            argstr='-detprefix %s',
            keep_extension=False,
            name_source='in_file',
            name_template='%s_detrend',
        ),
        out_file=dict(
            argstr='> %s',
            keep_extension=False,
            name_source='in_file',
            name_template='%s_fwhmx.out',
            position=-1,
        ),
        out_subbricks=dict(
            argstr='-out %s',
            keep_extension=False,
            name_source='in_file',
            name_template='%s_subbricks.out',
        ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
        unif=dict(argstr='-unif', ),
    )
    inputs = FWHMx.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_FWHMx_outputs():
    output_map = dict(
        acf_param=dict(),
        fwhm=dict(),
        out_acf=dict(),
        out_detrend=dict(),
        out_file=dict(),
        out_subbricks=dict(),
    )
    outputs = FWHMx.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
