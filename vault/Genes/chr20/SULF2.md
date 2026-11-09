---
symbol: "SULF2"
type: "gene"
col: 12237
ensembl_id: "ENSG00000196562"
name: "sulfatase 2"
location: "20q13.12"
module: 73
arm: "+"
pooled_cpm: 57.25
n_lines_expressing: 26
n_dd_up: 20
n_dd_down: 11
n_dd_up_clean: 13
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 49
direction_downstream: 47
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# SULF2

*sulfatase 2* — 20q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.01× (z +18.5, q 0e+00, up in 13 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.736× (z -5.8, q 5e-06, down in 19 of 24 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INPP1]] (+0.72, fdr 7e-06), [[SEPTIN9-DT]] (+0.69, fdr 7e-06), [[COL17A1]] (+0.64, fdr 7e-06).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 49 arrows point to it, the strongest [[NOSTRIN]] → it (grade B ⚠); 47 go from it, the strongest it → [[MYO18A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 13 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12237.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.01×** | +18.5 | 0e+00 | 13/24 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.98×** | +12.8 | 6e-35 | 7/23 (H4, A-172, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +11.2 | 1e-26 | 6/21 (A549, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +11.0 | 4e-26 | 9/24 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.87×** | +10.8 | 3e-25 | 8/21 (A-172, H4, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +9.1 | 1e-17 | 4/24 (BT-474, RPMI-7951, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +7.8 | 4e-13 | 10/24 (NCI-H460, A549, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.40×** | +6.3 | 2e-08 | 12/24 (SW1417, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.33×** | +5.4 | 5e-06 | 6/24 (SW1417, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +5.3 | 8e-06 | 7/22 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.6 | 2e-04 | 9/24 (SW48, A-172, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.4 | 6e-04 | 5/15 (A549, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.56×** | +4.3 | 7e-04 | 6/21 (SW480, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +4.0 | 0.002 | 9/24 (A498, LS 180, …) | all doses, flat | low cells (technical?) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.23×** | +3.9 | 0.004 | 3/23 (KATO III, Hs 766T, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.7 | 0.007 | 10/24 (A549, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Arbutin (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.017 | 3/24 (A498, Hs 766T, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.29×** | +3.4 | 0.019 | 1/24 (NCI-H460) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.4 | 0.020 | 8/23 (A549, BT-474, …) | inconsistent across doses | low cells (technical?) |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.21×** | +3.3 | 0.020 | 7/23 (CHP-212, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[OTS514 (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.061 | 4/23 (KATO III, Panc 03.27, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12237.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.736×** | -5.8 | 5e-06 | 19/24 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.751×** | -5.4 | 2e-05 | 13/24 (LoVo, AsPC-1, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.762×** | -5.1 | 6e-05 | 15/24 (Panc 03.27, LS 180, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.794×** | -4.3 | 0.002 | 17/24 (AsPC-1, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.851× | -4.3 | 0.002 | 12/24 (KATO III, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.660×** | -4.1 | 0.004 | 11/24 (LoVo, A-172, …) | rises with dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.943× | -4.0 | 0.005 | 2/24 (SW 1088, CHP-212) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 0.05 µM |  | **0.813×** | -3.7 | 0.016 | 0/24 | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.689×** | -3.7 | 0.016 | 7/24 (LoVo, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.816×** | -3.5 | 0.023 | 5/24 (SW480, CFPAC-1, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.825×** | -3.5 | 0.027 | 6/23 (Panc 03.27, KATO III, …) | top dose only |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | 0.835× | -3.4 | 0.028 | 7/24 (HT-29, COLO 205, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.835× | -3.4 | 0.028 | 1/24 (Hs 766T) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.878× | -3.4 | 0.028 | 7/24 (SW480, COLO 205, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.825×** | -3.3 | 0.032 | 0/24 | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.829×** | -3.3 | 0.041 | 0/24 | inconsistent across doses |  |
| [[Futibatinib (drug)]] 0.05 µM |  | 0.839× | -3.1 | 0.057 | 0/24 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12237. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 133 | 1 | 9 (6 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.93× (z +8.5) | [[Panobinostat (drug)]] 5 µM 0.105× (z -20.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.122× (z -19.3) |
| [[A498 (line)]] | wt | 53.6 | 6 (2 ⚠) | 1 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 5.27× (z +13.0) | [[Auranofin (drug)]] 5 µM 0.315× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 348 | 0 | 7 (4 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0835× (z -25.2) |
| [[LS 180 (line)]] | wt | 61.2 | 3 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.55× (z +18.5) | [[Panobinostat (drug)]] 5 µM 0.299× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.342× (z -9.3) |
| [[A549 (line)]] | wt | 35.1 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.51× (z +16.8) | — |
| [[NCI-H460 (line)]] | wt | 15.9 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.25× (z +19.3) | — |
| [[Panc 03.27 (line)]] | alt | 199 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.190× (z -15.0) |
| [[Hs 766T (line)]] | wt | 458 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -19.9) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.252× (z -13.3) |
| [[KATO III (line)]] | alt | 264 | 0 | 5 (3 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.179× (z -15.5) |
| [[HT-29 (line)]] | alt | 159 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -13.8) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.222× (z -10.2) |
| [[A-172 (line)]] | wt | 31.5 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.80× (z +12.5) | — |
| [[SW480 (line)]] | alt | 77.0 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.285× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.304× (z -12.3) |
| [[CFPAC-1 (line)]] | alt | 48.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -9.7) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H23 (line)]] | alt | 22.3 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 5.63× (z +9.9) ⚠ cell-cycle shift, explains ~24% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 141 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.00× (z +11.1) ⚠ cell-cycle shift, explains ~43% of this change | [[Panobinostat (drug)]] 0.5 µM 0.414× (z -10.0) |
| [[COLO 205 (line)]] | alt | 59.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -13.8) ⚠ cell-cycle shift, explains ~43% of this change |
| [[RPMI-7951 (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.203× (z -9.7) ⚠ cell-cycle shift, explains ~9% of this change |
| [[SW48 (line)]] | wt | 31.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.55× (z +11.2) | — |
| [[A-427 (line)]] | wt | 8.97 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 99.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 9.32 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.72 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 66.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 40.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.60 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.48 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.08 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.54 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.90 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.22 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.92 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.70 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.32 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 6.38 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.97 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.42 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.09 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.23 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 8.97 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.76 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.05 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12237), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INPP1]] | +0.72 | +0.67 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[SEPTIN9-DT]] | +0.69 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[COL17A1]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[SERPINB5]] | +0.64 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[DGKA]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[INPP5D]] | +0.61 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[PINCR]] | +0.60 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[KIAA0040]] | +0.60 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[ZMAT3]] | +0.59 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[AFAP1L2]] | +0.59 | +0.66 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_APICAL_SURFACE |
| [[EFNB1]] | +0.59 | +0.56 / +0.64 | both halves | 1e-05 |  |
| [[HSD17B2]] | +0.58 | +0.62 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*49 arrows, 49 of them with an alert ⚠; grade A 0, B 9, C 40. Shown: the 12 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NOSTRIN]] | B | NOSTRIN activity raises SULF2's level | lines that do not express NOSTRIN (16) vs lines expressing it (34) | 2.67× lower at baseline in the lines without NOSTRIN | 0.026 | ⚠ within organs, on part of the lines; also absent: SLC9A2, SLPI, SULT2B1; maybe low, not absent |
| [[GRHL3]] | B | GRHL3 activity raises SULF2's level | lines that do not express GRHL3 (16) vs lines expressing it (34) | 2.77× lower at baseline in the lines without GRHL3 | 0.049 | ⚠ within organs, on part of the lines; also absent: SPINT2, FA2H, CDC42BPG; maybe low, not absent |
| [[TGFA]] | B | TGFA activity raises SULF2's level | lines that do not express TGFA (17) vs lines expressing it (33) | 3.49× lower at baseline in the lines without TGFA | 0.060 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[PTPRB]] | B | PTPRB activity raises SULF2's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 2.54× lower at baseline in the lines without PTPRB | 0.063 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4 |
| [[TNFRSF14-AS1]] | B | TNFRSF14-AS1 activity raises SULF2's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 2.42× lower at baseline in the lines without TNFRSF14-AS1 | 0.065 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB |
| [[PCDH1]] | B | PCDH1 activity raises SULF2's level | lines that do not express PCDH1 (20) vs lines expressing it (30) | 2.68× lower at baseline in the lines without PCDH1 | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000286736, ERBB3, TRIM29 |
| [[PINCR]] | B | PINCR activity strengthens SULF2's drug response | lines that do not express PINCR (12) vs lines expressing it (12) | the lines without PINCR respond the other way (z diff +2.90); strongest at Epirubicin (hydrochloride) 5 µM: 0.65x vs 2.35x (z diff +7.8) | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; artifact flags |
| [[KIAA0040]] | B | KIAA0040 activity raises SULF2's level | lines that do not express KIAA0040 (24) vs lines expressing it (26) | 2.93× lower at baseline in the lines without KIAA0040 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, CLDN3, ESRP1 |
| [[HS3ST1]] | B | HS3ST1 activity raises SULF2's level | lines that do not express HS3ST1 (31) vs lines expressing it (19) | 3.03× lower at baseline in the lines without HS3ST1 | 0.087 | ⚠ within organs, on part of the lines; also absent: KLK10, ADGRF1, TMPRSS4 |
| [[LGR6]] | C | LGR6 activity raises SULF2's level | lines that do not express LGR6 (35) vs lines expressing it (15) | 6.32× lower at baseline in the lines without LGR6 | 0.001 | ⚠ within organs, on part of the lines; also absent: SLC6A20, LINC01559, VWA2; co-absent with the target |
| [[HSD17B2]] | C | HSD17B2 activity raises SULF2's level | lines that do not express HSD17B2 (35) vs lines expressing it (15) | 6.61× lower at baseline in the lines without HSD17B2 | 0.001 | ⚠ within organs, on part of the lines; also absent: KRT23, S100P, TFF2; co-absent with the target |
| [[SLC22A3]] | C | SLC22A3 activity raises SULF2's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 4.73× lower at baseline in the lines without SLC22A3 | 0.002 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA; co-absent with the target |

### Downstream of this gene

*47 arrows, 47 of them with an alert ⚠; grade A 0, B 20, C 27. Shown: the 12 strongest; 35 more arrows (35 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYO18A]] | B | SULF2 activity raises MYO18A's level | lines that do not express SULF2 (24) vs lines expressing it (26) | 1.74× lower at baseline in the lines without SULF2 | 0.007 | ⚠ within organs, on part of the lines; also absent: FOXQ1, HR, HNF1A-AS1 |
| [[PLCD3]] | B | SULF2 activity raises PLCD3's level | lines that do not express SULF2 (24) vs lines expressing it (26) | 1.80× lower at baseline in the lines without SULF2 | 0.018 | ⚠ within organs, on part of the lines; also absent: FOXQ1, HR, HNF1A-AS1 |
| [[BAIAP2L2]] | B | SULF2 activity raises BAIAP2L2's level | lines that do not express SULF2 (24) vs lines expressing it (26) | 2.06× lower at baseline in the lines without SULF2 | 0.021 | ⚠ within organs, on part of the lines; also absent: FOXQ1, HR, HNF1A-AS1 |
| [[NOSTRIN]] | B | SULF2 activity raises NOSTRIN's level | lines that do not express SULF2 (24) vs lines expressing it (26) | 2.05× lower at baseline in the lines without SULF2 | 0.023 | ⚠ within organs, on part of the lines; also absent: FOXQ1, HR, HNF1A-AS1 |
| [[SLC52A3]] | B | SULF2 activity raises SLC52A3's level | lines that do not express SULF2 (24) vs lines expressing it (26) | 2.38× lower at baseline in the lines without SULF2 | 0.038 | ⚠ within organs, on part of the lines; also absent: FOXQ1, HR, HNF1A-AS1 |
| [[EPB41L1]] | B | SULF2 activity raises EPB41L1's level | lines that do not express SULF2 (24) vs lines expressing it (26) | 2.08× lower at baseline in the lines without SULF2 | 0.044 | ⚠ within organs, on part of the lines; also absent: FOXQ1, HR, HNF1A-AS1 |
| [[ARHGAP27]] | B | SULF2 activity raises ARHGAP27's level | lines that do not express SULF2 (24) vs lines expressing it (26) | 1.80× lower at baseline in the lines without SULF2 | 0.046 | ⚠ within organs, on part of the lines; also absent: FOXQ1, HR, HNF1A-AS1 |
| [[PITX1]] | B | SULF2 activity raises PITX1's level | lines that do not express SULF2 (24) vs lines expressing it (26) | 1.89× lower at baseline in the lines without SULF2 | 0.046 | ⚠ within organs, on part of the lines; also absent: FOXQ1, HR, HNF1A-AS1 |
| [[ADAP1]] | B | SULF2 activity raises ADAP1's level | lines that do not express SULF2 (24) vs lines expressing it (26) | 2.04× lower at baseline in the lines without SULF2 | 0.050 | ⚠ within organs, on part of the lines; also absent: FOXQ1, HR, HNF1A-AS1 |
| [[TNFRSF14-AS1]] | B | SULF2 activity raises TNFRSF14-AS1's level | lines that do not express SULF2 (24) vs lines expressing it (26) | 1.78× lower at baseline in the lines without SULF2 | 0.058 | ⚠ within organs, on part of the lines; also absent: FOXQ1, HR, HNF1A-AS1 |
| [[KRT18]] | B | SULF2 activity raises KRT18's level | lines that do not express SULF2 (24) vs lines expressing it (26) | 2.63× lower at baseline in the lines without SULF2 | 0.061 | ⚠ within organs, on part of the lines; also absent: FOXQ1, HR, HNF1A-AS1 |
| [[EFNB1]] | B | SULF2 activity raises EFNB1's level | lines that do not express SULF2 (24) vs lines expressing it (26) | 2.24× lower at baseline in the lines without SULF2 | 0.062 | ⚠ within organs, on part of the lines; also absent: FOXQ1, HR, HNF1A-AS1 |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.652). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.5, 49.0); signed map (68.7, 7.5). **Vector** length 106, 34.8% of its response variance represented; |z| ≥ 3 in 798 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.7 | +10.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.6 | +11.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.5 | +18.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +12.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.6 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.6 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +4.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +3.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.3 | +2.6 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.9 | -5.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -3.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.2 | -0.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.2 | -3.7 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | -2.2 | -3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.0 | -4.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | sulfatase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.12 — chr20:47,656,197-47,786,616 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1247, HSULF-2, SULF-2 |
| Gene groups (HGNC) | Sulfatases |
| Hallmark sets | APICAL_SURFACE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWU5](https://www.uniprot.org/uniprotkb/Q8IWU5) (Extracellular sulfatase Sulf-2):

> Exhibits arylsulfatase activity and highly specific endoglucosamine-6-sulfatase activity. It can remove sulfate from the C-6 position of glucosamine within specific subregions of intact heparin.

**Summary**, from NCBI Gene [55959](https://www.ncbi.nlm.nih.gov/gene/55959):

> Heparan sulfate proteoglycans (HSPGs) act as coreceptors for numerous heparin-binding growth factors and cytokines and are involved in cell signaling. Heparan sulfate 6-O-endosulfatases, such as SULF2, selectively remove 6-O-sulfate groups from heparan sulfate. This activity modulates the effects of heparan sulfate by altering binding sites for signaling molecules (Dai et al., 2005 [PubMed 16192265]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:20392](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20392) · Entrez [55959](https://www.ncbi.nlm.nih.gov/gene/55959) · UniProt [Q8IWU5](https://www.uniprot.org/uniprotkb/Q8IWU5) · Ensembl [ENSG00000196562](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196562)

## Data

Gene col 12237: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12237); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12237, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12237]; `tensor/DDL_lfc|DDL_z.npy` [12237]; `embed/gene_vectors.npy` [12237]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12237 or target_col == 12237). Every well: [[SULF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SULF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
