---
symbol: "SH3PXD2A"
type: "gene"
col: 2904
ensembl_id: "ENSG00000107957"
name: "SH3 and PX domains 2A"
location: "10q24.33"
module: 84
arm: "+"
pooled_cpm: 84.73
n_lines_expressing: 45
n_dd_up: 3
n_dd_down: 47
n_dd_up_clean: 2
n_dd_down_clean: 35
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/084"]
generated_by: "tahoemap"
---

# SH3PXD2A

*SH3 and PX domains 2A* — 10q24.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 0.05 µM: 1.25× (z +4.1, q 0.027, up in 19 of 44 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.24× (z +3.5, q 0.096, up in 17 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 47 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.331× (z -27.9, q 0e+00, down in 39 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NECTIN1]] (+0.66, fdr 1e-05), [[RASA3]] (+0.58, fdr 1e-05), [[SPRY4]] (+0.57, fdr 1e-05); moves opposite to [[TGFB2]] (-0.48, fdr 6e-05), [[C1RL]] (-0.44, fdr 9e-05).
> It is in [[Module 084]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[PLXNA2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2904.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.25×** | +4.1 | 0.027 | 19/44 (LoVo, C-33 A, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.24×** | +3.5 | 0.096 | 17/42 (SW48, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.45×** | +3.5 | 0.096 | 18/43 (SW480, Hs 766T, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 60 in all, 18 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 47 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2904.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.331×** | -27.9 | 0e+00 | 39/43 (COLO 205, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.293×** | -21.9 | 0e+00 | 40/43 (LS 180, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.307×** | -21.0 | 0e+00 | 39/43 (LS 180, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.332×** | -19.6 | 0e+00 | 40/43 (H4, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.529×** | -16.0 | 0e+00 | 33/44 (Hs 766T, COLO 205, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.407×** | -16.0 | 0e+00 | 38/43 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.518×** | -11.3 | 2e-27 | 36/42 (RKO, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.534×** | -11.2 | 5e-27 | 39/43 (LS 180, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.528×** | -10.9 | 6e-26 | 30/43 (PANC-1, SW48, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **0.551×** | -10.6 | 2e-24 | 37/43 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.544×** | -10.4 | 1e-23 | 29/43 (LoVo, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.580×** | -9.7 | 2e-20 | 35/43 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.581×** | -9.3 | 8e-19 | 32/45 (A-172, PANC-1, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.596×** | -9.2 | 1e-18 | 31/43 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.571×** | -9.2 | 2e-18 | 30/44 (PANC-1, Hs 766T, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.652×** | -7.6 | 1e-12 | 30/43 (SK-MEL-2, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.457×** | -7.3 | 1e-11 | 30/44 (COLO 205, LS 180, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.780×** | -6.2 | 1e-08 | 27/43 (SW1417, Hs 766T, …) | top dose only |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.547×** | -5.6 | 6e-07 | 27/43 (CFPAC-1, AsPC-1, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2904. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 99.2 | 0 | 20 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -27.4) |
| [[PANC-1 (line)]] | alt | 130 | 0 | 18 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -19.2) |
| [[Hs 766T (line)]] | wt | 272 | 0 | 17 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -27.0) |
| [[LS 180 (line)]] | wt | 137 | 0 | 16 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -27.5) |
| [[AsPC-1 (line)]] | alt | 140 | 0 | 13 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.155× (z -23.2) |
| [[COLO 205 (line)]] | alt | 366 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0843× (z -32.7) |
| [[LoVo (line)]] | wt | 67.7 | 0 | 13 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.150× (z -21.0) |
| [[HT-29 (line)]] | alt | 85.1 | 0 | 12 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -17.8) |
| [[RKO (line)]] | wt | 56.8 | 0 | 12 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -28.2) |
| [[H4 (line)]] | wt | 108 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0377× (z -24.0) |
| [[MIA PaCa-2 (line)]] | alt | 84.8 | 0 | 10 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.113× (z -18.8) |
| [[A-172 (line)]] | wt | 131 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -23.6) |
| [[SW1417 (line)]] | alt | 86.1 | 0 | 9 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -18.1) |
| [[C32 (line)]] | wt | 97.0 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -20.5) |
| [[HepG2_C3A (line)]] | wt | 245 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.209× (z -16.2) |
| [[LOX-IMVI (line)]] | wt | 84.3 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -22.2) |
| [[NCI-H460 (line)]] | wt | 42.1 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -22.7) |
| [[BT-474 (line)]] | alt | 101 | 0 | 7 | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -15.9) |
| [[RPMI-7951 (line)]] | alt | 247 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -15.8) |
| [[NCI-H1792 (line)]] | alt | 104 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -27.0) |
| [[SK-MEL-2 (line)]] | alt | 111 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.271× (z -16.5) |
| [[SW48 (line)]] | wt | 64.3 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -12.8) |
| [[SW480 (line)]] | alt | 65.8 | 0 | 6 | — | [[Panobinostat (drug)]] 0.5 µM 0.307× (z -11.5) |
| [[AN3 CA (line)]] | alt | 189 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0552× (z -19.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.335× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 65.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -16.7) |
| [[HS-578T (line)]] | alt | 63.0 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.268× (z -12.6) |
| [[HCT15 (line)]] | alt | 31.5 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.130× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.184× (z -9.3) |
| [[Panc 03.27 (line)]] | alt | 80.9 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.216× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.289× (z -11.5) |
| [[hTERT-HPNE (line)]] | wt | 268 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.308× (z -10.6) |
| [[A-427 (line)]] | wt | 24.5 | 0 | 2 (1 ⚠) | — | [[PH-797804 (drug)]] 5 µM 0.0727× (z -9.2) |
| [[KATO III (line)]] | alt | 46.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -17.4) |
| [[NCI-H1573 (line)]] | alt | 80.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.392× (z -12.2) |
| [[SHP-77 (line)]] | alt | 84.9 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.413× (z -9.0) |
| [[SW 1088 (line)]] | alt | 179 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -10.8) |
| [[A498 (line)]] | wt | 23.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.363× (z -11.0) |
| [[A549 (line)]] | wt | 31.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -12.0) |
| [[SNU-423 (line)]] | alt | 56.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.381× (z -11.4) |
| [[SW 900 (line)]] | alt | 100 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.218× (z -12.9) |
| [[C-33 A (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 115 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.5 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 18.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 114 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 15.5 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 40.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 76.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.9 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2904), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NECTIN1]] | +0.66 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[RASA3]] | +0.58 | +0.63 / +0.53 | both halves | 1e-05 |  |
| [[SPRY4]] | +0.57 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[ZEB1]] | +0.57 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[SH3TC2]] | +0.56 | +0.58 / +0.49 | both halves | 1e-05 | same gene group |
| [[PRSS3]] | +0.56 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[NGEF]] | +0.55 | +0.56 / +0.54 | both halves | 1e-05 | same gene group; pathway: CDC42 GTPase cycle |
| [[KCNN4]] | +0.55 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[GLDC]] | +0.55 | +0.42 / +0.36 | both halves | 9e-05 |  |
| [[FLT1]] | +0.54 | +0.48 / +0.48 | both halves | 2e-05 |  |
| [[SH2B3]] | +0.54 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[IGSF9B]] | +0.53 | +0.46 / +0.48 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TGFB2]] | -0.48 | -0.50 / -0.39 | both halves | 6e-05 | pathway: Extracellular matrix organization |
| [[C1RL]] | -0.44 | -0.46 / -0.36 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLXNA2]] | B | PLXNA2 activity raises SH3PXD2A's level | lines that do not express PLXNA2 (15) vs lines expressing it (35) | 1.82× lower at baseline in the lines without PLXNA2 | 0.030 | ⚠ within organs, on part of the lines; also absent: GATA6, HS3ST3B1, IFI16 |
| [[PLAT]] | B | PLAT activity raises SH3PXD2A's level | lines that do not express PLAT (28) vs lines expressing it (22) | 1.93× lower at baseline in the lines without PLAT | 0.049 | ⚠ within organs, on part of the lines; also absent: TIMP3, FN1, SNAI2 |
| [[C1RL]] | C | C1RL activity raises SH3PXD2A's level | lines that do not express C1RL (3) vs lines expressing it (47) | 3.72× lower at baseline in the lines without C1RL | 0.033 | ⚠ few lines (3 vs 47); across organs; co-occurs with WNK2; also absent: PHLDA1, CASP8, SP100 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 084]]; 52 genes; every member is in the + arm (projection on the module's main direction 0.575). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.9, 5.7); signed map (1.6, 49.5). **Vector** length 93.5, 26.3% of its response variance represented; |z| ≥ 3 in 1,716 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~53% of this change | +6.3 | -6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +6.2 | -9.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.2 | -16.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.0 | -5.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | -1.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.9 | -2.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.4 | +3.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.8 | -0.6 |
| fall | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.2 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.9 | -2.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -5.0 | -2.9 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.9 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.8 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -4.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | SH3 and PX domains 2A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.33 — chr10:103,594,027-103,855,584 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FISH, KIAA0418; previously SH3MD1 |
| Gene groups (HGNC) | SH3 domain containing |
| Reactome | 6 pathways, smallest: Invadopodia formation; CDC42 GTPase cycle; Extracellular matrix organization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5TCZ1](https://www.uniprot.org/uniprotkb/Q5TCZ1) (SH3 and PX domain-containing protein 2A):

> Adapter protein involved in invadopodia and podosome formation, extracellular matrix degradation and invasiveness of some cancer cells. Binds matrix metalloproteinases (ADAMs), NADPH oxidases (NOXs) and phosphoinositides. Acts as an organizer protein that allows NOX1- or NOX3-dependent reactive oxygen species (ROS) generation and ROS localization. In association with ADAM12, mediates the neurotoxic effect of amyloid-beta peptide.

**Summary**, from NCBI Gene [9644](https://www.ncbi.nlm.nih.gov/gene/9644):

> Predicted to enable superoxide-generating NADPH oxidase activator activity. Involved in osteoclast fusion and superoxide metabolic process. Located in podosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23664](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23664) · Entrez [9644](https://www.ncbi.nlm.nih.gov/gene/9644) · UniProt [Q5TCZ1](https://www.uniprot.org/uniprotkb/Q5TCZ1) · Ensembl [ENSG00000107957](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107957)

## Data

Gene col 2904: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2904); `tables/drug_effects.parquet` (63 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2904, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2904]; `tensor/DDL_lfc|DDL_z.npy` [2904]; `embed/gene_vectors.npy` [2904]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2904 or target_col == 2904). Every well: [[SH3PXD2A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SH3PXD2A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
