---
symbol: "DSG4"
type: "gene"
col: 10557
ensembl_id: "ENSG00000175065"
name: "desmoglein 4"
location: "18q12.1"
module: 73
arm: "+"
pooled_cpm: 3.52
n_lines_expressing: 5
n_dd_up: 17
n_dd_down: 1
n_dd_up_clean: 6
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 12
direction_downstream: 48
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# DSG4

*desmoglein 4* — 18q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 7.89× (z +9.8, q 7e-20, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.94× (z +4.6, q 4e-04, up in 0 of 2 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Erlotinib (drug)]] 0.05 µM: 0.428× (z -3.9, q 0.058, down in 1 of 3 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 0.0472×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.146×); [[Panobinostat (drug)]] 5 µM in 1 line (LoVo 0.0774×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 1 line (LoVo 0.214×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TPTEP1-1]] (+0.83, fdr 7e-06), [[SLC6A20]] (+0.83, fdr 7e-06), [[HEPH]] (+0.82, fdr 7e-06).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[SPINK13]] → it (grade C ⚠); 48 go from it, the strongest it → [[NCF2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10557.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.89×** | +9.8 | 7e-20 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.01×** | +7.9 | 6e-13 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.49×** | +6.8 | 2e-09 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.68×** | +4.7 | 4e-04 | 0/1 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.94×** | +4.6 | 4e-04 | 0/2 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.34×** | +4.2 | 0.003 | 0/1 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.25×** | +4.0 | 0.005 | 0/1 | top dose only | cell-cycle shift (explains ~7% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **2.25×** | +4.0 | 0.005 | 0/1 | inconsistent across doses | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.58×** | +3.9 | 0.007 | 0/1 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.13×** | +3.7 | 0.011 | 0/1 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **4.20×** | +3.7 | 0.011 | 0/1 | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **2.02×** | +3.5 | 0.026 | 0/1 | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.05×** | +3.4 | 0.029 | 0/1 | top dose only | cell-cycle shift (explains ~5% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.92×** | +3.2 | 0.048 | 0/1 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.57×** | +3.1 | 0.067 | 1/3 (LS 180) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.93×** | +3.0 | 0.094 | 0/1 | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10557.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (LoVo 0.0472×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LoVo 0.146×); [[Panobinostat (drug)]] 5 µM in 1 line (LoVo 0.0774×; ⚠ cell-cycle shift, would explain all of this change); [[Belinostat (drug)]] 5 µM in 1 line (LoVo 0.214×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Erlotinib (drug)]] 0.05 µM |  | **0.428×** | -3.9 | 0.058 | 1/3 (LS 180) | inconsistent across doses | position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.489× | -3.3 | 0.30 | 0/3 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10557. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 93.9 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0472× (z -17.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -15.8) |
| [[A-172 (line)]] | wt | 0.312 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.311 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.229 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.266 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.599 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.759 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.316 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.316 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.404 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.424 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.317 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.470 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.255 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.291 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.631 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.398 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.377 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.884 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.225 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.527 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.254 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.301 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.291 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.284 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.394 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.275 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.228 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.344 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.277 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.252 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.276 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.291 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.314 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.614 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.794 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.00 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.290 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10557), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPTEP1-1]] | +0.83 | +0.86 / +0.72 | both halves | 7e-06 |  |
| [[SLC6A20]] | +0.83 | +0.75 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[HEPH]] | +0.82 | +0.76 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[LINC02582]] | +0.81 | +0.77 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[CALB1]] | +0.81 | +0.76 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[NPSR1]] | +0.77 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[SPON1]] | +0.76 | +0.70 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[FAM3D]] | +0.76 | +0.77 / +0.66 | both halves | 7e-06 |  |
| [[DSG3]] | +0.76 | +0.70 / +0.73 | both halves | 7e-06 | same gene group; pathway: Formation of the cornified envelope; STRING 711; ⚠ same locus (32.8 kb, same strand: neighbours can correlate without regulation) |
| [[TPRXL]] | +0.75 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[IGFL2]] | +0.75 | +0.83 / +0.63 | both halves | 7e-06 |  |
| [[LINC02474]] | +0.73 | +0.67 / +0.65 | both halves | 7e-06 |  |
| [[NOSTRIN]] | +0.71 | +0.61 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPINK13]] | C | SPINK13 activity raises DSG4's level | lines that do not express SPINK13 (45) vs lines expressing it (5) | 3.30× lower at baseline in the lines without SPINK13 | 0.005 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target |
| [[KRT14]] | C | KRT14 activity raises DSG4's level | lines that do not express KRT14 (43) vs lines expressing it (7) | 2.62× lower at baseline in the lines without KRT14 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230258, DSG4, SPINK13; co-absent with the target |
| [[LINC02582]] | C | LINC02582 activity raises DSG4's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 2.05× lower at baseline in the lines without LINC02582 | 0.043 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; co-absent with the target |
| [[TPTEP1-1]] | C | TPTEP1-1 activity raises DSG4's level | lines that do not express TPTEP1-1 (41) vs lines expressing it (9) | 2.01× lower at baseline in the lines without TPTEP1-1 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000283633, GCG, ENSG00000230975; co-absent with the target |
| [[C6orf132]] | C | C6orf132 activity raises DSG4's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 1.44× lower at baseline in the lines without C6orf132 | 0.050 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1; co-absent with the target |
| [[KRT6A]] | C | KRT6A activity raises DSG4's level | lines that do not express KRT6A (41) vs lines expressing it (9) | 2.33× lower at baseline in the lines without KRT6A | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DSG4, ENSG00000230975, ENSG00000248588; co-absent with the target |
| [[MMP28]] | C | MMP28 activity raises DSG4's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.32× lower at baseline in the lines without MMP28 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent; co-absent with the target |
| [[REG4]] | C | REG4 activity raises DSG4's level | lines that do not express REG4 (43) vs lines expressing it (7) | 2.69× lower at baseline in the lines without REG4 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |
| [[ZNF736P9Y]] | C | ZNF736P9Y activity raises DSG4's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 1.83× lower at baseline in the lines without ZNF736P9Y | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364; co-absent with the target |
| [[DSG3]] | C | DSG3 activity raises DSG4's level | lines that do not express DSG3 (41) vs lines expressing it (9) | 2.33× lower at baseline in the lines without DSG3 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, TRIM31, NPSR1; co-absent with the target |
| [[ERG]] | C | ERG activity raises DSG4's level | lines that do not express ERG (30) vs lines expressing it (20) | 1.32× lower at baseline in the lines without ERG | 0.092 | ⚠ within organs, on part of the lines; also absent: FUT9, ZIC1, MDGA2; maybe low, not absent; co-absent with the target |
| [[MUC2]] | C | MUC2 activity raises DSG4's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 2.22× lower at baseline in the lines without MUC2 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4; co-absent with the target |

### Downstream of this gene

*48 arrows, 48 of them with an alert ⚠; grade A 0, B 12, C 36. Shown: the 12 strongest; 36 more arrows (36 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCF2]] | B | DSG4 activity raises NCF2's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 2.90× lower at baseline in the lines without DSG4 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031 |
| [[GSKIP]] | B | DSG4 activity raises GSKIP's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 1.99× lower at baseline in the lines without DSG4 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031 |
| [[B4GALNT3]] | B | DSG4 activity raises B4GALNT3's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 5.69× lower at baseline in the lines without DSG4 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031 |
| [[TRABD2A]] | B | DSG4 activity raises TRABD2A's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 3.30× lower at baseline in the lines without DSG4 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031 |
| [[ITPK1]] | B | DSG4 activity raises ITPK1's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 2.87× lower at baseline in the lines without DSG4 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031 |
| [[NOSTRIN]] | B | DSG4 activity raises NOSTRIN's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 4.59× lower at baseline in the lines without DSG4 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031 |
| [[TLN2]] | B | DSG4 activity raises TLN2's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 2.54× lower at baseline in the lines without DSG4 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031 |
| [[IGSF9]] | B | DSG4 activity raises IGSF9's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 2.49× lower at baseline in the lines without DSG4 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031 |
| [[VILL]] | B | DSG4 activity raises VILL's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 2.43× lower at baseline in the lines without DSG4 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031 |
| [[TMEM229B]] | B | DSG4 activity raises TMEM229B's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 1.86× lower at baseline in the lines without DSG4 | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031 |
| [[INPP1]] | B | DSG4 activity raises INPP1's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 3.12× lower at baseline in the lines without DSG4 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031 |
| [[SLC9A2]] | B | DSG4 activity raises SLC9A2's level | lines that do not express DSG4 (45) vs lines expressing it (5) | 4.18× lower at baseline in the lines without DSG4 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, GPR15, ENSG00000237031 |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.853). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.5, 50.3); signed map (66.0, 7.9). **Vector** length 18.3, 11.1% of its response variance represented; |z| ≥ 3 in 83 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +0.6 | +4.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.5 | +0.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +0.4 | -0.8 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +0.4 | +2.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +0.4 | +7.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +0.3 | +0.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.2 | +1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.2 | +0.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +0.2 | +1.4 |
| fall | [[GSK1059615 (drug)]] 5 µM |  | -0.4 | -1.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -0.4 | +0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -0.3 | -0.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.3 | -0.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.3 | -2.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.2 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | desmoglein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q12.1 — chr18:31,376,777-31,414,912 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CDHF13, LAH |
| Gene groups (HGNC) | Desmosomal cadherins |
| Reactome | 2 pathways, smallest: Formation of the cornified envelope; Keratinization |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86SJ6](https://www.uniprot.org/uniprotkb/Q86SJ6) (Desmoglein-4):

> A component of desmosome cell-cell junctions which are required for positive regulation of cellular adhesion (By similarity). Coordinates the transition from proliferation to differentiation in hair follicle keratinocytes (By similarity). Plays a role in moderating lymphocyte migration to inflamed skin and maintaining homeostasis of the epidermal inflammatory response (By similarity).

**Summary**, from NCBI Gene [147409](https://www.ncbi.nlm.nih.gov/gene/147409):

> This gene encodes a member of the desmoglein subgroup of desmosomal cadherins. The encoded preproprotein is proteolytically processed to generate the mature protein. This protein is a transmembrane component of desmosomes and may play a role in cell-cell adhesion in epithelial cells. Mutations in the gene are associated with localized autosomal recessive hypotrichosis and monilethrix, characterized by impaired hair growth. [provided by RefSeq, May 2016]

**Accessions** — [HGNC:21307](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21307) · Entrez [147409](https://www.ncbi.nlm.nih.gov/gene/147409) · UniProt [Q86SJ6](https://www.uniprot.org/uniprotkb/Q86SJ6) · Ensembl [ENSG00000175065](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175065)

## Data

Gene col 10557: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10557); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10557, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10557]; `tensor/DDL_lfc|DDL_z.npy` [10557]; `embed/gene_vectors.npy` [10557]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10557 or target_col == 10557). Every well: [[DSG4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DSG4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
