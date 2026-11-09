---
symbol: "GALNS"
type: "gene"
col: 6479
ensembl_id: "ENSG00000141012"
name: "galactosamine (N-acetyl)-6-sulfatase"
location: "16q24.3"
module: 2
arm: "+"
pooled_cpm: 18.98
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 12
n_dd_up_clean: 8
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# GALNS

*galactosamine (N-acetyl)-6-sulfatase* — 16q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.23× (z +13.2, q 5e-37, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.533× (z -14.6, q 3e-45, down in 33 of 47 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.457× (z -12.8, q 4e-35, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLBD2]] (+0.67, fdr 7e-06), [[FBRSL1]] (+0.66, fdr 1e-05), [[SIN3B]] (+0.65, fdr 1e-05); moves opposite to [[RWDD2B]] (-0.60, fdr 7e-05), [[TP53]] (-0.59, fdr 4e-05), [[SLC16A14]] (-0.58, fdr 5e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6479.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.23×** | +13.2 | 5e-37 | 40/48 (SW480, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.87×** | +10.3 | 2e-22 | 37/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.43×** | +5.9 | 9e-07 | 25/48 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.38×** | +5.0 | 7e-05 | 22/47 (J82, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.31×** | +4.2 | 0.003 | 14/31 (LoVo, SW 900, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Rapamycin (drug)]] 5 µM |  | 1.19× | +4.1 | 0.003 | 8/48 (AsPC-1, NCI-H460, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.18× | +3.9 | 0.006 | 13/48 (MIA PaCa-2, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.30×** | +3.9 | 0.006 | 13/40 (PANC-1, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[GSK1059615 (drug)]] 5 µM |  | **1.52×** | +3.6 | 0.019 | 4/46 (A-427, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cepharanthine (drug)]] 5 µM |  | 1.17× | +3.6 | 0.019 | 8/48 (NCI-H2030, HEC-1-A, …) | rises with dose |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.020 | 10/48 (SW480, HT-29, …) | top dose only | plate-row cell shift; position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.025 | 12/47 (HOP62, HS-578T, …) | rises with dose | low cells (technical?) |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.24×** | +3.3 | 0.040 | 4/48 (NCI-H460, A-172, …) | inconsistent across doses | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.22×** | +3.3 | 0.040 | 9/48 (HOP62, A549, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.23×** | +3.2 | 0.060 | 11/34 (SHP-77, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.22×** | +3.1 | 0.077 | 5/47 (PANC-1, SW480, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6479.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.533×** | -14.6 | 3e-45 | 33/47 (HOP62, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.457×** | -12.8 | 4e-35 | 37/46 (A-427, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.659×** | -9.6 | 1e-19 | 34/46 (MIA PaCa-2, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.563×** | -8.9 | 8e-17 | 31/47 (H4, NCI-H2030, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.624×** | -7.3 | 3e-11 | 29/45 (NCI-H23, H4, …) | top dose only | cell-cycle shift (explains ~24% here); position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.613×** | -7.2 | 4e-11 | 37/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.789×** | -5.5 | 4e-06 | 25/48 (NCI-H2347, SNU-423, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.709×** | -5.3 | 7e-06 | 23/48 (BT-474, A-427, …) | top dose only | cell-cycle shift (explains ~7% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.718×** | -5.1 | 2e-05 | 24/47 (C-33 A, AN3 CA, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.912× | -5.1 | 2e-05 | 4/48 (AN3 CA, SW 1088, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.788×** | -3.9 | 0.005 | 18/48 (NCI-H661, NCI-H460, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.679×** | -3.3 | 0.043 | 8/48 (NCI-H1792, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.814×** | -3.1 | 0.086 | 16/46 (NCI-H460, SW 1271, …) | all doses, stronger at high dose | low cells (technical?); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | 0.876× | -3.0 | 0.100 | 11/48 (C32, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6479. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 12.3 | 0 | 4 | — | [[Fulvestrant (drug)]] 0.5 µM 0.0735× (z -11.0) |
| [[HOP62 (line)]] | alt | 21.3 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.18× (z +9.4) | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -14.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[MIA PaCa-2 (line)]] | alt | 36.1 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -13.2) |
| [[NCI-H2030 (line)]] | alt | 30.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.425× (z -10.3) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.362× (z -8.7) |
| [[A-172 (line)]] | wt | 43.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.313× (z -10.1) |
| [[H4 (line)]] | wt | 24.6 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0756× (z -12.1) ⚠ cell-cycle shift, explains ~39% of this change |
| [[hTERT-HPNE (line)]] | wt | 18.8 | 0 | 2 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.103× (z -10.4) |
| [[KATO III (line)]] | alt | 21.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.71× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 27.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.360× (z -10.5) |
| [[SNU-423 (line)]] | alt | 23.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -10.2) |
| [[A-427 (line)]] | wt | 23.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.202× (z -11.4) |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.116× (z -8.9) |
| [[C-33 A (line)]] | alt | 21.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -8.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[CFPAC-1 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -9.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HEC-1-A (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.189× (z -9.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 19.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -10.0) ⚠ cell-cycle shift, explains ~42% of this change |
| [[LoVo (line)]] | wt | 12.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -9.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H1792 (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0666× (z -9.2) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 6.63 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.288× (z -9.4) |
| [[SW1417 (line)]] | alt | 9.58 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -9.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[SW480 (line)]] | alt | 11.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.86× (z +10.0) | — |
| [[A498 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 17.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6479), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLBD2]] | +0.67 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[FBRSL1]] | +0.66 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[SIN3B]] | +0.65 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[GDI1]] | +0.65 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[MAN2B2]] | +0.64 | +0.66 / +0.53 | both halves | 1e-05 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[INTS1]] | +0.62 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[PPP1R12C]] | +0.62 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[INTS11]] | +0.62 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[STK25]] | +0.61 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[SBF1]] | +0.61 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[GNPTG]] | +0.60 | +0.64 / +0.39 | both halves | 5e-05 | STRING 448 |
| [[TCF3]] | +0.60 | +0.52 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RWDD2B]] | -0.60 | -0.57 / -0.38 | both halves | 7e-05 |  |
| [[TP53]] | -0.59 | -0.53 / -0.40 | both halves | 4e-05 |  |
| [[SLC16A14]] | -0.58 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[PPCS]] | -0.58 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[NFYB]] | -0.58 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[C1orf131]] | -0.57 | -0.59 / -0.43 | both halves | 3e-05 |  |
| [[MPLKIP]] | -0.56 | -0.57 / -0.51 | both halves | 1e-05 |  |
| [[C3orf38]] | -0.56 | -0.45 / -0.39 | both halves | 5e-05 |  |
| [[CREB3L4]] | -0.55 | -0.49 / -0.36 | both halves | 1e-04 |  |
| [[TAPT1]] | -0.55 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[HOXA10-AS]] | -0.55 | -0.44 / -0.38 | both halves | 7e-05 |  |
| [[ZNF85]] | -0.55 | -0.50 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises GALNS's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HOXB4]] | B | HOXB4 activity raises GALNS's level | lines that do not express HOXB4 (12) vs lines expressing it (38) | 1.30× lower at baseline in the lines without HOXB4 | 0.074 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LHFPL6]] | B | LHFPL6 activity raises GALNS's level | lines that do not express LHFPL6 (11) vs lines expressing it (39) | 1.45× lower at baseline in the lines without LHFPL6 | 0.091 | ⚠ within organs, on part of the lines; also absent: KATNAL2, AFAP1L1, TTC7B |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.698). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-6.7, -23.6); signed map (-45.7, -9.0). **Vector** length 88.5, 17.8% of its response variance represented; |z| ≥ 3 in 960 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +6.1 | +13.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.1 | +10.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +4.2 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.1 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +3.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.9 | +3.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.6 | -1.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.0 | +3.9 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.9 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.6 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.1 | -12.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -5.7 | -14.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -5.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.3 | -5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -3.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.4 | -2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.4 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | galactosamine (N-acetyl)-6-sulfatase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q24.3 — chr16:88,813,734-88,856,970 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GAS, GALNAC6S, GalN6S |
| Gene groups (HGNC) | Sulfatases |
| Reactome | 9 pathways, smallest: Keratan sulfate degradation; Mucopolysaccharidoses; Keratan sulfate/keratin metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P34059](https://www.uniprot.org/uniprotkb/P34059) (N-acetylgalactosamine-6-sulfatase):

> Lysosomal enzyme that hydrolyzes sulfate groups from glycosaminoglycans (GAGs), keratan sulfate (KS) and chondroitin-6-sulfate (C6S).

**Summary**, from NCBI Gene [2588](https://www.ncbi.nlm.nih.gov/gene/2588):

> This gene encodes N-acetylgalactosamine-6-sulfatase which is a lysosomal exohydrolase required for the degradation of the glycosaminoglycans, keratan sulfate, and chondroitin 6-sulfate. Sequence alterations including point, missense and nonsense mutations, as well as those that affect splicing, result in a deficiency of this enzyme. Deficiencies of this enzyme lead to Morquio A syndrome, a lysosomal storage disorder. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4122](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4122) · Entrez [2588](https://www.ncbi.nlm.nih.gov/gene/2588) · UniProt [P34059](https://www.uniprot.org/uniprotkb/P34059) · Ensembl [ENSG00000141012](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141012)

## Data

Gene col 6479: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6479); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6479, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6479]; `tensor/DDL_lfc|DDL_z.npy` [6479]; `embed/gene_vectors.npy` [6479]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6479 or target_col == 6479). Every well: [[GALNS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALNS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
