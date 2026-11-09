---
symbol: "CCAR2"
type: "gene"
col: 8205
ensembl_id: "ENSG00000158941"
name: "cell cycle and apoptosis regulator 2"
location: "8p21.3"
module: 127
arm: "+"
pooled_cpm: 28.44
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 0
n_dd_up_clean: 4
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/127"]
generated_by: "tahoemap"
---

# CCAR2

*cell cycle and apoptosis regulator 2* — 8p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 3.87× (z +7.6, q 2e-11, up in 45 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.193×, AsPC-1 0.226×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C32 0.115×, A-427 0.251×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (Hs 766T 0.0530×; ⚠ toxic; transcription drop); [[AZD-7648 (drug)]] 5 µM in 1 line (Hs 766T 0.0546×); [[Thymol (drug)]] 0.5 µM in 1 line (SW48 0.188×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCNX3]] (+0.72, fdr 7e-06), [[RNPS1]] (+0.71, fdr 7e-06), [[MTA2]] (+0.69, fdr 1e-05); moves opposite to [[EIF1B]] (-0.63, fdr 7e-06), [[PIGBOS1]] (-0.60, fdr 8e-06), [[RALGAPA1]] (-0.60, fdr 1e-05).
> It is in [[Module 127]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SPINK1]] → it (grade B ⚠); 2 go from it, the strongest it → cells under [[Celecoxib (drug)]] 0.05 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8205.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.87×** | +7.6 | 2e-11 | 45/48 (SW480, RKO, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.06×** | +6.3 | 1e-07 | 38/47 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +4.8 | 3e-04 | 31/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +4.2 | 0.004 | 30/48 (SW480, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.37× | +3.2 | 0.18 | 19/47 (C32, LOX-IMVI, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.33× | +3.1 | 0.21 | 18/46 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8205.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RKO 0.193×, AsPC-1 0.226×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (C32 0.115×, A-427 0.251×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (Hs 766T 0.0530×; ⚠ toxic; transcription drop); [[AZD-7648 (drug)]] 5 µM in 1 line (Hs 766T 0.0546×); [[Thymol (drug)]] 0.5 µM in 1 line (SW48 0.188×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.717× | -3.4 | 0.21 | 20/37 (Hs 766T, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.801× | -3.4 | 0.21 | 23/48 (SW 1088, C-33 A, …) | rises with dose |  |
| [[Entrectinib (drug)]] 5 µM |  | 0.744× | -3.2 | 0.28 | 22/47 (SW 1271, RPMI-7951, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 5 µM |  | 0.744× | -3.1 | 0.30 | 15/48 (NCI-H23, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8205. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 40.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0530× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[AZD-7648 (drug)]] 5 µM 0.0546× (z -8.9) |
| [[SW480 (line)]] | alt | 31.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 7.90× (z +8.8) | — |
| [[A-427 (line)]] | wt | 32.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 40.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.226× (z -10.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 22.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 41.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -8.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[LY-2584702 (tosylate salt) (drug)]] 5 µM 0.0587× (z -10.8) ⚠ toxic |
| [[RKO (line)]] | wt | 41.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.193× (z -11.8) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 59.6 | 0 | 1 (1 ⚠) | — | [[Torkinib (drug)]] 5 µM 0.0673× (z -10.0) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 44.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW48 (line)]] | wt | 33.0 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.188× (z -8.9) |
| [[A-172 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 32.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 46.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8205), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCNX3]] | +0.72 | +0.65 / +0.73 | both halves | 7e-06 |  |
| [[RNPS1]] | +0.71 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[MTA2]] | +0.69 | +0.54 / +0.76 | both halves | 1e-05 |  |
| [[RPSA]] | +0.69 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[EMC1]] | +0.68 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[ARHGAP4]] | +0.68 | +0.52 / +0.72 | both halves | 1e-05 |  |
| [[ATP13A1]] | +0.66 | +0.44 / +0.72 | both halves | 3e-05 |  |
| [[PRPF8]] | +0.66 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[TBL3]] | +0.66 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[ARF3]] | +0.66 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[ILF2]] | +0.65 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[U2AF2]] | +0.65 | +0.66 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF1B]] | -0.63 | -0.59 / -0.67 | both halves | 7e-06 |  |
| [[PIGBOS1]] | -0.60 | -0.59 / -0.58 | both halves | 8e-06 |  |
| [[RALGAPA1]] | -0.60 | -0.65 / -0.51 | both halves | 1e-05 |  |
| [[CHMP2B]] | -0.59 | -0.54 / -0.56 | both halves | 1e-05 |  |
| [[JMJD1C]] | -0.58 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[UBE2B]] | -0.58 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[SUMO4]] | -0.58 | -0.27 / -0.68 | both halves | 3e-04 |  |
| [[ATF4]] | -0.56 | -0.49 / -0.61 | both halves | 1e-05 |  |
| [[JUND]] | -0.56 | -0.52 / -0.60 | both halves | 1e-05 |  |
| [[EIF1]] | -0.56 | -0.46 / -0.62 | both halves | 2e-05 |  |
| [[MICU1]] | -0.55 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[ATP6V1F]] | -0.55 | -0.53 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPINK1]] | B | SPINK1 activity lowers CCAR2's level | lines that do not express SPINK1 (28) vs lines expressing it (22) | 1.29× higher at baseline in the lines without SPINK1 | 0.093 | ⚠ within organs, on part of the lines; also absent: CDH17, LYZ, GCNT3 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Celecoxib (drug)]] 0.05 µM | C | CCAR2's natural level raises the cells' numbers under Celecoxib 0.05 µM (protects the cells) | CCAR2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.66 | 0.352 over the table, 0.095 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | CCAR2's natural level raises the cells' numbers under ERK5-IN-2 0.5 µM (protects the cells) | CCAR2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.60 | 0.472 over the table, 0.064 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 127]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.674). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.27; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.6, -26.2); signed map (-24.4, -42.2). **Vector** length 74.8, 15.9% of its response variance represented; |z| ≥ 3 in 704 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +5.0 | -0.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.7 | -3.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.4 | -2.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.5 | +0.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.3 | -0.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +6.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +0.9 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.6 | +2.5 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.6 | +1.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +0.2 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -0.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +0.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +1.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -0.1 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -3.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | cell cycle and apoptosis regulator 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.3 — chr8:22,604,757-22,620,964 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DBC-1, DBC1, NET35; previously KIAA1967 |
| Reactome | 4 pathways, smallest: Regulation of HSF1-mediated heat shock response; Cellular response to heat stress; Cellular responses to stress |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N163](https://www.uniprot.org/uniprotkb/Q8N163) (Cell cycle and apoptosis regulator protein 2):

> Core component of the DBIRD complex, a multiprotein complex that acts at the interface between core mRNP particles and RNA polymerase II (RNAPII) and integrates transcript elongation with the regulation of alternative splicing: the DBIRD complex affects local transcript elongation rates and alternative splicing of a large set of exons embedded in (A + T)-rich DNA regions. Inhibits SIRT1 deacetylase activity leading to increasing levels of p53/TP53 acetylation and p53-mediated apoptosis. …

**Summary**, from NCBI Gene [57805](https://www.ncbi.nlm.nih.gov/gene/57805):

> Enables RNA polymerase II complex binding activity and enzyme inhibitor activity. Involved in several processes, including regulation of gene expression; regulation of protein metabolic process; and regulation of signal transduction. Located in several cellular components, including mitochondrial matrix; nuclear body; and spindle. Part of DBIRD complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:23360](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23360) · Entrez [57805](https://www.ncbi.nlm.nih.gov/gene/57805) · UniProt [Q8N163](https://www.uniprot.org/uniprotkb/Q8N163) · Ensembl [ENSG00000158941](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000158941)

## Data

Gene col 8205: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8205); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8205, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8205]; `tensor/DDL_lfc|DDL_z.npy` [8205]; `embed/gene_vectors.npy` [8205]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8205 or target_col == 8205). Every well: [[CCAR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCAR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
