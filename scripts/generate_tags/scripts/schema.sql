-- key는 복합키: category, title_path, updated_at
create table updated_tags
(
    category   varchar(191) not null,
    title_path varchar(191) not null,
    updated_at timestamp    not null,
    primary key (category, title_path)
) comment '최근 업데이트된 태그 목록' charset = utf8mb4
    row_format = DYNAMIC;