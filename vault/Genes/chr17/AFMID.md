---
symbol: "AFMID"
type: "gene"
col: 11366
ensembl_id: "ENSG00000183077"
name: "arylformamidase"
location: "17q25.3"
module: 3
arm: "+"
pooled_cpm: 57.02
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 15
n_dd_up_clean: 6
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# AFMID

*arylformamidase* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.42× (z +9.9, q 2e-20, up in 45 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.437× (z -9.3, q 8e-18, down in 47 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.321× (z -6.7, q 5e-09, down in 45 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRD37]] (+0.77, fdr 7e-06), [[CNNM4]] (+0.76, fdr 7e-06), [[ARID3A]] (+0.74, fdr 7e-06); moves opposite to [[SNX19]] (-0.70, fdr 7e-06), [[SOCS4]] (-0.69, fdr 1e-05), [[CAPRIN1]] (-0.69, fdr 1e-05).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11366.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.42×** | +9.9 | 2e-20 | 45/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.36×** | +9.6 | 2e-19 | 45/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.52×** | +6.7 | 5e-09 | 42/48 (NCI-H2347, A498, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +4.9 | 2e-04 | 31/48 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +4.0 | 0.006 | 30/46 (NCI-H2030, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.53×** | +3.4 | 0.063 | 28/47 (HepG2/C3A, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.091 | 22/49 (NCI-H2347, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.33× | +3.2 | 0.11 | 27/48 (SW480, NCI-H1573, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 6 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11366.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.437×** | -9.3 | 8e-18 | 47/48 (LOX-IMVI, A498, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.477×** | -7.7 | 4e-12 | 38/43 (C32, CHP-212, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.321×** | -6.7 | 5e-09 | 45/49 (SW480, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.565×** | -6.2 | 1e-07 | 34/48 (A-427, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.599×** | -5.8 | 1e-06 | 34/48 (LOX-IMVI, NCI-H661, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.596×** | -5.6 | 2e-06 | 28/42 (NCI-H460, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.717×** | -5.3 | 1e-05 | 28/47 (CHP-212, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.690×** | -4.0 | 0.004 | 29/47 (SNU-423, NCI-H661, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.710×** | -3.8 | 0.008 | 26/47 (A-427, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.708×** | -3.7 | 0.010 | 28/48 (NCI-H2347, NCI-H2030, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.530×** | -3.7 | 0.010 | 25/47 (LS 180, SW480, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.590×** | -3.1 | 0.087 | 18/36 (Panc 03.27, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.760×** | -3.1 | 0.087 | 23/48 (COLO 205, A498, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.825×** | -3.1 | 0.090 | 24/48 (SNU-423, A-427, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.599×** | -3.0 | 0.098 | 22/48 (COLO 205, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11366. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 74.6 | 3 | 3 | [[Panobinostat (drug)]] 5 µM 4.08× (z +16.8) | [[TAK-901 (drug)]] 5 µM 0.140× (z -12.2) |
| [[CHP-212 (line)]] | wt | 159 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -12.2) ⚠ cell-cycle shift, explains ~63% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.264× (z -12.1) |
| [[A-427 (line)]] | wt | 68.8 | 1 | 3 | [[Panobinostat (drug)]] 5 µM 2.79× (z +8.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.0626× (z -23.2) |
| [[A498 (line)]] | wt | 57.3 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.29× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.258× (z -10.3) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 40.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.63× (z +11.9) | — |
| [[KATO III (line)]] | alt | 49.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.12× (z +14.2) | — |
| [[COLO 205 (line)]] | alt | 88.6 | 1 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 2.98× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.286× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 60.7 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.25× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.115× (z -17.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 60.4 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.56× (z +13.8) | [[Dinaciclib (drug)]] 5 µM 0.111× (z -17.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 28.8 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.227× (z -10.2) ⚠ unreliable plate only · without an alert: [[Harringtonine (drug)]] 5 µM 0.233× (z -9.6) |
| [[A549 (line)]] | wt | 61.9 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.29× (z +9.6) | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -9.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 62.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.133× (z -13.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.380× (z -9.6) |
| [[HOP62 (line)]] | alt | 53.3 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.291× (z -9.4) |
| [[J82 (line)]] | alt | 34.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.09× (z +12.0) | — |
| [[LoVo (line)]] | wt | 36.9 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.81× (z +10.4) | — |
| [[LOX-IMVI (line)]] | wt | 66.9 | 0 | 2 (2 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.203× (z -12.3) ⚠ unreliable plate only |
| [[LS 180 (line)]] | wt | 48.5 | 0 | 2 | — | [[PH-797804 (drug)]] 5 µM 0.147× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 39.3 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.05× (z +8.8) | — |
| [[RKO (line)]] | wt | 40.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.273× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.432× (z -9.2) |
| [[SW1417 (line)]] | alt | 61.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.12× (z +9.7) | — |
| [[AsPC-1 (line)]] | alt | 31.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.61× (z +8.5) | — |
| [[H4 (line)]] | wt | 54.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.169× (z -9.5) ⚠ unreliable plate only |
| [[HEC-1-A (line)]] | alt | 77.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.350× (z -8.7) ⚠ unreliable plate only |
| [[Hs 766T (line)]] | wt | 34.2 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.216× (z -10.0) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 64.3 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.60× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 61.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.226× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 67.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.05× (z +10.5) | — |
| [[NCI-H661 (line)]] | alt | 46.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0478× (z -10.7) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 75.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -9.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 45.6 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.44× (z +8.8) | — |
| [[SNU-1 (line)]] | wt | 40.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0897× (z -13.2) |
| [[SNU-423 (line)]] | alt | 51.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.207× (z -10.6) ⚠ toxic |
| [[SW 900 (line)]] | alt | 40.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.100× (z -14.5) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 70.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 119 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 69.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 60.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11366), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD37]] | +0.77 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[CNNM4]] | +0.76 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[ARID3A]] | +0.74 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[ELP2]] | +0.74 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[CAMLG]] | +0.71 | +0.52 / +0.74 | both halves | 1e-05 |  |
| [[HILPDA]] | +0.70 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[HEATR5B]] | +0.70 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[LAMTOR5]] | +0.69 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[SEC22A]] | +0.69 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[SNHG19]] | +0.68 | +0.54 / +0.72 | both halves | 1e-05 |  |
| [[COMMD6]] | +0.67 | +0.45 / +0.69 | both halves | 3e-05 |  |
| [[CARHSP1]] | +0.66 | +0.44 / +0.65 | both halves | 3e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX19]] | -0.70 | -0.63 / -0.68 | both halves | 7e-06 |  |
| [[SOCS4]] | -0.69 | -0.70 / -0.52 | both halves | 1e-05 |  |
| [[CAPRIN1]] | -0.69 | -0.51 / -0.73 | both halves | 1e-05 |  |
| [[TUG1]] | -0.68 | -0.53 / -0.65 | both halves | 1e-05 |  |
| [[ZFP91]] | -0.67 | -0.57 / -0.61 | both halves | 9e-06 |  |
| [[TRIP12]] | -0.67 | -0.43 / -0.67 | both halves | 3e-05 |  |
| [[PSME3]] | -0.65 | -0.53 / -0.69 | both halves | 1e-05 |  |
| [[ANKRD40]] | -0.65 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[CPSF2]] | -0.65 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[PSME3IP1]] | -0.65 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[TASOR]] | -0.64 | -0.57 / -0.60 | both halves | 1e-05 |  |
| [[ZMPSTE24]] | -0.64 | -0.44 / -0.66 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers AFMID's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers AFMID's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[C2orf27A]] | B | C2orf27A activity raises AFMID's level | lines that do not express C2orf27A (5) vs lines expressing it (45) | 1.39× lower at baseline in the lines without C2orf27A | 0.091 | ⚠ within organs, on part of the lines; also absent: NBEAP2, UBA6-DT, ENSG00000287621; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.705). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (1.9, -18.5); signed map (-27.9, 13.2). **Vector** length 151, 50.1% of its response variance represented; |z| ≥ 3 in 942 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +7.7 | +9.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +7.7 | +9.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +6.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.6 | +4.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.3 | +4.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.9 | +3.4 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.5 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.1 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +3.0 | +2.2 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.4 | -7.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -8.2 | -5.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -8.1 | -5.8 |
|  | [[TAK-901 (drug)]] 5 µM |  | -8.0 | -6.7 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -7.0 | -9.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.1 | -3.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -4.9 | -3.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.5 | -3.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.3 | -3.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.1 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | arylformamidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:78,187,358-78,207,702 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZp686F03259, KF |
| Reactome | 2 pathways, smallest: Tryptophan catabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q63HM1](https://www.uniprot.org/uniprotkb/Q63HM1) (Kynurenine formamidase):

> Catalyzes the hydrolysis of N-formyl-L-kynurenine to L-kynurenine, the second step in the kynurenine pathway of tryptophan degradation. Kynurenine may be further oxidized to nicotinic acid, NAD(H) and NADP(H). Required for elimination of toxic metabolites.

**Summary**, from NCBI Gene [125061](https://www.ncbi.nlm.nih.gov/gene/125061):

> Predicted to enable arylformamidase activity. Predicted to be involved in obsolete L-tryptophan catabolic process to L-kynurenine. Predicted to be located in cytosol and nucleus. Predicted to be active in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20910](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20910) · Entrez [125061](https://www.ncbi.nlm.nih.gov/gene/125061) · UniProt [Q63HM1](https://www.uniprot.org/uniprotkb/Q63HM1) · Ensembl [ENSG00000183077](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183077)

## Data

Gene col 11366: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11366); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11366, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11366]; `tensor/DDL_lfc|DDL_z.npy` [11366]; `embed/gene_vectors.npy` [11366]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11366 or target_col == 11366). Every well: [[AFMID — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AFMID.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
