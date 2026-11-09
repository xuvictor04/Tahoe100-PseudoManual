---
symbol: "BTN3A2"
type: "gene"
col: 11818
ensembl_id: "ENSG00000186470"
name: "butyrophilin subfamily 3 member A2"
location: "6p22.2"
module: 70
arm: "+"
pooled_cpm: 21.37
n_lines_expressing: 48
n_dd_up: 2
n_dd_down: 27
n_dd_up_clean: 2
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# BTN3A2

*butyrophilin subfamily 3 member A2* — 6p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.77× (z +5.6, q 1e-05, up in 33 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.185× (z -24.2, q 0e+00, down in 45 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BTN3A1]] (+0.73, fdr 7e-06, ⚠ same locus), [[BTN3A3]] (+0.68, fdr 7e-06), [[UBE2L6]] (+0.64, fdr 1e-05), [[PSMB9]] (+0.62, fdr 1e-05); moves opposite to [[CRYGS]] (-0.59, fdr 2e-05), [[SEPTIN10]] (-0.57, fdr 1e-05), [[KLF13]] (-0.56, fdr 1e-05).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MAP2K1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11818.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.77×** | +5.6 | 1e-05 | 33/45 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.50×** | +4.0 | 0.022 | 20/45 (RKO, MIA PaCa-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.36× | +3.4 | 0.10 | 21/46 (MIA PaCa-2, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.39× | +3.4 | 0.10 | 21/46 (KATO III, NCI-H1792, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.38× | +3.3 | 0.11 | 18/45 (MIA PaCa-2, Hs 766T, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11818.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.185×** | -24.2 | 0e+00 | 45/45 (LoVo, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.277×** | -13.0 | 3e-36 | 42/43 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.359×** | -10.4 | 7e-23 | 45/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.374×** | -10.0 | 3e-21 | 41/46 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.383×** | -9.7 | 3e-20 | 39/46 (HS-578T, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.395×** | -9.0 | 2e-17 | 38/45 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.429×** | -8.6 | 1e-15 | 37/46 (PANC-1, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.454×** | -8.0 | 1e-13 | 37/46 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.458×** | -7.9 | 2e-13 | 39/45 (SW480, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.467×** | -7.7 | 8e-13 | 37/46 (PANC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.480×** | -7.4 | 6e-12 | 38/46 (HEC-1-A, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.646×** | -6.2 | 2e-08 | 34/44 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.309×** | -6.2 | 2e-08 | 36/46 (LoVo, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.547×** | -6.1 | 4e-08 | 29/46 (KATO III, SW480, …) | rises with dose | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.629×** | -4.7 | 1e-04 | 30/46 (H4, NCI-H23, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.433×** | -4.4 | 3e-04 | 24/44 (SW480, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.651×** | -4.3 | 5e-04 | 20/45 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.742×** | -4.2 | 7e-04 | 28/46 (CFPAC-1, NCI-H1573, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11818. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 16.1 | 0 | 12 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -21.8) |
| [[PANC-1 (line)]] | alt | 14.6 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0937× (z -22.9) |
| [[HEC-1-A (line)]] | alt | 23.2 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.178× (z -12.1) |
| [[LoVo (line)]] | wt | 41.1 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0615× (z -29.5) |
| [[A498 (line)]] | wt | 35.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -19.3) |
| [[C32 (line)]] | wt | 33.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -16.9) |
| [[HS-578T (line)]] | alt | 46.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.105× (z -23.5) |
| [[KATO III (line)]] | alt | 28.4 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -17.2) |
| [[MIA PaCa-2 (line)]] | alt | 17.5 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0846× (z -15.5) |
| [[NCI-H1792 (line)]] | alt | 30.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.147× (z -16.0) |
| [[NCI-H460 (line)]] | wt | 21.6 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -12.7) |
| [[A-427 (line)]] | wt | 14.3 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 34.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.143× (z -18.2) |
| [[COLO 205 (line)]] | alt | 30.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -12.9) |
| [[NCI-H1573 (line)]] | alt | 18.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0891× (z -19.0) |
| [[NCI-H23 (line)]] | alt | 16.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.272× (z -9.2) |
| [[SNU-423 (line)]] | alt | 63.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -22.4) |
| [[SW48 (line)]] | wt | 28.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -12.7) |
| [[A-172 (line)]] | wt | 27.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -15.6) |
| [[H4 (line)]] | wt | 31.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -13.6) |
| [[HCT15 (line)]] | alt | 13.9 | 0 | 2 (1 ⚠) | — | [[Temsirolimus (drug)]] 0.5 µM 0.108× (z -9.6) |
| [[HOP62 (line)]] | alt | 15.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -17.2) |
| [[NCI-H2030 (line)]] | alt | 7.83 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0892× (z -10.2) |
| [[RKO (line)]] | wt | 16.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -10.3) |
| [[SHP-77 (line)]] | alt | 10.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0612× (z -16.8) |
| [[SK-MEL-2 (line)]] | alt | 20.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -11.9) |
| [[SW 900 (line)]] | alt | 21.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -16.0) |
| [[A549 (line)]] | wt | 10.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0759× (z -16.1) |
| [[C-33 A (line)]] | alt | 18.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -12.5) |
| [[HT-29 (line)]] | alt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -12.4) |
| [[hTERT-HPNE (line)]] | wt | 35.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -17.0) |
| [[J82 (line)]] | alt | 43.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -12.9) |
| [[LS 180 (line)]] | wt | 12.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -11.1) |
| [[NCI-H2347 (line)]] | alt | 7.39 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -13.6) |
| [[SW1417 (line)]] | alt | 6.13 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -8.7) |
| [[AN3 CA (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.31 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11818), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BTN3A1]] | +0.73 | +0.59 / +0.82 | both halves | 7e-06 | same gene group; pathway: Butyrophilin (BTN) family interactions; STRING 993; ⚠ same locus (23.9 kb, same strand: neighbours can correlate without regulation) |
| [[BTN3A3]] | +0.68 | +0.75 / +0.73 | both halves | 7e-06 | same gene group; pathway: Butyrophilin (BTN) family interactions; STRING 960 |
| [[UBE2L6]] | +0.64 | +0.51 / +0.70 | both halves | 1e-05 | STRING 548 |
| [[PSMB9]] | +0.62 | +0.49 / +0.70 | both halves | 1e-05 | STRING 746 |
| [[RHOXF1]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[TNFSF10]] | +0.60 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[GBP4]] | +0.60 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[TLR3]] | +0.60 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[HERC5]] | +0.59 | +0.46 / +0.66 | both halves | 2e-05 |  |
| [[APOL3]] | +0.58 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[TRANK1]] | +0.58 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[GBP2]] | +0.57 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[PSMB8]] | +0.56 | +0.47 / +0.67 | both halves | 2e-05 | STRING 524 |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYGS]] | -0.59 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[SEPTIN10]] | -0.57 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[KLF13]] | -0.56 | -0.54 / -0.49 | both halves | 1e-05 |  |
| [[BCAR3]] | -0.54 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[ASB1]] | -0.52 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[SEC14L1]] | -0.52 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[GATAD2A]] | -0.52 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[LTO1]] | -0.51 | -0.37 / -0.54 | both halves | 9e-05 |  |
| [[MICAL2]] | -0.51 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[AGO2]] | -0.51 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[ERVK13-1]] | -0.50 | -0.30 / -0.51 | both halves | 2e-04 |  |
| [[ITPR3]] | -0.49 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP2K1]] | B | MAP2K1 activity lowers BTN3A2's level | compounds that target MAP2K1: 2 of 4 raise it (Cobimetinib, Trametinib) | 50% of the class's compounds vs 0.6% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds |
| [[APOL3]] | B | APOL3 activity raises BTN3A2's level | lines that do not express APOL3 (14) vs lines expressing it (36) | 1.72× lower at baseline in the lines without APOL3 | 0.074 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |
| [[ATP10D]] | B | ATP10D activity raises BTN3A2's level | lines that do not express ATP10D (5) vs lines expressing it (45) | 2.10× lower at baseline in the lines without ATP10D | 0.089 | ⚠ within organs, on part of the lines; also absent: DUBR, CLEC2D, VPS35L |
| [[UBE2L6]] | B | UBE2L6 activity raises BTN3A2's level | lines that do not express UBE2L6 (6) vs lines expressing it (44) | 1.65× lower at baseline in the lines without UBE2L6 | 0.096 | ⚠ within organs, on part of the lines; also absent: BLVRA, ADAMTSL4, HLA-B |
| [[GBP4]] | B | GBP4 activity raises BTN3A2's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.69× lower at baseline in the lines without GBP4 | 0.097 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.613). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (43.8, 52.4); signed map (60.1, 30.3). **Vector** length 82.6, 21.5% of its response variance represented; |z| ≥ 3 in 1,184 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Non-canonical inflammasome activation* (reactome, mean cos +0.57 to 4); *Antigen processing: Ub, ATP-independent proteasomal degradation* (reactome, mean cos +0.51 to 4); *CASP4 inflammasome assembly* (reactome, mean cos +0.57 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cobimetinib (drug)]] 5 µM |  | +4.0 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +2.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.2 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.0 | -2.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +3.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.9 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.7 | -1.9 |
| fall | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -4.0 | -4.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.9 | -4.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -3.8 | -0.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -6.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.7 | -7.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.1 | -3.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.9 | -2.6 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | butyrophilin subfamily 3 member A2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p22.2 — chr6:26,365,159-26,378,320 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BTN3.2 |
| Gene groups (HGNC) | Butyrophilins; V-set domain containing |
| Reactome | 2 pathways, smallest: Butyrophilin (BTN) family interactions; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P78410](https://www.uniprot.org/uniprotkb/P78410) (Butyrophilin subfamily 3 member A2):

> Plays a role in T-cell responses in the adaptive immune response. Inhibits the release of IFNG from activated T-cells.

**Summary**, from NCBI Gene [11118](https://www.ncbi.nlm.nih.gov/gene/11118):

> This gene encodes a member of the immunoglobulin superfamily, which resides in the juxta-telomeric region of the major histocompatability class 1 locus and is clustered with the other family members on chromosome 6. The encoded protein may be involved in the adaptive immune response. Alternatively spliced transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Jun 2013]

**Accessions** — [HGNC:1139](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1139) · Entrez [11118](https://www.ncbi.nlm.nih.gov/gene/11118) · UniProt [P78410](https://www.uniprot.org/uniprotkb/P78410) · Ensembl [ENSG00000186470](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186470)

## Data

Gene col 11818: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11818); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11818, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11818]; `tensor/DDL_lfc|DDL_z.npy` [11818]; `embed/gene_vectors.npy` [11818]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11818 or target_col == 11818). Every well: [[BTN3A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BTN3A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
