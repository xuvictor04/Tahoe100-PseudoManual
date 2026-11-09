---
symbol: "GREM2"
type: "gene"
col: 11140
ensembl_id: "ENSG00000180875"
name: "gremlin 2, DAN family BMP antagonist"
location: "1q43"
module: 19
arm: "+"
pooled_cpm: 14.59
n_lines_expressing: 10
n_dd_up: 4
n_dd_down: 0
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 31
direction_downstream: 36
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# GREM2

*gremlin 2, DAN family BMP antagonist* — 1q43

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.97× (z +9.3, q 1e-17, up in 0 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.86× (z +6.1, q 2e-07, up in 2 of 8 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (A-172 19.7×; ⚠ unreliable plate only).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 0.0785×, CHP-212 0.102×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (CHP-212 0.126×, NCI-H460 0.249×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (NCI-H460 0.124×, CHP-212 0.0874×; ⚠ cell-cycle shift, explains ~14% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.125×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (NCI-H460 0.158×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC03000]] (+0.90, fdr 7e-06), [[KCNK2]] (+0.88, fdr 7e-06), [[SCARA5]] (+0.86, fdr 7e-06).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 31 arrows point to it, the strongest [[PDE1A]] → it (grade C ⚠); 36 go from it, the strongest it → [[SLCO1C1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11140.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[c-Kit-IN-1 (drug)]] 0.05 µM in 1 line (A-172 19.7×; ⚠ unreliable plate only).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.97×** | +9.3 | 1e-17 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.47×** | +8.7 | 8e-16 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.86×** | +6.1 | 2e-07 | 2/8 (SNU-423, SW 900) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.09×** | +4.8 | 3e-04 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | 1.58× | +3.2 | 0.15 | 3/7 (SNU-423, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | 1.54× | +3.0 | 0.20 | 0/6 | top dose only | position effect removed |
| [[BAY1125976 (drug)]] 0.5 µM |  | 1.83× | +3.0 | 0.20 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11140.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 12 here, 7 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 0.0785×, CHP-212 0.102×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (CHP-212 0.126×, NCI-H460 0.249×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (NCI-H460 0.124×, CHP-212 0.0874×; ⚠ cell-cycle shift, explains ~14% of this change); [[Homoharringtonine (drug)]] 0.05 µM in 1 line (NCI-H460 0.125×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (NCI-H460 0.158×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.577× | -3.6 | 0.13 | 0/7 | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.608× | -3.5 | 0.13 | 3/6 (NCI-H460, CHP-212, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.725× | -3.2 | 0.16 | 3/8 (CHP-212, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.638× | -3.2 | 0.16 | 4/6 (NCI-H460, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.639× | -3.2 | 0.16 | 3/7 (A-172, SNU-423, …) | top dose only |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.620× | -3.1 | 0.16 | 1/7 (AN3 CA) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.634× | -3.1 | 0.16 | 2/7 (NCI-H460, CHP-212) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11140. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 226 | 0 | 13 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0785× (z -19.7) |
| [[CHP-212 (line)]] | wt | 284 | 0 | 7 (6 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -13.2) |
| [[A-172 (line)]] | wt | 10.6 | 1 (1 ⚠) | 0 | [[c-Kit-IN-1 (drug)]] 0.05 µM 19.7× (z +9.2) ⚠ unreliable plate only | — |
| [[A-427 (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.45 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 3.38 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.81 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.03 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.25 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.71 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.74 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.70 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11140), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC03000]] | +0.90 | +0.90 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[KCNK2]] | +0.88 | +0.86 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[SCARA5]] | +0.86 | +0.83 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[CHL1]] | +0.86 | +0.80 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[COL4A6]] | +0.85 | +0.87 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[FENDRR]] | +0.85 | +0.82 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[LINC01035]] | +0.85 | +0.81 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[DPP10]] | +0.83 | +0.76 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[ADGRD1]] | +0.83 | +0.79 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[CTNND2]] | +0.80 | +0.77 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[SERPINB11]] | +0.79 | +0.73 / +0.80 | both halves | 7e-06 |  |
| [[LIN7A]] | +0.79 | +0.76 / +0.76 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 0, C 31. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PDE1A]] | C | PDE1A activity raises GREM2's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 3.20× lower at baseline in the lines without PDE1A | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent; co-absent with the target |
| [[NLGN4Y]] | C | NLGN4Y activity raises GREM2's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 4.08× lower at baseline in the lines without NLGN4Y | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[GSG1L2]] | C | GSG1L2 activity raises GREM2's level | lines that do not express GSG1L2 (45) vs lines expressing it (5) | 5.57× lower at baseline in the lines without GSG1L2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC15A5, GTF2I-AS1, LINC03000; co-absent with the target |
| [[GTF2I-AS1]] | C | GTF2I-AS1 activity raises GREM2's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 3.88× lower at baseline in the lines without GTF2I-AS1 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[KCNE4]] | C | KCNE4 activity raises GREM2's level | lines that do not express KCNE4 (34) vs lines expressing it (16) | 3.26× lower at baseline in the lines without KCNE4 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, NCAM1, PTN; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises GREM2's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 9.56× lower at baseline in the lines without LINC03000 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |
| [[ZNF736P9Y]] | C | ZNF736P9Y activity raises GREM2's level | lines that do not express ZNF736P9Y (40) vs lines expressing it (10) | 2.34× lower at baseline in the lines without ZNF736P9Y | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SPINK13, SUCNR1, ENSG00000260364; co-absent with the target |
| [[SCARA5]] | C | SCARA5 activity raises GREM2's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 3.12× lower at baseline in the lines without SCARA5 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[ESM1]] | C | ESM1 activity raises GREM2's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 2.43× lower at baseline in the lines without ESM1 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865; co-absent with the target |
| [[UTY]] | C | UTY activity raises GREM2's level | lines that do not express UTY (31) vs lines expressing it (19) | 2.63× lower at baseline in the lines without UTY | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ANOS2P, KDM5D, EIF1AY; co-absent with the target |
| [[DPP10]] | C | DPP10 activity raises GREM2's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 4.67× lower at baseline in the lines without DPP10 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[CTNND2]] | C | CTNND2 activity raises GREM2's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 2.59× lower at baseline in the lines without CTNND2 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 5, C 31. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLCO1C1]] | B | GREM2 activity raises SLCO1C1's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 2.41× lower at baseline in the lines without GREM2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054 |
| [[TBX2]] | B | GREM2 activity raises TBX2's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 4.91× lower at baseline in the lines without GREM2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054 |
| [[PLAC4]] | B | GREM2 activity raises PLAC4's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 2.28× lower at baseline in the lines without GREM2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054 |
| [[ANO3]] | B | GREM2 activity raises ANO3's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 2.07× lower at baseline in the lines without GREM2 | 0.063 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054 |
| [[PCDH15]] | B | GREM2 activity raises PCDH15's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 2.60× lower at baseline in the lines without GREM2 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054 |
| [[NLGN4Y]] | C | GREM2 activity raises NLGN4Y's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 8.60× lower at baseline in the lines without GREM2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054; co-absent with the target |
| [[COL8A1]] | C | GREM2 activity raises COL8A1's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 6.93× lower at baseline in the lines without GREM2 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054; co-absent with the target |
| [[LINC03000]] | C | GREM2 activity raises LINC03000's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 4.54× lower at baseline in the lines without GREM2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054; co-absent with the target |
| [[KCNE4]] | C | GREM2 activity raises KCNE4's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 7.29× lower at baseline in the lines without GREM2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054; co-absent with the target |
| [[CDH11]] | C | GREM2 activity raises CDH11's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 5.16× lower at baseline in the lines without GREM2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054; co-absent with the target |
| [[EPB41L3]] | C | GREM2 activity raises EPB41L3's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 4.24× lower at baseline in the lines without GREM2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054; co-absent with the target |
| [[KCNK2]] | C | GREM2 activity raises KCNK2's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 3.07× lower at baseline in the lines without GREM2 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.850). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.1, 36.0); signed map (42.7, 43.9). **Vector** length 45.7, 24.7% of its response variance represented; |z| ≥ 3 in 187 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Neuronal System* (reactome, mean cos +0.52 to 18).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +9.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.8 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +6.1 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.9 | +2.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +0.8 | +2.4 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +0.8 | +1.8 |
| fall | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.3 | -3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -3.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.0 | -2.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -1.1 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.9 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | gremlin 2, DAN family BMP antagonist |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q43 — chr1:240,489,573-240,612,155 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Prdc, FLJ21195, CKTSF1B2, DAND3 |
| Gene groups (HGNC) | DAN family |
| Reactome | 2 pathways, smallest: Signaling by BMP; Signaling by TGFB family members |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H772](https://www.uniprot.org/uniprotkb/Q9H772) (Gremlin-2):

> Cytokine that inhibits the activity of BMP2 and BMP4 in a dose-dependent manner, and thereby modulates signaling by BMP family members. Contributes to the regulation of embryonic morphogenesis via BMP family members. Antagonizes BMP4-induced suppression of progesterone production in granulosa cells.

**Summary**, from NCBI Gene [64388](https://www.ncbi.nlm.nih.gov/gene/64388):

> This gene encodes a member of the BMP (bone morphogenic protein) antagonist family. Like BMPs, BMP antagonists contain cystine knots and typically form homo- and heterodimers. The CAN (cerberus and dan) subfamily of BMP antagonists, to which this gene belongs, is characterized by a C-terminal cystine knot with an eight-membered ring. The antagonistic effect of the secreted glycosylated protein encoded by this gene is likely due to its direct binding to BMP proteins. As an antagonist of BMP, …

**Accessions** — [HGNC:17655](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17655) · Entrez [64388](https://www.ncbi.nlm.nih.gov/gene/64388) · UniProt [Q9H772](https://www.uniprot.org/uniprotkb/Q9H772) · Ensembl [ENSG00000180875](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180875)

## Data

Gene col 11140: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11140); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11140, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11140]; `tensor/DDL_lfc|DDL_z.npy` [11140]; `embed/gene_vectors.npy` [11140]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11140 or target_col == 11140). Every well: [[GREM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GREM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
