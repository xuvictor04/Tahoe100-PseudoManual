---
symbol: "ARHGEF4"
type: "gene"
col: 5797
ensembl_id: "ENSG00000136002"
name: "Rho guanine nucleotide exchange factor 4"
location: "2q21.1"
module: 34
arm: "+"
pooled_cpm: 28.83
n_lines_expressing: 35
n_dd_up: 22
n_dd_down: 50
n_dd_up_clean: 20
n_dd_down_clean: 43
in_vector_space: true
direction_upstream: 7
direction_downstream: 7
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# ARHGEF4

*Rho guanine nucleotide exchange factor 4* — 2q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.27× (z +18.4, q 0e+00, up in 26 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 50 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.647× (z -9.5, q 1e-18, down in 20 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAQR5]] (+0.68, fdr 7e-06), [[WNT7B]] (+0.66, fdr 7e-06), [[LAMC2]] (+0.64, fdr 1e-05); moves opposite to [[WBP11]] (-0.58, fdr 1e-05), [[MGC32805]] (-0.55, fdr 3e-05), [[COBLL1]] (-0.53, fdr 3e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[MEGF6]] → it (grade B ⚠); 7 go from it, the strongest it → [[CDCP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5797.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.27×** | +18.4 | 0e+00 | 26/33 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.96×** | +16.9 | 0e+00 | 26/33 (HEC-1-A, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.05×** | +15.7 | 0e+00 | 28/33 (HOP62, BT-474, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **2.46×** | +14.0 | 3e-42 | 25/33 (AsPC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.82×** | +9.3 | 1e-18 | 25/33 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.67×** | +8.0 | 1e-13 | 24/34 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.61×** | +7.4 | 1e-11 | 18/34 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.54×** | +6.8 | 1e-09 | 20/33 (SW480, HEC-1-A, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.48×** | +5.9 | 2e-07 | 18/33 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.37×** | +4.9 | 6e-05 | 14/33 (SW48, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.75×** | +4.6 | 3e-04 | 13/32 (SW480, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +4.4 | 5e-04 | 15/32 (SW480, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +4.3 | 9e-04 | 11/33 (Hs 766T, NCI-H23, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.05 µM |  | **1.31×** | +3.9 | 0.003 | 12/33 (A-172, SW480, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.60×** | +3.8 | 0.005 | 9/28 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Dabrafenib (drug)]] 5 µM |  | **1.60×** | +3.8 | 0.005 | 12/34 (SW480, CFPAC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.18× | +3.6 | 0.010 | 8/33 (Hs 766T, NCI-H460, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 57 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 50 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5797.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.647×** | -9.5 | 1e-18 | 20/33 (SW480, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.539×** | -8.9 | 2e-16 | 19/27 (A-172, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.343×** | -8.7 | 8e-16 | 21/34 (NCI-H460, A-427, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.615×** | -7.5 | 8e-12 | 20/29 (NCI-H1573, A549, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.648×** | -6.7 | 2e-09 | 19/34 (AsPC-1, HOP62, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.696×** | -6.6 | 4e-09 | 22/33 (SW 900, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.701×** | -6.3 | 2e-08 | 20/34 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.688×** | -6.3 | 2e-08 | 18/34 (AsPC-1, HOP62, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.467×** | -6.2 | 4e-08 | 18/31 (NCI-H460, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.717×** | -6.2 | 4e-08 | 18/33 (AsPC-1, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.670×** | -5.9 | 2e-07 | 16/33 (A549, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.693×** | -5.4 | 2e-06 | 19/33 (HOP62, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.685×** | -5.4 | 3e-06 | 17/33 (A549, RPMI-7951, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.788×** | -5.1 | 1e-05 | 18/34 (AsPC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.541×** | -5.0 | 2e-05 | 14/30 (Hs 766T, A549, …) | top dose only | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.555×** | -4.8 | 6e-05 | 16/32 (NCI-H460, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.739×** | -4.5 | 2e-04 | 15/32 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5797. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 57.2 | 5 (2 ⚠) | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 5.22× (z +12.7) | [[Dinaciclib (drug)]] 5 µM 0.180× (z -12.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -10.0) |
| [[AsPC-1 (line)]] | alt | 29.2 | 4 (1 ⚠) | 3 | [[Panobinostat (drug)]] 5 µM 5.39× (z +10.1) | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.210× (z -9.3) |
| [[HEC-1-A (line)]] | alt | 70.6 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.35× (z +12.3) ⚠ cell-cycle shift, explains ~60% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 3.23× (z +12.0) | — |
| [[HOP62 (line)]] | alt | 20.0 | 2 | 4 | [[Tucidinostat (drug)]] 5 µM 3.50× (z +11.5) | [[Trametinib (drug)]] 5 µM 0.264× (z -9.4) |
| [[SW1417 (line)]] | alt | 37.6 | 4 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.68× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.405× (z -10.0) |
| [[A-427 (line)]] | wt | 49.2 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.207× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[PH-797804 (drug)]] 5 µM 0.128× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 70.7 | 1 | 4 (3 ⚠) | [[Pitavastatin (Calcium) (drug)]] 5 µM 2.93× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.0390× (z -26.8) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.101× (z -10.3) |
| [[LoVo (line)]] | wt | 31.0 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.226× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.452× (z -9.1) |
| [[RPMI-7951 (line)]] | alt | 33.3 | 2 | 2 | [[Panobinostat (drug)]] 5 µM 4.71× (z +8.6) | [[Cobimetinib (drug)]] 5 µM 0.0568× (z -15.2) |
| [[A-172 (line)]] | wt | 43.1 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0579× (z -21.2) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 15.1 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.94× (z +11.0) | [[Homoharringtonine (drug)]] 0.5 µM 0.177× (z -11.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW 900 (line)]] | alt | 39.0 | 1 | 2 | [[Tucidinostat (drug)]] 5 µM 2.91× (z +9.4) | [[Trametinib (drug)]] 0.5 µM 0.296× (z -9.8) |
| [[A549 (line)]] | wt | 37.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.182× (z -9.8) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 10.8 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 6.41× (z +10.4) | — |
| [[CFPAC-1 (line)]] | alt | 32.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.60× (z +9.7) | — |
| [[COLO 205 (line)]] | alt | 8.45 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 21.4× (z +9.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LS 180 (line)]] | wt | 64.4 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.10× (z +11.4) | — |
| [[NCI-H1573 (line)]] | alt | 94.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.123× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 19.7 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.225× (z -8.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.356× (z -8.5) |
| [[SNU-423 (line)]] | alt | 25.1 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -9.9) |
| [[SW48 (line)]] | wt | 82.6 | 1 | 1 | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 4.13× (z +9.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.336× (z -9.9) |
| [[AN3 CA (line)]] | alt | 33.6 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0988× (z -8.8) ⚠ cell-cycle shift, explains ~1% of this change |
| [[CHP-212 (line)]] | wt | 23.3 | 0 | 1 | — | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM 0.0632× (z -8.5) |
| [[HCT15 (line)]] | alt | 15.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 9.66× (z +8.8) | — |
| [[Hs 766T (line)]] | wt | 41.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.226× (z -9.3) ⚠ transcription drop; cell-cycle shift, explains ~37% of this change |
| [[NCI-H1792 (line)]] | alt | 8.08 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 9.12× (z +8.6) | — |
| [[NCI-H661 (line)]] | alt | 84.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0697× (z -8.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 39.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.164× (z -10.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.77 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.81 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.54 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.64 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.41 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.60 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 67.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.90 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.76 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.16 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.03 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.56 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 22.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5797), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAQR5]] | +0.68 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[WNT7B]] | +0.66 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[LAMC2]] | +0.64 | +0.54 / +0.60 | both halves | 1e-05 | pathway: Cell junction organization |
| [[TOR4A]] | +0.62 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[PLEK2]] | +0.62 | +0.53 / +0.56 | both halves | 1e-05 | same gene group |
| [[WSCD1]] | +0.60 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[CALB2]] | +0.60 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[CLIP2]] | +0.60 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[LINC01589]] | +0.59 | +0.48 / +0.55 | both halves | 2e-05 |  |
| [[AGPAT4]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[ITGA2]] | +0.58 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[PLEKHG5]] | +0.58 | +0.52 / +0.48 | both halves | 2e-05 | same gene group; pathway: Cell death signalling via NRAGE, NRIF and NADE |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WBP11]] | -0.58 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[MGC32805]] | -0.55 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[COBLL1]] | -0.53 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[RAF1]] | -0.53 | -0.42 / -0.51 | both halves | 4e-05 |  |
| [[GANC]] | -0.52 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[RPRD1B]] | -0.50 | -0.38 / -0.43 | both halves | 6e-05 |  |
| [[RBKS]] | -0.48 | -0.37 / -0.43 | both halves | 7e-05 |  |
| [[MTCP1]] | -0.48 | -0.31 / -0.38 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEGF6]] | B | MEGF6 activity raises ARHGEF4's level | lines that do not express MEGF6 (11) vs lines expressing it (39) | 2.88× lower at baseline in the lines without MEGF6 | 0.007 | ⚠ within organs, on part of the lines; also absent: SQOR; maybe low, not absent |
| [[CELSR1]] | B | CELSR1 activity raises ARHGEF4's level | lines that do not express CELSR1 (7) vs lines expressing it (43) | 3.17× lower at baseline in the lines without CELSR1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC2, PORCN, WNT9A |
| [[LAMC2]] | B | LAMC2 activity raises ARHGEF4's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 2.44× lower at baseline in the lines without LAMC2 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[MAP2K1]] | B | MAP2K1 activity raises ARHGEF4's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 8.7% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds |
| [[PLCG2]] | B | PLCG2 activity raises ARHGEF4's level | lines that do not express PLCG2 (10) vs lines expressing it (40) | 2.12× lower at baseline in the lines without PLCG2 | 0.088 | ⚠ within organs, on part of the lines; also absent: CRACD; maybe low, not absent |
| [[PLEK2]] | B | PLEK2 activity strengthens ARHGEF4's drug response | lines that do not express PLEK2 (10) vs lines expressing it (24) | the lines without PLEK2 respond 0.72× as strongly (z diff +0.88); strongest at Panobinostat 5 µM: 1.81x vs 3.61x (z diff +2.9) | 0.090 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5; target measured in part of the lines; both ways; artifact flags |
| [[NR2E3]] | C | NR2E3 activity raises ARHGEF4's level | lines that do not express NR2E3 (23) vs lines expressing it (27) | 2.96× lower at baseline in the lines without NR2E3 | 0.016 | ⚠ within organs, on part of the lines; also absent: THSD4, SLC35F3, MPV17L; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDCP1]] | B | ARHGEF4 activity raises CDCP1's level | lines that do not express ARHGEF4 (15) vs lines expressing it (35) | 3.90× lower at baseline in the lines without ARHGEF4 | 0.009 | ⚠ within organs, on part of the lines; also absent: GALNT12, RBM47, NR2E3 |
| [[CELSR1]] | B | ARHGEF4 activity raises CELSR1's level | lines that do not express ARHGEF4 (15) vs lines expressing it (35) | 2.56× lower at baseline in the lines without ARHGEF4 | 0.012 | ⚠ within organs, on part of the lines; also absent: GALNT12, RBM47, NR2E3 |
| [[PLCG2]] | B | ARHGEF4 activity raises PLCG2's level | lines that do not express ARHGEF4 (15) vs lines expressing it (35) | 2.39× lower at baseline in the lines without ARHGEF4 | 0.015 | ⚠ within organs, on part of the lines; also absent: GALNT12, RBM47, NR2E3 |
| [[KIAA1671]] | B | ARHGEF4 activity raises KIAA1671's level | lines that do not express ARHGEF4 (15) vs lines expressing it (35) | 1.91× lower at baseline in the lines without ARHGEF4 | 0.066 | ⚠ within organs, on part of the lines; also absent: GALNT12, RBM47, NR2E3 |
| [[LAMC2]] | B | ARHGEF4 activity raises LAMC2's level | lines that do not express ARHGEF4 (15) vs lines expressing it (35) | 2.92× lower at baseline in the lines without ARHGEF4 | 0.084 | ⚠ within organs, on part of the lines; also absent: GALNT12, RBM47, NR2E3 |
| [[KIF21B]] | B | ARHGEF4 activity raises KIF21B's level | lines that do not express ARHGEF4 (15) vs lines expressing it (35) | 1.31× lower at baseline in the lines without ARHGEF4 | 0.090 | ⚠ within organs, on part of the lines; also absent: GALNT12, RBM47, NR2E3 |
| [[MAMLD1]] | B | ARHGEF4 activity raises MAMLD1's level | lines that do not express ARHGEF4 (15) vs lines expressing it (35) | 1.79× lower at baseline in the lines without ARHGEF4 | 0.094 | ⚠ within organs, on part of the lines; also absent: GALNT12, RBM47, NR2E3 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.670). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (43.4, 0.4); signed map (1.3, 45.7). **Vector** length 119, 31.6% of its response variance represented; |z| ≥ 3 in 1,368 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.8 | +15.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +7.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +6.8 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.7 | +9.3 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.5 | +16.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.3 | +4.6 |
|  | [[Rapamycin (drug)]] 5 µM |  | +2.9 | +3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.6 | +1.0 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -5.6 | -8.7 |
|  | [[Trametinib (drug)]] 5 µM |  | -5.5 | -6.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.9 | -6.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.7 | -5.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -4.6 | -6.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.5 | -6.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.4 | -6.7 |

## What is on record

|  |  |
|---|---|
| Name | Rho guanine nucleotide exchange factor 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q21.1 — chr2:130,836,914-131,047,263 (+) |
| Ensembl biotype | protein_coding |
| Also known as | STM6, KIAA1112, ASEF, ASEF1 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs; SH3 domain containing |
| Reactome | 19 pathways, smallest: SRC activates STAT3 in a quantitative manner, through Cadherin-11 (CDH11), RAC1 and gp130 (IL6ST); NRAGE signals death through JNK; G alpha (12/13) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NR80](https://www.uniprot.org/uniprotkb/Q9NR80) (Rho guanine nucleotide exchange factor 4):

> Acts as a guanine nucleotide exchange factor (GEF) for RHOA, RAC1 and CDC42 GTPases. Binding of APC may activate RAC1 GEF activity. The APC-ARHGEF4 complex seems to be involved in cell migration as well as in E-cadherin-mediated cell-cell adhesion. Required for MMP9 up-regulation via the JNK signaling pathway in colorectal tumor cells. Involved in tumor angiogenesis and may play a role in intestinal adenoma formation and tumor progression.

**Summary**, from NCBI Gene [50649](https://www.ncbi.nlm.nih.gov/gene/50649):

> Rho GTPases play a fundamental role in numerous cellular processes that are initiated by extracellular stimuli that work through G protein coupled receptors. The protein encoded by this gene may form complex with G proteins and stimulate Rho-dependent signals. Multiple alternatively spliced transcript variants encoding different isoforms have been found, but the full-length nature of some variants has not been determined. [provided by RefSeq, Jun 2013]

**Accessions** — [HGNC:684](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:684) · Entrez [50649](https://www.ncbi.nlm.nih.gov/gene/50649) · UniProt [Q9NR80](https://www.uniprot.org/uniprotkb/Q9NR80) · Ensembl [ENSG00000136002](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136002)

## Data

Gene col 5797: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5797); `tables/drug_effects.parquet` (83 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5797, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5797]; `tensor/DDL_lfc|DDL_z.npy` [5797]; `embed/gene_vectors.npy` [5797]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5797 or target_col == 5797). Every well: [[ARHGEF4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
