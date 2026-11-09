---
symbol: "ALS2CL"
type: "gene"
col: 10890
ensembl_id: "ENSG00000178038"
name: "ALS2 C-terminal like"
location: "3p21.31"
module: 31
arm: "+"
pooled_cpm: 15.07
n_lines_expressing: 37
n_dd_up: 5
n_dd_down: 21
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 53
direction_downstream: 34
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# ALS2CL

*ALS2 C-terminal like* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 0.5 µM: 1.41× (z +4.6, q 0.002, up in 15 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (12 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.403× (z -6.3, q 1e-07, down in 23 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRYBG2]] (+0.64, fdr 7e-06), [[UNC13D]] (+0.62, fdr 1e-05), [[SEMA3B]] (+0.61, fdr 1e-05); moves opposite to [[IFT81]] (-0.45, fdr 3e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 53 arrows point to it, the strongest [[C1orf116]] → it (grade B ⚠); 34 go from it, the strongest it → [[PPP1R13L]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10890.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.41×** | +4.6 | 0.002 | 15/33 (HCT15, NCI-H1573, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.43×** | +4.5 | 0.002 | 14/33 (SW480, A498, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.35×** | +4.1 | 0.010 | 15/34 (NCI-H1573, SW480, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.012 | 14/34 (SW480, NCI-H1573, …) | two highest doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.49×** | +3.9 | 0.013 | 3/32 (SW1417, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.08× | +3.7 | 0.019 | 2/35 (HOP62, Panc 03.27) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | 1.56× | +3.1 | 0.14 | 3/23 (PANC-1, Panc 03.27, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (drug)]] 5 µM |  | 1.26× | +3.1 | 0.14 | 5/33 (A-172, SW480, …) | top dose only | position effect removed |
| [[Hydroxyurea (drug)]] 0.05 µM |  | 1.28× | +3.1 | 0.14 | 3/33 (NCI-H2347, KATO III, …) | inconsistent across doses | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | 1.25× | +3.0 | 0.14 | 5/32 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 13 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10890.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.403×** | -6.3 | 1e-07 | 23/34 (A549, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.634×** | -6.1 | 3e-07 | 20/34 (LoVo, HEC-1-A, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.431×** | -5.9 | 8e-07 | 18/33 (HOP62, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.699×** | -4.8 | 3e-04 | 15/34 (LoVo, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **0.664×** | -4.7 | 3e-04 | 16/31 (HOP62, A-172, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.704×** | -4.7 | 3e-04 | 19/34 (HEC-1-A, AsPC-1, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.729×** | -4.2 | 0.002 | 15/33 (LoVo, HOP62, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.730×** | -4.2 | 0.002 | 15/34 (LoVo, HEC-1-A, …) | two highest doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.732×** | -4.1 | 0.002 | 11/33 (LoVo, HOP62, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.571×** | -3.9 | 0.005 | 12/31 (Hs 766T, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **0.602×** | -3.5 | 0.021 | 14/32 (LoVo, NCI-H23, …) | top dose only | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~74% of this change | **0.773×** | -3.4 | 0.029 | 19/34 (HEC-1-A, LoVo, …) | top dose only | position effect removed |
| [[Ribociclib (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.774×** | -3.4 | 0.030 | 5/34 (HEC-1-A, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Sulfatinib (drug)]] 5 µM |  | **0.748×** | -3.3 | 0.037 | 11/33 (SW48, LoVo, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.841× | -3.2 | 0.044 | 12/34 (NCI-H1573, HEC-1-A, …) | rises with dose | low cells (technical?) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.630×** | -3.2 | 0.044 | 5/34 (Panc 03.27, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **0.634×** | -3.2 | 0.047 | 7/33 (HEC-1-A, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | **0.774×** | -2.9 | 0.097 | 6/33 (SW1417, J82, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 0.5 µM |  | **0.803×** | -2.9 | 0.097 | 9/33 (HEC-1-A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10890. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 32.9 | 0 | 11 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.254× (z -14.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 78.2 | 0 | 7 (7 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.192× (z -15.8) ⚠ cell-cycle shift, explains ~48% of this change |
| [[Hs 766T (line)]] | wt | 45.1 | 0 | 6 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.193× (z -10.8) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[EX229 (drug)]] 5 µM 0.0607× (z -9.6) |
| [[AsPC-1 (line)]] | alt | 37.8 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0703× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 12.2 | 1 (1 ⚠) | 3 (3 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.77× (z +10.0) ⚠ position not correctable | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.122× (z -10.4) ⚠ cell-cycle shift, explains ~53% of this change |
| [[NCI-H1573 (line)]] | alt | 14.8 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -11.7) ⚠ cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 36.6 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -12.4) ⚠ cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 12.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.113× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 40.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.290× (z -8.5) ⚠ cell-cycle shift, explains ~43% of this change |
| [[NCI-H2030 (line)]] | alt | 4.44 | 0 | 1 | — | [[Procainamide (hydrochloride) (drug)]] 0.5 µM 0.0916× (z -9.3) |
| [[SW1417 (line)]] | alt | 32.5 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.228× (z -9.8) ⚠ toxic; cell-cycle shift, explains ~18% of this change |
| [[A-172 (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 7.06 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 4.78 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.78 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.946 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.80 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.97 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.81 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.18 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.86 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.38 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10890), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYBG2]] | +0.64 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[UNC13D]] | +0.62 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[SEMA3B]] | +0.61 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[GJB3]] | +0.59 | +0.64 / +0.57 | both halves | 1e-05 |  |
| [[MST1R]] | +0.58 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[MDFI]] | +0.58 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[ARHGAP27]] | +0.58 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[PSORS1C1]] | +0.56 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[EPS8L1]] | +0.54 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[CLTB]] | +0.54 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[SLC12A4]] | +0.53 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[TMBIM1]] | +0.53 | +0.46 / +0.60 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT81]] | -0.45 | -0.49 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*53 arrows, 53 of them with an alert ⚠; grade A 0, B 51, C 2. Shown: the 12 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1orf116]] | B | C1orf116 activity raises ALS2CL's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 4.82× lower at baseline in the lines without C1orf116 | 0.001 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[C6orf132]] | B | C6orf132 activity raises ALS2CL's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 3.91× lower at baseline in the lines without C6orf132 | 0.001 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1 |
| [[KRT16]] | B | KRT16 activity raises ALS2CL's level | lines that do not express KRT16 (27) vs lines expressing it (23) | 3.27× lower at baseline in the lines without KRT16 | 0.001 | ⚠ within organs, on part of the lines; also absent: TRIM29, LGR6, IRF6 |
| [[LPAR5]] | B | LPAR5 activity raises ALS2CL's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 2.84× lower at baseline in the lines without LPAR5 | 0.003 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[TMPRSS4]] | B | TMPRSS4 activity raises ALS2CL's level | lines that do not express TMPRSS4 (33) vs lines expressing it (17) | 4.29× lower at baseline in the lines without TMPRSS4 | 0.004 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B |
| [[TINAGL1]] | B | TINAGL1 activity raises ALS2CL's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 3.30× lower at baseline in the lines without TINAGL1 | 0.004 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[INAVA]] | B | INAVA activity raises ALS2CL's level | lines that do not express INAVA (29) vs lines expressing it (21) | 3.16× lower at baseline in the lines without INAVA | 0.004 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[P2RY2]] | B | P2RY2 activity raises ALS2CL's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 3.43× lower at baseline in the lines without P2RY2 | 0.005 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223 |
| [[GJB3]] | B | GJB3 activity raises ALS2CL's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 4.47× lower at baseline in the lines without GJB3 | 0.005 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[LINC02582]] | B | LINC02582 activity raises ALS2CL's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 4.65× lower at baseline in the lines without LINC02582 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975 |
| [[B3GNT3]] | B | B3GNT3 activity raises ALS2CL's level | lines that do not express B3GNT3 (31) vs lines expressing it (19) | 3.18× lower at baseline in the lines without B3GNT3 | 0.005 | ⚠ within organs, on part of the lines; also absent: CDH1, INAVA, SLC5A1 |
| [[ITGB4]] | B | ITGB4 activity raises ALS2CL's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 3.77× lower at baseline in the lines without ITGB4 | 0.006 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |

### Downstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 32, C 2. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PPP1R13L]] | B | ALS2CL activity raises PPP1R13L's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 2.62× lower at baseline in the lines without ALS2CL | 0.003 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[EPHA2]] | B | ALS2CL activity raises EPHA2's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 3.33× lower at baseline in the lines without ALS2CL | 0.006 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[CCDC102B]] | B | ALS2CL activity lowers CCDC102B's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 3.65× higher at baseline in the lines without ALS2CL | 0.006 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[VSIR]] | B | ALS2CL activity raises VSIR's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 2.39× lower at baseline in the lines without ALS2CL | 0.010 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[TMCC1]] | B | ALS2CL activity raises TMCC1's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 1.41× lower at baseline in the lines without ALS2CL | 0.011 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[SLC16A5]] | B | ALS2CL activity raises SLC16A5's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 2.96× lower at baseline in the lines without ALS2CL | 0.015 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[ITGB4]] | B | ALS2CL activity raises ITGB4's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 4.93× lower at baseline in the lines without ALS2CL | 0.015 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[ARHGAP27]] | B | ALS2CL activity raises ARHGAP27's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 2.27× lower at baseline in the lines without ALS2CL | 0.017 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[SH3BP2]] | B | ALS2CL activity raises SH3BP2's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 1.69× lower at baseline in the lines without ALS2CL | 0.020 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[BCL2L1-AS1]] | B | ALS2CL activity raises BCL2L1-AS1's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 1.41× lower at baseline in the lines without ALS2CL | 0.024 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[NOXA1]] | B | ALS2CL activity raises NOXA1's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 2.07× lower at baseline in the lines without ALS2CL | 0.025 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[NGEF]] | B | ALS2CL activity raises NGEF's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 2.75× lower at baseline in the lines without ALS2CL | 0.027 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.647). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.7, 53.1); signed map (1.7, 35.8). **Vector** length 86.2, 21.4% of its response variance represented; |z| ≥ 3 in 815 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.4 | -0.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.6 | +3.9 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | +3.2 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +1.8 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +3.2 | +4.1 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +3.0 | +4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +3.9 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.8 | +2.9 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -2.6 | -5.9 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.3 | -2.9 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -2.2 | -1.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.2 | -6.3 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -2.1 | -2.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.0 | -3.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | ALS2 C-terminal like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:46,668,995-46,693,704 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ36525, RN49018, DKFZp686I0110 |
| Gene groups (HGNC) | Dbl family Rho GEFs; VPS9 domain containing; MORN repeat containing |
| Reactome | 4 pathways, smallest: RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q60I27](https://www.uniprot.org/uniprotkb/Q60I27) (ALS2 C-terminal-like protein):

> Acts as a guanine nucleotide exchange factor (GEF) for Rab5 GTPase. Regulates the ALS2-mediated endosome dynamics.

**Summary**, from NCBI Gene [259173](https://www.ncbi.nlm.nih.gov/gene/259173):

> Predicted to enable guanyl-nucleotide exchange factor activity and small GTPase binding activity. Predicted to be involved in endosomal transport. Predicted to act upstream of or within intracellular protein localization. Predicted to be located in cytosol. Predicted to be active in cytoplasmic vesicle. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20605](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20605) · Entrez [259173](https://www.ncbi.nlm.nih.gov/gene/259173) · UniProt [Q60I27](https://www.uniprot.org/uniprotkb/Q60I27) · Ensembl [ENSG00000178038](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178038)

## Data

Gene col 10890: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10890); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10890, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10890]; `tensor/DDL_lfc|DDL_z.npy` [10890]; `embed/gene_vectors.npy` [10890]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10890 or target_col == 10890). Every well: [[ALS2CL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALS2CL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
