---
symbol: "KCNQ1OT1"
type: "gene"
col: 15637
ensembl_id: "ENSG00000269821"
name: "KCNQ1 opposite strand/antisense transcript 1"
location: "11p15.5"
module: 56
arm: "+"
pooled_cpm: 248.64
n_lines_expressing: 44
n_dd_up: 7
n_dd_down: 27
n_dd_up_clean: 7
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# KCNQ1OT1

*KCNQ1 opposite strand/antisense transcript 1* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.73× (z +11.9, q 4e-30, up in 27 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.433× (z -12.9, q 1e-35, down in 41 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KDELR2]] (+0.75, fdr 7e-06), [[ARF4]] (+0.74, fdr 7e-06), [[SLC35A2]] (+0.72, fdr 7e-06); moves opposite to [[PAIP1]] (-0.59, fdr 1e-05), [[TADA2A]] (-0.58, fdr 1e-05), [[USP24]] (-0.58, fdr 2e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 1 goes from it, the strongest it → [[COL20A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15637.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +11.9 | 4e-30 | 27/42 (C32, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **2.13×** | +11.6 | 7e-29 | 39/42 (LOX-IMVI, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.86×** | +9.6 | 2e-19 | 33/42 (SK-MEL-2, HEC-1-A, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM |  | **1.73×** | +8.5 | 4e-15 | 34/42 (SK-MEL-2, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.71×** | +8.3 | 1e-14 | 37/42 (LOX-IMVI, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +5.3 | 1e-05 | 31/42 (SNU-423, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +4.1 | 0.003 | 22/42 (SW480, SW1417, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15637.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.433×** | -12.9 | 1e-35 | 41/42 (A549, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.469×** | -11.7 | 3e-29 | 35/43 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.474×** | -11.1 | 2e-26 | 30/38 (SHP-77, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.535×** | -8.9 | 5e-17 | 33/39 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.584×** | -8.3 | 1e-14 | 35/42 (A549, H4, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.611×** | -7.3 | 2e-11 | 26/42 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **0.635×** | -7.0 | 2e-10 | 32/42 (HepG2/C3A, SNU-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.452×** | -6.4 | 1e-08 | 30/43 (H4, A-172, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **0.668×** | -6.2 | 3e-08 | 32/42 (HT-29, BT-474, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.667×** | -6.0 | 1e-07 | 30/41 (HepG2/C3A, H4, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.691×** | -5.7 | 6e-07 | 29/42 (H4, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.694×** | -5.7 | 8e-07 | 29/42 (A549, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.707×** | -5.1 | 1e-05 | 28/42 (NCI-H1792, A549, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.729×** | -4.9 | 4e-05 | 26/42 (H4, BT-474, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.733×** | -4.8 | 6e-05 | 27/42 (COLO 205, HOP62, …) | two highest doses | cell-cycle shift (explains ~3% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.810×** | -4.6 | 2e-04 | 25/42 (AsPC-1, LS 180, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.826×** | -4.2 | 0.001 | 18/42 (NCI-H1792, H4, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.770×** | -3.7 | 0.006 | 26/41 (A549, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.792×** | -3.6 | 0.008 | 24/42 (LS 180, KATO III, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.661×** | -3.3 | 0.021 | 25/43 (SNU-423, NCI-H1792, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.815×** | -3.2 | 0.039 | 21/42 (BT-474, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15637. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 820 | 0 | 12 (6 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.164× (z -16.6) |
| [[SNU-423 (line)]] | alt | 328 | 5 | 6 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 3.21× (z +12.9) | [[Dinaciclib (drug)]] 0.5 µM 0.336× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.369× (z -11.1) |
| [[A-172 (line)]] | wt | 374 | 2 | 8 (5 ⚠) | [[Panobinostat (drug)]] 5 µM 2.62× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.282× (z -13.3) |
| [[SW480 (line)]] | alt | 590 | 5 | 5 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 2.79× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.266× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.324× (z -13.5) |
| [[A549 (line)]] | wt | 221 | 0 | 9 (4 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.109× (z -22.3) |
| [[BT-474 (line)]] | alt | 372 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -12.3) |
| [[HOP62 (line)]] | alt | 261 | 2 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +19.1) | [[Harringtonine (drug)]] 0.5 µM 0.233× (z -15.1) |
| [[NCI-H1792 (line)]] | alt | 455 | 1 | 7 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.65× (z +17.0) | [[Digitoxin (drug)]] 5 µM 0.320× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.333× (z -10.2) |
| [[PANC-1 (line)]] | alt | 194 | 3 | 5 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.89× (z +12.1) | [[Harringtonine (drug)]] 0.5 µM 0.343× (z -12.2) |
| [[A-427 (line)]] | wt | 128 | 3 | 4 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.65× (z +10.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.366× (z -11.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.373× (z -10.6) |
| [[J82 (line)]] | alt | 221 | 4 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.89× (z +21.3) | [[Dinaciclib (drug)]] 5 µM 0.375× (z -10.5) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 198 | 3 (1 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +12.7) | [[Harringtonine (drug)]] 0.5 µM 0.430× (z -9.0) |
| [[Hs 766T (line)]] | wt | 218 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +14.0) | [[Harringtonine (drug)]] 5 µM 0.396× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 125 | 5 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.72× (z +23.8) | [[Lonafarnib (drug)]] 5 µM 0.189× (z -9.4) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 525 | 0 | 5 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.217× (z -12.1) ⚠ toxic · without an alert: [[Ponatinib (drug)]] 5 µM 0.257× (z -11.2) |
| [[HT-29 (line)]] | alt | 612 | 1 | 4 (4 ⚠) | [[Auranofin (drug)]] 5 µM 2.51× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.270× (z -12.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 235 | 3 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +16.5) | [[Harringtonine (drug)]] 0.05 µM 0.334× (z -9.9) |
| [[SHP-77 (line)]] | alt | 191 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.98× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.237× (z -15.7) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 128 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 3.71× (z +13.1) | [[Harringtonine (drug)]] 0.5 µM 0.411× (z -8.9) |
| [[HCT15 (line)]] | alt | 430 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.256× (z -12.2) |
| [[hTERT-HPNE (line)]] | wt | 302 | 1 | 3 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +16.4) | [[Harringtonine (drug)]] 0.5 µM 0.232× (z -12.9) |
| [[LOX-IMVI (line)]] | wt | 108 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.27× (z +25.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 139 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +13.0) | — |
| [[RPMI-7951 (line)]] | alt | 304 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +13.9) | [[Harringtonine (drug)]] 0.5 µM 0.313× (z -10.8) |
| [[A498 (line)]] | wt | 453 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.269× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.378× (z -9.6) |
| [[C32 (line)]] | wt | 140 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.9× (z +29.7) | — |
| [[CHP-212 (line)]] | wt | 300 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -10.9) |
| [[KATO III (line)]] | alt | 204 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.327× (z -10.7) |
| [[LoVo (line)]] | wt | 261 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +14.7) | [[Harringtonine (drug)]] 0.5 µM 0.326× (z -10.1) |
| [[SW1417 (line)]] | alt | 223 | 3 | 0 | [[Auranofin (drug)]] 5 µM 2.08× (z +9.3) | — |
| [[CFPAC-1 (line)]] | alt | 273 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +11.2) | [[Dinaciclib (drug)]] 0.05 µM 0.432× (z -8.7) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 210 | 2 | 0 | [[Auranofin (drug)]] 5 µM 2.87× (z +14.1) | — |
| [[HS-578T (line)]] | alt | 396 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 2.82× (z +10.2) | [[Homoharringtonine (drug)]] 0.05 µM 0.407× (z -8.9) |
| [[LS 180 (line)]] | wt | 136 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.255× (z -11.5) |
| [[NCI-H2347 (line)]] | alt | 117 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.15× (z +9.9) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 168 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +12.2) | — |
| [[COLO 205 (line)]] | alt | 164 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.77× (z +16.0) | — |
| [[RKO (line)]] | wt | 133 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.99× (z +8.8) | — |
| [[SW 1271 (line)]] | alt | 237 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +9.0) | — |
| [[SW48 (line)]] | wt | 210 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.48× (z +12.0) | — |
| [[C-33 A (line)]] | alt | 139 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 21.3 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 21.2 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 242 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 285 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.7 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 19.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 296 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 29.2 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15637), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDELR2]] | +0.75 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[ARF4]] | +0.74 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[SLC35A2]] | +0.72 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[FAM114A1]] | +0.70 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[SEC31A]] | +0.68 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[TINCR]] | +0.68 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[PGM3]] | +0.68 | +0.58 / +0.75 | both halves | 7e-06 |  |
| [[POFUT2]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[TMEM263]] | +0.67 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[PDXDC1]] | +0.67 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[COPE]] | +0.66 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[MORF4L2]] | +0.65 | +0.62 / +0.69 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAIP1]] | -0.59 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[TADA2A]] | -0.58 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[USP24]] | -0.58 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[TGFBRAP1]] | -0.58 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[RNASEH2B]] | -0.58 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[FAIM]] | -0.56 | -0.46 / -0.52 | both halves | 3e-05 |  |
| [[KLHL42]] | -0.55 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[MTPAP]] | -0.55 | -0.43 / -0.60 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers KCNQ1OT1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers KCNQ1OT1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL20A1]] | B | KCNQ1OT1 activity lowers COL20A1's level | lines that do not express KCNQ1OT1 (6) vs lines expressing it (44) | 1.47× higher at baseline in the lines without KCNQ1OT1 | 0.079 | ⚠ within organs, on part of the lines |

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.710). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (10.9, -36.3); signed map (-51.0, 14.2). **Vector** length 143, 50.6% of its response variance represented; |z| ≥ 3 in 1,389 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.55 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.56 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.56 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +9.6 | +9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.6 | +11.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +4.0 | +2.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.7 | +11.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.4 | +8.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.0 | +2.9 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +3.0 | +1.6 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.8 | +1.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -8.8 | -12.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -8.0 | -7.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -7.8 | -8.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.5 | -4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -6.5 | -5.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.9 | -4.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -4.7 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | KCNQ1 opposite strand/antisense transcript 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 11p15.5 — chr11:2,597,308-2,700,003 (-) |
| Ensembl biotype | lncRNA |
| Also known as | KvDMR1, KCNQ1-AS2, KvLQT1-AS, LIT1, NCRNA00012 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [10984](https://www.ncbi.nlm.nih.gov/gene/10984):

> Human chromosomal region 11p15.5 contains two clusters of epigenetically-regulated genes that are expressed from only one chromosome in a parent-of-origin manner. Each cluster, or imprinted domain, is regulated by a functionally independent imprinting control region (ICR). The human CDKN1C/KCNQ1OT1 domain is regulated by an ICR located in an intron of KCNQ1, and contains at least eight genes that are expressed exclusively or preferentially from the maternally-inherited allele. The DNA of the …

**Accessions** — [HGNC:6295](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6295) · Entrez [10984](https://www.ncbi.nlm.nih.gov/gene/10984) · Ensembl [ENSG00000269821](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000269821)

## Data

Gene col 15637: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15637); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15637, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15637]; `tensor/DDL_lfc|DDL_z.npy` [15637]; `embed/gene_vectors.npy` [15637]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15637 or target_col == 15637). Every well: [[KCNQ1OT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNQ1OT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
