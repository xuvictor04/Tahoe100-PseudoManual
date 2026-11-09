---
symbol: "WASHC4"
type: "gene"
col: 5806
ensembl_id: "ENSG00000136051"
name: "WASH complex subunit 4"
location: "12q23.3"
module: 11
arm: "+"
pooled_cpm: 140.21
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 12
n_dd_up_clean: 11
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/011"]
generated_by: "tahoemap"
---

# WASHC4

*WASH complex subunit 4* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.83× (z +17.8, q 0e+00, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.592× (z -9.3, q 7e-18, down in 36 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.513× (z -6.5, q 9e-09, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB3GAP2]] (+0.63, fdr 7e-06), [[GRINA]] (+0.61, fdr 7e-06), [[DMTF1]] (+0.61, fdr 9e-06); moves opposite to [[ZNF668]] (-0.59, fdr 1e-05), [[FBXW11]] (-0.58, fdr 1e-05), [[PHTF1]] (-0.55, fdr 1e-05).
> It sits in the **+** arm of [[Module 011]] (Mitochondrial translation elongation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5806.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.83×** | +17.8 | 0e+00 | 43/48 (NCI-H460, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +11.8 | 7e-30 | 45/48 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.65×** | +10.4 | 5e-23 | 43/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.58×** | +9.2 | 4e-18 | 40/48 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.44×** | +7.7 | 2e-12 | 39/48 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.42×** | +7.3 | 2e-11 | 37/48 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +6.1 | 8e-08 | 29/48 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.30×** | +5.5 | 2e-06 | 31/48 (HT-29, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 1.16× | +4.4 | 7e-04 | 16/48 (C32, A498, …) | all doses, flat | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **1.52×** | +4.1 | 0.003 | 35/49 (SW480, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.20× | +3.8 | 0.009 | 22/49 (A-172, NCI-H460, …) | all doses, flat |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | 1.19× | +3.7 | 0.010 | 19/48 (NCI-H460, H4, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.016 | 23/49 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.076 | 18/48 (HT-29, AsPC-1, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.076 | 15/50 (NCI-H460, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5806.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.592×** | -9.3 | 7e-18 | 36/45 (SHP-77, A-172, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.683×** | -7.7 | 5e-12 | 30/44 (LS 180, NCI-H1573, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.728×** | -6.7 | 5e-09 | 29/49 (LoVo, A-172, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.513×** | -6.5 | 9e-09 | 39/49 (PANC-1, AsPC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.733×** | -6.5 | 9e-09 | 29/48 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.801×** | -4.6 | 3e-04 | 27/48 (CFPAC-1, COLO 205, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.801×** | -4.5 | 6e-04 | 26/47 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.818×** | -4.2 | 0.002 | 26/48 (CFPAC-1, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.654×** | -4.2 | 0.002 | 28/48 (SK-MEL-2, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~38% of this change | **0.821×** | -4.1 | 0.002 | 26/48 (hTERT-HPNE, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | 0.880× | -3.8 | 0.007 | 8/48 (PANC-1, HS-578T, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.843× | -3.4 | 0.033 | 23/48 (NCI-H2347, SK-MEL-2, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **0.830×** | -3.3 | 0.039 | 20/48 (SW 1088, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.720×** | -3.2 | 0.050 | 18/38 (LOX-IMVI, NCI-H1573, …) | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | 0.853× | -3.2 | 0.050 | 19/47 (SNU-423, A-172, …) | inconsistent across doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.898× | -3.2 | 0.050 | 2/49 (Hs 766T, LS 180) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5806. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 153 | 5 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +13.0) | [[Dinaciclib (drug)]] 0.5 µM 0.361× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[AsPC-1 (line)]] | alt | 199 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.80× (z +20.5) | [[Dinaciclib (drug)]] 0.05 µM 0.462× (z -9.3) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 125 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.36× (z +18.5) | — |
| [[HT-29 (line)]] | alt | 123 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +22.0) | — |
| [[NCI-H460 (line)]] | wt | 153 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.35× (z +27.7) | [[Dinaciclib (drug)]] 0.05 µM 0.511× (z -9.3) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 154 | 4 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +18.6) | [[Dinaciclib (drug)]] 0.5 µM 0.340× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[SNU-423 (line)]] | alt | 194 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.340× (z -11.5) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.412× (z -11.1) |
| [[HEC-1-A (line)]] | alt | 159 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +17.4) | [[Dinaciclib (drug)]] 0.05 µM 0.479× (z -8.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 107 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.04× (z +12.8) | — |
| [[LS 180 (line)]] | wt | 114 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.32× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.244× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[SHP-77 (line)]] | alt | 84.1 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 2.80× (z +12.0) | [[Dinaciclib (drug)]] 0.05 µM 0.255× (z -13.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 109 | 2 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +8.7) | [[Auranofin (drug)]] 5 µM 0.424× (z -10.5) |
| [[A-172 (line)]] | wt | 183 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.322× (z -12.6) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 145 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +14.4) | — |
| [[CFPAC-1 (line)]] | alt | 141 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.66× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.473× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change |
| [[COLO 205 (line)]] | alt | 109 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +16.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 187 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.380× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.443× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 121 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +14.1) | [[Dinaciclib (drug)]] 5 µM 0.416× (z -10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H2347 (line)]] | alt | 152 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +14.5) | — |
| [[Panc 03.27 (line)]] | alt | 109 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +17.7) | — |
| [[PANC-1 (line)]] | alt | 142 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +15.6) | [[Dinaciclib (drug)]] 0.05 µM 0.515× (z -8.8) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 119 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +13.4) | [[Dinaciclib (drug)]] 0.05 µM 0.485× (z -8.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 163 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.58× (z +8.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.527× (z -12.3) ⚠ cell-cycle shift, explains ~15% of this change |
| [[HOP62 (line)]] | alt | 130 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +11.3) | [[Auranofin (drug)]] 5 µM 0.499× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 154 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +10.9) | — |
| [[A-427 (line)]] | wt | 107 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.67× (z +11.9) | — |
| [[AN3 CA (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.208× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[BT-474 (line)]] | alt | 101 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.1) | — |
| [[C32 (line)]] | wt | 103 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.73× (z +8.7) | — |
| [[HCT15 (line)]] | alt | 175 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.80× (z +9.2) | — |
| [[Hs 766T (line)]] | wt | 140 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.27× (z +13.4) | — |
| [[J82 (line)]] | alt | 145 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.82× (z +11.3) | — |
| [[LOX-IMVI (line)]] | wt | 185 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.70× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 98.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.84× (z +10.2) | — |
| [[SNU-1 (line)]] | wt | 130 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.97× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 119 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.76× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 102 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 136 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 115 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 143 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 174 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 135 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 188 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 111 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 103 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5806), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB3GAP2]] | +0.63 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[GRINA]] | +0.61 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[DMTF1]] | +0.61 | +0.57 / +0.65 | both halves | 9e-06 |  |
| [[KIDINS220]] | +0.60 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[MOSPD2]] | +0.59 | +0.69 / +0.45 | both halves | 3e-05 |  |
| [[FNTA]] | +0.59 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[PKN2]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[ZC2HC1A]] | +0.56 | +0.63 / +0.52 | both halves | 1e-05 |  |
| [[SPG11]] | +0.54 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[VPS13C]] | +0.54 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[VPS8]] | +0.54 | +0.54 / +0.51 | both halves | 1e-05 |  |
| [[LRCH3]] | +0.54 | +0.64 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF668]] | -0.59 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[FBXW11]] | -0.58 | -0.59 / -0.54 | both halves | 1e-05 |  |
| [[PHTF1]] | -0.55 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[TRAPPC10]] | -0.54 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[CHUK]] | -0.53 | -0.60 / -0.40 | both halves | 5e-05 |  |
| [[MCM9]] | -0.53 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[SFXN5]] | -0.52 | -0.45 / -0.54 | both halves | 3e-05 |  |
| [[ZNF410]] | -0.52 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[SCD5]] | -0.51 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[BEND3]] | -0.50 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[SNRPA]] | -0.50 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[TMEM248]] | -0.50 | -0.55 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 011]] — Mitochondrial translation elongation; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.259). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (0.2, -33.6); signed map (6.1, -11.0). **Vector** length 113, 36.8% of its response variance represented; |z| ≥ 3 in 1,042 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +7.8 | +6.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.8 | +11.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.0 | +9.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | +4.4 | +5.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.6 | +2.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.5 | +2.0 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +2.4 | +1.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.1 | +1.4 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -7.8 | -6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | -7.7 | -2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -7.1 | -6.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.6 | -9.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.2 | -4.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.4 | -4.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.6 | -0.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -3.6 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | WASH complex subunit 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.3 — chr12:105,107,324-105,169,130 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SWIP; previously KIAA1033 |
| Gene groups (HGNC) | WASH complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q2M389](https://www.uniprot.org/uniprotkb/Q2M389) (WASH complex subunit 4):

> Acts as a component of the WASH core complex that functions as a nucleation-promoting factor (NPF) at the surface of endosomes, where it recruits and activates the Arp2/3 complex to induce actin polymerization, playing a key role in the fission of tubules that serve as transport intermediates during endosome sorting.

**Summary**, from NCBI Gene [23325](https://www.ncbi.nlm.nih.gov/gene/23325):

> This gene encodes a component of the WASH complex, which functions in the intracellular transport of endosomes. Mutations in this gene have been detected in individuals with autosomal recessive cognitive disability. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Jun 2014]

**Accessions** — [HGNC:29174](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29174) · Entrez [23325](https://www.ncbi.nlm.nih.gov/gene/23325) · UniProt [Q2M389](https://www.uniprot.org/uniprotkb/Q2M389) · Ensembl [ENSG00000136051](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136051)

## Data

Gene col 5806: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5806); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5806, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5806]; `tensor/DDL_lfc|DDL_z.npy` [5806]; `embed/gene_vectors.npy` [5806]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5806 or target_col == 5806). Every well: [[WASHC4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WASHC4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
