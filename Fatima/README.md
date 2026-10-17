# Blind Spots of Frontier Models: Does Verbal Confidence Track Mathematical Correctness?

**Project:** Fatima Institute Technical Challenge --- *Blind Spots of
Frontier Models*\
**Model:** `Qwen/Qwen3-1.7B`\
**Task domain:** Mathematical claims and proof-related questions about
uniform convergence\
**Evaluation size:** 25 cases\
**Status:** Exploratory evaluation

## 1. Overview

This project investigates a specific reliability question: **does a
language model's verbal confidence meaningfully reflect whether its
mathematical verdict is correct?**

The model was asked to judge mathematical claims or proof-related cases
involving uniform convergence, provide a short explanation, and report a
verbal confidence label (`LOW`, `MEDIUM`, or `HIGH`). Its verdicts were
compared with reference verdicts. The mathematical explanations were
also reviewed separately.

The central motivation is that a final answer can look decisive without
being mathematically reliable. In analysis, small mistakes involving
quantifiers, suprema, bounds, or the difference between pointwise and
uniform convergence can change whether an argument is valid. This makes
uniform convergence a useful focused domain for exploring the gap
between a model's stated confidence and its actual performance.

> **Scope note:** This is a small exploratory study of one model and 25
> selected cases. It does not establish that the same behavior occurs
> across all models or mathematical tasks.

## 2. Research Questions

1.  How accurately does `Qwen/Qwen3-1.7B` classify the selected
    uniform-convergence cases?
2.  Is higher verbal confidence associated with a greater likelihood of
    a correct verdict?
3.  Does the quality of the model's mathematical explanation agree with
    the correctness of its final verdict?
4.  What evaluation or training strategy could help make confidence more
    informative?

## 3. Research Motivation

My motivation comes from studying mathematics alongside computer science
and exploring how AI systems handle mathematical reasoning. Uniform
convergence is a useful test case because it requires careful attention
to quantifiers and bounds, not just recognition of familiar mathematical
patterns.

I wanted to examine a behavior that a simple accuracy score might miss:
even when a model gives a verdict and expresses confidence, the
confidence label may not help a reader judge whether the verdict is
correct. I therefore measured verdict correctness and verbal confidence
separately, and treated explanation quality as a third, distinct
dimension.

*Please personalize this section before submission so that it accurately
reflects your own experience and motivation.*

## 4. Model and Environment

-   **Model identifier:** `Qwen/Qwen3-1.7B`
-   **Model family:** Qwen3
-   **Environment:** Google Colab
-   **GPU used:** NVIDIA Tesla T4
-   **PyTorch:** `2.11.0+cu130`
-   **Transformers:** `5.20.1`
-   **Thinking mode:** Disabled
-   **Decoding:** `do_sample=False`
-   **Maximum generated tokens:** `300`

The model was loaded and run in the notebook. These settings describe
this run and are not a claim that the experiment will reproduce
identically across all software versions or environments.

## 5. Evaluation Method

### Dataset

The evaluation used 25 selected mathematical cases concerning uniform
convergence. The cases cover topics such as:

-   Pointwise versus uniform convergence.
-   Convergence on bounded and unbounded domains.
-   Using inequalities to establish uniform convergence.
-   Correct interpretation of maxima and suprema.
-   Whether the convergence index `N` may depend on `x`.
-   Mathematical validity of proof explanations.

The dataset is small and selected rather than randomly sampled from a
defined population of mathematical questions.

### Prompt procedure

The original prompts were retained, and a standardized follow-up
instruction was appended. The requested response format included:

1.  `Verdict: CORRECT or INCORRECT`
2.  `Reason: ...` (at most three sentences)
3.  `Confidence: HIGH, MEDIUM, or LOW`
4.  `Why this confidence: ...`

The standardized follow-up made the expected output fields more
consistent. However, the original prompts were not fully rewritten into
identical prompts, so differences in the original wording or embedded
instructions may have affected outputs.

### Metrics

**Verdict accuracy** was calculated as:

`Correct verdicts / Total cases × 100`

For the confidence association, labels were encoded ordinally as
`LOW = 1`, `MEDIUM = 2`, and `HIGH = 3`. Verdict correctness was encoded
as `1` for correct and `0` for incorrect. Spearman's rank correlation
was then calculated between these variables.

This analysis treats confidence as an ordinal label, **not** as a
calibrated probability. The analysis does not establish that `HIGH`
corresponds to any specific probability of correctness.

### Reasoning review

Explanations were separately assigned one of three preliminary labels:

-   `CORRECT`: the core mathematical explanation was considered sound.
-   `PARTIALLY_INCORRECT`: the explanation included a relevant idea or
    conclusion but also a material mathematical error or misleading
    detail.
-   `INCORRECT`: the core explanation was materially wrong,
    contradictory, or failed to support its conclusion.

These labels came from a preliminary review and were not independently
validated by multiple reviewers. They should be interpreted cautiously.

## 6. Results

### Overall verdict performance

  Metric                 Result
  -------------------- --------
  Total cases                25
  Correct verdicts           16
  Incorrect verdicts          9
  Verdict accuracy        64.0%

### Accuracy by verbal confidence

  ------------------------------------------------------------------------
  Confidence            Cases        Correct      Incorrect       Accuracy
  label                             verdicts       verdicts 
  ------------ -------------- -------------- -------------- --------------
  HIGH                      5              4              1          80.0%

  MEDIUM                    3              1              2          33.3%

  LOW                      17             11              6          64.7%

  **Total**            **25**         **16**          **9**      **64.0%**
  ------------------------------------------------------------------------

The observed subgroup accuracies do not increase consistently across the
ordered confidence labels. The HIGH and MEDIUM groups are particularly
small, so their percentages are descriptive and unstable.

### Confidence--correctness association

  Statistic          Result
  ---------------- --------
  Spearman's rho     0.0281
  p-value            0.8940
  Sample size            25

The observed correlation is very close to zero, and the p-value is above
the conventional 0.05 threshold. Thus, this experiment did not find
statistically significant evidence of a monotonic association between
verbal confidence and verdict correctness in these 25 cases.

This does **not** prove that confidence and correctness are unrelated in
general. The small sample may be insufficient to detect a relationship,
and the result may differ with another dataset, prompt, or model.

### Preliminary explanation review

  Reasoning label          Cases   Percentage
  --------------------- -------- ------------
  CORRECT                      8          32%
  PARTIALLY_INCORRECT          8          32%
  INCORRECT                    9          36%
  **Total**               **25**     **100%**

This review suggests that verdict correctness alone does not capture all
aspects of mathematical response quality. However, the reasoning labels
are preliminary and involve reviewer judgment.

## 7. Interpretation

In this evaluation, verbal confidence did not meaningfully track verdict
correctness: Spearman's rho was `0.0281` with `p = 0.8940`. The
confidence labels therefore provided little evidence of a monotonic
ordering of correctness in this sample.

A model can also reach a correct verdict while giving a flawed
explanation, or produce an incorrect verdict while mentioning a relevant
mathematical idea. For that reason, this project distinguishes three
questions:

1.  Was the final verdict correct?
2.  Was the explanation mathematically sound?
3.  Did the stated confidence correspond to observed correctness?

These are related but different evaluation targets.

## 8. Proposed Path Forward

A possible way to address this gap is to create a **mathematical
confidence-evaluation dataset** designed specifically to distinguish
correctness, reasoning validity, and confidence.

### Data curation strategy

1.  **Build paired examples.** Include closely related cases where a
    proof is valid in one version and invalid in another, with the
    precise mathematical difference annotated.
2.  **Annotate more than the final answer.** Record the reference
    verdict, the key mathematical justification, common failure modes
    (such as quantifier errors or incorrect suprema), and whether the
    explanation actually supports the verdict.
3.  **Use independent review.** Have at least two mathematically
    qualified reviewers label each case, resolve disagreements, and
    report agreement.
4.  **Balance difficulty and outcomes.** Include correct and incorrect
    claims across multiple topics and difficulty levels, avoiding a
    dataset where one answer label dominates.
5.  **Separate development and test sets.** Keep held-out cases to
    reduce the risk that prompt tuning or fine-tuning merely memorizes
    the evaluation examples.

### Fine-tuning and evaluation idea

A possible fine-tuning approach is to train the model to produce a
verdict, a checkable justification, and a confidence estimate as
separate outputs. The training data should include examples where the
model is correct but overconfident, incorrect but overconfident, correct
but uncertain, and appropriately uncertain.

The model could also be encouraged to identify the specific step it
cannot justify and express uncertainty when its reasoning does not
establish the verdict. Evaluation should measure verdict accuracy,
explanation validity, confidence--correctness association, and
probability calibration separately. If numerical probabilities are used,
calibration metrics such as the Brier score could supplement rank
correlation.

A stronger future experiment would compare the original model with the
fine-tuned model on a held-out dataset and test whether confidence
becomes more informative without reducing mathematical accuracy.

This is a proposed direction, not a method that has already been
implemented or validated in this project.

## 9. Limitations

-   **Small sample:** only 25 cases were evaluated.
-   **Selected cases:** the dataset is not a random, representative
    sample of mathematical reasoning tasks.
-   **Single model:** only `Qwen/Qwen3-1.7B` was tested.
-   **Prompt variation:** a standardized follow-up was appended to
    original prompts, but original wording was not fully normalized.
-   **Ordinal confidence:** `LOW`, `MEDIUM`, and `HIGH` are not
    calibrated probabilities.
-   **Preliminary reasoning labels:** explanations were not
    independently annotated by multiple reviewers.
-   **Reference labels:** the accuracy result depends on the correctness
    of the reference verdicts.
-   **Statistical uncertainty:** a non-significant result does not
    establish that the true association is zero.

## 10. Conclusion

This project evaluated whether verbal confidence tracks mathematical
verdict correctness in `Qwen/Qwen3-1.7B` on 25 selected
uniform-convergence cases. The model achieved 64.0% verdict accuracy.
The Spearman correlation between ordinal confidence and verdict
correctness was `0.0281` (`p = 0.8940`), showing no statistically
significant monotonic association in this sample.

The preliminary reasoning review also illustrates why final-answer
accuracy and explanation validity should be assessed separately. The
findings are exploratory and limited to this model, prompt procedure,
and selected dataset.

The next step is to evaluate the proposed approach on a larger,
independently reviewed dataset and test whether targeted training can
make confidence more informative about mathematical correctness.

## 11. Reproducibility and Artifacts

This project should be accompanied by the actual artifacts used in the
evaluation, where available:

-   The Google Colab notebook or exported `.ipynb` file.
-   The 25-case evaluation dataset and reference labels.
-   The raw model outputs.
-   The reviewed results CSV.
-   The summary metrics CSV.
-   This README.

Suggested filenames, if they match the files actually uploaded:

-   `fatima_fellowship_uniform_rerun_v2.json`
-   `fatima_fellowship_uniform_reviewed_v5.csv`
-   `fatima_fellowship_final_summary.csv`

Only include files that are actually present in the public repository.
Do not upload model weights unless redistribution is permitted and the
weights are genuinely part of your project; the model can instead be
referenced by its Hugging Face model identifier.

## References

-   Qwen Team. (2025). *Qwen3 Technical Report*. arXiv:2505.09388.
    https://arxiv.org/abs/2505.09388
-   Rudin, W. (1976). *Principles of Mathematical Analysis* (3rd ed.).
    McGraw-Hill.
-   Spearman, C. (1904). The proof and measurement of association
    between two things. *The American Journal of Psychology, 15*(1),
    72--101. https://doi.org/10.2307/1412159
