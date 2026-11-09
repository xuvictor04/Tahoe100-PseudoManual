---
symbol: "CCDC85C"
type: "gene"
col: 12981
ensembl_id: "ENSG00000205476"
name: "coiled-coil domain containing 85C"
location: "14q32.2"
module: 22
arm: "+"
pooled_cpm: 27.47
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 8
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# CCDC85C

*coiled-coil domain containing 85C* — 14q32.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.96× (z +24.4, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.754× (z -9.0, q 2e-16, down in 28 of 48 measured lines) ⚠ cell-cycle shift, explains ~30% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.763× (z -6.1, q 3e-07, down in 18 of 47 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFAIP8L1]] (+0.59, fdr 4e-05), [[GPSM2]] (+0.59, fdr 8e-05), [[CCNF]] (+0.58, fdr 3e-05); moves opposite to [[MFF-DT]] (-0.55, fdr 3e-04), [[GPATCH2]] (-0.53, fdr 4e-04), [[RBM48]] (-0.51, fdr 3e-04).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12981.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.96×** | +24.4 | 0e+00 | 47/48 (Panc 03.27, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.81×** | +23.2 | 0e+00 | 46/47 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.45×** | +20.1 | 0e+00 | 43/48 (Panc 03.27, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.64×** | +11.2 | 8e-27 | 36/48 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.39×** | +10.5 | 7e-24 | 27/47 (HEC-1-A, A498, …) | top dose only | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.24×** | +9.5 | 2e-19 | 36/48 (A549, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.39×** | +7.4 | 1e-11 | 25/47 (SW480, A-172, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +5.1 | 2e-05 | 17/48 (A-172, HT-29, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.45×** | +4.4 | 7e-04 | 9/46 (J82, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.21×** | +4.2 | 0.001 | 15/47 (HEC-1-A, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | 1.18× | +3.7 | 0.009 | 13/42 (LoVo, A549, …) | two highest doses | composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.17× | +3.6 | 0.018 | 12/47 (NCI-H1573, hTERT-HPNE, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 7 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12981.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.754×** | -9.0 | 2e-16 | 28/48 (Hs 766T, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.742×** | -6.7 | 6e-09 | 23/48 (HOP62, RKO, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.763×** | -6.1 | 3e-07 | 18/47 (RKO, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.809×** | -4.7 | 3e-04 | 21/48 (LOX-IMVI, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Amsacrine (drug)]] 5 µM |  | 0.865× | -4.6 | 5e-04 | 12/48 (SW48, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.816×** | -4.6 | 5e-04 | 17/47 (LOX-IMVI, HT-29, …) | top dose only |  |
| [[Cytarabine (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.811×** | -4.5 | 5e-04 | 17/47 (C32, SNU-1, …) | all doses, stronger at high dose |  |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.823×** | -4.4 | 9e-04 | 11/47 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.832×** | -4.1 | 0.002 | 15/48 (RKO, SW48, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 0.836× | -4.0 | 0.003 | 14/47 (CFPAC-1, LOX-IMVI, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.856× | -3.5 | 0.026 | 12/48 (LOX-IMVI, AN3 CA, …) | inconsistent across doses |  |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | 0.858× | -3.4 | 0.027 | 4/47 (CHP-212, SHP-77, …) | inconsistent across doses |  |
| [[Larotrectinib sulfate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.863× | -3.3 | 0.043 | 4/47 (A-172, LS 180, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12981. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 56.9 | 0 | 13 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -16.0) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.186× (z -11.5) |
| [[PANC-1 (line)]] | alt | 19.6 | 5 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 4.11× (z +12.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.33× (z +10.6) | — |
| [[A549 (line)]] | wt | 18.3 | 4 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.09× (z +10.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.54× (z +10.1) | — |
| [[CFPAC-1 (line)]] | alt | 33.5 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.19× (z +11.9) | — |
| [[J82 (line)]] | alt | 28.9 | 4 (2 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 4.52× (z +13.9) | — |
| [[Panc 03.27 (line)]] | alt | 50.5 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.58× (z +13.6) | — |
| [[RKO (line)]] | wt | 39.2 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -14.2) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.225× (z -11.6) |
| [[HEC-1-A (line)]] | alt | 57.7 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +15.4) ⚠ cell-cycle shift, explains ~41% of this change | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.438× (z -8.7) ⚠ cell-cycle shift, explains ~4% of this change |
| [[HT-29 (line)]] | alt | 28.1 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 3.69× (z +10.6) | [[Auranofin (drug)]] 5 µM 0.294× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 23.7 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.78× (z +10.1) | — |
| [[NCI-H1792 (line)]] | alt | 14.0 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +12.5) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 5.94× (z +9.9) | — |
| [[NCI-H2347 (line)]] | alt | 41.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.1) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 3.10× (z +9.1) | — |
| [[SW1417 (line)]] | alt | 40.4 | 3 | 0 | [[Belinostat (drug)]] 5 µM 3.40× (z +10.6) | — |
| [[SW480 (line)]] | alt | 30.7 | 3 | 0 | [[Belinostat (drug)]] 5 µM 2.92× (z +13.0) | — |
| [[A498 (line)]] | wt | 11.9 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.15× (z +14.9) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 4.09× (z +9.0) | — |
| [[LoVo (line)]] | wt | 33.4 | 2 (1 ⚠) | 0 | [[Belinostat (drug)]] 5 µM 2.39× (z +8.7) | — |
| [[A-172 (line)]] | wt | 31.9 | 1 | 0 | [[Belinostat (drug)]] 5 µM 3.35× (z +8.6) | — |
| [[CHP-212 (line)]] | wt | 39.7 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.103× (z -9.0) |
| [[HepG2_C3A (line)]] | wt | 20.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.86× (z +8.5) | — |
| [[Hs 766T (line)]] | wt | 18.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.184× (z -12.1) ⚠ cell-cycle shift, explains ~30% of this change |
| [[LS 180 (line)]] | wt | 32.7 | 1 | 0 | [[Belinostat (drug)]] 5 µM 2.80× (z +8.6) | — |
| [[NCI-H2030 (line)]] | alt | 29.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 2.77× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 11.2 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.181× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 10.4 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.109× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.267× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 13.5 | 1 | 0 | [[Belinostat (drug)]] 5 µM 4.42× (z +8.6) | — |
| [[SW48 (line)]] | wt | 71.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.281× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 54.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.1 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 29.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 22.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12981), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*63 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFAIP8L1]] | +0.59 | +0.45 / +0.41 | both halves | 4e-05 |  |
| [[GPSM2]] | +0.59 | +0.37 / +0.51 | both halves | 8e-05 |  |
| [[CCNF]] | +0.58 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[CEP131]] | +0.55 | +0.33 / +0.33 | both halves | 1e-04 |  |
| [[SAPCD2]] | +0.55 | +0.53 / +0.40 | both halves | 4e-05 |  |
| [[MICAL3]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[NEURL1B]] | +0.55 | +0.36 / +0.54 | both halves | 1e-04 |  |
| [[ACBD7]] | +0.54 | +0.43 / +0.49 | both halves | 3e-05 |  |
| [[UBE2S]] | +0.54 | +0.46 / +0.44 | both halves | 3e-05 |  |
| [[FOXO6]] | +0.53 | +0.39 / +0.42 | both halves | 5e-05 |  |
| [[NCOR2]] | +0.53 | +0.40 / +0.41 | both halves | 5e-05 |  |
| [[NOS1AP]] | +0.53 | +0.43 / +0.45 | both halves | 4e-05 |  |

## Genes that move opposite

*37 of its nearest partners move opposite, 11 of them with an alert (⚠; 11 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MFF-DT]] | -0.55 | -0.28 / -0.37 | both halves | 3e-04 |  |
| [[GPATCH2]] | -0.53 | -0.43 / -0.26 | both halves | 4e-04 |  |
| [[RBM48]] | -0.51 | -0.45 / -0.29 | both halves | 3e-04 |  |
| [[LINC01134]] | -0.51 | -0.30 / -0.29 | both halves | 2e-04 |  |
| [[SUPT7L]] | -0.50 | -0.33 / -0.39 | both halves | 1e-04 |  |
| [[LINC00571]] | -0.50 | -0.21 / -0.38 | both halves | 6e-04 |  |
| [[ZNF234]] | -0.50 | -0.33 / -0.30 | both halves | 2e-04 |  |
| [[LINC01829]] | -0.49 | -0.31 / -0.21 | both halves | 7e-04 |  |
| [[CARD6]] | -0.49 | -0.34 / -0.34 | both halves | 1e-04 |  |
| [[COA6]] | -0.49 | -0.32 / -0.29 | both halves | 2e-04 |  |
| [[C12orf60]] | -0.49 | -0.30 / -0.07 | ⚠ not reproduced | 0.004 |  |
| [[PCF11-AS1]] | -0.49 | -0.48 / -0.25 | both halves | 4e-04 |  |
| [[PNISR-AS1]] | -0.49 | -0.31 / -0.21 | both halves | 6e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers CCDC85C's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers CCDC85C's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[LINC01829]] | C | LINC01829 activity lowers CCDC85C's level | lines that do not express LINC01829 (3) vs lines expressing it (47) | 1.57× higher at baseline in the lines without LINC01829 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: PARP11, GNG12-AS1, LINC02763; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.424). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-34.8, -58.8); signed map (-50.8, -39.2). **Vector** length 100, 22.9% of its response variance represented; |z| ≥ 3 in 1,130 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +5.3 | +23.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.9 | +24.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.3 | +20.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.0 | +11.2 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.0 | +7.4 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +9.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +5.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.3 | +4.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +1.8 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | -7.3 | -9.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.2 | -1.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -5.3 | -2.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -4.9 | -6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.5 | -4.6 |
|  | [[Amsacrine (drug)]] 5 µM |  | -3.4 | -4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -1.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | -2.3 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 85C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.2 — chr14:99,500,190-99,604,207 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [A6NKD9](https://www.uniprot.org/uniprotkb/A6NKD9) (Coiled-coil domain-containing protein 85C):

> May play a role in cell-cell adhesion and epithelium development through its interaction with proteins of the beta-catenin family (Probable). May play an important role in cortical development, especially in the maintenance of radial glia (By similarity).

**Summary**, from NCBI Gene [317762](https://www.ncbi.nlm.nih.gov/gene/317762):

> Predicted to be involved in cerebral cortex development. Predicted to act upstream of or within several processes, including Notch signaling pathway; establishment of cell polarity; and radial glial cell differentiation. Located in adherens junction. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:35459](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:35459) · Entrez [317762](https://www.ncbi.nlm.nih.gov/gene/317762) · UniProt [A6NKD9](https://www.uniprot.org/uniprotkb/A6NKD9) · Ensembl [ENSG00000205476](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000205476)

## Data

Gene col 12981: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12981); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12981, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12981]; `tensor/DDL_lfc|DDL_z.npy` [12981]; `embed/gene_vectors.npy` [12981]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12981 or target_col == 12981). Every well: [[CCDC85C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC85C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
