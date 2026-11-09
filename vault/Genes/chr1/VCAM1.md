---
symbol: "VCAM1"
type: "gene"
col: 8562
ensembl_id: "ENSG00000162692"
name: "vascular cell adhesion molecule 1"
location: "1p21.2"
module: 14
arm: "+"
pooled_cpm: 19.16
n_lines_expressing: 10
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 13
direction_downstream: 1
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# VCAM1

*vascular cell adhesion molecule 1* — 1p21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (11 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.92× (z +14.2, q 5e-43, up in 9 of 9 measured lines) ⚠ cell-cycle shift, explains ~29% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.68× (z +10.3, q 2e-22, up in 8 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[5-Azacytidine (drug)]] 5 µM: 0.603× (z -3.7, q 0.075, down in 5 of 9 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (A498 0.138×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bortezomib (drug)]] 5 µM in 1 line (A498 0.0387×; ⚠ toxic); [[Auranofin (drug)]] 5 µM in 1 line (A498 0.192×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 0.357×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CSF1]] (+0.75, fdr 7e-06), [[TNFAIP2]] (+0.64, fdr 1e-05), [[AKR1B1]] (+0.63, fdr 1e-05); moves opposite to [[DIP2A]] (-0.48, fdr 4e-05), [[ZIM2-AS1]] (-0.47, fdr 6e-05), [[ZNF71]] (-0.46, fdr 2e-04).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[IRAG2]] → it (grade C ⚠); 1 goes from it, the strongest it → [[IRAG2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 11 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8562.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **3.92×** | +14.2 | 5e-43 | 9/9 (HOP62, SNU-423, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.07×** | +10.3 | 1e-22 | 1/8 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.68×** | +10.3 | 2e-22 | 8/9 (HOP62, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.97×** | +9.8 | 2e-20 | 1/6 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.88×** | +7.5 | 8e-12 | 9/9 (SNU-423, HOP62, …) | rises with dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.95×** | +7.4 | 2e-11 | 2/5 (HOP62, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.66×** | +7.2 | 5e-11 | 8/9 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.29×** | +6.1 | 8e-08 | 8/9 (A-172, HOP62, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +5.8 | 4e-07 | 7/9 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.08×** | +5.4 | 4e-06 | 8/9 (A-172, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~37% of this change | **1.99×** | +5.1 | 2e-05 | 1/8 (RPMI-7951) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.95×** | +4.7 | 1e-04 | 6/9 (SNU-423, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.97×** | +3.6 | 0.017 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.60×** | +3.4 | 0.024 | 8/9 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.42×** | +3.4 | 0.026 | 2/4 (HOP62, SNU-423) | top dose only | noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | **1.61×** | +3.4 | 0.028 | 4/9 (HS-578T, A498, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.38×** | +3.3 | 0.028 | 6/9 (SNU-423, RPMI-7951, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8562.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (A498 0.138×; ⚠ cell-cycle shift, explains ~0% of this change); [[Bortezomib (drug)]] 5 µM in 1 line (A498 0.0387×; ⚠ toxic); [[Auranofin (drug)]] 5 µM in 1 line (A498 0.192×); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (A498 0.357×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[5-Azacytidine (drug)]] 5 µM |  | **0.603×** | -3.7 | 0.075 | 5/9 (H4, A498, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.614×** | -3.6 | 0.075 | 2/9 (A498, SW 1088) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.619×** | -3.5 | 0.075 | 1/9 (A498) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Fluvoxamine (drug)]] 0.5 µM |  | 0.635× | -3.4 | 0.11 | 0/9 | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.650× | -3.2 | 0.16 | 3/9 (A498, HS-578T, …) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.885× | -3.1 | 0.16 | 0/9 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.32 per unit of S-phase module lfc, +0.65 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8562. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 8.49 | 6 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 26.5× (z +15.1) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 18.4× (z +9.5) | — |
| [[A498 (line)]] | wt | 383 | 0 | 6 (4 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.138× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.192× (z -10.0) |
| [[HOP62 (line)]] | alt | 31.4 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 12.4× (z +15.9) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.55× (z +10.8) | — |
| [[SNU-423 (line)]] | alt | 28.6 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 16.9× (z +15.4) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.36× (z +10.8) | — |
| [[HS-578T (line)]] | alt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.3× (z +9.6) | — |
| [[Panc 03.27 (line)]] | alt | 6.36 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 32.7× (z +13.2) ⚠ cell-cycle shift, explains ~29% of this change | — |
| [[RPMI-7951 (line)]] | alt | 16.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.03× (z +9.1) | — |
| [[A-427 (line)]] | wt | 0.632 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.891 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.751 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.944 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.884 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.65 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.864 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.992 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.791 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.869 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.76 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.926 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.855 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.763 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.940 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.754 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.899 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.786 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.790 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.716 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.95 n.m. | — | — | — | — |
| [[NCI-H23 (line)]] | alt | 0.740 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.719 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.882 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.843 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.796 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.897 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.899 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.980 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 91.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.983 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.888 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.821 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8562), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CSF1]] | +0.75 | +0.72 / +0.71 | both halves | 7e-06 | STRING 542 |
| [[TNFAIP2]] | +0.64 | +0.53 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[AKR1B1]] | +0.63 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[TNFAIP6]] | +0.63 | +0.64 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[CCL2]] | +0.63 | +0.57 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 907 |
| [[CFH]] | +0.63 | +0.64 / +0.50 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[OLR1]] | +0.62 | +0.64 / +0.49 | both halves | 1e-05 | STRING 613 |
| [[LUM]] | +0.62 | +0.62 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 421 |
| [[MSC]] | +0.61 | +0.49 / +0.60 | both halves | 1e-05 |  |
| [[KCNT2]] | +0.60 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[LINC02605]] | +0.59 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[EYA4]] | +0.59 | +0.53 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DIP2A]] | -0.48 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[ZIM2-AS1]] | -0.47 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[ZNF71]] | -0.46 | -0.52 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 0, C 13. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRAG2]] | C | IRAG2 activity raises VCAM1's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 2.62× lower at baseline in the lines without IRAG2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411; co-absent with the target |
| [[PTN]] | C | PTN activity raises VCAM1's level | lines that do not express PTN (28) vs lines expressing it (22) | 3.90× lower at baseline in the lines without PTN | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, SPARC, BAALC; co-absent with the target |
| [[IL6]] | C | IL6 activity raises VCAM1's level | lines that do not express IL6 (32) vs lines expressing it (18) | 3.78× lower at baseline in the lines without IL6 | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000232949, STEAP1B-AS1, G0S2; co-absent with the target |
| [[CFH]] | C | CFH activity raises VCAM1's level | lines that do not express CFH (28) vs lines expressing it (22) | 2.61× lower at baseline in the lines without CFH | 0.024 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1; co-absent with the target |
| [[CCBE1]] | C | CCBE1 activity raises VCAM1's level | lines that do not express CCBE1 (28) vs lines expressing it (22) | 2.85× lower at baseline in the lines without CCBE1 | 0.039 | ⚠ within organs, on part of the lines; also absent: EDNRA, IL7R, EFEMP1; co-absent with the target |
| [[LUM]] | C | LUM activity raises VCAM1's level | lines that do not express LUM (34) vs lines expressing it (16) | 2.56× lower at baseline in the lines without LUM | 0.043 | ⚠ within organs, on part of the lines; also absent: ITGA11, DCN, IRAG2; co-absent with the target |
| [[IL7R]] | C | IL7R activity raises VCAM1's level | lines that do not express IL7R (30) vs lines expressing it (20) | 3.63× lower at baseline in the lines without IL7R | 0.044 | ⚠ within organs, on part of the lines; also absent: IL1B, COL5A1, CCBE1; co-absent with the target |
| [[CXCL5]] | C | CXCL5 activity raises VCAM1's level | lines that do not express CXCL5 (35) vs lines expressing it (15) | 1.47× lower at baseline in the lines without CXCL5 | 0.044 | ⚠ within organs, on part of the lines; also absent: ANXA10, IRAK3, TRBC2; co-absent with the target |
| [[C1QTNF1-AS1]] | C | C1QTNF1-AS1 activity raises VCAM1's level | lines that do not express C1QTNF1-AS1 (24) vs lines expressing it (26) | 2.63× lower at baseline in the lines without C1QTNF1-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ADAMTS12, ENSG00000287335, FBLN2; maybe low, not absent; co-absent with the target |
| [[ALPK2]] | C | ALPK2 activity raises VCAM1's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 3.75× lower at baseline in the lines without ALPK2 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4; co-absent with the target |
| [[TNFAIP6]] | C | TNFAIP6 activity raises VCAM1's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 3.04× lower at baseline in the lines without TNFAIP6 | 0.082 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF; co-absent with the target |
| [[KYNU]] | C | KYNU activity raises VCAM1's level | lines that do not express KYNU (29) vs lines expressing it (21) | 2.78× lower at baseline in the lines without KYNU | 0.084 | ⚠ within organs, on part of the lines; also absent: ENSG00000289600, CRLF2, LINC02725; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRAG2]] | C | VCAM1 activity raises IRAG2's level | lines that do not express VCAM1 (40) vs lines expressing it (10) | 2.30× lower at baseline in the lines without VCAM1 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, TMPRSS15, GLYATL2; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.600). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.5, 22.6); signed map (45.8, 21.7). **Vector** length 47.5, 19.4% of its response variance represented; |z| ≥ 3 in 276 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +10.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | +1.9 | +14.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +1.8 | +7.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +1.6 | +6.1 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.5 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.2 | +1.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.2 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.1 | +2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.1 | +1.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.0 | -1.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | +0.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.8 | -0.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | -1.7 | +1.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | -0.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.1 | -0.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | vascular cell adhesion molecule 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.2 — chr1:100,719,742-100,739,045 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD106 |
| Gene groups (HGNC) | CD molecules; Receptor ligands; C2-set domain containing; I-set domain containing; Ig-like cell adhesion molecule family |
| Hallmark sets | APICAL_JUNCTION, INTERFERON_GAMMA_RESPONSE, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 11 pathways, smallest: Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Integrin cell surface interactions; Interferon gamma signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P19320](https://www.uniprot.org/uniprotkb/P19320) (Vascular cell adhesion protein 1):

> Cell adhesion glycoprotein predominantly expressed on the surface of endothelial cells that plays an important role in immune surveillance and inflammation. Acts as a major regulator of leukocyte adhesion to the endothelium through interaction with different types of integrins. During inflammatory responses, binds ligands on the surface of activated endothelial cells to initiate the activation of calcium channels and the plasma membrane-associated small GTPase RAC1 leading to leukocyte …

**Summary**, from NCBI Gene [7412](https://www.ncbi.nlm.nih.gov/gene/7412):

> This gene is a member of the Ig superfamily and encodes a cell surface sialoglycoprotein expressed by cytokine-activated endothelium. This type I membrane protein mediates leukocyte-endothelial cell adhesion and signal transduction, and may play a role in the development of artherosclerosis and rheumatoid arthritis. Three alternatively spliced transcripts encoding different isoforms have been described for this gene. [provided by RefSeq, Dec 2010]

**Accessions** — [HGNC:12663](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12663) · Entrez [7412](https://www.ncbi.nlm.nih.gov/gene/7412) · UniProt [P19320](https://www.uniprot.org/uniprotkb/P19320) · Ensembl [ENSG00000162692](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162692)

## Data

Gene col 8562: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8562); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8562, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8562]; `tensor/DDL_lfc|DDL_z.npy` [8562]; `embed/gene_vectors.npy` [8562]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8562 or target_col == 8562). Every well: [[VCAM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/VCAM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
