delimiter $$

CREATE TABLE `weather_data` (
  `DATUM` datetime DEFAULT NULL,
  `STN` int(11) DEFAULT NULL,
  `DVEC` int(11) DEFAULT NULL,
  `FHVEC` int(11) DEFAULT NULL,
  `FG` int(11) DEFAULT NULL,
  `FHX` int(11) DEFAULT NULL,
  `FHXH` int(11) DEFAULT NULL,
  `FXX` int(11) DEFAULT NULL,
  `FXXH` int(11) DEFAULT NULL,
  `TG` int(11) DEFAULT NULL,
  `TN` int(11) DEFAULT NULL,
  `TNH` int(11) DEFAULT NULL,
  `TX` int(11) DEFAULT NULL,
  `TXH` int(11) DEFAULT NULL,
  `T10N` int(11) DEFAULT NULL,
  `T10NH` int(11) DEFAULT NULL,
  `SQ` int(11) DEFAULT NULL,
  `SP` int(11) DEFAULT NULL,
  `Q` int(11) DEFAULT NULL,
  `DR` int(11) DEFAULT NULL,
  `RH` int(11) DEFAULT NULL,
  `RHX` int(11) DEFAULT NULL,
  `RHXH` int(11) DEFAULT NULL,
  `PG` int(11) DEFAULT NULL,
  `PX` int(11) DEFAULT NULL,
  `PXH` int(11) DEFAULT NULL,
  `PN` int(11) DEFAULT NULL,
  `PNH` int(11) DEFAULT NULL,
  `VVN` int(11) DEFAULT NULL,
  `VVNH` int(11) DEFAULT NULL,
  `VVX` int(11) DEFAULT NULL,
  `VVXH` int(11) DEFAULT NULL,
  `NG` int(11) DEFAULT NULL,
  `UG` int(11) DEFAULT NULL,
  `UX` int(11) DEFAULT NULL,
  `UXH` int(11) DEFAULT NULL,
  `UN` int(11) DEFAULT NULL,
  `UNH` int(11) DEFAULT NULL,
  `EV24` int(11) DEFAULT NULL,
  `INSERTED` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY `DATUM_UNIQUE` (`DATUM`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1$$
