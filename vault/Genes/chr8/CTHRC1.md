---
symbol: "CTHRC1"
type: "gene"
col: 9034
ensembl_id: "ENSG00000164932"
name: "collagen triple helix repeat containing 1"
location: "8q22.3"
module: 13
arm: "+"
pooled_cpm: 8.93
n_lines_expressing: 24
n_dd_up: 5
n_dd_down: 14
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 22
direction_downstream: 28
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# CTHRC1

*collagen triple helix repeat containing 1* — 8q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.85× (z +10.5, q 7e-23, up in 7 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.41× (z +5.0, q 8e-05, up in 5 of 18 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 2.16×; ⚠ cell-cycle shift, explains ~82% of this change).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.481× (z -7.6, q 2e-11, down in 17 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRRX1]] (+0.70, fdr 7e-06), [[FRMD4A]] (+0.70, fdr 7e-06), [[SETBP1]] (+0.68, fdr 7e-06).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[STING1]] → it (grade B ⚠); 28 go from it, the strongest it → [[GPR68]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9034.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H2347 2.16×; ⚠ cell-cycle shift, explains ~82% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.85×** | +10.5 | 7e-23 | 7/13 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.42×** | +9.2 | 1e-17 | 8/17 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +7.0 | 5e-10 | 6/15 (SK-MEL-2, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.0 | 8e-05 | 5/18 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.25×** | +3.3 | 0.099 | 4/18 (NCI-H2347, A-172, …) | top dose only | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.38× | +3.2 | 0.11 | 3/17 (NCI-H2347, C32, …) | top dose only | cell-cycle shift (explains ~13% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9034.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.481×** | -7.6 | 2e-11 | 17/20 (NCI-H1792, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.524×** | -6.7 | 5e-09 | 17/21 (hTERT-HPNE, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.526×** | -6.7 | 5e-09 | 16/20 (C32, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.612×** | -5.1 | 5e-05 | 15/19 (HOP62, SNU-423, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.625×** | -4.9 | 1e-04 | 15/19 (SK-MEL-2, C32, …) | inconsistent across doses | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.645×** | -4.5 | 5e-04 | 15/21 (HOP62, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.664×** | -4.3 | 0.002 | 14/19 (SK-MEL-2, hTERT-HPNE, …) | two highest doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.488×** | -3.9 | 0.007 | 14/19 (SK-MEL-2, NCI-H2347, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.700×** | -3.7 | 0.012 | 6/19 (HepG2/C3A, SK-MEL-2, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.690×** | -3.7 | 0.012 | 7/19 (SW 900, HepG2/C3A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.707×** | -3.6 | 0.017 | 13/20 (C32, NCI-H1792, …) | two highest doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.711×** | -3.5 | 0.019 | 7/19 (HOP62, HS-578T, …) | two highest doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.725×** | -3.3 | 0.036 | 11/21 (hTERT-HPNE, HOP62, …) | inconsistent across doses | position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.707×** | -3.3 | 0.036 | 1/21 (NCI-H661) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9034. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 39.9 | 0 | 7 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0734× (z -12.8) |
| [[HOP62 (line)]] | alt | 19.8 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0906× (z -14.8) |
| [[SK-MEL-2 (line)]] | alt | 63.5 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0398× (z -19.9) |
| [[C32 (line)]] | wt | 42.8 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0565× (z -15.2) |
| [[NCI-H1792 (line)]] | alt | 21.5 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0204× (z -21.8) |
| [[hTERT-HPNE (line)]] | wt | 28.6 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0163× (z -19.1) |
| [[RPMI-7951 (line)]] | alt | 56.2 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0948× (z -14.3) |
| [[SNU-423 (line)]] | alt | 29.5 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0607× (z -15.6) |
| [[HS-578T (line)]] | alt | 26.7 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.130× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 39.7 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.16× (z +9.1) ⚠ cell-cycle shift, explains ~82% of this change | [[Panobinostat (drug)]] 0.5 µM 0.296× (z -10.2) |
| [[SHP-77 (line)]] | alt | 16.9 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.148× (z -10.2) |
| [[SW 900 (line)]] | alt | 6.15 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0759× (z -8.5) |
| [[A-172 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.78 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.59 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.24 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.909 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.49 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.25 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.47 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.59 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9034), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRRX1]] | +0.70 | +0.66 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION |
| [[FRMD4A]] | +0.70 | +0.66 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[SETBP1]] | +0.68 | +0.66 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[C10orf90]] | +0.67 | +0.63 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[AEBP1]] | +0.66 | +0.64 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[ANGPTL2]] | +0.66 | +0.64 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[APCDD1L]] | +0.65 | +0.68 / +0.59 | both halves | 7e-06 |  |
| [[COL19A1]] | +0.64 | +0.57 / +0.64 | both halves | 9e-06 |  |
| [[SDC2]] | +0.64 | +0.60 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[IGFBP7]] | +0.64 | +0.60 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[DOCK2]] | +0.63 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[LOXL3]] | +0.63 | +0.61 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 1, C 21. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STING1]] | B | STING1 activity raises CTHRC1's level | lines that do not express STING1 (17) vs lines expressing it (33) | 1.75× lower at baseline in the lines without STING1 | 0.048 | ⚠ within organs, on part of the lines; also absent: MANCR, SATB1, NLRP1 |
| [[TIMP3]] | C | TIMP3 activity raises CTHRC1's level | lines that do not express TIMP3 (33) vs lines expressing it (17) | 3.36× lower at baseline in the lines without TIMP3 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: MGP, HTR1F, AEBP1; co-absent with the target |
| [[LAMA4]] | C | LAMA4 activity raises CTHRC1's level | lines that do not express LAMA4 (27) vs lines expressing it (23) | 2.85× lower at baseline in the lines without LAMA4 | 0.005 | ⚠ within organs, on part of the lines; also absent: SLFN12, ARMCX1, BAALC; co-absent with the target |
| [[EVA1A]] | C | EVA1A activity raises CTHRC1's level | lines that do not express EVA1A (21) vs lines expressing it (29) | 3.19× lower at baseline in the lines without EVA1A | 0.014 | ⚠ within organs, on part of the lines; also absent: NLRP1, MILR1, SNAI2; co-absent with the target |
| [[SHROOM4]] | C | SHROOM4 activity raises CTHRC1's level | lines that do not express SHROOM4 (30) vs lines expressing it (20) | 3.00× lower at baseline in the lines without SHROOM4 | 0.015 | ⚠ within organs, on part of the lines; also absent: CX3CL1, CD74, ENSG00000233539; co-absent with the target |
| [[IGFBP7]] | C | IGFBP7 activity raises CTHRC1's level | lines that do not express IGFBP7 (27) vs lines expressing it (23) | 3.65× lower at baseline in the lines without IGFBP7 | 0.020 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, FN1; co-absent with the target |
| [[GDNF]] | C | GDNF activity raises CTHRC1's level | lines that do not express GDNF (38) vs lines expressing it (12) | 5.64× lower at baseline in the lines without GDNF | 0.023 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ITIH5, TDRD9; co-absent with the target |
| [[CSPG4]] | C | CSPG4 activity raises CTHRC1's level | lines that do not express CSPG4 (31) vs lines expressing it (19) | 2.94× lower at baseline in the lines without CSPG4 | 0.028 | ⚠ within organs, on part of the lines; also absent: MMP2, PCDH18, AEBP1; co-absent with the target |
| [[NAV1]] | C | NAV1 activity raises CTHRC1's level | lines that do not express NAV1 (22) vs lines expressing it (28) | 2.83× lower at baseline in the lines without NAV1 | 0.028 | ⚠ within organs, on part of the lines; also absent: NAV2, ENSG00000287622, CDK15; maybe low, not absent; co-absent with the target |
| [[AEBP1]] | C | AEBP1 activity raises CTHRC1's level | lines that do not express AEBP1 (39) vs lines expressing it (11) | 3.95× lower at baseline in the lines without AEBP1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TYR, FCRLA, LHFPL3-AS1; co-absent with the target |
| [[ITGA11]] | C | ITGA11 activity raises CTHRC1's level | lines that do not express ITGA11 (34) vs lines expressing it (16) | 2.75× lower at baseline in the lines without ITGA11 | 0.045 | ⚠ within organs, on part of the lines; also absent: GYPC, INSYN2B, LINC01411; co-absent with the target |
| [[TNC]] | C | TNC activity raises CTHRC1's level | lines that do not express TNC (23) vs lines expressing it (27) | 2.79× lower at baseline in the lines without TNC | 0.045 | ⚠ within organs, on part of the lines; also absent: RDUR, RFX8, ENSG00000287622; co-absent with the target |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 4, C 24. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR68]] | B | CTHRC1 activity raises GPR68's level | lines that do not express CTHRC1 (26) vs lines expressing it (24) | 2.07× lower at baseline in the lines without CTHRC1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ARMCX1, MAGI2-AS3, ITGA4; maybe low, not absent |
| [[CYGB]] | B | CTHRC1 activity raises CYGB's level | lines that do not express CTHRC1 (26) vs lines expressing it (24) | 2.71× lower at baseline in the lines without CTHRC1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ARMCX1, MAGI2-AS3, ITGA4; maybe low, not absent |
| cells under [[Dinaciclib (drug)]] 5 µM | B | CTHRC1 activity raises the cells' numbers under Dinaciclib 5 µM (protects the cells) | lines that do not express CTHRC1 (26) vs lines expressing it (22) | the lines without CTHRC1: 0.38× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: ARMCX1, MAGI2-AS3, ITGA4; maybe low, not absent |
| [[ZPLD1]] | B | CTHRC1 activity raises ZPLD1's level | lines that do not express CTHRC1 (26) vs lines expressing it (24) | 1.72× lower at baseline in the lines without CTHRC1 | 0.098 | ⚠ within organs, on part of the lines; also absent: ARMCX1, MAGI2-AS3, ITGA4; maybe low, not absent |
| [[NAV1]] | C | CTHRC1 activity raises NAV1's level | lines that do not express CTHRC1 (26) vs lines expressing it (24) | 4.95× lower at baseline in the lines without CTHRC1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ARMCX1, MAGI2-AS3, ITGA4; maybe low, not absent; co-absent with the target |
| [[IGFBP7]] | C | CTHRC1 activity raises IGFBP7's level | lines that do not express CTHRC1 (26) vs lines expressing it (24) | 7.48× lower at baseline in the lines without CTHRC1 | 0.010 | ⚠ within organs, on part of the lines; also absent: ARMCX1, MAGI2-AS3, ITGA4; maybe low, not absent; co-absent with the target |
| [[MAGI2]] | C | CTHRC1 activity raises MAGI2's level | lines that do not express CTHRC1 (26) vs lines expressing it (24) | 7.65× lower at baseline in the lines without CTHRC1 | 0.016 | ⚠ within organs, on part of the lines; also absent: ARMCX1, MAGI2-AS3, ITGA4; maybe low, not absent; co-absent with the target |
| [[MMP14]] | C | CTHRC1 activity raises MMP14's level | lines that do not express CTHRC1 (26) vs lines expressing it (24) | 5.54× lower at baseline in the lines without CTHRC1 | 0.022 | ⚠ within organs, on part of the lines; also absent: ARMCX1, MAGI2-AS3, ITGA4; maybe low, not absent; co-absent with the target |
| [[ITGA11]] | C | CTHRC1 activity raises ITGA11's level | lines that do not express CTHRC1 (26) vs lines expressing it (24) | 4.84× lower at baseline in the lines without CTHRC1 | 0.031 | ⚠ within organs, on part of the lines; also absent: ARMCX1, MAGI2-AS3, ITGA4; maybe low, not absent; co-absent with the target |
| [[FRMD4A]] | C | CTHRC1 activity raises FRMD4A's level | lines that do not express CTHRC1 (26) vs lines expressing it (24) | 4.94× lower at baseline in the lines without CTHRC1 | 0.032 | ⚠ within organs, on part of the lines; also absent: ARMCX1, MAGI2-AS3, ITGA4; maybe low, not absent; co-absent with the target |
| [[DENND2A]] | C | CTHRC1 activity raises DENND2A's level | lines that do not express CTHRC1 (26) vs lines expressing it (24) | 2.81× lower at baseline in the lines without CTHRC1 | 0.033 | ⚠ within organs, on part of the lines; also absent: ARMCX1, MAGI2-AS3, ITGA4; maybe low, not absent; co-absent with the target |
| [[GNG2]] | C | CTHRC1 activity raises GNG2's level | lines that do not express CTHRC1 (26) vs lines expressing it (24) | 4.19× lower at baseline in the lines without CTHRC1 | 0.033 | ⚠ within organs, on part of the lines; also absent: ARMCX1, MAGI2-AS3, ITGA4; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.648). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.6, 17.4); signed map (27.3, 41.4). **Vector** length 70.9, 21.9% of its response variance represented; |z| ≥ 3 in 579 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.5 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.3 | +10.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +4.9 | +3.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.7 | +7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | -0.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +1.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | -1.2 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.2 | +1.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.2 | +1.2 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -4.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -2.9 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.9 | -3.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -2.8 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.5 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | collagen triple helix repeat containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q22.3 — chr8:103,371,538-103,382,989 (+) |
| Ensembl biotype | protein_coding |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CG8](https://www.uniprot.org/uniprotkb/Q96CG8) (Collagen triple helix repeat-containing protein 1):

> May act as a negative regulator of collagen matrix deposition.

**Summary**, from NCBI Gene [115908](https://www.ncbi.nlm.nih.gov/gene/115908):

> This locus encodes a protein that may play a role in the cellular response to arterial injury through involvement in vascular remodeling. Mutations at this locus have been associated with Barrett esophagus and esophageal adenocarcinoma. Alternatively spliced transcript variants have been described. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:18831](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18831) · Entrez [115908](https://www.ncbi.nlm.nih.gov/gene/115908) · UniProt [Q96CG8](https://www.uniprot.org/uniprotkb/Q96CG8) · Ensembl [ENSG00000164932](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164932)

## Data

Gene col 9034: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9034); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9034, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9034]; `tensor/DDL_lfc|DDL_z.npy` [9034]; `embed/gene_vectors.npy` [9034]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9034 or target_col == 9034). Every well: [[CTHRC1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CTHRC1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
