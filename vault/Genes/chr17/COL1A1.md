---
symbol: "COL1A1"
type: "gene"
col: 2998
ensembl_id: "ENSG00000108821"
name: "collagen type I alpha 1 chain"
location: "17q21.33"
module: 66
arm: "+"
pooled_cpm: 82.52
n_lines_expressing: 16
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 43
direction_downstream: 35
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# COL1A1

*collagen type I alpha 1 chain* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.82× (z +13.0, q 8e-36, up in 9 of 15 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.91× (z +7.5, q 9e-12, up in 9 of 14 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (HS-578T 0.211×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.419×; ⚠ cell-cycle shift, explains ~15% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL3A1]] (+0.75, fdr 7e-06), [[COL1A2]] (+0.75, fdr 7e-06), [[SPARC]] (+0.71, fdr 7e-06); moves opposite to [[ZC3H8]] (-0.44, fdr 2e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 43 arrows point to it, the strongest [[MYL9]] → it (grade B ⚠); 35 go from it, the strongest it → [[COL5A3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2998.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.82×** | +13.0 | 8e-36 | 9/15 (HS-578T, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.04×** | +11.1 | 5e-26 | 7/12 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.76×** | +7.7 | 2e-12 | 10/13 (SNU-423, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.91×** | +7.5 | 9e-12 | 9/14 (BT-474, A-172, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.23×** | +6.6 | 5e-09 | 8/14 (NCI-H2347, NCI-H1792, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.02×** | +5.4 | 6e-06 | 11/15 (BT-474, CHP-212, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.78×** | +4.7 | 2e-04 | 1/14 (NCI-H1792) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.68×** | +4.2 | 0.002 | 2/14 (NCI-H1792, SW 900) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.69×** | +3.8 | 0.008 | 8/15 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **1.52×** | +3.8 | 0.009 | 7/14 (HOP62, A-172, …) | two highest doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.58×** | +3.7 | 0.010 | 8/14 (NCI-H2347, SW 900, …) | rises with dose | composition shift; position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.08×** | +3.6 | 0.017 | 2/14 (BT-474, NCI-H1573) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.44×** | +3.2 | 0.052 | 4/11 (HS-578T, A-172, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.52×** | +3.2 | 0.055 | 6/14 (HS-578T, CHP-212, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~39% of this change | **1.50×** | +3.2 | 0.059 | 5/13 (NCI-H1792, NCI-H2347, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | **1.29×** | +2.9 | 0.097 | 9/14 (SNU-423, RPMI-7951, …) | rises with dose | position effect removed |
| [[Capmatinib (drug)]] 5 µM |  | **2.24×** | +2.9 | 0.097 | 5/14 (RPMI-7951, HOP62, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2998.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (HS-578T 0.211×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2347 0.419×; ⚠ cell-cycle shift, explains ~15% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.660× | -3.5 | 0.27 | 4/14 (A-172, CHP-212, …) | rises with dose |  |
| [[Budesonide (drug)]] 5 µM |  | 0.681× | -3.2 | 0.27 | 7/14 (NCI-H2347, A-172, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.684× | -3.2 | 0.27 | 4/14 (NCI-H2347, A-172, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.20 per unit of S-phase module lfc, +0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2998. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 101 | 2 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.70× (z +9.2) ⚠ cell-cycle shift, explains ~51% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.419× (z -8.9) ⚠ cell-cycle shift, explains ~15% of this change |
| [[HOP62 (line)]] | alt | 194 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.71× (z +8.6) ⚠ position not correctable | — |
| [[HS-578T (line)]] | alt | 1,708 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.211× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 58.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.60 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 15.6 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.90 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.8 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.05 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 47.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 6.71 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 5.59 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 646 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.65 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 16.8 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.37 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.53 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.62 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.08 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 7.59 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 876 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 12.6 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.59 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 5.44 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.5 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.67 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.54 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 72.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 7.19 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 73.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.5 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 5.59 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 527 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.45 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.76 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 6.17 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 249 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 577 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.89 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.33 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.07 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 8.07 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2998), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL3A1]] | +0.75 | +0.66 / +0.73 | both halves | 7e-06 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 999 |
| [[COL1A2]] | +0.75 | +0.72 / +0.78 | both halves | 7e-06 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 999 |
| [[SPARC]] | +0.71 | +0.64 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 968 |
| [[FBN1]] | +0.61 | +0.51 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 929 |
| [[NID2]] | +0.60 | +0.51 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 643 |
| [[DKK3]] | +0.59 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[SULF1]] | +0.58 | +0.45 / +0.57 | both halves | 3e-05 | STRING 621 |
| [[TIMP3]] | +0.58 | +0.38 / +0.71 | both halves | 7e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 684 |
| [[PDGFRB]] | +0.57 | +0.49 / +0.67 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 831 |
| [[COL5A2]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 995 |
| [[SMPD1]] | +0.57 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[PRSS23]] | +0.56 | +0.50 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZC3H8]] | -0.44 | -0.39 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*43 arrows, 43 of them with an alert ⚠; grade A 0, B 5, C 38. Shown: the 12 strongest; 31 more arrows (31 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MYL9]] | B | MYL9 activity raises COL1A1's level | lines that do not express MYL9 (22) vs lines expressing it (28) | 2.87× lower at baseline in the lines without MYL9 | 0.049 | ⚠ within organs, on part of the lines; also absent: CCBE1, EFEMP1, SEC14L4 |
| [[IGFBP6]] | B | IGFBP6 activity raises COL1A1's level | lines that do not express IGFBP6 (16) vs lines expressing it (34) | 3.11× lower at baseline in the lines without IGFBP6 | 0.081 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, HOXA10, COL6A1 |
| [[CCDC80]] | B | CCDC80 activity raises COL1A1's level | lines that do not express CCDC80 (21) vs lines expressing it (29) | 3.46× lower at baseline in the lines without CCDC80 | 0.082 | ⚠ within organs, on part of the lines; also absent: ABCC9, WNT5A, ALPK2 |
| [[COL5A3]] | B | COL5A3 activity raises COL1A1's level | lines that do not express COL5A3 (24) vs lines expressing it (26) | 2.42× lower at baseline in the lines without COL5A3 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZEB2, OR4F15, HS3ST3A1 |
| [[LINC00842]] | B | LINC00842 activity raises COL1A1's level | lines that do not express LINC00842 (25) vs lines expressing it (25) | 2.25× lower at baseline in the lines without LINC00842 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000276850, KRT81, EDN2 |
| [[PDGFRB]] | C | PDGFRB activity raises COL1A1's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 10.82× lower at baseline in the lines without PDGFRB | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises COL1A1's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 9.46× lower at baseline in the lines without APCDD1L | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[ITGA4]] | C | ITGA4 activity raises COL1A1's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 8.21× lower at baseline in the lines without ITGA4 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[SPARC]] | C | SPARC activity raises COL1A1's level | lines that do not express SPARC (34) vs lines expressing it (16) | 8.24× lower at baseline in the lines without SPARC | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032; co-absent with the target |
| [[MMP2]] | C | MMP2 activity raises COL1A1's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 8.40× lower at baseline in the lines without MMP2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L; co-absent with the target |
| [[COL5A1]] | C | COL5A1 activity raises COL1A1's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 6.68× lower at baseline in the lines without COL5A1 | 0.009 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[TIMP3]] | C | TIMP3 activity raises COL1A1's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 6.60× lower at baseline in the lines without TIMP3 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1; co-absent with the target |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 7, C 28. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL5A3]] | B | COL1A1 activity raises COL5A3's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 3.77× lower at baseline in the lines without COL1A1 | 0.005 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411 |
| [[ZC3H8]] | B | COL1A1 activity lowers ZC3H8's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 1.25× higher at baseline in the lines without COL1A1 | 0.032 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411 |
| [[B3GNT9]] | B | COL1A1 activity raises B3GNT9's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 1.53× lower at baseline in the lines without COL1A1 | 0.035 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411 |
| [[BMP1]] | B | COL1A1 activity strengthens BMP1's drug response | lines that do not express COL1A1 (32) vs lines expressing it (13) | the lines without COL1A1 respond 0.62× as strongly (z diff +1.72); strongest at Idarubicin (hydrochloride) 5 µM: 0.90x vs 0.48x (z diff +6.4) | 0.039 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; target measured in part of the lines; artifact flags |
| [[BMP1]] | B | COL1A1 activity raises BMP1's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 1.86× lower at baseline in the lines without COL1A1 | 0.059 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411 |
| [[MARCKS]] | B | COL1A1 activity raises MARCKS's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 2.78× lower at baseline in the lines without COL1A1 | 0.073 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411 |
| [[NREP]] | B | COL1A1 activity weakens NREP's drug response | lines that do not express COL1A1 (22) vs lines expressing it (13) | the lines without COL1A1 respond 1.54× as strongly (z diff -2.25); strongest at Homoharringtonine 5 µM: 0.29x vs 0.82x (z diff -5.3) | 0.090 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; target measured in part of the lines; artifact flags |
| [[COL6A1]] | C | COL1A1 activity raises COL6A1's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 5.29× lower at baseline in the lines without COL1A1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; co-absent with the target |
| [[FBN1]] | C | COL1A1 activity raises FBN1's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 6.74× lower at baseline in the lines without COL1A1 | 0.001 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; co-absent with the target |
| [[SPARC]] | C | COL1A1 activity raises SPARC's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 7.74× lower at baseline in the lines without COL1A1 | 0.001 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; co-absent with the target |
| [[PDGFRB]] | C | COL1A1 activity raises PDGFRB's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 6.37× lower at baseline in the lines without COL1A1 | 0.003 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; co-absent with the target |
| [[CREB3L1]] | C | COL1A1 activity raises CREB3L1's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 3.87× lower at baseline in the lines without COL1A1 | 0.003 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (55.9, 22.0); signed map (25.8, 42.7). **Vector** length 52.0, 18.4% of its response variance represented; |z| ≥ 3 in 350 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *angiogenesis* (hallmark, mean cos +0.51 to 5); *Signaling by PDGF* (reactome, mean cos +0.54 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.5 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.3 | +13.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.3 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.2 | +11.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +2.7 | +6.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.0 | +3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.7 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +2.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.5 | -1.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -2.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.3 | +0.3 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -2.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.3 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.2 | -0.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.2 | -3.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.2 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | collagen type I alpha 1 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:50,184,101-50,201,632 (-) |
| Ensembl biotype | protein_coding |
| Also known as | OI4 |
| Gene groups (HGNC) | Fibrillar collagens |
| Hallmark sets | UV_RESPONSE_DN, MYOGENESIS, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 42 pathways, smallest: Defective VWF cleavage by ADAMTS13 variant; Defects of platelet adhesion to exposed collagen; Enhanced cleavage of VWF variant by ADAMTS13 |
| Matched by | ensembl_id |

**Function**, from UniProt [P02452](https://www.uniprot.org/uniprotkb/P02452) (Collagen alpha-1(I) chain):

> Type I collagen is a member of group I collagen (fibrillar forming collagen).

**Summary**, from NCBI Gene [1277](https://www.ncbi.nlm.nih.gov/gene/1277):

> This gene encodes the pro-alpha1 chains of type I collagen whose triple helix comprises two alpha1 chains and one alpha2 chain. Type I is a fibril-forming collagen found in most connective tissues and is abundant in bone, cornea, dermis and tendon. Mutations in this gene are associated with osteogenesis imperfecta types I-IV, Ehlers-Danlos syndrome type VIIA, Ehlers-Danlos syndrome Classical type, Caffey Disease and idiopathic osteoporosis. Reciprocal translocations between chromosomes 17 and …

**Accessions** — [HGNC:2197](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2197) · Entrez [1277](https://www.ncbi.nlm.nih.gov/gene/1277) · UniProt [P02452](https://www.uniprot.org/uniprotkb/P02452) · Ensembl [ENSG00000108821](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108821)

## Data

Gene col 2998: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2998); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2998, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2998]; `tensor/DDL_lfc|DDL_z.npy` [2998]; `embed/gene_vectors.npy` [2998]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2998 or target_col == 2998). Every well: [[COL1A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL1A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
