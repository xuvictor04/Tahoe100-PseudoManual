---
symbol: "SPDYE10"
type: "gene"
col: 15825
ensembl_id: "ENSG00000274570"
name: "speedy/RINGO cell cycle regulator family member E10"
location: "7q11.23"
module: 19
arm: "+"
pooled_cpm: 2.2
n_lines_expressing: 40
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 10
direction_downstream: 2
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SPDYE10

*speedy/RINGO cell cycle regulator family member E10* — 7q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.57× (z +11.0, q 2e-25, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.81× (z +8.9, q 9e-17, up in 8 of 10 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.0273×, A498 0.0513×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0513×; ⚠ cell-cycle shift, explains ~10% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0544×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.147×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCKAP5-AS2]] (+0.80, fdr 7e-06), [[GTF2I-AS1]] (+0.79, fdr 7e-06), [[PAX7]] (+0.78, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[GTF2I-AS1]] → it (grade B ⚠); 2 go from it, the strongest it → [[IQCM]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15825.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.57×** | +11.0 | 2e-25 | 1/2 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.44×** | +9.1 | 3e-17 | 2/3 (A498, PANC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.81×** | +8.9 | 9e-17 | 8/10 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.08×** | +7.9 | 3e-13 | 1/2 (A498) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.43×** | +3.9 | 0.010 | 0/2 | top dose only | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.21×** | +3.4 | 0.055 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.79×** | +3.3 | 0.087 | 0/3 | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.76×** | +3.2 | 0.087 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.66× | +3.1 | 0.11 | 0/5 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.77× | +3.1 | 0.11 | 1/3 (A498) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.74× | +3.0 | 0.13 | 1/6 (SW480) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H460 0.0273×, A498 0.0513×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0513×; ⚠ cell-cycle shift, explains ~10% of this change); [[Harringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0544×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.147×).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15825. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.5 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0273× (z -23.7) |
| [[A498 (line)]] | wt | 4.50 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0513× (z -13.4) |
| [[A-172 (line)]] | wt | 0.786 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.617 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.824 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.501 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.881 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.734 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.974 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.707 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.499 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.679 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.693 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.759 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.815 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.714 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.646 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.600 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.657 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.455 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.477 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.595 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.438 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.833 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.727 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.508 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.636 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.839 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.660 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.800 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.560 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.829 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.471 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.552 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.493 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.623 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.635 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.600 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.733 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.690 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.733 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.605 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15825), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCKAP5-AS2]] | +0.80 | +0.74 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[GTF2I-AS1]] | +0.79 | +0.86 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[PAX7]] | +0.78 | +0.77 / +0.75 | both halves | 7e-06 |  |
| [[GLP2R]] | +0.77 | +0.80 / +0.66 | both halves | 7e-06 |  |
| [[CTNND2]] | +0.77 | +0.73 / +0.73 | both halves | 7e-06 |  |
| [[SCARA5]] | +0.75 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[LINC03000]] | +0.75 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[P3H2-AS1]] | +0.74 | +0.70 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[CHL1]] | +0.72 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[DPP10]] | +0.71 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[LINC01035]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[LAMB4]] | +0.70 | +0.67 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GTF2I-AS1]] | B | GTF2I-AS1 activity raises SPDYE10's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 2.79× lower at baseline in the lines without GTF2I-AS1 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent |
| [[SPINK13]] | B | SPINK13 activity raises SPDYE10's level | lines that do not express SPINK13 (45) vs lines expressing it (5) | 2.26× lower at baseline in the lines without SPINK13 | 0.010 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975 |
| [[GSG1L2]] | B | GSG1L2 activity raises SPDYE10's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 2.63× lower at baseline in the lines without GSG1L2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000 |
| [[LINC03000]] | B | LINC03000 activity raises SPDYE10's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 2.24× lower at baseline in the lines without LINC03000 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4 |
| [[SLC15A5]] | B | SLC15A5 activity raises SPDYE10's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 2.24× lower at baseline in the lines without SLC15A5 | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent |
| [[CHL1]] | B | CHL1 activity raises SPDYE10's level | lines that do not express CHL1 (42) vs lines expressing it (8) | 1.83× lower at baseline in the lines without CHL1 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, GSG1L2, ENSG00000241168 |
| [[SCARA5]] | B | SCARA5 activity raises SPDYE10's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 1.91× lower at baseline in the lines without SCARA5 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5 |
| [[SERPINB11]] | B | SERPINB11 activity raises SPDYE10's level | lines that do not express SERPINB11 (43) vs lines expressing it (7) | 1.92× lower at baseline in the lines without SERPINB11 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, SUCNR1, HOPX |
| [[CTNND2]] | B | CTNND2 activity raises SPDYE10's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 1.59× lower at baseline in the lines without CTNND2 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent |
| [[TBXT]] | C | TBXT activity raises SPDYE10's level | lines that do not express TBXT (47) vs lines expressing it (3) | 4.10× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; its own permutation p |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IQCM]] | B | SPDYE10 activity lowers IQCM's level | lines that do not express SPDYE10 (10) vs lines expressing it (40) | 1.19× higher at baseline in the lines without SPDYE10 | 0.055 | ⚠ within organs, on part of the lines; also absent: SSPOP, SCML2, DISP3; maybe low, not absent |
| [[LINC02864]] | B | SPDYE10 activity lowers LINC02864's level | lines that do not express SPDYE10 (10) vs lines expressing it (40) | 2.44× higher at baseline in the lines without SPDYE10 | 0.079 | ⚠ within organs, on part of the lines; also absent: SSPOP, SCML2, DISP3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.787). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.5, 36.4); signed map (42.8, 44.7). **Vector** length 33.5, 6.34% of its response variance represented; |z| ≥ 3 in 482 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +11.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +9.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +1.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +1.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.9 | +1.8 |
|  | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | +0.8 | +1.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.5 | -2.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.5 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.3 | -1.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.2 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -2.5 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -1.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.8 | -2.5 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.8 | -0.2 |

## What is on record

|  |  |
|---|---|
| Name | speedy/RINGO cell cycle regulator family member E10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q11.23 — chr7:73,104,008-73,155,431 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously SPDYE10P |
| Gene groups (HGNC) | Speedy/RINGO cell cycle regulator family |
| Matched by | ensembl_id |

UniProt [P0DUX0](https://www.uniprot.org/uniprotkb/P0DUX0) carries no function annotation.

**Summary**, from NCBI Gene [643862](https://www.ncbi.nlm.nih.gov/gene/643862):

> Enables acetylcholine receptor regulator activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:51506](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51506) · Entrez [643862](https://www.ncbi.nlm.nih.gov/gene/643862) · UniProt [P0DUX0](https://www.uniprot.org/uniprotkb/P0DUX0) · Ensembl [ENSG00000274570](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000274570)

## Data

Gene col 15825: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15825); `tables/drug_effects.parquet` (11 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15825, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15825]; `tensor/DDL_lfc|DDL_z.npy` [15825]; `embed/gene_vectors.npy` [15825]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15825 or target_col == 15825). Every well: [[SPDYE10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPDYE10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
