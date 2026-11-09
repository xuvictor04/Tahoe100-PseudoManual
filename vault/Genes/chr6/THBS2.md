---
symbol: "THBS2"
type: "gene"
col: 11806
ensembl_id: "ENSG00000186340"
name: "thrombospondin 2"
location: "6q27"
module: 13
arm: "+"
pooled_cpm: 30.74
n_lines_expressing: 13
n_dd_up: 12
n_dd_down: 6
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 38
direction_downstream: 39
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# THBS2

*thrombospondin 2* — 6q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.78× (z +13.0, q 8e-36, up in 6 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.48× (z +5.7, q 2e-06, up in 6 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.502× (z -7.0, q 1e-09, down in 9 of 11 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[COL6A2]] (+0.79, fdr 7e-06), [[COL5A1]] (+0.77, fdr 7e-06), [[COL6A3]] (+0.76, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 38 arrows point to it, the strongest [[F3]] → it (grade B ⚠); 39 go from it, the strongest it → [[SYTL3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11806.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.78×** | +13.0 | 8e-36 | 6/10 (KATO III, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.57×** | +12.9 | 8e-36 | 6/10 (KATO III, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.40×** | +8.2 | 3e-14 | 4/10 (KATO III, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.48×** | +5.7 | 2e-06 | 6/11 (A498, LOX-IMVI, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.34×** | +4.5 | 7e-04 | 2/6 (C32, SNU-423) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +4.1 | 0.004 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.75×** | +4.1 | 0.004 | 1/10 (LOX-IMVI) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.47×** | +3.9 | 0.007 | 0/11 | inconsistent across doses | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.6 | 0.017 | 1/11 (C32) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +3.6 | 0.017 | 1/11 (C32) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.62×** | +3.5 | 0.023 | 0/10 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.54×** | +3.1 | 0.088 | 0/11 | inconsistent across doses | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11806.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.502×** | -7.0 | 1e-09 | 9/11 (HOP62, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.642×** | -4.5 | 0.001 | 9/11 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.632×** | -4.5 | 0.001 | 8/11 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 0.5 µM |  | **0.682×** | -3.9 | 0.014 | 0/11 | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.696×** | -3.7 | 0.023 | 1/11 (CHP-212) | inconsistent across doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.906× | -3.7 | 0.023 | 1/11 (LOX-IMVI) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.704×** | -3.3 | 0.078 | 0/11 | inconsistent across doses |  |
| [[Allantoin (drug)]] 5 µM |  | 0.802× | -3.2 | 0.11 | 0/11 | top dose only |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.724× | -3.0 | 0.15 | 0/11 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11806. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 138 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.135× (z -10.3) |
| [[A-172 (line)]] | wt | 598 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.222× (z -9.5) |
| [[A498 (line)]] | wt | 18.4 | 2 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 3.81× (z +10.8) | — |
| [[KATO III (line)]] | alt | 14.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 8.83× (z +8.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 191 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -12.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.173× (z -9.7) |
| [[LOX-IMVI (line)]] | wt | 9.98 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0440× (z -11.3) ⚠ cell-cycle shift, explains ~1% of this change |
| [[A-427 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.69 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 66.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.36 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.06 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 135 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.94 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 66.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.58 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.40 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.64 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11806), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COL6A2]] | +0.79 | +0.79 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 754 |
| [[COL5A1]] | +0.77 | +0.74 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 742 |
| [[COL6A3]] | +0.76 | +0.76 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 799 |
| [[COL6A1]] | +0.75 | +0.79 / +0.65 | both halves | 7e-06 | pathway: Signaling by PDGF; STRING 756 |
| [[LINC01615]] | +0.73 | +0.72 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[PDGFRB]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 449 |
| [[DKK3]] | +0.68 | +0.70 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[SARDH]] | +0.67 | +0.61 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[CSPG4]] | +0.66 | +0.69 / +0.57 | both halves | 1e-05 | pathway: Diseases of glycosylation |
| [[NAV1]] | +0.65 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[SEMA5A]] | +0.64 | +0.60 / +0.65 | both halves | 7e-06 | pathway: Defective B3GALTL causes PpS |
| [[INSYN2B]] | +0.64 | +0.67 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 1, C 37. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F3]] | B | F3 activity raises THBS2's level | lines that do not express F3 (24) vs lines expressing it (26) | 2.23× lower at baseline in the lines without F3 | 0.080 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[PDGFRB]] | C | PDGFRB activity raises THBS2's level | lines that do not express PDGFRB (36) vs lines expressing it (14) | 5.39× lower at baseline in the lines without PDGFRB | 0.002 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL3A1, ALPK2, GREM2; co-absent with the target |
| [[ITGA4]] | C | ITGA4 activity raises THBS2's level | lines that do not express ITGA4 (33) vs lines expressing it (17) | 6.37× lower at baseline in the lines without ITGA4 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: MMP2, SPARC, LINC01411; co-absent with the target |
| [[LINC01411]] | C | LINC01411 activity raises THBS2's level | lines that do not express LINC01411 (38) vs lines expressing it (12) | 7.44× lower at baseline in the lines without LINC01411 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: VCAM1, TMPRSS15, ENSG00000222032; co-absent with the target |
| [[COL4A1]] | C | COL4A1 activity raises THBS2's level | lines that do not express COL4A1 (29) vs lines expressing it (21) | 4.11× lower at baseline in the lines without COL4A1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: COL4A2, NID2, ABI3BP; co-absent with the target |
| [[HS3ST3A1]] | C | HS3ST3A1 activity raises THBS2's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 5.24× lower at baseline in the lines without HS3ST3A1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1; co-absent with the target |
| [[MMP2]] | C | MMP2 activity raises THBS2's level | lines that do not express MMP2 (34) vs lines expressing it (16) | 5.90× lower at baseline in the lines without MMP2 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, SPARC, APCDD1L; co-absent with the target |
| [[KIRREL3]] | C | KIRREL3 activity raises THBS2's level | lines that do not express KIRREL3 (36) vs lines expressing it (14) | 4.82× lower at baseline in the lines without KIRREL3 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN; co-absent with the target |
| [[COL6A1]] | C | COL6A1 activity raises THBS2's level | lines that do not express COL6A1 (24) vs lines expressing it (26) | 4.53× lower at baseline in the lines without COL6A1 | 0.021 | ⚠ within organs, on part of the lines; also absent: COL6A2, PLAT, PTN; co-absent with the target |
| [[SEMA5A]] | C | SEMA5A activity raises THBS2's level | lines that do not express SEMA5A (28) vs lines expressing it (22) | 3.99× lower at baseline in the lines without SEMA5A | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SNHG18, C5orf46, AMPH; co-absent with the target |
| [[SPOCK1]] | C | SPOCK1 activity raises THBS2's level | lines that do not express SPOCK1 (29) vs lines expressing it (21) | 3.30× lower at baseline in the lines without SPOCK1 | 0.023 | ⚠ within organs, on part of the lines; also absent: SRGN, ENSG00000280241, TEX41; co-absent with the target |
| [[COL1A1]] | C | COL1A1 activity raises THBS2's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 3.93× lower at baseline in the lines without COL1A1 | 0.023 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; co-absent with the target |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 6, C 33. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SYTL3]] | B | THBS2 activity raises SYTL3's level | lines that do not express THBS2 (37) vs lines expressing it (13) | 3.42× lower at baseline in the lines without THBS2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SPARC, ENSG00000254337, ITGA4 |
| [[NAV1]] | B | THBS2 activity raises NAV1's level | lines that do not express THBS2 (37) vs lines expressing it (13) | 3.55× lower at baseline in the lines without THBS2 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SPARC, ENSG00000254337, ITGA4 |
| [[THBS2-AS1]] | B | THBS2 activity raises THBS2-AS1's level | lines that do not express THBS2 (37) vs lines expressing it (13) | 1.67× lower at baseline in the lines without THBS2 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SPARC, ENSG00000254337, ITGA4 |
| [[LRIG1]] | B | THBS2 activity raises LRIG1's level | lines that do not express THBS2 (37) vs lines expressing it (13) | 2.05× lower at baseline in the lines without THBS2 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SPARC, ENSG00000254337, ITGA4 |
| [[SARDH]] | B | THBS2 activity raises SARDH's level | lines that do not express THBS2 (37) vs lines expressing it (13) | 1.89× lower at baseline in the lines without THBS2 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SPARC, ENSG00000254337, ITGA4 |
| [[PPFIBP1]] | B | THBS2 activity raises PPFIBP1's level | lines that do not express THBS2 (37) vs lines expressing it (13) | 1.43× lower at baseline in the lines without THBS2 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SPARC, ENSG00000254337, ITGA4 |
| [[HS3ST3A1]] | C | THBS2 activity raises HS3ST3A1's level | lines that do not express THBS2 (37) vs lines expressing it (13) | 8.38× lower at baseline in the lines without THBS2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SPARC, ENSG00000254337, ITGA4; co-absent with the target |
| [[COL6A1]] | C | THBS2 activity raises COL6A1's level | lines that do not express THBS2 (37) vs lines expressing it (13) | 5.51× lower at baseline in the lines without THBS2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SPARC, ENSG00000254337, ITGA4; co-absent with the target |
| [[GDNF]] | C | THBS2 activity raises GDNF's level | lines that do not express THBS2 (37) vs lines expressing it (13) | 4.09× lower at baseline in the lines without THBS2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SPARC, ENSG00000254337, ITGA4; co-absent with the target |
| [[LINC01411]] | C | THBS2 activity raises LINC01411's level | lines that do not express THBS2 (37) vs lines expressing it (13) | 4.33× lower at baseline in the lines without THBS2 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SPARC, ENSG00000254337, ITGA4; co-absent with the target |
| [[PDGFRB]] | C | THBS2 activity raises PDGFRB's level | lines that do not express THBS2 (37) vs lines expressing it (13) | 5.01× lower at baseline in the lines without THBS2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SPARC, ENSG00000254337, ITGA4; co-absent with the target |
| [[INSYN2B]] | C | THBS2 activity raises INSYN2B's level | lines that do not express THBS2 (37) vs lines expressing it (13) | 4.86× lower at baseline in the lines without THBS2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: SPARC, ENSG00000254337, ITGA4; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.739). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (53.6, 18.2); signed map (24.9, 45.8). **Vector** length 47.9, 18.9% of its response variance represented; |z| ≥ 3 in 247 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Extracellular matrix organization* (reactome, mean cos +0.51 to 22); *Collagen formation* (reactome, mean cos +0.57 to 12); *Assembly of collagen fibrils and other multimeric structures* (reactome, mean cos +0.58 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +13.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.9 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.7 | +8.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +5.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.5 | +0.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | +0.7 | +0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.6 | +0.0 |
|  | [[Flutamide (drug)]] 5 µM |  | +0.6 | +0.7 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +0.5 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.9 | -7.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.7 | -4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.5 | -2.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.2 | -4.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | -1.0 | -1.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -1.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -0.9 | -1.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.7 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | thrombospondin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q27 — chr6:169,215,780-169,254,050 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TSP2 |
| Gene groups (HGNC) | Thrombospondin family |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 8 pathways, smallest: Defective B3GALTL causes PpS; O-glycosylation of TSR domain-containing proteins; Signaling by PDGF |
| Matched by | ensembl_id |

**Function**, from UniProt [P35442](https://www.uniprot.org/uniprotkb/P35442) (Thrombospondin-2):

> Adhesive glycoprotein that mediates cell-to-cell and cell-to-matrix interactions. Ligand for CD36 mediating antiangiogenic properties.

**Summary**, from NCBI Gene [7058](https://www.ncbi.nlm.nih.gov/gene/7058):

> The protein encoded by this gene belongs to the thrombospondin family. It is a disulfide-linked homotrimeric glycoprotein that mediates cell-to-cell and cell-to-matrix interactions. This protein has been shown to function as a potent inhibitor of tumor growth and angiogenesis. Studies of the mouse counterpart suggest that this protein may modulate the cell surface properties of mesenchymal cells and be involved in cell adhesion and migration. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11786](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11786) · Entrez [7058](https://www.ncbi.nlm.nih.gov/gene/7058) · UniProt [P35442](https://www.uniprot.org/uniprotkb/P35442) · Ensembl [ENSG00000186340](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186340)

## Data

Gene col 11806: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11806); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11806, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11806]; `tensor/DDL_lfc|DDL_z.npy` [11806]; `embed/gene_vectors.npy` [11806]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11806 or target_col == 11806). Every well: [[THBS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/THBS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
