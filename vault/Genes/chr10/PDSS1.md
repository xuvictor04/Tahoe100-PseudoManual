---
symbol: "PDSS1"
type: "gene"
col: 7286
ensembl_id: "ENSG00000148459"
name: "decaprenyl diphosphate synthase subunit 1"
location: "10p12.1"
module: 33
arm: "+"
pooled_cpm: 17.03
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 10
n_dd_up_clean: 13
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# PDSS1

*decaprenyl diphosphate synthase subunit 1* — 10p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.81× (z +11.1, q 1e-25, up in 38 of 47 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[EX229 (drug)]] 5 µM: 2.28× (z +6.7, q 2e-09, up in 25 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 0.616× (z -9.0, q 9e-17, down in 28 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POLR1B]] (+0.71, fdr 7e-06), [[AGK]] (+0.69, fdr 7e-06), [[PIGU]] (+0.69, fdr 7e-06); moves opposite to [[YPEL5]] (-0.74, fdr 7e-06), [[TAX1BP1]] (-0.66, fdr 3e-05), [[SMIM14]] (-0.66, fdr 1e-05).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TERT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7286.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.81×** | +11.1 | 1e-25 | 38/47 (NCI-H460, A498, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **1.48×** | +7.4 | 6e-11 | 25/47 (A498, NCI-H1792, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.47×** | +7.2 | 1e-10 | 26/48 (A498, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **2.28×** | +6.7 | 2e-09 | 25/45 (A498, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | **1.43×** | +6.5 | 1e-08 | 23/43 (NCI-H1573, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.38×** | +6.1 | 1e-07 | 22/48 (A498, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +5.1 | 4e-05 | 19/47 (CFPAC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-733 (drug)]] 5 µM |  | **1.78×** | +4.7 | 2e-04 | 12/45 (A498, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.42×** | +4.7 | 2e-04 | 11/48 (A498, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.41×** | +4.5 | 3e-04 | 12/47 (NCI-H23, A498, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.74×** | +4.5 | 3e-04 | 11/24 (NCI-H2030, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.73×** | +4.5 | 4e-04 | 10/45 (A498, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.70×** | +4.4 | 6e-04 | 13/44 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.64×** | +4.0 | 0.002 | 10/48 (HEC-1-A, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.24×** | +3.9 | 0.004 | 15/47 (LoVo, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **1.60×** | +3.8 | 0.005 | 8/42 (NCI-H460, A498, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.5 µM |  | **1.31×** | +3.6 | 0.011 | 10/48 (A498, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.53×** | +3.5 | 0.014 | 7/47 (A498, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **1.43×** | +2.9 | 0.090 | 7/43 (SW48, A498, …) | top dose only | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | 1.18× | +2.9 | 0.097 | 8/48 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7286.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **0.616×** | -9.0 | 9e-17 | 28/46 (AN3 CA, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.769×** | -4.9 | 2e-04 | 18/48 (KATO III, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.763×** | -4.8 | 2e-04 | 17/46 (C32, HOP62, …) | rises with dose |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.713×** | -4.5 | 9e-04 | 15/46 (BT-474, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.815×** | -4.5 | 9e-04 | 16/48 (NCI-H23, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.798×** | -4.2 | 0.003 | 18/42 (C-33 A, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.835× | -4.1 | 0.003 | 13/48 (SW480, HEC-1-A, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.798×** | -4.1 | 0.003 | 11/48 (SW48, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 0.5 µM |  | **0.759×** | -3.7 | 0.015 | 10/45 (COLO 205, HEC-1-A, …) | two highest doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | 0.871× | -3.6 | 0.016 | 13/48 (LS 180, HT-29, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.819×** | -3.6 | 0.019 | 12/46 (NCI-H23, HepG2/C3A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.876× | -3.5 | 0.024 | 17/47 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.832×** | -3.4 | 0.027 | 6/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Cyclosporin A (drug)]] 0.5 µM |  | 0.834× | -3.4 | 0.030 | 7/47 (SW 1088, SHP-77, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.837× | -3.3 | 0.036 | 14/47 (KATO III, NCI-H460, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.853× | -3.1 | 0.068 | 7/48 (SW480, NCI-H460, …) | two highest doses | noisy plate (z scaled) |
| [[Ferulic acid (drug)]] 0.05 µM |  | 0.838× | -3.0 | 0.082 | 10/46 (PANC-1, BT-474, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.851× | -3.0 | 0.088 | 5/46 (A-172, LS 180, …) | inconsistent across doses | low cells (technical?) |
| [[Cyclosporin A (drug)]] 0.05 µM |  | 0.852× | -3.0 | 0.088 | 7/48 (J82, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7286. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 16.8 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -9.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.273× (z -8.6) |
| [[BT-474 (line)]] | alt | 16.5 | 0 | 3 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.133× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 17.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.227× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.274× (z -8.8) |
| [[A-427 (line)]] | wt | 20.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -10.1) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 21.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0753× (z -9.1) |
| [[C-33 A (line)]] | alt | 30.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.150× (z -11.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.328× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 12.9 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.0853× (z -9.2) |
| [[HOP62 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[hTERT-HPNE (line)]] | wt | 11.4 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.0595× (z -11.9) |
| [[KATO III (line)]] | alt | 11.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.166× (z -8.9) |
| [[LOX-IMVI (line)]] | wt | 26.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.430× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 27.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H23 (line)]] | alt | 21.6 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.307× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 14.6 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.17× (z +8.7) ⚠ unreliable plate only | — |
| [[SW480 (line)]] | alt | 26.1 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.388× (z -8.6) |
| [[A498 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.32 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.83 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.06 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7286), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR1B]] | +0.71 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[AGK]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 |  |
| [[PIGU]] | +0.69 | +0.58 / +0.68 | both halves | 7e-06 |  |
| [[LYAR]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[NLE1]] | +0.68 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[EIF2B3]] | +0.67 | +0.53 / +0.70 | both halves | 1e-05 |  |
| [[DDX31]] | +0.67 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[SNRPD1]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[GEMIN5]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[WDR3]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[C19orf48]] | +0.66 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[XPO4]] | +0.65 | +0.63 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YPEL5]] | -0.74 | -0.65 / -0.73 | both halves | 7e-06 |  |
| [[TAX1BP1]] | -0.66 | -0.46 / -0.72 | both halves | 3e-05 |  |
| [[SMIM14]] | -0.66 | -0.49 / -0.70 | both halves | 1e-05 |  |
| [[GABARAPL1]] | -0.65 | -0.50 / -0.63 | both halves | 1e-05 |  |
| [[KLHL24]] | -0.64 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[TCP11L2]] | -0.64 | -0.54 / -0.69 | both halves | 1e-05 |  |
| [[RB1CC1]] | -0.62 | -0.52 / -0.66 | both halves | 1e-05 |  |
| [[HBP1]] | -0.61 | -0.53 / -0.60 | both halves | 1e-05 |  |
| [[CREBRF]] | -0.60 | -0.51 / -0.58 | both halves | 1e-05 |  |
| [[SWT1]] | -0.58 | -0.48 / -0.55 | both halves | 2e-05 |  |
| [[ATOSA]] | -0.57 | -0.56 / -0.51 | both halves | 1e-05 |  |
| [[SQSTM1]] | -0.57 | -0.51 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | TERT activity raises PDSS1's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.41× lower at baseline in the lines without TERT | 0.047 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[ATXN1]] | B | ATXN1 activity strengthens PDSS1's drug response | lines that do not express ATXN1 (6) vs lines expressing it (42) | the lines without ATXN1 respond 0.64× as strongly (z diff +0.62); strongest at Panobinostat 5 µM: 0.95x vs 1.47x (z diff +2.3) | 0.076 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2; target measured in part of the lines; artifact flags |
| [[FBXO32]] | B | FBXO32 activity lowers PDSS1's level | lines that do not express FBXO32 (14) vs lines expressing it (36) | 1.40× higher at baseline in the lines without FBXO32 | 0.089 | ⚠ within organs, on part of the lines; also absent: ETS2, BACE2, MLPH; maybe low, not absent |
| [[ATXN1]] | B | ATXN1 activity lowers PDSS1's level | lines that do not express ATXN1 (6) vs lines expressing it (44) | 1.60× higher at baseline in the lines without ATXN1 | 0.093 | ⚠ within organs, on part of the lines; also absent: ATXN1-AS1, LAMB1, SYTL2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.748). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-13.3, -40.3); signed map (-7.9, -49.2). **Vector** length 94.0, 19.4% of its response variance represented; |z| ≥ 3 in 905 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MYC targets v2* (hallmark, mean cos +0.53 to 8); *rRNA modification in the nucleus and cytosol* (reactome, mean cos +0.56 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.7 | +11.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~48% of this change | +5.2 | +6.5 |
|  | [[EX229 (drug)]] 5 µM |  | +4.7 | +6.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.0 | +4.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.9 | +4.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.3 | +4.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.0 | +3.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.9 | -9.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -4.2 | -4.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.1 | -4.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.0 | -3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.0 | -4.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -2.7 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | decaprenyl diphosphate synthase subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p12.1 — chr10:26,697,701-26,746,798 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TPT, COQ1, COQ1A; previously TPRT |
| Reactome | 3 pathways, smallest: Ubiquinol biosynthesis; Metabolism of cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T2R2](https://www.uniprot.org/uniprotkb/Q5T2R2) (All trans-polyprenyl-diphosphate synthase PDSS1):

> Heterotetrameric enzyme that catalyzes the condensation of farnesyl diphosphate (FPP), which acts as a primer, and isopentenyl diphosphate (IPP) to produce prenyl diphosphates of varying chain lengths and participates in the determination of the side chain of ubiquinone. Supplies nona and decaprenyl diphosphate, the precursors for the side chain of the isoprenoid quinones ubiquinone-9 (Q9)and ubiquinone-10 (Q10) respectively. The enzyme adds isopentenyl diphosphate molecules sequentially to …

**Summary**, from NCBI Gene [23590](https://www.ncbi.nlm.nih.gov/gene/23590):

> The protein encoded by this gene is an enzyme that elongates the prenyl side-chain of coenzyme Q, or ubiquinone, one of the key elements in the respiratory chain. The gene product catalyzes the formation of all trans-polyprenyl pyrophosphates from isopentyl diphosphate in the assembly of polyisoprenoid side chains, the first step in coenzyme Q biosynthesis. The protein may be peripherally associated with the inner mitochondrial membrane, though no transit peptide has been definitively …

**Accessions** — [HGNC:17759](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17759) · Entrez [23590](https://www.ncbi.nlm.nih.gov/gene/23590) · UniProt [Q5T2R2](https://www.uniprot.org/uniprotkb/Q5T2R2) · Ensembl [ENSG00000148459](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148459)

## Data

Gene col 7286: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7286); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7286, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7286]; `tensor/DDL_lfc|DDL_z.npy` [7286]; `embed/gene_vectors.npy` [7286]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7286 or target_col == 7286). Every well: [[PDSS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDSS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
