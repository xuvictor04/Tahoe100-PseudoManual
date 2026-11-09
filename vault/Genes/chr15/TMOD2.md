---
symbol: "TMOD2"
type: "gene"
col: 4926
ensembl_id: "ENSG00000128872"
name: "tropomodulin 2"
location: "15q21.2"
module: 132
arm: "+"
pooled_cpm: 7.81
n_lines_expressing: 44
n_dd_up: 34
n_dd_down: 22
n_dd_up_clean: 25
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 7
direction_downstream: 8
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# TMOD2

*tropomodulin 2* — 15q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (9 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.74× (z +18.9, q 0e+00, up in 37 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.469× (z -13.8, q 2e-40, down in 28 of 37 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.452× (z -11.0, q 1e-25, down in 26 of 39 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNAZ]] (+0.66, fdr 7e-06), [[STX7]] (+0.66, fdr 3e-05), [[RAB6B]] (+0.66, fdr 1e-05); moves opposite to [[LINC01134]] (-0.62, fdr 3e-05), [[KIAA0753]] (-0.61, fdr 5e-05), [[CDK12]] (-0.60, fdr 3e-05).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[CAPG]] → it (grade B ⚠); 8 go from it, the strongest it → [[KIF3A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 9 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4926.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.74×** | +18.9 | 0e+00 | 37/41 (LoVo, HT-29, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.74×** | +18.3 | 0e+00 | 33/41 (SW480, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **3.45×** | +17.2 | 0e+00 | 36/41 (SW480, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.29×** | +16.5 | 0e+00 | 38/41 (SW480, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.26×** | +16.4 | 0e+00 | 36/41 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.67×** | +13.6 | 3e-40 | 36/39 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **4.39×** | +10.7 | 6e-25 | 35/39 (SW480, LoVo, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.20×** | +10.5 | 4e-24 | 11/14 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +8.3 | 9e-15 | 9/19 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.80×** | +8.2 | 2e-14 | 25/36 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.66×** | +7.0 | 1e-10 | 19/30 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.61×** | +6.6 | 2e-09 | 22/40 (LoVo, RKO, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +5.6 | 8e-07 | 14/32 (LoVo, SNU-423, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.30×** | +5.0 | 3e-05 | 11/41 (A-172, SNU-423, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.29×** | +4.8 | 6e-05 | 11/40 (NCI-H1573, Panc 03.27, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.38×** | +4.5 | 3e-04 | 12/37 (HT-29, BT-474, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.36×** | +4.3 | 5e-04 | 8/39 (HCT15, LOX-IMVI, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 0.5 µM |  | **1.51×** | +4.1 | 0.001 | 6/40 (SW1417, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.002 | 5/41 (LoVo, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4926.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.469×** | -13.8 | 2e-40 | 28/37 (NCI-H2030, A549, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.452×** | -11.0 | 1e-25 | 26/39 (A-427, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.481×** | -10.1 | 7e-22 | 30/41 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.490×** | -9.9 | 8e-21 | 29/41 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.533×** | -8.7 | 4e-16 | 25/38 (A549, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.538×** | -8.6 | 9e-16 | 22/41 (NCI-H2030, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.574×** | -7.4 | 1e-11 | 21/39 (NCI-H2030, LoVo, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.609×** | -6.9 | 5e-10 | 20/40 (NCI-H2030, A-427, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.622×** | -6.6 | 3e-09 | 20/36 (HEC-1-A, NCI-H2030, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.626×** | -6.5 | 5e-09 | 18/41 (A498, NCI-H2030, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.415×** | -6.4 | 1e-08 | 20/38 (HEC-1-A, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.664×** | -5.6 | 8e-07 | 16/39 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.689×** | -4.9 | 5e-05 | 17/36 (LOX-IMVI, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.511×** | -4.9 | 5e-05 | 16/35 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.550×** | -4.3 | 6e-04 | 10/37 (LOX-IMVI, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 0.05 µM |  | **0.726×** | -4.2 | 0.001 | 15/40 (SW 1271, LoVo, …) | all doses, flat |  |
| [[TAK-733 (drug)]] 0.05 µM |  | **0.764×** | -3.5 | 0.013 | 7/41 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.701×** | -3.5 | 0.013 | 5/41 (A549, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.621×** | -3.4 | 0.014 | 7/29 (hTERT-HPNE, RKO, …) | top dose only | noisy plate (z scaled) |
| [[Vilanterol (drug)]] 5 µM |  | 0.839× | -3.2 | 0.033 | 7/40 (Panc 03.27, SW 1271, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4926. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 11.6 | 3 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 4.23× (z +11.5) | [[Digitoxin (drug)]] 0.5 µM 0.169× (z -10.6) |
| [[SW480 (line)]] | alt | 8.33 | 6 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.47× (z +11.0) | — |
| [[HEC-1-A (line)]] | alt | 13.3 | 1 | 4 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.94× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -13.4) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.268× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 18.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -17.8) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.204× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 7.54 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.96× (z +9.9) | — |
| [[A-427 (line)]] | wt | 17.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -11.0) ⚠ cell-cycle shift, explains ~33% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.240× (z -9.3) |
| [[A549 (line)]] | wt | 8.55 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.103× (z -14.0) ⚠ cell-cycle shift, explains ~33% of this change |
| [[J82 (line)]] | alt | 7.60 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0917× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.154× (z -8.5) |
| [[NCI-H2347 (line)]] | alt | 4.63 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.49× (z +9.4) | — |
| [[SW48 (line)]] | wt | 19.7 | 0 | 2 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0948× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 21.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -8.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HT-29 (line)]] | alt | 3.82 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 12.2× (z +11.3) | — |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.171× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 7.57 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0843× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 2.14 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.77× (z +9.7) | — |
| [[A498 (line)]] | wt | 4.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.93 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.991 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.65 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.46 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.59 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 8.20 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.871 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.884 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.14 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.30 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4926), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNAZ]] | +0.66 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[STX7]] | +0.66 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[RAB6B]] | +0.66 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[ABRAXAS1]] | +0.65 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[MCUR1]] ⚠ | +0.64 | +0.50 / +0.65 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RAB4A]] | +0.64 | +0.45 / +0.60 | both halves | 3e-05 |  |
| [[RIMS3]] | +0.63 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[IL17RD]] | +0.63 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[ARRB2]] | +0.63 | +0.43 / +0.60 | both halves | 3e-05 |  |
| [[STX2]] | +0.62 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[TSPAN33]] | +0.62 | +0.43 / +0.63 | both halves | 3e-05 |  |
| [[DUBR]] | +0.62 | +0.58 / +0.72 | both halves | 8e-06 |  |
| [[ZDHHC2]] | +0.62 | +0.65 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01134]] | -0.62 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[KIAA0753]] | -0.61 | -0.40 / -0.61 | both halves | 5e-05 |  |
| [[CDK12]] | -0.60 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[ACAD9]] | -0.59 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[LINC01004]] | -0.59 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[MIRLET7IHG]] | -0.59 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[UBE3B]] | -0.58 | -0.37 / -0.54 | both halves | 8e-05 |  |
| [[GOSR1]] | -0.58 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[RECQL5]] | -0.58 | -0.44 / -0.58 | both halves | 3e-05 |  |
| [[MPDU1]] | -0.58 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[PDHX]] | -0.57 | -0.37 / -0.46 | both halves | 7e-05 |  |
| [[LINS1]] | -0.56 | -0.30 / -0.49 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAPG]] | B | CAPG activity lowers TMOD2's level | lines that do not express CAPG (17) vs lines expressing it (33) | 1.60× higher at baseline in the lines without CAPG | 0.033 | ⚠ within organs, on part of the lines; also absent: MALL, LINC02086, SH3RF2 |
| [[PRKAR2B]] | B | PRKAR2B activity raises TMOD2's level | lines that do not express PRKAR2B (12) vs lines expressing it (38) | 2.07× lower at baseline in the lines without PRKAR2B | 0.054 | ⚠ within organs, on part of the lines; also absent: EML1, GALNT16, KATNAL2 |
| [[ZDHHC2]] | B | ZDHHC2 activity raises TMOD2's level | lines that do not express ZDHHC2 (10) vs lines expressing it (40) | 1.72× lower at baseline in the lines without ZDHHC2 | 0.056 | ⚠ within organs, on part of the lines; also absent: ENSG00000289145, TGFB1, PGM5P2 |
| [[TMEM170B]] | B | TMEM170B activity raises TMOD2's level | lines that do not express TMEM170B (8) vs lines expressing it (42) | 2.38× lower at baseline in the lines without TMEM170B | 0.072 | ⚠ within organs, on part of the lines; also absent: KCNK13, KDM2B-DT, LINC02609 |
| [[TMEM150C]] | B | TMEM150C activity raises TMOD2's level | lines that do not express TMEM150C (13) vs lines expressing it (37) | 1.89× lower at baseline in the lines without TMEM150C | 0.078 | ⚠ within organs, on part of the lines; also absent: AP3B2, MED12L, RAB6B; maybe low, not absent |
| [[MYO5A]] | C | MYO5A activity raises TMOD2's level | lines that do not express MYO5A (6) vs lines expressing it (44) | 2.99× lower at baseline in the lines without MYO5A | 0.012 | ⚠ within organs, on part of the lines; also absent: TPST1, CYP46A1, CSRP2; co-absent with the target |
| [[PHC1]] | C | PHC1 activity raises TMOD2's level | lines that do not express PHC1 (4) vs lines expressing it (46) | 3.34× lower at baseline in the lines without PHC1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HECTD2, TPST1, TBKBP1; its own permutation p |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 5, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KIF3A]] | B | TMOD2 activity raises KIF3A's level | lines that do not express TMOD2 (6) vs lines expressing it (44) | 2.09× lower at baseline in the lines without TMOD2 | 0.018 | ⚠ within organs, on part of the lines; also absent: CCDC102A, CYP46A1, FZD1; maybe low, not absent |
| [[SOAT1]] | B | TMOD2 activity raises SOAT1's level | lines that do not express TMOD2 (6) vs lines expressing it (44) | 2.65× lower at baseline in the lines without TMOD2 | 0.033 | ⚠ within organs, on part of the lines; also absent: CCDC102A, CYP46A1, FZD1; maybe low, not absent |
| [[SEMA4F]] | B | TMOD2 activity raises SEMA4F's level | lines that do not express TMOD2 (6) vs lines expressing it (44) | 1.92× lower at baseline in the lines without TMOD2 | 0.065 | ⚠ within organs, on part of the lines; also absent: CCDC102A, CYP46A1, FZD1; maybe low, not absent |
| [[CBX6]] | B | TMOD2 activity raises CBX6's level | lines that do not express TMOD2 (6) vs lines expressing it (44) | 1.70× lower at baseline in the lines without TMOD2 | 0.087 | ⚠ within organs, on part of the lines; also absent: CCDC102A, CYP46A1, FZD1; maybe low, not absent |
| [[GNB5]] | B | TMOD2 activity raises GNB5's level | lines that do not express TMOD2 (6) vs lines expressing it (44) | 1.68× lower at baseline in the lines without TMOD2 | 0.098 | ⚠ within organs, on part of the lines; also absent: CCDC102A, CYP46A1, FZD1; maybe low, not absent |
| [[MYO5A]] | C | TMOD2 activity raises MYO5A's level | lines that do not express TMOD2 (6) vs lines expressing it (44) | 5.93× lower at baseline in the lines without TMOD2 | 0.013 | ⚠ within organs, on part of the lines; also absent: CCDC102A, CYP46A1, FZD1; maybe low, not absent; co-absent with the target |
| [[SNPH]] | C | TMOD2 activity raises SNPH's level | lines that do not express TMOD2 (6) vs lines expressing it (44) | 2.97× lower at baseline in the lines without TMOD2 | 0.033 | ⚠ within organs, on part of the lines; also absent: CCDC102A, CYP46A1, FZD1; maybe low, not absent; co-absent with the target |
| [[MITF]] | C | TMOD2 activity raises MITF's level | lines that do not express TMOD2 (6) vs lines expressing it (44) | 5.57× lower at baseline in the lines without TMOD2 | 0.053 | ⚠ within organs, on part of the lines; also absent: CCDC102A, CYP46A1, FZD1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.689). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.9, -4.3); signed map (-34.3, -12.9). **Vector** length 80.9, 16.1% of its response variance represented; |z| ≥ 3 in 1,159 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.8 | +18.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.1 | +13.6 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.9 | +16.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.7 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | +10.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.5 | +10.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.6 | +2.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.5 | +3.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +4.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.8 | -13.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.6 | -7.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -2.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -2.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.8 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -6.9 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.7 | -3.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.5 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | tropomodulin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.2 — chr15:51,751,597-51,816,363 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NTMOD |
| Gene groups (HGNC) | Tropomodulins |
| Reactome | 2 pathways, smallest: Striated Muscle Contraction; Muscle contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZR1](https://www.uniprot.org/uniprotkb/Q9NZR1) (Tropomodulin-2):

> Blocks the elongation and depolymerization of the actin filaments at the pointed end. The Tmod/TM complex contributes to the formation of the short actin protofilament, which in turn defines the geometry of the membrane skeleton (By similarity).

**Summary**, from NCBI Gene [29767](https://www.ncbi.nlm.nih.gov/gene/29767):

> This gene encodes a neuronal-specific member of the tropomodulin family of actin-regulatory proteins. The encoded protein caps the pointed end of actin filaments preventing both elongation and depolymerization. The capping activity of this protein is dependent on its association with tropomyosin. Alternatively spliced transcript variants encoding different isoforms have been described. [provided by RefSeq, Dec 2008]

**Accessions** — [HGNC:11872](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11872) · Entrez [29767](https://www.ncbi.nlm.nih.gov/gene/29767) · UniProt [Q9NZR1](https://www.uniprot.org/uniprotkb/Q9NZR1) · Ensembl [ENSG00000128872](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128872)

## Data

Gene col 4926: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4926); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4926, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4926]; `tensor/DDL_lfc|DDL_z.npy` [4926]; `embed/gene_vectors.npy` [4926]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4926 or target_col == 4926). Every well: [[TMOD2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMOD2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
