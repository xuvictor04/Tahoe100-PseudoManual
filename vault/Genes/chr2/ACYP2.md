---
symbol: "ACYP2"
type: "gene"
col: 9990
ensembl_id: "ENSG00000170634"
name: "acylphosphatase 2"
location: "2p16.2"
module: 26
arm: "+"
pooled_cpm: 71.7
n_lines_expressing: 50
n_dd_up: 36
n_dd_down: 8
n_dd_up_clean: 30
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# ACYP2

*acylphosphatase 2* — 2p16.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.35× (z +15.8, q 0e+00, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.386× (z -6.5, q 4e-08, down in 40 of 49 measured lines).
> Its strongest partners by |cos| (90 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 10 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CATSPERE]] (+0.80, fdr 7e-06), [[RFX3-DT]] (+0.78, fdr 1e-05), [[MAD2L1-DT]] (+0.76, fdr 4e-05); moves opposite to [[ATG4C]] (-0.66, fdr 4e-05), [[L2HGDH]] (-0.66, fdr 8e-05), [[RAB3A]] (-0.64, fdr 1e-04).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[LHX2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9990.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +15.8 | 0e+00 | 46/49 (AsPC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.66×** | +9.3 | 3e-18 | 32/48 (NCI-H460, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.78×** | +7.6 | 7e-12 | 34/48 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +6.9 | 9e-10 | 41/48 (HS-578T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.76×** | +6.8 | 9e-10 | 30/45 (SW 900, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +6.6 | 4e-09 | 46/48 (A-427, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +6.4 | 2e-08 | 35/48 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.57×** | +5.9 | 3e-07 | 37/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.58×** | +5.8 | 6e-07 | 32/47 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.53×** | +5.6 | 1e-06 | 29/48 (A498, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.49×** | +5.0 | 2e-05 | 33/47 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +4.6 | 2e-04 | 25/49 (SW 900, C32, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.42×** | +4.6 | 2e-04 | 33/49 (SW480, PANC-1, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.26×** | +4.3 | 6e-04 | 26/48 (NCI-H1573, A498, …) | top dose only | low cells (technical?) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.27×** | +4.1 | 0.001 | 27/48 (SW480, HepG2/C3A, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **1.41×** | +4.1 | 0.001 | 30/50 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~22% here); noisy plate (z scaled) |
| [[Bimiralisib (drug)]] 5 µM |  | **1.78×** | +3.9 | 0.003 | 31/50 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +3.8 | 0.004 | 30/47 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.24×** | +3.7 | 0.007 | 25/49 (SW480, HCT15, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9990.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.386×** | -6.5 | 4e-08 | 40/49 (LOX-IMVI, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.404×** | -6.2 | 2e-07 | 38/48 (A-427, MIA PaCa-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **0.648×** | -5.7 | 3e-06 | 30/48 (J82, Panc 03.27, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.666×** | -5.3 | 2e-05 | 31/48 (PANC-1, J82, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.688×** | -4.9 | 1e-04 | 37/48 (NCI-H2030, BT-474, …) | two highest doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.738×** | -4.0 | 0.006 | 27/48 (NCI-H23, SW480, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.739×** | -4.0 | 0.006 | 28/48 (SW 1088, J82, …) | rises with dose |  |
| [[Fumaric acid (drug)]] 5 µM |  | **0.774×** | -3.2 | 0.088 | 26/49 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9990. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 62.3 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +14.3) | — |
| [[AsPC-1 (line)]] | alt | 38.7 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.45× (z +21.7) | — |
| [[SW 900 (line)]] | alt | 65.6 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.49× (z +14.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +13.3) | — |
| [[A-427 (line)]] | wt | 129 | 0 | 3 (2 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.130× (z -10.7) |
| [[C32 (line)]] | wt | 108 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.05× (z +16.9) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 80.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.59× (z +14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.96× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 54.5 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +9.3) | — |
| [[NCI-H1573 (line)]] | alt | 97.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.7) | — |
| [[PANC-1 (line)]] | alt | 66.9 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +13.1) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.356× (z -11.2) ⚠ cell-cycle shift, explains ~56% of this change |
| [[CFPAC-1 (line)]] | alt | 58.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.89× (z +12.4) | — |
| [[H4 (line)]] | wt | 56.7 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +9.2) | — |
| [[HepG2_C3A (line)]] | wt | 155 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.23× (z +9.4) | [[Niclosamide (olamine) (drug)]] 5 µM 0.326× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~63% of this change |
| [[HOP62 (line)]] | alt | 81.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.76× (z +11.9) | — |
| [[Hs 766T (line)]] | wt | 30.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 46.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.10× (z +12.2) | — |
| [[HT-29 (line)]] | alt | 88.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.60× (z +12.4) | — |
| [[J82 (line)]] | alt | 40.2 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.295× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[KATO III (line)]] | alt | 67.1 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +13.2) | — |
| [[LOX-IMVI (line)]] | wt | 72.0 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.99× (z +8.5) | [[TAK-901 (drug)]] 5 µM 0.157× (z -8.5) |
| [[MIA PaCa-2 (line)]] | alt | 89.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.15× (z +12.7) | — |
| [[NCI-H23 (line)]] | alt | 119 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +11.5) | — |
| [[Panc 03.27 (line)]] | alt | 74.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +13.3) | [[Digitoxin (drug)]] 5 µM 0.365× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[RKO (line)]] | wt | 77.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.46× (z +9.6) | — |
| [[SW1417 (line)]] | alt | 74.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +8.9) | — |
| [[SW480 (line)]] | alt | 82.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.10× (z +11.1) | — |
| [[A-172 (line)]] | wt | 60.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.95× (z +12.2) | — |
| [[A498 (line)]] | wt | 56.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +10.9) | — |
| [[A549 (line)]] | wt | 92.0 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.387× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[BT-474 (line)]] | alt | 67.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.15× (z +8.5) | — |
| [[COLO 205 (line)]] | alt | 53.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.67× (z +12.1) | — |
| [[HCT15 (line)]] | alt | 69.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.66× (z +13.6) | — |
| [[HEC-1-A (line)]] | alt | 64.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +10.5) | — |
| [[hTERT-HPNE (line)]] | wt | 68.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 37.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +8.7) | — |
| [[RPMI-7951 (line)]] | alt | 98.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 97.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.26× (z +9.4) | — |
| [[SK-MEL-2 (line)]] | alt | 95.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.98× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 82.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +12.3) | — |
| [[SNU-423 (line)]] | alt | 51.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.38× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 90.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 71.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 72.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 81.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 89.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 80.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 60.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9990), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CATSPERE]] | +0.80 | +0.77 / +0.61 | both halves | 7e-06 |  |
| [[RFX3-DT]] | +0.78 | +0.79 / +0.51 | both halves | 1e-05 |  |
| [[MAD2L1-DT]] | +0.76 | +0.79 / +0.42 | both halves | 4e-05 |  |
| [[RAB30-DT]] | +0.75 | +0.81 / +0.43 | both halves | 3e-05 |  |
| [[CHD1-DT]] | +0.75 | +0.78 / +0.51 | both halves | 1e-05 |  |
| [[NEK11]] | +0.75 | +0.77 / +0.46 | both halves | 3e-05 |  |
| [[CCDC90B-AS1]] | +0.74 | +0.76 / +0.40 | both halves | 5e-05 |  |
| [[BDNF-AS]] | +0.74 | +0.76 / +0.43 | both halves | 3e-05 |  |
| [[HEXIM2-AS1]] | +0.73 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[PPP1R12A-AS2]] | +0.73 | +0.77 / +0.40 | both halves | 5e-05 |  |
| [[MSTO1]] | +0.73 | +0.79 / +0.51 | both halves | 1e-05 |  |
| [[FBXL19-AS1]] | +0.72 | +0.68 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATG4C]] | -0.66 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[L2HGDH]] | -0.66 | -0.58 / -0.37 | both halves | 8e-05 |  |
| [[RAB3A]] | -0.64 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[EFNA4]] | -0.63 | -0.60 / -0.29 | both halves | 2e-04 |  |
| [[ZNF511]] | -0.63 | -0.63 / -0.32 | both halves | 2e-04 |  |
| [[MAST3]] | -0.62 | -0.63 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LHX2]] | B | LHX2 activity raises ACYP2's level | lines that do not express LHX2 (26) vs lines expressing it (24) | 1.22× lower at baseline in the lines without LHX2 | 0.015 | ⚠ within organs, on part of the lines; also absent: CECR2, COL4A4, GHR |
| [[TOP2A]] | B | TOP2A activity lowers ACYP2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[LNC-LBCS]] | B | LNC-LBCS activity raises ACYP2's level | lines that do not express LNC-LBCS (13) vs lines expressing it (37) | 1.27× lower at baseline in the lines without LNC-LBCS | 0.063 | ⚠ within organs, on part of the lines; also absent: ANKS1B, TERT, SAMD11; maybe low, not absent |
| [[FAM66C]] | B | FAM66C activity raises ACYP2's level | lines that do not express FAM66C (15) vs lines expressing it (35) | 1.23× lower at baseline in the lines without FAM66C | 0.089 | ⚠ within organs, on part of the lines; also absent: MED12L, LONRF2, LMX1B; maybe low, not absent |
| [[ZDHHC1]] | C | ZDHHC1 activity raises ACYP2's level | lines that do not express ZDHHC1 (4) vs lines expressing it (46) | 1.63× lower at baseline in the lines without ZDHHC1 | 0.089 | ⚠ few lines (4 vs 46); across organs; also absent: PDE4C, KIF5A |
| [[DPF1]] | C | DPF1 activity raises ACYP2's level | lines that do not express DPF1 (4) vs lines expressing it (46) | 1.37× lower at baseline in the lines without DPF1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: ASAP3, CCDC102A, TPST1; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.718). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (5.5, 16.4); signed map (26.1, -8.7). **Vector** length 114, 35.9% of its response variance represented; |z| ≥ 3 in 1,165 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.0 | +6.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.8 | +7.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.4 | +6.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.1 | +9.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.8 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +3.3 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +2.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.8 | +1.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -7.5 | +1.8 |
|  | [[Panobinostat (drug)]] 5 µM |  | -6.8 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.9 | +0.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.7 | +1.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -3.4 | +1.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -6.2 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | -2.8 | -2.6 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -2.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | acylphosphatase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p16.2 — chr2:53,970,838-54,305,300 (+) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [P14621](https://www.uniprot.org/uniprotkb/P14621) (Acylphosphatase-2):

> catalyzes the hydrolysis of acylphosphates compounds containing a carboxylphosphate bond.

**Summary**, from NCBI Gene [98](https://www.ncbi.nlm.nih.gov/gene/98):

> Acylphosphatase can hydrolyze the phosphoenzyme intermediate of different membrane pumps, particularly the Ca2+/Mg2+-ATPase from sarcoplasmic reticulum of skeletal muscle. Two isoenzymes have been isolated, called muscle acylphosphatase and erythrocyte acylphosphatase on the basis of their tissue localization. This gene encodes the muscle-type isoform (MT). An increase of the MT isoform is associated with muscle differentiation. Several transcript variants encoding different isoforms have been …

**Accessions** — [HGNC:180](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:180) · Entrez [98](https://www.ncbi.nlm.nih.gov/gene/98) · UniProt [P14621](https://www.uniprot.org/uniprotkb/P14621) · Ensembl [ENSG00000170634](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170634)

## Data

Gene col 9990: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9990); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9990, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9990]; `tensor/DDL_lfc|DDL_z.npy` [9990]; `embed/gene_vectors.npy` [9990]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9990 or target_col == 9990). Every well: [[ACYP2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACYP2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
