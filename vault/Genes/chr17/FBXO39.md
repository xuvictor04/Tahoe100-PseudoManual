---
symbol: "FBXO39"
type: "gene"
col: 10808
ensembl_id: "ENSG00000177294"
name: "F-box protein 39"
location: "17p13.1"
module: 32
arm: "+"
pooled_cpm: 6.53
n_lines_expressing: 34
n_dd_up: 6
n_dd_down: 30
n_dd_up_clean: 4
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 39
direction_downstream: 74
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# FBXO39

*F-box protein 39* — 17p13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.96× (z +7.6, q 2e-11, up in 0 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.55× (z +4.6, q 0.002, up in 9 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (2 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.203× (z -11.5, q 8e-28, down in 25 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NRIR]] (+0.90, fdr 7e-06), [[OAS2]] (+0.87, fdr 7e-06), [[CMPK2]] (+0.87, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 39 arrows point to it, the strongest [[LINC02015]] → it (grade B ⚠); 74 go from it, the strongest it → [[PLSCR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10808.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.96×** | +7.6 | 2e-11 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +4.6 | 0.002 | 9/26 (AsPC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.88×** | +4.3 | 0.004 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.72×** | +4.0 | 0.010 | 8/26 (SW 900, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.68×** | +3.8 | 0.018 | 12/31 (A498, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.60×** | +3.4 | 0.059 | 10/32 (A498, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10808.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.203×** | -11.5 | 8e-28 | 25/30 (LoVo, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.330×** | -8.0 | 5e-13 | 22/28 (LoVo, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.463×** | -7.8 | 1e-12 | 21/31 (CFPAC-1, COLO 205, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.344×** | -7.7 | 2e-12 | 30/31 (COLO 205, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.515×** | -6.7 | 2e-09 | 23/31 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.520×** | -6.6 | 3e-09 | 25/31 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.412×** | -6.4 | 2e-08 | 22/30 (LoVo, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.450×** | -5.7 | 7e-07 | 20/31 (LoVo, HepG2/C3A, …) | top dose only |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.465×** | -5.5 | 3e-06 | 17/28 (HepG2/C3A, LoVo, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.467×** | -5.5 | 3e-06 | 20/30 (Hs 766T, SNU-423, …) | two highest doses |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.481×** | -5.2 | 8e-06 | 18/28 (KATO III, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.539×** | -4.4 | 5e-04 | 17/31 (LoVo, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.553×** | -4.2 | 1e-03 | 12/30 (BT-474, LoVo, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.564×** | -4.1 | 0.002 | 16/30 (BT-474, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.674×** | -4.0 | 0.003 | 14/25 (COLO 205, HepG2/C3A, …) | top dose only | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **0.360×** | -3.8 | 0.004 | 15/29 (Hs 766T, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.31 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10808. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 22.2 | 0 | 13 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0173× (z -18.6) |
| [[CFPAC-1 (line)]] | alt | 31.7 | 0 | 8 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0358× (z -14.9) ⚠ toxic; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.0605× (z -13.0) |
| [[COLO 205 (line)]] | alt | 86.7 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0409× (z -14.2) |
| [[HepG2_C3A (line)]] | wt | 9.90 | 0 | 5 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0182× (z -11.3) |
| [[BT-474 (line)]] | alt | 6.92 | 0 | 4 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0337× (z -9.6) |
| [[Hs 766T (line)]] | wt | 11.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0712× (z -9.3) |
| [[A498 (line)]] | wt | 32.5 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0321× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0939× (z -10.1) |
| [[KATO III (line)]] | alt | 4.60 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0317× (z -11.6) |
| [[SNU-423 (line)]] | alt | 10.4 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.0272× (z -12.0) |
| [[HS-578T (line)]] | alt | 3.02 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 46.0× (z +9.3) | — |
| [[RPMI-7951 (line)]] | alt | 17.0 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0733× (z -8.8) |
| [[A-172 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.573 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.776 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.837 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.55 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.87 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.844 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.783 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.90 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.15 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.670 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.746 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.890 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 7.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.845 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.687 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10808), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NRIR]] | +0.90 | +0.83 / +0.89 | both halves | 7e-06 | **novel candidate** |
| [[OAS2]] | +0.87 | +0.79 / +0.88 | both halves | 7e-06 |  |
| [[CMPK2]] | +0.87 | +0.78 / +0.88 | both halves | 7e-06 |  |
| [[XAF1]] | +0.86 | +0.81 / +0.86 | both halves | 7e-06 | ⚠ same locus (0.6 kb, same strand: neighbours can correlate without regulation) |
| [[MX1]] | +0.86 | +0.77 / +0.88 | both halves | 7e-06 |  |
| [[IFI44]] | +0.85 | +0.74 / +0.87 | both halves | 7e-06 |  |
| [[RSAD2]] | +0.85 | +0.79 / +0.83 | both halves | 7e-06 |  |
| [[MX2]] | +0.84 | +0.73 / +0.86 | both halves | 7e-06 |  |
| [[USP18]] | +0.84 | +0.73 / +0.86 | both halves | 7e-06 |  |
| [[CCDC194]] | +0.84 | +0.84 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[IFI44L]] | +0.84 | +0.70 / +0.86 | both halves | 7e-06 |  |
| [[IFIT3]] | +0.83 | +0.75 / +0.82 | both halves | 7e-06 |  |
| [[OAS1]] | +0.83 | +0.77 / +0.86 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 30, C 9. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02015]] | B | LINC02015 activity raises FBXO39's level | lines that do not express LINC02015 (27) vs lines expressing it (23) | 1.94× lower at baseline in the lines without LINC02015 | 0.001 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, CRLF2, PXDN |
| [[TNFSF14]] | B | TNFSF14 activity raises FBXO39's level | lines that do not express TNFSF14 (34) vs lines expressing it (16) | 2.55× lower at baseline in the lines without TNFSF14 | 0.002 | ⚠ within organs, on part of the lines; also absent: C3, ENSG00000286546, CP; maybe low, not absent |
| [[MMP13]] | B | MMP13 activity raises FBXO39's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 2.29× lower at baseline in the lines without MMP13 | 0.003 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[FGB]] | B | FGB activity raises FBXO39's level | lines that do not express FGB (42) vs lines expressing it (8) | 2.53× lower at baseline in the lines without FGB | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2 |
| [[CP]] | B | CP activity raises FBXO39's level | lines that do not express CP (39) vs lines expressing it (11) | 2.25× lower at baseline in the lines without CP | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB |
| [[MX1]] | B | MX1 activity raises FBXO39's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.34× lower at baseline in the lines without MX1 | 0.020 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[EPSTI1]] | B | EPSTI1 activity raises FBXO39's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 2.67× lower at baseline in the lines without EPSTI1 | 0.023 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[SAMD9L]] | B | SAMD9L activity raises FBXO39's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 2.38× lower at baseline in the lines without SAMD9L | 0.023 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[BST2]] | B | BST2 activity raises FBXO39's level | lines that do not express BST2 (18) vs lines expressing it (32) | 2.65× lower at baseline in the lines without BST2 | 0.024 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[IDO1]] | B | IDO1 activity raises FBXO39's level | lines that do not express IDO1 (28) vs lines expressing it (22) | 1.74× lower at baseline in the lines without IDO1 | 0.032 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, DKK3 |
| [[ALDH1A2]] | B | ALDH1A2 activity raises FBXO39's level | lines that do not express ALDH1A2 (13) vs lines expressing it (37) | 2.50× lower at baseline in the lines without ALDH1A2 | 0.036 | ⚠ within organs, on part of the lines; also absent: SH3TC1, GBP2, CCDC194; maybe low, not absent |
| [[OAS1]] | B | OAS1 activity raises FBXO39's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.33× lower at baseline in the lines without OAS1 | 0.038 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |

### Downstream of this gene

*74 arrows, 74 of them with an alert ⚠; grade A 0, B 65, C 9. Shown: the 12 strongest; 62 more arrows (62 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLSCR1]] | B | FBXO39 activity raises PLSCR1's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 2.56× lower at baseline in the lines without FBXO39 | 0.002 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[IRF9]] | B | FBXO39 activity raises IRF9's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 2.03× lower at baseline in the lines without FBXO39 | 0.003 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[REC8]] | B | FBXO39 activity raises REC8's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 1.77× lower at baseline in the lines without FBXO39 | 0.003 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[PARP9]] | B | FBXO39 activity raises PARP9's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 2.37× lower at baseline in the lines without FBXO39 | 0.004 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[OAS3]] | B | FBXO39 activity raises OAS3's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 2.58× lower at baseline in the lines without FBXO39 | 0.004 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[OAS1]] | B | FBXO39 activity raises OAS1's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 2.80× lower at baseline in the lines without FBXO39 | 0.005 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[IFIT5]] | B | FBXO39 activity raises IFIT5's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 1.87× lower at baseline in the lines without FBXO39 | 0.007 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[USP18]] | B | FBXO39 activity raises USP18's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 2.17× lower at baseline in the lines without FBXO39 | 0.007 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[CMPK2]] | B | FBXO39 activity raises CMPK2's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 2.59× lower at baseline in the lines without FBXO39 | 0.008 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[IFI27]] | B | FBXO39 activity raises IFI27's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 3.33× lower at baseline in the lines without FBXO39 | 0.010 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[PML]] | B | FBXO39 activity raises PML's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 1.89× lower at baseline in the lines without FBXO39 | 0.010 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[LAP3]] | B | FBXO39 activity raises LAP3's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 1.70× lower at baseline in the lines without FBXO39 | 0.010 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.866). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.6, 53.7); signed map (64.9, 31.5). **Vector** length 91.9, 23.1% of its response variance represented; |z| ≥ 3 in 1,060 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.71 to 56); *interferon gamma response* (hallmark, mean cos +0.73 to 60); *interferon* (control, mean cos +0.81 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.8 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +2.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Docetaxel (drug)]] 5 µM |  | +1.6 | +1.9 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | +1.5 | +2.7 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -5.1 | -6.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.4 | -6.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.3 | -5.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.0 | -5.7 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.9 | -5.2 |

## What is on record

|  |  |
|---|---|
| Name | F-box protein 39 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17p13.1 — chr17:6,776,215-6,797,101 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC35179, Fbx39, CT144 |
| Gene groups (HGNC) | F-boxes other |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N4B4](https://www.uniprot.org/uniprotkb/Q8N4B4) (F-box only protein 39):

> Testis-enriched substrate-recognition component of the SCF (SKP1-CUL1-F-box protein)-type E3 ubiquitin ligase complex. Acts as a critical regulator of spermatogenesis, maintaining mitochondrial homeostasis to inhibit ferroptotic cell death. Mechanistically, targets lysine-specific demethylase 5A (KDM5A) for ubiquitin-dependent degradation.

**Summary**, from NCBI Gene [162517](https://www.ncbi.nlm.nih.gov/gene/162517):

> Members of the F-box protein family, such as FBXO39, are characterized by an approximately 40-amino acid F-box motif. SCF complexes, formed by SKP1 (MIM 601434), cullin (see CUL1; MIM 603134), and F-box proteins, act as protein-ubiquitin ligases. F-box proteins interact with SKP1 through the F box, and they interact with ubiquitination targets through other protein interaction domains (Jin et al., 2004 [PubMed 15520277]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:28565](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28565) · Entrez [162517](https://www.ncbi.nlm.nih.gov/gene/162517) · UniProt [Q8N4B4](https://www.uniprot.org/uniprotkb/Q8N4B4) · Ensembl [ENSG00000177294](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177294)

## Data

Gene col 10808: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10808); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10808, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10808]; `tensor/DDL_lfc|DDL_z.npy` [10808]; `embed/gene_vectors.npy` [10808]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10808 or target_col == 10808). Every well: [[FBXO39 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FBXO39.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
