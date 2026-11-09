---
symbol: "SUZ12"
type: "gene"
col: 10947
ensembl_id: "ENSG00000178691"
name: "SUZ12 polycomb repressive complex 2 subunit"
location: "17q11.2"
module: 91
arm: "+"
pooled_cpm: 136.6
n_lines_expressing: 50
n_dd_up: 21
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/091"]
generated_by: "tahoemap"
---

# SUZ12

*SUZ12 polycomb repressive complex 2 subunit* — 17q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.13× (z +28.5, q 0e+00, up in 46 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C-33 A 0.362×, NCI-H1573 0.409×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Phenytoin (sodium) (drug)]] 5 µM in 1 line (SW 1088 0.0748×); [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.679×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTDSPL2]] (+0.59, fdr 3e-05), [[FAM111A]] (+0.55, fdr 1e-05), [[PHIP]] (+0.54, fdr 2e-05); moves opposite to [[TPD52L2]] (-0.52, fdr 3e-05), [[GPSM1]] (-0.50, fdr 3e-05), [[BLCAP]] (-0.49, fdr 5e-05).
> It is in [[Module 091]], a single-armed module (HDR through Homologous Recombination (HRR)).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[E2F8]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 22 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10947.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.13×** | +28.5 | 0e+00 | 46/48 (PANC-1, A549, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.96×** | +18.0 | 0e+00 | 44/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.98×** | +17.5 | 0e+00 | 47/48 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.80×** | +15.8 | 0e+00 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +11.8 | 6e-30 | 40/48 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.27×** | +11.4 | 3e-28 | 46/49 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.52×** | +10.7 | 6e-25 | 44/47 (NCI-H460, LoVo, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.47×** | +10.3 | 8e-23 | 40/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~95% of this change | **1.36×** | +8.2 | 2e-14 | 30/49 (SW480, NCI-H1792, …) | two highest doses | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.34×** | +7.7 | 5e-13 | 35/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.74×** | +7.7 | 7e-13 | 30/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.34×** | +7.5 | 2e-12 | 31/50 (SW1417, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.33×** | +7.2 | 2e-11 | 31/48 (SW48, MIA PaCa-2, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | 1.19× | +6.5 | 3e-09 | 25/49 (AsPC-1, NCI-H2347, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.27×** | +6.4 | 4e-09 | 31/48 (CFPAC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sonidegib (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.007 | 18/48 (HCT15, COLO 205, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | 1.14× | +3.6 | 0.008 | 7/49 (HOP62, SNU-423, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.021 | 19/48 (A498, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.12× | +3.1 | 0.036 | 16/48 (CFPAC-1, HCT15, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.036 | 11/48 (NCI-H460, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Elagolix sodium (drug)]] 5 µM |  | 1.08× | +2.9 | 0.069 | 0/48 | rises with dose |  |
| [[Riluzole hydrochloride (drug)]] 5 µM |  | 1.08× | +2.8 | 0.078 | 0/49 | top dose only | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | 1.11× | +2.8 | 0.090 | 6/48 (J82, A-427, …) | top dose only | position effect removed |
| [[Berbamine (drug)]] 5 µM |  | 1.08× | +2.8 | 0.090 | 1/49 (RPMI-7951) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10947.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C-33 A 0.362×, NCI-H1573 0.409×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change); [[Phenytoin (sodium) (drug)]] 5 µM in 1 line (SW 1088 0.0748×); [[Selinexor (drug)]] 5 µM in 1 line (A-427 0.679×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.917× | -7.8 | 3e-12 | 0/50 | inconsistent across doses |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.865× | -3.7 | 0.051 | 11/48 (SW480, COLO 205, …) | rises with dose |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 0.876× | -3.4 | 0.11 | 9/49 (HT-29, CHP-212, …) | top dose only | plate-row cell shift |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~68% of this change | 0.875× | -3.4 | 0.11 | 6/48 (A498, COLO 205, …) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~64% of this change | 0.844× | -3.2 | 0.13 | 8/48 (MIA PaCa-2, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Posaconazole (drug)]] 5 µM |  | 0.883× | -3.2 | 0.13 | 9/48 (HT-29, HOP62, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10947. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 132 | 13 (8 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +24.8) | — |
| [[SW480 (line)]] | alt | 140 | 10 (6 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.43× (z +17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.72× (z +13.2) | — |
| [[PANC-1 (line)]] | alt | 176 | 8 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.69× (z +34.3) | — |
| [[HEC-1-A (line)]] | alt | 215 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.30× (z +21.4) | — |
| [[HOP62 (line)]] | alt | 136 | 6 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.76× (z +13.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.89× (z +11.6) | — |
| [[A549 (line)]] | wt | 142 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.80× (z +27.0) | — |
| [[J82 (line)]] | alt | 163 | 5 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.66× (z +20.9) | — |
| [[LOX-IMVI (line)]] | wt | 122 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.96× (z +14.3) | — |
| [[NCI-H1573 (line)]] | alt | 106 | 4 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +13.5) | [[Dinaciclib (drug)]] 0.05 µM 0.409× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 99.2 | 5 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 2.92× (z +11.5) | — |
| [[A-172 (line)]] | wt | 200 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +20.8) | — |
| [[C32 (line)]] | wt | 110 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +20.5) | — |
| [[HT-29 (line)]] | alt | 224 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +16.9) | — |
| [[SW48 (line)]] | wt | 146 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +11.6) | — |
| [[A498 (line)]] | wt | 115 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +18.5) | — |
| [[Hs 766T (line)]] | wt | 93.6 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.14× (z +11.3) | — |
| [[KATO III (line)]] | alt | 166 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +12.9) | — |
| [[LoVo (line)]] | wt | 110 | 3 (3 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.40× (z +10.8) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H23 (line)]] | alt | 168 | 3 (2 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.33× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 2.02× (z +9.2) | — |
| [[NCI-H2347 (line)]] | alt | 134 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.51× (z +21.3) | — |
| [[SNU-423 (line)]] | alt | 126 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.92× (z +17.2) | — |
| [[AsPC-1 (line)]] | alt | 70.8 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +17.1) | — |
| [[CFPAC-1 (line)]] | alt | 74.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +18.4) | — |
| [[COLO 205 (line)]] | alt | 112 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.54× (z +9.6) ⚠ toxic; cell-cycle shift, explains ~33% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 4.59× (z +8.6) | — |
| [[H4 (line)]] | wt | 80.6 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +10.5) | — |
| [[HS-578T (line)]] | alt | 99.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +14.9) | — |
| [[hTERT-HPNE (line)]] | wt | 87.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +12.9) | — |
| [[LS 180 (line)]] | wt | 116 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.47× (z +12.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 1.79× (z +11.1) | — |
| [[Panc 03.27 (line)]] | alt | 158 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +10.9) | — |
| [[RPMI-7951 (line)]] | alt | 95.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.25× (z +12.2) | — |
| [[SK-MEL-2 (line)]] | alt | 114 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +15.3) | — |
| [[SW 900 (line)]] | alt | 93.4 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.27× (z +9.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A-427 (line)]] | wt | 229 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 1.79× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | — |
| [[BT-474 (line)]] | alt | 129 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.77× (z +10.8) | — |
| [[C-33 A (line)]] | alt | 168 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.362× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HepG2_C3A (line)]] | wt | 77.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.48× (z +12.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 129 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 2.07× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 120 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +22.7) | — |
| [[RKO (line)]] | wt | 175 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +20.1) | — |
| [[SHP-77 (line)]] | alt | 120 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 2.09× (z +9.1) ⚠ toxic; cell-cycle shift, explains ~33% of this change | — |
| [[SNU-1 (line)]] | wt | 163 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.17× (z +8.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SW 1088 (line)]] | alt | 87.5 | 0 | 1 | — | [[Phenytoin (sodium) (drug)]] 5 µM 0.0748× (z -10.0) |
| [[SW1417 (line)]] | alt | 131 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.81× (z +13.8) | — |
| [[AN3 CA (line)]] | alt | 147 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 154 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10947), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTDSPL2]] | +0.59 | +0.44 / +0.60 | both halves | 3e-05 |  |
| [[FAM111A]] | +0.55 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[PHIP]] | +0.54 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[PCM1]] | +0.54 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[SMCHD1]] | +0.53 | +0.44 / +0.59 | both halves | 3e-05 | STRING 414 |
| [[CASP8AP2]] | +0.53 | +0.57 / +0.50 | both halves | 1e-05 | pathway: SUMO E3 ligases SUMOylate target proteins |
| [[LSM14A]] | +0.52 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[SCAF11]] | +0.52 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[ANKRD26]] | +0.52 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[USP1]] | +0.51 | +0.44 / +0.53 | both halves | 3e-05 |  |
| [[ZNF638]] | +0.51 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[NUCKS1]] | +0.50 | +0.55 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPD52L2]] | -0.52 | -0.59 / -0.46 | both halves | 3e-05 |  |
| [[GPSM1]] | -0.50 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[BLCAP]] | -0.49 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[LINC01399]] | -0.48 | -0.40 / -0.41 | both halves | 5e-05 |  |
| [[ST6GALNAC6]] | -0.47 | -0.53 / -0.39 | both halves | 6e-05 |  |
| [[YKT6]] | -0.46 | -0.49 / -0.39 | both halves | 5e-05 |  |
| [[FAM131A]] | -0.45 | -0.40 / -0.40 | both halves | 5e-05 |  |
| [[SNHG21]] | -0.45 | -0.39 / -0.43 | both halves | 5e-05 |  |
| [[ZNF275]] | -0.44 | -0.45 / -0.42 | both halves | 4e-05 | same gene group |
| [[PIP5KL1]] | -0.44 | -0.36 / -0.41 | both halves | 1e-04 |  |
| [[SLC39A13]] | -0.44 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[PDE2A]] | -0.44 | -0.37 / -0.45 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[E2F8]] | B | E2F8 activity raises SUZ12's level | lines that do not express E2F8 (5) vs lines expressing it (45) | 1.50× lower at baseline in the lines without E2F8 | 0.070 | ⚠ across organs; also absent: CYB561, NMRAL1, RRM2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 091]] — HDR through Homologous Recombination (HRR); 49 genes; every member is in the + arm (projection on the module's main direction 0.510). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-41.9, -50.1); signed map (-44.2, -49.4). **Vector** length 82.7, 22.4% of its response variance represented; |z| ≥ 3 in 1,081 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.9 | +7.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +3.5 | +7.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | +3.1 | +10.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.0 | +17.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | -0.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.9 | +2.4 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | +1.6 | +1.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.6 | +1.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.5 | +1.6 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.1 | -0.3 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.6 | -7.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.4 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.0 | -0.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | +0.1 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -2.3 | +0.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | SUZ12 polycomb repressive complex 2 subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q11.2 — chr17:31,937,007-32,001,038 (+) |
| Ensembl biotype | protein_coding |
| Also known as | JJAZ1, KIAA0160, CHET9 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; Polycomb repressive complex 2 |
| Reactome | 38 pathways, smallest: Defective pyroptosis; PRC2 methylates histones and DNA; Transcriptional Regulation by E2F6 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15022](https://www.uniprot.org/uniprotkb/Q15022) (Polycomb protein SUZ12):

> Polycomb group (PcG) protein. Component of the PRC2 complex, which methylates 'Lys-9' (H3K9me) and 'Lys-27' (H3K27me) of histone H3, leading to transcriptional repression of the affected target gene. The PRC2 complex may also serve as a recruiting platform for DNA methyltransferases, thereby linking two epigenetic repression systems. Genes repressed by the PRC2 complex include HOXC8, HOXA9, MYT1 and CDKN2A.

**Summary**, from NCBI Gene [23512](https://www.ncbi.nlm.nih.gov/gene/23512):

> This zinc finger gene has been identified at the breakpoints of a recurrent chromosomal translocation reported in endometrial stromal sarcoma. Recombination of these breakpoints results in the fusion of this gene and JAZF1. The protein encoded by this gene contains a zinc finger domain in the C terminus of the coding region. [provided by RefSeq, Jul 2009]

**Accessions** — [HGNC:17101](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17101) · Entrez [23512](https://www.ncbi.nlm.nih.gov/gene/23512) · UniProt [Q15022](https://www.uniprot.org/uniprotkb/Q15022) · Ensembl [ENSG00000178691](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178691)

## Data

Gene col 10947: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10947); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10947, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10947]; `tensor/DDL_lfc|DDL_z.npy` [10947]; `embed/gene_vectors.npy` [10947]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10947 or target_col == 10947). Every well: [[SUZ12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SUZ12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
