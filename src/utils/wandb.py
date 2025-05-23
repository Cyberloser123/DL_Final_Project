import wandb

class WandbLogger:
    def __init__(self, args, wandb_run=None):
        self.args = args
        self.use_wandb = True
        self.use_print = True
        self.wandb_project = "vjepa-reg" #args.wandb_project
        if self.use_wandb:
            self.wandb_run = wandb_run
            if self.wandb_run is None:
                self.wandb_run = wandb.init(project=self.wandb_project, config=args, save_code=True)
    
    def log(self, dict_msg):
        if self.use_wandb:
            self.wandb_run.log(dict_msg)
        elif self.use_print:
            print(dict_msg)

    def histogram_log(self, dict_msg, histogram_dist_msg):
        if self.use_wandb:
            upload_dict = {}
            for key, value in dict_msg.items():
                upload_dict[f"{key}"] = value
            for key, value in histogram_dist_msg.items():
                upload_dict[f"{key}"] = wandb.Histogram(value)
            self.wandb_run.log(upload_dict)
        elif self.use_print:
            print(dict_msg)
            print(histogram_dist_msg)