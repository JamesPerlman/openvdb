from __future__ import annotations
from typing import List, Optional, Tuple, Union, Iterator, Sequence, Iterable

from typing import overload
import numpy
import torch
from enum import Enum

Numeric = Union[int, float]
TorchDeviceOrString = Union[torch.device, str]
Vec3iBatch = Union[
    torch.Tensor, numpy.ndarray, List[int], List[List[int]], Tuple[int, int, int], List[Tuple[int, int, int]]
]
Vec3dBatch = Union[
    torch.Tensor,
    numpy.ndarray,
    List[float],
    List[List[float]],
    Tuple[float, float, float],
    List[Tuple[float, float, float]],
    Vec3iBatch,
]
Vec3dBatchOrScalar = Union[
    torch.Tensor,
    numpy.ndarray,
    List[float],
    List[List[float]],
    Tuple[float, float, float],
    List[Tuple[float, float, float]],
    float,
    Vec3iBatch,
    int,
]

Vec3i = Union[torch.Tensor, numpy.ndarray, List[int], Tuple[int, int, int]]
Vec3d = Union[torch.Tensor, numpy.ndarray, List[float], Tuple[float, float, float]]
Vec3dOrScalar = Union[Vec3d, float, int]
Vec3iOrScalar = Union[Vec3i, int]
Vec4i = Union[torch.Tensor, numpy.ndarray, List[int], Tuple[int, int, int, int]]

Index = Union[int, slice, type(Ellipsis), None]

GridIdentifier = Union[str, int, List[str], List[int], Tuple[str, ...], Tuple[int, ...]]

LShapeSpec = Union[Iterable[int], Iterable[Iterable[int]]]
RShapeSpec = Iterable[int]

class config:
    enable_ultra_sparse_acceleration: bool = ...
    pedantic_error_checking: bool = ...

class JaggedTensor:
    jdata: torch.Tensor
    def __init__(self, tensor_list: Union[List[List[torch.Tensor]], List[torch.Tensor], torch.Tensor]) -> None: ...
    def cpu(self) -> JaggedTensor: ...
    def cuda(self) -> JaggedTensor: ...
    def double(self) -> JaggedTensor: ...
    def float(self) -> JaggedTensor: ...
    def int(self) -> JaggedTensor: ...
    def long(self) -> JaggedTensor: ...
    def type(self, arg0: torch.dtype) -> JaggedTensor: ...
    def to(self, device: TorchDeviceOrString | torch.dtype) -> JaggedTensor: ...
    def rmask(self, mask: torch.Tensor) -> JaggedTensor: ...
    def __add__(self, other: Union[int, float, JaggedTensor]) -> JaggedTensor: ...
    def __sub__(self, other: Union[int, float, JaggedTensor]) -> JaggedTensor: ...
    def __mul__(self, other: Union[int, float, JaggedTensor]) -> JaggedTensor: ...
    def __pow__(self, other: Union[int, float, JaggedTensor]) -> JaggedTensor: ...
    def __truediv__(self, other: Union[int, float, JaggedTensor]) -> JaggedTensor: ...
    def __floordiv__(self, other: Union[int, float, JaggedTensor]) -> JaggedTensor: ...
    def __mod__(self, other: Union[int, float, JaggedTensor]) -> JaggedTensor: ...
    def __iadd__(self, other: Union[int, float, JaggedTensor]) -> JaggedTensor: ...
    def __isub__(self, other: Union[int, float, JaggedTensor]) -> JaggedTensor: ...
    def __imul__(self, other: Union[int, float, JaggedTensor]) -> JaggedTensor: ...
    def __ipow__(self, other: Union[int, float, JaggedTensor]) -> JaggedTensor: ...
    def __itruediv__(self, other: Union[int, float, JaggedTensor]) -> JaggedTensor: ...
    def __ifloordiv__(self, other: Union[int, float, JaggedTensor]) -> JaggedTensor: ...
    def __imod__(self, other: Union[int, float, JaggedTensor]) -> JaggedTensor: ...
    def __gt__(self, other: Union[int, float, JaggedTensor]) -> JaggedTensor: ...
    def __ge__(self, other: Union[int, float, JaggedTensor]) -> JaggedTensor: ...
    def __lt__(self, other: Union[int, float, JaggedTensor]) -> JaggedTensor: ...
    def __le__(self, other: Union[int, float, JaggedTensor]) -> JaggedTensor: ...
    def __eq__(self, other: Union[int, float, JaggedTensor]) -> JaggedTensor: ...
    def __ne__(self, other: Union[int, float, JaggedTensor]) -> JaggedTensor: ...
    def __getitem__(self, idx: Index | JaggedTensor) -> JaggedTensor: ...
    def __iter__(self) -> Iterator[JaggedTensor]: ...
    def __len__(self) -> int: ...
    def __getstate__(self) -> tuple: ...
    def __setstate__(self, arg0: tuple) -> None: ...
    def detach(self) -> JaggedTensor: ...
    def requires_grad_(self, requires_grad: bool) -> JaggedTensor: ...
    def jagged_like(self, data: torch.Tensor) -> JaggedTensor: ...
    def clone(self) -> JaggedTensor: ...
    def sqrt(self) -> JaggedTensor: ...
    def abs(self) -> JaggedTensor: ...
    def round(self, decimals: int = ...) -> JaggedTensor: ...
    def floor(self) -> JaggedTensor: ...
    def ceil(self) -> JaggedTensor: ...
    def sqrt_(self) -> JaggedTensor: ...
    def abs_(self) -> JaggedTensor: ...
    def round_(self, decimals: int = ...) -> JaggedTensor: ...
    def floor_(self) -> JaggedTensor: ...
    def ceil_(self) -> JaggedTensor: ...

    # def jagged_argsort(self) -> JaggedTensor: ...
    def jsum(self, dim: int = 0, keepdim: bool = False) -> JaggedTensor: ...
    def jmin(self, dim: int = 0, keepdim: bool = False) -> Tuple[JaggedTensor, JaggedTensor]: ...
    def jmax(self, dim: int = 0, keepdim: bool = False) -> Tuple[JaggedTensor, JaggedTensor]: ...
    def jreshape(self, lshape: LShapeSpec) -> JaggedTensor: ...
    def jreshape_as(self, other: JaggedTensor) -> JaggedTensor: ...
    def jflatten(self, dim: int = 0) -> JaggedTensor: ...
    def unbind(self) -> Union[List[torch.Tensor], List[List[torch.Tensor]]]: ...
    @property
    def num_tensors(self) -> int: ...
    @property
    def is_cuda(self) -> bool: ...
    @property
    def is_cpu(self) -> bool: ...
    @property
    def device(self) -> torch.device: ...
    @property
    def dtype(self) -> torch.dtype: ...
    @property
    def jidx(self) -> torch.IntTensor: ...
    @property
    def jlidx(self) -> torch.IntTensor: ...
    @property
    def joffsets(self) -> torch.LongTensor: ...
    @property
    def rshape(self) -> List[int]: ...
    @property
    def lshape(self) -> Union[List[int], List[List[int]]]: ...
    @property
    def ldim(self) -> int: ...
    @property
    def eshape(self) -> List[int]: ...
    @property
    def edim(self) -> int: ...
    @property
    def requires_grad(self) -> bool: ...
    @staticmethod
    def from_data_and_indices(data: torch.Tensor, indices: torch.Tensor, num_tensors: int) -> JaggedTensor: ...
    @staticmethod
    def from_data_indices_and_list_ids(
        data: torch.Tensor, indices: torch.Tensor, list_ids: torch.Tensor, num_tensors: int
    ) -> JaggedTensor: ...
    @staticmethod
    def from_data_and_offsets(data: torch.Tensor, offsets: torch.Tensor) -> JaggedTensor: ...
    @staticmethod
    def from_data_offsets_and_list_ids(
        data: torch.Tensor, offsets: torch.Tensor, list_ids: torch.Tensor
    ) -> JaggedTensor: ...

JaggedTensorOrTensor = Union[torch.Tensor, JaggedTensor]

class GridBatch:
    def __init__(self, device: TorchDeviceOrString = ..., mutable: bool = ...) -> None: ...

    max_grids_per_batch: int = ...

    @property
    def cum_enabled_voxels(self) -> torch.LongTensor: ...
    @property
    def cum_voxels(self) -> torch.LongTensor: ...
    @property
    def device(self) -> torch.device: ...
    @property
    def disabled_mask(self) -> JaggedTensor: ...
    @property
    def enabled_mask(self) -> JaggedTensor: ...
    @property
    def grid_count(self) -> int: ...
    @property
    def ijk(self) -> JaggedTensor: ...
    @property
    def ijk_enabled(self) -> JaggedTensor: ...
    @property
    def jidx(self) -> torch.ShortTensor: ...
    @property
    def joffsets(self) -> torch.LongTensor: ...
    @property
    def mutable(self) -> bool: ...
    @property
    def num_enabled_voxels(self) -> torch.LongTensor: ...
    @property
    def num_voxels(self) -> torch.LongTensor: ...
    @property
    def origins(self) -> torch.FloatTensor: ...
    @property
    def total_enabled_voxels(self) -> int: ...
    @property
    def total_voxels(self) -> int: ...
    @property
    def viz_edge_network(self) -> Tuple[JaggedTensor, JaggedTensor]: ...
    @property
    def voxel_sizes(self) -> torch.FloatTensor: ...
    @property
    def total_bytes(self) -> int: ...
    @property
    def num_bytes(self) -> torch.LongTensor: ...
    @property
    def total_leaf_nodes(self) -> int: ...
    @property
    def num_leaf_nodes(self) -> torch.LongTensor: ...
    @property
    def grid_to_world_matrices(self) -> torch.FloatTensor: ...
    @property
    def world_to_grid_matrices(self) -> torch.FloatTensor: ...
    @property
    def bbox(self) -> torch.IntTensor: ...
    @property
    def dual_bbox(self) -> torch.IntTensor: ...
    @property
    def total_bbox(self) -> torch.IntTensor: ...
    @property
    def address(self) -> int: ...
    def voxel_size_at(self, bi: int) -> torch.FloatTensor: ...
    def origin_at(self, bi: int) -> torch.FloatTensor: ...
    def num_voxels_at(self, bi: int) -> int: ...
    def cum_voxels_at(self, bi: int) -> int: ...
    def num_enabled_voxels_at(self, bi: int) -> int: ...
    def cum_enabled_voxels_at(self, bi: int) -> int: ...
    def bbox_at(self, bi: int) -> torch.IntTensor: ...
    def dual_bbox_at(self, bi: int) -> torch.IntTensor: ...
    def jagged_like(self, data: torch.Tensor, ignore_disabled: bool = ...) -> JaggedTensor: ...
    def set_global_origin(self, origin: Vec3d) -> None: ...
    def set_global_voxel_size(self, voxel_size: Vec3dOrScalar) -> None: ...
    def set_from_dense_grid(
        self,
        num_grids: int,
        dense_dims: Vec3i,
        ijk_min: Vec3i = ...,
        voxel_sizes: Vec3dBatchOrScalar = ...,
        origins: Vec3dBatch = ...,
        mask: Optional[torch.Tensor] = ...,
    ) -> None: ...
    def set_from_ijk(
        self,
        ijk: JaggedTensorOrTensor,
        pad_min: Vec3i = ...,
        pad_max: Vec3i = ...,
        voxel_sizes: Vec3dBatchOrScalar = ...,
        origins: Vec3dBatch = ...,
    ) -> None: ...
    def set_from_nearest_voxels_to_points(
        self, points: JaggedTensorOrTensor, voxel_sizes: Vec3dBatchOrScalar = ..., origins: Vec3dBatch = ...
    ) -> None: ...
    def set_from_points(
        self,
        points: JaggedTensorOrTensor,
        pad_min: Vec3i = ...,
        pad_max: Vec3i = ...,
        voxel_sizes: Vec3dBatchOrScalar = ...,
        origins: Vec3dBatch = ...,
    ) -> None: ...
    def set_from_mesh(
        self,
        mesh_vertices: JaggedTensorOrTensor,
        mesh_faces: JaggedTensorOrTensor,
        voxel_sizes: Vec3dBatchOrScalar = ...,
        origins: Vec3dBatch = ...,
    ) -> None: ...
    def read_from_dense(self, dense_data: torch.Tensor, dense_origins: Vec3iBatch = ...) -> JaggedTensor: ...
    def read_into_dense(
        self, sparse_data: JaggedTensorOrTensor, min_coord: Optional[Vec3iBatch] = ..., grid_size: Optional[Vec3i] = ...
    ) -> torch.Tensor: ...
    def clip(
        self, features: JaggedTensorOrTensor, ijk_min: Vec3iBatch, ijk_max: Vec3iBatch
    ) -> Tuple[JaggedTensor, GridBatch]: ...
    def clipped_grid(self, ijk_min: Vec3iBatch, ijk_max: Vec3iBatch) -> GridBatch: ...
    def dual_grid(self, exclude_border: bool = False) -> GridBatch: ...
    def fill_to_grid(
        self, features: JaggedTensor, other_grid: GridBatch, default_value: float = ...
    ) -> JaggedTensor: ...
    def coarsened_grid(self, coarsening_factor: Vec3iOrScalar) -> GridBatch: ...
    def subdivided_grid(self, subdiv_factor: Vec3iOrScalar, mask: JaggedTensorOrTensor = ...) -> GridBatch: ...
    def max_pool(
        self,
        pool_factor: Vec3iOrScalar,
        data: JaggedTensorOrTensor,
        stride: Vec3iOrScalar = 0,
        coarse_grid: Optional[GridBatch] = None,
    ) -> Tuple[JaggedTensor, GridBatch]: ...
    def avg_pool(
        self,
        pool_factor: Vec3iOrScalar,
        data: JaggedTensorOrTensor,
        stride: Vec3iOrScalar = 0,
        coarse_grid: Optional[GridBatch] = None,
    ) -> Tuple[JaggedTensor, GridBatch]: ...
    def subdivide(
        self,
        subdiv_factor: Vec3iOrScalar,
        data: JaggedTensorOrTensor,
        mask: Optional[JaggedTensorOrTensor] = None,
        fine_grid: Optional[GridBatch] = None,
    ) -> Tuple[JaggedTensor, GridBatch]: ...
    def disable_ijk(self, ijk: JaggedTensorOrTensor) -> None: ...
    def enable_ijk(self, ijk: JaggedTensorOrTensor) -> None: ...
    def points_in_active_voxel(self, xyz: JaggedTensorOrTensor, ignore_disabled: bool = False) -> JaggedTensor: ...
    def coords_in_active_voxel(self, ijk: JaggedTensorOrTensor, ignore_disabled: bool = False) -> JaggedTensor: ...
    def cubes_in_grid(
        self,
        cube_centers: JaggedTensorOrTensor,
        cube_min: Vec3dOrScalar = 0.0,
        cube_max: Vec3dOrScalar = 0.0,
        ignore_disabled: bool = False,
    ) -> JaggedTensor: ...
    def cubes_intersect_grid(
        self,
        cube_centers: JaggedTensorOrTensor,
        cube_min: Vec3dOrScalar = 0.0,
        cube_max: Vec3dOrScalar = 0.0,
        ignore_disabled: bool = False,
    ) -> JaggedTensor: ...
    def ijk_to_index(self, ijk: JaggedTensorOrTensor, cumulative: bool = False) -> JaggedTensor: ...
    def ijk_to_inv_index(self, ijk: JaggedTensorOrTensor, cumulative: bool = False) -> JaggedTensor: ...
    def neighbor_indexes(self, ijk: JaggedTensorOrTensor, extent: int, bitshift: int = 0) -> JaggedTensor: ...
    def splat_bezier(self, points: JaggedTensorOrTensor, points_data: JaggedTensorOrTensor) -> JaggedTensor: ...
    def splat_trilinear(self, points: JaggedTensorOrTensor, points_data: JaggedTensorOrTensor) -> JaggedTensor: ...
    def sample_bezier(self, points: JaggedTensorOrTensor, voxel_data: JaggedTensorOrTensor) -> JaggedTensor: ...
    def sample_bezier_with_grad(
        self, points: JaggedTensorOrTensor, voxel_data: JaggedTensorOrTensor
    ) -> Tuple[JaggedTensor, JaggedTensor]: ...
    def sample_trilinear(self, points: JaggedTensorOrTensor, voxel_data: JaggedTensorOrTensor) -> JaggedTensor: ...
    def sample_trilinear_with_grad(
        self, points: JaggedTensorOrTensor, voxel_data: JaggedTensorOrTensor
    ) -> Tuple[JaggedTensor, JaggedTensor]: ...
    def segments_along_rays(
        self,
        ray_origins: JaggedTensorOrTensor,
        ray_directions: JaggedTensorOrTensor,
        max_segments: int,
        eps: float = 0.0,
        ignore_masked: bool = False,
    ) -> JaggedTensor: ...
    def voxels_along_rays(
        self,
        ray_origins: JaggedTensorOrTensor,
        ray_directions: JaggedTensorOrTensor,
        max_voxels: int,
        eps: float = 0.0,
        return_ijk: bool = True,
        cumulative: bool = False,
    ) -> Tuple[JaggedTensor, JaggedTensor]: ...
    def uniform_ray_samples(
        self,
        ray_origins: JaggedTensorOrTensor,
        ray_directions: JaggedTensorOrTensor,
        t_min: JaggedTensorOrTensor,
        t_max: JaggedTensorOrTensor,
        step_size: float,
        cone_angle: float = 0.0,
        include_end_segments: bool = True,
        return_midpoints: bool = False,
        eps: float = 0.0,
    ) -> JaggedTensor: ...
    def ray_implicit_intersection(
        self,
        ray_origins: JaggedTensorOrTensor,
        ray_directions: JaggedTensorOrTensor,
        grid_scalars: JaggedTensorOrTensor,
        eps: float = 0.0,
    ) -> JaggedTensor: ...
    def grid_to_world(self, ijk: JaggedTensorOrTensor) -> JaggedTensor: ...
    def world_to_grid(self, ijk: JaggedTensorOrTensor) -> JaggedTensor: ...
    def marching_cubes(
        self, field: JaggedTensorOrTensor, level: float = 0.0
    ) -> Tuple[JaggedTensor, JaggedTensor, JaggedTensor]: ...
    def sparse_conv_kernel_map(
        self, kernel_size: Union[int, Sequence], stride: Union[int, Sequence], target_grid: Optional[GridBatch] = None
    ) -> Tuple[SparseConvPackInfo, GridBatch]: ...
    def sparse_conv_halo(self, input: JaggedTensorOrTensor, weight: torch.Tensor, variant: int = 8) -> JaggedTensor: ...
    def is_contiguous(self) -> bool: ...
    def contiguous(self) -> GridBatch: ...
    @overload
    def to(self, device: TorchDeviceOrString) -> GridBatch: ...
    @overload
    def to(self, to_tensor: torch.Tensor) -> GridBatch: ...
    @overload
    def to(self, to_jtensor: JaggedTensor) -> GridBatch: ...
    @overload
    def to(self, to_grid: GridBatch) -> GridBatch: ...
    @overload
    def __getitem__(self, arg0: int) -> GridBatch: ...
    @overload
    def __getitem__(self, arg0: slice) -> GridBatch: ...
    @overload
    def __getitem__(self, arg0: List[int]) -> GridBatch: ...
    @overload
    def __getitem__(self, arg0: List[bool]) -> GridBatch: ...
    @overload
    def __getitem__(self, arg0: torch.Tensor) -> GridBatch: ...
    @overload
    def __getitem__(self, arg0: numpy.ndarray) -> GridBatch: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[GridBatch]: ...
    def __getstate__(self) -> tuple: ...
    def __setstate__(self, arg0: tuple) -> None: ...

class ConvPackBackend(Enum):
    GATHER_SCATTER = 0
    IGEMM = 1
    CUTLASS = 2
    LGGS = 3

class SparseConvPackInfo:
    def __init__(
        self,
        kernel_size: Vec3iOrScalar,
        stride: Vec3iOrScalar,
        source_grid: GridBatch,
        target_grid: Optional[GridBatch],
    ) -> None: ...
    def sparse_conv_3d(
        self,
        input: JaggedTensorOrTensor,
        weights: torch.Tensor,
        backend: ConvPackBackend = ConvPackBackend.GATHER_SCATTER,
    ) -> JaggedTensor: ...
    def sparse_transpose_conv_3d(
        self,
        input: JaggedTensorOrTensor,
        weights: torch.Tensor,
        backend: ConvPackBackend = ConvPackBackend.GATHER_SCATTER,
    ) -> JaggedTensor: ...
    @property
    def kernel_size(self) -> Tuple: ...
    @property
    def neighborhood_map(self) -> torch.Tensor: ...
    @property
    def neighborhood_sizes(self) -> torch.Tensor: ...
    @property
    def out_in_map(self) -> torch.Tensor: ...
    @property
    def reorder_loc(self) -> torch.Tensor: ...
    @property
    def sorted_mask(self) -> torch.Tensor: ...
    @property
    def reduced_sorted_mask(self) -> torch.Tensor: ...
    @property
    def reorder_out_in_map(self) -> torch.Tensor: ...
    @property
    def out_in_map_bwd(self) -> torch.Tensor: ...
    @property
    def reorder_loc_bwd(self) -> torch.Tensor: ...
    @property
    def sorted_mask_bwd_w(self) -> torch.Tensor: ...
    @property
    def sorted_mask_bwd_d(self) -> torch.Tensor: ...
    @property
    def reorder_out_in_map_bwd(self) -> torch.Tensor: ...
    @property
    def halo_index_buffer(self) -> torch.Tensor: ...
    @property
    def output_index_buffer(self) -> torch.Tensor: ...
    @property
    def block_kernel_ranges(self) -> torch.Tensor: ...
    @property
    def block_kernel_rel_out_idx(self) -> torch.Tensor: ...
    @property
    def block_kernel_in_idx(self) -> torch.Tensor: ...
    @property
    def source_grid(self) -> GridBatch: ...
    @property
    def stride(self) -> Tuple: ...
    @property
    def target_grid(self) -> GridBatch: ...
    def build_gather_scatter(self, use_me: bool = False) -> None: ...
    def build_implicit_gemm(
        self,
        sorted: bool = False,
        split_mask_num: int = 1,
        training: bool = False,
        split_mask_num_bwd: int = 1,
        use_tf32: bool = False,
    ) -> None: ...
    def build_cutlass(self, benchmark: bool = False) -> None: ...
    def build_lggs(self) -> None: ...

@overload
def jcat(grid_batches: List[GridBatch]) -> GridBatch: ...
@overload
def jcat(jagged_tensors: List[JaggedTensorOrTensor], dim: int | None = ...) -> JaggedTensor: ...
def sparse_grid_from_ijk(
    ijk: JaggedTensorOrTensor,
    pad_min: Vec3i = ...,
    pad_max: Vec3i = ...,
    voxel_sizes: Vec3dBatchOrScalar = ...,
    origins: Vec3dBatch = ...,
    mutable: bool = ...,
) -> GridBatch: ...
def sparse_grid_from_nearest_voxels_to_points(
    points: JaggedTensorOrTensor, voxel_sizes: Vec3dBatchOrScalar = ..., origins: Vec3dBatch = ..., mutable: bool = ...
) -> GridBatch: ...
def sparse_grid_from_points(
    points: JaggedTensorOrTensor,
    pad_min: Vec3i = ...,
    pad_max: Vec3i = ...,
    voxel_sizes: Vec3dBatchOrScalar = ...,
    origins: Vec3dBatch = ...,
    mutable: bool = ...,
) -> GridBatch: ...
def sparse_grid_from_dense(
    num_grids: int,
    dense_dims: Vec3i,
    ijk_min: Vec3i = ...,
    voxel_sizes: Vec3dBatchOrScalar = ...,
    origins: Vec3dBatch = ...,
    device: TorchDeviceOrString = ...,
    mutable: bool = ...,
) -> GridBatch: ...
def sparse_grid_from_mesh(
    vertices: JaggedTensorOrTensor,
    faces: JaggedTensorOrTensor,
    voxel_sizes: Vec3dBatchOrScalar = ...,
    origins: Vec3dBatch = ...,
    device: TorchDeviceOrString = ...,
    mutable: bool = ...,
) -> GridBatch: ...
def volume_render(
    sigmas: torch.Tensor,
    rgbs: torch.Tensor,
    deltaTs: torch.Tensor,
    ts: torch.Tensor,
    packInfo: torch.Tensor,
    transmittanceThresh: float,
) -> List[torch.Tensor]: ...
def load(
    path: str, grid_id: Optional[GridIdentifier] = None, device: TorchDeviceOrString = "cpu", verbose: bool = False
) -> Tuple[GridBatch, JaggedTensor, list[str]]: ...
def save(
    path: str,
    grid: GridBatch,
    data: Optional[JaggedTensorOrTensor] = None,
    names: Optional[Union[str, List[str]]] = None,
    compressed: bool = False,
    verbose: bool = False,
): ...
def jrand(
    lsizes: LShapeSpec,
    rsizes: RShapeSpec | None = None,
    dtype: torch.dtype | None = None,
    device: TorchDeviceOrString | None = None,
    requires_grad: bool = False,
    pin_memory: bool = False,
) -> JaggedTensor: ...
def jrandn(
    lsizes: LShapeSpec,
    rsizes: RShapeSpec | None = None,
    dtype: torch.dtype | None = None,
    device: TorchDeviceOrString | None = None,
    requires_grad: bool = False,
    pin_memory: bool = False,
) -> JaggedTensor: ...
def jones(
    lsizes: LShapeSpec,
    rsizes: RShapeSpec | None = None,
    dtype: torch.dtype | None = None,
    device: TorchDeviceOrString | None = None,
    requires_grad: bool = False,
    pin_memory: bool = False,
) -> JaggedTensor: ...
def jzeros(
    lsizes: LShapeSpec,
    rsizes: RShapeSpec | None = None,
    dtype: torch.dtype | None = None,
    device: TorchDeviceOrString | None = None,
    requires_grad: bool = False,
    pin_memory: bool = False,
) -> JaggedTensor: ...
def jempty(
    lsizes: LShapeSpec,
    rsizes: RShapeSpec | None = None,
    dtype: torch.dtype | None = None,
    device: TorchDeviceOrString | None = None,
    requires_grad: bool = False,
    pin_memory: bool = False,
) -> JaggedTensor: ...
