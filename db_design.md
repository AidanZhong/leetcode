[toc]

**此数据库设计遵从BCNF范式**

# 开采用户表
表名：mine_user
|属性名称|属性类型|约束|备注|
|-|-|-|-|
|id|varchar(50)|主键||
|user_name|varchar(50)|unique||

# 证书与用户关联关系表
表名：certificate_user_map
|属性名称|属性类型|约束|备注|
|-|-|-|-|
|cert_id|varchar(50)|外键(certificate.id)||
|user_id|varchar(50)|外键(user.id)||

# 证书表
表名：certificate
|属性名称|属性类型|约束|备注|
|-|-|-|-|
|id|varchar(50)|主键|||
|cert_name|varchar(50)||证书名称|

# 证书和许可关系表
表名：certificate_permission_map
|属性名称|属性类型|约束|备注|
|-|-|-|-|
|cert_id|varchar(50)|外键(certificate.id)||
|permission|varchar(50)||此证书，允许开采x矿物，或驾驶y车辆|

联合主键：cert_id + permission

# 矿区位置边界表
表名：mine_zone_border
|属性名称|属性类型|约束|备注|
|-|-|-|-|
|id|varchar(50)|主键||
|start_lon|varchar(20)||起始点经度|
|start_lat|varchar(20)||起始点纬度|
|end_lon|varchar(20)||终止点经度|
|end_lat|varchar(20)||终止点纬度|

# 开采日志表
表名：mine_log
|属性名称|属性类型|约束|备注|
|-|-|-|-|
|id|varchar(50)|主键||
|user_id|varchar(50)|外键(mine_user.user_id)|开采用户id|
|mine_lon|varchar(20)||开采经度|
|mine_lat|varchar(20)||开采纬度|
|mine_timestamp|datetime||开采日期|
|mine_type|varchar(50)|外键(mineral.id)|开采矿石种类|
|mine_quatity|varchar(50)||开采矿石数量|

# 林区位置边界表
表名：forest_zone_border
|属性名称|属性类型|约束|备注|
|-|-|-|-|
|id|varchar(50)|主键||
|start_lon|varchar(20)||起始点经度|
|start_lat|varchar(20)||起始点纬度|
|end_lon|varchar(20)||终止点经度|
|end_lat|varchar(20)||终止点纬度|

# 车辆数据表
表名：vehicle
|属性名称|属性类型|约束|备注|
|-|-|-|-|
|id|varchar(50)|主键||
|vehicle_type|varchar(50)||车辆类型|
|vehicle_max_load|varchar(50)||车辆满载重量|
|vehicle_last_maintained|varchar(50)||车辆距离上次维修保养的时间|
|vehicle_deprecated_date|datetime||车辆报废年|

# 矿物类型表
表名：mineral
|属性名称|属性类型|约束|备注|
|-|-|-|-|
|id|varchar(50)|主键||
|mineral_name|varchar(50)||矿物名称|

# 车辆类型和矿物类型关系表
表名：vehicle_mineral_map
|属性名称|属性类型|约束|备注|
|-|-|-|-|
|vehicle_id|varchar(50)|外键(vehicle.id)|车辆id|
|mineral_type|varchar(50)|外键(mineral.id)|矿物id|

# 车辆运载日志表
表名：transportation_log
|属性名称|属性类型|约束|备注|
|-|-|-|-|
|id|varchar(50)|主键||
|user_id|varchar(50)|外键(mine_user.user_id)|司机用户id|
|transport_start_time|datetime||运输开始时间|
|transport_end_time|datetime||运输结束时间|
|transport_start_lat|varchar(20)||运输起始点纬度|
|transport_start_lon|varchar(20)||运输起始点经度|
|transport_end_lat|varchar(20)||运输终止点纬度|
|transport_end_lon|varchar(20)||运输终止点经度|
|mine_log_id|varchar(50)|外键(mine_log.id)|对应某次开采活动的运输|
|mineral_type|varchar(50)|外键(mineral.id)|开采矿石种类|
|mineral_quatity|varchar(50)||开采矿石数量|
|have_cover|boolean||是否遮盖防尘布|

# 扬尘指数监测日志
表名：dust_log
|属性名称|属性类型|约束|备注|
|-|-|-|-|
|id|varchar(50)|主键||
|dust_data|varchar(50)||扬尘指标|

# 噪声指数监测日志
表名：noise_log
|属性名称|属性类型|约束|备注|
|-|-|-|-|
|id|varchar(50)|主键||
|noise_data|varchar(50)||噪声指标|

# 土壤污染监测日志
表名：soil_log
|属性名称|属性类型|约束|备注|
|-|-|-|-|
|id|varchar(50)|主键||
|soil_data|varchar(50)||土壤污染指标|