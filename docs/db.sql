CREATE DATABASE IF NOT EXISTS `wolf_spider` DEFAULT CHARACTER SET utf8mb4;
USE `wolf_spider`;

DROP TABLE IF EXISTS `webpage`;
CREATE TABLE IF NOT EXISTS `webpage`
(
    `id`                BIGINT(20) UNSIGNED     NOT NULL AUTO_INCREMENT,

    `url`               VARCHAR(500)            NOT NULL DEFAULT '' COMMENT '',
    `type`              TINYINT(4) UNSIGNED     NOT NULL DEFAULT 0,
    `request_status`    TINYINT(4) UNSIGNED     NOT NULL DEFAULT 0,
    `parse_status`      TINYINT(4) UNSIGNED     NOT NULL DEFAULT 0,

    `request`           text,
    `header`            text,
    `content`           text,
    
    `version`           INT(11) UNSIGNED        NOT NULL DEFAULT 0 COMMENT '版本号',
    `delete_flag`       TINYINT(3) UNSIGNED     NOT NULL DEFAULT 0 COMMENT '是否删除 0未删除，1已删除',
    `last_editor`       BIGINT(20) UNSIGNED     NOT NULL DEFAULT 0 COMMENT '最后编辑者',
    `created_at`        DATETIME                NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `updated_at`        DATETIME ON UPDATE CURRENT_TIMESTAMP COMMENT '编辑时间',
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4 COMMENT = 'webpage'; 

DROP TABLE IF EXISTS `webinfo`;
CREATE TABLE IF NOT EXISTS `webinfo`
(
    `id`                BIGINT(20) UNSIGNED     NOT NULL AUTO_INCREMENT,
    `page_id`           BIGINT(20) UNSIGNED     NOT NULL DEFAULT 0,
    `type`              TINYINT(4) UNSIGNED     NOT NULL DEFAULT 0,

    `name`              VARCHAR(500)            NOT NULL DEFAULT '' COMMENT '',
    `tag`               JSON,
    `data`              JSON,

    `version`           INT(11) UNSIGNED        NOT NULL DEFAULT 0 COMMENT '版本号',
    `delete_flag`       TINYINT(3) UNSIGNED     NOT NULL DEFAULT 0 COMMENT '是否删除 0未删除，1已删除',
    `last_editor`       BIGINT(20) UNSIGNED     NOT NULL DEFAULT 0 COMMENT '最后编辑者',
    `created_at`        DATETIME                NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    `updated_at`        DATETIME ON UPDATE CURRENT_TIMESTAMP COMMENT '编辑时间',
    PRIMARY KEY (`id`)
) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4 COMMENT = 'webinfo';  