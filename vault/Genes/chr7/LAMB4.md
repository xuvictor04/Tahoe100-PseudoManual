---
symbol: "LAMB4"
type: "gene"
col: 1652
ensembl_id: "ENSG00000091128"
name: "laminin subunit beta 4"
location: "7q31.1"
module: 19
arm: "+"
pooled_cpm: 2.16
n_lines_expressing: 24
n_dd_up: 20
n_dd_down: 0
n_dd_up_clean: 11
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 10
direction_downstream: 7
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# LAMB4

*laminin subunit beta 4* — 7q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.67× (z +14.4, q 2e-44, up in 7 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NRCAM]] (+0.78, fdr 7e-06, ⚠ read-through risk), [[SPDYE10]] (+0.70, fdr 7e-06), [[GABBR2]] (+0.70, fdr 1e-05), [[HORMAD1]] (+0.69, fdr 1e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 7 go from it, the strongest it → [[NRCAM]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1652.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.67×** | +14.4 | 2e-44 | 7/11 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.84×** | +11.2 | 8e-27 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **5.39×** | +11.1 | 1e-26 | 9/13 (SW480, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.28×** | +11.0 | 5e-26 | 1/5 (NCI-H1792) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.67×** | +9.4 | 5e-19 | 2/3 (A498, C32) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.06×** | +6.8 | 1e-09 | 5/16 (A498, A549, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.57×** | +6.2 | 4e-08 | 2/14 (SW480, HEC-1-A) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +5.4 | 4e-06 | 1/12 (SW480) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.22×** | +5.1 | 3e-05 | 1/9 (NCI-H1792) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.59×** | +4.3 | 8e-04 | 7/15 (BT-474, SW480, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.91×** | +4.1 | 0.002 | 1/12 (HEC-1-A) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.86×** | +4.1 | 0.002 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~3% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +4.0 | 0.002 | 2/12 (SW480, LS 180) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cepharanthine (drug)]] 5 µM |  | **1.49×** | +3.7 | 0.009 | 0/15 | top dose only | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.68×** | +3.4 | 0.024 | 1/9 (NCI-H1792) | top dose only | cell-cycle shift (explains ~15% here) |
| [[palbociclib (drug)]] 0.05 µM |  | **1.68×** | +3.2 | 0.041 | 0/11 | inconsistent across doses |  |
| [[Lactate (calcium) (drug)]] 5 µM |  | **1.59×** | +3.1 | 0.064 | 0/16 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1652.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Goserelin (acetate) (drug)]] 5 µM |  | 0.701× | -3.4 | 0.45 | 3/19 (H4, SW 900, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1652. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 0.430 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.324 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.651 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.390 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.808 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.648 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.537 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.897 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.439 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.22 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.464 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.530 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.536 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.470 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.427 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.461 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.515 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.19 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.594 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.669 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.411 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.372 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.391 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.625 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.898 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.840 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.367 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.517 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.454 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.825 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1652), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRCAM]] | +0.78 | +0.77 / +0.72 | both halves | 7e-06 | ⚠ **readthrough risk**: this gene lies 17.3 kb 3′ of NRCAM on the same strand (can correlate by spillover, not regulation) |
| [[SPDYE10]] | +0.70 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[GABBR2]] | +0.70 | +0.56 / +0.68 | both halves | 1e-05 | **novel candidate** |
| [[HORMAD1]] | +0.69 | +0.65 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[RHOH]] | +0.68 | +0.54 / +0.60 | both halves | 1e-05 | **novel candidate** |
| [[GLP2R]] | +0.66 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[LINC01257]] | +0.65 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[KCNK2]] | +0.64 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[COL4A6]] | +0.61 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[NCKAP5-AS2]] | +0.61 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[CHL1]] | +0.61 | +0.58 / +0.52 | both halves | 1e-05 |  |
| [[DPP10]] | +0.61 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[SERPINB11]] | +0.60 | +0.57 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 1, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LAMB4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NRCAM]] | C | NRCAM activity raises LAMB4's level | lines that do not express NRCAM (36) vs lines expressing it (14) | 2.59× lower at baseline in the lines without NRCAM | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SPP1, FGG; co-absent with the target |
| [[TM4SF18]] | C | TM4SF18 activity raises LAMB4's level | lines that do not express TM4SF18 (33) vs lines expressing it (17) | 1.81× lower at baseline in the lines without TM4SF18 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000244468, LINC01610, SERPINB11; co-absent with the target |
| [[GLP2R]] | C | GLP2R activity raises LAMB4's level | lines that do not express GLP2R (43) vs lines expressing it (7) | 2.22× lower at baseline in the lines without GLP2R | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, GSG1L2, ENSG00000238054; co-absent with the target |
| [[SERPINB11]] | C | SERPINB11 activity raises LAMB4's level | lines that do not express SERPINB11 (43) vs lines expressing it (7) | 2.28× lower at baseline in the lines without SERPINB11 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SUCNR1, HOPX; co-absent with the target |
| [[SOX6]] | C | SOX6 activity raises LAMB4's level | lines that do not express SOX6 (22) vs lines expressing it (28) | 1.52× lower at baseline in the lines without SOX6 | 0.053 | ⚠ within organs, on part of the lines; also absent: CFI, MGP, SLC16A6; maybe low, not absent; co-absent with the target |
| [[LIN7A]] | C | LIN7A activity raises LAMB4's level | lines that do not express LIN7A (34) vs lines expressing it (16) | 1.73× lower at baseline in the lines without LIN7A | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000239268, DPP10, FGL1; co-absent with the target |
| [[GPRIN3]] | C | GPRIN3 activity raises LAMB4's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 1.79× lower at baseline in the lines without GPRIN3 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031; co-absent with the target |
| [[LINC00824]] | C | LINC00824 activity raises LAMB4's level | lines that do not express LINC00824 (46) vs lines expressing it (4) | 3.40× lower at baseline in the lines without LINC00824 | 0.074 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, SUCNR1, ENSG00000289530; co-absent with the target |
| [[ZNF736P9Y]] | C | ZNF736P9Y activity raises LAMB4's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 1.31× lower at baseline in the lines without ZNF736P9Y | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRCAM]] | C | LAMB4 activity raises NRCAM's level | lines that do not express LAMB4 (26) vs lines expressing it (24) | 4.39× lower at baseline in the lines without LAMB4 | 0.003 | ⚠ within organs, on part of the lines; also absent: NRCAM, MEIOB, SOX2; maybe low, not absent; co-absent with the target |
| [[SOX6]] | C | LAMB4 activity raises SOX6's level | lines that do not express LAMB4 (26) vs lines expressing it (24) | 2.29× lower at baseline in the lines without LAMB4 | 0.033 | ⚠ within organs, on part of the lines; also absent: NRCAM, MEIOB, SOX2; maybe low, not absent; co-absent with the target |
| [[GPRIN3]] | C | LAMB4 activity raises GPRIN3's level | lines that do not express LAMB4 (26) vs lines expressing it (24) | 2.74× lower at baseline in the lines without LAMB4 | 0.054 | ⚠ within organs, on part of the lines; also absent: NRCAM, MEIOB, SOX2; maybe low, not absent; co-absent with the target |
| [[KCNJ6]] | C | LAMB4 activity raises KCNJ6's level | lines that do not express LAMB4 (26) vs lines expressing it (24) | 2.67× lower at baseline in the lines without LAMB4 | 0.064 | ⚠ within organs, on part of the lines; also absent: NRCAM, MEIOB, SOX2; maybe low, not absent; co-absent with the target |
| [[CLDN10-AS1]] | C | LAMB4 activity raises CLDN10-AS1's level | lines that do not express LAMB4 (26) vs lines expressing it (24) | 2.13× lower at baseline in the lines without LAMB4 | 0.067 | ⚠ within organs, on part of the lines; also absent: NRCAM, MEIOB, SOX2; maybe low, not absent; co-absent with the target |
| [[FSTL4]] | C | LAMB4 activity raises FSTL4's level | lines that do not express LAMB4 (26) vs lines expressing it (24) | 1.90× lower at baseline in the lines without LAMB4 | 0.072 | ⚠ within organs, on part of the lines; also absent: NRCAM, MEIOB, SOX2; maybe low, not absent; co-absent with the target |
| [[DOK6]] | C | LAMB4 activity raises DOK6's level | lines that do not express LAMB4 (26) vs lines expressing it (24) | 2.35× lower at baseline in the lines without LAMB4 | 0.089 | ⚠ within organs, on part of the lines; also absent: NRCAM, MEIOB, SOX2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.700). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.1, 36.9); signed map (43.1, 45.3). **Vector** length 30.5, 6.20% of its response variance represented; |z| ≥ 3 in 415 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.9 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +9.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +14.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +6.8 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.1 | +1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.1 | +1.4 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -0.2 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -1.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -0.9 | -1.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.9 | -1.4 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.9 | -2.2 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.8 | -1.0 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.8 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | laminin subunit beta 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q31.1 — chr7:108,023,548-108,130,361 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Laminin subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [A4D0S4](https://www.uniprot.org/uniprotkb/A4D0S4) (Laminin subunit beta-4):

> Binding to cells via a high affinity receptor, laminin is thought to mediate the attachment, migration and organization of cells into tissues during embryonic development by interacting with other extracellular matrix components.

**Summary**, from NCBI Gene [22798](https://www.ncbi.nlm.nih.gov/gene/22798):

> Predicted to be an extracellular matrix structural constituent. Predicted to be involved in substrate adhesion-dependent cell spreading. Predicted to be located in extracellular region. Predicted to be part of laminin-121 trimer. Predicted to be active in basement membrane and obsolete extracellular space. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:6491](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6491) · Entrez [22798](https://www.ncbi.nlm.nih.gov/gene/22798) · UniProt [A4D0S4](https://www.uniprot.org/uniprotkb/A4D0S4) · Ensembl [ENSG00000091128](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000091128)

## Data

Gene col 1652: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1652); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1652, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1652]; `tensor/DDL_lfc|DDL_z.npy` [1652]; `embed/gene_vectors.npy` [1652]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1652 or target_col == 1652). Every well: [[LAMB4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAMB4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
