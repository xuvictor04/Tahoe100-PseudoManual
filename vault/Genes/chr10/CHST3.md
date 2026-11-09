---
symbol: "CHST3"
type: "gene"
col: 4380
ensembl_id: "ENSG00000122863"
name: "carbohydrate sulfotransferase 3"
location: "10q22.1"
module: 94
arm: "+"
pooled_cpm: 18.22
n_lines_expressing: 46
n_dd_up: 23
n_dd_down: 5
n_dd_up_clean: 18
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/094"]
generated_by: "tahoemap"
---

# CHST3

*carbohydrate sulfotransferase 3* — 10q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (5 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 5 µM: 3.07× (z +17.0, q 0e+00, up in 35 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.424× (z -13.5, q 9e-39, down in 33 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC16A14]] (+0.65, fdr 1e-05), [[FAM169A]] (+0.64, fdr 3e-05), [[CFL2]] (+0.62, fdr 1e-05); moves opposite to [[PIBF1]] (-0.57, fdr 2e-05), [[SBNO1]] (-0.52, fdr 3e-05), [[SCART1]] (-0.51, fdr 1e-04).
> It is in [[Module 094]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PYGO1]] → it (grade B ⚠); 5 go from it, the strongest it → [[NSD1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4380.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **3.07×** | +17.0 | 0e+00 | 35/44 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.78×** | +12.8 | 5e-35 | 31/44 (PANC-1, LoVo, …) | all doses, flat | low cells (technical?); cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.71×** | +12.0 | 5e-31 | 26/44 (Panc 03.27, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 0.05 µM |  | **2.13×** | +11.9 | 1e-30 | 36/44 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.04×** | +11.5 | 2e-28 | 33/44 (Panc 03.27, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.88×** | +10.0 | 2e-21 | 30/44 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.81×** | +9.3 | 7e-19 | 28/44 (PANC-1, LS 180, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.56×** | +7.0 | 2e-10 | 28/43 (LoVo, LS 180, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.24×** | +6.6 | 2e-09 | 24/41 (HEC-1-A, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.49×** | +6.3 | 2e-08 | 22/44 (SW1417, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.43×** | +5.7 | 8e-07 | 19/44 (HS-578T, A-172, …) | all doses, stronger at high dose |  |
| [[Radotinib (drug)]] 5 µM |  | **1.26×** | +5.2 | 9e-06 | 17/44 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.73×** | +4.5 | 3e-04 | 16/35 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~10% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.29×** | +4.1 | 0.002 | 16/43 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.28×** | +3.8 | 0.004 | 14/35 (A498, SNU-423, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.007 | 17/43 (HS-578T, NCI-H1792, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.5 | 0.015 | 10/42 (HS-578T, SW48, …) | all doses, stronger at high dose | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4380.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.424×** | -13.5 | 9e-39 | 33/44 (HEC-1-A, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.436×** | -13.0 | 2e-36 | 36/44 (HEC-1-A, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.648×** | -6.8 | 2e-09 | 25/43 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.740×** | -4.7 | 3e-04 | 13/44 (HOP62, NCI-H2347, …) | top dose only |  |
| [[Isocorydine (drug)]] 0.5 µM |  | **0.792×** | -3.7 | 0.029 | 10/42 (Panc 03.27, SW 900, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4380. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 65.3 | 1 | 3 | [[PH-797804 (drug)]] 5 µM 5.22× (z +8.7) | [[Panobinostat (drug)]] 0.5 µM 0.168× (z -18.0) |
| [[NCI-H2347 (line)]] | alt | 23.6 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +14.9) | [[Panobinostat (drug)]] 0.5 µM 0.310× (z -9.4) |
| [[A-172 (line)]] | wt | 58.2 | 1 | 2 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.276× (z -10.5) |
| [[C-33 A (line)]] | alt | 26.9 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0922× (z -13.2) |
| [[C32 (line)]] | wt | 45.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0662× (z -20.1) |
| [[HS-578T (line)]] | alt | 27.6 | 3 | 0 | [[Harringtonine (drug)]] 5 µM 8.58× (z +12.6) | — |
| [[J82 (line)]] | alt | 19.9 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.34× (z +14.9) | [[Panobinostat (drug)]] 0.5 µM 0.244× (z -10.1) |
| [[LoVo (line)]] | wt | 10.9 | 2 | 1 | [[Selinexor (drug)]] 5 µM 3.10× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.366× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 15.3 | 1 | 2 | [[Homoharringtonine (drug)]] 0.5 µM 5.39× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.207× (z -8.6) |
| [[Panc 03.27 (line)]] | alt | 28.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.31× (z +20.0) | — |
| [[PANC-1 (line)]] | alt | 25.0 | 3 | 0 | [[Selinexor (drug)]] 5 µM 2.28× (z +11.0) | — |
| [[CFPAC-1 (line)]] | alt | 18.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +15.3) | — |
| [[KATO III (line)]] | alt | 8.65 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +10.5) | — |
| [[LS 180 (line)]] | wt | 9.56 | 2 | 0 | [[Selinexor (drug)]] 5 µM 4.21× (z +10.0) | — |
| [[SK-MEL-2 (line)]] | alt | 15.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -11.8) |
| [[SW1417 (line)]] | alt | 8.47 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.6× (z +16.0) | — |
| [[SW48 (line)]] | wt | 33.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 6.13× (z +8.9) | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -11.3) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 67.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0662× (z -12.3) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 9.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.60× (z +12.1) | — |
| [[BT-474 (line)]] | alt | 10.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.71× (z +8.9) | — |
| [[HepG2_C3A (line)]] | wt | 31.3 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.12× (z +8.9) | — |
| [[HOP62 (line)]] | alt | 9.98 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 10.6× (z +13.5) | — |
| [[Hs 766T (line)]] | wt | 17.2 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.192× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 10.6 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 19.8× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 15.3 | 1 | 0 | [[Selinexor (drug)]] 5 µM 3.13× (z +9.5) | — |
| [[NCI-H1573 (line)]] | alt | 9.07 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.183× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 16.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 16.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.135× (z -10.1) |
| [[SNU-1 (line)]] | wt | 14.3 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0993× (z -8.5) |
| [[A-427 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 32.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.31 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 5.21 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4380), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC16A14]] | +0.65 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[FAM169A]] | +0.64 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[CFL2]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[ZNF391]] | +0.62 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[XPO1]] | +0.61 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[SLC16A9]] | +0.61 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[SDSL]] | +0.60 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[ZNF441]] | +0.60 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[KLHL42]] | +0.59 | +0.59 / +0.40 | both halves | 4e-05 |  |
| [[POMK]] | +0.59 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[SLC43A2]] | +0.59 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[PHYH]] | +0.58 | +0.44 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIBF1]] | -0.57 | -0.47 / -0.46 | both halves | 2e-05 |  |
| [[SBNO1]] | -0.52 | -0.43 / -0.44 | both halves | 3e-05 |  |
| [[SCART1]] | -0.51 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[SENP5]] | -0.49 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[SLC25A42]] | -0.49 | -0.43 / -0.29 | both halves | 2e-04 |  |
| [[POLR2J4]] | -0.49 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[SLC25A5]] | -0.48 | -0.27 / -0.48 | both halves | 3e-04 |  |
| [[ODF2]] | -0.48 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[WIPI1]] | -0.48 | -0.36 / -0.40 | both halves | 9e-05 |  |
| [[COX6A1]] | -0.48 | -0.37 / -0.38 | both halves | 7e-05 |  |
| [[RASA4B]] | -0.48 | -0.48 / -0.34 | both halves | 1e-04 |  |
| [[GLCCI1]] | -0.47 | -0.33 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PYGO1]] | B | PYGO1 activity raises CHST3's level | lines that do not express PYGO1 (16) vs lines expressing it (34) | 2.00× lower at baseline in the lines without PYGO1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with ACVR2A; also absent: MIR130AHG, RBMS3, TCF7L1 |
| [[SUCLG2-DT]] | B | SUCLG2-DT activity raises CHST3's level | lines that do not express SUCLG2-DT (7) vs lines expressing it (43) | 2.82× lower at baseline in the lines without SUCLG2-DT | 0.020 | ⚠ within organs, on part of the lines; also absent: TMCC2, DRAM1, ELK3; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises CHST3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 0, C 5.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NSD1]] | C | CHST3 activity raises NSD1's level | lines that do not express CHST3 (4) vs lines expressing it (46) | 1.54× lower at baseline in the lines without CHST3 | 0.005 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HOMER3, RGS10, ENSG00000290876 |
| [[DLG5]] | C | CHST3 activity raises DLG5's level | lines that do not express CHST3 (4) vs lines expressing it (46) | 1.50× lower at baseline in the lines without CHST3 | 0.022 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HOMER3, RGS10, ENSG00000290876 |
| [[SUCLG2-DT]] | C | CHST3 activity raises SUCLG2-DT's level | lines that do not express CHST3 (4) vs lines expressing it (46) | 3.06× lower at baseline in the lines without CHST3 | 0.063 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HOMER3, RGS10, ENSG00000290876 |
| [[TP53I3]] | C | CHST3 activity raises TP53I3's level | lines that do not express CHST3 (4) vs lines expressing it (46) | 1.59× lower at baseline in the lines without CHST3 | 0.086 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HOMER3, RGS10, ENSG00000290876 |
| cells under [[Ixazomib (drug)]] 5 µM | C | CHST3 activity lowers the cells' numbers under Ixazomib 5 µM (makes them more sensitive) | lines that do not express CHST3 (4) vs lines expressing it (44) | the lines without CHST3: 1.45× the cells of the other lines | 0.090 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HOMER3, RGS10, ENSG00000290876 |

## Where it sits

- **Module**: [[Module 094]]; 49 genes; every member is in the + arm (projection on the module's main direction 0.681). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-23.7, 23.3); signed map (19.1, -31.1). **Vector** length 105, 23.9% of its response variance represented; |z| ≥ 3 in 1,077 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +9.9 | +12.8 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +7.4 | +10.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.8 | +17.0 |
|  | [[Selinexor (drug)]] 0.5 µM |  | +6.5 | +9.3 |
|  | [[Selinexor (drug)]] 0.05 µM |  | +5.5 | +11.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.1 | +5.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.1 | +5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +2.3 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +3.3 | +7.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.2 | +6.6 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -5.0 | -13.5 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.8 | -13.0 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.9 | -6.8 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -3.3 | -4.7 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.2 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.8 | -0.2 |
|  | [[Vilanterol (drug)]] 5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | carbohydrate sulfotransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.1 — chr10:71,964,395-72,013,558 (+) |
| Ensembl biotype | protein_coding |
| Also known as | C6ST, C6ST1 |
| Gene groups (HGNC) | Sulfotransferases, membrane bound |
| Hallmark sets | HYPOXIA |
| Reactome | 10 pathways, smallest: Defective CHST3 causes SEDCJD; CS-GAG biosynthesis; Keratan sulfate biosynthesis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7LGC8](https://www.uniprot.org/uniprotkb/Q7LGC8) (Carbohydrate sulfotransferase 3):

> Sulfotransferase that utilizes 3'-phospho-5'-adenylyl sulfate (PAPS) as sulfonate donor to catalyze the transfer of sulfate to position 6 of the N-acetylgalactosamine (GalNAc) residue of chondroitin. Chondroitin sulfate constitutes the predominant proteoglycan present in cartilage and is distributed on the surfaces of many cells and extracellular matrices. Catalyzes with a lower efficiency the sulfation of Gal residues of keratan sulfate, another glycosaminoglycan. Can also catalyze the …

**Summary**, from NCBI Gene [9469](https://www.ncbi.nlm.nih.gov/gene/9469):

> This gene encodes an enzyme which catalyzes the sulfation of chondroitin, a proteoglycan found in the extracellular matrix and most cells which is involved in cell migration and differentiation. Mutations in this gene are associated with spondylepiphyseal dysplasia and humerospinal dysostosis. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:1971](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1971) · Entrez [9469](https://www.ncbi.nlm.nih.gov/gene/9469) · UniProt [Q7LGC8](https://www.uniprot.org/uniprotkb/Q7LGC8) · Ensembl [ENSG00000122863](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122863)

## Data

Gene col 4380: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4380); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4380, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4380]; `tensor/DDL_lfc|DDL_z.npy` [4380]; `embed/gene_vectors.npy` [4380]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4380 or target_col == 4380). Every well: [[CHST3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHST3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
