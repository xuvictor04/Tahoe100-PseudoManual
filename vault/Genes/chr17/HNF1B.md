---
symbol: "HNF1B"
type: "gene"
col: 15850
ensembl_id: "ENSG00000275410"
name: "HNF1 homeobox B"
location: "17q12"
module: 8
arm: "+"
pooled_cpm: 17.98
n_lines_expressing: 19
n_dd_up: 18
n_dd_down: 5
n_dd_up_clean: 8
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 49
direction_downstream: 75
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# HNF1B

*HNF1 homeobox B* — 17q12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.50× (z +11.8, q 4e-29, up in 0 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.79× (z +10.6, q 1e-23, up in 5 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.583× (z -6.9, q 3e-09, down in 17 of 17 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNF1A-AS1]] (+0.62, fdr 7e-06), [[FAAH2]] (+0.58, fdr 1e-05), [[SLC44A4]] (+0.57, fdr 1e-05); moves opposite to [[SNED1]] (-0.46, fdr 5e-05), [[ZNF891]] (-0.45, fdr 3e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 49 arrows point to it, the strongest [[HNF4G]] → it (grade B ⚠); 75 go from it, the strongest it → [[ATP1B1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15850.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.50×** | +11.8 | 4e-29 | 0/15 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +10.6 | 1e-23 | 5/17 (LS 180, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.25×** | +10.1 | 2e-21 | 0/13 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +8.1 | 9e-14 | 3/17 (LS 180, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.45×** | +6.7 | 2e-09 | 2/17 (A498, CFPAC-1) | top dose only | cell-cycle shift (explains ~16% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +5.5 | 3e-06 | 4/17 (SNU-423, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +5.4 | 6e-06 | 0/15 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +4.9 | 6e-05 | 1/16 (SNU-423) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +4.1 | 0.002 | 0/14 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +4.0 | 0.003 | 0/16 | top dose only | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +4.0 | 0.004 | 0/13 | top dose only | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.52×** | +3.8 | 0.006 | 0/15 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.73×** | +3.7 | 0.010 | 0/10 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.32×** | +3.6 | 0.013 | 0/17 | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.037 | 0/17 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 0.05 µM |  | **1.29×** | +3.3 | 0.037 | 2/17 (COLO 205, Panc 03.27) | inconsistent across doses |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.062 | 0/17 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15850.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.583×** | -6.9 | 3e-09 | 17/17 (KATO III, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.622×** | -6.1 | 4e-07 | 15/17 (HEC-1-A, KATO III, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.628×** | -5.9 | 5e-07 | 16/17 (KATO III, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.660×** | -5.3 | 2e-05 | 15/17 (A498, KATO III, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.723×** | -4.2 | 0.004 | 9/17 (A498, SW 900, …) | all doses, flat |  |
| [[vincristine (drug)]] 0.05 µM |  | 0.748× | -3.3 | 0.10 | 2/17 (KATO III, HT-29) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | 0.773× | -3.1 | 0.12 | 10/17 (NCI-H2347, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Paclitaxel (drug)]] 5 µM |  | 0.628× | -3.1 | 0.12 | 0/17 | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.776× | -3.1 | 0.12 | 2/17 (KATO III, CFPAC-1) | top dose only |  |
| [[9-ING-41 (drug)]] 5 µM |  | 0.633× | -3.1 | 0.12 | 0/17 | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15850. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 92.3 | 0 | 15 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0448× (z -20.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.0752× (z -17.5) |
| [[HEC-1-A (line)]] | alt | 58.1 | 0 | 6 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.122× (z -16.0) |
| [[A498 (line)]] | wt | 45.3 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.195× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.216× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 172 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -16.3) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.280× (z -11.1) |
| [[Panc 03.27 (line)]] | alt | 46.8 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.207× (z -9.9) |
| [[NCI-H2030 (line)]] | alt | 51.5 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.341× (z -11.7) |
| [[A549 (line)]] | wt | 40.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.188× (z -10.7) |
| [[COLO 205 (line)]] | alt | 24.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.152× (z -12.0) |
| [[NCI-H2347 (line)]] | alt | 26.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.157× (z -13.1) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -8.9) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 27.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.132× (z -11.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.897 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 43.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.949 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.974 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.900 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.54 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.17 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15850), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNF1A-AS1]] | +0.62 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[FAAH2]] | +0.58 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[SLC44A4]] | +0.57 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[EPCAM-DT]] | +0.57 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[SLC37A1]] | +0.57 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[ST14]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[RHBDL2]] | +0.57 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[ADGRF1]] | +0.56 | +0.59 / +0.48 | both halves | 2e-05 |  |
| [[TRIM31]] | +0.56 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[FRK]] | +0.56 | +0.61 / +0.47 | both halves | 2e-05 |  |
| [[PLCH1]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[ERBB3]] | +0.55 | +0.56 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNED1]] | -0.46 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[ZNF891]] | -0.45 | -0.27 / -0.40 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*49 arrows, 49 of them with an alert ⚠; grade A 0, B 8, C 41. Shown: the 12 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HNF4G]] | B | HNF4G activity raises HNF1B's level | lines that do not express HNF4G (16) vs lines expressing it (34) | 3.56× lower at baseline in the lines without HNF4G | 0.023 | ⚠ within organs, on part of the lines; also absent: MPZL3, ELF3, ARHGEF5 |
| [[SPATA6L]] | B | SPATA6L activity raises HNF1B's level | lines that do not express SPATA6L (15) vs lines expressing it (35) | 2.87× lower at baseline in the lines without SPATA6L | 0.038 | ⚠ within organs, on part of the lines; also absent: RHOV, ANO9, ELF3; maybe low, not absent |
| [[DOCK11]] | B | DOCK11 activity lowers HNF1B's level | lines that do not express DOCK11 (13) vs lines expressing it (37) | 3.07× higher at baseline in the lines without DOCK11 | 0.051 | ⚠ within organs, on part of the lines; also absent: KIF26A, HOXD8, ABCA17P; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises HNF1B's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ATP8B1]] | B | ATP8B1 activity raises HNF1B's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 3.58× lower at baseline in the lines without ATP8B1 | 0.069 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[SLC44A3]] | B | SLC44A3 activity raises HNF1B's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 3.06× lower at baseline in the lines without SLC44A3 | 0.072 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[TMEM51-AS1]] | B | TMEM51-AS1 activity raises HNF1B's level | lines that do not express TMEM51-AS1 (13) vs lines expressing it (37) | 3.19× lower at baseline in the lines without TMEM51-AS1 | 0.089 | ⚠ within organs, on part of the lines; also absent: RAB17, PLEKHG1, EPHA1; maybe low, not absent |
| [[EPCAM-DT]] | B | EPCAM-DT activity raises HNF1B's level | lines that do not express EPCAM-DT (13) vs lines expressing it (37) | 3.49× lower at baseline in the lines without EPCAM-DT | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000267737, GPRC5C, PLEKHG1 |
| [[INAVA]], [[MROH3P]] | C | INAVA, MROH3P activity raises HNF1B's level | lines that do not express INAVA, MROH3P (29) vs lines expressing them (21) | 5.84× lower at baseline in the lines without INAVA, MROH3P | 0.001 | ⚠ within organs, on part of the lines; also absent: CDH1, MAL2, B3GNT3; co-absent with the target; co-absent genes |
| [[PDZK1IP1]] | C | PDZK1IP1 activity raises HNF1B's level | lines that do not express PDZK1IP1 (32) vs lines expressing it (18) | 6.88× lower at baseline in the lines without PDZK1IP1 | 0.001 | ⚠ within organs, on part of the lines; also absent: MUC5B, UCA1, PRSS8; co-absent with the target |
| [[SLC44A4]] | C | SLC44A4 activity raises HNF1B's level | lines that do not express SLC44A4 (37) vs lines expressing it (13) | 5.87× lower at baseline in the lines without SLC44A4 | 0.003 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC1, LCN2, NPSR1; co-absent with the target |
| [[GRHL2]] | C | GRHL2 activity raises HNF1B's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 5.34× lower at baseline in the lines without GRHL2 | 0.005 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent with the target |

### Downstream of this gene

*75 arrows, 75 of them with an alert ⚠; grade A 0, B 30, C 45. Shown: the 12 strongest; 63 more arrows (63 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP1B1]] | B | HNF1B activity raises ATP1B1's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 3.73× lower at baseline in the lines without HNF1B | 6e-04 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |
| [[TMEM51]] | B | HNF1B activity raises TMEM51's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 2.13× lower at baseline in the lines without HNF1B | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |
| [[TMEM51-AS1]] | B | HNF1B activity raises TMEM51-AS1's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 2.23× lower at baseline in the lines without HNF1B | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |
| [[SLC44A3]] | B | HNF1B activity raises SLC44A3's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 2.84× lower at baseline in the lines without HNF1B | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |
| [[EPCAM-DT]] | B | HNF1B activity raises EPCAM-DT's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 2.74× lower at baseline in the lines without HNF1B | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |
| [[EFNA1]] | B | HNF1B activity raises EFNA1's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 2.85× lower at baseline in the lines without HNF1B | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |
| [[SAMD12]] | B | HNF1B activity raises SAMD12's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 2.97× lower at baseline in the lines without HNF1B | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |
| [[BCL2L15]] | B | HNF1B activity raises BCL2L15's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 2.16× lower at baseline in the lines without HNF1B | 0.015 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |
| [[SLC37A1]] | B | HNF1B activity raises SLC37A1's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 2.24× lower at baseline in the lines without HNF1B | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |
| [[SLC11A2]] | B | HNF1B activity raises SLC11A2's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 1.54× lower at baseline in the lines without HNF1B | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |
| [[GPRC5C]] | B | HNF1B activity raises GPRC5C's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 3.45× lower at baseline in the lines without HNF1B | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |
| [[SPATA6L]] | B | HNF1B activity raises SPATA6L's level | lines that do not express HNF1B (31) vs lines expressing it (19) | 3.05× lower at baseline in the lines without HNF1B | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000254261, PDZK1IP1, ADGRF1 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.645). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.6, 53.6); signed map (56.4, 0.6). **Vector** length 58.2, 17.8% of its response variance represented; |z| ≥ 3 in 446 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.8 | +10.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +8.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +1.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +1.6 | +6.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.5 | +2.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.3 | +1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.1 | +1.8 |
| fall | [[Auranofin (drug)]] 5 µM |  | -3.5 | -5.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.9 | -1.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.5 | -6.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -4.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -0.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.2 | -1.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | HNF1 homeobox B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q12 — chr17:37,686,431-37,745,059 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LFB3, VHNF1, HNF1beta, MODY5, HNF1β; previously TCF2 |
| Gene groups (HGNC) | HNF class homeoboxes |
| Reactome | 5 pathways, smallest: Regulation of gene expression in early pancreatic precursor cells; Nephron development; Regulation of gene expression in late stage (branching morphogenesis) pancreatic bud precursor cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P35680](https://www.uniprot.org/uniprotkb/P35680) (Hepatocyte nuclear factor 1-beta):

> Transcription factor that binds to the inverted palindrome 5'-GTTAATNATTAAC-3'. Binds to the FPC element in the cAMP regulatory unit of the PLAU gene (By similarity). Transcriptional activity is increased by coactivator PCBD1.

**Summary**, from NCBI Gene [6928](https://www.ncbi.nlm.nih.gov/gene/6928):

> This gene encodes a member of the homeodomain-containing superfamily of transcription factors. The protein binds to DNA as either a homodimer, or a heterodimer with the related protein hepatocyte nuclear factor 1-alpha. The gene has been shown to function in nephron development, and regulates development of the embryonic pancreas. Mutations in this gene result in renal cysts and diabetes syndrome and noninsulin-dependent diabetes mellitus, and expression of this gene is altered in some types of …

**Accessions** — [HGNC:11630](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11630) · Entrez [6928](https://www.ncbi.nlm.nih.gov/gene/6928) · UniProt [P35680](https://www.uniprot.org/uniprotkb/P35680) · Ensembl [ENSG00000275410](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000275410)

## Data

Gene col 15850: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15850); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15850, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15850]; `tensor/DDL_lfc|DDL_z.npy` [15850]; `embed/gene_vectors.npy` [15850]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15850 or target_col == 15850). Every well: [[HNF1B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HNF1B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
