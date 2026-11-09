---
symbol: "SPINK13"
type: "gene"
col: 13205
ensembl_id: "ENSG00000214510"
name: "serine peptidase inhibitor Kazal type 13"
location: "5q32"
module: 19
arm: "+"
pooled_cpm: 9.73
n_lines_expressing: 5
n_dd_up: 8
n_dd_down: 0
n_dd_up_clean: 2
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 13
direction_downstream: 39
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# SPINK13

*serine peptidase inhibitor Kazal type 13* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.49× (z +8.9, q 5e-16, up in 1 of 2 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.06× (z +6.3, q 5e-08, up in 2 of 3 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (A-172 24.5×); [[Trametinib (drug)]] 0.5 µM in 1 line (A-172 26.3×); [[Cobimetinib (drug)]] 5 µM in 1 line (A-172 58.5×).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (LoVo 0.0269×; ⚠ cell-cycle shift, explains ~35% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (LoVo 0.0290×; ⚠ cell-cycle shift, explains ~50% of this change); [[Belinostat (drug)]] 5 µM in 1 line (LoVo 0.0458×); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H460 0.0562×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (LoVo 0.134×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MARCOL]] (+0.93, fdr 7e-06, ⚠ same locus), [[MYO16-AS1]] (+0.61, fdr 2e-05), [[GASK1B]] (+0.61, fdr 1e-05), [[GASK1B-AS1]] (+0.61, fdr 1e-05); moves opposite to [[LTBP3]] (-0.48, fdr 5e-05), [[TGFB1]] (-0.47, fdr 7e-05), [[ETV5]] (-0.47, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[SCARA5]] → it (grade C ⚠); 39 go from it, the strongest it → [[SPDYE10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13205.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Selinexor (drug)]] 5 µM in 1 line (A-172 24.5×); [[Trametinib (drug)]] 0.5 µM in 1 line (A-172 26.3×); [[Cobimetinib (drug)]] 5 µM in 1 line (A-172 58.5×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.49×** | +8.9 | 5e-16 | 1/2 (NCI-H460) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.82×** | +8.2 | 6e-14 | 0/3 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.10×** | +8.0 | 2e-13 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.06×** | +6.3 | 5e-08 | 2/3 (A-172, LoVo) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.38×** | +5.1 | 3e-05 | 1/3 (A-172) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.04×** | +4.4 | 0.001 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.86×** | +3.8 | 0.011 | 1/3 (A-172) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.81×** | +3.6 | 0.019 | 0/3 | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.69× | +3.1 | 0.12 | 0/3 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | 1.42× | +3.1 | 0.12 | 2/3 (A-172, NCI-H460) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 0.05 µM |  | 1.64× | +3.0 | 0.12 | 0/3 | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.41× | +3.0 | 0.13 | 1/3 (A-172) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13205.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 1 line (LoVo 0.0269×; ⚠ cell-cycle shift, explains ~35% of this change); [[Panobinostat (drug)]] 5 µM in 1 line (LoVo 0.0290×; ⚠ cell-cycle shift, explains ~50% of this change); [[Belinostat (drug)]] 5 µM in 1 line (LoVo 0.0458×); [[Digitoxin (drug)]] 0.05 µM in 1 line (NCI-H460 0.0562×); [[Ixazomib citrate (drug)]] 0.5 µM in 1 line (LoVo 0.134×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.844× | -3.5 | 0.24 | 0/3 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.583× | -3.3 | 0.29 | 2/3 (LoVo, NCI-H460) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.599× | -3.1 | 0.29 | 2/3 (NCI-H460, LoVo) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tirabrutinib (drug)]] 0.05 µM |  | 0.584× | -3.0 | 0.29 | 0/3 | inconsistent across doses |  |
| [[Phenytoin (sodium) (drug)]] 0.5 µM |  | 0.608× | -3.0 | 0.29 | 0/3 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13205. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 241 | 0 | 5 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0269× (z -15.8) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0458× (z -13.5) |
| [[A-172 (line)]] | wt | 8.79 | 4 | 0 | [[Selinexor (drug)]] 5 µM 24.5× (z +10.7) | — |
| [[NCI-H460 (line)]] | wt | 9.33 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.0562× (z -10.4) |
| [[A-427 (line)]] | wt | 0.775 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.991 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.954 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.982 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.993 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.832 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.805 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.945 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.608 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.751 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.979 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.82 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.913 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.879 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.688 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.985 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.911 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.746 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.884 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.861 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.988 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.20 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.953 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.863 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13205), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 4 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MARCOL]] | +0.93 | +0.95 / +0.92 | both halves | 7e-06 | ⚠ same locus (24.6 kb, same strand: neighbours can correlate without regulation) |
| [[MYO16-AS1]] | +0.61 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[GASK1B]] | +0.61 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[GASK1B-AS1]] | +0.61 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[PDE1A]] | +0.60 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[SCARA5]] | +0.59 | +0.66 / +0.42 | both halves | 4e-05 |  |
| [[ABCC9]] | +0.59 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[LINC01508]] | +0.58 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[GLP2R]] | +0.58 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[PAX7]] | +0.57 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[LINC00457]] | +0.55 | +0.64 / +0.42 | both halves | 4e-05 |  |
| [[LINC02945]] | +0.55 | +0.41 / +0.43 | both halves | 4e-05 |  |
| [[SLC15A5]] | +0.54 | +0.53 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LTBP3]] | -0.48 | -0.40 / -0.50 | both halves | 5e-05 |  |
| [[TGFB1]] | -0.47 | -0.37 / -0.40 | both halves | 7e-05 |  |
| [[ETV5]] | -0.47 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[PGF]] | -0.43 | -0.38 / -0.43 | both halves | 7e-05 |  |
| [[DNAAF9]] | -0.43 | -0.41 / -0.37 | both halves | 7e-05 |  |
| [[RGS17]] | -0.43 | -0.32 / -0.52 | both halves | 1e-04 |  |
| [[OGG1]] | -0.42 | -0.34 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 0, C 13. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCARA5]] | C | SCARA5 activity raises SPINK13's level | lines that do not express SCARA5 (43) vs lines expressing it (7) | 4.06× lower at baseline in the lines without SCARA5 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000260364, GSG1L2, SLC15A5; co-absent with the target |
| [[PRICKLE1]] | C | PRICKLE1 activity raises SPINK13's level | lines that do not express PRICKLE1 (26) vs lines expressing it (24) | 1.52× lower at baseline in the lines without PRICKLE1 | 0.009 | ⚠ within organs, on part of the lines; also absent: COL4A2, NR0B1, THBD; co-absent with the target |
| [[P3H2-AS1]] | C | P3H2-AS1 activity raises SPINK13's level | lines that do not express P3H2-AS1 (30) vs lines expressing it (20) | 1.72× lower at baseline in the lines without P3H2-AS1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: P3H2, SRGN, KIRREL3; co-absent with the target |
| [[LINC01508]] | C | LINC01508 activity raises SPINK13's level | lines that do not express LINC01508 (42) vs lines expressing it (8) | 3.15× lower at baseline in the lines without LINC01508 | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, SPINK13, RHEX; co-absent with the target |
| [[NLGN4Y]] | C | NLGN4Y activity raises SPINK13's level | lines that do not express NLGN4Y (37) vs lines expressing it (13) | 1.45× lower at baseline in the lines without NLGN4Y | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GREM2, PDGFRB, PSG9; co-absent with the target |
| [[GTF2I-AS1]] | C | GTF2I-AS1 activity raises SPINK13's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 2.19× lower at baseline in the lines without GTF2I-AS1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[LINC01257]] | C | LINC01257 activity raises SPINK13's level | lines that do not express LINC01257 (31) vs lines expressing it (19) | 1.85× lower at baseline in the lines without LINC01257 | 0.044 | ⚠ within organs, on part of the lines; also absent: MIR3667HG, LINC01446, NAA11; maybe low, not absent; co-absent with the target |
| [[SLC15A5]] | C | SLC15A5 activity raises SPINK13's level | lines that do not express SLC15A5 (44) vs lines expressing it (6) | 2.19× lower at baseline in the lines without SLC15A5 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, CGA, GTF2I-AS1; maybe low, not absent; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises SPINK13's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 2.14× lower at baseline in the lines without LINC03000 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |
| [[P3H2]] | C | P3H2 activity raises SPINK13's level | lines that do not express P3H2 (28) vs lines expressing it (22) | 1.61× lower at baseline in the lines without P3H2 | 0.052 | ⚠ within organs, on part of the lines; also absent: P3H2-AS1, SRGN, SPOCK1; co-absent with the target |
| [[TBXT]] | C | TBXT activity raises SPINK13's level | lines that do not express TBXT (47) vs lines expressing it (3) | 3.93× lower at baseline in the lines without TBXT | 0.060 | ⚠ few lines (47 vs 3); within organs, on part of the lines; co-occurs with TP53; also absent: LINC00824, APOB, BMP10; co-absent with the target; its own permutation p |
| [[PDE1A]] | C | PDE1A activity raises SPINK13's level | lines that do not express PDE1A (38) vs lines expressing it (12) | 1.54× lower at baseline in the lines without PDE1A | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253474, ENSG00000249894, CHL1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 5, C 34. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SPDYE10]] | B | SPINK13 activity raises SPDYE10's level | lines that do not express SPINK13 (45) vs lines expressing it (5) | 2.26× lower at baseline in the lines without SPINK13 | 0.010 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975 |
| [[SLC9A2]] | B | [[MARCOL]], SPINK13 activity raises SLC9A2's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 3.00× lower at baseline in the lines without MARCOL, SPINK13 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent genes |
| [[PTPRB]] | B | [[MARCOL]], SPINK13 activity raises PTPRB's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 3.76× lower at baseline in the lines without MARCOL, SPINK13 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent genes |
| [[LINC00534]] | B | [[MARCOL]], SPINK13 activity raises LINC00534's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 2.33× lower at baseline in the lines without MARCOL, SPINK13 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent genes |
| [[SOX6]] | B | [[MARCOL]], SPINK13 activity raises SOX6's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 1.69× lower at baseline in the lines without MARCOL, SPINK13 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent genes |
| [[SCARA5]] | C | [[MARCOL]], SPINK13 activity raises SCARA5's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 4.95× lower at baseline in the lines without MARCOL, SPINK13 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[LINC00589]] | C | SPINK13 activity raises LINC00589's level | lines that do not express SPINK13 (45) vs lines expressing it (5) | 4.56× lower at baseline in the lines without SPINK13 | 0.004 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target |
| [[DSG4]] | C | SPINK13 activity raises DSG4's level | lines that do not express SPINK13 (45) vs lines expressing it (5) | 3.30× lower at baseline in the lines without SPINK13 | 0.005 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target |
| [[LINC00457]] | C | [[MARCOL]], SPINK13 activity raises LINC00457's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 2.89× lower at baseline in the lines without MARCOL, SPINK13 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[TBXT]] | C | [[MARCOL]], SPINK13 activity raises TBXT's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 5.87× lower at baseline in the lines without MARCOL, SPINK13 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[PRICKLE1]] | C | [[MARCOL]], SPINK13 activity raises PRICKLE1's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 2.63× lower at baseline in the lines without MARCOL, SPINK13 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |
| [[P3H2-AS1]] | C | [[MARCOL]], SPINK13 activity raises P3H2-AS1's level | lines that do not express MARCOL, SPINK13 (45) vs lines expressing them (5) | 3.44× lower at baseline in the lines without MARCOL, SPINK13 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TBXT, ENSG00000230258, ENSG00000230975; co-absent with the target; co-absent genes |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.528). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.1, 37.4); signed map (44.4, 43.0). **Vector** length 21.6, 11.4% of its response variance represented; |z| ≥ 3 in 100 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.2 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.0 | +8.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.9 | +2.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.8 | +2.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.8 | +1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.7 | +2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.6 | +3.0 |
| fall | [[GSK1059615 (drug)]] 5 µM |  | -0.6 | -1.5 |
|  | [[Belinostat (drug)]] 5 µM |  | -0.6 | -2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -0.6 | -1.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | -0.5 | -1.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.5 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.4 | -1.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.4 | -2.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.4 | -2.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.4 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | serine peptidase inhibitor Kazal type 13 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:148,268,180-148,286,255 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SPINK5L3, LiESP6, HESPINTOR, MGC149260 |
| Gene groups (HGNC) | Serine peptidase inhibitors, Kazal type |
| Matched by | ensembl_id |

**Function**, from UniProt [Q1W4C9](https://www.uniprot.org/uniprotkb/Q1W4C9) (Serine protease inhibitor Kazal-type 13):

> May be a serine protease inhibitor (By similarity). Essential for sperm maturation and fertility. Inhibits sperm acrosome reaction, protecting sperm from premature reaction (By similarity).

**Summary**, from NCBI Gene [153218](https://www.ncbi.nlm.nih.gov/gene/153218):

> Predicted to enable serine-type endopeptidase inhibitor activity. Predicted to be involved in negative regulation of acrosome reaction. Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:27200](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:27200) · Entrez [153218](https://www.ncbi.nlm.nih.gov/gene/153218) · UniProt [Q1W4C9](https://www.uniprot.org/uniprotkb/Q1W4C9) · Ensembl [ENSG00000214510](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214510)

## Data

Gene col 13205: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13205); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13205, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13205]; `tensor/DDL_lfc|DDL_z.npy` [13205]; `embed/gene_vectors.npy` [13205]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13205 or target_col == 13205). Every well: [[SPINK13 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SPINK13.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
