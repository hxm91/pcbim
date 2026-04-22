This project demonstrates an end-to-end pipeline for the semantic segmentation of large-scale LiDAR point clouds, specifically optimized for **Scan-to-BIM** workflows.
## 🚀 Overview
The core challenge in BIM automation is the efficient processing of dense 3D scans. This implementation utilizes **RangeNet++**, projecting 3D point clouds into 2D spherical range images. This allows for high-speed inference while maintaining structural consistency.
### Key Technical Features:
- **Custom LAS Preprocessing:** Integration of `laspy` for handling terrestrial laser scans (TLS).
- **Spherical Projection:** Mapping 3D XYZ coordinates to 2D range/intensity grids.
- **BIM-Class Mapping:** Scalable dictionary-based remapping of raw LIDAR classifications to architectural BIM classes (Walls, Floors, Ceilings).
- **Post-Processing Ready:** Prepared for kNN-filtering to ensure sharp object boundaries in 3D space.
## Project details
###  data
This project use data from Heritage Pointcloud Instance Collection (HePIC)
URL to download the data: https://drive.google.com/drive/folders/1NmRegFS9HQQx7IJ7Klpn8mgWbW6bv9Eo
based on: https://github.com/LTTM/Scan-to-BIM
#### view the data
view the example gelabeled point cloud 
<img width="1400" height="1000" alt="pointcloud_view1_from_a_better_view" src="https://github.com/user-attachments/assets/5f43fc19-74c9-4892-947b-5bbba06e6c5b" />
view the example gelabeled point cloud in range image form, approach 1
<img width="2898" height="1484" alt="range_and_label_image" src="https://github.com/user-attachments/assets/87471358-ff78-4f5a-aeca-b688fc2b16db" />

### 🛠 Installation
