-- key는 복합키: category, title_path, updated_at
create table updated_tags
(
    category   varchar(191) not null comment '카테고리(ex. cloud, devops)',
    title      varchar(191) not null comment '제목 경로',
    updated_at timestamp    not null comment '업데이트 시간',
    primary key (category, title)
) comment '최근 업데이트된 태그 목록' charset = utf8mb4
                           row_format = DYNAMIC;