---
symbol: "GYG2"
type: "gene"
col: 642
ensembl_id: "ENSG00000056998"
name: "glycogenin 2"
location: "Xp22.33"
module: 19
arm: "+"
pooled_cpm: 2.68
n_lines_expressing: 30
n_dd_up: 16
n_dd_down: 8
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 1
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# GYG2

*glycogenin 2* — Xp22.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.00× (z +10.8, q 2e-24, up in 2 of 5 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.67× (z +5.9, q 7e-07, up in 11 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.432× (z -6.8, q 5e-09, down in 17 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLITRK4]] (+0.62, fdr 1e-05), [[MAP2K6]] (+0.60, fdr 1e-05), [[SLC19A3]] (+0.60, fdr 6e-05); moves opposite to [[C6orf62]] (-0.44, fdr 3e-04), [[ZNF341-AS1]] (-0.42, fdr 1e-04), [[RNH1]] (-0.41, fdr 4e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ATP2A3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[LINC02994]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 7 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 642.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.00×** | +10.8 | 2e-24 | 2/5 (SNU-423, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.60×** | +7.8 | 3e-12 | 2/10 (SNU-423, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.57×** | +7.1 | 3e-10 | 2/5 (SNU-423, J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.67×** | +5.9 | 7e-07 | 11/24 (SW480, BT-474, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.54×** | +4.9 | 9e-05 | 5/24 (A-172, C-33 A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~19% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.69×** | +4.2 | 0.002 | 10/22 (SK-MEL-2, NCI-H1573, …) | two highest doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.71×** | +4.2 | 0.002 | 0/6 | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.9 | 0.008 | 1/18 (BT-474) | top dose only | cell-cycle shift (explains ~4% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.20×** | +3.3 | 0.050 | 1/5 (NCI-H460) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +3.3 | 0.050 | 7/20 (BT-474, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.75×** | +3.2 | 0.066 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.47×** | +3.1 | 0.076 | 6/25 (RPMI-7951, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.50×** | +3.1 | 0.076 | 9/18 (SK-MEL-2, A498, …) | rises with dose |  |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.081 | 2/17 (COLO 205, C-33 A) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.05×** | +3.0 | 0.086 | 1/8 (A-172) | top dose only | cell-cycle shift (explains ~12% here); noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.45×** | +3.0 | 0.086 | 13/26 (SK-MEL-2, J82, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 642.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.432×** | -6.8 | 5e-09 | 17/22 (COLO 205, A549, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.575×** | -4.5 | 0.002 | 14/26 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.613×** | -4.0 | 0.012 | 12/18 (A-172, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.616×** | -3.9 | 0.012 | 10/26 (NCI-H460, NCI-H661, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.654×** | -3.5 | 0.056 | 9/24 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.656×** | -3.4 | 0.056 | 5/25 (NCI-H460, SW480, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.658×** | -3.3 | 0.084 | 16/22 (COLO 205, J82, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.575×** | -3.2 | 0.095 | 7/26 (BT-474, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.684× | -3.1 | 0.13 | 10/21 (LoVo, NCI-H661, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 642. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 7.46 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -9.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.129× (z -9.0) |
| [[COLO 205 (line)]] | alt | 7.58 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0438× (z -10.3) |
| [[LS 180 (line)]] | wt | 5.04 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H460 (line)]] | wt | 13.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.174× (z -9.6) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 3.70 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0952× (z -8.6) |
| [[J82 (line)]] | alt | 6.79 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.115× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 0.260 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 5.43 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.669 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.559 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.01 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.364 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.805 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.334 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.902 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.390 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.372 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.296 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.315 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.282 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.772 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.579 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.76 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.614 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.291 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.382 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.72 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.359 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.90 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 642), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLITRK4]] | +0.62 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[MAP2K6]] | +0.60 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[SLC19A3]] | +0.60 | +0.39 / +0.62 | both halves | 6e-05 |  |
| [[DDIT4L]] | +0.53 | +0.46 / +0.46 | both halves | 3e-05 |  |
| [[CNTN1]] | +0.52 | +0.36 / +0.52 | both halves | 1e-04 |  |
| [[SLC16A4]] | +0.52 | +0.38 / +0.55 | both halves | 6e-05 |  |
| [[PDE1C]] | +0.50 | +0.42 / +0.48 | both halves | 4e-05 |  |
| [[BCHE]] | +0.49 | +0.38 / +0.54 | both halves | 7e-05 |  |
| [[LRRC63]] | +0.49 | +0.33 / +0.57 | both halves | 1e-04 |  |
| [[SPDYE10]] | +0.49 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[CRYZL2P]] | +0.49 | +0.38 / +0.47 | both halves | 7e-05 |  |
| [[AMDHD1]] | +0.48 | +0.43 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C6orf62]] | -0.44 | -0.28 / -0.38 | both halves | 3e-04 |  |
| [[ZNF341-AS1]] | -0.42 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[RNH1]] | -0.41 | -0.24 / -0.44 | both halves | 4e-04 |  |
| [[LETM2]] | -0.41 | -0.33 / -0.31 | both halves | 2e-04 |  |
| [[PITRM1]] | -0.41 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[SLC10A3]] | -0.39 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[TMEM217]] | -0.38 | -0.23 / -0.31 | both halves | 5e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP2A3]] | B | ATP2A3 activity raises GYG2's level | lines that do not express ATP2A3 (16) vs lines expressing it (34) | 1.50× lower at baseline in the lines without ATP2A3 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: WBP2NL, BEX4, NSUN7; maybe low, not absent |
| [[PDE1C]] | B | PDE1C activity raises GYG2's level | lines that do not express PDE1C (26) vs lines expressing it (24) | 1.73× lower at baseline in the lines without PDE1C | 0.069 | ⚠ within organs, on part of the lines; also absent: NTRK3, LINC02211, LINC02945 |
| [[MAP2K6]] | B | MAP2K6 activity raises GYG2's level | lines that do not express MAP2K6 (21) vs lines expressing it (29) | 1.42× lower at baseline in the lines without MAP2K6 | 0.094 | ⚠ within organs, on part of the lines; also absent: AGMO, MTMR8, ENSG00000286133; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02994]] | B | GYG2 activity raises LINC02994's level | lines that do not express GYG2 (20) vs lines expressing it (30) | 2.67× lower at baseline in the lines without GYG2 | 0.060 | ⚠ within organs, on part of the lines; also absent: FRMPD3, PALM, GAS7 |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.469). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.9, 38.7); signed map (45.3, 45.6). **Vector** length 44.3, 8.45% of its response variance represented; |z| ≥ 3 in 610 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.1 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +7.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +5.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +2.1 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.3 | +4.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.1 | +2.4 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -3.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.2 | -3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.0 | -3.5 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -6.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.8 | -4.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.3 | -2.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.2 | -2.0 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | glycogenin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.33 — chrX:2,828,822-2,882,818 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GN-2 |
| Gene groups (HGNC) | Glycosyltransferase family 8 |
| Reactome | 7 pathways, smallest: Glycogen synthesis; Glycogen storage diseases; Glycogen breakdown (glycogenolysis) |
| Matched by | ensembl_id |

**Function**, from UniProt [O15488](https://www.uniprot.org/uniprotkb/O15488) (Glycogenin-2):

> Glycogenin participates in the glycogen biosynthetic process along with glycogen synthase and glycogen branching enzyme. It catalyzes the formation of a short alpha (1,4)-glucosyl chain covalently attached via a glucose 1-O-tyrosyl linkage to internal tyrosine residues and these chains act as primers for the elongation reaction catalyzed by glycogen synthase.

**Summary**, from NCBI Gene [8908](https://www.ncbi.nlm.nih.gov/gene/8908):

> This gene encodes a member of the the glycogenin family. Glycogenin is a self-glucosylating protein involved in the initiation reactions of glycogen biosynthesis. A gene on chromosome 3 encodes the muscle glycogenin and this X-linked gene encodes the glycogenin mainly present in liver; both are involved in blood glucose homeostasis. This gene has a short version on chromosome Y, which is 3' truncated and can not make a functional protein. Multiple alternatively spliced transcript variants …

**Accessions** — [HGNC:4700](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4700) · Entrez [8908](https://www.ncbi.nlm.nih.gov/gene/8908) · UniProt [O15488](https://www.uniprot.org/uniprotkb/O15488) · Ensembl [ENSG00000056998](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000056998)

## Data

Gene col 642: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 642); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 642, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 642]; `tensor/DDL_lfc|DDL_z.npy` [642]; `embed/gene_vectors.npy` [642]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 642 or target_col == 642). Every well: [[GYG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GYG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
