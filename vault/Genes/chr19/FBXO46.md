---
symbol: "FBXO46"
type: "gene"
col: 10784
ensembl_id: "ENSG00000177051"
name: "F-box protein 46"
location: "19q13.32"
module: 160
arm: "+"
pooled_cpm: 27.68
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 17
n_dd_up_clean: 7
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/160"]
generated_by: "tahoemap"
---

# FBXO46

*F-box protein 46* — 19q13.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 1.40× (z +6.3, q 9e-08, up in 28 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.651× (z -8.1, q 4e-13, down in 28 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC66A2]] (+0.64, fdr 1e-05), [[NECTIN2]] (+0.62, fdr 3e-05), [[TBC1D25]] (+0.62, fdr 1e-05); moves opposite to [[STRADB]] (-0.55, fdr 1e-05), [[RAB11FIP2]] (-0.55, fdr 3e-05), [[SNX5]] (-0.52, fdr 5e-05).
> It sits in the **+** arm of [[Module 160]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[LMTK3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10784.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +6.3 | 9e-08 | 28/47 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.40×** | +6.3 | 9e-08 | 23/48 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +5.7 | 2e-06 | 27/46 (LS 180, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.35×** | +5.6 | 3e-06 | 23/48 (HOP62, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.73×** | +5.4 | 7e-06 | 21/48 (PANC-1, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.28×** | +4.7 | 3e-04 | 22/47 (A498, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.19× | +4.6 | 3e-04 | 18/48 (A498, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.24×** | +4.1 | 0.003 | 16/48 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 0.5 µM |  | 1.20× | +3.4 | 0.045 | 14/45 (LOX-IMVI, SNU-1, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 11 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10784.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.651×** | -8.1 | 4e-13 | 28/47 (SW480, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.921× | -5.3 | 3e-05 | 2/48 (MIA PaCa-2, CHP-212) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **0.764×** | -5.1 | 8e-05 | 20/43 (HCT15, NCI-H460, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.779×** | -4.7 | 4e-04 | 20/48 (AN3 CA, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.781×** | -4.7 | 4e-04 | 21/48 (COLO 205, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.783×** | -4.4 | 9e-04 | 20/48 (BT-474, HS-578T, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.797×** | -4.3 | 0.002 | 21/47 (A-427, SNU-423, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~17% of this change | **0.796×** | -4.1 | 0.003 | 19/45 (C-33 A, RPMI-7951, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.811×** | -4.0 | 0.005 | 18/48 (HEC-1-A, C-33 A, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.823×** | -3.7 | 0.014 | 19/46 (RPMI-7951, HT-29, …) | rises with dose |  |
| [[EX229 (drug)]] 0.05 µM |  | **0.816×** | -3.6 | 0.014 | 12/48 (HT-29, LOX-IMVI, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.694×** | -3.6 | 0.014 | 15/30 (HT-29, SNU-423, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.826×** | -3.6 | 0.014 | 11/48 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.830×** | -3.5 | 0.018 | 12/47 (AsPC-1, RKO, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.831×** | -3.5 | 0.019 | 19/47 (COLO 205, SW480, …) | rises with dose |  |
| [[Ixazomib (drug)]] 0.05 µM |  | **0.824×** | -3.4 | 0.021 | 10/46 (SW1417, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Gefitinib (drug)]] 5 µM |  | 0.846× | -3.1 | 0.055 | 7/48 (NCI-H460, LoVo, …) | inconsistent across doses |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 0.842× | -3.1 | 0.061 | 12/47 (A549, CFPAC-1, …) | top dose only |  |
| [[Riluzole hydrochloride (drug)]] 0.5 µM |  | 0.856× | -2.9 | 0.092 | 12/48 (SNU-1, H4, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.745×** | -2.9 | 0.097 | 9/47 (LOX-IMVI, HT-29, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10784. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 38.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.127× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[C-33 A (line)]] | alt | 38.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.138× (z -13.2) ⚠ toxic; cell-cycle shift, explains ~17% of this change |
| [[C32 (line)]] | wt | 18.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.169× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[Hs 766T (line)]] | wt | 28.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[NCI-H1792 (line)]] | alt | 25.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -15.7) ⚠ cell-cycle shift, explains ~92% of this change |
| [[PANC-1 (line)]] | alt | 21.9 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.15× (z +15.9) ⚠ cell-cycle shift, explains ~92% of this change | — |
| [[HCT15 (line)]] | alt | 34.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.144× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[LOX-IMVI (line)]] | wt | 14.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[NCI-H1573 (line)]] | alt | 30.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[NCI-H460 (line)]] | wt | 21.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.313× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[Panc 03.27 (line)]] | alt | 28.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.223× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[RPMI-7951 (line)]] | alt | 29.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.234× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~17% of this change |
| [[SW1417 (line)]] | alt | 46.8 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.402× (z -9.3) ⚠ transcription drop; cell-cycle shift, explains ~42% of this change |
| [[SW48 (line)]] | wt | 27.5 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.113× (z -10.7) |
| [[SW480 (line)]] | alt | 34.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.518× (z -10.2) ⚠ cell-cycle shift, explains ~92% of this change |
| [[A-172 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 32.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 35.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 53.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 32.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10784), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC66A2]] | +0.64 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[NECTIN2]] | +0.62 | +0.67 / +0.44 | both halves | 3e-05 |  |
| [[TBC1D25]] | +0.62 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[GRAMD1A]] | +0.59 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[ZGPAT]] | +0.58 | +0.67 / +0.38 | both halves | 6e-05 |  |
| [[TICAM1]] | +0.56 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[DTX2]] | +0.56 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[PRKD2]] | +0.55 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[ATG2A]] | +0.55 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[ASMTL]] | +0.55 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[PLIN3]] | +0.54 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[VPS37C]] | +0.54 | +0.40 / +0.55 | both halves | 4e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STRADB]] | -0.55 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[RAB11FIP2]] | -0.55 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[SNX5]] | -0.52 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[PAK2]] | -0.52 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[SCRN1]] | -0.51 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[TWF1]] | -0.51 | -0.36 / -0.59 | both halves | 1e-04 |  |
| [[NT5DC1]] | -0.51 | -0.55 / -0.38 | both halves | 7e-05 |  |
| [[DNAJC13]] | -0.51 | -0.37 / -0.56 | both halves | 8e-05 |  |
| [[LRRC58]] | -0.49 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[TMEM106B]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[ERAP1]] | -0.48 | -0.41 / -0.36 | both halves | 9e-05 |  |
| [[CRPPA]] | -0.47 | -0.41 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LMTK3]] | B | LMTK3 activity raises FBXO46's level | lines that do not express LMTK3 (15) vs lines expressing it (35) | 1.30× lower at baseline in the lines without LMTK3 | 0.046 | ⚠ within organs, on part of the lines; also absent: CRYBG2, CXADR, CCDC120; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers FBXO46's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers FBXO46's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 160]]; 27 genes; this gene is in the **+** arm (projection on the module's main direction 0.661). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (7.2, 0.2); signed map (-25.2, 29.3). **Vector** length 82.5, 15.5% of its response variance represented; |z| ≥ 3 in 815 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +5.0 | +5.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +4.3 | +5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.0 | +1.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.8 | +2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.8 | +2.4 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.9 | +1.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | +1.9 | +2.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.9 | +3.4 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -4.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.5 | -8.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -3.4 | -2.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~2% of this change | -3.1 | -3.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -3.0 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.6 | -4.0 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -4.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 46 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.32 — chr19:45,710,629-45,730,896 (-) |
| Ensembl biotype | protein_coding |
| Also known as | 20D7-FC4, Fbx46; previously FBXO34L |
| Gene groups (HGNC) | F-boxes other |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6PJ61](https://www.uniprot.org/uniprotkb/Q6PJ61) (F-box only protein 46):

> Substrate-recognition component of the SCF(FBXO46) protein ligase complex, which mediates the ubiquitination and degradation of target proteins. In absence of stress, the SCF(FBXO46) complex catalyzes ubiquitination and degradation of MTOR-phosphorylated FBXO31.

**Summary**, from NCBI Gene [23403](https://www.ncbi.nlm.nih.gov/gene/23403):

> Members of the F-box protein family, such as FBXO46, are characterized by an approximately 40-amino acid F-box motif. SCF complexes, formed by SKP1 (MIM 601434), cullin (see CUL1; MIM 603134), and F-box proteins, act as protein-ubiquitin ligases. F-box proteins interact with SKP1 through the F box, and they interact with ubiquitination targets through other protein interaction domains (Jin et al., 2004 [PubMed 15520277]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:25069](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25069) · Entrez [23403](https://www.ncbi.nlm.nih.gov/gene/23403) · UniProt [Q6PJ61](https://www.uniprot.org/uniprotkb/Q6PJ61) · Ensembl [ENSG00000177051](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177051)

## Data

Gene col 10784: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10784); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10784, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10784]; `tensor/DDL_lfc|DDL_z.npy` [10784]; `embed/gene_vectors.npy` [10784]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10784 or target_col == 10784). Every well: [[FBXO46 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO46.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
