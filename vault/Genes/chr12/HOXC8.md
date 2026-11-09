---
symbol: "HOXC8"
type: "gene"
col: 447
ensembl_id: "ENSG00000037965"
name: "homeobox C8"
location: "12q13.13"
module: 46
arm: "+"
pooled_cpm: 8.14
n_lines_expressing: 39
n_dd_up: 5
n_dd_down: 6
n_dd_up_clean: 1
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 6
direction_downstream: 7
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# HOXC8

*homeobox C8* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +6.6, q 3e-08, up in 19 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (KATO III 3.77×; ⚠ cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.309× (z -10.1, q 4e-21, down in 28 of 36 measured lines).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HOXC9]] (+0.78, fdr 7e-06, ⚠ same locus), [[ZIC2]] (+0.68, fdr 2e-05), [[KIF9-AS1]] (+0.66, fdr 1e-05), [[ZBTB8A]] (+0.65, fdr 2e-05); moves opposite to [[IQGAP1]] (-0.57, fdr 3e-05), [[CORO1C]] (-0.56, fdr 6e-05), [[FAM91A1]] (-0.54, fdr 7e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[HOXC10]] → it (grade B ⚠); 7 go from it, the strongest it → [[MTG2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 447.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (KATO III 3.77×; ⚠ cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +6.6 | 3e-08 | 19/32 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +5.1 | 1e-04 | 5/15 (A-427, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.64×** | +4.1 | 0.009 | 12/24 (KATO III, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.59×** | +4.0 | 0.009 | 11/24 (NCI-H2030, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.4 | 0.087 | 14/33 (PANC-1, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 447.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.309×** | -10.1 | 4e-21 | 28/36 (PANC-1, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.340×** | -9.2 | 7e-18 | 26/36 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.423×** | -7.4 | 3e-11 | 23/36 (C-33 A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.605×** | -4.3 | 0.002 | 17/36 (C-33 A, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.627×** | -4.0 | 0.007 | 17/36 (AsPC-1, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.477×** | -3.3 | 0.086 | 12/34 (RKO, LOX-IMVI, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.699× | -3.1 | 0.18 | 11/35 (BT-474, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 447. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 47.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0870× (z -13.6) |
| [[PANC-1 (line)]] | alt | 30.0 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -15.8) |
| [[A-427 (line)]] | wt | 40.3 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.104× (z -14.0) |
| [[KATO III (line)]] | alt | 14.9 | 1 (1 ⚠) | 2 | [[Homoharringtonine (drug)]] 5 µM 3.77× (z +9.9) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 0.5 µM 0.0996× (z -11.9) |
| [[RKO (line)]] | wt | 15.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -14.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.155× (z -9.1) |
| [[AN3 CA (line)]] | alt | 41.9 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0819× (z -9.3) ⚠ cell-cycle shift, explains ~17% of this change |
| [[AsPC-1 (line)]] | alt | 9.45 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0911× (z -10.0) |
| [[BT-474 (line)]] | alt | 9.00 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 11.7 | 0 | 1 | — | [[HI-TOPK-032 (drug)]] 0.05 µM 0.0820× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 18.2 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.162× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H661 (line)]] | alt | 50.7 | 0 | 1 | — | [[LY-2584702 (tosylate salt) (drug)]] 0.05 µM 0.0726× (z -8.9) |
| [[A-172 (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.18 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.816 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.973 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.809 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.34 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.45 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.849 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 7.64 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.605 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.64 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.72 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.81 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.08 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.96 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 447), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 7 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXC9]] | +0.78 | +0.69 / +0.70 | both halves | 7e-06 | same gene group; STRING 883; ⚠ same locus (5.6 kb, same strand: neighbours can correlate without regulation) |
| [[ZIC2]] | +0.68 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[KIF9-AS1]] | +0.66 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[ZBTB8A]] | +0.65 | +0.49 / +0.47 | both halves | 2e-05 |  |
| [[HOXC6]] | +0.63 | +0.68 / +0.44 | both halves | 3e-05 | same gene group; STRING 840; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ZCCHC10]] | +0.60 | +0.37 / +0.57 | both halves | 9e-05 |  |
| [[ATAD2B]] | +0.59 | +0.50 / +0.37 | both halves | 7e-05 |  |
| [[RNF135]] | +0.59 | +0.38 / +0.50 | both halves | 7e-05 |  |
| [[RPP38]] | +0.58 | +0.42 / +0.45 | both halves | 4e-05 |  |
| [[CARNMT1-AS1]] | +0.58 | +0.33 / +0.52 | both halves | 1e-04 |  |
| [[SETD1B]] | +0.58 | +0.42 / +0.40 | both halves | 5e-05 |  |
| [[C1orf56]] | +0.58 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[KDM3B]] | +0.57 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[ZNF785]] | +0.57 | +0.34 / +0.42 | both halves | 1e-04 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IQGAP1]] | -0.57 | -0.48 / -0.44 | both halves | 3e-05 | pathway: Cell-Cell communication |
| [[CORO1C]] | -0.56 | -0.39 / -0.48 | both halves | 6e-05 |  |
| [[FAM91A1]] | -0.54 | -0.37 / -0.58 | both halves | 7e-05 |  |
| [[TGOLN2]] | -0.53 | -0.39 / -0.58 | both halves | 6e-05 |  |
| [[EIF3H]] | -0.51 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[RALY]] | -0.51 | -0.44 / -0.32 | both halves | 2e-04 |  |
| [[TMED7]] | -0.51 | -0.41 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 4, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXC10]] | B | HOXC10 activity raises HOXC8's level | lines that do not express HOXC10 (26) vs lines expressing it (24) | 2.65× lower at baseline in the lines without HOXC10 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: NTRK3, CES1, POTEE |
| [[HOXB-AS1]] | B | HOXB-AS1 activity raises HOXC8's level | lines that do not express HOXB-AS1 (14) vs lines expressing it (36) | 2.45× lower at baseline in the lines without HOXB-AS1 | 0.021 | ⚠ within organs, on part of the lines; also absent: MAP1A, HOXB2, ADAMTS18 |
| [[HDAC6]] | B | HDAC6 activity raises HOXC8's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[ZIC2]] | B | ZIC2 activity raises HOXC8's level | lines that do not express ZIC2 (10) vs lines expressing it (40) | 1.68× lower at baseline in the lines without ZIC2 | 0.094 | ⚠ within organs, on part of the lines; also absent: FOXD1, BEND7 |
| [[HOXC6]] | C | HOXC6 activity raises HOXC8's level | lines that do not express HOXC6 (10) vs lines expressing it (40) | 3.71× lower at baseline in the lines without HOXC6 | 0.006 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC8, FLJ12825; maybe low, not absent; co-absent with the target |
| [[HOXC9]] | C | HOXC9 activity raises HOXC8's level | lines that do not express HOXC9 (10) vs lines expressing it (40) | 3.67× lower at baseline in the lines without HOXC9 | 0.011 | ⚠ within organs, on part of the lines; also absent: HOXC4, LINC01013, SOCS2; co-absent with the target |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 5, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTG2]] | B | HOXC8 activity raises MTG2's level | lines that do not express HOXC8 (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without HOXC8 | 0.019 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC6, IRX5 |
| [[HOXB-AS1]] | B | HOXC8 activity raises HOXB-AS1's level | lines that do not express HOXC8 (11) vs lines expressing it (39) | 2.23× lower at baseline in the lines without HOXC8 | 0.027 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC6, IRX5 |
| [[TSTD3]] | B | HOXC8 activity raises TSTD3's level | lines that do not express HOXC8 (11) vs lines expressing it (39) | 1.36× lower at baseline in the lines without HOXC8 | 0.035 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC6, IRX5 |
| [[ZNRF2P2]] | B | HOXC8 activity raises ZNRF2P2's level | lines that do not express HOXC8 (11) vs lines expressing it (39) | 1.60× lower at baseline in the lines without HOXC8 | 0.037 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC6, IRX5 |
| [[HOXC10]] | B | HOXC8 activity raises HOXC10's level | lines that do not express HOXC8 (11) vs lines expressing it (39) | 3.57× lower at baseline in the lines without HOXC8 | 0.054 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC6, IRX5 |
| [[HOXC6]] | C | HOXC8 activity raises HOXC6's level | lines that do not express HOXC8 (11) vs lines expressing it (39) | 4.36× lower at baseline in the lines without HOXC8 | 0.001 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC6, IRX5; co-absent with the target |
| [[HOXC9]] | C | HOXC8 activity raises HOXC9's level | lines that do not express HOXC8 (11) vs lines expressing it (39) | 3.76× lower at baseline in the lines without HOXC8 | 0.012 | ⚠ within organs, on part of the lines; also absent: HOXC4, HOXC6, IRX5; co-absent with the target |

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.617). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-6.7, 15.6); signed map (4.9, -4.0). **Vector** length 53.7, 9.30% of its response variance represented; |z| ≥ 3 in 661 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +6.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +4.1 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +2.3 | -0.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +1.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +1.6 | +1.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.1 | +0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.0 | +0.8 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +2.1 |
|  | [[venetoclax (drug)]] 5 µM |  | +0.9 | +0.7 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +0.8 | +2.6 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -3.2 | -10.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.1 | -9.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -2.5 | +4.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.3 | +5.1 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.1 | -7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.1 | -3.0 |
|  | [[Fusidic acid (drug)]] 5 µM |  | -0.8 | -1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -0.8 | -1.5 |
|  | [[OTS514 (drug)]] 5 µM |  | -0.8 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | homeobox C8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:54,008,985-54,012,769 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HOX3, HOX3A |
| Gene groups (HGNC) | HOXL subclass homeoboxes |
| Reactome | 8 pathways, smallest: Regulation of CDH11 gene transcription; Regulation of CDH11 Expression and Function; Regulation of Expression and Function of Type II Classical Cadherins |
| Matched by | ensembl_id |

**Function**, from UniProt [P31273](https://www.uniprot.org/uniprotkb/P31273) (Homeobox protein Hox-C8):

> Sequence-specific transcription factor which is part of a developmental regulatory system that provides cells with specific positional identities on the anterior-posterior axis.

**Summary**, from NCBI Gene [3224](https://www.ncbi.nlm.nih.gov/gene/3224):

> This gene belongs to the homeobox family of genes. The homeobox genes encode a highly conserved family of transcription factors that play an important role in morphogenesis in all multicellular organisms. Mammals possess four similar homeobox gene clusters, HOXA, HOXB, HOXC and HOXD, which are located on different chromosomes and consist of 9 to 11 genes arranged in tandem. This gene is one of several homeobox HOXC genes located in a cluster on chromosome 12. The product of this gene may play a …

**Accessions** — [HGNC:5129](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5129) · Entrez [3224](https://www.ncbi.nlm.nih.gov/gene/3224) · UniProt [P31273](https://www.uniprot.org/uniprotkb/P31273) · Ensembl [ENSG00000037965](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000037965)

## Data

Gene col 447: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 447); `tables/drug_effects.parquet` (12 rows, flagged included); `relations/gene_relations.parquet` (col_a == 447, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 447]; `tensor/DDL_lfc|DDL_z.npy` [447]; `embed/gene_vectors.npy` [447]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 447 or target_col == 447). Every well: [[HOXC8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HOXC8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
