"""Radiation related operators."""

# Third-party
import xarray as xr


def compute_athd_s(athb_s: xr.DataArray, tsurf: xr.DataArray) -> xr.DataArray:
    """Compute incoming longwave radiation at surface level.

    Parameters
    ----------
    athb_s : xarray.DataArray
        Net long-wave radiation flux at surface [W m-2]
    tsurf : xarray.DataArray
        Temperature at surface [K]

    Returns
    -------
    xarray.DataArray
        Average downward longwave radiation at the surface [W m-2]

    """
    pc_emissivity_surface = 0.996
    pc_boltzman_cst = 5.6697e-8
    return athb_s / pc_emissivity_surface + pc_boltzman_cst * tsurf**4