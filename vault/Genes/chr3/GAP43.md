---
symbol: "GAP43"
type: "gene"
col: 10200
ensembl_id: "ENSG00000172020"
name: "growth associated protein 43"
location: "3q13.31"
module: 9
arm: "+"
pooled_cpm: 4.38
n_lines_expressing: 28
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 13
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# GAP43

*growth associated protein 43* — 3q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.15× (z +12.1, q 6e-31, up in 5 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.46× (z +10.8, q 7e-25, up in 17 of 23 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SHP-77 0.278×, C-33 A 0.229×, NCI-H460 0.344×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SHP-77 0.216×, NCI-H460 0.213×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (C-33 A 0.105×, RKO 0.118×); [[Belinostat (drug)]] 5 µM in 1 line (RKO 0.123×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RIMS1]] (+0.64, fdr 3e-05), [[NCAM1]] (+0.59, fdr 9e-05), [[PKIA]] (+0.58, fdr 2e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ARL14]] → it (grade B ⚠); 13 go from it, the strongest it → [[SYN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10200.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.15×** | +12.1 | 6e-31 | 5/9 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.99×** | +11.3 | 3e-27 | 2/4 (NCI-H460, NCI-H661) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.46×** | +10.8 | 7e-25 | 17/23 (SW480, A-172, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.40×** | +10.5 | 1e-23 | 4/17 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.29×** | +9.4 | 1e-18 | 3/6 (NCI-H460, NCI-H661, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.55×** | +7.9 | 2e-13 | 12/19 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.10×** | +6.3 | 3e-08 | 2/9 (NCI-H661, A-172) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.76×** | +4.8 | 1e-04 | 1/15 (NCI-H460) | two highest doses | cell-cycle shift (explains ~1% here); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **1.81×** | +3.6 | 0.021 | 2/12 (NCI-H460, NCI-H661) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.19×** | +3.5 | 0.030 | 1/4 (NCI-H1792) | top dose only | noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.71×** | +3.2 | 0.061 | 1/7 (RKO) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Fulvestrant (drug)]] 0.5 µM |  | **1.47×** | +3.2 | 0.061 | 1/19 (SW480) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.06×** | +3.2 | 0.061 | 0/8 | rises with dose | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.45×** | +3.1 | 0.075 | 1/14 (NCI-H460) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10200.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (SHP-77 0.278×, C-33 A 0.229×, NCI-H460 0.344×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (SHP-77 0.216×, NCI-H460 0.213×; ⚠ cell-cycle shift, would explain all of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (C-33 A 0.105×, RKO 0.118×); [[Belinostat (drug)]] 5 µM in 1 line (RKO 0.123×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Neratinib (drug)]] 0.5 µM |  | 0.700× | -3.1 | 0.48 | 3/23 (NCI-H1573, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 5 µM |  | 0.706× | -3.0 | 0.48 | 6/24 (NCI-H1792, RPMI-7951, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | 0.706× | -3.0 | 0.48 | 6/21 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10200. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 15.9 | 2 | 3 (2 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.96× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -13.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -9.0) |
| [[C-33 A (line)]] | alt | 43.2 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.105× (z -11.0) |
| [[RKO (line)]] | wt | 16.4 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.118× (z -9.7) |
| [[SW480 (line)]] | alt | 5.72 | 3 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 4.87× (z +12.2) | — |
| [[SHP-77 (line)]] | alt | 61.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -13.5) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.278× (z -11.3) |
| [[A-172 (line)]] | wt | 6.03 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.34× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 1.75 | 0 | 1 | — | [[Dexamethasone (drug)]] 0.5 µM 0.0533× (z -8.7) |
| [[NCI-H1792 (line)]] | alt | 13.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.116× (z -9.3) ⚠ toxic |
| [[A-427 (line)]] | wt | 0.634 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.682 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.718 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.47 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.789 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.652 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.844 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.68 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.797 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.748 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.713 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.864 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.81 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.668 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.29 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.684 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.617 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.672 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.638 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 78.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.697 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.637 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.822 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.800 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.999 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10200), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RIMS1]] | +0.64 | +0.45 / +0.68 | both halves | 3e-05 | **novel candidate** |
| [[NCAM1]] | +0.59 | +0.37 / +0.54 | both halves | 9e-05 | pathway: L1CAM interactions; STRING 831 |
| [[PKIA]] | +0.58 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[ZMAT4]] | +0.57 | +0.38 / +0.57 | both halves | 6e-05 |  |
| [[ASXL3]] | +0.56 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[ANOS1]] | +0.56 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[RGS4]] | +0.56 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[CREB5]] | +0.55 | +0.39 / +0.61 | both halves | 5e-05 |  |
| [[AFF2]] | +0.54 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[F2RL2]] | +0.54 | +0.36 / +0.47 | both halves | 9e-05 |  |
| [[PAK3]] | +0.54 | +0.57 / +0.46 | both halves | 2e-05 |  |
| [[LINC01885]] | +0.53 | +0.36 / +0.53 | both halves | 9e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 1, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARL14]] | B | ARL14 activity lowers GAP43's level | lines that do not express ARL14 (23) vs lines expressing it (27) | 2.01× higher at baseline in the lines without ARL14 | 0.009 | ⚠ within organs, on part of the lines; also absent: TMEM92, LIPH, AFAP1L2; maybe low, not absent |
| [[LINC01885]] | C | LINC01885 activity raises GAP43's level | lines that do not express LINC01885 (34) vs lines expressing it (16) | 3.47× lower at baseline in the lines without LINC01885 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287598, ZNF208, LINC00383; co-absent with the target |
| [[PTN]] | C | PTN activity raises GAP43's level | lines that do not express PTN (28) vs lines expressing it (22) | 1.47× lower at baseline in the lines without PTN | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, SPARC, BAALC; co-absent with the target |
| [[RGS4]] | C | RGS4 activity raises GAP43's level | lines that do not express RGS4 (35) vs lines expressing it (15) | 2.16× lower at baseline in the lines without RGS4 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286853, CCDC190, ENSG00000243486; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 7, C 6. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYN1]] | B | GAP43 activity raises SYN1's level | lines that do not express GAP43 (22) vs lines expressing it (28) | 1.53× lower at baseline in the lines without GAP43 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000287622, ENSG00000242880, ENSG00000286540; maybe low, not absent |
| [[SEMA6D]] | B | GAP43 activity raises SEMA6D's level | lines that do not express GAP43 (22) vs lines expressing it (28) | 2.18× lower at baseline in the lines without GAP43 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000287622, ENSG00000242880, ENSG00000286540; maybe low, not absent |
| [[MIAT]] | B | GAP43 activity raises MIAT's level | lines that do not express GAP43 (22) vs lines expressing it (28) | 1.88× lower at baseline in the lines without GAP43 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000287622, ENSG00000242880, ENSG00000286540; maybe low, not absent |
| cells under [[Docetaxel (Trihydrate) (drug)]] 5 µM | B | GAP43 activity lowers the cells' numbers under Docetaxel (Trihydrate) 5 µM (makes them more sensitive) | lines that do not express GAP43 (22) vs lines expressing it (26) | the lines without GAP43: 1.21× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000287622, ENSG00000242880, ENSG00000286540; maybe low, not absent |
| cells under [[Tucidinostat (drug)]] 5 µM | B | GAP43 activity lowers the cells' numbers under Tucidinostat 5 µM (makes them more sensitive) | lines that do not express GAP43 (22) vs lines expressing it (26) | the lines without GAP43: 1.11× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000287622, ENSG00000242880, ENSG00000286540; maybe low, not absent |
| [[INHBA]] | B | GAP43 activity raises INHBA's level | lines that do not express GAP43 (22) vs lines expressing it (28) | 2.51× lower at baseline in the lines without GAP43 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000287622, ENSG00000242880, ENSG00000286540; maybe low, not absent |
| [[RIMS1]] | B | GAP43 activity raises RIMS1's level | lines that do not express GAP43 (22) vs lines expressing it (28) | 1.66× lower at baseline in the lines without GAP43 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000287622, ENSG00000242880, ENSG00000286540; maybe low, not absent |
| [[SGIP1]] | C | GAP43 activity raises SGIP1's level | lines that do not express GAP43 (22) vs lines expressing it (28) | 4.10× lower at baseline in the lines without GAP43 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000287622, ENSG00000242880, ENSG00000286540; maybe low, not absent; co-absent with the target |
| [[PTN]] | C | GAP43 activity raises PTN's level | lines that do not express GAP43 (22) vs lines expressing it (28) | 3.70× lower at baseline in the lines without GAP43 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000287622, ENSG00000242880, ENSG00000286540; maybe low, not absent; co-absent with the target |
| [[HGF]] | C | GAP43 activity raises HGF's level | lines that do not express GAP43 (22) vs lines expressing it (28) | 2.91× lower at baseline in the lines without GAP43 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000287622, ENSG00000242880, ENSG00000286540; maybe low, not absent; co-absent with the target |
| [[SYT1]] | C | GAP43 activity raises SYT1's level | lines that do not express GAP43 (22) vs lines expressing it (28) | 2.76× lower at baseline in the lines without GAP43 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000287622, ENSG00000242880, ENSG00000286540; maybe low, not absent; co-absent with the target |
| [[LINC01885]] | C | GAP43 activity raises LINC01885's level | lines that do not express GAP43 (22) vs lines expressing it (28) | 3.71× lower at baseline in the lines without GAP43 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000287622, ENSG00000242880, ENSG00000286540; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.541). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.5, 31.7); signed map (33.3, 33.4). **Vector** length 41.6, 7.46% of its response variance represented; |z| ≥ 3 in 600 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +10.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +7.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.7 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.6 | +9.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +0.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.1 | +0.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.0 | +2.8 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -2.6 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.4 | -1.7 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -1.2 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.4 | -3.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -1.3 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | growth associated protein 43 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.31 — chr3:115,623,510-115,721,490 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B-50, PP46, GAP-43 |
| Reactome | 3 pathways, smallest: L1CAM interactions; Axon guidance; Nervous system development |
| Matched by | ensembl_id |

**Function**, from UniProt [P17677](https://www.uniprot.org/uniprotkb/P17677) (Neuromodulin):

> This protein is associated with nerve growth. It is a major component of the motile 'growth cones' that form the tips of elongating axons. Plays a role in axonal and dendritic filopodia induction.

**Summary**, from NCBI Gene [2596](https://www.ncbi.nlm.nih.gov/gene/2596):

> The protein encoded by this gene has been termed a 'growth' or 'plasticity' protein because it is expressed at high levels in neuronal growth cones during development and axonal regeneration. This protein is considered a crucial component of an effective regenerative response in the nervous system. Alternatively spliced transcript variants encoding distinct isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4140](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4140) · Entrez [2596](https://www.ncbi.nlm.nih.gov/gene/2596) · UniProt [P17677](https://www.uniprot.org/uniprotkb/P17677) · Ensembl [ENSG00000172020](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172020)

## Data

Gene col 10200: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10200); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10200, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10200]; `tensor/DDL_lfc|DDL_z.npy` [10200]; `embed/gene_vectors.npy` [10200]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10200 or target_col == 10200). Every well: [[GAP43 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GAP43.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
