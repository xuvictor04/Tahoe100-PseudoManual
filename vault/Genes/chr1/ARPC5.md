---
symbol: "ARPC5"
type: "gene"
col: 8566
ensembl_id: "ENSG00000162704"
name: "actin related protein 2/3 complex subunit 5"
location: "1q25.3"
module: 60
arm: "+"
pooled_cpm: 112.83
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 14
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# ARPC5

*actin related protein 2/3 complex subunit 5* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.75× (z +15.5, q 0e+00, up in 47 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Peretinoin (drug)]] 5 µM: 1.39× (z +4.9, q 2e-04, up in 31 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.395× (z -20.1, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PSMD2]] (+0.65, fdr 7e-06), [[PRDX1]] (+0.61, fdr 1e-05), [[ACTR2]] (+0.59, fdr 8e-06); moves opposite to [[YY1AP1]] (-0.66, fdr 7e-06), [[PER1]] (-0.60, fdr 1e-05), [[SAT2]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[DYNLT3]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 6 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8566.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.75×** | +15.5 | 0e+00 | 47/49 (KATO III, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.76×** | +14.9 | 0e+00 | 42/44 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.13×** | +10.7 | 1e-24 | 39/45 (SNU-423, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.39×** | +4.9 | 2e-04 | 31/47 (NCI-H460, NCI-H1573, …) | rises with dose | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.34×** | +4.5 | 8e-04 | 29/47 (NCI-H460, SW 900, …) | two highest doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.29×** | +4.0 | 0.007 | 29/48 (J82, HOP62, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.8 | 0.011 | 30/47 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.27×** | +3.7 | 0.017 | 30/48 (hTERT-HPNE, HOP62, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.054 | 20/48 (CFPAC-1, MIA PaCa-2, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | 1.22× | +3.1 | 0.12 | 23/48 (RKO, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8566.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.395×** | -20.1 | 0e+00 | 47/48 (AsPC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.595×** | -7.9 | 6e-13 | 38/48 (LoVo, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.620×** | -7.0 | 4e-10 | 38/48 (AsPC-1, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.647×** | -6.7 | 4e-09 | 36/48 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.483×** | -5.8 | 6e-07 | 37/49 (A-427, AsPC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.505×** | -5.5 | 4e-06 | 38/48 (SW480, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.728×** | -4.9 | 9e-05 | 33/48 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.747×** | -4.5 | 6e-04 | 28/48 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.763×** | -4.1 | 0.002 | 26/48 (HepG2/C3A, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.780×** | -3.7 | 0.015 | 26/49 (HepG2/C3A, A-172, …) | top dose only |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.653×** | -3.5 | 0.029 | 27/48 (KATO III, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | **0.800×** | -3.4 | 0.031 | 26/48 (AN3 CA, SW48, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **0.810×** | -3.2 | 0.055 | 25/48 (PANC-1, SNU-1, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **0.815×** | -3.1 | 0.071 | 21/48 (NCI-H2347, A549, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8566. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 112 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.75× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -21.3) |
| [[A-172 (line)]] | wt | 197 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.88× (z +11.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -19.9) |
| [[A498 (line)]] | wt | 177 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +14.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.335× (z -18.2) |
| [[AsPC-1 (line)]] | alt | 188 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -24.5) |
| [[CFPAC-1 (line)]] | alt | 98.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.63× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -13.7) |
| [[HOP62 (line)]] | alt | 84.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +12.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -12.1) |
| [[J82 (line)]] | alt | 179 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.37× (z +14.1) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.454× (z -13.5) |
| [[KATO III (line)]] | alt | 116 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.47× (z +17.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -16.9) |
| [[LOX-IMVI (line)]] | wt | 79.6 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.91× (z +14.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.486× (z -11.0) |
| [[Panc 03.27 (line)]] | alt | 98.3 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.46× (z +13.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -17.1) |
| [[RPMI-7951 (line)]] | alt | 109 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.81× (z +12.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -10.9) |
| [[SW480 (line)]] | alt | 94.9 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.50× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -18.1) |
| [[A-427 (line)]] | wt | 168 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -21.9) |
| [[HepG2_C3A (line)]] | wt | 108 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -16.7) |
| [[Hs 766T (line)]] | wt | 251 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.97× (z +12.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.379× (z -16.1) |
| [[HS-578T (line)]] | alt | 102 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +12.2) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 111 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.46× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.463× (z -8.9) |
| [[LoVo (line)]] | wt | 146 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -20.8) |
| [[MIA PaCa-2 (line)]] | alt | 58.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.27× (z +11.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -10.4) |
| [[NCI-H1792 (line)]] | alt | 69.6 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.77× (z +15.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.453× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 101 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.80× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -12.5) |
| [[NCI-H460 (line)]] | wt | 114 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.71× (z +11.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -14.8) |
| [[PANC-1 (line)]] | alt | 106 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 2.91× (z +12.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.542× (z -10.4) |
| [[RKO (line)]] | wt | 95.6 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.64× (z +9.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -16.1) |
| [[SNU-423 (line)]] | alt | 76.2 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.08× (z +15.6) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 94.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.70× (z +17.2) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 89.2 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.11× (z +10.4) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -9.2) |
| [[C32 (line)]] | wt | 93.6 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.13× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -15.3) |
| [[H4 (line)]] | wt | 91.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.78× (z +9.3) ⚠ toxic; transcription drop | — |
| [[HCT15 (line)]] | alt | 68.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.13× (z +10.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -9.7) |
| [[HT-29 (line)]] | alt | 99.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.07× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.295× (z -16.5) |
| [[BT-474 (line)]] | alt | 49.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -10.2) |
| [[COLO 205 (line)]] | alt | 93.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.383× (z -11.5) |
| [[HEC-1-A (line)]] | alt | 92.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -15.4) |
| [[LS 180 (line)]] | wt | 147 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -13.8) |
| [[NCI-H1573 (line)]] | alt | 107 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.400× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 124 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.418× (z -13.5) |
| [[SHP-77 (line)]] | alt | 85.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +11.5) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 113 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.23× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 70.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -10.0) |
| [[SW 900 (line)]] | alt | 96.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -8.9) |
| [[SW1417 (line)]] | alt | 65.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -13.5) |
| [[AN3 CA (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 82.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 91.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 92.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 115 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 76.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 80.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8566), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD2]] | +0.65 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[PRDX1]] | +0.61 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[ACTR2]] | +0.59 | +0.57 / +0.62 | both halves | 8e-06 | same gene group; pathway: Clathrin-mediated endocytosis; STRING 999 |
| [[TPM3]] | +0.59 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[DSG2]] | +0.59 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[MAP1B]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[TMOD3]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ZNF731P]] | +0.56 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[YWHAQ]] | +0.56 | +0.57 / +0.46 | both halves | 3e-05 | pathway: RHO GTPase Effectors |
| [[TWF1]] | +0.55 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[RHOC]] | +0.54 | +0.51 / +0.54 | both halves | 1e-05 | pathway: RHO GTPase Effectors |
| [[RALB]] | +0.54 | +0.58 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YY1AP1]] | -0.66 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[PER1]] | -0.60 | -0.56 / -0.59 | both halves | 1e-05 |  |
| [[SAT2]] | -0.58 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[CPT1B]] | -0.57 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[ZNF316]] | -0.56 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[NSUN5P1-1]] | -0.56 | -0.56 / -0.57 | both halves | 1e-05 |  |
| [[NISCH]] | -0.55 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[SNHG8]] | -0.54 | -0.54 / -0.51 | both halves | 1e-05 |  |
| [[SETDB1]] | -0.54 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[NOP53]] | -0.54 | -0.52 / -0.50 | both halves | 1e-05 |  |
| [[VEGFB]] | -0.53 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[POLR1H]] | -0.52 | -0.51 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DYNLT3]] | C | DYNLT3 activity raises ARPC5's level | lines that do not express DYNLT3 (4) vs lines expressing it (46) | 1.82× lower at baseline in the lines without DYNLT3 | 0.022 | ⚠ few lines (4 vs 46); across organs; also absent: PLEKHA5, LRRCC1, RGL1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.512). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-21.2, -11.4); signed map (-7.3, 38.6). **Vector** length 106, 35.1% of its response variance represented; |z| ≥ 3 in 971 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +5.1 | +4.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.9 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | +1.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.2 | +4.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.6 | +0.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +3.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | +3.1 | +3.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.7 | +2.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.6 | -20.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.7 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.4 | -7.9 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -3.3 | -1.4 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.3 | -3.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -3.3 | +0.1 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.2 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | actin related protein 2/3 complex subunit 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:183,620,846-183,635,783 (-) |
| Ensembl biotype | protein_coding |
| Also known as | p16-Arc, ARC16, dJ127C7.3 |
| Gene groups (HGNC) | Actin related protein 2/3 complex subunits |
| Reactome | 20 pathways, smallest: RHO GTPases Activate WASPs and WAVEs; EPHB-mediated forward signaling; FCGR3A-mediated phagocytosis |
| Matched by | ensembl_id |

**Function**, from UniProt [O15511](https://www.uniprot.org/uniprotkb/O15511) (Actin-related protein 2/3 complex subunit 5):

> Component of the Arp2/3 complex, a multiprotein complex that mediates actin polymerization upon stimulation by nucleation-promoting factor (NPF). The Arp2/3 complex mediates the formation of branched actin networks in the cytoplasm, providing the force for cell motility. In addition to its role in the cytoplasmic cytoskeleton, the Arp2/3 complex also promotes actin polymerization in the nucleus, thereby regulating gene transcription and repair of damaged DNA. The Arp2/3 complex promotes …

**Summary**, from NCBI Gene [10092](https://www.ncbi.nlm.nih.gov/gene/10092):

> This gene encodes one of seven subunits of the human Arp2/3 protein complex. The Arp2/3 protein complex has been implicated in the control of actin polymerization in cells and has been conserved through evolution. The exact role of the protein encoded by this gene, the p16 subunit, has yet to be determined. Alternatively spliced transcript variants encoding different isoforms have been observed for this gene. [provided by RefSeq, Jul 2012]

**Accessions** — [HGNC:708](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:708) · Entrez [10092](https://www.ncbi.nlm.nih.gov/gene/10092) · UniProt [O15511](https://www.uniprot.org/uniprotkb/O15511) · Ensembl [ENSG00000162704](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162704)

## Data

Gene col 8566: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8566); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8566, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8566]; `tensor/DDL_lfc|DDL_z.npy` [8566]; `embed/gene_vectors.npy` [8566]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8566 or target_col == 8566). Every well: [[ARPC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARPC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
