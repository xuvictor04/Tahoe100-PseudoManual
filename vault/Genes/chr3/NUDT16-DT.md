---
symbol: "NUDT16-DT"
type: "gene"
col: 14706
ensembl_id: "ENSG00000250608"
name: "NUDT16 divergent transcript"
location: "3q21.3"
module: 15
arm: "+"
pooled_cpm: 16.36
n_lines_expressing: 48
n_dd_up: 11
n_dd_down: 15
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# NUDT16-DT

*NUDT16 divergent transcript* — 3q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.15× (z +11.6, q 3e-28, up in 29 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (12 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 0.379× (z -10.0, q 9e-21, down in 35 of 43 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.416× (z -4.9, q 5e-05, down in 24 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CCNY-AS1]] (+0.70, fdr 1e-05), [[ZNF529-AS1]] (+0.67, fdr 1e-05), [[VPS13B-DT]] (+0.65, fdr 1e-05); moves opposite to [[THEM6]] (-0.59, fdr 2e-05), [[NFE2L3]] (-0.51, fdr 3e-05), [[MAP3K4]] (-0.51, fdr 7e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14706.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.15×** | +11.6 | 3e-28 | 29/42 (HEC-1-A, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.16×** | +8.2 | 6e-14 | 30/44 (SW480, LoVo, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.39×** | +5.0 | 1e-04 | 23/45 (SW1417, LS 180, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.6 | 6e-04 | 20/40 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.54×** | +4.2 | 0.002 | 15/43 (H4, NCI-H1792, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +4.1 | 0.005 | 19/44 (NCI-H23, KATO III, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.41×** | +3.5 | 0.032 | 16/42 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.032 | 13/45 (RKO, HOP62, …) | rises with dose | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.27×** | +3.5 | 0.034 | 12/46 (SW480, A-427, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.3 | 0.055 | 12/42 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.35×** | +3.2 | 0.071 | 14/43 (LoVo, KATO III, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 12 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14706.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.379×** | -10.0 | 9e-21 | 35/43 (A498, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.453×** | -8.5 | 7e-15 | 35/42 (PANC-1, AsPC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.458×** | -8.4 | 1e-14 | 32/45 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.446×** | -8.3 | 1e-14 | 29/39 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.514×** | -6.6 | 6e-09 | 24/45 (NCI-H460, COLO 205, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.361×** | -5.7 | 1e-06 | 29/43 (AsPC-1, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.567×** | -5.6 | 2e-06 | 27/45 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.594×** | -5.6 | 2e-06 | 26/44 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.701×** | -5.4 | 4e-06 | 25/44 (A498, NCI-H460, …) | rises with dose | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.605×** | -5.4 | 4e-06 | 21/45 (Panc 03.27, NCI-H460, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.416×** | -4.9 | 5e-05 | 24/41 (COLO 205, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.554×** | -3.3 | 0.045 | 13/40 (AsPC-1, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.741×** | -3.2 | 0.057 | 19/40 (A498, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~78% of this change | **0.744×** | -3.2 | 0.062 | 13/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.575×** | -3.1 | 0.074 | 11/42 (A498, NCI-H460, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14706. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 36.7 | 0 | 9 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -19.5) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 14.3 | 0 | 8 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.119× (z -14.2) ⚠ cell-cycle shift, explains ~51% of this change |
| [[A498 (line)]] | wt | 23.2 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0943× (z -24.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 24.1 | 0 | 4 (3 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 37.7 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -13.9) ⚠ cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 21.9 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Rosiglitazone (drug)]] 5 µM 0.223× (z -9.0) |
| [[HOP62 (line)]] | alt | 45.1 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[LoVo (line)]] | wt | 8.58 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.96× (z +11.5) ⚠ cell-cycle shift, would explain all of this change | [[Digitoxin (drug)]] 5 µM 0.184× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[Panc 03.27 (line)]] | alt | 60.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -10.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 24.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.211× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 20.1 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0627× (z -12.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HCT15 (line)]] | alt | 11.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.87× (z +10.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[HEC-1-A (line)]] | alt | 10.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +11.1) | — |
| [[KATO III (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.155× (z -10.6) ⚠ cell-cycle shift, explains ~51% of this change |
| [[MIA PaCa-2 (line)]] | alt | 8.32 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0766× (z -10.3) ⚠ cell-cycle shift, explains ~31% of this change |
| [[NCI-H1573 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.114× (z -10.5) ⚠ toxic; cell-cycle shift, explains ~32% of this change |
| [[SNU-1 (line)]] | wt | 21.3 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.0946× (z -9.3) |
| [[SNU-423 (line)]] | alt | 8.72 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 9.80 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.186× (z -10.2) ⚠ cell-cycle shift, explains ~51% of this change |
| [[A-172 (line)]] | wt | 9.94 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.14 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.02 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.01 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.06 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.04 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14706), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCNY-AS1]] | +0.70 | +0.57 / +0.72 | both halves | 1e-05 |  |
| [[ZNF529-AS1]] | +0.67 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[VPS13B-DT]] | +0.65 | +0.54 / +0.64 | both halves | 1e-05 | same gene group |
| [[LINC01772]] | +0.64 | +0.51 / +0.70 | both halves | 1e-05 |  |
| [[GLUD1P3]] | +0.64 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[CAPN10-DT]] | +0.64 | +0.45 / +0.66 | both halves | 3e-05 | same gene group |
| [[PPP1R26-AS1]] | +0.63 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[FRG1HP]] | +0.63 | +0.57 / +0.63 | both halves | 1e-05 |  |
| [[ZNF596]] | +0.62 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[C8orf44-SGK3]] | +0.61 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[ZNF778]] | +0.60 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[ZNF213-AS1]] | +0.59 | +0.51 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THEM6]] | -0.59 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[NFE2L3]] | -0.51 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[MAP3K4]] | -0.51 | -0.38 / -0.57 | both halves | 7e-05 |  |
| [[CEP83]] | -0.50 | -0.33 / -0.48 | both halves | 1e-04 |  |
| [[SERBP1]] | -0.49 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[LMCD1]] | -0.49 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[STIM2]] | -0.49 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[HES1]] | -0.48 | -0.41 / -0.48 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NUDT16-DT's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.661). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-8.3, 24.2); signed map (2.2, -1.8). **Vector** length 87.5, 19.6% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.6 | +8.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.4 | +11.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +3.5 | +5.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +0.8 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | +2.6 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.3 | -0.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.2 | +2.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.1 | +4.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -4.3 | -2.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -4.0 | -10.0 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | -3.8 | -8.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | -0.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -5.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | +0.8 |
|  | [[Cyclosporin A (drug)]] 0.05 µM |  | -1.7 | -2.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.7 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | NUDT16 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 3q21.3 — chr3:131,325,092-131,381,656 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:27947](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27947) · Entrez [339874](https://www.ncbi.nlm.nih.gov/gene/339874) · Ensembl [ENSG00000250608](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250608)

## Data

Gene col 14706: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14706); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14706, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14706]; `tensor/DDL_lfc|DDL_z.npy` [14706]; `embed/gene_vectors.npy` [14706]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14706 or target_col == 14706). Every well: [[NUDT16-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NUDT16-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
