---
symbol: "PGLS-DT"
type: "gene"
col: 15623
ensembl_id: "ENSG00000269439"
name: "PGLS divergent transcript"
location: "19p13.11"
module: 15
arm: "+"
pooled_cpm: 12.42
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 3
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# PGLS-DT

*PGLS divergent transcript* — 19p13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.45× (z +14.8, q 0e+00, up in 44 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.574× (z -6.7, q 1e-08, down in 30 of 48 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.654× (z -4.9, q 2e-04, down in 23 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A498 0.162×; ⚠ cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A-427 0.143×; ⚠ toxic); [[Selinexor (drug)]] 5 µM in 1 line (C-33 A 0.244×; ⚠ cell-cycle shift, explains ~29% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-172 0.193×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM267]] (+0.76, fdr 7e-06), [[NRSN2-AS1]] (+0.73, fdr 7e-06), [[ZNF529-AS1]] (+0.70, fdr 1e-05); moves opposite to [[POLR2E]] (-0.54, fdr 4e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC02609]] → it (grade B ⚠); 3 go from it, the strongest it → cells under [[Irinotecan (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15623.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.45×** | +14.8 | 0e+00 | 44/47 (SW480, LoVo, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +10.0 | 3e-21 | 36/45 (HEC-1-A, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +8.7 | 6e-16 | 30/40 (SW1417, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.35×** | +5.0 | 8e-05 | 22/48 (J82, RPMI-7951, …) | rises with dose | low cells (technical?) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.51×** | +4.9 | 1e-04 | 24/45 (LoVo, SW480, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +4.7 | 2e-04 | 23/45 (C32, LOX-IMVI, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.45×** | +4.5 | 6e-04 | 19/47 (HS-578T, SW480, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.29×** | +4.3 | 0.001 | 16/48 (hTERT-HPNE, LoVo, …) | two highest doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.42×** | +4.2 | 0.002 | 13/47 (NCI-H460, LS 180, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.27×** | +4.1 | 0.003 | 20/48 (SW480, SNU-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.40×** | +4.0 | 0.004 | 17/47 (HCT15, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.37×** | +3.6 | 0.015 | 16/43 (SW480, A498, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.22×** | +3.4 | 0.033 | 11/48 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.31×** | +3.2 | 0.058 | 8/44 (SNU-423, J82, …) | top dose only |  |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.43×** | +3.1 | 0.077 | 2/46 (PANC-1, SW1417) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.62×** | +3.0 | 0.077 | 7/45 (Panc 03.27, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.62×** | +3.0 | 0.077 | 9/42 (Panc 03.27, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.29×** | +3.0 | 0.077 | 6/46 (PANC-1, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15623.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A498 0.162×; ⚠ cell-cycle shift, explains ~0% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A-427 0.143×; ⚠ toxic); [[Selinexor (drug)]] 5 µM in 1 line (C-33 A 0.244×; ⚠ cell-cycle shift, explains ~29% of this change); [[Harringtonine (drug)]] 5 µM in 1 line (A-172 0.193×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.574×** | -6.7 | 1e-08 | 30/48 (HepG2/C3A, HS-578T, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.645×** | -5.3 | 4e-05 | 26/47 (SW480, HS-578T, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.654×** | -4.9 | 2e-04 | 23/47 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.892× | -4.9 | 2e-04 | 7/48 (SW 1271, NCI-H1573, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.717×** | -4.0 | 0.007 | 20/48 (HS-578T, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.758×** | -3.3 | 0.082 | 13/47 (KATO III, NCI-H23, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | 0.774× | -3.1 | 0.16 | 14/43 (Panc 03.27, AsPC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.777× | -3.0 | 0.17 | 8/48 (NCI-H460, LoVo, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15623. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 11.0 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.193× (z -8.8) |
| [[A-427 (line)]] | wt | 10.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.143× (z -9.5) ⚠ toxic |
| [[A498 (line)]] | wt | 12.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.162× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.244× (z -9.4) ⚠ cell-cycle shift, explains ~29% of this change |
| [[LoVo (line)]] | wt | 14.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.70× (z +12.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 15.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.19× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 9.16 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.12× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 14.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.70× (z +8.7) | — |
| [[SK-MEL-2 (line)]] | alt | 17.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.55× (z +8.6) | — |
| [[SW480 (line)]] | alt | 15.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.97× (z +13.3) | — |
| [[A549 (line)]] | wt | 7.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.92 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.58 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 21.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 14.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.82 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.72 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.51 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.33 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15623), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM267]] | +0.76 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[NRSN2-AS1]] | +0.73 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[ZNF529-AS1]] | +0.70 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[CCNY-AS1]] | +0.70 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[NBR2]] | +0.66 | +0.56 / +0.66 | both halves | 1e-05 |  |
| [[ZNF460-AS1]] | +0.66 | +0.42 / +0.72 | both halves | 4e-05 |  |
| [[ZBTB8OS]] | +0.66 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[ZCCHC8]] | +0.65 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[CNPY2-AS1]] | +0.64 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[CAPN10-DT]] | +0.64 | +0.31 / +0.72 | both halves | 2e-04 | same gene group |
| [[ZKSCAN2-DT]] | +0.64 | +0.46 / +0.67 | both halves | 2e-05 | same gene group |
| [[DMGDH]] | +0.63 | +0.62 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2E]] | -0.54 | -0.41 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02609]] | B | LINC02609 activity raises PGLS-DT's level | lines that do not express LINC02609 (6) vs lines expressing it (44) | 1.43× lower at baseline in the lines without LINC02609 | 0.028 | ⚠ within organs, on part of the lines; also absent: TPST1, HLTF, FERMT2; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises PGLS-DT's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| KDR | B | KDR activity lowers PGLS-DT's level | compounds that target KDR: 4 of 8 raise it (Cabozantinib, Ponatinib, Sunitinib, c-Kit-IN-1) | 50% of the class's compounds vs 4.5% of all compounds | 0.077 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ASNSP1]] | B | ASNSP1 activity raises PGLS-DT's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.28× lower at baseline in the lines without ASNSP1 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Irinotecan (drug)]] 0.5 µM | C | PGLS-DT's natural level raises the cells' numbers under Irinotecan 0.5 µM (protects the cells) | PGLS-DT's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.69 | 0.285 over the table, 0.029 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Aliskiren (drug)]] 0.5 µM | C | PGLS-DT's natural level raises the cells' numbers under Aliskiren 0.5 µM (protects the cells) | PGLS-DT's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.68 | 0.285 over the table, 0.085 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |
| cells under [[Belzutifan (drug)]] 5 µM | C | PGLS-DT's natural level lowers the cells' numbers under Belzutifan 5 µM (makes them more sensitive) | PGLS-DT's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66 | 0.360 over the table, 0.036 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.674). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-8.9, 24.5); signed map (2.0, -0.1). **Vector** length 94.8, 20.6% of its response variance represented; |z| ≥ 3 in 769 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +11.1 | +14.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.3 | +8.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +10.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.4 | +4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.4 | +4.0 |
|  | [[Neratinib (drug)]] 5 µM |  | +3.5 | +4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.0 | +3.4 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.8 | -4.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -3.1 | -4.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -3.0 | -6.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | -2.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.7 | -5.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.1 | -3.0 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.0 | -2.0 |
|  | [[Methotrexate (drug)]] 5 µM |  | -1.9 | -2.2 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | -1.8 | -1.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.7 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | PGLS divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 19p13.11 — chr19:17,488,990-17,511,889 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55274](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55274) · Entrez [100507551](https://www.ncbi.nlm.nih.gov/gene/100507551) · Ensembl [ENSG00000269439](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000269439)

## Data

Gene col 15623: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15623); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15623, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15623]; `tensor/DDL_lfc|DDL_z.npy` [15623]; `embed/gene_vectors.npy` [15623]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15623 or target_col == 15623). Every well: [[PGLS-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PGLS-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
