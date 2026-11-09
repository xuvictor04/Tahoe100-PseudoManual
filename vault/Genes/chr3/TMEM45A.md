---
symbol: "TMEM45A"
type: "gene"
col: 11189
ensembl_id: "ENSG00000181458"
name: "transmembrane protein 45A"
location: "3q12.2"
module: 103
arm: "+"
pooled_cpm: 29.08
n_lines_expressing: 37
n_dd_up: 29
n_dd_down: 36
n_dd_up_clean: 27
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 28
direction_downstream: 4
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# TMEM45A

*transmembrane protein 45A* — 3q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (2 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.47× (z +4.6, q 0.002, up in 21 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 36 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.296× (z -21.6, q 0e+00, down in 34 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NREP]] (+0.66, fdr 7e-06), [[PTPRD]] (+0.64, fdr 1e-05), [[LINC03047]] (+0.61, fdr 7e-06); moves opposite to [[CALML4]] (-0.50, fdr 8e-05), [[ARMC9]] (-0.47, fdr 5e-05), [[APPL2]] (-0.46, fdr 1e-04).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[AEBP1]] → it (grade B ⚠); 4 go from it, the strongest it → [[ABL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 2 with an alert ⚠; shown: the 15 strongest. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11189.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +4.6 | 0.002 | 21/34 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.41×** | +4.3 | 0.004 | 18/34 (NCI-H23, SNU-423, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.28×** | +4.2 | 0.005 | 13/35 (SW480, HOP62, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **1.86×** | +4.1 | 0.007 | 15/34 (H4, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.008 | 20/35 (NCI-H1792, RPMI-7951, …) | top dose only |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.36×** | +3.8 | 0.010 | 19/35 (RPMI-7951, NCI-H1792, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.010 | 14/35 (HOP62, J82, …) | all doses, stronger at high dose |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +3.8 | 0.010 | 18/35 (HS-578T, SW 900, …) | top dose only |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.012 | 16/35 (RKO, HS-578T, …) | top dose only |  |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.015 | 12/35 (SNU-423, HOP62, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.33×** | +3.6 | 0.017 | 11/35 (SNU-423, A-172, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.017 | 15/33 (HOP62, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Carbamazepine (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.020 | 15/34 (RPMI-7951, SK-MEL-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.022 | 9/35 (Panc 03.27, BT-474, …) | rises with dose |  |
| [[Pexidartinib (hydrochloride) (drug)]] 0.5 µM |  | **1.32×** | +3.4 | 0.022 | 9/35 (RPMI-7951, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 36 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11189.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.296×** | -21.6 | 0e+00 | 34/35 (C32, H4, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.283×** | -15.8 | 0e+00 | 35/35 (H4, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.300×** | -14.5 | 1e-45 | 32/35 (C32, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.304×** | -14.4 | 1e-44 | 30/32 (J82, C32, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.327×** | -14.0 | 1e-42 | 31/35 (J82, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.329×** | -13.9 | 4e-42 | 32/35 (C32, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.347×** | -13.3 | 3e-38 | 33/35 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.352×** | -13.1 | 3e-37 | 33/35 (H4, C32, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.368×** | -12.5 | 3e-34 | 30/34 (C32, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.374×** | -12.3 | 4e-33 | 31/35 (C32, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.396×** | -11.6 | 2e-29 | 29/35 (C32, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.401×** | -11.5 | 1e-28 | 33/35 (NCI-H23, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.482×** | -9.2 | 2e-18 | 27/35 (SK-MEL-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.501×** | -8.7 | 2e-16 | 28/35 (J82, RPMI-7951, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.523×** | -7.7 | 6e-13 | 24/35 (C32, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.597×** | -6.5 | 4e-09 | 28/35 (H4, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.631×** | -5.8 | 2e-07 | 22/34 (H4, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11189. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 125 | 0 | 19 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0640× (z -30.0) |
| [[J82 (line)]] | alt | 103 | 0 | 17 (6 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0605× (z -24.3) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.157× (z -23.6) |
| [[C32 (line)]] | wt | 145 | 0 | 16 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0913× (z -31.9) |
| [[SK-MEL-2 (line)]] | alt | 137 | 0 | 14 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -20.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.210× (z -14.4) |
| [[NCI-H460 (line)]] | wt | 26.3 | 0 | 13 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.127× (z -15.4) |
| [[RPMI-7951 (line)]] | alt | 130 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -17.6) |
| [[SNU-423 (line)]] | alt | 69.9 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -24.4) |
| [[NCI-H1792 (line)]] | alt | 45.0 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0970× (z -22.6) |
| [[HS-578T (line)]] | alt | 78.6 | 0 | 9 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.127× (z -15.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -13.9) |
| [[AN3 CA (line)]] | alt | 92.8 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -15.5) |
| [[NCI-H23 (line)]] | alt | 56.4 | 0 | 7 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.136× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.139× (z -16.4) |
| [[hTERT-HPNE (line)]] | wt | 72.0 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.176× (z -12.0) |
| [[SHP-77 (line)]] | alt | 28.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0693× (z -19.1) |
| [[A-172 (line)]] | wt | 41.2 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.101× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.144× (z -13.7) |
| [[HOP62 (line)]] | alt | 30.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -17.4) |
| [[LOX-IMVI (line)]] | wt | 24.3 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0890× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~85% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.195× (z -9.2) |
| [[PANC-1 (line)]] | alt | 15.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.175× (z -17.9) |
| [[SW480 (line)]] | alt | 17.2 | 0 | 4 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.198× (z -11.7) |
| [[HepG2_C3A (line)]] | wt | 22.2 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0482× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.0886× (z -10.4) |
| [[NCI-H2030 (line)]] | alt | 44.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.385× (z -10.7) |
| [[A498 (line)]] | wt | 26.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -9.5) |
| [[C-33 A (line)]] | alt | 17.3 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -9.3) |
| [[CHP-212 (line)]] | wt | 24.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.116× (z -9.8) |
| [[SW 1271 (line)]] | alt | 60.9 | 0 | 2 | — | [[Radotinib (drug)]] 0.5 µM 0.0818× (z -8.6) |
| [[SW 900 (line)]] | alt | 12.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0318× (z -15.7) |
| [[A549 (line)]] | wt | 7.70 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.117× (z -8.7) ⚠ toxic |
| [[HCT15 (line)]] | alt | 10.8 | 0 | 1 | — | [[Entecavir (monohydrate) (drug)]] 0.05 µM 0.0514× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 8.47 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -10.5) |
| [[SW 1088 (line)]] | alt | 131 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0559× (z -11.2) |
| [[A-427 (line)]] | wt | 8.98 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 7.31 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 6.62 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.62 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.64 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.01 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.88 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.66 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.70 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.97 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11189), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NREP]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[PTPRD]] | +0.64 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[LINC03047]] | +0.61 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[SMAD9]] | +0.61 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[MDGA2]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[NRN1]] | +0.59 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[NIM1K]] | +0.59 | +0.50 / +0.58 | both halves | 1e-05 |  |
| [[KCTD16]] | +0.58 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[EPHA3]] | +0.58 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[NR2F2-AS1]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[LRRC7]] | +0.56 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[PLOD2]] | +0.56 | +0.49 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CALML4]] | -0.50 | -0.57 / -0.37 | both halves | 8e-05 |  |
| [[ARMC9]] | -0.47 | -0.39 / -0.44 | both halves | 5e-05 |  |
| [[APPL2]] | -0.46 | -0.35 / -0.44 | both halves | 1e-04 |  |
| [[ARHGEF16]] | -0.45 | -0.44 / -0.29 | both halves | 2e-04 |  |
| [[CLIC5]] | -0.45 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[PATJ]] | -0.45 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[SPIRE2]] | -0.45 | -0.31 / -0.40 | both halves | 2e-04 |  |
| [[PIK3CB]] | -0.45 | -0.33 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 22, C 6. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AEBP1]] | B | AEBP1 activity raises TMEM45A's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 4.89× lower at baseline in the lines without AEBP1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1 |
| [[HTRA3]] | B | HTRA3 activity raises TMEM45A's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 3.17× lower at baseline in the lines without HTRA3 | 0.011 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |
| [[C10orf90]] | B | C10orf90 activity raises TMEM45A's level | lines that do not express C10orf90 (35) vs lines expressing it (15) | 4.14× lower at baseline in the lines without C10orf90 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GRIN2A, LINC01242, ADGRG7; maybe low, not absent |
| [[FAM13C]] | B | FAM13C activity raises TMEM45A's level | lines that do not express FAM13C (15) vs lines expressing it (35) | 3.55× lower at baseline in the lines without FAM13C | 0.035 | ⚠ within organs, on part of the lines; also absent: DENND2A, SOX5, ANK2; maybe low, not absent |
| [[ZNF521]] | B | ZNF521 activity raises TMEM45A's level | lines that do not express ZNF521 (27) vs lines expressing it (23) | 2.87× lower at baseline in the lines without ZNF521 | 0.037 | ⚠ within organs, on part of the lines; also absent: LEF1, SNAI2, ITGA4 |
| [[MSC-AS1]] | B | MSC-AS1 activity raises TMEM45A's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 4.74× lower at baseline in the lines without MSC-AS1 | 0.037 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2 |
| [[KC6]] | B | KC6 activity raises TMEM45A's level | lines that do not express KC6 (32) vs lines expressing it (18) | 4.56× lower at baseline in the lines without KC6 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: GYPC, CCNYL2, COL19A1 |
| [[PDGFRB]] | B | PDGFRB activity raises TMEM45A's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 4.46× lower at baseline in the lines without PDGFRB | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2 |
| [[LINC01583]] | B | LINC01583 activity raises TMEM45A's level | lines that do not express LINC01583 (28) vs lines expressing it (22) | 4.42× lower at baseline in the lines without LINC01583 | 0.048 | ⚠ within organs, on part of the lines; also absent: INSYN2B, ADAM12, ZEB2 |
| [[LOXL3]] | B | LOXL3 activity raises TMEM45A's level | lines that do not express LOXL3 (26) vs lines expressing it (24) | 2.58× lower at baseline in the lines without LOXL3 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02240, KCNE4, LINC02941; maybe low, not absent |
| [[FZD1]] | B | FZD1 activity raises TMEM45A's level | lines that do not express FZD1 (6) vs lines expressing it (44) | 3.80× lower at baseline in the lines without FZD1 | 0.049 | ⚠ within organs, on part of the lines; also absent: TMOD2, SNPH, DNAI1; maybe low, not absent |
| [[NRN1]] | B | NRN1 activity raises TMEM45A's level | lines that do not express NRN1 (27) vs lines expressing it (23) | 2.22× lower at baseline in the lines without NRN1 | 0.050 | ⚠ within organs, on part of the lines; also absent: ILDR2, PHACTR1, ENSG00000250137 |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABL1]] | B | TMEM45A activity raises ABL1's level | lines that do not express TMEM45A (13) vs lines expressing it (37) | 1.59× lower at baseline in the lines without TMEM45A | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000289516, TTC28, ARHGEF25 |
| [[ITGB3BP]] | B | TMEM45A activity raises ITGB3BP's level | lines that do not express TMEM45A (13) vs lines expressing it (37) | 1.60× lower at baseline in the lines without TMEM45A | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000289516, TTC28, ARHGEF25 |
| cells under [[Entecavir (monohydrate) (drug)]] 5 µM | B | TMEM45A activity raises the cells' numbers under Entecavir (monohydrate) 5 µM (protects the cells) | lines that do not express TMEM45A (13) vs lines expressing it (35) | the lines without TMEM45A: 0.81× the cells of the other lines | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000289516, TTC28, ARHGEF25 |
| [[NREP]] | C | TMEM45A activity raises NREP's level | lines that do not express TMEM45A (13) vs lines expressing it (37) | 5.22× lower at baseline in the lines without TMEM45A | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000289516, TTC28, ARHGEF25; co-absent with the target |

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.646). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (49.2, 28.5); signed map (31.2, 42.1). **Vector** length 103, 28.9% of its response variance represented; |z| ≥ 3 in 1,134 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.1 | +3.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.2 | +3.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.3 | -0.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.7 | -0.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | +4.7 | -3.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.7 | +2.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | -0.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.4 | +4.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +3.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -13.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.7 | -5.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.6 | -13.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.8 | -14.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -8.7 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -2.1 | -1.0 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.0 | -1.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -5.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.9 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 45A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q12.2 — chr3:100,492,619-100,577,444 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10134, DERP7 |
| Hallmark sets | HYPOXIA |
| Matched by | ensembl_id |

UniProt [Q9NWC5](https://www.uniprot.org/uniprotkb/Q9NWC5) carries no function annotation.

**Summary**, from NCBI Gene [55076](https://www.ncbi.nlm.nih.gov/gene/55076):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25480](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25480) · Entrez [55076](https://www.ncbi.nlm.nih.gov/gene/55076) · UniProt [Q9NWC5](https://www.uniprot.org/uniprotkb/Q9NWC5) · Ensembl [ENSG00000181458](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181458)

## Data

Gene col 11189: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11189); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11189, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11189]; `tensor/DDL_lfc|DDL_z.npy` [11189]; `embed/gene_vectors.npy` [11189]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11189 or target_col == 11189). Every well: [[TMEM45A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM45A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
