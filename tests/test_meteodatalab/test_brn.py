# Third-party
from numpy.testing import assert_allclose

# First-party
import meteodatalab.operators.brn as mbrn
from meteodatalab.data_source import DataSource
from meteodatalab.grib_decoder import load
from meteodatalab.metadata import set_origin_xy


def test_brn(data_dir, fieldextra):
    datafile = data_dir / "COSMO-1E/1h/ml_sl/000/lfff00000000"
    cdatafile = data_dir / "COSMO-1E/1h/const/000/lfff00000000c"

    source = DataSource(datafiles=[datafile, cdatafile])
    ds = load(source, {"param": ["P", "T", "QV", "U", "V", "HHL", "HSURF"]})
    set_origin_xy(ds, "HHL")

    brn = mbrn.fbrn(
        ds["P"], ds["T"], ds["QV"], ds["U"], ds["V"], ds["HHL"], ds["HSURF"]
    )

    assert brn.parameter == {
        "centre": "lssw",
        "paramId": 503154,
        "shortName": "BRN",
        "units": "Numeric",
        "name": "Bulk Richardson number",
    }

    fs_ds = fieldextra("BRN")

    assert_allclose(fs_ds["BRN"], brn, rtol=5e-3, atol=5e-2)
