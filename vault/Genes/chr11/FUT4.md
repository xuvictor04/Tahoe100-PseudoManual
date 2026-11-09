---
symbol: "FUT4"
type: "gene"
col: 12191
ensembl_id: "ENSG00000196371"
name: "fucosyltransferase 4"
location: "11q21"
module: 73
arm: "+"
pooled_cpm: 7.28
n_lines_expressing: 40
n_dd_up: 2
n_dd_down: 11
n_dd_up_clean: 1
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 1
direction_downstream: 8
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# FUT4

*fucosyltransferase 4* — 11q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.65× (z +5.2, q 9e-05, up in 2 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM: 1.43× (z +3.9, q 0.030, up in 9 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.503× (z -10.4, q 1e-22, down in 23 of 33 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTSE]] (+0.65, fdr 1e-05), [[TPTEP1-1]] (+0.62, fdr 2e-05), [[DSG4]] (+0.61, fdr 1e-05); moves opposite to [[RNF10]] (-0.53, fdr 3e-05), [[EZH1]] (-0.53, fdr 4e-05), [[HOXA9]] (-0.51, fdr 9e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PIWIL4]] → it (grade C ⚠); 8 go from it, the strongest it → [[CTDSP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12191.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +5.2 | 9e-05 | 2/10 (LoVo, HT-29) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.43×** | +3.9 | 0.030 | 9/32 (SW48, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | 1.52× | +3.2 | 0.22 | 4/32 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.49× | +3.1 | 0.26 | 6/23 (HT-29, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12191.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.503×** | -10.4 | 1e-22 | 23/33 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.576×** | -5.9 | 9e-07 | 16/37 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.589×** | -5.7 | 3e-06 | 20/37 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.610×** | -5.3 | 2e-05 | 15/36 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.632×** | -4.9 | 1e-04 | 18/35 (HT-29, SW48, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.743×** | -4.5 | 7e-04 | 15/32 (HT-29, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.683×** | -3.9 | 0.007 | 17/36 (LoVo, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.519×** | -3.7 | 0.017 | 13/34 (KATO III, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.722×** | -3.5 | 0.032 | 11/35 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.725×** | -3.4 | 0.035 | 13/36 (LoVo, C32, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.720×** | -3.4 | 0.040 | 15/33 (KATO III, LS 180, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.750× | -3.1 | 0.10 | 13/36 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~7% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12191. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 40.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.250× (z -11.7) |
| [[LoVo (line)]] | wt | 24.9 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0856× (z -20.8) |
| [[LOX-IMVI (line)]] | wt | 7.27 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0960× (z -14.2) |
| [[HT-29 (line)]] | alt | 26.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -8.8) |
| [[J82 (line)]] | alt | 6.22 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -10.0) |
| [[Panc 03.27 (line)]] | alt | 7.41 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 0.05 µM 0.0884× (z -8.7) |
| [[SW48 (line)]] | wt | 13.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0579× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.02 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.943 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.670 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.44 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.73 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.509 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.856 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.30 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 7.01 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.739 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.01 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.68 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.545 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12191), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTSE]] | +0.65 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[TPTEP1-1]] | +0.62 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[DSG4]] | +0.61 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[SLC52A3]] | +0.60 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[SLC6A20]] | +0.59 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[JPH1]] | +0.59 | +0.45 / +0.55 | both halves | 3e-05 |  |
| [[PITPNB]] | +0.58 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[PIWIL4]] | +0.58 | +0.64 / +0.56 | both halves | 1e-05 | STRING 475; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[PWP2]] | +0.58 | +0.49 / +0.53 | both halves | 1e-05 |  |
| [[SPON1]] | +0.58 | +0.59 / +0.46 | both halves | 3e-05 |  |
| [[HEPH]] | +0.57 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[TNS4]] | +0.57 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[ALDH1B1]] | +0.56 | +0.52 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF10]] | -0.53 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[EZH1]] | -0.53 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[HOXA9]] | -0.51 | -0.51 / -0.37 | both halves | 9e-05 |  |
| [[OGA]] | -0.49 | -0.36 / -0.55 | both halves | 1e-04 |  |
| [[PPP1R3E]] | -0.48 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[MBIP]] | -0.47 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[MYL6B]] | -0.47 | -0.46 / -0.38 | both halves | 6e-05 |  |
| [[CLIP3]] | -0.47 | -0.38 / -0.49 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PIWIL4]] | C | PIWIL4 activity raises FUT4's level | lines that do not express PIWIL4 (11) vs lines expressing it (39) | 3.26× lower at baseline in the lines without PIWIL4 | 0.007 | ⚠ within organs, on part of the lines; also absent: FUT4, CTSZ, ARHGAP23; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTDSP1]] | B | FUT4 activity raises CTDSP1's level | lines that do not express FUT4 (10) vs lines expressing it (40) | 1.36× lower at baseline in the lines without FUT4 | 0.012 | ⚠ within organs, on part of the lines; also absent: PIWIL4, LRRK1, LONRF3 |
| [[NOP16]] | B | FUT4 activity lowers NOP16's level | lines that do not express FUT4 (10) vs lines expressing it (40) | 1.35× higher at baseline in the lines without FUT4 | 0.035 | ⚠ within organs, on part of the lines; also absent: PIWIL4, LRRK1, LONRF3 |
| [[EVA1C]] | B | FUT4 activity raises EVA1C's level | lines that do not express FUT4 (10) vs lines expressing it (40) | 3.20× lower at baseline in the lines without FUT4 | 0.054 | ⚠ within organs, on part of the lines; also absent: PIWIL4, LRRK1, LONRF3 |
| [[DIAPH2]] | B | FUT4 activity raises DIAPH2's level | lines that do not express FUT4 (10) vs lines expressing it (40) | 2.44× lower at baseline in the lines without FUT4 | 0.065 | ⚠ within organs, on part of the lines; also absent: PIWIL4, LRRK1, LONRF3 |
| [[TMEM201]] | B | FUT4 activity lowers TMEM201's level | lines that do not express FUT4 (10) vs lines expressing it (40) | 1.52× higher at baseline in the lines without FUT4 | 0.067 | ⚠ within organs, on part of the lines; also absent: PIWIL4, LRRK1, LONRF3 |
| [[RNF10]] | B | FUT4 activity lowers RNF10's level | lines that do not express FUT4 (10) vs lines expressing it (40) | 1.08× higher at baseline in the lines without FUT4 | 0.089 | ⚠ within organs, on part of the lines; also absent: PIWIL4, LRRK1, LONRF3 |
| [[LRCH1]] | B | FUT4 activity raises LRCH1's level | lines that do not express FUT4 (10) vs lines expressing it (40) | 1.59× lower at baseline in the lines without FUT4 | 0.098 | ⚠ within organs, on part of the lines; also absent: PIWIL4, LRRK1, LONRF3 |
| [[PIWIL4]] | C | FUT4 activity raises PIWIL4's level | lines that do not express FUT4 (10) vs lines expressing it (40) | 4.32× lower at baseline in the lines without FUT4 | 0.012 | ⚠ within organs, on part of the lines; also absent: PIWIL4, LRRK1, LONRF3; co-absent with the target |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.610). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.4, 49.6); signed map (66.3, 7.5). **Vector** length 59.5, 10.5% of its response variance represented; |z| ≥ 3 in 730 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.2 | +0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +1.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.2 | +0.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.1 | -0.8 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +1.0 | +2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +0.9 | +0.7 |
|  | [[vincristine (drug)]] 0.5 µM |  | +0.9 | +3.2 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +0.9 | +2.0 |
|  | [[Larotrectinib (drug)]] 0.05 µM |  | +0.9 | +1.9 |
| fall | [[Ponatinib (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -1.7 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -1.9 | -3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.6 | -2.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -1.5 | +0.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.5 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -4.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | fucosyltransferase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q21 — chr11:94,543,921-94,549,895 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FUC-TIV; previously CD15, FCT3A, ELFT |
| Gene groups (HGNC) | Fucosyltransferases; CD molecules |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 3 pathways, smallest: Lewis blood group biosynthesis; Blood group systems biosynthesis; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P22083](https://www.uniprot.org/uniprotkb/P22083) (Alpha-(1,3)-fucosyltransferase 4):

> [Isoform Short]: Catalyzes alpha(1->3) linkage of fucosyl moiety transferred from GDP-beta-L-fucose to N-acetyl glucosamine (GlcNAc) within type 2 lactosamine (LacNAc, Gal-beta(1->4)GlcNAc) glycan attached to N- or O-linked glycoproteins. Robustly fucosylates nonsialylated distal LacNAc unit of the polylactosamine chain to form Lewis X antigen (CD15), a glycan determinant known to mediate important cellular functions in development and immunity. Fucosylates with lower efficiency sialylated …

**Summary**, from NCBI Gene [2526](https://www.ncbi.nlm.nih.gov/gene/2526):

> The product of this gene transfers fucose to N-acetyllactosamine polysaccharides to generate fucosylated carbohydrate structures. It catalyzes the synthesis of the non-sialylated antigen, Lewis x (CD15). [provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:4015](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4015) · Entrez [2526](https://www.ncbi.nlm.nih.gov/gene/2526) · UniProt [P22083](https://www.uniprot.org/uniprotkb/P22083) · Ensembl [ENSG00000196371](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196371)

## Data

Gene col 12191: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12191); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12191, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12191]; `tensor/DDL_lfc|DDL_z.npy` [12191]; `embed/gene_vectors.npy` [12191]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12191 or target_col == 12191). Every well: [[FUT4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FUT4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
