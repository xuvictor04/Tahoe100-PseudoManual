---
symbol: "MAPKAP1"
type: "gene"
col: 4071
ensembl_id: "ENSG00000119487"
name: "MAPK associated protein 1"
location: "9q33.3"
module: 5
arm: "+"
pooled_cpm: 135.6
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# MAPKAP1

*MAPK associated protein 1* — 9q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.71× (z +11.1, q 7e-26, up in 35 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.41× (z +10.4, q 8e-23, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.818× (z -6.2, q 3e-07, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAT1]] (+0.74, fdr 7e-06), [[SNX19]] (+0.69, fdr 7e-06), [[DOCK1]] (+0.68, fdr 1e-05); moves opposite to [[PLEKHH3]] (-0.66, fdr 7e-06), [[KBTBD3]] (-0.62, fdr 3e-05), [[SIRT2]] (-0.62, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[CXXC5]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Docetaxel (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4071.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.71×** | +11.1 | 7e-26 | 35/44 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +10.4 | 8e-23 | 30/48 (A-172, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.24×** | +9.1 | 2e-17 | 38/49 (SW480, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.61×** | +9.0 | 4e-17 | 35/49 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +8.3 | 8e-15 | 36/48 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +7.4 | 2e-11 | 34/48 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +6.8 | 7e-10 | 27/45 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.83×** | +6.8 | 7e-10 | 38/48 (SW480, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.25×** | +6.6 | 2e-09 | 25/49 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.29×** | +5.2 | 1e-05 | 31/50 (LS 180, NCI-H460, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.24×** | +4.5 | 4e-04 | 25/47 (PANC-1, SW 900, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.16× | +4.4 | 6e-04 | 19/48 (A498, MIA PaCa-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +4.4 | 6e-04 | 23/48 (PANC-1, H4, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.21×** | +4.0 | 0.003 | 20/48 (A498, SNU-423, …) | top dose only |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.22×** | +3.9 | 0.003 | 22/47 (A-172, SW480, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.20× | +3.9 | 0.004 | 23/48 (SNU-423, CFPAC-1, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 1.19× | +3.7 | 0.007 | 16/48 (A-172, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 1.18× | +3.3 | 0.024 | 15/48 (SW480, COLO 205, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4071.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.818×** | -6.2 | 3e-07 | 25/48 (RKO, A-172, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.777×** | -5.3 | 4e-05 | 24/47 (RKO, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.797×** | -4.9 | 2e-04 | 28/49 (KATO III, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.806×** | -4.7 | 4e-04 | 24/48 (SW48, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.806×** | -4.5 | 7e-04 | 22/47 (J82, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~15% of this change | **0.820×** | -4.3 | 0.001 | 25/48 (A-172, NCI-H2030, …) | inconsistent across doses | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.789×** | -3.7 | 0.019 | 21/48 (HEC-1-A, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.853× | -3.5 | 0.037 | 18/48 (HEC-1-A, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4071. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 693 | 0 | 28 (11 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -19.3) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Radotinib (drug)]] 5 µM 0.311× (z -16.5) |
| [[NCI-H460 (line)]] | wt | 137 | 4 (1 ⚠) | 6 (6 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +16.4) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.380× (z -14.6) ⚠ cell-cycle shift, explains ~6% of this change |
| [[SW480 (line)]] | alt | 115 | 6 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.33× (z +12.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 3.69× (z +11.3) | [[Digitoxin (drug)]] 5 µM 0.551× (z -10.0) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 43.3 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +14.1) | — |
| [[J82 (line)]] | alt | 222 | 0 | 5 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.314× (z -14.0) ⚠ toxic |
| [[A-172 (line)]] | wt | 227 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.96× (z +20.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.643× (z -8.5) ⚠ cell-cycle shift, explains ~15% of this change |
| [[HOP62 (line)]] | alt | 99.1 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.76× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.75× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 112 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.28× (z +12.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.04× (z +11.2) | — |
| [[LS 180 (line)]] | wt | 102 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.20× (z +9.0) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +8.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 129 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.92× (z +11.8) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.48× (z +10.0) | — |
| [[NCI-H23 (line)]] | alt | 192 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.3) | [[Niclosamide (olamine) (drug)]] 5 µM 0.417× (z -10.5) ⚠ toxic |
| [[PANC-1 (line)]] | alt | 121 | 2 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.62× (z +11.7) | [[Digitoxin (drug)]] 5 µM 0.457× (z -13.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 107 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.134× (z -17.4) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 91.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.83× (z +10.4) | — |
| [[hTERT-HPNE (line)]] | wt | 100 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.24× (z +19.6) | — |
| [[KATO III (line)]] | alt | 121 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +9.0) | — |
| [[LoVo (line)]] | wt | 122 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 3.06× (z +8.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.502× (z -9.9) ⚠ toxic |
| [[LOX-IMVI (line)]] | wt | 459 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -13.1) ⚠ cell-cycle shift, explains ~15% of this change |
| [[NCI-H1573 (line)]] | alt | 96.9 | 0 | 2 (2 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.252× (z -9.3) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 101 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.97× (z +13.4) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 100 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.63× (z +8.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.424× (z -10.5) ⚠ toxic |
| [[A-427 (line)]] | wt | 110 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.13× (z +14.2) | — |
| [[A498 (line)]] | wt | 117 | 1 | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 2.11× (z +9.1) | — |
| [[C32 (line)]] | wt | 129 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -11.4) |
| [[COLO 205 (line)]] | alt | 92.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 7.57× (z +9.7) | — |
| [[Hs 766T (line)]] | wt | 111 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.74× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 85.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +16.4) | — |
| [[NCI-H2347 (line)]] | alt | 78.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.91× (z +8.8) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 90.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.40× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 74.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.388× (z -9.2) ⚠ toxic |
| [[A549 (line)]] | wt | 110 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 113 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 88.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 169 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 156 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 109 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 90.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 86.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 138 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 75.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 99.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 78.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 121 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 147 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 379 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 126 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4071), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*57 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAT1]] | +0.74 | +0.73 / +0.62 | both halves | 7e-06 |  |
| [[SNX19]] | +0.69 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[DOCK1]] | +0.68 | +0.49 / +0.77 | both halves | 1e-05 | pathway: Signaling by VEGF |
| [[CPSF2]] | +0.65 | +0.62 / +0.65 | both halves | 7e-06 | pathway: Dengue Virus-Host Interactions |
| [[CPSF3]] | +0.64 | +0.73 / +0.48 | both halves | 2e-05 | pathway: Dengue Virus-Host Interactions |
| [[ENOX2]] | +0.64 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[PARG]] | +0.64 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[TRIM44]] | +0.62 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[SRFBP1]] | +0.61 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[PRDM5]] | +0.61 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[DNAJC11]] | +0.61 | +0.65 / +0.51 | both halves | 1e-05 |  |
| [[ABCF2]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*43 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEKHH3]] | -0.66 | -0.62 / -0.65 | both halves | 7e-06 |  |
| [[KBTBD3]] | -0.62 | -0.45 / -0.60 | both halves | 3e-05 |  |
| [[SIRT2]] | -0.62 | -0.50 / -0.64 | both halves | 1e-05 |  |
| [[VPS37D]] | -0.61 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[KCTD7]] | -0.60 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[EFNA4]] | -0.59 | -0.58 / -0.51 | both halves | 1e-05 |  |
| [[ANKMY2]] | -0.59 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[AHDC1]] | -0.58 | -0.53 / -0.56 | both halves | 1e-05 |  |
| [[CBX4]] | -0.58 | -0.29 / -0.69 | both halves | 2e-04 | pathway: Intracellular signaling by second messengers |
| [[SUFU]] | -0.58 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[CNNM4]] | -0.57 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[LMBR1L]] | -0.57 | -0.56 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXXC5]] | B | CXXC5 activity strengthens MAPKAP1's drug response | lines that do not express CXXC5 (10) vs lines expressing it (39) | the lines without CXXC5 respond 0.53× as strongly (z diff +2.35); strongest at Dinaciclib 0.05 µM: 0.84x vs 1.44x (z diff +5.7) | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers MAPKAP1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[CXXC5]] | B | CXXC5 activity lowers MAPKAP1's level | lines that do not express CXXC5 (10) vs lines expressing it (40) | 1.44× higher at baseline in the lines without CXXC5 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000249526, LFNG; maybe low, not absent |
| [[ASAP1]] | C | ASAP1's natural level weakens MAPKAP1's drug response | ASAP1's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.64, reverse +0.07; direction not clear | 0.051 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Docetaxel (drug)]] 5 µM | C | MAPKAP1's natural level lowers the cells' numbers under Docetaxel 5 µM (makes them more sensitive) | MAPKAP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.67 | 0.308 over the table, 0.050 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.546). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-3.8, -34.2); signed map (-6.1, -39.5). **Vector** length 148, 48.0% of its response variance represented; |z| ≥ 3 in 1,243 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +7.8 | +9.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.8 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +9.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.4 | +11.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.8 | +4.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.0 | +6.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.6 | +3.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +5.3 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.2 | +3.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -9.4 | -6.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -7.6 | -4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -5.6 | -5.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.9 | -4.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.1 | -4.5 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -3.3 | -3.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -3.2 | -3.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -3.2 | -2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | MAPK associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q33.3 — chr9:125,437,393-125,707,234 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC2745, SIN1, MIP1 |
| Gene groups (HGNC) | MTOR complex 2 |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 25 pathways, smallest: Dengue virus modulates apoptosis; CD28 dependent PI3K/Akt signaling; Constitutive Signaling by AKT1 E17K in Cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BPZ7](https://www.uniprot.org/uniprotkb/Q9BPZ7) (Target of rapamycin complex 2 subunit MAPKAP1):

> Component of the mechanistic target of rapamycin complex 2 (mTORC2), which transduces signals from growth factors to pathways involved in proliferation, cytoskeletal organization, lipogenesis and anabolic output. In response to growth factors, mTORC2 phosphorylates and activates AGC protein kinase family members, including AKT (AKT1, AKT2 and AKT3), PKC (PRKCA, PRKCB and PRKCE) and SGK1. In contrast to mTORC1, mTORC2 is nutrient-insensitive. Within the mTORC2 complex, MAPKAP1/SIN1 acts as a …

**Summary**, from NCBI Gene [79109](https://www.ncbi.nlm.nih.gov/gene/79109):

> This gene encodes a protein that is highly similar to the yeast SIN1 protein, a stress-activated protein kinase. Alternatively spliced transcript variants encoding distinct isoforms have been described. Alternate polyadenylation sites as well as alternate 3' UTRs have been identified for transcripts of this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18752](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18752) · Entrez [79109](https://www.ncbi.nlm.nih.gov/gene/79109) · UniProt [Q9BPZ7](https://www.uniprot.org/uniprotkb/Q9BPZ7) · Ensembl [ENSG00000119487](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000119487)

## Data

Gene col 4071: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4071); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4071, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4071]; `tensor/DDL_lfc|DDL_z.npy` [4071]; `embed/gene_vectors.npy` [4071]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4071 or target_col == 4071). Every well: [[MAPKAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPKAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
