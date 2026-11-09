---
symbol: "NAP1L4"
type: "gene"
col: 12984
ensembl_id: "ENSG00000205531"
name: "nucleosome assembly protein 1 like 4"
location: "11p15.4"
module: 57
arm: "+"
pooled_cpm: 199.12
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 4
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# NAP1L4

*nucleosome assembly protein 1 like 4* — 11p15.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.79× (z +13.3, q 1e-37, up in 46 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.70× (z +12.2, q 2e-31, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.796× (z -7.4, q 1e-10, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPA1]] (+0.71, fdr 7e-06), [[CDS2]] (+0.65, fdr 7e-06), [[NUP43]] (+0.65, fdr 1e-05); moves opposite to [[GSPT2]] (-0.71, fdr 7e-06), [[MRFAP1L1]] (-0.67, fdr 7e-06), [[UTP3]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HHEX]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 9 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12984.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.79×** | +13.3 | 1e-37 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.70×** | +12.2 | 2e-31 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.50×** | +9.3 | 2e-18 | 43/48 (PANC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +9.1 | 1e-17 | 39/47 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.45×** | +8.4 | 3e-15 | 36/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +7.8 | 5e-13 | 38/48 (SW480, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +7.5 | 7e-12 | 37/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **1.39×** | +7.4 | 7e-12 | 35/49 (PANC-1, KATO III, …) | all doses, flat | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.31×** | +5.9 | 3e-07 | 35/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.28×** | +5.3 | 7e-06 | 28/45 (SW480, KATO III, …) | all doses, flat | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.53×** | +5.0 | 2e-05 | 31/48 (PANC-1, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **1.26×** | +5.0 | 3e-05 | 24/44 (C-33 A, KATO III, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.51×** | +5.0 | 3e-05 | 28/49 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.47×** | +4.6 | 2e-04 | 27/38 (PANC-1, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.24×** | +4.5 | 2e-04 | 26/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 1.14× | +4.3 | 7e-04 | 6/49 (RPMI-7951, LS 180, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.13× | +4.1 | 0.002 | 11/49 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | 1.18× | +3.6 | 0.011 | 15/49 (SHP-77, hTERT-HPNE, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.24×** | +3.4 | 0.018 | 23/49 (PANC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 0.05 µM |  | 1.16× | +3.3 | 0.026 | 12/48 (SK-MEL-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 0.05 µM |  | 1.15× | +2.9 | 0.094 | 4/48 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12984.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.796×** | -7.4 | 1e-10 | 27/48 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.818×** | -6.5 | 2e-08 | 30/48 (A-172, NCI-H2347, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.774×** | -5.8 | 1e-06 | 27/48 (A-172, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.811×** | -4.8 | 3e-04 | 28/49 (SW480, J82, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.875× | -4.3 | 0.002 | 13/48 (HOP62, RPMI-7951, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 0.835× | -4.0 | 0.007 | 22/48 (A-172, HCT15, …) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | 0.842× | -3.9 | 0.009 | 18/47 (NCI-H23, A549, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.848× | -3.8 | 0.012 | 13/48 (A498, A549, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | 0.849× | -3.6 | 0.021 | 17/47 (A-172, NCI-H1792, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.849× | -3.5 | 0.023 | 16/47 (SW 900, A-427, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | 0.857× | -3.5 | 0.023 | 16/48 (NCI-H1573, A549, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.961× | -3.3 | 0.049 | 0/50 | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.877× | -3.0 | 0.12 | 14/48 (J82, HCT15, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12984. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 296 | 9 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.34× (z +23.1) | — |
| [[NCI-H460 (line)]] | wt | 127 | 8 (4 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.34× (z +12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.26× (z +11.9) | — |
| [[SW480 (line)]] | alt | 256 | 7 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +18.0) | — |
| [[NCI-H1792 (line)]] | alt | 144 | 6 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.53× (z +15.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 3.03× (z +13.6) | — |
| [[LoVo (line)]] | wt | 178 | 5 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.87× (z +16.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.52× (z +14.4) | — |
| [[HepG2_C3A (line)]] | wt | 177 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.89× (z +12.9) | — |
| [[HT-29 (line)]] | alt | 169 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.69× (z +13.0) | — |
| [[KATO III (line)]] | alt | 110 | 4 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.93× (z +14.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.83× (z +14.2) | — |
| [[NCI-H23 (line)]] | alt | 157 | 4 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +12.3) | — |
| [[A-427 (line)]] | wt | 173 | 1 | 2 | [[Ixazomib citrate (drug)]] 5 µM 1.83× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.459× (z -16.6) |
| [[C-33 A (line)]] | alt | 179 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.82× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 1.92× (z +8.8) | — |
| [[COLO 205 (line)]] | alt | 138 | 3 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.56× (z +10.3) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.37× (z +9.4) | — |
| [[LS 180 (line)]] | wt | 214 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.13× (z +14.8) | — |
| [[NCI-H1573 (line)]] | alt | 103 | 1 (1 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 2.06× (z +8.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.563× (z -9.9) |
| [[A-172 (line)]] | wt | 210 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.540× (z -15.2) |
| [[H4 (line)]] | wt | 277 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.33× (z +10.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.20× (z +9.5) | — |
| [[HOP62 (line)]] | alt | 214 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -13.6) |
| [[J82 (line)]] | alt | 332 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.90× (z +11.2) | — |
| [[RKO (line)]] | wt | 190 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +9.2) | — |
| [[SHP-77 (line)]] | alt | 91.5 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.71× (z +11.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +11.1) | — |
| [[SNU-423 (line)]] | alt | 229 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.05× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[SW1417 (line)]] | alt | 263 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +12.9) | — |
| [[C32 (line)]] | wt | 144 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +9.4) ⚠ cell-cycle shift, explains ~69% of this change | — |
| [[CFPAC-1 (line)]] | alt | 130 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.590× (z -10.0) |
| [[Hs 766T (line)]] | wt | 209 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.561× (z -10.9) |
| [[hTERT-HPNE (line)]] | wt | 150 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.587× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 191 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.657× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 213 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.43× (z +11.8) | — |
| [[NCI-H2030 (line)]] | alt | 136 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.95× (z +8.8) | — |
| [[NCI-H2347 (line)]] | alt | 270 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.583× (z -8.8) |
| [[SNU-1 (line)]] | wt | 185 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.354× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW 900 (line)]] | alt | 97.7 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.75× (z +10.0) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 294 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 218 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 231 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 241 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 134 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 202 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 208 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 173 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 191 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 179 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 203 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 212 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12984), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*39 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPA1]] | +0.71 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[CDS2]] | +0.65 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[NUP43]] | +0.65 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[DIP2A]] | +0.63 | +0.75 / +0.52 | both halves | 1e-05 |  |
| [[ADD1]] | +0.62 | +0.73 / +0.59 | both halves | 7e-06 |  |
| [[PMS2P3-1]] | +0.61 | +0.72 / +0.51 | both halves | 1e-05 |  |
| [[ATP6AP2]] | +0.61 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[SETD3]] | +0.61 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[UBAC1]] | +0.61 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[HACD3]] | +0.60 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[SDHAP4]] | +0.60 | +0.72 / +0.50 | both halves | 1e-05 |  |
| [[VDAC3]] | +0.60 | +0.73 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*61 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GSPT2]] | -0.71 | -0.65 / -0.73 | both halves | 7e-06 |  |
| [[MRFAP1L1]] | -0.67 | -0.71 / -0.64 | both halves | 7e-06 |  |
| [[UTP3]] | -0.65 | -0.72 / -0.63 | both halves | 7e-06 |  |
| [[FAM200A]] | -0.65 | -0.75 / -0.57 | both halves | 1e-05 |  |
| [[ZNF620]] | -0.64 | -0.74 / -0.53 | both halves | 1e-05 |  |
| [[ZNF155]] | -0.64 | -0.64 / -0.65 | both halves | 7e-06 |  |
| [[RTL6]] | -0.63 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[ZNF140]] | -0.63 | -0.64 / -0.46 | both halves | 2e-05 |  |
| [[ZNF317]] | -0.62 | -0.59 / -0.61 | both halves | 7e-06 |  |
| [[CMTR2]] | -0.61 | -0.65 / -0.56 | both halves | 1e-05 |  |
| [[ZNF776]] | -0.61 | -0.69 / -0.47 | both halves | 2e-05 |  |
| [[HELQ]] | -0.61 | -0.73 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HHEX]] | B | HHEX activity raises NAP1L4's level | lines that do not express HHEX (18) vs lines expressing it (32) | 1.13× lower at baseline in the lines without HHEX | 0.023 | ⚠ within organs, on part of the lines; also absent: HEYL, MT1A, NUP62CL |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.558). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-34.0, 8.6); signed map (-38.3, -10.5). **Vector** length 109, 36.2% of its response variance represented; |z| ≥ 3 in 1,085 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +5.8 | +7.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +5.7 | +5.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +5.7 | +3.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.7 | +2.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +4.1 | +9.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +7.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.3 | +3.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.3 | +1.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | +2.0 | +1.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.0 | +3.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -10.8 | -7.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -10.2 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -10.0 | -5.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.3 | -2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.4 | -6.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.8 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | +0.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -1.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.2 | -3.5 |

## What is on record

|  |  |
|---|---|
| Name | nucleosome assembly protein 1 like 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.4 — chr11:2,944,431-2,992,377 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NAP2 |
| Gene groups (HGNC) | Small nucleolar RNA protein coding host genes; Nucleosome assembly protein 1 like family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99733](https://www.uniprot.org/uniprotkb/Q99733) (Nucleosome assembly protein 1-like 4):

> Acts as a histone chaperone in nucleosome assembly.

**Summary**, from NCBI Gene [4676](https://www.ncbi.nlm.nih.gov/gene/4676):

> This gene encodes a member of the nucleosome assembly protein (NAP) family which can interact with both core and linker histones. It can shuttle between the cytoplasm and nucleus, suggesting a role as a histone chaperone. This gene is one of several located near the imprinted gene domain of 11p15.5, an important tumor-suppressor gene region. Alterations in this region have been associated with the Beckwith-Wiedemann syndrome, Wilms tumor, rhabdomyosarcoma, adrenocortical carcinoma, and lung, …

**Accessions** — [HGNC:7640](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7640) · Entrez [4676](https://www.ncbi.nlm.nih.gov/gene/4676) · UniProt [Q99733](https://www.uniprot.org/uniprotkb/Q99733) · Ensembl [ENSG00000205531](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205531)

## Data

Gene col 12984: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12984); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12984, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12984]; `tensor/DDL_lfc|DDL_z.npy` [12984]; `embed/gene_vectors.npy` [12984]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12984 or target_col == 12984). Every well: [[NAP1L4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAP1L4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
