---
symbol: "INTS7"
type: "gene"
col: 6755
ensembl_id: "ENSG00000143493"
name: "integrator complex subunit 7"
location: "1q32.3"
module: 4
arm: "+"
pooled_cpm: 56.05
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 7
n_dd_up_clean: 3
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# INTS7

*integrator complex subunit 7* — 1q32.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.68× (z +7.4, q 1e-10, up in 39 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 1.48× (z +5.4, q 1e-05, up in 33 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.449× (z -16.0, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IPO9]] (+0.76, fdr 7e-06), [[SARS2]] (+0.63, fdr 8e-06), [[NUP155]] (+0.62, fdr 7e-06); moves opposite to [[KDM5B]] (-0.65, fdr 7e-06), [[STX5-DT]] (-0.64, fdr 1e-05), [[IFT20]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6755.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.68×** | +7.4 | 1e-10 | 39/48 (MIA PaCa-2, PANC-1, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.54×** | +6.1 | 4e-07 | 36/48 (MIA PaCa-2, SNU-423, …) | two highest doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.48×** | +5.4 | 1e-05 | 33/48 (NCI-H1573, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +4.0 | 0.007 | 24/48 (SHP-77, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +4.0 | 0.007 | 22/48 (C-33 A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **1.31×** | +3.8 | 0.014 | 27/48 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~98% of this change | **1.30×** | +3.7 | 0.018 | 21/48 (SW 900, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.27×** | +3.4 | 0.046 | 24/48 (LoVo, COLO 205, …) | rises with dose |  |
| [[TAK-733 (drug)]] 5 µM |  | 1.52× | +3.1 | 0.13 | 18/48 (AsPC-1, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6755.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.449×** | -16.0 | 0e+00 | 45/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.530×** | -8.7 | 1e-15 | 40/47 (SW48, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.598×** | -7.0 | 5e-10 | 35/49 (LS 180, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.731×** | -4.5 | 0.001 | 28/48 (CHP-212, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.738×** | -4.3 | 0.002 | 25/48 (HEC-1-A, NCI-H23, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.819×** | -4.0 | 0.006 | 22/49 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.784×** | -3.4 | 0.046 | 23/48 (CFPAC-1, A-172, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | 0.801× | -3.2 | 0.11 | 22/46 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.44 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6755. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 94.5 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.374× (z -14.9) |
| [[LS 180 (line)]] | wt | 78.3 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -16.5) |
| [[NCI-H460 (line)]] | wt | 96.7 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -18.5) |
| [[SW480 (line)]] | alt | 92.2 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.355× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.517× (z -11.4) |
| [[COLO 205 (line)]] | alt | 83.1 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.110× (z -18.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.260× (z -16.2) |
| [[LoVo (line)]] | wt | 48.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -13.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.468× (z -10.8) |
| [[MIA PaCa-2 (line)]] | alt | 47.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.424× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 48.5 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.170× (z -14.0) |
| [[Panc 03.27 (line)]] | alt | 34.6 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -10.0) |
| [[SNU-1 (line)]] | wt | 60.8 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.194× (z -11.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -9.7) |
| [[SW 1271 (line)]] | alt | 52.1 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.108× (z -11.5) |
| [[A498 (line)]] | wt | 53.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -15.3) |
| [[A549 (line)]] | wt | 44.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -9.2) |
| [[AsPC-1 (line)]] | alt | 29.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -10.1) |
| [[C-33 A (line)]] | alt | 75.5 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.266× (z -10.9) |
| [[CFPAC-1 (line)]] | alt | 36.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -9.9) |
| [[H4 (line)]] | wt | 58.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 51.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -14.0) |
| [[HS-578T (line)]] | alt | 29.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -8.5) |
| [[HT-29 (line)]] | alt | 46.4 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -8.7) |
| [[J82 (line)]] | alt | 55.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.439× (z -9.9) |
| [[KATO III (line)]] | alt | 70.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 52.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -14.4) |
| [[NCI-H2030 (line)]] | alt | 56.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.332× (z -14.4) |
| [[NCI-H2347 (line)]] | alt | 25.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[PANC-1 (line)]] | alt | 97.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -17.0) |
| [[RKO (line)]] | wt | 61.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -14.6) |
| [[RPMI-7951 (line)]] | alt | 44.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -10.3) |
| [[SHP-77 (line)]] | alt | 81.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.285× (z -16.7) |
| [[SW1417 (line)]] | alt | 46.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -10.9) |
| [[SW48 (line)]] | wt | 45.2 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0524× (z -16.8) |
| [[A-172 (line)]] | wt | 42.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 44.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 40.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 96.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 32.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 42.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 53.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 56.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6755), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO9]] | +0.76 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[SARS2]] | +0.63 | +0.58 / +0.63 | both halves | 8e-06 |  |
| [[NUP155]] | +0.62 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[TUBGCP3]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[EXOG]] | +0.61 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[COA1]] | +0.61 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[MCM3]] | +0.61 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[TAF1B]] | +0.60 | +0.45 / +0.65 | both halves | 3e-05 |  |
| [[EXOSC2]] | +0.59 | +0.53 / +0.63 | both halves | 1e-05 |  |
| [[AGPS]] | +0.59 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[MTHFD1]] | +0.59 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[RAD51D]] | +0.59 | +0.40 / +0.67 | both halves | 4e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM5B]] | -0.65 | -0.66 / -0.60 | both halves | 7e-06 |  |
| [[STX5-DT]] | -0.64 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[IFT20]] | -0.63 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[OSER1-DT]] | -0.61 | -0.42 / -0.64 | both halves | 4e-05 |  |
| [[WBP1]] | -0.60 | -0.46 / -0.62 | both halves | 3e-05 |  |
| [[C14orf28]] | -0.59 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[CDK7]] | -0.58 | -0.59 / -0.53 | both halves | 1e-05 | pathway: RNA polymerase II transcribes snRNA genes |
| [[JMY]] | -0.58 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[UBXN7]] | -0.57 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[RSRP1]] | -0.56 | -0.52 / -0.57 | both halves | 1e-05 |  |
| [[RAB11FIP5]] | -0.56 | -0.51 / -0.57 | both halves | 1e-05 |  |
| [[EOGT-DT]] | -0.56 | -0.48 / -0.57 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises INTS7's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 1.7% of all compounds | 0.036 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.636). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-2.2, -36.9); signed map (-11.0, -47.5). **Vector** length 127, 36.8% of its response variance represented; |z| ≥ 3 in 923 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.2 | +7.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +7.0 | +6.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.9 | +3.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.7 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.6 | +2.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.9 | +3.0 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.9 | +2.5 |
|  | [[EX229 (drug)]] 5 µM |  | +3.7 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +2.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -13.0 | -16.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -8.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -7.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -4.1 | -4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.7 | -4.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.8 | -3.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.6 | -1.8 |
|  | [[Temsirolimus (drug)]] 0.5 µM |  | -2.6 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | integrator complex subunit 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.3 — chr1:211,940,399-212,035,557 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434B168, INT7; previously C1orf73 |
| Gene groups (HGNC) | Integrator complex; Armadillo like helical domain containing |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NVH2](https://www.uniprot.org/uniprotkb/Q9NVH2) (Integrator complex subunit 7):

> Component of the integrator complex, a multiprotein complex that terminates RNA polymerase II (Pol II) transcription in the promoter-proximal region of genes. The integrator complex provides a quality checkpoint during transcription elongation by driving premature transcription termination of transcripts that are unfavorably configured for transcriptional elongation: the complex terminates transcription by (1) catalyzing dephosphorylation of the C-terminal domain (CTD) of Pol II subunit …

**Summary**, from NCBI Gene [25896](https://www.ncbi.nlm.nih.gov/gene/25896):

> This gene encodes a subunit of the integrator complex. The integrator complex associates with the C-terminal domain of RNA polymerase II and mediates 3'-end processing of the small nuclear RNAs U1 and U2. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:24484](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24484) · Entrez [25896](https://www.ncbi.nlm.nih.gov/gene/25896) · UniProt [Q9NVH2](https://www.uniprot.org/uniprotkb/Q9NVH2) · Ensembl [ENSG00000143493](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143493)

## Data

Gene col 6755: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6755); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6755, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6755]; `tensor/DDL_lfc|DDL_z.npy` [6755]; `embed/gene_vectors.npy` [6755]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6755 or target_col == 6755). Every well: [[INTS7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/INTS7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
