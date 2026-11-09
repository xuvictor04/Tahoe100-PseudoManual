---
symbol: "ICE2"
type: "gene"
col: 4931
ensembl_id: "ENSG00000128915"
name: "interactor of little elongation complex ELL subunit 2"
location: "15q22.2"
module: 1
arm: "+"
pooled_cpm: 76.66
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 20
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 0
direction_downstream: 1
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# ICE2

*interactor of little elongation complex ELL subunit 2* — 15q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.21× (z +6.4, q 1e-07, up in 26 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (11 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.427× (z -20.1, q 0e+00, down in 48 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.517× (z -15.6, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAGOHB]] (+0.75, fdr 7e-06), [[GTF2H3]] (+0.73, fdr 7e-06), [[RPL7L1]] (+0.71, fdr 7e-06); moves opposite to [[SEC11A]] (-0.66, fdr 1e-05), [[UBTD1]] (-0.65, fdr 1e-05), [[ATOX1]] (-0.63, fdr 2e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 1 goes from it, the strongest it → [[CPNE1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4931.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.21×** | +6.4 | 1e-07 | 26/48 (NCI-H2030, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +6.2 | 1e-07 | 25/48 (A-427, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.25×** | +5.2 | 3e-05 | 27/48 (CFPAC-1, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +4.1 | 0.007 | 17/48 (Panc 03.27, SW 900, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | 1.16× | +3.5 | 0.047 | 11/48 (NCI-H460, HEC-1-A, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | 1.09× | +3.1 | 0.18 | 13/48 (AsPC-1, J82, …) | top dose only | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | 1.14× | +3.1 | 0.18 | 11/48 (CFPAC-1, KATO III, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 14 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4931.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.427×** | -20.1 | 0e+00 | 48/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.517×** | -15.6 | 0e+00 | 44/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.533×** | -14.9 | 0e+00 | 42/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.662×** | -13.7 | 8e-41 | 40/49 (HEC-1-A, PANC-1, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.566×** | -13.4 | 6e-39 | 39/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.620×** | -10.8 | 2e-25 | 37/47 (PANC-1, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.687×** | -8.8 | 8e-17 | 35/48 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.698×** | -8.5 | 2e-15 | 35/48 (MIA PaCa-2, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.718×** | -7.8 | 4e-13 | 37/48 (PANC-1, C-33 A, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.759×** | -6.5 | 4e-09 | 30/48 (PANC-1, C-33 A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **0.767×** | -5.8 | 4e-07 | 24/45 (SNU-1, H4, …) | inconsistent across doses | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.783×** | -5.5 | 1e-06 | 27/50 (SNU-1, RPMI-7951, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.797×** | -5.3 | 4e-06 | 26/48 (LoVo, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.798×** | -5.3 | 4e-06 | 26/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.807×** | -5.1 | 2e-05 | 26/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.870× | -4.6 | 1e-04 | 18/48 (NCI-H460, PANC-1, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.694×** | -4.5 | 2e-04 | 26/49 (PANC-1, HepG2/C3A, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.729×** | -3.9 | 0.003 | 19/48 (C32, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.906× | -3.3 | 0.024 | 13/48 (RPMI-7951, HEC-1-A, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.884× | -2.9 | 0.086 | 12/48 (NCI-H2030, SW1417, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4931. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 81.9 | 0 | 8 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.328× (z -15.0) |
| [[PANC-1 (line)]] | alt | 126 | 0 | 8 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.163× (z -31.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.245× (z -24.3) |
| [[LoVo (line)]] | wt | 129 | 0 | 6 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.397× (z -11.7) |
| [[SNU-1 (line)]] | wt | 87.1 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -11.9) |
| [[SW480 (line)]] | alt | 86.3 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.315× (z -18.1) |
| [[HOP62 (line)]] | alt | 66.3 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.255× (z -16.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.347× (z -12.6) |
| [[KATO III (line)]] | alt | 82.4 | 1 | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.03× (z +9.5) | [[Digitoxin (drug)]] 5 µM 0.254× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.383× (z -12.7) |
| [[LOX-IMVI (line)]] | wt | 81.4 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.490× (z -13.0) |
| [[NCI-H1573 (line)]] | alt | 123 | 1 (1 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.04× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Digitoxin (drug)]] 5 µM 0.328× (z -13.8) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.459× (z -9.7) |
| [[AsPC-1 (line)]] | alt | 60.6 | 1 (1 ⚠) | 2 (1 ⚠) | [[Selinexor (drug)]] 5 µM 2.40× (z +11.2) ⚠ cell-cycle shift, explains ~88% of this change | [[Digitoxin (drug)]] 5 µM 0.153× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.226× (z -13.4) |
| [[H4 (line)]] | wt | 92.1 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.176× (z -14.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.275× (z -10.8) |
| [[HEC-1-A (line)]] | alt | 84.6 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.477× (z -14.8) |
| [[HepG2_C3A (line)]] | wt | 78.9 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.246× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.251× (z -11.9) |
| [[RKO (line)]] | wt | 69.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.179× (z -18.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 62.3 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.273× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.296× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 57.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0961× (z -24.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.489× (z -10.4) |
| [[A-427 (line)]] | wt | 62.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 2.44× (z +10.3) | [[Digitoxin (drug)]] 5 µM 0.402× (z -10.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 76.6 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.384× (z -9.3) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.544× (z -8.7) |
| [[BT-474 (line)]] | alt | 44.0 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.267× (z -10.5) |
| [[C-33 A (line)]] | alt | 134 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.568× (z -8.8) |
| [[HT-29 (line)]] | alt | 68.5 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.479× (z -8.8) |
| [[J82 (line)]] | alt | 66.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.396× (z -10.0) |
| [[LS 180 (line)]] | wt | 63.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.313× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.390× (z -10.1) |
| [[NCI-H2030 (line)]] | alt | 79.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +9.2) | [[Niclosamide (olamine) (drug)]] 5 µM 0.387× (z -9.8) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 77.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.434× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 64.0 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.246× (z -9.6) |
| [[A-172 (line)]] | wt | 55.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.569× (z -8.6) |
| [[COLO 205 (line)]] | alt | 87.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.397× (z -9.2) ⚠ toxic |
| [[HCT15 (line)]] | alt | 84.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.361× (z -8.9) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 65.8 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.412× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 69.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.390× (z -9.6) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 69.6 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -9.1) ⚠ cell-cycle shift, explains ~18% of this change |
| [[SNU-423 (line)]] | alt | 45.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.440× (z -8.5) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 69.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.305× (z -13.3) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 96.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 77.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 55.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 77.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 61.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 65.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 79.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 69.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4931), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAGOHB]] | +0.75 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[GTF2H3]] | +0.73 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[RPL7L1]] | +0.71 | +0.76 / +0.61 | both halves | 7e-06 |  |
| [[NOL8]] | +0.71 | +0.76 / +0.65 | both halves | 7e-06 |  |
| [[GUF1]] | +0.70 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[MTIF2]] | +0.70 | +0.75 / +0.58 | both halves | 7e-06 |  |
| [[RAD50]] | +0.70 | +0.78 / +0.56 | both halves | 1e-05 |  |
| [[TRMT13]] | +0.70 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[NEK9]] | +0.70 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[COX18]] | +0.70 | +0.78 / +0.54 | both halves | 1e-05 |  |
| [[LZIC]] | +0.69 | +0.75 / +0.56 | both halves | 1e-05 |  |
| [[PYM1]] | +0.68 | +0.66 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEC11A]] | -0.66 | -0.69 / -0.55 | both halves | 1e-05 |  |
| [[UBTD1]] | -0.65 | -0.64 / -0.57 | both halves | 1e-05 |  |
| [[ATOX1]] | -0.63 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[GNB2]] | -0.63 | -0.67 / -0.44 | both halves | 3e-05 |  |
| [[SNN]] | -0.62 | -0.65 / -0.36 | both halves | 1e-04 |  |
| [[TRIM62]] | -0.62 | -0.56 / -0.52 | both halves | 1e-05 |  |
| [[STRN]] | -0.62 | -0.72 / -0.40 | both halves | 5e-05 |  |
| [[GTF2IP4]] | -0.62 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[LMTK2]] | -0.61 | -0.62 / -0.44 | both halves | 3e-05 |  |
| [[IGSF8]] | -0.61 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[NPTN]] | -0.61 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[HDAC3]] | -0.60 | -0.60 / -0.53 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CPNE1]] | C | ICE2's natural level strengthens CPNE1's drug response | ICE2's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.65, reverse -0.09; direction not clear | 0.045 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.682). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-22.5, 7.3); signed map (10.1, -28.5). **Vector** length 102, 27.2% of its response variance represented; |z| ≥ 3 in 1,106 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +10.2 | +6.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +8.0 | +6.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.1 | +2.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +6.9 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +6.0 | +4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +1.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +0.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +3.5 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | +1.9 | +1.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.1 | -13.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.5 | -4.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.5 | -20.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.1 | -3.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | -4.4 | -5.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.9 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -1.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.2 | -0.5 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | interactor of little elongation complex ELL subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.2 — chr15:60,419,609-60,479,160 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11896, BRCC1; previously NARG2 |
| Reactome | 1 pathways, smallest: RNA polymerase II transcribes snRNA genes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q659A1](https://www.uniprot.org/uniprotkb/Q659A1) (Little elongation complex subunit 2):

> Component of the little elongation complex (LEC), a complex required to regulate small nuclear RNA (snRNA) gene transcription by RNA polymerase II and III.

**Summary**, from NCBI Gene [79664](https://www.ncbi.nlm.nih.gov/gene/79664):

> This gene encodes a protein component of the little elongation complex (LEC), which plays a role in small nuclear RNA (snRNA) transcription. The LEC regulates snRNA transcription by enhancing both RNA Polymerase II occupancy and transcriptional elongation. The encoded protein and other LEC components have been shown to localize to Cajal bodies, which are sites of ribonucleoprotein (RNP) complex assembly. Pseudogenes of this gene have been identified on chromosomes 3 and 4. [provided by RefSeq, …

**Accessions** — [HGNC:29885](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29885) · Entrez [79664](https://www.ncbi.nlm.nih.gov/gene/79664) · UniProt [Q659A1](https://www.uniprot.org/uniprotkb/Q659A1) · Ensembl [ENSG00000128915](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128915)

## Data

Gene col 4931: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4931); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4931, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4931]; `tensor/DDL_lfc|DDL_z.npy` [4931]; `embed/gene_vectors.npy` [4931]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4931 or target_col == 4931). Every well: [[ICE2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ICE2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
