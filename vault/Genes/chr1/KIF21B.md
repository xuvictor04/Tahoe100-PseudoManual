---
symbol: "KIF21B"
type: "gene"
col: 3847
ensembl_id: "ENSG00000116852"
name: "kinesin family member 21B"
location: "1q32.1"
module: 84
arm: "+"
pooled_cpm: 5.84
n_lines_expressing: 39
n_dd_up: 16
n_dd_down: 33
n_dd_up_clean: 11
n_dd_down_clean: 30
in_vector_space: true
direction_upstream: 12
direction_downstream: 10
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# KIF21B

*kinesin family member 21B* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 4.93× (z +15.8, q 0e+00, up in 33 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.371× (z -13.9, q 3e-41, down in 27 of 29 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.308× (z -11.3, q 6e-27, down in 23 of 34 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GPRIN1]] (+0.71, fdr 1e-05), [[ABTB3]] (+0.70, fdr 7e-06), [[ATP13A2]] (+0.69, fdr 2e-05); moves opposite to [[CASD1]] (-0.66, fdr 5e-05), [[CREBBP]] (-0.65, fdr 4e-05), [[BAZ2B]] (-0.64, fdr 6e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 10 go from it, the strongest it → [[MFF-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 5 with an alert ⚠; shown: the 15 strongest. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3847.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **4.93×** | +15.8 | 0e+00 | 33/35 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **4.92×** | +15.8 | 0e+00 | 34/36 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **4.86×** | +15.7 | 0e+00 | 33/35 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.50×** | +12.8 | 2e-35 | 30/36 (SW480, A498, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.50×** | +12.4 | 3e-33 | 34/36 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **2.66×** | +9.7 | 4e-20 | 25/29 (A549, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.17×** | +7.7 | 1e-12 | 20/34 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.17×** | +6.0 | 2e-07 | 16/35 (SW480, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.61×** | +4.7 | 1e-04 | 8/35 (A498, A549, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.56×** | +4.4 | 6e-04 | 13/35 (NCI-H1792, SW1417, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.50×** | +3.8 | 0.008 | 10/34 (A498, SW480, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.46×** | +3.8 | 0.008 | 12/35 (KATO III, SW480, …) | top dose only | position effect removed |
| [[Artesunate (drug)]] 5 µM |  | **1.29×** | +3.6 | 0.014 | 11/37 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.026 | 10/35 (SNU-423, A-172, …) | rises with dose | low cells (technical?) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.41×** | +3.4 | 0.026 | 9/36 (NCI-H2347, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3847.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.371×** | -13.9 | 3e-41 | 27/29 (HOP62, LS 180, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.308×** | -11.3 | 6e-27 | 23/34 (HOP62, COLO 205, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.486×** | -10.1 | 7e-22 | 21/31 (A-172, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.373×** | -9.8 | 2e-20 | 22/28 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.393×** | -9.3 | 2e-18 | 24/36 (LS 180, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.472×** | -7.2 | 8e-11 | 19/28 (A-172, J82, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.533×** | -6.2 | 3e-08 | 20/34 (KATO III, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.556×** | -5.6 | 2e-06 | 18/28 (LS 180, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.719×** | -4.6 | 2e-04 | 18/35 (A-172, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.648×** | -4.6 | 2e-04 | 16/37 (HOP62, J82, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.626×** | -4.4 | 5e-04 | 13/34 (A-172, HOP62, …) | inconsistent across doses | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.643×** | -4.4 | 5e-04 | 17/36 (HOP62, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.702×** | -4.3 | 8e-04 | 15/36 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 5 µM |  | **0.699×** | -4.1 | 0.002 | 15/37 (HOP62, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.706×** | -4.1 | 0.002 | 14/36 (HOP62, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.456×** | -4.1 | 0.002 | 14/33 (HOP62, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.40 per unit of S-phase module lfc, -0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3847. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 19.5 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0335× (z -22.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.0407× (z -14.6) |
| [[A-172 (line)]] | wt | 23.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -13.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.132× (z -13.1) |
| [[LS 180 (line)]] | wt | 21.7 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -14.5) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -12.1) |
| [[J82 (line)]] | alt | 4.70 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -10.6) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -9.6) |
| [[SW1417 (line)]] | alt | 10.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -12.1) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Menadione (drug)]] 0.05 µM 0.155× (z -8.6) |
| [[COLO 205 (line)]] | alt | 14.3 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0312× (z -13.4) |
| [[H4 (line)]] | wt | 22.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0764× (z -10.0) |
| [[KATO III (line)]] | alt | 12.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.153× (z -12.7) |
| [[LoVo (line)]] | wt | 9.85 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.115× (z -10.4) |
| [[SW480 (line)]] | alt | 5.29 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.131× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 8.99 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -8.6) |
| [[A549 (line)]] | wt | 8.80 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -8.9) ⚠ cell-cycle shift, explains ~33% of this change |
| [[AsPC-1 (line)]] | alt | 3.54 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0689× (z -10.4) ⚠ cell-cycle shift, explains ~33% of this change |
| [[Panc 03.27 (line)]] | alt | 3.98 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -8.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[A-427 (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.14 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.683 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.910 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.782 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.623 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.56 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.788 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.66 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.757 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 9.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.53 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3847), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*56 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRIN1]] | +0.71 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ABTB3]] | +0.70 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[ATP13A2]] | +0.69 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[RAC2]] | +0.68 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[RASA3]] | +0.68 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[AP3M2]] | +0.66 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[SPTLC2]] | +0.66 | +0.62 / +0.38 | both halves | 6e-05 |  |
| [[PPARD]] | +0.65 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[STX1A]] | +0.65 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[FCHO1]] | +0.65 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[LINC02970]] | +0.65 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[MICAL2]] | +0.64 | +0.64 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*44 of its nearest partners move opposite, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 4 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CASD1]] | -0.66 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[CREBBP]] | -0.65 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[BAZ2B]] | -0.64 | -0.59 / -0.38 | both halves | 6e-05 |  |
| [[GTF2IRD2B]] | -0.64 | -0.59 / -0.36 | both halves | 1e-04 |  |
| [[ERCC6L2-AS1]] | -0.64 | -0.62 / -0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[MFF-DT]] | -0.64 | -0.59 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[TMEM202-AS1]] | -0.63 | -0.63 / -0.11 | ⚠ one half (not replicated) | 0.002 |  |
| [[PLS3-AS1]] | -0.63 | -0.59 / -0.33 | both halves | 1e-04 |  |
| [[DNAI4]] | -0.63 | -0.58 / -0.30 | both halves | 2e-04 | same gene group |
| [[EFCAB2]] | -0.63 | -0.54 / -0.27 | both halves | 3e-04 |  |
| [[PBLD]] | -0.62 | -0.56 / -0.19 | ⚠ one half (not replicated) | 9e-04 |  |
| [[ZFX]] | -0.62 | -0.54 / -0.33 | both halves | 1e-04 |  |
| [[RNF115]] | -0.61 | -0.62 / -0.34 | both halves | 1e-04 |  |
| [[RBKS]] | -0.61 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[TMEM35B]] | -0.61 | -0.54 / -0.37 | both halves | 8e-05 |  |
| [[AHI1-DT]] | -0.61 | -0.54 / -0.22 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises KIF21B's level | compounds that target TOP2A: 5 of 5 lower it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 5.9% of all compounds | 0.007 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[TMEM92]] | B | TMEM92 activity raises KIF21B's level | lines that do not express TMEM92 (22) vs lines expressing it (28) | 2.28× lower at baseline in the lines without TMEM92 | 0.013 | ⚠ within organs, on part of the lines; also absent: ARL14, LINC01589, TNFSF10 |
| [[CACNA2D4]] | B | CACNA2D4 activity raises KIF21B's level | lines that do not express CACNA2D4 (22) vs lines expressing it (28) | 1.81× lower at baseline in the lines without CACNA2D4 | 0.018 | ⚠ within organs, on part of the lines; also absent: ARHGDIB, NRP2, RFX8; maybe low, not absent |
| [[CARD11]] | B | CARD11 activity raises KIF21B's level | lines that do not express CARD11 (33) vs lines expressing it (17) | 1.81× lower at baseline in the lines without CARD11 | 0.020 | ⚠ within organs, on part of the lines; also absent: TNFSF14, KRT81, C3 |
| [[TMCC3]] | B | TMCC3 activity raises KIF21B's level | lines that do not express TMCC3 (19) vs lines expressing it (31) | 1.82× lower at baseline in the lines without TMCC3 | 0.029 | ⚠ within organs, on part of the lines; also absent: PTPRB, KRT7, ADGRF4 |
| [[PAEP]] | B | PAEP activity raises KIF21B's level | lines that do not express PAEP (33) vs lines expressing it (17) | 1.58× lower at baseline in the lines without PAEP | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GREM2, UNC5D |
| [[TINAGL1]] | B | TINAGL1 activity raises KIF21B's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 1.92× lower at baseline in the lines without TINAGL1 | 0.042 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[PLCG2]] | B | PLCG2 activity weakens KIF21B's drug response | lines that do not express PLCG2 (7) vs lines expressing it (30) | the lines without PLCG2 respond 0.96× as strongly (z diff -0.16); strongest at Panobinostat 0.5 µM: 7.31x vs 3.76x (z diff -1.9) | 0.044 | ⚠ within organs, on part of the lines; also absent: CRACD; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[SGSM1]] | B | SGSM1 activity raises KIF21B's level | lines that do not express SGSM1 (6) vs lines expressing it (44) | 1.91× lower at baseline in the lines without SGSM1 | 0.083 | ⚠ within organs, on part of the lines; also absent: DANT2, KCNIP3, PIK3C2B; maybe low, not absent |
| [[MTUS1-DT]] | B | MTUS1-DT activity raises KIF21B's level | lines that do not express MTUS1-DT (17) vs lines expressing it (33) | 1.81× lower at baseline in the lines without MTUS1-DT | 0.088 | ⚠ within organs, on part of the lines; co-absent genes; also absent: MTUS1, ELF3-AS1, ELF3 |
| [[ARHGEF4]] | B | ARHGEF4 activity raises KIF21B's level | lines that do not express ARHGEF4 (15) vs lines expressing it (35) | 1.31× lower at baseline in the lines without ARHGEF4 | 0.090 | ⚠ within organs, on part of the lines; also absent: GALNT12, RBM47, NR2E3 |
| [[PLEK2]] | B | PLEK2 activity raises KIF21B's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 1.29× lower at baseline in the lines without PLEK2 | 0.098 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MFF-DT]] | B | KIF21B activity lowers MFF-DT's level | lines that do not express KIF21B (11) vs lines expressing it (39) | 1.47× higher at baseline in the lines without KIF21B | 0.006 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SPTLC2]] | B | KIF21B activity raises SPTLC2's level | lines that do not express KIF21B (11) vs lines expressing it (39) | 1.33× lower at baseline in the lines without KIF21B | 0.046 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[DNAI4]] | B | KIF21B activity lowers DNAI4's level | lines that do not express KIF21B (11) vs lines expressing it (39) | 1.44× higher at baseline in the lines without KIF21B | 0.050 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PCNX4-DT]] | B | KIF21B activity lowers PCNX4-DT's level | lines that do not express KIF21B (11) vs lines expressing it (39) | 1.23× higher at baseline in the lines without KIF21B | 0.050 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MTUS1-DT]] | B | KIF21B activity raises MTUS1-DT's level | lines that do not express KIF21B (11) vs lines expressing it (39) | 2.31× lower at baseline in the lines without KIF21B | 0.059 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SLC46A3]] | B | KIF21B activity lowers SLC46A3's level | lines that do not express KIF21B (11) vs lines expressing it (39) | 1.29× higher at baseline in the lines without KIF21B | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HPCAL1]] | B | KIF21B activity raises HPCAL1's level | lines that do not express KIF21B (11) vs lines expressing it (39) | 1.58× lower at baseline in the lines without KIF21B | 0.092 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[TMEM92]] | B | KIF21B activity raises TMEM92's level | lines that do not express KIF21B (11) vs lines expressing it (39) | 2.05× lower at baseline in the lines without KIF21B | 0.094 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[LINC02693]] | B | KIF21B activity lowers LINC02693's level | lines that do not express KIF21B (11) vs lines expressing it (39) | 1.53× higher at baseline in the lines without KIF21B | 0.096 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[STAP2]] | B | KIF21B activity raises STAP2's level | lines that do not express KIF21B (11) vs lines expressing it (39) | 2.22× lower at baseline in the lines without KIF21B | 0.0996 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.680). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.7, 3.5); signed map (1.3, 48.7). **Vector** length 103, 25.0% of its response variance represented; |z| ≥ 3 in 1,134 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +12.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.8 | +15.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +5.6 | +15.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.5 | +15.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.2 | +12.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.6 | +6.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.5 | +3.8 |
|  | [[Neratinib (drug)]] 5 µM |  | +1.6 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.8 | -9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -5.2 | -13.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.9 | -11.3 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.4 | -4.1 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.4 | -4.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.4 | -4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.3 | -3.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.9 | -4.6 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -3.7 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 21B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:200,969,390-201,023,714 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434J212, KIAA0449 |
| Gene groups (HGNC) | WD repeat domain containing; Kinesins |
| Reactome | 8 pathways, smallest: Kinesins; COPI-dependent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [O75037](https://www.uniprot.org/uniprotkb/O75037) (Kinesin-like protein KIF21B):

> Plus-end directed microtubule-dependent motor protein which displays processive activity. Is involved in regulation of microtubule dynamics, synapse function and neuronal morphology, including dendritic tree branching and spine formation. Plays a role in lerning and memory. Involved in delivery of gamma-aminobutyric acid (GABA(A)) receptor to cell surface.

**Summary**, from NCBI Gene [23046](https://www.ncbi.nlm.nih.gov/gene/23046):

> This gene encodes a member of the kinesin superfamily. Kinesins are ATP-dependent microtubule-based motor proteins that are involved in the intracellular transport of membranous organelles. Single nucleotide polymorphisms in this gene are associated with inflammatory bowel disease and multiple sclerosis. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Nov 2011]

**Accessions** — [HGNC:29442](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29442) · Entrez [23046](https://www.ncbi.nlm.nih.gov/gene/23046) · UniProt [O75037](https://www.uniprot.org/uniprotkb/O75037) · Ensembl [ENSG00000116852](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000116852)

## Data

Gene col 3847: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3847); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3847, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3847]; `tensor/DDL_lfc|DDL_z.npy` [3847]; `embed/gene_vectors.npy` [3847]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3847 or target_col == 3847). Every well: [[KIF21B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF21B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
