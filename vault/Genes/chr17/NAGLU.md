---
symbol: "NAGLU"
type: "gene"
col: 2993
ensembl_id: "ENSG00000108784"
name: "N-acetyl-alpha-glucosaminidase"
location: "17q21.2"
module: 36
arm: "+"
pooled_cpm: 6.65
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 13
n_dd_up_clean: 4
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/036"]
generated_by: "tahoemap"
---

# NAGLU

*N-acetyl-alpha-glucosaminidase* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.5 µM: 1.58× (z +6.4, q 8e-08, up in 20 of 44 measured lines) ⚠ cell-cycle shift, explains ~55% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.40× (z +4.8, q 3e-04, up in 9 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.666× (z -8.1, q 4e-13, down in 24 of 42 measured lines) ⚠ cell-cycle shift, explains ~73% of this change. The strongest without an alert is [[5-Azacytidine (drug)]] 5 µM: 0.765× (z -3.8, q 0.011, down in 8 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MED9]] (+0.59, fdr 1e-05), [[MORN4]] (+0.55, fdr 1e-05), [[JRK]] (+0.54, fdr 2e-05); moves opposite to [[ZSWIM6]] (-0.52, fdr 3e-05), [[DDX5]] (-0.49, fdr 3e-05), [[TEX14]] (-0.46, fdr 3e-05).
> It sits in the **+** arm of [[Module 036]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2993.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **1.58×** | +6.4 | 8e-08 | 20/44 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.35×** | +6.1 | 4e-07 | 16/47 (NCI-H2347, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +4.8 | 3e-04 | 9/47 (A-172, HOP62, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.25×** | +4.3 | 0.002 | 9/47 (HepG2/C3A, HCT15, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.37×** | +3.8 | 0.018 | 2/44 (A-172, A498) | rises with dose |  |
| [[Afatinib (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.072 | 5/48 (CFPAC-1, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.31× | +3.2 | 0.10 | 6/45 (NCI-H460, HOP62, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | 1.25× | +3.1 | 0.11 | 3/48 (SNU-423, A549, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.26× | +3.1 | 0.11 | 5/33 (NCI-H1573, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 1.24× | +3.1 | 0.12 | 8/46 (NCI-H460, A-172, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.25× | +3.0 | 0.12 | 2/14 (CFPAC-1, NCI-H2030) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.24× | +3.0 | 0.12 | 5/46 (SNU-423, C32, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 10 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2993.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~73% of this change | **0.666×** | -8.1 | 4e-13 | 24/42 (A498, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.582×** | -7.3 | 8e-11 | 24/45 (SW 900, SK-MEL-2, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.660×** | -5.8 | 1e-06 | 19/40 (KATO III, HS-578T, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **0.672×** | -5.6 | 3e-06 | 14/47 (SW480, HOP62, …) | inconsistent across doses | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.714×** | -4.5 | 6e-04 | 15/41 (NCI-H2347, A498, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.728×** | -4.5 | 8e-04 | 20/46 (A549, SW48, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.572×** | -4.1 | 0.003 | 12/46 (PANC-1, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.756×** | -3.9 | 0.007 | 8/47 (KATO III, H4, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.765×** | -3.8 | 0.011 | 8/47 (HT-29, SW1417, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.751×** | -3.4 | 0.039 | 10/46 (HT-29, C-33 A, …) | two highest doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | **0.788×** | -3.3 | 0.044 | 14/44 (HOP62, NCI-H2347, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.653×** | -3.1 | 0.080 | 9/41 (SW480, LS 180, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.793×** | -3.1 | 0.080 | 14/42 (hTERT-HPNE, C32, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2993. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 4.29 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0763× (z -10.9) |
| [[AsPC-1 (line)]] | alt | 3.02 | 0 | 2 | — | [[Canagliflozin (drug)]] 0.5 µM 0.0587× (z -8.8) |
| [[A498 (line)]] | wt | 9.28 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -10.1) ⚠ cell-cycle shift, explains ~73% of this change |
| [[BT-474 (line)]] | alt | 5.81 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -8.6) ⚠ cell-cycle shift, explains ~73% of this change |
| [[NCI-H1792 (line)]] | alt | 4.80 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0816× (z -8.7) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H460 (line)]] | wt | 6.03 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.212× (z -9.1) |
| [[PANC-1 (line)]] | alt | 6.76 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -12.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 6.66 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.207× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.15 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.85 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.91 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.90 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.33 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.49 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.28 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.11 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.85 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.20 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2993), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MED9]] | +0.59 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[MORN4]] | +0.55 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[JRK]] | +0.54 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[ZNF169]] | +0.54 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[AVL9]] | +0.54 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[SNX8]] | +0.54 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[VPS33A]] | +0.53 | +0.43 / +0.62 | both halves | 3e-05 |  |
| [[HEXA]] | +0.53 | +0.41 / +0.61 | both halves | 4e-05 | pathway: Diseases of metabolism; STRING 442 |
| [[CLCN6]] | +0.53 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[SPNS1]] | +0.52 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[TIGD1]] | +0.51 | +0.39 / +0.54 | both halves | 6e-05 |  |
| [[GTF3C2]] | +0.50 | +0.47 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZSWIM6]] | -0.52 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[DDX5]] | -0.49 | -0.43 / -0.61 | both halves | 3e-05 |  |
| [[TEX14]] | -0.46 | -0.52 / -0.46 | both halves | 3e-05 |  |
| [[MAST4]] | -0.46 | -0.38 / -0.42 | both halves | 6e-05 |  |
| [[FOSB]] | -0.46 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[SCHIP1]] | -0.45 | -0.26 / -0.55 | both halves | 4e-04 |  |
| [[TLE4]] | -0.45 | -0.36 / -0.47 | both halves | 9e-05 |  |
| [[SETBP1]] | -0.44 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[MYH15]] | -0.44 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[KBTBD8]] | -0.44 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[HOMER1]] | -0.43 | -0.40 / -0.44 | both halves | 4e-05 |  |
| [[DPF3]] | -0.43 | -0.25 / -0.48 | both halves | 4e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.239). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-29.3, -7.8); signed map (-14.4, -19.4). **Vector** length 56.4, 7.56% of its response variance represented; |z| ≥ 3 in 881 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | +4.0 | +6.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | +3.7 | +6.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.7 | +3.1 |
|  | [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | +2.2 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.1 | +1.3 |
|  | [[EX229 (drug)]] 5 µM |  | +2.0 | +2.0 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +4.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.8 | +1.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.8 | +0.8 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.4 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -2.2 | -7.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -1.8 | -4.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -2.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -1.7 | -3.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.4 | -2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | N-acetyl-alpha-glucosaminidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:42,536,241-42,544,449 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NAG |
| Gene groups (HGNC) | Glycoside hydrolase family |
| Reactome | 7 pathways, smallest: Mucopolysaccharidoses; HS-GAG degradation; Diseases of carbohydrate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P54802](https://www.uniprot.org/uniprotkb/P54802) (Alpha-N-acetylglucosaminidase):

> Involved in the degradation of heparan sulfate.

**Summary**, from NCBI Gene [4669](https://www.ncbi.nlm.nih.gov/gene/4669):

> This gene encodes an enzyme that degrades heparan sulfate by hydrolysis of terminal N-acetyl-D-glucosamine residues in N-acetyl-alpha-D-glucosaminides. Defects in this gene are the cause of mucopolysaccharidosis type IIIB (MPS-IIIB), also known as Sanfilippo syndrome B. This disease is characterized by the lysosomal accumulation and urinary excretion of heparan sulfate. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7632](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7632) · Entrez [4669](https://www.ncbi.nlm.nih.gov/gene/4669) · UniProt [P54802](https://www.uniprot.org/uniprotkb/P54802) · Ensembl [ENSG00000108784](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108784)

## Data

Gene col 2993: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2993); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2993, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2993]; `tensor/DDL_lfc|DDL_z.npy` [2993]; `embed/gene_vectors.npy` [2993]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2993 or target_col == 2993). Every well: [[NAGLU — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAGLU.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
