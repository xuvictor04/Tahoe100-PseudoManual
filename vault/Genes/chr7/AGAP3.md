---
symbol: "AGAP3"
type: "gene"
col: 5456
ensembl_id: "ENSG00000133612"
name: "ArfGAP with GTPase domain, ankyrin repeat and PH domain 3"
location: "7q36.1"
module: 3
arm: "+"
pooled_cpm: 43.47
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 7
n_dd_up_clean: 11
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# AGAP3

*ArfGAP with GTPase domain, ankyrin repeat and PH domain 3* — 7q36.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.76× (z +12.1, q 5e-31, up in 43 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.647× (z -9.3, q 8e-18, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBTD1]] (+0.68, fdr 7e-06), [[CSNK1G2]] (+0.67, fdr 7e-06), [[TMEM38A]] (+0.65, fdr 1e-05); moves opposite to [[TAF2]] (-0.63, fdr 7e-06), [[EPC2]] (-0.58, fdr 1e-05), [[TTPAL]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[P3H3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5456.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.76×** | +12.1 | 5e-31 | 43/48 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.92×** | +9.5 | 8e-19 | 40/47 (C32, PANC-1, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +7.0 | 5e-10 | 37/48 (C-33 A, NCI-H2347, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.56×** | +6.7 | 2e-09 | 35/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.49×** | +6.0 | 2e-07 | 40/48 (SW480, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.4 | 0.001 | 24/47 (SW480, SNU-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.32×** | +4.2 | 0.002 | 24/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +4.0 | 0.005 | 26/47 (AsPC-1, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | **1.20×** | +3.9 | 0.006 | 23/48 (NCI-H1792, RPMI-7951, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.006 | 24/48 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.28×** | +3.7 | 0.011 | 22/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +3.3 | 0.045 | 19/48 (RKO, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +3.2 | 0.068 | 16/48 (LOX-IMVI, NCI-H2030, …) | rises with dose |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.34×** | +3.1 | 0.073 | 13/48 (MIA PaCa-2, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5456.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.647×** | -9.3 | 8e-18 | 36/48 (AN3 CA, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.547×** | -9.1 | 2e-17 | 36/48 (NCI-H23, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.672×** | -6.0 | 4e-07 | 31/48 (SK-MEL-2, SW48, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.689×** | -5.5 | 5e-06 | 29/48 (A-427, NCI-H1573, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Busulfan (drug)]] 0.05 µM |  | **0.715×** | -5.1 | 5e-05 | 25/48 (NCI-H2030, KATO III, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.724×** | -4.7 | 3e-04 | 27/48 (AsPC-1, LOX-IMVI, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.745×** | -4.4 | 7e-04 | 24/48 (SK-MEL-2, C32, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Larotrectinib (drug)]] 0.05 µM |  | 0.817× | -3.1 | 0.16 | 13/49 (A-172, A549, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.819× | -3.0 | 0.17 | 11/49 (SHP-77, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5456. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 52.3 | 6 (2 ⚠) | 2 | [[Digitoxin (drug)]] 5 µM 3.13× (z +13.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.01× (z +11.9) | [[Homoharringtonine (drug)]] 0.5 µM 0.407× (z -11.0) |
| [[SK-MEL-2 (line)]] | alt | 93.7 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -20.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.275× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 31.0 | 3 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.71× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.481× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 32.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -11.8) |
| [[LoVo (line)]] | wt | 40.1 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.62× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.498× (z -9.0) |
| [[NCI-H2030 (line)]] | alt | 31.5 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.04× (z +9.1) | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -12.1) |
| [[RKO (line)]] | wt | 52.6 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -12.5) |
| [[A-427 (line)]] | wt | 31.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~11% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.401× (z -10.6) |
| [[C-33 A (line)]] | alt | 87.2 | 1 | 1 | [[Auranofin (drug)]] 5 µM 3.13× (z +9.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.352× (z -9.0) |
| [[LOX-IMVI (line)]] | wt | 32.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.21× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -8.7) |
| [[NCI-H23 (line)]] | alt | 35.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -12.9) |
| [[PANC-1 (line)]] | alt | 28.5 | 2 (2 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.53× (z +10.5) ⚠ toxic | — |
| [[SW 900 (line)]] | alt | 62.4 | 1 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 3.01× (z +8.6) ⚠ toxic | [[Homoharringtonine (drug)]] 0.5 µM 0.329× (z -8.9) |
| [[A498 (line)]] | wt | 50.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.29× (z +13.2) | — |
| [[A549 (line)]] | wt | 23.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.74× (z +11.4) | — |
| [[AN3 CA (line)]] | alt | 91.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -13.1) |
| [[BT-474 (line)]] | alt | 33.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.36× (z +8.8) | — |
| [[C32 (line)]] | wt | 188 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.09× (z +10.6) ⚠ toxic | — |
| [[H4 (line)]] | wt | 34.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +9.8) | — |
| [[HEC-1-A (line)]] | alt | 35.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.94× (z +9.4) | — |
| [[HOP62 (line)]] | alt | 28.0 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.24× (z +8.6) ⚠ toxic | — |
| [[HS-578T (line)]] | alt | 39.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.365× (z -10.5) |
| [[HT-29 (line)]] | alt | 56.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -8.9) |
| [[LS 180 (line)]] | wt | 40.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +9.8) | — |
| [[SHP-77 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.251× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change |
| [[SW1417 (line)]] | alt | 67.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.78× (z +8.6) | — |
| [[A-172 (line)]] | wt | 42.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 52.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 41.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 58.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 67.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 46.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 46.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 47.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 81.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5456), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBTD1]] | +0.68 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[CSNK1G2]] | +0.67 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[TMEM38A]] | +0.65 | +0.52 / +0.67 | both halves | 1e-05 |  |
| [[LRP5L]] | +0.65 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[RENO1]] | +0.64 | +0.51 / +0.71 | both halves | 1e-05 |  |
| [[ANKRD13D]] | +0.64 | +0.59 / +0.69 | both halves | 7e-06 | same gene group |
| [[HOXB5]] | +0.64 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[HOXB6]] | +0.63 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[CASTOR2]] | +0.63 | +0.59 / +0.55 | both halves | 1e-05 |  |
| [[PTDSS2]] | +0.62 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[SLC12A9]] | +0.61 | +0.40 / +0.73 | both halves | 5e-05 |  |
| [[PPP3R1]] | +0.61 | +0.65 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF2]] | -0.63 | -0.67 / -0.66 | both halves | 7e-06 |  |
| [[EPC2]] | -0.58 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[TTPAL]] | -0.58 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[ZNF414]] | -0.57 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[ZNF674]] | -0.57 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[PABIR1]] | -0.56 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[HUS1]] | -0.56 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[STAMBP]] | -0.56 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[YTHDC2]] | -0.55 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[FBXO38]] | -0.54 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[GTF2H3]] | -0.54 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[NUBP1]] | -0.54 | -0.64 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[P3H3]] | B | P3H3 activity raises AGAP3's level | lines that do not express P3H3 (10) vs lines expressing it (40) | 1.58× lower at baseline in the lines without P3H3 | 0.017 | ⚠ within organs, on part of the lines; also absent: STARD9, GSTA4, CTXN1 |
| [[SLC43A1]] | B | SLC43A1 activity raises AGAP3's level | lines that do not express SLC43A1 (9) vs lines expressing it (41) | 1.62× lower at baseline in the lines without SLC43A1 | 0.026 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[KREMEN2]] | B | KREMEN2 activity raises AGAP3's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 1.40× lower at baseline in the lines without KREMEN2 | 0.062 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |
| [[TFPI]] | B | TFPI activity lowers AGAP3's level | lines that do not express TFPI (14) vs lines expressing it (36) | 1.51× higher at baseline in the lines without TFPI | 0.086 | ⚠ within organs, on part of the lines; also absent: STC1, C2orf74-DT, CALCRL |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.450). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-9.7, -3.7); signed map (-41.4, 1.8). **Vector** length 127, 36.0% of its response variance represented; |z| ≥ 3 in 898 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +7.9 | +6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +12.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +6.1 | +9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.8 | +7.0 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.8 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.5 | +4.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.3 | +3.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +3.2 | +1.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -8.8 | -9.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -7.6 | -9.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.0 | -5.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -6.9 | -4.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.7 | -2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.5 | -1.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -3.1 | -2.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.1 | -3.0 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -3.0 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | ArfGAP with GTPase domain, ankyrin repeat and PH domain 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q36.1 — chr7:151,085,831-151,144,436 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CENTG3 |
| Gene groups (HGNC) | ArfGAPs; Ankyrin repeat domain containing; BAR-PH domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96P47](https://www.uniprot.org/uniprotkb/Q96P47) (Arf-GAP with GTPase, ANK repeat and PH domain-containing protein 3):

> GTPase-activating protein for the ADP ribosylation factor family (Potential). GTPase which may be involved in the degradation of expanded polyglutamine proteins through the ubiquitin-proteasome pathway.

**Summary**, from NCBI Gene [116988](https://www.ncbi.nlm.nih.gov/gene/116988):

> This gene encodes an essential component of the N-methyl-D-aspartate (NMDA) receptor signaling complex which mediates long-term potentiation in synapses by linking activation of NMDA receptor to alpha-amino-3-hydroxy-5-methyl-4-isoxazolepropionic acid (AMPA) receptor trafficking. The encoded protein contains an N-terminal GTPase-like domain, a pleckstrin homology domain, an ArfGAP domain and several C-terminal ankryn repeat domains. [provided by RefSeq, Apr 2017]

**Accessions** — [HGNC:16923](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16923) · Entrez [116988](https://www.ncbi.nlm.nih.gov/gene/116988) · UniProt [Q96P47](https://www.uniprot.org/uniprotkb/Q96P47) · Ensembl [ENSG00000133612](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000133612)

## Data

Gene col 5456: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5456); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5456, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5456]; `tensor/DDL_lfc|DDL_z.npy` [5456]; `embed/gene_vectors.npy` [5456]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5456 or target_col == 5456). Every well: [[AGAP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGAP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
