---
symbol: "CUZD1"
type: "gene"
col: 6135
ensembl_id: "ENSG00000138161"
name: "CUB and zona pellucida like domains 1"
location: "10q26.13"
module: 49
arm: "+"
pooled_cpm: 2.65
n_lines_expressing: 41
n_dd_up: 10
n_dd_down: 7
n_dd_up_clean: 7
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# CUZD1

*CUB and zona pellucida like domains 1* — 10q26.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 1.72× (z +4.8, q 7e-04, up in 12 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.425× (z -7.7, q 6e-12, down in 20 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FAM24B]] (+0.60, fdr 1e-05, ⚠ same locus), [[CCDC138]] (+0.58, fdr 3e-05), [[ST6GALNAC6-1]] (+0.58, fdr 6e-05), [[TMEM243]] (+0.56, fdr 5e-05); moves opposite to [[ARFGAP2]] (-0.55, fdr 5e-05), [[LRRC57]] (-0.55, fdr 3e-05), [[BAZ2B]] (-0.54, fdr 6e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); 5 go from it, the strongest it → [[TOMM5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6135.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **1.72×** | +4.8 | 7e-04 | 12/34 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.66×** | +4.2 | 0.007 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~6% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.59×** | +4.1 | 0.007 | 7/37 (NCI-H1792, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.26×** | +3.8 | 0.018 | 5/32 (PANC-1, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.7 | 0.029 | 5/10 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Gallic acid (drug)]] 0.05 µM |  | **1.47×** | +3.4 | 0.054 | 3/34 (A498, J82, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.46×** | +3.4 | 0.054 | 4/33 (NCI-H1792, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +3.4 | 0.054 | 3/35 (NCI-H460, PANC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.47×** | +3.3 | 0.060 | 0/2 | inconsistent across doses | cell-cycle shift (explains ~7% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +3.2 | 0.069 | 7/34 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6135.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.425×** | -7.7 | 6e-12 | 20/36 (SW1417, KATO III, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.466×** | -6.6 | 8e-09 | 15/31 (SHP-77, J82, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.523×** | -5.9 | 9e-07 | 16/35 (SW 900, H4, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.544×** | -5.5 | 5e-06 | 14/21 (PANC-1, SHP-77, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.638×** | -4.1 | 0.005 | 13/32 (SHP-77, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **0.765×** | -3.4 | 0.055 | 16/26 (SHP-77, A498, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.691×** | -3.4 | 0.063 | 12/34 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Artesunate (drug)]] 0.5 µM |  | 0.705× | -3.2 | 0.11 | 5/34 (A498, MIA PaCa-2, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6135. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 25.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -11.5) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Triamcinolone (drug)]] 0.5 µM 0.0961× (z -9.4) |
| [[PANC-1 (line)]] | alt | 4.13 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0722× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[A498 (line)]] | wt | 2.02 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -9.3) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SW 900 (line)]] | alt | 3.28 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0432× (z -8.5) |
| [[SW480 (line)]] | alt | 2.26 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.0794× (z -9.5) |
| [[A-172 (line)]] | wt | 0.231 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.93 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.51 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.244 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.974 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.12 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.294 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.815 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.78 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.12 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.51 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.911 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.38 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.44 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.364 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.303 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.271 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6135), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FAM24B]] | +0.60 | +0.51 / +0.62 | both halves | 1e-05 | ⚠ same locus (2.9 kb, same strand: neighbours can correlate without regulation) |
| [[CCDC138]] | +0.58 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[ST6GALNAC6-1]] | +0.58 | +0.39 / +0.64 | both halves | 6e-05 |  |
| [[TMEM243]] | +0.56 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[RBAK-RBAKDN]] | +0.55 | +0.39 / +0.53 | both halves | 6e-05 |  |
| [[GNB1L]] | +0.54 | +0.42 / +0.53 | both halves | 4e-05 |  |
| [[ATP2A1]] | +0.53 | +0.40 / +0.62 | both halves | 5e-05 |  |
| [[IQCB1]] | +0.52 | +0.44 / +0.51 | both halves | 3e-05 |  |
| [[TBX20]] | +0.51 | +0.36 / +0.46 | both halves | 1e-04 |  |
| [[SMIM41]] | +0.51 | +0.37 / +0.54 | both halves | 8e-05 |  |
| [[ERCC3]] | +0.50 | +0.37 / +0.56 | both halves | 8e-05 |  |
| [[ZNF215]] | +0.50 | +0.40 / +0.45 | both halves | 4e-05 |  |
| [[SNU13]] | +0.50 | +0.47 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARFGAP2]] | -0.55 | -0.39 / -0.62 | both halves | 5e-05 |  |
| [[LRRC57]] | -0.55 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[BAZ2B]] | -0.54 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[CUX1]] | -0.53 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[TAPBP]] | -0.52 | -0.39 / -0.52 | both halves | 5e-05 |  |
| [[SLC38A4-AS1]] | -0.51 | -0.50 / -0.41 | both halves | 4e-05 |  |
| [[GRINA]] | -0.51 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[TAF9B]] | -0.50 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[UBE2A]] | -0.50 | -0.42 / -0.41 | both halves | 4e-05 |  |
| [[H2AJ]] | -0.50 | -0.39 / -0.37 | both halves | 8e-05 |  |
| [[CGGBP1]] | -0.49 | -0.32 / -0.49 | both halves | 2e-04 |  |
| [[ZHX1]] | -0.49 | -0.36 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers CUZD1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers CUZD1's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FAM24B]] | C | FAM24B activity raises CUZD1's level | lines that do not express FAM24B (8) vs lines expressing it (42) | 2.58× lower at baseline in the lines without FAM24B | 0.019 | ⚠ within organs, on part of the lines; also absent: CUZD1, C10orf88B; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOMM5]] | B | CUZD1 activity raises TOMM5's level | lines that do not express CUZD1 (9) vs lines expressing it (41) | 1.48× lower at baseline in the lines without CUZD1 | 0.045 | ⚠ within organs, on part of the lines; also absent: FAM24B, C10orf88B |
| [[NOP58]] | B | CUZD1 activity raises NOP58's level | lines that do not express CUZD1 (9) vs lines expressing it (41) | 1.29× lower at baseline in the lines without CUZD1 | 0.079 | ⚠ within organs, on part of the lines; also absent: FAM24B, C10orf88B |
| [[THOC3]] | B | CUZD1 activity raises THOC3's level | lines that do not express CUZD1 (9) vs lines expressing it (41) | 1.11× lower at baseline in the lines without CUZD1 | 0.085 | ⚠ within organs, on part of the lines; also absent: FAM24B, C10orf88B |
| [[IL9RP3]] | B | CUZD1 activity lowers IL9RP3's level | lines that do not express CUZD1 (9) vs lines expressing it (41) | 1.53× higher at baseline in the lines without CUZD1 | 0.098 | ⚠ within organs, on part of the lines; also absent: FAM24B, C10orf88B |
| [[FAM24B]] | C | CUZD1 activity raises FAM24B's level | lines that do not express CUZD1 (9) vs lines expressing it (41) | 5.12× lower at baseline in the lines without CUZD1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: FAM24B, C10orf88B; co-absent with the target |

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.361). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (38.2, -23.7); signed map (-51.0, -1.8). **Vector** length 47.2, 6.50% of its response variance represented; |z| ≥ 3 in 902 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +3.4 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +2.4 | +2.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.1 | +3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.9 | +3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.5 | -0.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.2 | +0.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.1 | +0.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.0 | -6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.9 | -7.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.5 | -5.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -3.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -3.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | -2.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.2 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | CUB and zona pellucida like domains 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.13 — chr10:122,832,158-122,846,175 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ERG-1, UO-44 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UP6](https://www.uniprot.org/uniprotkb/Q86UP6) (CUB and zona pellucida-like domain-containing protein 1):

> Localized to zymogen granules, where it functions in trypsinogen activation (By similarity). May indirectly regulate cell motility, cell-cell and cell/extracellular matrix interactions.

**Summary**, from NCBI Gene [50624](https://www.ncbi.nlm.nih.gov/gene/50624):

> Predicted to be involved in trypsinogen activation. Located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:17937](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17937) · Entrez [50624](https://www.ncbi.nlm.nih.gov/gene/50624) · UniProt [Q86UP6](https://www.uniprot.org/uniprotkb/Q86UP6) · Ensembl [ENSG00000138161](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138161)

## Data

Gene col 6135: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6135); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6135, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6135]; `tensor/DDL_lfc|DDL_z.npy` [6135]; `embed/gene_vectors.npy` [6135]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6135 or target_col == 6135). Every well: [[CUZD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CUZD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
