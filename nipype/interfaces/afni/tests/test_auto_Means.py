# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import Means


def test_Means_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        count=dict(argstr='-count', ),
        datum=dict(argstr='-datum %s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file_a=dict(
            argstr='%s',
            mandatory=True,
            position=-2,
        ),
        in_file_b=dict(
            argstr='%s',
            position=-1,
        ),
        mask_inter=dict(argstr='-mask_inter', ),
        mask_union=dict(argstr='-mask_union', ),
        non_zero=dict(argstr='-non_zero', ),
        num_threads=dict(
            nohash=True,
            usedefault=True,
        ),
        out_file=dict(
            argstr='-prefix %s',
            name_source='in_file_a',
            name_template='%s_mean',
        ),
        outputtype=dict(),
        scale=dict(argstr='-%sscale', ),
        sqr=dict(argstr='-sqr', ),
        std_dev=dict(argstr='-stdev', ),
        summ=dict(argstr='-sum', ),
    )
    inputs = Means.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Means_outputs():
    output_map = dict(out_file=dict(), )
    outputs = Means.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
