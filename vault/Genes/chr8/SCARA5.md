---
symbol: "SCARA5"
type: "gene"
col: 9596
ensembl_id: "ENSG00000168079"
name: "scavenger receptor class A member 5"
location: "8p21.1"
module: 19
arm: "+"
pooled_cpm: 8.44
n_lines_expressing: 7
n_dd_up: 6
n_dd_down: 0
n_dd_up_clean: 3
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 23
direction_downstream: 40
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SCARA5

*scavenger receptor class A member 5* — 8p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.82× (z +10.8, q 3e-24, up in 0 of 1 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.63× (z +5.6, q 3e-06, up in 0 of 3 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.0304×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0167×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0537×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.144×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHL1]] (+0.91, fdr 7e-06), [[SLC15A5]] (+0.90, fdr 7e-06), [[LINC03000]] (+0.90, fdr 7e-06); moves opposite to [[ADRA2C]] (-0.50, fdr 3e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 23 arrows point to it, the strongest [[MARCOL]], [[SPINK13]] → it (grade C ⚠); 40 go from it, the strongest it → [[PLAC4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9596.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.82×** | +10.8 | 3e-24 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.30×** | +9.7 | 7e-20 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.47×** | +8.1 | 1e-13 | 0/1 | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.63×** | +5.6 | 3e-06 | 0/3 | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.90×** | +5.3 | 2e-05 | 0/3 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.76×** | +4.6 | 4e-04 | 1/4 (RPMI-7951) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | 1.73× | +3.2 | 0.13 | 0/2 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9596.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 15 here, 6 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H460 0.0304×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (NCI-H460 0.0167×); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.0537×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 0.144×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | 0.555× | -3.5 | 0.30 | 1/3 (NCI-H460) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | 0.577× | -3.2 | 0.35 | 3/3 (NCI-H460, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9596. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 150 | 0 | 16 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0304× (z -24.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0167× (z -20.5) |
| [[A-172 (line)]] | wt | 0.951 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.636 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.738 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.941 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.928 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.858 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.819 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.917 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.948 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.799 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.734 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.812 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.656 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.951 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.683 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.948 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.763 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.873 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.812 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.899 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.60 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.866 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.794 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9596), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHL1]] | +0.91 | +0.84 / +0.91 | both halves | 7e-06 | **novel candidate** |
| [[SLC15A5]] | +0.90 | +0.92 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[LINC03000]] | +0.90 | +0.87 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[PAX7]] | +0.89 | +0.88 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[DPP10]] | +0.88 | +0.82 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[CTNND2]] | +0.87 | +0.84 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[GREM2]] | +0.86 | +0.83 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[LINC01035]] | +0.84 | +0.77 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[GLP2R]] | +0.82 | +0.81 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[SERPINB11]] | +0.80 | +0.74 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[ADGRD1]] | +0.80 | +0.73 / +0.85 | both halves | 7e-06 |  |
| [[PDE1A]] | +0.79 | +0.72 / +0.84 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADRA2C]] | -0.50 | -0.49 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 0, C 23. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MARCOL]], [[SPINK13]] | C | MARCOL, SPINK13 activity raises SCARA5's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 4.95× lower at baseline in the lines without MARCOL, SPINK13 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[ZNF736P9Y]] | C | ZNF736P9Y activity raises SCARA5's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 2.33× lower at baseline in the lines without ZNF736P9Y | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364; co-absent with the target |
| [[GTF2I-AS1]] | C | GTF2I-AS1 activity raises SCARA5's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 3.80× lower at baseline in the lines without GTF2I-AS1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[GSG1L2]] | C | GSG1L2 activity raises SCARA5's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 5.19× lower at baseline in the lines without GSG1L2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises SCARA5's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 3.97× lower at baseline in the lines without LINC03000 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |
| [[C5orf46]] | C | C5orf46 activity raises SCARA5's level | lines that do not express C5orf46 (33) vs lines expressing it (17) | 1.84× lower at baseline in the lines without C5orf46 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, LOX, CARMN; co-absent with the target |
| [[SLC15A5]] | C | SLC15A5 activity raises SCARA5's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 4.00× lower at baseline in the lines without SLC15A5 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent; co-absent with the target |
| [[AKR1B10]] | C | AKR1B10 activity raises SCARA5's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 2.09× lower at baseline in the lines without AKR1B10 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[LINC01508]] | C | LINC01508 activity raises SCARA5's level | lines that do not express LINC01508 (42) vs lines expressing it (8) | 2.56× lower at baseline in the lines without LINC01508 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, SPINK13, RHEX; co-absent with the target |
| [[CTNND2]] | C | CTNND2 activity raises SCARA5's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 2.31× lower at baseline in the lines without CTNND2 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent; co-absent with the target |
| [[KCNE4]] | C | KCNE4 activity raises SCARA5's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 1.79× lower at baseline in the lines without KCNE4 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN; co-absent with the target |
| [[NLGN4Y]] | C | NLGN4Y activity raises SCARA5's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 1.79× lower at baseline in the lines without NLGN4Y | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |

### Downstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 7, C 33. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLAC4]] | B | SCARA5 activity raises PLAC4's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 3.26× lower at baseline in the lines without SCARA5 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5 |
| [[KCNMB2]] | B | SCARA5 activity raises KCNMB2's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 4.06× lower at baseline in the lines without SCARA5 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5 |
| [[PART1]] | B | SCARA5 activity raises PART1's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 1.99× lower at baseline in the lines without SCARA5 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5 |
| [[SLC9A2]] | B | SCARA5 activity raises SLC9A2's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 2.79× lower at baseline in the lines without SCARA5 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5 |
| [[PDE8B]] | B | SCARA5 activity raises PDE8B's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 2.00× lower at baseline in the lines without SCARA5 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5 |
| [[SPDYE10]] | B | SCARA5 activity raises SPDYE10's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 1.91× lower at baseline in the lines without SCARA5 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5 |
| [[PRSS23-AS1]] | B | SCARA5 activity raises PRSS23-AS1's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 1.90× lower at baseline in the lines without SCARA5 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5 |
| [[SPINK13]] | C | SCARA5 activity raises SPINK13's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 4.06× lower at baseline in the lines without SCARA5 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[MARCOL]] | C | SCARA5 activity raises MARCOL's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 3.88× lower at baseline in the lines without SCARA5 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[ZNF736P9Y]] | C | SCARA5 activity raises ZNF736P9Y's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 4.25× lower at baseline in the lines without SCARA5 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[KCNE4]] | C | SCARA5 activity raises KCNE4's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 8.52× lower at baseline in the lines without SCARA5 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[P3H2]] | C | SCARA5 activity raises P3H2's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 4.26× lower at baseline in the lines without SCARA5 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.807). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.1, 36.3); signed map (43.0, 44.1). **Vector** length 34.3, 29.0% of its response variance represented; |z| ≥ 3 in 89 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.0 | +9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.7 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +0.7 | +10.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +0.7 | +5.3 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +0.6 | -0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.5 | +5.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.5 | +3.0 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +0.4 | +2.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.4 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -0.6 | -0.6 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -0.5 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -0.5 | -3.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.5 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.5 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.4 | -2.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.4 | -1.6 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.4 | -1.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.4 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | scavenger receptor class A member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p21.1 — chr8:27,869,883-27,992,673 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ23907, MGC45780, NET33 |
| Gene groups (HGNC) | Scavenger receptors; Scavenger receptor cysteine rich domain containing; MicroRNA protein coding host genes |
| Reactome | 3 pathways, smallest: Scavenging by Class A Receptors; Binding and Uptake of Ligands by Scavenger Receptors; Vesicle-mediated transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6ZMJ2](https://www.uniprot.org/uniprotkb/Q6ZMJ2) (Scavenger receptor class A member 5):

> Ferritin receptor that mediates non-transferrin-dependent delivery of iron. Mediates cellular uptake of ferritin-bound iron by stimulating ferritin endocytosis from the cell surface with consequent iron delivery within the cell. Delivery of iron to cells by ferritin is required for the development of specific cell types, suggesting the existence of cell type-specific mechanisms of iron traffic in organogenesis, which alternatively utilize transferrin or non-transferrin iron delivery pathways. …

**Summary**, from NCBI Gene [286133](https://www.ncbi.nlm.nih.gov/gene/286133):

> Predicted to enable ferritin receptor activity and scavenger receptor activity. Predicted to be involved in several processes, including intracellular iron ion homeostasis; iron ion transmembrane transport; and protein homotrimerization. Predicted to act upstream of or within cellular response to heat. Predicted to be located in cell surface and membrane. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28701](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28701) · Entrez [286133](https://www.ncbi.nlm.nih.gov/gene/286133) · UniProt [Q6ZMJ2](https://www.uniprot.org/uniprotkb/Q6ZMJ2) · Ensembl [ENSG00000168079](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000168079)

## Data

Gene col 9596: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9596); `tables/drug_effects.parquet` (9 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9596, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9596]; `tensor/DDL_lfc|DDL_z.npy` [9596]; `embed/gene_vectors.npy` [9596]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9596 or target_col == 9596). Every well: [[SCARA5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCARA5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
