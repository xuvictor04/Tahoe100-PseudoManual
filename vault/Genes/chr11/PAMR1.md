---
symbol: "PAMR1"
type: "gene"
col: 7339
ensembl_id: "ENSG00000149090"
name: "peptidase domain containing associated with muscle regeneration 1"
location: "11p13"
module: 166
arm: "+"
pooled_cpm: 2.66
n_lines_expressing: 22
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 10
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 11
tags: ["gene", "module/166"]
generated_by: "tahoemap"
---

# PAMR1

*peptidase domain containing associated with muscle regeneration 1* — 11p13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.97× (z +21.5, q 0e+00, up in 10 of 12 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (hTERT-HPNE 0.165×; ⚠ cell-cycle shift, explains ~60% of this change).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IPO9-AS1]] (+0.69, fdr 1e-05), [[SLCO1C1]] (+0.66, fdr 3e-05), [[COL23A1]] (+0.66, fdr 7e-06); moves opposite to [[DTNB]] (-0.48, fdr 2e-04).
> It is in [[Module 166]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 11 go from it, the strongest it → [[STARD13-AS]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7339.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.97×** | +21.5 | 0e+00 | 10/12 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.99×** | +11.9 | 2e-30 | 1/2 (SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.11×** | +11.3 | 2e-27 | 3/5 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.76×** | +8.5 | 3e-15 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **3.09×** | +7.5 | 5e-12 | 7/11 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.88×** | +7.1 | 2e-10 | 4/9 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.58×** | +6.6 | 4e-09 | 5/13 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.86×** | +6.1 | 7e-08 | 4/13 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +5.2 | 1e-05 | 6/16 (HOP62, SNU-423, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.64×** | +4.9 | 6e-05 | 4/16 (A-172, J82, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +4.0 | 0.003 | 1/6 (SNU-423) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.69×** | +3.7 | 0.012 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.71×** | +3.6 | 0.015 | 1/5 (SNU-423) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.04×** | +3.5 | 0.016 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.51×** | +3.3 | 0.031 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Vandetanib (drug)]] 0.5 µM |  | **1.55×** | +3.1 | 0.077 | 0/10 | inconsistent across doses |  |
| [[Trifluridine (drug)]] 5 µM |  | **1.36×** | +3.0 | 0.081 | 1/12 (SW480) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.55×** | +3.0 | 0.099 | 0/6 | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7339.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 1 line (hTERT-HPNE 0.165×; ⚠ cell-cycle shift, explains ~60% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | 0.634× | -3.1 | 0.52 | 2/16 (NCI-H2030, PANC-1) | inconsistent across doses |  |
| [[Ferulic acid (drug)]] 5 µM |  | 0.624× | -3.1 | 0.52 | 3/11 (HOP62, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7339. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 136 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.165× (z -10.5) ⚠ cell-cycle shift, explains ~60% of this change |
| [[PANC-1 (line)]] | alt | 0.831 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +8.9) | — |
| [[A-172 (line)]] | wt | 8.42 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.343 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.552 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.654 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.952 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.509 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.617 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.884 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.466 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.487 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.32 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.566 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.552 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.552 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.994 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.405 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.39 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.417 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.408 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.735 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.532 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.948 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.618 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.27 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.780 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.409 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.633 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.540 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.555 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.668 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.448 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.607 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.694 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7339), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 6 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IPO9-AS1]] | +0.69 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[SLCO1C1]] | +0.66 | +0.69 / +0.46 | both halves | 3e-05 |  |
| [[COL23A1]] | +0.66 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[LINC01500]] | +0.64 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[CFAP20DC-DT]] | +0.64 | +0.60 / +0.58 | both halves | 8e-06 |  |
| [[SLC8A1-AS1]] | +0.62 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[SOCS2-AS1]] | +0.61 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[SLC14A2]] | +0.58 | +0.52 / +0.58 | both halves | 1e-05 |  |
| [[C2orf92]] | +0.57 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[ANO3]] | +0.57 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[TEK]] | +0.57 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[C12orf40]] | +0.56 | +0.38 / +0.50 | both halves | 6e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DTNB]] | -0.48 | -0.35 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 1, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PAMR1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[DIRAS3]] | C | DIRAS3 activity raises PAMR1's level | lines that do not express DIRAS3 (44) vs lines expressing it (6) | 6.06× lower at baseline in the lines without DIRAS3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000230258, MTND1P23, APOB; co-absent with the target |
| [[PDGFRB]] | C | PDGFRB activity raises PAMR1's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 2.78× lower at baseline in the lines without PDGFRB | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[PRRX1]] | C | PRRX1 activity raises PAMR1's level | lines that do not express PRRX1 (34) vs lines expressing it (16) | 1.96× lower at baseline in the lines without PRRX1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, LINC00383, DCN; co-absent with the target |
| [[COL15A1]] | C | COL15A1 activity raises PAMR1's level | lines that do not express COL15A1 (28) vs lines expressing it (22) | 1.94× lower at baseline in the lines without COL15A1 | 0.024 | ⚠ within organs, on part of the lines; also absent: LINC01583, PHACTR1, GYPC; co-absent with the target |
| [[ADAMTS2]] | C | ADAMTS2 activity raises PAMR1's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 1.94× lower at baseline in the lines without ADAMTS2 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1; co-absent with the target |
| [[PDE3A]] | C | PDE3A activity raises PAMR1's level | lines that do not express PDE3A (34) vs lines expressing it (16) | 1.85× lower at baseline in the lines without PDE3A | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PGR, SNTG1, COL19A1; co-absent with the target |
| [[BAALC]] | C | BAALC activity raises PAMR1's level | lines that do not express BAALC (32) vs lines expressing it (18) | 2.10× lower at baseline in the lines without BAALC | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent; co-absent with the target |
| [[SEMA5A]] | C | SEMA5A activity raises PAMR1's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 1.87× lower at baseline in the lines without SEMA5A | 0.092 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STARD13-AS]] | B | PAMR1 activity raises STARD13-AS's level | lines that do not express PAMR1 (28) vs lines expressing it (22) | 1.26× lower at baseline in the lines without PAMR1 | 0.019 | ⚠ within organs, on part of the lines; also absent: MARCHF4, FLRT2, ESM1; maybe low, not absent |
| [[RETREG1-AS1]] | B | PAMR1 activity raises RETREG1-AS1's level | lines that do not express PAMR1 (28) vs lines expressing it (22) | 1.15× lower at baseline in the lines without PAMR1 | 0.037 | ⚠ within organs, on part of the lines; also absent: MARCHF4, FLRT2, ESM1; maybe low, not absent |
| [[ST7-AS2]] | B | PAMR1 activity raises ST7-AS2's level | lines that do not express PAMR1 (28) vs lines expressing it (22) | 1.13× lower at baseline in the lines without PAMR1 | 0.050 | ⚠ within organs, on part of the lines; also absent: MARCHF4, FLRT2, ESM1; maybe low, not absent |
| [[SYT16]] | B | PAMR1 activity raises SYT16's level | lines that do not express PAMR1 (28) vs lines expressing it (22) | 1.64× lower at baseline in the lines without PAMR1 | 0.062 | ⚠ within organs, on part of the lines; also absent: MARCHF4, FLRT2, ESM1; maybe low, not absent |
| [[LRRC8C-DT]] | B | PAMR1 activity strengthens LRRC8C-DT's drug response | lines that do not express PAMR1 (28) vs lines expressing it (18) | the lines without PAMR1 respond 0.67× as strongly (z diff +0.62); strongest at Idarubicin (hydrochloride) 5 µM: 2.71x vs 4.46x (z diff +2.4) | 0.069 | ⚠ within organs, on part of the lines; also absent: MARCHF4, FLRT2, ESM1; maybe low, not absent; target measured in part of the lines; artifact flags |
| cells under [[Imiquimod (hydrochloride) (drug)]] 5 µM | B | PAMR1 activity lowers the cells' numbers under Imiquimod (hydrochloride) 5 µM (makes them more sensitive) | lines that do not express PAMR1 (28) vs lines expressing it (20) | the lines without PAMR1: 1.14× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; also absent: MARCHF4, FLRT2, ESM1; maybe low, not absent |
| [[SOCS2-AS1]] | B | PAMR1 activity raises SOCS2-AS1's level | lines that do not express PAMR1 (28) vs lines expressing it (22) | 1.92× lower at baseline in the lines without PAMR1 | 0.079 | ⚠ within organs, on part of the lines; also absent: MARCHF4, FLRT2, ESM1; maybe low, not absent |
| [[PRSS23]] | B | PAMR1 activity raises PRSS23's level | lines that do not express PAMR1 (28) vs lines expressing it (22) | 2.35× lower at baseline in the lines without PAMR1 | 0.090 | ⚠ within organs, on part of the lines; also absent: MARCHF4, FLRT2, ESM1; maybe low, not absent |
| [[DCC]] | B | PAMR1 activity raises DCC's level | lines that do not express PAMR1 (28) vs lines expressing it (22) | 1.59× lower at baseline in the lines without PAMR1 | 0.095 | ⚠ within organs, on part of the lines; also absent: MARCHF4, FLRT2, ESM1; maybe low, not absent |
| [[SEMA5A]] | C | PAMR1 activity raises SEMA5A's level | lines that do not express PAMR1 (28) vs lines expressing it (22) | 3.56× lower at baseline in the lines without PAMR1 | 0.035 | ⚠ within organs, on part of the lines; also absent: MARCHF4, FLRT2, ESM1; maybe low, not absent; co-absent with the target |
| [[TBX2]] | C | PAMR1 activity raises TBX2's level | lines that do not express PAMR1 (28) vs lines expressing it (22) | 2.85× lower at baseline in the lines without PAMR1 | 0.075 | ⚠ within organs, on part of the lines; also absent: MARCHF4, FLRT2, ESM1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 166]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.603). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (23.6, 25.7); signed map (29.2, 15.9). **Vector** length 24.7, 4.49% of its response variance represented; |z| ≥ 3 in 344 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +21.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.6 | +11.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +8.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +5.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +4.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.9 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +2.9 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +0.7 | +0.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.9 | -2.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -3.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.8 | -1.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.7 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -2.5 |
|  | [[Fenofibrate (drug)]] 0.05 µM |  | -0.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | peptidase domain containing associated with muscle regeneration 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p13 — chr11:35,431,823-35,530,300 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RAMP, DKFZP586H2123 |
| Gene groups (HGNC) | Sushi domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UXH9](https://www.uniprot.org/uniprotkb/Q6UXH9) (Inactive serine protease PAMR1):

> May play a role in regeneration of skeletal muscle.

**Summary**, from NCBI Gene [25891](https://www.ncbi.nlm.nih.gov/gene/25891):

> Predicted to enable calcium ion binding activity and serine-type endopeptidase activity. Predicted to be involved in proteolysis. Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24554](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24554) · Entrez [25891](https://www.ncbi.nlm.nih.gov/gene/25891) · UniProt [Q6UXH9](https://www.uniprot.org/uniprotkb/Q6UXH9) · Ensembl [ENSG00000149090](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149090)

## Data

Gene col 7339: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7339); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7339, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7339]; `tensor/DDL_lfc|DDL_z.npy` [7339]; `embed/gene_vectors.npy` [7339]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7339 or target_col == 7339). Every well: [[PAMR1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PAMR1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
