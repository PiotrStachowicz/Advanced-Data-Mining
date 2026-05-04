from recbole.quick_start import run_recbole

run_recbole(
    model='Pop',
    dataset='beauty',
    config_dict={
        'data_path': './dataset',
        'epochs': 10,
        'train_batch_size': 2048,
        'eval_step': 1,
        'wandb': True,
        'wandb_project': 'ADM',
        'wandb_run_name': 'baseline_popular'
    }
)