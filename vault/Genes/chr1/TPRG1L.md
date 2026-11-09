---
symbol: "TPRG1L"
type: "gene"
col: 8133
ensembl_id: "ENSG00000158109"
name: "tumor protein p63 regulated 1 like"
location: "1p36.32"
module: 76
arm: "+"
pooled_cpm: 13.99
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 17
n_dd_up_clean: 6
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/076"]
generated_by: "tahoemap"
---

# TPRG1L

*tumor protein p63 regulated 1 like* — 1p36.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.71× (z +12.0, q 2e-30, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.366× (z -17.3, q 0e+00, down in 41 of 46 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPSB3]] (+0.68, fdr 9e-06), [[GET1]] (+0.67, fdr 1e-05), [[RAB40B]] (+0.63, fdr 1e-05); moves opposite to [[ANKRD18A]] (-0.63, fdr 1e-05), [[THOC7]] (-0.62, fdr 4e-05), [[PATL2]] (-0.61, fdr 4e-05).
> It is in [[Module 076]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8133.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.71×** | +12.0 | 2e-30 | 44/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.53×** | +11.2 | 1e-26 | 46/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.94×** | +8.0 | 2e-13 | 42/47 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.19× | +7.3 | 3e-11 | 19/48 (Hs 766T, A498, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +4.4 | 0.001 | 17/44 (SW1417, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.38×** | +3.7 | 0.019 | 16/44 (HOP62, A549, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.021 | 14/45 (A-172, NCI-H460, …) | rises with dose | low cells (technical?); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +3.4 | 0.044 | 16/42 (SW480, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.20× | +3.0 | 0.15 | 13/47 (J82, CFPAC-1, …) | top dose only | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8133.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.366×** | -17.3 | 0e+00 | 41/46 (A498, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.350×** | -12.3 | 4e-32 | 43/46 (AsPC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.522×** | -7.9 | 5e-13 | 31/47 (A-427, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.598×** | -6.3 | 5e-08 | 25/42 (SW48, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.426×** | -5.4 | 7e-06 | 29/46 (Hs 766T, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.648×** | -5.3 | 1e-05 | 29/47 (AsPC-1, MIA PaCa-2, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.710×** | -4.2 | 0.002 | 22/44 (LoVo, SW480, …) | top dose only | position effect removed |
| [[venetoclax (drug)]] 5 µM |  | **0.536×** | -4.0 | 0.005 | 20/43 (SK-MEL-2, LoVo, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.657×** | -3.7 | 0.016 | 13/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.747×** | -3.6 | 0.020 | 15/46 (SW480, SW48, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.818×** | -3.5 | 0.023 | 17/47 (NCI-H2347, NCI-H661, …) | all doses, flat | position effect removed |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.670×** | -3.5 | 0.023 | 16/46 (A498, H4, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.754×** | -3.5 | 0.023 | 15/45 (NCI-H2347, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.05 µM |  | **0.766×** | -3.3 | 0.042 | 14/47 (Panc 03.27, RKO, …) | all doses, flat | position effect removed |
| [[Salicylic acid (drug)]] 0.5 µM |  | **0.766×** | -3.3 | 0.042 | 13/47 (SW 1088, SW480, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8133. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 9.61 | 2 | 2 | [[Panobinostat (drug)]] 5 µM 4.33× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -10.6) |
| [[A498 (line)]] | wt | 13.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.160× (z -17.2) |
| [[A-172 (line)]] | wt | 13.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.179× (z -13.9) |
| [[AsPC-1 (line)]] | alt | 24.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -15.9) |
| [[Hs 766T (line)]] | wt | 43.3 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -11.9) ⚠ cell-cycle shift, explains ~38% of this change |
| [[HT-29 (line)]] | alt | 30.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -9.9) |
| [[hTERT-HPNE (line)]] | wt | 21.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -10.4) |
| [[NCI-H460 (line)]] | wt | 6.72 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.272× (z -9.7) |
| [[SNU-1 (line)]] | wt | 10.5 | 0 | 2 (1 ⚠) | — | [[Thymol (drug)]] 0.05 µM 0.0590× (z -10.0) |
| [[SNU-423 (line)]] | alt | 12.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.252× (z -10.0) |
| [[SW48 (line)]] | wt | 14.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0994× (z -12.2) |
| [[A-427 (line)]] | wt | 12.1 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.108× (z -12.0) |
| [[A549 (line)]] | wt | 8.42 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -10.5) |
| [[H4 (line)]] | wt | 19.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0985× (z -10.3) |
| [[HOP62 (line)]] | alt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.339× (z -9.3) |
| [[J82 (line)]] | alt | 15.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -9.8) |
| [[LoVo (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[MIA PaCa-2 (line)]] | alt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -13.6) |
| [[NCI-H1573 (line)]] | alt | 12.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.204× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 9.17 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -13.1) |
| [[NCI-H23 (line)]] | alt | 13.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 13.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -12.0) |
| [[Panc 03.27 (line)]] | alt | 13.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -10.2) |
| [[PANC-1 (line)]] | alt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -12.6) |
| [[SHP-77 (line)]] | alt | 10.6 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0824× (z -11.3) |
| [[SK-MEL-2 (line)]] | alt | 23.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -9.5) |
| [[SW 900 (line)]] | alt | 10.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.146× (z -8.5) |
| [[SW1417 (line)]] | alt | 13.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -10.2) |
| [[AN3 CA (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.86 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.17 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8133), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*67 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPSB3]] | +0.68 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[GET1]] | +0.67 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[RAB40B]] | +0.63 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[HECTD3]] | +0.62 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[SNAPC2]] | +0.62 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[ADIPOR1]] | +0.62 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[WASF2]] | +0.62 | +0.58 / +0.53 | both halves | 1e-05 |  |
| [[KLHDC3]] | +0.61 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[MARF1]] | +0.61 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[RETREG2]] | +0.61 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[STRN]] | +0.60 | +0.63 / +0.32 | both halves | 2e-04 |  |
| [[LINC01881]] | +0.59 | +0.47 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*33 of its nearest partners move opposite, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD18A]] | -0.63 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[THOC7]] | -0.62 | -0.51 / -0.41 | both halves | 4e-05 |  |
| [[PATL2]] | -0.61 | -0.60 / -0.42 | both halves | 4e-05 |  |
| [[GTF3C6]] | -0.59 | -0.56 / -0.18 | ⚠ one half (not replicated) | 1e-03 |  |
| [[POGLUT1]] | -0.58 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[GABPB2]] | -0.58 | -0.58 / -0.27 | both halves | 3e-04 |  |
| [[SLC16A9]] | -0.58 | -0.57 / -0.32 | both halves | 2e-04 |  |
| [[TIA1]] | -0.58 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[ZNF518A]] | -0.57 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[LINC00869-1]] | -0.57 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[LINC00705]] | -0.57 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[ENOSF1]] | -0.56 | -0.44 / -0.38 | both halves | 6e-05 |  |
| [[ANKRD26]] | -0.56 | -0.65 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers TPRG1L's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZNF462]] | B | ZNF462 activity lowers TPRG1L's level | lines that do not express ZNF462 (5) vs lines expressing it (45) | 1.69× higher at baseline in the lines without ZNF462 | 0.096 | ⚠ within organs, on part of the lines; also absent: PDE11A, ENSG00000214803 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 076]]; 59 genes; every member is in the + arm (projection on the module's main direction 0.638). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (4.0, -13.7); signed map (-39.0, -1.5). **Vector** length 104, 24.0% of its response variance represented; |z| ≥ 3 in 921 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +7.3 | +11.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.4 | +12.0 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.9 | +8.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.5 | +3.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.3 | +7.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.7 | +2.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.4 | +3.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +2.0 | +1.7 |
|  | [[OTS514 (drug)]] 5 µM |  | +1.7 | +1.2 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.7 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.7 | -17.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | -7.5 | -12.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.5 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.5 | -6.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -4.2 | -3.0 |
|  | [[venetoclax (drug)]] 5 µM |  | -3.5 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.1 | -1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.8 | -2.9 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | tumor protein p63 regulated 1 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.32 — chr1:3,625,015-3,630,127 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RP11-46F15.3, FLJ21811, TPRGL, SVAP30, h-Mover; previously FAM79A |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T0D9](https://www.uniprot.org/uniprotkb/Q5T0D9) (Tumor protein p63-regulated gene 1-like protein):

> Presynaptic protein involved in the synaptic transmission tuning. Regulates synaptic release probability by decreasing the calcium sensitivity of release.

**Summary**, from NCBI Gene [127262](https://www.ncbi.nlm.nih.gov/gene/127262):

> Predicted to enable calmodulin binding activity and identical protein binding activity. Predicted to be involved in regulation of glutamatergic synaptic transmission and regulation of synaptic vesicle exocytosis. Predicted to act upstream of or within calcineurin-NFAT signaling cascade; negative regulation of synaptic transmission; and synaptic vesicle docking. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:27007](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27007) · Entrez [127262](https://www.ncbi.nlm.nih.gov/gene/127262) · UniProt [Q5T0D9](https://www.uniprot.org/uniprotkb/Q5T0D9) · Ensembl [ENSG00000158109](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158109)

## Data

Gene col 8133: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8133); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8133, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8133]; `tensor/DDL_lfc|DDL_z.npy` [8133]; `embed/gene_vectors.npy` [8133]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8133 or target_col == 8133). Every well: [[TPRG1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TPRG1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
