---
symbol: "FAT4"
type: "gene"
col: 12144
ensembl_id: "ENSG00000196159"
name: "FAT atypical cadherin 4"
location: "4q28.1"
module: 121
arm: "+"
pooled_cpm: 27.89
n_lines_expressing: 30
n_dd_up: 3
n_dd_down: 23
n_dd_up_clean: 3
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 13
direction_downstream: 18
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# FAT4

*FAT atypical cadherin 4* — 4q28.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.68× (z +5.1, q 2e-04, up in 13 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.526× (z -6.2, q 2e-07, down in 21 of 27 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAH11]] (+0.66, fdr 7e-06), [[ZFHX4]] (+0.65, fdr 7e-06), [[SLITRK5]] (+0.64, fdr 7e-06); moves opposite to [[CCL3]] (-0.39, fdr 9e-05), [[TMPRSS5]] (-0.39, fdr 6e-05).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[RNF217]] → it (grade B ⚠); 18 go from it, the strongest it → [[RNF217]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12144.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.68×** | +5.1 | 2e-04 | 13/28 (SW 900, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.68×** | +4.9 | 3e-04 | 18/27 (C32, LOX-IMVI, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.9 | 0.016 | 14/28 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.26× | +3.2 | 0.16 | 10/28 (HS-578T, H4, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.38× | +3.2 | 0.16 | 12/27 (C32, LOX-IMVI, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | 1.38× | +3.1 | 0.16 | 12/27 (A549, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 1.36× | +3.0 | 0.19 | 6/28 (SNU-423, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12144.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.526×** | -6.2 | 2e-07 | 21/27 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.545×** | -5.9 | 1e-06 | 20/28 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.538×** | -5.8 | 1e-06 | 17/26 (LOX-IMVI, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.553×** | -5.4 | 7e-06 | 18/28 (AN3 CA, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.586×** | -5.0 | 7e-05 | 19/27 (NCI-H2030, J82, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.587×** | -4.8 | 2e-04 | 15/25 (Panc 03.27, hTERT-HPNE, …) | all doses, flat | composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.606×** | -4.7 | 2e-04 | 19/27 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.620×** | -4.6 | 2e-04 | 17/28 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.628×** | -4.5 | 4e-04 | 15/26 (PANC-1, NCI-H460, …) | all doses, flat | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.633×** | -4.4 | 5e-04 | 18/28 (LOX-IMVI, HOP62, …) | rises with dose | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.443×** | -4.1 | 0.002 | 16/28 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.650×** | -4.0 | 0.003 | 14/28 (NCI-H23, NCI-H460, …) | rises with dose | composition shift |
| [[EX229 (drug)]] 5 µM |  | **0.457×** | -4.0 | 0.003 | 15/27 (PANC-1, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.461×** | -3.9 | 0.003 | 14/27 (NCI-H460, NCI-H1792, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **0.691×** | -3.6 | 0.013 | 15/27 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.607×** | -3.5 | 0.019 | 16/28 (NCI-H460, PANC-1, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.718×** | -3.1 | 0.062 | 12/28 (Hs 766T, SW 1271, …) | rises with dose |  |
| [[EX229 (drug)]] 0.5 µM |  | **0.641×** | -3.1 | 0.062 | 11/28 (A498, PANC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.736×** | -3.0 | 0.080 | 14/27 (LOX-IMVI, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.654×** | -2.9 | 0.080 | 10/28 (SNU-423, A498, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.654×** | -2.9 | 0.080 | 10/26 (PANC-1, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.21 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12144. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 52.3 | 0 | 9 (6 ⚠) | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.183× (z -13.0) |
| [[LOX-IMVI (line)]] | wt | 105 | 0 | 6 (5 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.152× (z -10.9) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.242× (z -8.5) |
| [[HOP62 (line)]] | alt | 70.8 | 0 | 5 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.224× (z -9.7) ⚠ cell-cycle shift, explains ~31% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.285× (z -8.5) |
| [[NCI-H2030 (line)]] | alt | 123 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.291× (z -12.2) ⚠ cell-cycle shift, would explain all of this change |
| [[PANC-1 (line)]] | alt | 73.8 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[NCI-H23 (line)]] | alt | 37.3 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.130× (z -10.8) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 97.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +9.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[AN3 CA (line)]] | alt | 34.9 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0589× (z -9.7) |
| [[C32 (line)]] | wt | 8.52 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.42× (z +10.2) ⚠ cell-cycle shift, would explain all of this change | — |
| [[H4 (line)]] | wt | 38.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~65% of this change |
| [[hTERT-HPNE (line)]] | wt | 30.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.124× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[J82 (line)]] | alt | 27.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[Panc 03.27 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.141× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 92.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.15 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 9.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.01 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.59 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.28 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.70 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.92 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.44 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.31 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.51 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12144), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAH11]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[ZFHX4]] | +0.65 | +0.62 / +0.58 | both halves | 7e-06 | STRING 572 |
| [[SLITRK5]] | +0.64 | +0.62 / +0.58 | both halves | 7e-06 | STRING 427 |
| [[BDNF]] | +0.63 | +0.62 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[NEGR1]] | +0.56 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[ODAD2]] | +0.55 | +0.46 / +0.47 | both halves | 3e-05 | **novel candidate** |
| [[NALCN]] | +0.54 | +0.40 / +0.49 | both halves | 5e-05 |  |
| [[BASP1-AS1]] | +0.52 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[FLRT2]] | +0.52 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[PRR16]] | +0.52 | +0.46 / +0.54 | both halves | 3e-05 |  |
| [[ADGRG6]] | +0.52 | +0.40 / +0.46 | both halves | 5e-05 |  |
| [[RBMS3]] | +0.51 | +0.45 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCL3]] | -0.39 | -0.39 / -0.36 | both halves | 9e-05 |  |
| [[TMPRSS5]] | -0.39 | -0.38 / -0.40 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 1, C 12. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF217]] | B | RNF217 activity raises FAT4's level | lines that do not express RNF217 (9) vs lines expressing it (41) | 3.54× lower at baseline in the lines without RNF217 | 0.098 | ⚠ within organs, on part of the lines; also absent: RNF217-AS1, LRP12, BEX3 |
| [[DPY19L2]] | C | DPY19L2 activity raises FAT4's level | lines that do not express DPY19L2 (22) vs lines expressing it (28) | 5.83× lower at baseline in the lines without DPY19L2 | 0.003 | ⚠ within organs, on part of the lines; also absent: BVES, SLC8A1, MPDZ; co-absent with the target |
| [[CACNA2D1]] | C | CACNA2D1 activity raises FAT4's level | lines that do not express CACNA2D1 (20) vs lines expressing it (30) | 5.36× lower at baseline in the lines without CACNA2D1 | 0.025 | ⚠ within organs, on part of the lines; also absent: ZNF229, BVES-AS1, CCDC169; co-absent with the target |
| [[MSRB3]] | C | MSRB3 activity raises FAT4's level | lines that do not express MSRB3 (20) vs lines expressing it (30) | 4.17× lower at baseline in the lines without MSRB3 | 0.027 | ⚠ within organs, on part of the lines; also absent: ARHGEF6, KCNG1, FHL1; co-absent with the target |
| [[NEGR1]] | C | NEGR1 activity raises FAT4's level | lines that do not express NEGR1 (24) vs lines expressing it (26) | 4.44× lower at baseline in the lines without NEGR1 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000286863, ENSG00000232949, CACNA2D1; co-absent with the target |
| [[ODAD2]] | C | ODAD2 activity raises FAT4's level | lines that do not express ODAD2 (27) vs lines expressing it (23) | 3.12× lower at baseline in the lines without ODAD2 | 0.055 | ⚠ within organs, on part of the lines; also absent: FBN2, NDNF, EPHA5; co-absent with the target |
| [[PDGFC]] | C | PDGFC activity raises FAT4's level | lines that do not express PDGFC (13) vs lines expressing it (37) | 5.24× lower at baseline in the lines without PDGFC | 0.060 | ⚠ within organs, on part of the lines; also absent: OSMR-DT, GLRB, DNAH11; co-absent with the target |
| [[BNC2]] | C | BNC2 activity raises FAT4's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 3.98× lower at baseline in the lines without BNC2 | 0.061 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182; co-absent with the target |
| [[GPR176]] | C | GPR176 activity raises FAT4's level | lines that do not express GPR176 (18) vs lines expressing it (32) | 5.94× lower at baseline in the lines without GPR176 | 0.066 | ⚠ within organs, on part of the lines; also absent: RFTN1, ARMCX1, AFAP1L1; co-absent with the target |
| [[DPY19L2P1]] | C | DPY19L2P1 activity raises FAT4's level | lines that do not express DPY19L2P1 (26) vs lines expressing it (24) | 4.91× lower at baseline in the lines without DPY19L2P1 | 0.066 | ⚠ within organs, on part of the lines; also absent: STAC, RNF180, SRGN; co-absent with the target |
| [[FBN2]] | C | FBN2 activity raises FAT4's level | lines that do not express FBN2 (31) vs lines expressing it (19) | 3.95× lower at baseline in the lines without FBN2 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZEB2, ENSG00000289884, ABI3BP; maybe low, not absent; co-absent with the target |
| [[PCDH7]] | C | PCDH7 activity raises FAT4's level | lines that do not express PCDH7 (18) vs lines expressing it (32) | 3.86× lower at baseline in the lines without PCDH7 | 0.081 | ⚠ within organs, on part of the lines; also absent: ADGRL4, KCNQ5, ST8SIA4; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 4, C 14. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF217]] | B | FAT4 activity raises RNF217's level | lines that do not express FAT4 (20) vs lines expressing it (30) | 2.82× lower at baseline in the lines without FAT4 | 0.018 | ⚠ within organs, on part of the lines; also absent: RFTN1, GPR176, GNG11 |
| [[NR2F2]] | B | FAT4 activity raises NR2F2's level | lines that do not express FAT4 (20) vs lines expressing it (30) | 1.61× lower at baseline in the lines without FAT4 | 0.065 | ⚠ within organs, on part of the lines; also absent: RFTN1, GPR176, GNG11 |
| [[CRIM1]] | B | FAT4 activity raises CRIM1's level | lines that do not express FAT4 (20) vs lines expressing it (30) | 1.71× lower at baseline in the lines without FAT4 | 0.073 | ⚠ within organs, on part of the lines; also absent: RFTN1, GPR176, GNG11 |
| cells under [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | B | FAT4 activity lowers the cells' numbers under Mitoxantrone (dihydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express FAT4 (20) vs lines expressing it (28) | the lines without FAT4: 1.21× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: RFTN1, GPR176, GNG11 |
| [[RBMS3]] | C | FAT4 activity raises RBMS3's level | lines that do not express FAT4 (20) vs lines expressing it (30) | 6.77× lower at baseline in the lines without FAT4 | 0.010 | ⚠ within organs, on part of the lines; also absent: RFTN1, GPR176, GNG11; co-absent with the target |
| [[MSRB3]] | C | FAT4 activity raises MSRB3's level | lines that do not express FAT4 (20) vs lines expressing it (30) | 4.00× lower at baseline in the lines without FAT4 | 0.020 | ⚠ within organs, on part of the lines; also absent: RFTN1, GPR176, GNG11; co-absent with the target |
| [[EFEMP1]] | C | FAT4 activity raises EFEMP1's level | lines that do not express FAT4 (20) vs lines expressing it (30) | 4.39× lower at baseline in the lines without FAT4 | 0.020 | ⚠ within organs, on part of the lines; also absent: RFTN1, GPR176, GNG11; co-absent with the target |
| [[GPR176]] | C | FAT4 activity raises GPR176's level | lines that do not express FAT4 (20) vs lines expressing it (30) | 6.31× lower at baseline in the lines without FAT4 | 0.021 | ⚠ within organs, on part of the lines; also absent: RFTN1, GPR176, GNG11; co-absent with the target |
| [[DPY19L2]] | C | FAT4 activity raises DPY19L2's level | lines that do not express FAT4 (20) vs lines expressing it (30) | 3.02× lower at baseline in the lines without FAT4 | 0.031 | ⚠ within organs, on part of the lines; also absent: RFTN1, GPR176, GNG11; co-absent with the target |
| [[PCDH7]] | C | FAT4 activity raises PCDH7's level | lines that do not express FAT4 (20) vs lines expressing it (30) | 4.55× lower at baseline in the lines without FAT4 | 0.054 | ⚠ within organs, on part of the lines; also absent: RFTN1, GPR176, GNG11; co-absent with the target |
| [[COL4A5]] | C | FAT4 activity raises COL4A5's level | lines that do not express FAT4 (20) vs lines expressing it (30) | 5.35× lower at baseline in the lines without FAT4 | 0.062 | ⚠ within organs, on part of the lines; also absent: RFTN1, GPR176, GNG11; co-absent with the target |
| [[BDNF]] | C | FAT4 activity raises BDNF's level | lines that do not express FAT4 (20) vs lines expressing it (30) | 4.03× lower at baseline in the lines without FAT4 | 0.065 | ⚠ within organs, on part of the lines; also absent: RFTN1, GPR176, GNG11; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.548). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.9, 31.7); signed map (39.3, 37.7). **Vector** length 82.2, 23.1% of its response variance represented; |z| ≥ 3 in 809 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.7 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +3.2 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +1.9 | +3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.8 | +1.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +2.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.5 | +0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | +2.9 |
|  | [[Busulfan (drug)]] 5 µM |  | +1.3 | +1.8 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -3.9 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.3 | -6.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.9 | -1.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.5 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -4.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | +0.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.9 | -2.8 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | FAT atypical cadherin 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q28.1 — chr4:125,314,918-125,492,932 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CDHF14, FAT-J, CDHR11 |
| Gene groups (HGNC) | Cadherin related |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6V0I7](https://www.uniprot.org/uniprotkb/Q6V0I7) (Protocadherin Fat 4):

> Cadherins are calcium-dependent cell adhesion proteins. FAT4 plays a role in the maintenance of planar cell polarity as well as in inhibition of YAP1-mediated neuroprogenitor cell proliferation and differentiation (By similarity).

**Summary**, from NCBI Gene [79633](https://www.ncbi.nlm.nih.gov/gene/79633):

> The protein encoded by this gene is a member of the protocadherin family. This gene may play a role in regulating planar cell polarity (PCP). Studies in mice suggest that loss of PCP signaling may cause cystic kidney disease, and mutations in this gene have been associated with Van Maldergem Syndrome 2. Alternatively spliced transcript variants have been noted for this gene. [provided by RefSeq, Mar 2014]

**Accessions** — [HGNC:23109](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23109) · Entrez [79633](https://www.ncbi.nlm.nih.gov/gene/79633) · UniProt [Q6V0I7](https://www.uniprot.org/uniprotkb/Q6V0I7) · Ensembl [ENSG00000196159](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196159)

## Data

Gene col 12144: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12144); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12144, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12144]; `tensor/DDL_lfc|DDL_z.npy` [12144]; `embed/gene_vectors.npy` [12144]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12144 or target_col == 12144). Every well: [[FAT4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAT4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
