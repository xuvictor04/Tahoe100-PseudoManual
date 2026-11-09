---
symbol: "TMEM200A"
type: "gene"
col: 8954
ensembl_id: "ENSG00000164484"
name: "transmembrane protein 200A"
location: "6q23.1"
module: 13
arm: "+"
pooled_cpm: 12.41
n_lines_expressing: 21
n_dd_up: 6
n_dd_down: 25
n_dd_up_clean: 2
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 33
direction_downstream: 47
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# TMEM200A

*transmembrane protein 200A* — 6q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.01× (z +12.2, q 3e-31, up in 0 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.53× (z +6.9, q 6e-10, up in 0 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (4 with an alert ⚠); the strongest is [[Betamethasone dipropionate (drug)]] 0.5 µM: 0.552× (z -6.8, q 5e-09, down in 13 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAMD3]] (+0.93, fdr 7e-06, ⚠ same locus), [[GPR68]] (+0.76, fdr 7e-06), [[SIGLEC15]] (+0.75, fdr 7e-06), [[INSYN2B]] (+0.74, fdr 7e-06); moves opposite to [[CMKLR2]] (-0.48, fdr 5e-05).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 33 arrows point to it, the strongest [[ARL4C]] → it (grade B ⚠); 47 go from it, the strongest it → [[RFTN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8954.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.01×** | +12.2 | 3e-31 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.01×** | +8.0 | 3e-13 | 0/15 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.08×** | +7.8 | 1e-12 | 0/14 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +6.9 | 6e-10 | 0/16 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +4.1 | 0.005 | 11/17 (LoVo, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.26×** | +3.7 | 0.019 | 2/17 (HepG2/C3A, RPMI-7951) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | 1.22× | +3.2 | 0.11 | 2/19 (HepG2/C3A, RPMI-7951) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 1.46× | +3.1 | 0.12 | 2/13 (J82, NCI-H1792) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Arbutin (drug)]] 0.05 µM |  | 1.34× | +3.1 | 0.12 | 3/18 (SNU-423, A-172, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 1.30× | +3.0 | 0.12 | 1/18 (HepG2/C3A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | 1.32× | +3.0 | 0.12 | 0/17 | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8954.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.552×** | -6.8 | 5e-09 | 13/18 (HOP62, LOX-IMVI, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.571×** | -6.4 | 3e-08 | 11/18 (LOX-IMVI, H4, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **0.584×** | -6.2 | 1e-07 | 13/19 (LOX-IMVI, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.593×** | -6.0 | 3e-07 | 9/19 (HOP62, LOX-IMVI, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.591×** | -5.8 | 7e-07 | 10/18 (J82, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **0.616×** | -5.6 | 2e-06 | 10/19 (HOP62, Panc 03.27, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.635×** | -5.2 | 1e-05 | 8/18 (SHP-77, H4, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.614×** | -5.2 | 1e-05 | 8/18 (HOP62, RPMI-7951, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.739×** | -4.9 | 5e-05 | 11/19 (HOP62, SNU-423, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.653×** | -4.9 | 5e-05 | 10/18 (HOP62, SW 900, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.666×** | -4.7 | 2e-04 | 9/19 (J82, LOX-IMVI, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.672×** | -4.6 | 2e-04 | 8/18 (hTERT-HPNE, H4, …) | all doses, flat |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.673×** | -4.6 | 2e-04 | 6/18 (J82, H4, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.639×** | -4.5 | 3e-04 | 10/18 (HOP62, SHP-77, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.640×** | -4.5 | 3e-04 | 14/18 (LOX-IMVI, HOP62, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8954. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 133 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -16.0) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.217× (z -13.7) |
| [[J82 (line)]] | alt | 7.32 | 0 | 6 (1 ⚠) | — | [[Sulfatinib (drug)]] 5 µM 0.0355× (z -11.5) |
| [[A-172 (line)]] | wt | 20.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -9.0) |
| [[HOP62 (line)]] | alt | 25.0 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.131× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Budesonide (drug)]] 0.05 µM 0.188× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 93.0 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.140× (z -9.5) |
| [[SNU-423 (line)]] | alt | 99.0 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -12.4) |
| [[SW1417 (line)]] | alt | 36.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.143× (z -11.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 26.7 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0964× (z -12.0) |
| [[LS 180 (line)]] | wt | 22.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.156× (z -8.7) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H1792 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.161× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.109× (z -8.9) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A-427 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.842 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.873 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.994 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.887 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.922 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.928 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.780 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.848 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.750 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.854 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.710 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.903 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.705 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.954 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.874 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.59 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.919 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8954), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAMD3]] | +0.93 | +0.91 / +0.92 | both halves | 7e-06 | STRING 441; ⚠ same locus (0.6 kb: neighbours can correlate without regulation) |
| [[GPR68]] | +0.76 | +0.70 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[SIGLEC15]] | +0.75 | +0.72 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[INSYN2B]] | +0.74 | +0.69 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[ADAMTS6]] | +0.72 | +0.67 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[ITGA11]] | +0.71 | +0.70 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[RFX8]] | +0.71 | +0.63 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[FAM167A]] | +0.71 | +0.60 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[ADAMTS12]] | +0.69 | +0.66 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[SPOCD1]] | +0.68 | +0.65 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[APCDD1L]] | +0.67 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[NLRP3]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[NALF1]] | +0.67 | +0.57 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMKLR2]] | -0.48 | -0.39 / -0.55 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 4, C 29. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARL4C]] | B | ARL4C activity raises TMEM200A's level | lines that do not express ARL4C (14) vs lines expressing it (36) | 2.32× lower at baseline in the lines without ARL4C | 0.036 | ⚠ within organs, on part of the lines; also absent: NLRP1, ENSG00000225330, TRPM8 |
| [[LRIG1]] | B | LRIG1 activity raises TMEM200A's level | lines that do not express LRIG1 (11) vs lines expressing it (39) | 3.16× lower at baseline in the lines without LRIG1 | 0.040 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NR3C1]] | B | NR3C1 activity lowers TMEM200A's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.9% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds |
| [[CMKLR2]] | B | CMKLR2 activity raises TMEM200A's level | lines that do not express CMKLR2 (16) vs lines expressing it (34) | 2.66× lower at baseline in the lines without CMKLR2 | 0.059 | ⚠ within organs, on part of the lines; also absent: SATB1-AS1, ENSG00000231772, NYAP2; maybe low, not absent |
| [[SAMD3]] | C | SAMD3 activity raises TMEM200A's level | lines that do not express SAMD3 (32) vs lines expressing it (18) | 9.12× lower at baseline in the lines without SAMD3 | 5e-06 | ⚠ within organs, on part of the lines; also absent: TMEM200A, LINC01615, ITGA11; co-absent with the target |
| [[ADAMTS12]] | C | ADAMTS12 activity raises TMEM200A's level | lines that do not express ADAMTS12 (33) vs lines expressing it (17) | 4.61× lower at baseline in the lines without ADAMTS12 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LINC01411, APBB1IP, VCAM1; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises TMEM200A's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 4.56× lower at baseline in the lines without ITGA11 | 0.005 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[IL1B]] | C | IL1B activity raises TMEM200A's level | lines that do not express IL1B (30) vs lines expressing it (20) | 4.06× lower at baseline in the lines without IL1B | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA; co-absent with the target |
| [[TCF4]] | C | TCF4 activity raises TMEM200A's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 2.99× lower at baseline in the lines without TCF4 | 0.007 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises TMEM200A's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 3.97× lower at baseline in the lines without APCDD1L | 0.007 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[WNT5A]] | C | WNT5A activity raises TMEM200A's level | lines that do not express WNT5A (30) vs lines expressing it (20) | 3.67× lower at baseline in the lines without WNT5A | 0.010 | ⚠ within organs, on part of the lines; also absent: APCDD1L, ABCC9, CDH13; co-absent with the target |
| [[EVA1A]] | C | EVA1A activity raises TMEM200A's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 3.36× lower at baseline in the lines without EVA1A | 0.013 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2; co-absent with the target |

### Downstream of this gene

*47 arrows, 47 of them with an alert ⚠; grade A 0, B 11, C 36. Shown: the 12 strongest; 35 more arrows (35 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RFTN1]] | B | TMEM200A activity raises RFTN1's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 4.01× lower at baseline in the lines without TMEM200A | 7e-04 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615 |
| [[FAM167A]] | B | TMEM200A activity raises FAM167A's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 2.56× lower at baseline in the lines without TMEM200A | 0.003 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615 |
| [[TSHZ3]] | B | TMEM200A activity strengthens TSHZ3's drug response | lines that do not express TMEM200A (11) vs lines expressing it (12) | the lines without TMEM200A respond 0.73× as strongly (z diff +1.03); strongest at Dinaciclib 0.05 µM: 0.53x vs 0.20x (z diff +4.9) | 0.005 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615; target measured in part of the lines; both ways; artifact flags |
| [[LRIG1]] | B | TMEM200A activity raises LRIG1's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 2.73× lower at baseline in the lines without TMEM200A | 0.014 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615 |
| [[DOCK2]] | B | TMEM200A activity raises DOCK2's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 2.27× lower at baseline in the lines without TMEM200A | 0.015 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615 |
| [[ARL4C]] | B | TMEM200A activity raises ARL4C's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 1.77× lower at baseline in the lines without TMEM200A | 0.041 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615 |
| [[GPR68]] | B | TMEM200A activity raises GPR68's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 1.82× lower at baseline in the lines without TMEM200A | 0.051 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615 |
| [[PDE4DIPP2]] | B | TMEM200A activity raises PDE4DIPP2's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 2.08× lower at baseline in the lines without TMEM200A | 0.052 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615 |
| [[NTNG2]] | B | TMEM200A activity raises NTNG2's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 1.83× lower at baseline in the lines without TMEM200A | 0.052 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615 |
| [[LINC01426]] | B | TMEM200A activity raises LINC01426's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 1.66× lower at baseline in the lines without TMEM200A | 0.053 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615 |
| [[BCL11B]] | B | TMEM200A activity strengthens BCL11B's drug response | lines that do not express TMEM200A (19) vs lines expressing it (11) | the lines without TMEM200A respond 0.95× as strongly (z diff +0.14); strongest at Bortezomib 0.05 µM: 0.57x vs 0.35x (z diff +3.0) | 0.070 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615; target measured in part of the lines; both ways; artifact flags |
| [[SAMD3]] | C | TMEM200A activity raises SAMD3's level | lines that do not express TMEM200A (29) vs lines expressing it (21) | 6.89× lower at baseline in the lines without TMEM200A | 8e-05 | ⚠ within organs, on part of the lines; also absent: SAMD3, ITGA11, LINC01615; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.751). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.4, 14.0); signed map (19.8, 47.6). **Vector** length 77.0, 26.7% of its response variance represented; |z| ≥ 3 in 622 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Defective B3GALTL causes PpS* (reactome, mean cos +0.56 to 8); *O-glycosylation of TSR domain-containing proteins* (reactome, mean cos +0.56 to 8); *Diseases of glycosylation* (reactome, mean cos +0.50 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.3 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.7 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +6.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +2.6 | +3.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +1.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | +1.9 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.3 | +3.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.0 | +0.7 |
| fall | [[Triamcinolone (drug)]] 5 µM |  | -2.6 | -4.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.3 | -4.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.3 | -6.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.2 | -5.6 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.2 | -3.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.1 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 200A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q23.1 — chr6:130,366,017-130,443,067 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TTMC; previously KIAA1913 |
| Matched by | ensembl_id |

UniProt [Q86VY9](https://www.uniprot.org/uniprotkb/Q86VY9) carries no function annotation.

**Summary**, from NCBI Gene [114801](https://www.ncbi.nlm.nih.gov/gene/114801):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:21075](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21075) · Entrez [114801](https://www.ncbi.nlm.nih.gov/gene/114801) · UniProt [Q86VY9](https://www.uniprot.org/uniprotkb/Q86VY9) · Ensembl [ENSG00000164484](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164484)

## Data

Gene col 8954: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8954); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8954, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8954]; `tensor/DDL_lfc|DDL_z.npy` [8954]; `embed/gene_vectors.npy` [8954]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8954 or target_col == 8954). Every well: [[TMEM200A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM200A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
