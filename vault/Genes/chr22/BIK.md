---
symbol: "BIK"
type: "gene"
col: 1913
ensembl_id: "ENSG00000100290"
name: "BCL2 interacting killer"
location: "22q13.2"
module: 162
arm: "+"
pooled_cpm: 8.44
n_lines_expressing: 35
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 13
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 15
direction_downstream: 18
tags: ["gene", "module/162"]
generated_by: "tahoemap"
---

# BIK

*BCL2 interacting killer* — 22q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.66× (z +14.7, q 0e+00, up in 20 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 0.5 µM: 0.637× (z -4.8, q 8e-04, down in 19 of 31 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CNNM4]] (+0.67, fdr 8e-06), [[EPHB3]] (+0.66, fdr 1e-05), [[AHDC1]] (+0.64, fdr 4e-05); moves opposite to [[NAF1]] (-0.62, fdr 1e-05), [[TIMM23B-AGAP6]] (-0.61, fdr 1e-05), [[CERS2]] (-0.61, fdr 2e-05).
> It is in [[Module 162]], a single-armed module (estrogen response late).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[MPZL3]] → it (grade B ⚠); 18 go from it, the strongest it → [[NUDT11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1913.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.66×** | +14.7 | 0e+00 | 20/25 (HOP62, C32, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.40×** | +13.2 | 3e-37 | 27/31 (A498, C32, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.98×** | +11.6 | 6e-29 | 18/31 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.98×** | +11.6 | 6e-29 | 22/32 (NCI-H2030, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.62×** | +10.3 | 1e-22 | 24/32 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.04×** | +7.6 | 3e-12 | 16/32 (LoVo, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.99×** | +7.3 | 2e-11 | 21/30 (A498, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +6.0 | 1e-07 | 10/22 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.72×** | +5.6 | 2e-06 | 13/32 (LS 180, NCI-H2347, …) | top dose only | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.65×** | +5.3 | 7e-06 | 13/26 (C32, COLO 205, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.65×** | +3.8 | 0.007 | 10/24 (Panc 03.27, HEC-1-A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.42×** | +3.7 | 0.008 | 2/21 (A498, A549) | inconsistent across doses | composition shift; position effect removed |
| [[Nimesulide (drug)]] 5 µM | ⚠ toxic; unreliable plate only | **1.39×** | +3.5 | 0.020 | 3/30 (A-427, HEC-1-A, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.030 | 8/29 (RKO, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.55×** | +3.3 | 0.030 | 7/29 (SW480, KATO III, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.55×** | +3.3 | 0.030 | 4/30 (CFPAC-1, SK-MEL-2, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.53×** | +3.2 | 0.043 | 7/29 (SW480, LS 180, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1913.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.637×** | -4.8 | 8e-04 | 19/31 (NCI-H2030, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.644×** | -4.7 | 8e-04 | 19/31 (LoVo, Hs 766T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.651×** | -4.6 | 8e-04 | 15/31 (Hs 766T, HepG2/C3A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.654×** | -4.5 | 8e-04 | 10/31 (HCT15, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 0.736× | -3.1 | 0.17 | 12/26 (HCT15, A549, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.746× | -3.1 | 0.17 | 9/32 (Hs 766T, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1913. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2030 (line)]] | alt | 6.21 | 2 | 2 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 7.70× (z +8.9) | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.0859× (z -10.7) |
| [[CFPAC-1 (line)]] | alt | 60.4 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -11.3) ⚠ cell-cycle shift, explains ~7% of this change |
| [[Hs 766T (line)]] | wt | 12.5 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -10.6) ⚠ cell-cycle shift, explains ~7% of this change |
| [[A498 (line)]] | wt | 2.13 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.71× (z +9.8) | — |
| [[AsPC-1 (line)]] | alt | 13.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +10.1) | — |
| [[C32 (line)]] | wt | 3.08 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.4× (z +10.3) | — |
| [[HepG2_C3A (line)]] | wt | 16.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 2.57 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.2× (z +11.2) | — |
| [[KATO III (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.105× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change |
| [[LS 180 (line)]] | wt | 28.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 6.29 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.78× (z +10.3) | — |
| [[Panc 03.27 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.177× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 2.47 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.33 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 9.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 4.67 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.932 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.21 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.892 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.71 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.684 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.767 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.919 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.61 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.41 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1913), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNNM4]] | +0.67 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[EPHB3]] | +0.66 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[AHDC1]] | +0.64 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[JPT1]] | +0.64 | +0.49 / +0.66 | both halves | 1e-05 |  |
| [[BCORL1]] | +0.63 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[PDGFB]] | +0.63 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[VAV1]] | +0.62 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[ACAP1]] | +0.62 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[PIM3]] | +0.60 | +0.56 / +0.55 | both halves | 1e-05 |  |
| [[CCDC88B]] | +0.60 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[CTR9]] | +0.60 | +0.50 / +0.61 | both halves | 1e-05 |  |
| [[ABCB9]] | +0.59 | +0.37 / +0.61 | both halves | 7e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NAF1]] | -0.62 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[TIMM23B-AGAP6]] | -0.61 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[CERS2]] | -0.61 | -0.48 / -0.56 | both halves | 2e-05 |  |
| [[MAPKAPK5]] | -0.60 | -0.30 / -0.67 | both halves | 2e-04 |  |
| [[MCM3AP]] | -0.59 | -0.29 / -0.62 | both halves | 2e-04 |  |
| [[HCFC1]] | -0.58 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[ABCF2]] | -0.58 | -0.39 / -0.53 | both halves | 6e-05 |  |
| [[NAA50]] | -0.58 | -0.49 / -0.51 | both halves | 1e-05 |  |
| [[STMP1]] | -0.57 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[TRNT1]] | -0.57 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[TMX3]] | -0.57 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[EIF3F]] | -0.56 | -0.38 / -0.53 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 15, C 0. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPZL3]] | B | MPZL3 activity raises BIK's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 3.22× lower at baseline in the lines without MPZL3 | 4e-04 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[RNF223]] | B | RNF223 activity raises BIK's level | lines that do not express RNF223 (28) vs lines expressing it (22) | 3.73× lower at baseline in the lines without RNF223 | 0.002 | ⚠ within organs, on part of the lines; also absent: CDH1, IRF6, MPZL2 |
| [[PTAFR]] | B | PTAFR activity raises BIK's level | lines that do not express PTAFR (29) vs lines expressing it (21) | 3.25× lower at baseline in the lines without PTAFR | 0.002 | ⚠ within organs, on part of the lines; also absent: TJP3, BSPRY, KDF1; maybe low, not absent |
| [[SPNS2]] | B | SPNS2 activity raises BIK's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 2.82× lower at baseline in the lines without SPNS2 | 0.005 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N |
| [[CGN]] | B | CGN activity raises BIK's level | lines that do not express CGN (21) vs lines expressing it (29) | 2.86× lower at baseline in the lines without CGN | 0.012 | ⚠ within organs, on part of the lines; also absent: SPINT1-AS1, CRACDL, CAMSAP3 |
| [[CDC42BPG]] | B | CDC42BPG activity raises BIK's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 2.90× lower at baseline in the lines without CDC42BPG | 0.013 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[KCNK5]] | B | KCNK5 activity raises BIK's level | lines that do not express KCNK5 (22) vs lines expressing it (28) | 2.89× lower at baseline in the lines without KCNK5 | 0.017 | ⚠ within organs, on part of the lines; also absent: ENSG00000267748, SLC52A3, SPINT2 |
| [[KRT19]] | B | KRT19 activity raises BIK's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 2.94× lower at baseline in the lines without KRT19 | 0.041 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4 |
| [[CAMSAP3]] | B | CAMSAP3 activity raises BIK's level | lines that do not express CAMSAP3 (16) vs lines expressing it (34) | 2.67× lower at baseline in the lines without CAMSAP3 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CGN, FGFR4, UNC5A; maybe low, not absent |
| [[EPHB3]] | B | EPHB3 activity raises BIK's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 1.96× lower at baseline in the lines without EPHB3 | 0.050 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| [[ESPN]] | B | ESPN activity raises BIK's level | lines that do not express ESPN (26) vs lines expressing it (24) | 2.24× lower at baseline in the lines without ESPN | 0.053 | ⚠ within organs, on part of the lines; also absent: B3GNT7, HSD17B2, FXYD3 |
| [[PDGFB]] | B | PDGFB activity raises BIK's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 1.94× lower at baseline in the lines without PDGFB | 0.074 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 18, C 0. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NUDT11]] | B | BIK activity lowers NUDT11's level | lines that do not express BIK (15) vs lines expressing it (35) | 2.47× higher at baseline in the lines without BIK | 0.012 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3 |
| [[L3HYPDH]] | B | BIK activity lowers L3HYPDH's level | lines that do not express BIK (15) vs lines expressing it (35) | 1.73× higher at baseline in the lines without BIK | 0.017 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3 |
| [[TMX3]] | B | BIK activity lowers TMX3's level | lines that do not express BIK (15) vs lines expressing it (35) | 1.67× higher at baseline in the lines without BIK | 0.019 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3 |
| [[PPP1R13B]] | B | BIK activity raises PPP1R13B's level | lines that do not express BIK (15) vs lines expressing it (35) | 1.70× lower at baseline in the lines without BIK | 0.022 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3 |
| [[ABTB2]] | B | BIK activity raises ABTB2's level | lines that do not express BIK (15) vs lines expressing it (35) | 2.25× lower at baseline in the lines without BIK | 0.024 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3 |
| [[CAMSAP3]] | B | BIK activity raises CAMSAP3's level | lines that do not express BIK (15) vs lines expressing it (35) | 2.78× lower at baseline in the lines without BIK | 0.049 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3 |
| [[NOS1AP]] | B | BIK activity raises NOS1AP's level | lines that do not express BIK (15) vs lines expressing it (35) | 2.20× lower at baseline in the lines without BIK | 0.058 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3 |
| [[CDC42BPG]] | B | BIK activity raises CDC42BPG's level | lines that do not express BIK (15) vs lines expressing it (35) | 2.80× lower at baseline in the lines without BIK | 0.064 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3 |
| [[NEDD9]] | B | BIK activity raises NEDD9's level | lines that do not express BIK (15) vs lines expressing it (35) | 2.36× lower at baseline in the lines without BIK | 0.064 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3 |
| [[LIMK2]] | B | BIK activity strengthens LIMK2's drug response | lines that do not express BIK (15) vs lines expressing it (33) | the lines without BIK respond 0.96× as strongly (z diff +0.08); strongest at Belinostat 5 µM: 1.29x vs 1.69x (z diff +2.0) | 0.072 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3; target measured in part of the lines; both ways; artifact flags |
| [[RAB11FIP1]] | B | BIK activity raises RAB11FIP1's level | lines that do not express BIK (15) vs lines expressing it (35) | 2.35× lower at baseline in the lines without BIK | 0.082 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3 |
| cells under [[Peretinoin (drug)]] 5 µM | B | BIK activity raises the cells' numbers under Peretinoin 5 µM (protects the cells) | lines that do not express BIK (15) vs lines expressing it (33) | the lines without BIK: 0.81× the cells of the other lines | 0.084 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3 |

## Where it sits

- **Module**: [[Module 162]] — estrogen response late; 26 genes; every member is in the + arm (projection on the module's main direction 0.598). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.9, -6.3); signed map (-1.9, 25.6). **Vector** length 66.0, 14.4% of its response variance represented; |z| ≥ 3 in 656 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +13.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.9 | +14.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.7 | +7.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +2.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +1.5 | +3.3 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.5 | -4.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -3.0 | -4.5 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.6 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.5 | -4.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.6 | -0.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -1.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | BCL2 interacting killer |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.2 — chr22:43,110,750-43,129,712 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NBK |
| Gene groups (HGNC) | BCL2 homology region 3 (BH3) only |
| Hallmark sets | APOPTOSIS, GLYCOLYSIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13323](https://www.uniprot.org/uniprotkb/Q13323) (Bcl-2-interacting killer):

> Accelerates programmed cell death. Association to the apoptosis repressors Bcl-X(L), BHRF1, Bcl-2 or its adenovirus homolog E1B 19k protein suppresses this death-promoting activity. Does not interact with BAX.

**Summary**, from NCBI Gene [638](https://www.ncbi.nlm.nih.gov/gene/638):

> The protein encoded by this gene shares a critical BH3 domain with other death-promoting proteins, such as BID, BAK, BAD and BAX, that is required for its pro-apoptotic activity, and for interaction with anti-apoptotic members of the BCL2 family, and viral survival-promoting proteins. Since the activity of this protein is suppressed in the presence of survival-promoting proteins, it is suggested as a likely target for anti-apoptotic proteins. [provided by RefSeq, Sep 2011]

**Accessions** — [HGNC:1051](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1051) · Entrez [638](https://www.ncbi.nlm.nih.gov/gene/638) · UniProt [Q13323](https://www.uniprot.org/uniprotkb/Q13323) · Ensembl [ENSG00000100290](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100290)

## Data

Gene col 1913: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1913); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1913, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1913]; `tensor/DDL_lfc|DDL_z.npy` [1913]; `embed/gene_vectors.npy` [1913]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1913 or target_col == 1913). Every well: [[BIK — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BIK.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
