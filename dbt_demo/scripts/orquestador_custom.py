def main():

    delta_days = 1
    delta_days = 280    # debug

    dbt_configs = [

        # ["Raw models with no daily loop",
        #  "path:models/raw",
        #  "tag:ignore tag:daily-loop",
        #  False],

        # ["Raw models with daily loop",
        #  "tag:daily-loop",
        #  "tag:ignore",
        #  True],

        ["Raw models with daily loop",
         "tag:venta-hora",
         "tag:ignore",
         True],
    ]

    # Itera por cada configuración de modelos indicada en el array dbt_config

    for config in dbt_configs:

        print('-' * 80)
        print(f'Running : {config[0]}')
        print('-' * 80)

        # Si el 4o valor del array es true, ejecuta el loop diario en base a delta_days

        if config[3] == True:
            run_raw_daily_models(
                config[1],
                config[2],
                delta_days
            )

            # run_raw_daily_models_from_list(
            #     config[1],
            #     config[2],
            #     delta_days
            # )

        # caso contrario, ejecuta el pool de modelos indicado

        else:
            run_raw_models(
                config[1],
                config[2],
                f'{0}'
            )

    print(f"\n{'='*60}")
    print(f"{datetime.now()} > Proceso completado exitosamente.")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()