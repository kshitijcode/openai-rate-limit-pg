from dataclasses import (
    dataclass,
    field)



@dataclass
class StatusTracker:
    """Stores metadata about the script's progress. Only one instance is created."""

    num_tasks_started: int = 0
    num_tasks_in_progress: int = 0  # script ends when this reaches 0
    num_tasks_succeeded: int = 0
    num_tasks_failed: int = 0
    num_rate_limit_errors: int = 0
    num_api_errors: int = 0  # excluding rate limit errors, counted above
    num_other_errors: int = 0
    time_of_last_rate_limit_error: int = 0  # used to cool off after hitting rate limits
    average_prompt_tokens: int = 0
    average_completion_tokens: int = 0 

    total_prompt_tokens: int = 0
    total_completion_tokens: int = 0 

    peak_prompt_tokens: int = 0
    peak_completion_tokens: int = 0 
    peak_total_tokens: int= 0
    model_name: str = ""
    max_tokens: int = 0

    def update_token_metrics(self, prompt_tokens: int, completion_tokens: int):
        # Update totals
        self.total_prompt_tokens += prompt_tokens
        self.total_completion_tokens += completion_tokens

        # Update averages
        self.average_prompt_tokens = self.total_prompt_tokens / self.num_tasks_succeeded
        self.average_completion_tokens = self.total_completion_tokens / self.num_tasks_succeeded

        # Update peaks
        self.peak_prompt_tokens = max(self.peak_prompt_tokens, prompt_tokens)
        self.peak_completion_tokens = max(self.peak_completion_tokens, completion_tokens)
        total_tokens = prompt_tokens + completion_tokens
        self.peak_total_tokens = max(self.peak_total_tokens, total_tokens)

