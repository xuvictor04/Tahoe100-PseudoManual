---
symbol: "COX10-DT"
type: "gene"
col: 14060
ensembl_id: "ENSG00000236088"
name: "COX10 divergent transcript"
location: "17p12"
module: 18
arm: "+"
pooled_cpm: 31.76
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 19
n_dd_up_clean: 20
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# COX10-DT

*COX10 divergent transcript* — 17p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.17× (z +17.9, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.601× (z -8.3, q 4e-14, down in 31 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.672× (z -6.5, q 9e-09, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF749]] (+0.65, fdr 5e-05), [[RFT1]] (+0.57, fdr 2e-05), [[METTL3]] (+0.56, fdr 6e-05); moves opposite to [[WBP2]] (-0.58, fdr 3e-05), [[TBC1D17]] (-0.50, fdr 4e-05), [[PNPLA2]] (-0.49, fdr 7e-04).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14060.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.17×** | +17.9 | 0e+00 | 42/48 (LS 180, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **2.30×** | +13.7 | 4e-40 | 46/48 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.06×** | +11.8 | 4e-30 | 40/48 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.91×** | +10.6 | 3e-24 | 43/48 (HOP62, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.85×** | +9.7 | 4e-20 | 30/46 (NCI-H2030, HT-29, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.77×** | +9.4 | 7e-19 | 33/48 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.44×** | +8.4 | 3e-15 | 30/48 (SW 900, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.67×** | +8.1 | 5e-14 | 33/48 (HS-578T, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.39×** | +7.6 | 2e-12 | 31/48 (NCI-H23, A-427, …) | rises with dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.52×** | +6.8 | 5e-10 | 35/48 (HS-578T, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.7 | 5e-07 | 27/48 (HOP62, SNU-423, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.35×** | +4.9 | 4e-05 | 22/48 (NCI-H460, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +4.8 | 7e-05 | 19/48 (NCI-H23, SW480, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.29×** | +4.2 | 0.001 | 13/48 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.61×** | +4.1 | 0.002 | 14/48 (SW480, SW 900, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.25×** | +3.7 | 0.008 | 16/48 (SW480, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.25×** | +3.6 | 0.010 | 9/48 (C-33 A, SW 900, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.25×** | +3.5 | 0.014 | 13/47 (SW480, A549, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.22×** | +3.2 | 0.034 | 7/48 (SHP-77, C-33 A, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.22×** | +3.2 | 0.035 | 14/48 (NCI-H1573, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14060.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.601×** | -8.3 | 4e-14 | 31/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.627×** | -7.7 | 5e-12 | 33/48 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.730×** | -7.3 | 5e-11 | 29/47 (A498, PANC-1, …) | top dose only | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **0.630×** | -7.3 | 5e-11 | 26/48 (PANC-1, A498, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.672×** | -6.5 | 9e-09 | 29/48 (H4, COLO 205, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.680×** | -6.3 | 3e-08 | 27/48 (H4, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.498×** | -6.0 | 2e-07 | 26/48 (NCI-H23, MIA PaCa-2, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.703×** | -5.8 | 5e-07 | 25/48 (NCI-H460, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.700×** | -5.6 | 1e-06 | 25/47 (C32, H4, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.700×** | -5.5 | 2e-06 | 27/48 (SW480, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.732×** | -5.1 | 2e-05 | 22/48 (H4, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.768×** | -4.3 | 7e-04 | 21/48 (H4, NCI-H460, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.605×** | -4.3 | 7e-04 | 17/48 (LOX-IMVI, NCI-H23, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **0.625×** | -4.0 | 0.002 | 14/47 (C32, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.788×** | -3.9 | 0.004 | 14/47 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.821×** | -3.2 | 0.038 | 7/48 (NCI-H460, SHP-77, …) | rises with dose |  |
| [[Cyclosporin A (drug)]] 0.05 µM |  | **0.833×** | -3.0 | 0.082 | 7/48 (AsPC-1, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.46 per unit of S-phase module lfc, -0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14060. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 39.6 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.37× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.249× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[HOP62 (line)]] | alt | 24.2 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +12.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 49.5 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.102× (z -8.5) |
| [[PANC-1 (line)]] | alt | 22.0 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.35× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -13.2) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 110 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[A498 (line)]] | wt | 43.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -14.5) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 25.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +9.9) | [[Harringtonine (drug)]] 0.5 µM 0.274× (z -9.0) ⚠ cell-cycle shift, explains ~52% of this change |
| [[Hs 766T (line)]] | wt | 13.2 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +11.7) | [[Ritonavir (drug)]] 0.5 µM 0.187× (z -8.8) |
| [[HS-578T (line)]] | alt | 25.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.22× (z +11.5) | — |
| [[NCI-H23 (line)]] | alt | 72.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.145× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 50.8 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.320× (z -9.5) ⚠ cell-cycle shift, explains ~52% of this change |
| [[SW 900 (line)]] | alt | 26.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +11.1) | [[Docetaxel (drug)]] 0.05 µM 0.176× (z -10.8) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 11.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.55× (z +8.7) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[C32 (line)]] | wt | 28.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.244× (z -8.7) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 33.0 | 0 | 1 | — | [[18β-Glycyrrhetinic acid (drug)]] 0.5 µM 0.0926× (z -9.5) |
| [[H4 (line)]] | wt | 47.7 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.275× (z -8.6) |
| [[HCT15 (line)]] | alt | 27.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.19× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 9.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.14× (z +8.6) | — |
| [[KATO III (line)]] | alt | 25.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +9.2) | — |
| [[LoVo (line)]] | wt | 19.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 18.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +13.7) | — |
| [[NCI-H1573 (line)]] | alt | 21.2 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.04× (z +10.1) ⚠ cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H1792 (line)]] | alt | 9.01 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.05× (z +9.0) | — |
| [[NCI-H2030 (line)]] | alt | 10.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +9.0) | — |
| [[RKO (line)]] | wt | 26.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -9.9) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 156 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.302× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change |
| [[SNU-423 (line)]] | alt | 13.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +10.0) | — |
| [[SW 1271 (line)]] | alt | 50.5 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.5 µM 0.0617× (z -9.5) |
| [[SW1417 (line)]] | alt | 11.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.56× (z +10.4) | — |
| [[SW480 (line)]] | alt | 38.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.81× (z +8.9) | — |
| [[A-427 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 50.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 67.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 40.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14060), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF749]] | +0.65 | +0.39 / +0.61 | both halves | 5e-05 |  |
| [[RFT1]] | +0.57 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[METTL3]] | +0.56 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[ADAT2]] | +0.55 | +0.38 / +0.60 | both halves | 6e-05 |  |
| [[TIPIN]] | +0.55 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[DIDO1]] | +0.55 | +0.26 / +0.43 | both halves | 4e-04 |  |
| [[FAM120C]] | +0.54 | +0.50 / +0.46 | both halves | 3e-05 |  |
| [[SDHAF4]] | +0.54 | +0.49 / +0.48 | both halves | 2e-05 |  |
| [[ANAPC1]] | +0.54 | +0.56 / +0.48 | both halves | 2e-05 |  |
| [[CTTN-DT]] | +0.53 | +0.41 / +0.55 | both halves | 4e-05 | same gene group |
| [[STARD7-AS1]] | +0.53 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[ENTPD1-AS1]] | +0.53 | +0.58 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WBP2]] | -0.58 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[TBC1D17]] | -0.50 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[PNPLA2]] | -0.49 | -0.21 / -0.46 | both halves | 7e-04 |  |
| [[SKAP2]] | -0.48 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[CHP1]] | -0.48 | -0.52 / -0.37 | both halves | 8e-05 |  |
| [[TTBK2]] | -0.47 | -0.33 / -0.27 | both halves | 3e-04 |  |
| [[WDTC1]] | -0.46 | -0.43 / -0.42 | both halves | 4e-05 |  |
| [[KIAA1522]] | -0.45 | -0.46 / -0.37 | both halves | 7e-05 |  |
| [[GOLGB1]] | -0.44 | -0.19 / -0.53 | ⚠ one half (not replicated) | 9e-04 |  |
| [[GKAP1]] | -0.44 | -0.19 / -0.27 | ⚠ not reproduced | 8e-04 |  |
| [[JUND]] | -0.44 | -0.18 / -0.36 | ⚠ not reproduced | 1e-03 |  |
| [[ZSWIM4]] | -0.44 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[RB1CC1]] | -0.44 | -0.37 / -0.44 | both halves | 9e-05 |  |
| [[DDAH2]] | -0.44 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[HDAC5]] | -0.44 | -0.35 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers COX10-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.421). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-11.8, -31.2); signed map (-2.6, -52.0). **Vector** length 76.6, 16.4% of its response variance represented; |z| ≥ 3 in 1,167 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.3 | +9.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.3 | +4.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.4 | +2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | +3.3 | +9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +17.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.3 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.1 | +5.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.9 | +2.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -5.4 | -7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.9 | -7.3 |
|  | [[Entrectinib (drug)]] 5 µM |  | -2.3 | -1.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | +0.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.1 | -5.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.7 | -1.8 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.4 | -1.6 |
|  | [[crizotinib (drug)]] 5 µM |  | -1.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | COX10 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 17p12 — chr17:13,755,574-14,069,495 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously COX10AS, COX10-AS, COX10-AS1 |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:38873](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:38873) · Entrez [100874058](https://www.ncbi.nlm.nih.gov/gene/100874058) · Ensembl [ENSG00000236088](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000236088)

## Data

Gene col 14060: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14060); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14060, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14060]; `tensor/DDL_lfc|DDL_z.npy` [14060]; `embed/gene_vectors.npy` [14060]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14060 or target_col == 14060). Every well: [[COX10-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COX10-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
