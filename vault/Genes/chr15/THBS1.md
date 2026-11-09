---
symbol: "THBS1"
type: "gene"
col: 6065
ensembl_id: "ENSG00000137801"
name: "thrombospondin 1"
location: "15q14"
module: 66
arm: "+"
pooled_cpm: 61.61
n_lines_expressing: 36
n_dd_up: 31
n_dd_down: 15
n_dd_up_clean: 17
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 6
direction_downstream: 7
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# THBS1

*thrombospondin 1* — 15q14

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.14× (z +21.0, q 0e+00, up in 27 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 5 µM: 0.515× (z -6.7, q 1e-08, down in 20 of 33 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL12A1]] (+0.68, fdr 7e-06), [[CDH2]] (+0.68, fdr 7e-06), [[CRIM1]] (+0.67, fdr 7e-06); moves opposite to [[FLYWCH1]] (-0.58, fdr 1e-05), [[CCDC167]] (-0.57, fdr 1e-05), [[MED10]] (-0.56, fdr 1e-05).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LUM]] → it (grade B ⚠); 7 go from it, the strongest it → [[MED10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 15 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6065.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.14×** | +21.0 | 0e+00 | 27/34 (CFPAC-1, A498, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.87×** | +18.5 | 0e+00 | 33/35 (Panc 03.27, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.07×** | +18.2 | 0e+00 | 27/28 (Panc 03.27, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.67×** | +14.9 | 0e+00 | 31/32 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.87×** | +9.2 | 3e-18 | 26/34 (J82, hTERT-HPNE, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **4.52×** | +8.3 | 1e-14 | 27/35 (CFPAC-1, BT-474, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.11×** | +7.8 | 5e-13 | 22/34 (A498, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **2.10×** | +7.8 | 6e-13 | 25/34 (J82, hTERT-HPNE, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.15×** | +7.7 | 8e-13 | 21/33 (HOP62, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.06×** | +7.6 | 2e-12 | 26/34 (J82, hTERT-HPNE, …) | all doses, stronger at high dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.00×** | +7.2 | 2e-11 | 22/34 (HT-29, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +6.7 | 8e-10 | 18/34 (SW480, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.88×** | +6.3 | 1e-08 | 18/34 (A549, HT-29, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.76×** | +5.9 | 1e-07 | 20/34 (Panc 03.27, HOP62, …) | rises with dose | composition shift; position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.17× | +5.7 | 4e-07 | 10/35 (HOP62, NCI-H1792, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.66×** | +5.3 | 4e-06 | 21/34 (SW480, NCI-H1573, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.62×** | +5.0 | 2e-05 | 22/34 (J82, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.58×** | +4.6 | 1e-04 | 17/34 (HS-578T, SNU-423, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.006 | 19/34 (HOP62, hTERT-HPNE, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.41×** | +3.6 | 0.009 | 13/34 (J82, SNU-423, …) | all doses, flat | position effect removed |
| [[Bimiralisib (drug)]] 5 µM |  | **1.79×** | +3.2 | 0.032 | 12/35 (HS-578T, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **1.73×** | +3.0 | 0.058 | 11/34 (HS-578T, HOP62, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.32×** | +2.9 | 0.071 | 11/34 (HS-578T, A549, …) | inconsistent across doses |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **1.21×** | +2.9 | 0.087 | 9/34 (J82, SNU-423, …) | all doses, flat | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6065.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.515×** | -6.7 | 1e-08 | 20/33 (SW1417, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.580×** | -5.7 | 3e-06 | 19/33 (NCI-H2030, H4, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Verteporfin (drug)]] 5 µM |  | **0.582×** | -5.5 | 8e-06 | 20/34 (SW 1088, HepG2/C3A, …) | top dose only | position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.597×** | -5.4 | 8e-06 | 22/34 (J82, NCI-H23, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.621×** | -5.0 | 6e-05 | 21/34 (AsPC-1, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.627×** | -4.9 | 9e-05 | 19/34 (HepG2/C3A, Panc 03.27, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.649×** | -4.3 | 0.001 | 16/34 (HepG2/C3A, NCI-H2030, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.766×** | -4.0 | 0.005 | 16/34 (J82, HS-578T, …) | top dose only | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.695×** | -3.8 | 0.008 | 16/34 (NCI-H1792, H4, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **0.726×** | -3.4 | 0.042 | 14/34 (H4, J82, …) | top dose only | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.803×** | -3.3 | 0.054 | 14/34 (J82, H4, …) | rises with dose |  |
| [[Terfenadine (drug)]] 5 µM |  | **0.807×** | -3.2 | 0.061 | 11/34 (RPMI-7951, A498, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.739×** | -3.2 | 0.061 | 14/34 (NCI-H2030, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **0.745×** | -3.1 | 0.072 | 13/34 (J82, H4, …) | two highest doses | position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.745×** | -3.1 | 0.072 | 12/34 (SW 1088, SW 900, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6065. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 141 | 8 (6 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.91× (z +13.2) | — |
| [[HOP62 (line)]] | alt | 178 | 7 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 34.1× (z +17.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.99× (z +9.8) | — |
| [[hTERT-HPNE (line)]] | wt | 94.6 | 7 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 15.4× (z +17.8) | — |
| [[A498 (line)]] | wt | 30.3 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +21.2) | — |
| [[NCI-H2030 (line)]] | alt | 141 | 5 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.94× (z +11.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.34× (z +10.7) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.256× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 97.8 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.5× (z +24.9) | — |
| [[HS-578T (line)]] | alt | 92.0 | 5 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.6× (z +14.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.72× (z +11.5) | — |
| [[Panc 03.27 (line)]] | alt | 196 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.59× (z +18.7) | — |
| [[A549 (line)]] | wt | 38.1 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.3× (z +17.5) | — |
| [[BT-474 (line)]] | alt | 27.2 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 13.2× (z +14.5) | — |
| [[H4 (line)]] | wt | 96.5 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 13.4× (z +11.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 4.31× (z +9.2) | — |
| [[NCI-H1792 (line)]] | alt | 134 | 3 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.09× (z +16.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.206× (z -9.9) ⚠ toxic; cell-cycle shift, explains ~72% of this change |
| [[NCI-H2347 (line)]] | alt | 38.2 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.43× (z +16.1) | — |
| [[RPMI-7951 (line)]] | alt | 263 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.2× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 3.05× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 15.6 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 26.3× (z +11.0) | — |
| [[HT-29 (line)]] | alt | 53.4 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +19.8) | — |
| [[NCI-H1573 (line)]] | alt | 21.5 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.70× (z +13.1) | — |
| [[SNU-423 (line)]] | alt | 308 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 15.8× (z +14.5) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 132 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +11.6) | — |
| [[SW480 (line)]] | alt | 32.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.71× (z +14.3) | — |
| [[LoVo (line)]] | wt | 72.5 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.62× (z +11.4) | [[Digitoxin (drug)]] 5 µM 0.315× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 49.7 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 18.6× (z +11.2) | — |
| [[AN3 CA (line)]] | alt | 98.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 14.2× (z +10.3) | — |
| [[AsPC-1 (line)]] | alt | 47.3 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.232× (z -9.5) |
| [[C-33 A (line)]] | alt | 34.2 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0469× (z -9.5) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 57.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.21× (z +8.8) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 33.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +8.5) | — |
| [[SW 1088 (line)]] | alt | 242 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.0479× (z -8.8) |
| [[SW1417 (line)]] | alt | 87.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +14.2) | — |
| [[A-172 (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 4.17 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.99 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 240 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.23 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.78 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 99.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.88 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.20 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 14.9 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.50 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 607 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 10.3 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.63 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.03 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.27 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6065), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL12A1]] | +0.68 | +0.65 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 529 |
| [[CDH2]] | +0.68 | +0.60 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 585 |
| [[CRIM1]] | +0.67 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[IL6ST]] | +0.63 | +0.58 / +0.63 | both halves | 7e-06 |  |
| [[GLIPR1]] | +0.60 | +0.46 / +0.60 | both halves | 2e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[TGFB2]] | +0.60 | +0.51 / +0.53 | both halves | 1e-05 | pathway: Extracellular matrix organization; STRING 892 |
| [[TPM1]] | +0.60 | +0.46 / +0.59 | both halves | 3e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[CDK6]] | +0.59 | +0.52 / +0.54 | both halves | 1e-05 | pathway: Transcriptional regulation by RUNX1 |
| [[ALCAM]] | +0.59 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[ALPK2]] | +0.59 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[DDX3X]] | +0.58 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[FAT1]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 4 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLYWCH1]] | -0.58 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[CCDC167]] | -0.57 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[MED10]] | -0.56 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[CAMLG]] | -0.55 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[RPP21]] | -0.55 | -0.41 / -0.54 | both halves | 4e-05 |  |
| [[TULP3]] | -0.54 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[IL17RA]] | -0.54 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[C1orf174]] | -0.54 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[BAHD1]] | -0.53 | -0.48 / -0.41 | both halves | 4e-05 |  |
| [[C1orf35]] | -0.53 | -0.29 / -0.52 | both halves | 2e-04 |  |
| [[EMC2]] | -0.52 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[MRPS36]] ⚠ | -0.52 | -0.32 / -0.54 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[CRYZL1]] | -0.52 | -0.47 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LUM]] | B | LUM activity raises THBS1's level | lines that do not express LUM (34) vs lines expressing it (16) | 5.62× lower at baseline in the lines without LUM | 0.008 | ⚠ within organs, on part of the lines; also absent: ITGA11, DCN, IRAG2 |
| [[VGLL3]] | B | VGLL3 activity raises THBS1's level | lines that do not express VGLL3 (30) vs lines expressing it (20) | 3.59× lower at baseline in the lines without VGLL3 | 0.021 | ⚠ within organs, on part of the lines; also absent: EDNRA, APBB1IP, LINC02882 |
| [[TOP2A]] | B | TOP2A activity lowers THBS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[BICC1]] | B | BICC1 activity raises THBS1's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 3.67× lower at baseline in the lines without BICC1 | 0.066 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2 |
| [[TGFBI]] | B | TGFBI activity raises THBS1's level | lines that do not express TGFBI (25) vs lines expressing it (25) | 3.12× lower at baseline in the lines without TGFBI | 0.095 | ⚠ within organs, on part of the lines; also absent: IL6, SRPX2, ENSG00000232949 |
| [[TPM1]] | C | TPM1 activity raises THBS1's level | lines that do not express TPM1 (3) vs lines expressing it (47) | 8.74× lower at baseline in the lines without TPM1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: B4GALT1, SSUH2, XIRP2; maybe low, not absent; its own permutation p |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MED10]] | B | THBS1 activity raises MED10's level | lines that do not express THBS1 (14) vs lines expressing it (36) | 1.34× lower at baseline in the lines without THBS1 | 0.034 | ⚠ within organs, on part of the lines; also absent: ETNK2, SLC35G2, ENSG00000176593 |
| [[ASB7]] | B | THBS1 activity raises ASB7's level | lines that do not express THBS1 (14) vs lines expressing it (36) | 1.10× lower at baseline in the lines without THBS1 | 0.034 | ⚠ within organs, on part of the lines; also absent: ETNK2, SLC35G2, ENSG00000176593 |
| [[CARD19]] | B | THBS1 activity raises CARD19's level | lines that do not express THBS1 (14) vs lines expressing it (36) | 1.37× lower at baseline in the lines without THBS1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ETNK2, SLC35G2, ENSG00000176593 |
| [[LUM]] | B | THBS1 activity raises LUM's level | lines that do not express THBS1 (14) vs lines expressing it (36) | 2.30× lower at baseline in the lines without THBS1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ETNK2, SLC35G2, ENSG00000176593 |
| [[SLC39A10]] | B | THBS1 activity lowers SLC39A10's level | lines that do not express THBS1 (14) vs lines expressing it (36) | 1.24× higher at baseline in the lines without THBS1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ETNK2, SLC35G2, ENSG00000176593 |
| [[FSIP1]] | B | THBS1 activity raises FSIP1's level | lines that do not express THBS1 (14) vs lines expressing it (36) | 1.54× lower at baseline in the lines without THBS1 | 0.083 | ⚠ within organs, on part of the lines; also absent: ETNK2, SLC35G2, ENSG00000176593 |
| [[VGLL3]] | B | THBS1 activity raises VGLL3's level | lines that do not express THBS1 (14) vs lines expressing it (36) | 3.36× lower at baseline in the lines without THBS1 | 0.083 | ⚠ within organs, on part of the lines; also absent: ETNK2, SLC35G2, ENSG00000176593 |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.689). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.4, 15.2); signed map (45.7, 19.0). **Vector** length 115, 30.4% of its response variance represented; |z| ≥ 3 in 1,184 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.4 | +14.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.2 | +18.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.0 | +21.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.7 | +8.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +18.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +9.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +7.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +3.1 | +5.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +4.6 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | -4.4 | -4.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.4 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | -4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~72% of this change | -3.2 | +1.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -2.7 | -3.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.5 | -5.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.4 | -3.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.2 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | thrombospondin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q14 — chr15:39,581,079-39,599,466 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TSP1, THBS, TSP, THBS-1, TSP-1 |
| Gene groups (HGNC) | Thrombospondin family |
| Hallmark sets | TGF_BETA_SIGNALING, COAGULATION, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 18 pathways, smallest: Syndecan interactions; Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P07996](https://www.uniprot.org/uniprotkb/P07996) (Thrombospondin-1):

> Adhesive glycoprotein that mediates cell-to-cell and cell-to-matrix interactions. Multifunctional, involved in inflammation, angiogenesis, wound healing, reactive oxygen species (ROS) signaling, nitrous oxide (NO) signaling, apoptosis, senescence, aging, cellular self-renewal, stemness, and cardiovascular and metabolic homeostasis. Negatively modulates dendritic cell activation and cytokine release, as part of an autocrine feedback loop, contributing to the resolution of inflammation and immune …

**Summary**, from NCBI Gene [7057](https://www.ncbi.nlm.nih.gov/gene/7057):

> The protein encoded by this gene is a subunit of a disulfide-linked homotrimeric protein. This protein is an adhesive glycoprotein that mediates cell-to-cell and cell-to-matrix interactions. This protein can bind to fibrinogen, fibronectin, laminin, type V collagen and integrins alpha-V/beta-1. This protein has been shown to play roles in platelet aggregation, angiogenesis, and tumorigenesis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11785](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11785) · Entrez [7057](https://www.ncbi.nlm.nih.gov/gene/7057) · UniProt [P07996](https://www.uniprot.org/uniprotkb/P07996) · Ensembl [ENSG00000137801](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000137801)

## Data

Gene col 6065: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6065); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6065, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6065]; `tensor/DDL_lfc|DDL_z.npy` [6065]; `embed/gene_vectors.npy` [6065]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6065 or target_col == 6065). Every well: [[THBS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THBS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
