---
symbol: "RAP1GAP"
type: "gene"
col: 1165
ensembl_id: "ENSG00000076864"
name: "RAP1 GTPase activating protein"
location: "1p36.12"
module: 189
arm: "+"
pooled_cpm: 10.87
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 7
direction_downstream: 0
tags: ["gene", "module/189"]
generated_by: "tahoemap"
---

# RAP1GAP

*RAP1 GTPase activating protein* — 1p36.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.45× (z +17.3, q 0e+00, up in 12 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.86× (z +12.7, q 7e-35, up in 30 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.506× (z -9.9, q 2e-20, down in 29 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPK8IP1]] (+0.70, fdr 7e-06), [[ZDHHC11B]] (+0.66, fdr 9e-06), [[SYT5]] (+0.62, fdr 1e-05); moves opposite to [[ATR]] (-0.59, fdr 2e-05), [[LARS2]] (-0.53, fdr 3e-05), [[NUDCD1]] (-0.51, fdr 2e-05).
> It is in [[Module 189]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[PPL]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1165.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.45×** | +17.3 | 0e+00 | 12/16 (SW1417, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.92×** | +15.6 | 0e+00 | 28/34 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.86×** | +12.7 | 7e-35 | 30/43 (J82, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **2.37×** | +12.6 | 5e-34 | 34/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.41×** | +11.8 | 3e-30 | 16/25 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.25×** | +11.8 | 5e-30 | 33/47 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.56×** | +9.1 | 7e-18 | 28/46 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.72×** | +7.9 | 2e-13 | 24/47 (KATO III, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.58×** | +6.6 | 2e-09 | 19/45 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +6.3 | 2e-08 | 19/48 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pimitespib (drug)]] 5 µM |  | **1.59×** | +3.5 | 0.022 | 2/35 (J82, HT-29) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.053 | 4/45 (KATO III, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1165.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.506×** | -9.9 | 2e-20 | 29/45 (hTERT-HPNE, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.611×** | -7.2 | 2e-10 | 27/45 (H4, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.647×** | -6.3 | 5e-08 | 24/48 (HT-29, CFPAC-1, …) | two highest doses | cell-cycle shift (explains ~17% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.651×** | -6.2 | 6e-08 | 21/45 (HT-29, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.538×** | -4.7 | 3e-04 | 14/46 (SW480, CFPAC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.748×** | -4.2 | 0.002 | 15/47 (HT-29, CFPAC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.770×** | -3.8 | 0.012 | 13/45 (NCI-H2030, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Berbamine (drug)]] 0.05 µM |  | **0.777×** | -3.7 | 0.017 | 9/46 (HCT15, C32, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.775×** | -3.6 | 0.024 | 15/43 (HT-29, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.849× | -3.4 | 0.045 | 10/48 (CFPAC-1, NCI-H1573, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1165. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 19.8 | 5 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.09× (z +12.1) | — |
| [[HT-29 (line)]] | alt | 42.6 | 0 | 5 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.382× (z -9.2) |
| [[NCI-H460 (line)]] | wt | 5.11 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 14.0× (z +13.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 3.72× (z +9.5) | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.182× (z -8.7) |
| [[PANC-1 (line)]] | alt | 5.35 | 4 | 0 | [[Harringtonine (drug)]] 5 µM 7.57× (z +11.2) | — |
| [[SW1417 (line)]] | alt | 18.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 5.43× (z +10.9) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.333× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 4.00 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.8× (z +12.8) | — |
| [[C32 (line)]] | wt | 14.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.0× (z +10.5) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 12.6 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0801× (z -9.4) |
| [[J82 (line)]] | alt | 6.14 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +15.1) | — |
| [[NCI-H2030 (line)]] | alt | 8.82 | 0 | 2 (1 ⚠) | — | [[Rosiglitazone (drug)]] 5 µM 0.0607× (z -13.1) |
| [[SW480 (line)]] | alt | 12.7 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.246× (z -9.4) |
| [[BT-474 (line)]] | alt | 14.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.84× (z +10.3) | — |
| [[KATO III (line)]] | alt | 12.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +9.6) | — |
| [[LoVo (line)]] | wt | 10.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +8.6) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 13.9 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0402× (z -9.6) |
| [[SHP-77 (line)]] | alt | 35.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.73× (z +9.4) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.92 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.62 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.82 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 4.02 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.81 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.98 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.82 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.59 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1165), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK8IP1]] | +0.70 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[ZDHHC11B]] | +0.66 | +0.57 / +0.63 | both halves | 9e-06 |  |
| [[SYT5]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[VAV1]] | +0.61 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[MYO7A]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[CDC42BPG]] | +0.60 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[LRP1]] | +0.59 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[DDAH2]] | +0.59 | +0.51 / +0.45 | both halves | 3e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[TPPP]] | +0.58 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[CDA]] | +0.57 | +0.43 / +0.57 | both halves | 3e-05 | pathway: HALLMARK_XENOBIOTIC_METABOLISM |
| [[AHDC1]] | +0.57 | +0.45 / +0.52 | both halves | 3e-05 |  |
| [[PLCH2]] | +0.56 | +0.44 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATR]] | -0.59 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[LARS2]] | -0.53 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[NUDCD1]] | -0.51 | -0.61 / -0.48 | both halves | 2e-05 |  |
| [[PRR14L]] | -0.51 | -0.39 / -0.54 | both halves | 5e-05 |  |
| [[TMEM11-DT]] | -0.49 | -0.50 / -0.40 | both halves | 4e-05 |  |
| [[NR2C2AP]] | -0.49 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[ENOX2]] | -0.47 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[WDR53]] | -0.47 | -0.26 / -0.51 | both halves | 4e-04 |  |
| [[PKD2]] | -0.47 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[TRMT61B]] | -0.46 | -0.41 / -0.41 | both halves | 4e-05 |  |
| [[CASP8AP2]] | -0.46 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[NR2C2]] | -0.46 | -0.40 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPL]] | B | PPL activity raises RAP1GAP's level | lines that do not express PPL (19) vs lines expressing it (31) | 1.65× lower at baseline in the lines without PPL | 0.032 | ⚠ within organs, on part of the lines; also absent: EPPK1, SMPDL3B, PLEKHG6 |
| [[EPHB3]] | B | EPHB3 activity raises RAP1GAP's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 1.63× lower at baseline in the lines without EPHB3 | 0.036 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| [[SYTL1]] | B | SYTL1 activity raises RAP1GAP's level | lines that do not express SYTL1 (15) vs lines expressing it (35) | 1.73× lower at baseline in the lines without SYTL1 | 0.057 | ⚠ within organs, on part of the lines; also absent: ATAD3C, PLEKHG6, SORL1; maybe low, not absent |
| [[RCN3]] | B | RCN3 activity raises RAP1GAP's level | lines that do not express RCN3 (11) vs lines expressing it (39) | 1.71× lower at baseline in the lines without RCN3 | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ADGRG1]] | B | ADGRG1 activity raises RAP1GAP's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 1.35× lower at baseline in the lines without ADGRG1 | 0.085 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers RAP1GAP's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers RAP1GAP's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 189]]; 18 genes; every member is in the + arm (projection on the module's main direction 0.531). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.4, 18.3); signed map (-2.4, 23.9). **Vector** length 84.7, 15.9% of its response variance represented; |z| ≥ 3 in 1,112 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.9 | +17.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.3 | +15.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.2 | +11.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.1 | +9.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +12.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.6 | +2.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +1.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +2.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -4.3 | -9.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -3.9 | -7.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~1% of this change | -3.7 | -1.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~17% of this change | -3.6 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | -6.3 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.3 | -3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -3.4 |
|  | [[vincristine (drug)]] 0.05 µM |  | -2.0 | -1.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.9 | -1.9 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | RAP1 GTPase activating protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.12 — chr1:21,596,221-21,669,357 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0474, RAP1GAP1, RAP1GAPII; previously RAP1GA1 |
| Hallmark sets | XENOBIOTIC_METABOLISM, HEME_METABOLISM |
| Reactome | 5 pathways, smallest: Rap1 signalling; RET signaling; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [P47736](https://www.uniprot.org/uniprotkb/P47736) (Rap1 GTPase-activating protein 1):

> GTPase activator for the nuclear Ras-related regulatory protein RAP-1A (KREV-1), converting it to the putatively inactive GDP-bound state.

**Summary**, from NCBI Gene [5909](https://www.ncbi.nlm.nih.gov/gene/5909):

> This gene encodes a type of GTPase-activating-protein (GAP) that down-regulates the activity of the ras-related RAP1 protein. RAP1 acts as a molecular switch by cycling between an inactive GDP-bound form and an active GTP-bound form. The product of this gene, RAP1GAP, promotes the hydrolysis of bound GTP and hence returns RAP1 to the inactive state whereas other proteins, guanine nucleotide exchange factors (GEFs), act as RAP1 activators by facilitating the conversion of RAP1 from the GDP- to …

**Accessions** — [HGNC:9858](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9858) · Entrez [5909](https://www.ncbi.nlm.nih.gov/gene/5909) · UniProt [P47736](https://www.uniprot.org/uniprotkb/P47736) · Ensembl [ENSG00000076864](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076864)

## Data

Gene col 1165: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1165); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1165, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1165]; `tensor/DDL_lfc|DDL_z.npy` [1165]; `embed/gene_vectors.npy` [1165]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1165 or target_col == 1165). Every well: [[RAP1GAP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAP1GAP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
