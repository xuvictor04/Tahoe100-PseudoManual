---
symbol: "FGD1"
type: "gene"
col: 2235
ensembl_id: "ENSG00000102302"
name: "FYVE, RhoGEF and PH domain containing 1"
location: "Xp11.22"
module: 15
arm: "+"
pooled_cpm: 11.11
n_lines_expressing: 41
n_dd_up: 1
n_dd_down: 14
n_dd_up_clean: 1
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 18
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# FGD1

*FYVE, RhoGEF and PH domain containing 1* — Xp11.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.34× (z +7.3, q 2e-10, up in 21 of 36 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 1.95×, A549 3.30×).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.554× (z -14.8, q 0e+00, down in 28 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SMO]] (+0.62, fdr 1e-05), [[PCGF6]] (+0.62, fdr 7e-06), [[P3H3]] (+0.61, fdr 9e-06); moves opposite to [[ZNF474]] (-0.53, fdr 1e-05), [[FGGY]] (-0.49, fdr 3e-05), [[PMFBP1]] (-0.48, fdr 3e-05).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[DZIP1L]] → it (grade B ⚠); 18 go from it, the strongest it → [[HACD3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2235.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H460 1.95×, A549 3.30×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.34×** | +7.3 | 2e-10 | 21/36 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~75% of this change | 1.15× | +3.5 | 0.12 | 8/39 (NCI-H23, LoVo, …) | top dose only | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.21× | +3.4 | 0.15 | 8/38 (NCI-H460, HOP62, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2235.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.554×** | -14.8 | 0e+00 | 28/37 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.522×** | -11.1 | 5e-26 | 25/37 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.554×** | -10.4 | 3e-23 | 21/37 (RKO, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.620×** | -8.5 | 4e-15 | 24/38 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.632×** | -8.1 | 5e-14 | 19/37 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.633×** | -8.1 | 5e-14 | 21/37 (SHP-77, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.732×** | -5.5 | 3e-06 | 17/38 (SHP-77, BT-474, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.597×** | -4.8 | 1e-04 | 12/38 (NCI-H460, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.765×** | -4.7 | 1e-04 | 13/37 (NCI-H460, A-427, …) | two highest doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.816×** | -3.6 | 0.019 | 13/39 (NCI-H460, A-427, …) | inconsistent across doses | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.820×** | -3.5 | 0.024 | 11/37 (NCI-H460, SW48, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.825×** | -3.4 | 0.030 | 12/37 (A-172, A-427, …) | top dose only |  |
| [[Docetaxel (drug)]] 5 µM |  | 0.872× | -3.4 | 0.030 | 6/39 (NCI-H23, NCI-H661, …) | inconsistent across doses |  |
| [[Mozavaptan (drug)]] 0.05 µM |  | **0.823×** | -3.2 | 0.058 | 7/37 (CFPAC-1, A-172, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.718×** | -3.1 | 0.085 | 4/36 (NCI-H2347, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2235. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 23.8 | 1 | 6 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.95× (z +9.3) | [[Homoharringtonine (drug)]] 5 µM 0.362× (z -14.3) |
| [[A-172 (line)]] | wt | 23.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -14.0) |
| [[SHP-77 (line)]] | alt | 58.6 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.371× (z -10.1) |
| [[AN3 CA (line)]] | alt | 67.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.190× (z -9.7) |
| [[C32 (line)]] | wt | 11.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -9.8) |
| [[A-427 (line)]] | wt | 6.40 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.119× (z -9.4) |
| [[A498 (line)]] | wt | 13.1 | 0 | 1 (1 ⚠) | — | [[Torkinib (drug)]] 5 µM 0.0858× (z -9.8) ⚠ toxic |
| [[A549 (line)]] | wt | 9.68 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 15.8 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0827× (z -13.2) ⚠ cell-cycle shift, explains ~52% of this change |
| [[C-33 A (line)]] | alt | 25.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.160× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~43% of this change |
| [[CFPAC-1 (line)]] | alt | 3.55 | 0 | 1 | — | [[Tadalafil (drug)]] 5 µM 0.0736× (z -8.9) |
| [[HOP62 (line)]] | alt | 18.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -13.8) |
| [[hTERT-HPNE (line)]] | wt | 12.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -12.1) |
| [[J82 (line)]] | alt | 9.64 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0767× (z -13.3) ⚠ toxic; cell-cycle shift, explains ~43% of this change |
| [[NCI-H2030 (line)]] | alt | 6.89 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.122× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~94% of this change |
| [[NCI-H23 (line)]] | alt | 7.90 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0900× (z -10.8) |
| [[PANC-1 (line)]] | alt | 9.73 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.303× (z -8.9) |
| [[RKO (line)]] | wt | 17.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0682× (z -15.7) |
| [[SNU-423 (line)]] | alt | 27.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.237× (z -15.4) |
| [[AsPC-1 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.81 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.72 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.75 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.38 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2235), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SMO]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[PCGF6]] | +0.62 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[P3H3]] | +0.61 | +0.59 / +0.57 | both halves | 9e-06 |  |
| [[MSI1]] | +0.60 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[ADCY3]] | +0.59 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[DENND10]] | +0.58 | +0.47 / +0.60 | both halves | 2e-05 |  |
| [[BMPR1A]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[ZNF250]] | +0.56 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[CRTC3]] | +0.56 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[PTPN9]] | +0.56 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[ZNF398]] | +0.55 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[SLC35D1]] | +0.55 | +0.56 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF474]] | -0.53 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[FGGY]] | -0.49 | -0.43 / -0.45 | both halves | 3e-05 |  |
| [[PMFBP1]] | -0.48 | -0.43 / -0.48 | both halves | 3e-05 |  |
| [[SFR1]] | -0.47 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[DARS1]] | -0.47 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[OMA1]] | -0.47 | -0.46 / -0.43 | both halves | 3e-05 |  |
| [[NFKBIZ]] | -0.47 | -0.38 / -0.47 | both halves | 6e-05 |  |
| [[PPP1R10]] | -0.46 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[PABIR1]] | -0.46 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[LINC01239]] | -0.46 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[LRGUK]] | -0.46 | -0.42 / -0.39 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DZIP1L]] | B | DZIP1L activity raises FGD1's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 3.08× lower at baseline in the lines without DZIP1L | 0.040 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[PLEKHO1]] | B | PLEKHO1 activity raises FGD1's level | lines that do not express PLEKHO1 (13) vs lines expressing it (37) | 2.55× lower at baseline in the lines without PLEKHO1 | 0.043 | ⚠ within organs, on part of the lines; also absent: AKT3, ENSG00000285804, ZNF829; maybe low, not absent |
| [[P3H3]] | B | P3H3 activity raises FGD1's level | lines that do not express P3H3 (10) vs lines expressing it (40) | 2.14× lower at baseline in the lines without P3H3 | 0.071 | ⚠ within organs, on part of the lines; also absent: STARD9, GSTA4, CTXN1 |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 18, C 0. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HACD3]] | B | FGD1 activity raises HACD3's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 1.41× lower at baseline in the lines without FGD1 | 0.015 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |
| [[MZT2A]] | B | FGD1 activity raises MZT2A's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 1.38× lower at baseline in the lines without FGD1 | 0.020 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |
| [[DZIP1L]] | B | FGD1 activity raises DZIP1L's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 2.91× lower at baseline in the lines without FGD1 | 0.022 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |
| [[KLHL8]] | B | FGD1 activity raises KLHL8's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 1.18× lower at baseline in the lines without FGD1 | 0.022 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |
| [[POMT1]] | B | FGD1 activity raises POMT1's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 1.29× lower at baseline in the lines without FGD1 | 0.025 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |
| [[RILPL1]] | B | FGD1 activity raises RILPL1's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 2.42× lower at baseline in the lines without FGD1 | 0.037 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |
| [[PLEKHO1]] | B | FGD1 activity raises PLEKHO1's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 2.73× lower at baseline in the lines without FGD1 | 0.037 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |
| [[NENF]] | B | FGD1 activity raises NENF's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 1.52× lower at baseline in the lines without FGD1 | 0.057 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |
| [[ZNF398]] | B | FGD1 activity raises ZNF398's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 1.06× lower at baseline in the lines without FGD1 | 0.067 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |
| [[ADCY3]] | B | FGD1 activity raises ADCY3's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 1.70× lower at baseline in the lines without FGD1 | 0.075 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |
| [[PCGF6]] | B | FGD1 activity raises PCGF6's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 1.43× lower at baseline in the lines without FGD1 | 0.081 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |
| [[TMED8]] | B | FGD1 activity raises TMED8's level | lines that do not express FGD1 (9) vs lines expressing it (41) | 1.40× lower at baseline in the lines without FGD1 | 0.082 | ⚠ within organs, on part of the lines; also absent: CERCAM, CMTM3, CSRP2 |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.365). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-12.4, 18.8); signed map (-26.6, -18.2). **Vector** length 61.5, 10.3% of its response variance represented; |z| ≥ 3 in 726 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +7.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.2 | -0.1 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.9 | +1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.9 | +2.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +0.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.9 | +1.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.6 | +1.5 |
|  | [[EX229 (drug)]] 5 µM |  | +1.5 | +1.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -3.9 | -11.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.7 | -10.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.3 | -8.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.6 | -14.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -3.5 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -1.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.2 | -1.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.2 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | FYVE, RhoGEF and PH domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.22 — chrX:54,445,454-54,496,234 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ZFYVE3; previously FGDY |
| Gene groups (HGNC) | Zinc fingers FYVE-type; Pleckstrin homology domain containing; Dbl family Rho GEFs |
| Reactome | 11 pathways, smallest: NRAGE signals death through JNK; G alpha (12/13) signalling events; Cell death signalling via NRAGE, NRIF and NADE |
| Matched by | ensembl_id |

**Function**, from UniProt [P98174](https://www.uniprot.org/uniprotkb/P98174) (FYVE, RhoGEF and PH domain-containing protein 1):

> Activates CDC42, a member of the Ras-like family of Rho- and Rac proteins, by exchanging bound GDP for free GTP. Plays a role in regulating the actin cytoskeleton and cell shape.

**Summary**, from NCBI Gene [2245](https://www.ncbi.nlm.nih.gov/gene/2245):

> This gene encodes a protein that contains Dbl (DH) and pleckstrin (PH) homology domains and is similar to the Rho family of small GTP-binding proteins. The encoded protein specifically binds to the Rho family GTPase Cdc42Hs and can stimulate the GDP-GTP exchange of the isoprenylated form of Cdc42Hs. It also stimulates the mitogen activated protein kinase cascade leading to c-Jun kinase SAPK/JNK1 activation. Defects in this gene are the cause of the faciogenital dysplasia in Aarskog-Scott …

**Accessions** — [HGNC:3663](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3663) · Entrez [2245](https://www.ncbi.nlm.nih.gov/gene/2245) · UniProt [P98174](https://www.uniprot.org/uniprotkb/P98174) · Ensembl [ENSG00000102302](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102302)

## Data

Gene col 2235: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2235); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2235, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2235]; `tensor/DDL_lfc|DDL_z.npy` [2235]; `embed/gene_vectors.npy` [2235]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2235 or target_col == 2235). Every well: [[FGD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FGD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
