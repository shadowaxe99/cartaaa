<%text>
# Alembic migration script template
# Each new migration will use this template when created.
# This script is executed in an Alembic environment that provides
# the variables `config` and `context`.
</%text>
<%!
    from alembic import context
    from logging.config import fileConfig
    from sqlalchemy import engine_from_config, pool
    from sqlalchemy import MetaData

    # Import the shared dependencies for table definitions
    from backend.models import Base
    config = context.config

    # Interpret the config file for Python logging.
    # This line sets up loggers basically.
    fileConfig(config.config_file_name)

    # Add your model's MetaData object here for 'autogenerate' support
    # from myapp import mymodel
    # target_metadata = mymodel.Base.metadata
    target_metadata = Base.metadata
%>
<%block name="imports">
    from sqlalchemy import engine_from_config, pool
    from alembic import context
</%block>

<%block name="pre_imports">
</%block>

<%block name="post_imports">
</%block>

<%block name="run_migrations_offline">
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True
    )

    with context.begin_transaction():
        context.run_migrations()
</%block>

<%block name="run_migrations_online">
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix='sqlalchemy.',
        poolclass=pool.NullPool)

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()
</%block>

<%block name="after_run_migrations_online">
</%block>

<%block name="after_run_migrations_offline">
</%block>