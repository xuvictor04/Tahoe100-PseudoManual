---
symbol: "PECAM1"
type: "gene"
col: 15341
ensembl_id: "ENSG00000261371"
name: "platelet and endothelial cell adhesion molecule 1"
location: "17q23.3"
module: 90
arm: "+"
pooled_cpm: 4.19
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 7
n_dd_up_clean: 9
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 13
direction_downstream: 0
tags: ["gene", "module/090"]
generated_by: "tahoemap"
---

# PECAM1

*platelet and endothelial cell adhesion molecule 1* — 17q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.80× (z +26.5, q 0e+00, up in 27 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.872× (z -4.7, q 0.002, down in 15 of 46 measured lines) ⚠ position not correctable. The strongest without an alert is [[Belinostat (drug)]] 5 µM: 0.645× (z -4.3, q 0.004, down in 17 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01500]] (+0.72, fdr 7e-06), [[CNTNAP5]] (+0.71, fdr 7e-06), [[PTPRT]] (+0.71, fdr 7e-06).
> It is in [[Module 090]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[ANGPTL2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15341.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.80×** | +26.5 | 0e+00 | 27/32 (A498, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.96×** | +15.0 | 0e+00 | 23/32 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.03×** | +10.9 | 3e-25 | 7/14 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.16×** | +10.7 | 2e-24 | 19/44 (HOP62, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.01×** | +10.4 | 4e-23 | 1/6 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.56×** | +8.5 | 2e-15 | 1/7 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.06×** | +7.1 | 1e-10 | 19/38 (A-172, SK-MEL-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.05×** | +6.8 | 9e-10 | 8/32 (MIA PaCa-2, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.80×** | +5.8 | 5e-07 | 2/13 (SW480, NCI-H1792) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.26×** | +4.2 | 0.002 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.49×** | +3.9 | 0.005 | 8/41 (LoVo, SNU-423, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.9 | 0.005 | 0/15 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.48×** | +3.9 | 0.005 | 7/32 (A498, C32, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.66×** | +3.5 | 0.016 | 1/10 (Hs 766T) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **1.43×** | +3.5 | 0.016 | 1/20 (NCI-H1573) | top dose only | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.049 | 4/27 (HEC-1-A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Decitabine (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.081 | 3/35 (NCI-H460, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 15341.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.872× | -4.7 | 0.002 | 15/46 (HT-29, HOP62, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.645×** | -4.3 | 0.004 | 17/42 (HS-578T, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.607×** | -4.2 | 0.004 | 14/46 (SHP-77, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.652×** | -4.2 | 0.004 | 10/42 (SHP-77, NCI-H460, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.646×** | -4.1 | 0.004 | 13/33 (SHP-77, SK-MEL-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.753×** | -3.5 | 0.048 | 14/41 (SHP-77, RPMI-7951, …) | rises with dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.759×** | -3.3 | 0.066 | 10/43 (SHP-77, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.693×** | -3.3 | 0.066 | 10/43 (SHP-77, NCI-H1792, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.729× | -3.1 | 0.12 | 11/44 (HS-578T, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15341. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 32.7 | 0 | 11 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0886× (z -15.6) |
| [[RPMI-7951 (line)]] | alt | 40.3 | 0 | 7 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0176× (z -22.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.106× (z -12.5) |
| [[A498 (line)]] | wt | 1.43 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.8× (z +14.4) | — |
| [[HepG2_C3A (line)]] | wt | 9.32 | 0 | 2 | — | [[Ponatinib (drug)]] 5 µM 0.0663× (z -9.2) |
| [[HS-578T (line)]] | alt | 29.6 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.106× (z -10.7) |
| [[NCI-H460 (line)]] | wt | 1.52 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.6× (z +10.5) | — |
| [[A-172 (line)]] | wt | 1.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +9.6) | — |
| [[BT-474 (line)]] | alt | 2.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.3× (z +8.7) | — |
| [[C32 (line)]] | wt | 1.72 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 84.1× (z +13.1) | — |
| [[CFPAC-1 (line)]] | alt | 2.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.30× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 2.88 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.39× (z +9.6) | — |
| [[Hs 766T (line)]] | wt | 15.8 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.149× (z -9.4) ⚠ unreliable plate only |
| [[hTERT-HPNE (line)]] | wt | 3.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.1× (z +11.5) | — |
| [[LoVo (line)]] | wt | 1.55 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 29.5× (z +13.1) | — |
| [[NCI-H1792 (line)]] | alt | 7.35 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0671× (z -9.1) |
| [[NCI-H2347 (line)]] | alt | 1.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.5× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 1.23 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.20× (z +9.0) | — |
| [[A-427 (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.97 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.55 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.76 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.30 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.96 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.41 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.46 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.83 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.66 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15341), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01500]] | +0.72 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[CNTNAP5]] | +0.71 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[PTPRT]] | +0.71 | +0.70 / +0.67 | both halves | 7e-06 | same gene group |
| [[PLXNA4]] | +0.69 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[MYT1L]] | +0.69 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[DNAH2]] | +0.69 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[GRIA1]] | +0.67 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[MILR1]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 | same gene group; ⚠ same locus (35.3 kb: neighbours can correlate without regulation) |
| [[ZPLD1]] | +0.65 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[CCDC26]] | +0.65 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[C2CD6]] | +0.65 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[IPCEF1]] | +0.65 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[CLVS1]] | +0.65 | +0.53 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANGPTL2]] | B | ANGPTL2 activity raises PECAM1's level | lines that do not express ANGPTL2 (29) vs lines expressing it (21) | 2.01× lower at baseline in the lines without ANGPTL2 | 0.006 | ⚠ within organs, on part of the lines; also absent: LINC01611, ENSG00000189229, CDH13; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises PECAM1's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 1.1% of all compounds | 0.013 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity lowers PECAM1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[AK4P3]] | B | AK4P3 activity raises PECAM1's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 2.00× lower at baseline in the lines without AK4P3 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF |
| [[ADAM28]] | B | ADAM28 activity raises PECAM1's level | lines that do not express ADAM28 (31) vs lines expressing it (19) | 2.00× lower at baseline in the lines without ADAM28 | 0.027 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5 |
| [[MILR1]] | B | MILR1 activity raises PECAM1's level | lines that do not express MILR1 (19) vs lines expressing it (31) | 1.88× lower at baseline in the lines without MILR1 | 0.036 | ⚠ within organs, on part of the lines; also absent: EVA1A, LINC00973, NLRP1 |
| [[LINC01287]] | B | LINC01287 activity raises PECAM1's level | lines that do not express LINC01287 (39) vs lines expressing it (11) | 2.65× lower at baseline in the lines without LINC01287 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253642, POU6F2, RIT2 |
| [[BAALC]] | B | BAALC activity raises PECAM1's level | lines that do not express BAALC (32) vs lines expressing it (18) | 2.00× lower at baseline in the lines without BAALC | 0.052 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: SPARC, ENSG00000287598, LINC01411; maybe low, not absent |
| [[MAP2K2]] | B | MAP2K2 activity raises PECAM1's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |
| [[CALCA]] | B | CALCA activity raises PECAM1's level | lines that do not express CALCA (45) vs lines expressing it (5) | 2.10× lower at baseline in the lines without CALCA | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[ZNF385D]] | B | ZNF385D activity raises PECAM1's level | lines that do not express ZNF385D (25) vs lines expressing it (25) | 1.89× lower at baseline in the lines without ZNF385D | 0.062 | ⚠ within organs, on part of the lines; also absent: ARMCX1, LINC03047, ITGA4; maybe low, not absent |
| [[ADAM28]] | B | ADAM28 activity weakens PECAM1's drug response | lines that do not express ADAM28 (29) vs lines expressing it (17) | the lines without ADAM28 respond 5.59× as strongly (z diff -2.00); strongest at Dinaciclib 5 µM: 2.89x vs 0.36x (z diff -9.0) | 0.065 | ⚠ within organs, on part of the lines; also absent: DHRS9, BATF, IGFBP5; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 090]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.687). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.8, 31.1); signed map (31.6, 17.1). **Vector** length 73.2, 12.5% of its response variance represented; |z| ≥ 3 in 1,073 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.7 | +26.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +9.5 | +15.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.6 | +10.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.5 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.2 | +10.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +10.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +2.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.5 | +1.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +0.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.1 | -3.3 |
|  | [[Trametinib (drug)]] 5 µM |  | -3.0 | -4.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.8 | -2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.4 | -2.6 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.3 | -4.7 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -2.2 | -2.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.1 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | platelet and endothelial cell adhesion molecule 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.3 — chr17:64,319,415-64,413,776 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD31 |
| Gene groups (HGNC) | CD molecules; Immunoglobulin like domain containing; Ig-like cell adhesion molecule family |
| Hallmark sets | COAGULATION, KRAS_SIGNALING_UP, APICAL_JUNCTION |
| Reactome | 16 pathways, smallest: PECAM1 interactions; Platelet sensitization by LDL; High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells |
| Matched by | ensembl_id |

**Function**, from UniProt [P16284](https://www.uniprot.org/uniprotkb/P16284) (Platelet endothelial cell adhesion molecule):

> Cell adhesion molecule which is required for leukocyte transendothelial migration (TEM) under most inflammatory conditions. Tyr-690 plays a critical role in TEM and is required for efficient trafficking of PECAM1 to and from the lateral border recycling compartment (LBRC) and is also essential for the LBRC membrane to be targeted around migrating leukocytes. Trans-homophilic interaction may play a role in endothelial cell-cell adhesion via cell junctions. Heterophilic interaction with CD177 …

**Summary**, from NCBI Gene [5175](https://www.ncbi.nlm.nih.gov/gene/5175):

> The protein encoded by this gene is found on the surface of platelets, monocytes, neutrophils, and some types of T-cells, and makes up a large portion of endothelial cell intercellular junctions. The encoded protein is a member of the immunoglobulin superfamily and is likely involved in leukocyte migration, angiogenesis, and integrin activation. [provided by RefSeq, May 2010]

**Accessions** — [HGNC:8823](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8823) · Entrez [5175](https://www.ncbi.nlm.nih.gov/gene/5175) · UniProt [P16284](https://www.uniprot.org/uniprotkb/P16284) · Ensembl [ENSG00000261371](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000261371)

## Data

Gene col 15341: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15341); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15341, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15341]; `tensor/DDL_lfc|DDL_z.npy` [15341]; `embed/gene_vectors.npy` [15341]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15341 or target_col == 15341). Every well: [[PECAM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PECAM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
