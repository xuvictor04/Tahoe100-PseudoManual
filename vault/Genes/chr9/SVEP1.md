---
symbol: "SVEP1"
type: "gene"
col: 9074
ensembl_id: "ENSG00000165124"
name: "sushi, von Willebrand factor type A, EGF and pentraxin domain containing 1"
location: "9q31.3"
module: 150
arm: "+"
pooled_cpm: 4.99
n_lines_expressing: 35
n_dd_up: 25
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 8
tags: ["gene", "module/150"]
generated_by: "tahoemap"
---

# SVEP1

*sushi, von Willebrand factor type A, EGF and pentraxin domain containing 1* — 9q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.03× (z +17.5, q 0e+00, up in 16 of 25 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RPMI-7951 0.266×); [[Panobinostat (drug)]] 0.5 µM in 1 line (Hs 766T 0.0322×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (Hs 766T 0.0784×; ⚠ toxic; transcription drop); [[Belumosudil (drug)]] 0.05 µM in 1 line (SNU-423 0.0592×); [[Tadalafil (drug)]] 5 µM in 1 line (NCI-H460 0.0586×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00607]] (+0.69, fdr 1e-05), [[STXBP5-AS1]] (+0.63, fdr 1e-05), [[PPFIA2]] (+0.62, fdr 1e-05).
> It is in [[Module 150]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[HTRA3]] → it (grade B ⚠); 8 go from it, the strongest it → [[BICC1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9074.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.03×** | +17.5 | 0e+00 | 16/25 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.37×** | +13.7 | 6e-40 | 23/30 (NCI-H460, LS 180, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.68×** | +11.1 | 4e-26 | 3/15 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.63×** | +10.4 | 3e-23 | 1/6 (NCI-H2030) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.24×** | +9.0 | 2e-17 | 10/26 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.00×** | +7.7 | 1e-12 | 14/26 (LS 180, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.01×** | +7.2 | 4e-11 | 3/9 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.71×** | +6.0 | 1e-07 | 8/27 (HOP62, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +5.7 | 7e-07 | 11/26 (A-172, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +5.3 | 6e-06 | 9/26 (A-172, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +4.6 | 2e-04 | 4/26 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.49×** | +4.5 | 4e-04 | 9/28 (RPMI-7951, J82, …) | inconsistent across doses |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.04×** | +4.2 | 0.001 | 1/7 (NCI-H23) | top dose only | noisy plate (z scaled) |
| [[Drospirenone (drug)]] 0.5 µM |  | **1.43×** | +4.0 | 0.003 | 6/28 (CFPAC-1, COLO 205, …) | inconsistent across doses | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **1.43×** | +3.8 | 0.005 | 8/28 (NCI-H1573, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.016 | 4/24 (SNU-423, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.35×** | +3.3 | 0.028 | 7/30 (RPMI-7951, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.38×** | +3.3 | 0.031 | 5/24 (COLO 205, KATO III, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.032 | 9/28 (RPMI-7951, hTERT-HPNE, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9074.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (RPMI-7951 0.266×); [[Panobinostat (drug)]] 0.5 µM in 1 line (Hs 766T 0.0322×; ⚠ cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (Hs 766T 0.0784×; ⚠ toxic; transcription drop); [[Belumosudil (drug)]] 0.05 µM in 1 line (SNU-423 0.0592×); [[Tadalafil (drug)]] 5 µM in 1 line (NCI-H460 0.0586×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | 0.802× | -3.6 | 0.21 | 9/29 (CHP-212, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9074. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 9.38 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0322× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.33 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.2× (z +10.1) | — |
| [[KATO III (line)]] | alt | 3.13 | 0 | 1 | — | [[L-Thyroxine (sodium salt pentahydrate) (drug)]] 0.5 µM 0.0799× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.546× (z -8.8) ⚠ position not correctable |
| [[NCI-H460 (line)]] | wt | 1.88 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0586× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 129 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -14.3) |
| [[SNU-423 (line)]] | alt | 4.76 | 0 | 1 | — | [[Belumosudil (drug)]] 0.05 µM 0.0592× (z -8.7) |
| [[A-427 (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.19 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.65 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.14 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.28 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.831 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.917 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.856 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.76 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.985 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.913 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.589 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.989 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.819 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.761 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.752 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.782 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.03 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.749 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.72 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.33 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9074), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00607]] | +0.69 | +0.55 / +0.74 | both halves | 1e-05 |  |
| [[STXBP5-AS1]] | +0.63 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[PPFIA2]] | +0.62 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[TG]] | +0.61 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[MYO3B]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[KCNB1]] | +0.60 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[AOX1]] | +0.59 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[ABCA6]] | +0.58 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[DYNLRB2-AS1]] | +0.58 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[SAMSN1]] | +0.57 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[SPOCK3]] | +0.57 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[LINC01807]] | +0.57 | +0.48 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HTRA3]] | B | HTRA3 activity raises SVEP1's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 2.55× lower at baseline in the lines without HTRA3 | 0.006 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |
| [[TOP2A]] | B | TOP2A activity lowers SVEP1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ERC2]] | B | ERC2 activity raises SVEP1's level | lines that do not express ERC2 (20) vs lines expressing it (30) | 1.89× lower at baseline in the lines without ERC2 | 0.033 | ⚠ within organs, on part of the lines; also absent: VAT1L, LDOC1, SNAP91; maybe low, not absent |
| [[ITGA8]] | B | ITGA8 activity raises SVEP1's level | lines that do not express ITGA8 (37) vs lines expressing it (13) | 2.63× lower at baseline in the lines without ITGA8 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000224865, CARMN, THY1; maybe low, not absent |
| [[S1PR3]] | B | S1PR3 activity raises SVEP1's level | lines that do not express S1PR3 (21) vs lines expressing it (29) | 2.09× lower at baseline in the lines without S1PR3 | 0.059 | ⚠ within organs, on part of the lines; also absent: BASP1, VEGFC, SPANXA2-OT1 |
| [[SLC2A14]] | B | SLC2A14 activity raises SVEP1's level | lines that do not express SLC2A14 (13) vs lines expressing it (37) | 1.86× lower at baseline in the lines without SLC2A14 | 0.060 | ⚠ within organs, on part of the lines; also absent: NPAS3, SLC2A3, HEY1; maybe low, not absent |
| [[RP1]] | B | RP1 activity raises SVEP1's level | lines that do not express RP1 (19) vs lines expressing it (31) | 1.67× lower at baseline in the lines without RP1 | 0.073 | ⚠ within organs, on part of the lines; also absent: CYB5R2, KIAA1549L, KCNN4; maybe low, not absent |
| [[BICC1]] | B | BICC1 activity raises SVEP1's level | lines that do not express BICC1 (28) vs lines expressing it (22) | 2.19× lower at baseline in the lines without BICC1 | 0.074 | ⚠ within organs, on part of the lines; also absent: ITGB3, COL4A1, COL4A2 |
| [[LPAR1]] | C | LPAR1 activity raises SVEP1's level | lines that do not express LPAR1 (15) vs lines expressing it (35) | 2.20× lower at baseline in the lines without LPAR1 | 0.056 | ⚠ within organs, on part of the lines; also absent: SVEP1, PAPSS2, TOX2; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BICC1]] | B | SVEP1 activity raises BICC1's level | lines that do not express SVEP1 (15) vs lines expressing it (35) | 3.00× lower at baseline in the lines without SVEP1 | 0.038 | ⚠ within organs, on part of the lines; also absent: LPAR1, CDH8, ENSG00000253100; maybe low, not absent |
| [[ADPRHL1]] | B | SVEP1 activity raises ADPRHL1's level | lines that do not express SVEP1 (15) vs lines expressing it (35) | 1.68× lower at baseline in the lines without SVEP1 | 0.051 | ⚠ within organs, on part of the lines; also absent: LPAR1, CDH8, ENSG00000253100; maybe low, not absent |
| [[LINC00298]] | B | SVEP1 activity raises LINC00298's level | lines that do not express SVEP1 (15) vs lines expressing it (35) | 1.30× lower at baseline in the lines without SVEP1 | 0.087 | ⚠ within organs, on part of the lines; also absent: LPAR1, CDH8, ENSG00000253100; maybe low, not absent |
| [[SAMSN1]] | B | SVEP1 activity raises SAMSN1's level | lines that do not express SVEP1 (15) vs lines expressing it (35) | 1.62× lower at baseline in the lines without SVEP1 | 0.093 | ⚠ within organs, on part of the lines; also absent: LPAR1, CDH8, ENSG00000253100; maybe low, not absent |
| cells under [[Anethole trithione (drug)]] 0.5 µM | B | SVEP1 activity raises the cells' numbers under Anethole trithione 0.5 µM (protects the cells) | lines that do not express SVEP1 (15) vs lines expressing it (33) | the lines without SVEP1: 0.89× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; also absent: LPAR1, CDH8, ENSG00000253100; maybe low, not absent |
| [[KCNQ3]] | B | SVEP1 activity lowers KCNQ3's level | lines that do not express SVEP1 (15) vs lines expressing it (35) | 1.55× higher at baseline in the lines without SVEP1 | 0.096 | ⚠ within organs, on part of the lines; also absent: LPAR1, CDH8, ENSG00000253100; maybe low, not absent |
| [[ERC2]] | B | SVEP1 activity raises ERC2's level | lines that do not express SVEP1 (15) vs lines expressing it (35) | 1.76× lower at baseline in the lines without SVEP1 | 0.099 | ⚠ within organs, on part of the lines; also absent: LPAR1, CDH8, ENSG00000253100; maybe low, not absent |
| [[LPAR1]] | C | SVEP1 activity raises LPAR1's level | lines that do not express SVEP1 (15) vs lines expressing it (35) | 4.91× lower at baseline in the lines without SVEP1 | 0.032 | ⚠ within organs, on part of the lines; also absent: LPAR1, CDH8, ENSG00000253100; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 150]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.624). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (26.0, 21.3); signed map (25.9, 13.2). **Vector** length 48.4, 7.71% of its response variance represented; |z| ≥ 3 in 742 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.3 | +11.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +13.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +7.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +17.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +3.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +6.0 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.2 | +4.5 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +1.9 | +3.3 |
| fall | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.3 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -1.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -0.6 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -1.1 | +0.2 |

## What is on record

|  |  |
|---|---|
| Name | sushi, von Willebrand factor type A, EGF and pentraxin domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.3 — chr9:110,365,248-110,579,880 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA427L11.3, POLYDOM, FLJ13529; previously C9orf13 |
| Gene groups (HGNC) | Sushi domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4LDE5](https://www.uniprot.org/uniprotkb/Q4LDE5) (Sushi, von Willebrand factor type A, EGF and pentraxin domain-containing protein 1):

> Required for morphological development, cell alignment and migration of lymphatic endothelial cells during embryonic development, potentially via modulation of ANGPT2-TIE1 signaling and subsequent activation of FOXC2 transcription (By similarity). Required for embryonic lymphatic vascular development, via mediating the correct formation of the first lymphovenous contact site and tight association of the lymphatic endothelium with the venous endothelium (By similarity). Represses PRKCA-mediated …

**Summary**, from NCBI Gene [79987](https://www.ncbi.nlm.nih.gov/gene/79987):

> Enables integrin binding activity. Involved in negative regulation of vasoconstriction and positive regulation of platelet activation. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:15985](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15985) · Entrez [79987](https://www.ncbi.nlm.nih.gov/gene/79987) · UniProt [Q4LDE5](https://www.uniprot.org/uniprotkb/Q4LDE5) · Ensembl [ENSG00000165124](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165124)

## Data

Gene col 9074: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9074); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9074, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9074]; `tensor/DDL_lfc|DDL_z.npy` [9074]; `embed/gene_vectors.npy` [9074]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9074 or target_col == 9074). Every well: [[SVEP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SVEP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
