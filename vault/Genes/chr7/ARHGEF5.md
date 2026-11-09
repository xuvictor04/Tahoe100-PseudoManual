---
symbol: "ARHGEF5"
type: "gene"
col: 562
ensembl_id: "ENSG00000050327"
name: "Rho guanine nucleotide exchange factor 5"
location: "7q35"
module: 31
arm: "+"
pooled_cpm: 8.25
n_lines_expressing: 31
n_dd_up: 1
n_dd_down: 28
n_dd_up_clean: 1
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 54
direction_downstream: 54
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# ARHGEF5

*Rho guanine nucleotide exchange factor 5* — 7q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[XRK3F2 (drug)]] 0.5 µM: 1.69× (z +5.2, q 9e-05, up in 8 of 27 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.246× (z -19.6, q 0e+00, down in 26 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGEF34P]] (+0.86, fdr 7e-06), [[GPR35]] (+0.62, fdr 1e-05), [[B3GNT3]] (+0.62, fdr 7e-06); moves opposite to [[CHD1L]] (-0.56, fdr 3e-05), [[PDE3A]] (-0.50, fdr 2e-04), [[COL1A2]] (-0.47, fdr 3e-04).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 54 arrows point to it, the strongest [[ADCY4]] → it (grade B ⚠); 54 go from it, the strongest it → [[EPS8L1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 562.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.69×** | +5.2 | 9e-05 | 8/27 (LoVo, BT-474, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.39× | +3.3 | 0.21 | 6/27 (LS 180, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.39× | +3.3 | 0.21 | 3/27 (Panc 03.27, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | 1.36× | +3.1 | 0.24 | 4/27 (PANC-1, SW48, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | 1.52× | +3.1 | 0.24 | 4/26 (A498, HT-29, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Bergenin (drug)]] 0.5 µM |  | 1.24× | +3.0 | 0.25 | 7/27 (NCI-H23, SW 900, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 562.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.246×** | -19.6 | 0e+00 | 26/28 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.361×** | -14.3 | 8e-44 | 26/28 (SW480, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.535×** | -12.4 | 4e-33 | 21/26 (LoVo, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.413×** | -12.4 | 4e-33 | 23/28 (SNU-423, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.601×** | -10.1 | 8e-22 | 20/26 (AsPC-1, BT-474, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.533×** | -8.8 | 1e-16 | 21/26 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.534×** | -8.8 | 1e-16 | 18/27 (COLO 205, KATO III, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.552×** | -8.0 | 9e-14 | 16/27 (NCI-H1792, COLO 205, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.628×** | -6.5 | 4e-09 | 17/28 (SW480, HEC-1-A, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.645×** | -6.1 | 5e-08 | 15/28 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.652×** | -6.0 | 1e-07 | 14/27 (RKO, SW48, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.668×** | -5.7 | 8e-07 | 14/28 (COLO 205, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.672×** | -5.4 | 4e-06 | 12/27 (SW1417, SW480, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.494×** | -5.2 | 1e-05 | 13/27 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.664×** | -5.1 | 1e-05 | 11/19 (KATO III, Panc 03.27, …) | all doses, flat | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.787×** | -4.7 | 7e-05 | 14/28 (HEC-1-A, SW 900, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.572×** | -4.1 | 0.001 | 12/26 (Panc 03.27, BT-474, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.818×** | -4.0 | 0.002 | 12/28 (SW480, LoVo, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 562. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 16.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0831× (z -15.5) |
| [[SW480 (line)]] | alt | 15.6 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.194× (z -14.0) |
| [[AsPC-1 (line)]] | alt | 13.5 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.0980× (z -12.1) |
| [[LoVo (line)]] | wt | 18.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.386× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 17.1 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.205× (z -9.6) |
| [[SW 900 (line)]] | alt | 6.56 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0796× (z -8.7) |
| [[BT-474 (line)]] | alt | 12.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -8.5) |
| [[CFPAC-1 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0685× (z -15.6) ⚠ toxic; cell-cycle shift, explains ~31% of this change |
| [[COLO 205 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0903× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 17.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.329× (z -8.6) |
| [[HT-29 (line)]] | alt | 19.6 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.178× (z -11.2) |
| [[NCI-H1792 (line)]] | alt | 7.56 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0561× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 7.90 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0751× (z -10.9) |
| [[RKO (line)]] | wt | 6.38 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0547× (z -10.4) |
| [[SNU-423 (line)]] | alt | 6.13 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0269× (z -14.6) |
| [[SW1417 (line)]] | alt | 20.6 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.289× (z -9.2) |
| [[A-172 (line)]] | wt | 0.742 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 5.50 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.838 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.769 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.838 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.30 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.702 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.899 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.548 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.07 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.889 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.891 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.91 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.650 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.992 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.829 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.836 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 12.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 562), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF34P]] | +0.86 | +0.86 / +0.84 | both halves | 7e-06 | same gene group |
| [[GPR35]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[B3GNT3]] | +0.62 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[EPS8L1]] | +0.61 | +0.64 / +0.54 | both halves | 1e-05 | same gene group |
| [[MST1R]] | +0.61 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[TMPRSS4]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[SDR16C5]] | +0.59 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[FAM83B]] | +0.58 | +0.53 / +0.56 | both halves | 1e-05 | **novel candidate** |
| [[TMC6]] | +0.56 | +0.60 / +0.55 | both halves | 1e-05 |  |
| [[SPINT1]] | +0.56 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[CEACAM1]] | +0.56 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[FAM83E]] | +0.55 | +0.57 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHD1L]] | -0.56 | -0.43 / -0.49 | both halves | 3e-05 |  |
| [[PDE3A]] | -0.50 | -0.55 / -0.30 | both halves | 2e-04 |  |
| [[COL1A2]] | -0.47 | -0.44 / -0.28 | both halves | 3e-04 |  |
| [[TENM2]] | -0.47 | -0.44 / -0.40 | both halves | 5e-05 |  |
| [[LOXL3]] | -0.46 | -0.49 / -0.26 | both halves | 4e-04 |  |
| [[ARHGAP35]] | -0.45 | -0.35 / -0.42 | both halves | 1e-04 | pathway: CDC42 GTPase cycle |
| [[LRP11]] | -0.45 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[KCNE4]] | -0.45 | -0.50 / -0.25 | both halves | 4e-04 |  |
| [[SLC6A6]] | -0.45 | -0.32 / -0.46 | both halves | 2e-04 |  |
| [[LOXL2]] | -0.44 | -0.35 / -0.37 | both halves | 1e-04 |  |
| [[TCF4]] | -0.44 | -0.49 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*54 arrows, 54 of them with an alert ⚠; grade A 0, B 16, C 38. Shown: the 12 strongest; 42 more arrows (42 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADCY4]] | B | ADCY4 activity raises ARHGEF5's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 3.16× lower at baseline in the lines without ADCY4 | 0.006 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5 |
| [[CCDC120]] | B | CCDC120 activity raises ARHGEF5's level | lines that do not express CCDC120 (11) vs lines expressing it (39) | 3.05× lower at baseline in the lines without CCDC120 | 0.016 | ⚠ within organs, on part of the lines; also absent: PARD6B, LMTK3, AP1G2 |
| [[FAM83E]] | B | FAM83E activity raises ARHGEF5's level | lines that do not express FAM83E (11) vs lines expressing it (39) | 2.34× lower at baseline in the lines without FAM83E | 0.020 | ⚠ within organs, on part of the lines; also absent: TFCP2L1, OCLN; maybe low, not absent |
| [[GRAMD2B]] | B | GRAMD2B activity raises ARHGEF5's level | lines that do not express GRAMD2B (15) vs lines expressing it (35) | 3.12× lower at baseline in the lines without GRAMD2B | 0.022 | ⚠ within organs, on part of the lines; also absent: VAMP5, MAPK13, ARHGEF35-AS1 |
| [[EPS8L1]] | B | EPS8L1 activity raises ARHGEF5's level | lines that do not express EPS8L1 (14) vs lines expressing it (36) | 2.29× lower at baseline in the lines without EPS8L1 | 0.034 | ⚠ within organs, on part of the lines; also absent: KIAA0040, IL1RN, MBNL3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises ARHGEF5's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[IQANK1]] | B | IQANK1 activity raises ARHGEF5's level | lines that do not express IQANK1 (18) vs lines expressing it (32) | 2.93× lower at baseline in the lines without IQANK1 | 0.047 | ⚠ within organs, on part of the lines; also absent: LSR, ENTPD2, FAM83H; maybe low, not absent |
| [[UNC13D]] | B | UNC13D activity raises ARHGEF5's level | lines that do not express UNC13D (14) vs lines expressing it (36) | 2.44× lower at baseline in the lines without UNC13D | 0.048 | ⚠ within organs, on part of the lines; also absent: PRAG1, CDS1, VAMP5; maybe low, not absent |
| [[FAM83A]] | B | FAM83A activity raises ARHGEF5's level | lines that do not express FAM83A (37) vs lines expressing it (13) | 1.82× lower at baseline in the lines without FAM83A | 0.050 | ⚠ within organs, on part of the lines; also absent: GSDMC, DAPP1, S100A9 |
| [[DSG3]] | B | DSG3 activity raises ARHGEF5's level | lines that do not express DSG3 (41) vs lines expressing it (9) | 3.47× lower at baseline in the lines without DSG3 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TFF2, TRIM31, NPSR1 |
| [[SLC28A3]] | B | SLC28A3 activity raises ARHGEF5's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 1.68× lower at baseline in the lines without SLC28A3 | 0.060 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14 |
| [[LPAR5]] | B | LPAR5 activity raises ARHGEF5's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 2.06× lower at baseline in the lines without LPAR5 | 0.069 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |

### Downstream of this gene

*54 arrows, 54 of them with an alert ⚠; grade A 0, B 22, C 32. Shown: the 12 strongest; 42 more arrows (42 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPS8L1]] | B | ARHGEF5, [[ARHGEF34P]] activity raises EPS8L1's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 2.90× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[ELMO3]] | B | ARHGEF5, [[ARHGEF34P]] activity raises ELMO3's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 2.23× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[CCDC120]] | B | ARHGEF5, [[ARHGEF34P]] activity raises CCDC120's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 2.36× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[SSH3]] | B | ARHGEF5 activity raises SSH3's level | lines that do not express ARHGEF5 (19) vs lines expressing it (31) | 1.79× lower at baseline in the lines without ARHGEF5 | 0.007 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000284644, ESRP2, GOLT1A |
| [[STEAP1]] | B | ARHGEF5, [[ARHGEF34P]] activity raises STEAP1's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 2.49× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[FAM83E]] | B | ARHGEF5, [[ARHGEF34P]] activity raises FAM83E's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 2.78× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[IQANK1]] | B | ARHGEF5, [[ARHGEF34P]] activity raises IQANK1's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 3.19× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.026 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[GRAMD2B]] | B | ARHGEF5, [[ARHGEF34P]] activity raises GRAMD2B's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 3.47× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[TMEM184A]] | B | ARHGEF5 activity raises TMEM184A's level | lines that do not express ARHGEF5 (19) vs lines expressing it (31) | 2.39× lower at baseline in the lines without ARHGEF5 | 0.032 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000284644, ESRP2, GOLT1A |
| [[PKP3]] | B | ARHGEF5 activity raises PKP3's level | lines that do not express ARHGEF5 (19) vs lines expressing it (31) | 3.21× lower at baseline in the lines without ARHGEF5 | 0.035 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ENSG00000284644, ESRP2, GOLT1A |
| [[ADCY4]] | B | ARHGEF5, [[ARHGEF34P]] activity raises ADCY4's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 2.09× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |
| [[ARHGAP27]] | B | ARHGEF5, [[ARHGEF34P]] activity raises ARHGAP27's level | lines that do not express ARHGEF5, ARHGEF34P (19) vs lines expressing them (31) | 2.36× lower at baseline in the lines without ARHGEF5, ARHGEF34P | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000284644, ESRP2, GOLT1A; co-absent genes |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.639). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.3, 54.6); signed map (57.3, 9.9). **Vector** length 58.9, 13.1% of its response variance represented; |z| ≥ 3 in 583 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.7 | +2.2 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.7 | +1.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | +1.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.5 | +1.7 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.4 | +2.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +1.4 | +2.5 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +5.2 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | -1.3 | -5.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.3 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.3 | -6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.1 | -4.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | -1.1 | -4.8 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.0 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | Rho guanine nucleotide exchange factor 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q35 — chr7:144,355,288-144,380,632 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TIM, TIM1, GEF5, P60 |
| Gene groups (HGNC) | Dbl family Rho GEFs; SH3 domain containing |
| Reactome | 16 pathways, smallest: NRAGE signals death through JNK; G alpha (12/13) signalling events; RHOB GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12774](https://www.uniprot.org/uniprotkb/Q12774) (Rho guanine nucleotide exchange factor 5):

> Guanine nucleotide exchange factor which activates Rho GTPases. Strongly activates RHOA. Also strongly activates RHOB, weakly activates RHOC and RHOG and shows no effect on RHOD, RHOV, RHOQ or RAC1 (By similarity). Involved in regulation of cell shape and actin cytoskeletal organization. Plays a role in actin organization by generating a loss of actin stress fibers and the formation of membrane ruffles and filopodia. Required for SRC-induced podosome formation (By similarity). Involved in …

**Summary**, from NCBI Gene [7984](https://www.ncbi.nlm.nih.gov/gene/7984):

> Rho GTPases play a fundamental role in numerous cellular processes initiated by extracellular stimuli that work through G protein coupled receptors. The encoded protein may form a complex with G proteins and stimulate Rho-dependent signals. This protein may be involved in the control of cytoskeletal organization. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:13209](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13209) · Entrez [7984](https://www.ncbi.nlm.nih.gov/gene/7984) · UniProt [Q12774](https://www.uniprot.org/uniprotkb/Q12774) · Ensembl [ENSG00000050327](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000050327)

## Data

Gene col 562: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 562); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 562, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 562]; `tensor/DDL_lfc|DDL_z.npy` [562]; `embed/gene_vectors.npy` [562]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 562 or target_col == 562). Every well: [[ARHGEF5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
