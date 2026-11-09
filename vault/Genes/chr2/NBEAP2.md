---
symbol: "NBEAP2"
type: "gene"
col: 12488
ensembl_id: "ENSG00000197927"
name: "neurobeachin pseudogene 2"
location: "2q21.1"
module: 33
arm: "+"
pooled_cpm: 22.11
n_lines_expressing: 45
n_dd_up: 8
n_dd_down: 22
n_dd_up_clean: 5
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 2
direction_downstream: 5
tags: ["gene", "module/033"]
generated_by: "tahoemap"
---

# NBEAP2

*neurobeachin pseudogene 2* — 2q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.57× (z +7.8, q 3e-12, up in 15 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.31× (z +6.9, q 1e-09, up in 21 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.419× (z -15.7, q 0e+00, down in 32 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.475× (z -13.5, q 8e-39, down in 33 of 43 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C2orf27A]] (+0.63, fdr 7e-06, ⚠ same locus), [[DUXAP8]] (+0.58, fdr 2e-05), [[DUXAP9]] (+0.51, fdr 4e-05), [[CARNMT1]] (+0.51, fdr 3e-05); moves opposite to [[VPS18]] (-0.49, fdr 2e-04), [[WDR83]] (-0.47, fdr 8e-05), [[TRADD]] (-0.45, fdr 1e-04).
> It sits in the **+** arm of [[Module 033]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MYBL1]] → it (grade B ⚠); 5 go from it, the strongest it → [[GNL3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12488.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +7.8 | 3e-12 | 15/28 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +6.9 | 1e-09 | 21/43 (LoVo, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +6.4 | 2e-08 | 17/36 (Panc 03.27, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.30×** | +4.8 | 2e-04 | 16/43 (LoVo, NCI-H460, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | 1.18× | +4.3 | 0.002 | 13/43 (A-172, A-427, …) | rises with dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +4.1 | 0.004 | 16/42 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.23×** | +3.8 | 0.010 | 12/43 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.090 | 8/41 (C-33 A, RKO, …) | inconsistent across doses | low cells (technical?) |
| [[Bentamapimod (drug)]] 0.05 µM |  | **1.20×** | +3.2 | 0.100 | 9/42 (SW480, HT-29, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.15 | 7/42 (HOP62, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12488.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.419×** | -15.7 | 0e+00 | 32/42 (PANC-1, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.475×** | -13.5 | 8e-39 | 33/43 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.498×** | -12.6 | 5e-34 | 30/43 (H4, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.636×** | -11.6 | 9e-29 | 31/42 (NCI-H2030, PANC-1, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.571×** | -10.1 | 5e-22 | 33/43 (MIA PaCa-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.577×** | -9.9 | 3e-21 | 30/43 (C-33 A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.705×** | -8.9 | 4e-17 | 27/43 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.616×** | -8.8 | 1e-16 | 29/42 (NCI-H460, HT-29, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.639×** | -8.1 | 4e-14 | 29/43 (SW480, NCI-H23, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.474×** | -7.1 | 1e-10 | 27/43 (KATO III, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~13% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.490×** | -6.8 | 7e-10 | 26/41 (MIA PaCa-2, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.680×** | -6.7 | 1e-09 | 23/42 (PANC-1, NCI-H460, …) | top dose only | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.713×** | -5.8 | 3e-07 | 22/42 (H4, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~24% of this change | **0.735×** | -5.3 | 4e-06 | 18/41 (PANC-1, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.757×** | -5.0 | 2e-05 | 21/43 (H4, A-172, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.664×** | -3.9 | 0.003 | 15/41 (RPMI-7951, SNU-1, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.691×** | -3.5 | 0.013 | 14/43 (LOX-IMVI, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.820×** | -3.4 | 0.015 | 12/43 (PANC-1, J82, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.702×** | -3.3 | 0.020 | 13/42 (H4, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Budesonide (drug)]] 0.05 µM |  | 0.836× | -3.2 | 0.030 | 11/43 (SW 1088, LOX-IMVI, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12488. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 30.8 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -17.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.260× (z -15.4) |
| [[SW480 (line)]] | alt | 18.4 | 0 | 7 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.296× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.348× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 8.49 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -14.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.222× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 30.4 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -12.3) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0795× (z -11.0) |
| [[BT-474 (line)]] | alt | 17.9 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0495× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.156× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 30.5 | 0 | 3 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0230× (z -15.3) |
| [[NCI-H23 (line)]] | alt | 21.8 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.180× (z -11.8) |
| [[RKO (line)]] | wt | 29.3 | 0 | 3 (2 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0352× (z -11.1) |
| [[SW 900 (line)]] | alt | 32.7 | 0 | 3 (2 ⚠) | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.141× (z -14.1) |
| [[A-427 (line)]] | wt | 35.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -17.8) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A549 (line)]] | wt | 5.98 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0765× (z -11.4) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 30.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.109× (z -13.8) |
| [[HepG2_C3A (line)]] | wt | 15.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0661× (z -11.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 29.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -21.4) ⚠ cell-cycle shift, explains ~40% of this change |
| [[A-172 (line)]] | wt | 46.1 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.65× (z +8.5) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[H4 (line)]] | wt | 44.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.179× (z -10.9) |
| [[J82 (line)]] | alt | 40.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -8.5) |
| [[KATO III (line)]] | alt | 14.2 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0313× (z -11.1) |
| [[LS 180 (line)]] | wt | 5.76 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.112× (z -8.8) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 20.6 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0735× (z -8.9) |
| [[SHP-77 (line)]] | alt | 12.4 | 0 | 1 | — | [[Ipatasertib (drug)]] 0.05 µM 0.177× (z -8.6) |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -9.3) |
| [[SNU-1 (line)]] | wt | 20.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -8.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SW48 (line)]] | wt | 28.3 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.187× (z -8.8) |
| [[A498 (line)]] | wt | 40.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.03 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 17.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.51 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 36.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 5.76 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 61.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 36.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.47 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12488), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C2orf27A]] | +0.63 | +0.65 / +0.65 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[DUXAP8]] | +0.58 | +0.47 / +0.56 | both halves | 2e-05 |  |
| [[DUXAP9]] | +0.51 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[CARNMT1]] | +0.51 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[LNCOG]] | +0.50 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[MYLK]] | +0.48 | +0.40 / +0.39 | both halves | 5e-05 |  |
| [[POLE4]] ⚠ | +0.45 | +0.49 / +0.35 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[CALD1]] | +0.44 | +0.33 / +0.50 | both halves | 1e-04 |  |
| [[TRDMT1]] | +0.44 | +0.34 / +0.41 | both halves | 1e-04 |  |
| [[CLNS1A]] | +0.43 | +0.40 / +0.40 | both halves | 5e-05 |  |
| [[EVC]] | +0.43 | +0.35 / +0.43 | both halves | 1e-04 |  |
| [[IMPACT]] | +0.43 | +0.24 / +0.47 | both halves | 4e-04 |  |
| [[B3GNTL1]] | +0.43 | +0.28 / +0.42 | both halves | 3e-04 |  |
| [[TXNRD3]] | +0.42 | +0.38 / +0.44 | both halves | 6e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VPS18]] | -0.49 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[WDR83]] | -0.47 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[TRADD]] | -0.45 | -0.35 / -0.41 | both halves | 1e-04 |  |
| [[ZNF430]] | -0.43 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[SERTAD3]] | -0.43 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[TOM1]] | -0.42 | -0.36 / -0.34 | both halves | 1e-04 |  |
| [[ZBTB7B]] | -0.42 | -0.40 / -0.42 | both halves | 5e-05 |  |
| [[SMIM27]] | -0.42 | -0.25 / -0.40 | both halves | 4e-04 |  |
| [[A1BG-AS1]] | -0.41 | -0.22 / -0.33 | both halves | 6e-04 |  |
| [[NAA38]] | -0.41 | -0.35 / -0.32 | both halves | 1e-04 |  |
| [[BAHD1]] | -0.41 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[MSRB1]] | -0.41 | -0.36 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYBL1]] | B | MYBL1 activity raises NBEAP2's level | lines that do not express MYBL1 (8) vs lines expressing it (42) | 2.36× lower at baseline in the lines without MYBL1 | 0.095 | ⚠ within organs, on part of the lines; also absent: NCS1, KCNC4, JAZF1; maybe low, not absent |
| [[C2orf27A]] | C | C2orf27A activity raises NBEAP2's level | lines that do not express C2orf27A (5) vs lines expressing it (45) | 5.90× lower at baseline in the lines without C2orf27A | 0.002 | ⚠ within organs, on part of the lines; also absent: NBEAP2, UBA6-DT, ENSG00000287621; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNL3]] | B | NBEAP2 activity raises GNL3's level | lines that do not express NBEAP2 (5) vs lines expressing it (45) | 1.56× lower at baseline in the lines without NBEAP2 | 0.048 | ⚠ within organs, on part of the lines; also absent: C2orf27A, ROPN1L, ENSG00000287621 |
| [[SNHG16]] | B | NBEAP2 activity raises SNHG16's level | lines that do not express NBEAP2 (5) vs lines expressing it (45) | 1.87× lower at baseline in the lines without NBEAP2 | 0.060 | ⚠ within organs, on part of the lines; also absent: C2orf27A, ROPN1L, ENSG00000287621 |
| [[WDR36]] | B | NBEAP2 activity raises WDR36's level | lines that do not express NBEAP2 (5) vs lines expressing it (45) | 1.58× lower at baseline in the lines without NBEAP2 | 0.067 | ⚠ within organs, on part of the lines; also absent: C2orf27A, ROPN1L, ENSG00000287621 |
| [[FYCO1]] | B | NBEAP2 activity raises FYCO1's level | lines that do not express NBEAP2 (5) vs lines expressing it (45) | 1.64× lower at baseline in the lines without NBEAP2 | 0.094 | ⚠ within organs, on part of the lines; also absent: C2orf27A, ROPN1L, ENSG00000287621 |
| [[C2orf27A]] | C | NBEAP2 activity raises C2orf27A's level | lines that do not express NBEAP2 (5) vs lines expressing it (45) | 5.62× lower at baseline in the lines without NBEAP2 | 0.006 | ⚠ within organs, on part of the lines; also absent: C2orf27A, ROPN1L, ENSG00000287621; co-absent with the target |

## Where it sits

- **Module**: [[Module 033]] — MYC targets v2; 139 genes; this gene is in the **+** arm (projection on the module's main direction 0.231). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-27.0, -29.7); signed map (-17.1, -47.5). **Vector** length 69.1, 12.0% of its response variance represented; |z| ≥ 3 in 1,085 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +6.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.0 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.9 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +1.8 | -3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | -1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.6 | -0.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | +1.6 | -1.2 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.2 | -8.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.6 | -8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -3.3 | -11.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.3 | -1.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -3.1 | -1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.9 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -8.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | -1.7 | +1.0 |

## What is on record

|  |  |
|---|---|
| Name | neurobeachin pseudogene 2 |
| Locus type | pseudogene |
| Location | 2q21.1 — chr2:131,722,417-131,751,584 (+) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | BCL8D |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:40003](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:40003) · Entrez [100418881](https://www.ncbi.nlm.nih.gov/gene/100418881) · Ensembl [ENSG00000197927](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197927)

## Data

Gene col 12488: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12488); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12488, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12488]; `tensor/DDL_lfc|DDL_z.npy` [12488]; `embed/gene_vectors.npy` [12488]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12488 or target_col == 12488). Every well: [[NBEAP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NBEAP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
