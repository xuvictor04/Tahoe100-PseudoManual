---
symbol: "NGEF"
type: "gene"
col: 822
ensembl_id: "ENSG00000066248"
name: "neuronal guanine nucleotide exchange factor"
location: "2q37.1"
module: 34
arm: "+"
pooled_cpm: 18.16
n_lines_expressing: 38
n_dd_up: 5
n_dd_down: 33
n_dd_up_clean: 1
n_dd_down_clean: 29
in_vector_space: true
direction_upstream: 27
direction_downstream: 11
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# NGEF

*neuronal guanine nucleotide exchange factor* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.49× (z +5.9, q 2e-06, up in 7 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.28× (z +5.4, q 2e-05, up in 11 of 35 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 7.18×).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (4 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.546× (z -8.9, q 3e-16, down in 23 of 31 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEK2]] (+0.64, fdr 7e-06), [[PTK6]] (+0.64, fdr 2e-05), [[TMC6]] (+0.64, fdr 1e-05); moves opposite to [[ATXN7]] (-0.49, fdr 1e-04).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 27 arrows point to it, the strongest [[ITGB4]] → it (grade B ⚠); 11 go from it, the strongest it → [[CDA]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 822.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 0.5 µM in 1 line (RKO 7.18×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +5.9 | 2e-06 | 7/22 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +5.4 | 2e-05 | 11/35 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.39×** | +5.1 | 8e-05 | 7/28 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | 1.19× | +3.8 | 0.017 | 8/35 (CFPAC-1, A-172, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | 1.17× | +3.3 | 0.085 | 4/36 (AsPC-1, MIA PaCa-2, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **1.24×** | +3.3 | 0.085 | 9/33 (SW480, HOP62, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.24×** | +3.3 | 0.088 | 7/32 (NCI-H460, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 822.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.546×** | -8.9 | 3e-16 | 23/31 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.704×** | -7.6 | 1e-11 | 19/34 (HT-29, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.621×** | -7.3 | 6e-11 | 21/35 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.633×** | -7.0 | 4e-10 | 18/35 (LoVo, LS 180, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.654×** | -6.5 | 9e-09 | 19/33 (LS 180, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.681×** | -5.9 | 4e-07 | 21/31 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.685×** | -5.8 | 6e-07 | 16/35 (HT-29, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.686×** | -5.5 | 2e-06 | 16/32 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.692×** | -5.4 | 4e-06 | 17/34 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.771×** | -5.1 | 2e-05 | 13/35 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.792×** | -5.0 | 3e-05 | 16/32 (LS 180, HT-29, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.795×** | -4.8 | 6e-05 | 16/35 (CFPAC-1, NCI-H1573, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.728×** | -4.7 | 1e-04 | 17/32 (LS 180, HT-29, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.759×** | -4.4 | 5e-04 | 12/36 (CFPAC-1, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.792×** | -4.3 | 8e-04 | 11/34 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.767×** | -4.1 | 0.002 | 13/35 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 822. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 87.5 | 0 | 16 (8 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0851× (z -21.4) ⚠ cell-cycle shift, explains ~86% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -19.2) |
| [[HT-29 (line)]] | alt | 55.5 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -18.4) |
| [[A-172 (line)]] | wt | 69.1 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.203× (z -14.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 75.3 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -14.0) |
| [[Hs 766T (line)]] | wt | 35.3 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -14.0) |
| [[KATO III (line)]] | alt | 13.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -13.7) |
| [[SW480 (line)]] | alt | 22.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -11.4) |
| [[CFPAC-1 (line)]] | alt | 43.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -13.4) |
| [[LoVo (line)]] | wt | 12.1 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.114× (z -13.5) |
| [[MIA PaCa-2 (line)]] | alt | 35.4 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.282× (z -10.4) |
| [[A549 (line)]] | wt | 20.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -9.9) |
| [[BT-474 (line)]] | alt | 5.48 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0517× (z -8.9) |
| [[HepG2_C3A (line)]] | wt | 23.3 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0595× (z -12.4) ⚠ cell-cycle shift, explains ~53% of this change |
| [[HOP62 (line)]] | alt | 8.09 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.179× (z -8.7) |
| [[NCI-H460 (line)]] | wt | 15.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0626× (z -17.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 9.89 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 7.18× (z +8.7) | — |
| [[A-427 (line)]] | wt | 5.71 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.39 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.23 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.82 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.16 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.48 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.65 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 822), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEK2]] | +0.64 | +0.65 / +0.59 | both halves | 7e-06 | STRING 509 |
| [[PTK6]] | +0.64 | +0.66 / +0.48 | both halves | 2e-05 | same gene group |
| [[TMC6]] | +0.64 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[SULT2B1]] | +0.62 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[PRSS3]] | +0.62 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[SLC5A1]] | +0.62 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[PLEKHG5]] | +0.61 | +0.59 / +0.54 | both halves | 1e-05 | same gene group; pathway: Cell death signalling via NRAGE, NRIF and NADE |
| [[NECTIN1]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[KRT15]] | +0.59 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[LCK]] | +0.59 | +0.53 / +0.54 | both halves | 1e-05 | same gene group |
| [[PLEKHM1P1]] | +0.59 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[KLK11]] | +0.59 | +0.57 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATXN7]] | -0.49 | -0.52 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 25, C 2. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGB4]] | B | ITGB4 activity raises NGEF's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 3.57× lower at baseline in the lines without ITGB4 | 4e-04 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[LASTR]] | B | LASTR activity raises NGEF's level | lines that do not express LASTR (22) vs lines expressing it (28) | 2.69× lower at baseline in the lines without LASTR | 0.007 | ⚠ within organs, on part of the lines; also absent: TINAGL1, PCSK9, ANXA3; maybe low, not absent |
| [[FA2H]] | B | FA2H activity raises NGEF's level | lines that do not express FA2H (27) vs lines expressing it (23) | 2.55× lower at baseline in the lines without FA2H | 0.009 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2 |
| [[LPAR5]] | B | LPAR5 activity raises NGEF's level | lines that do not express LPAR5 (20) vs lines expressing it (30) | 2.50× lower at baseline in the lines without LPAR5 | 0.009 | ⚠ within organs, on part of the lines; also absent: PTAFR, SCNN1A, ITGB4; maybe low, not absent |
| [[GJB3]] | B | GJB3 activity raises NGEF's level | lines that do not express GJB3 (31) vs lines expressing it (19) | 3.01× lower at baseline in the lines without GJB3 | 0.010 | ⚠ within organs, on part of the lines; also absent: IRF6, COL17A1, KLK10 |
| [[IL2RG]] | B | IL2RG activity raises NGEF's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 2.37× lower at baseline in the lines without IL2RG | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850 |
| [[TINAGL1]] | B | TINAGL1 activity raises NGEF's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 2.72× lower at baseline in the lines without TINAGL1 | 0.015 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[HNF4A]] | B | HNF4A activity raises NGEF's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 2.71× lower at baseline in the lines without HNF4A | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964 |
| [[KLK10]] | B | KLK10 activity raises NGEF's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 2.76× lower at baseline in the lines without KLK10 | 0.025 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6 |
| [[ALS2CL]] | B | ALS2CL activity raises NGEF's level | lines that do not express ALS2CL (13) vs lines expressing it (37) | 2.75× lower at baseline in the lines without ALS2CL | 0.027 | ⚠ within organs, on part of the lines; also absent: KCNK6, LRRK1, CDCP1 |
| [[CDA]] | B | CDA activity raises NGEF's level | lines that do not express CDA (16) vs lines expressing it (34) | 2.41× lower at baseline in the lines without CDA | 0.031 | ⚠ within organs, on part of the lines; also absent: TMEM92, LASTR, KITLG |
| [[SPNS2]] | B | SPNS2 activity raises NGEF's level | lines that do not express SPNS2 (26) vs lines expressing it (24) | 2.33× lower at baseline in the lines without SPNS2 | 0.036 | ⚠ within organs, on part of the lines; also absent: MACC1, CATSPERB, TC2N |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 9, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDA]] | B | NGEF activity raises CDA's level | lines that do not express NGEF (12) vs lines expressing it (38) | 3.77× lower at baseline in the lines without NGEF | 0.005 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TSPAN15, PDGFB |
| [[ITGB4]] | B | NGEF activity raises ITGB4's level | lines that do not express NGEF (12) vs lines expressing it (38) | 6.14× lower at baseline in the lines without NGEF | 0.019 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TSPAN15, PDGFB |
| [[ALS2CL]] | B | NGEF activity raises ALS2CL's level | lines that do not express NGEF (12) vs lines expressing it (38) | 3.38× lower at baseline in the lines without NGEF | 0.055 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TSPAN15, PDGFB |
| [[FA2H]] | B | NGEF activity raises FA2H's level | lines that do not express NGEF (12) vs lines expressing it (38) | 4.42× lower at baseline in the lines without NGEF | 0.067 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TSPAN15, PDGFB |
| [[KIAA1671]] | B | NGEF activity raises KIAA1671's level | lines that do not express NGEF (12) vs lines expressing it (38) | 1.85× lower at baseline in the lines without NGEF | 0.074 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TSPAN15, PDGFB |
| [[TINAGL1]] | B | NGEF activity raises TINAGL1's level | lines that do not express NGEF (12) vs lines expressing it (38) | 4.58× lower at baseline in the lines without NGEF | 0.079 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TSPAN15, PDGFB |
| [[ARHGAP27]] | B | NGEF activity raises ARHGAP27's level | lines that do not express NGEF (12) vs lines expressing it (38) | 2.20× lower at baseline in the lines without NGEF | 0.094 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TSPAN15, PDGFB |
| [[TMC7]] | B | NGEF activity raises TMC7's level | lines that do not express NGEF (12) vs lines expressing it (38) | 2.01× lower at baseline in the lines without NGEF | 0.096 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TSPAN15, PDGFB |
| [[GTF2IP7]] | B | NGEF activity raises GTF2IP7's level | lines that do not express NGEF (12) vs lines expressing it (38) | 1.74× lower at baseline in the lines without NGEF | 0.099 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TSPAN15, PDGFB |
| [[PTK6]] | C | NGEF activity raises PTK6's level | lines that do not express NGEF (12) vs lines expressing it (38) | 2.91× lower at baseline in the lines without NGEF | 0.078 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TSPAN15, PDGFB; co-absent with the target |
| [[ARHGEF16]] | C | NGEF activity raises ARHGEF16's level | lines that do not express NGEF (12) vs lines expressing it (38) | 2.75× lower at baseline in the lines without NGEF | 0.086 | ⚠ within organs, on part of the lines; also absent: TNFRSF10A-DT, TSPAN15, PDGFB; co-absent with the target |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.671). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.5, 54.9); signed map (0.2, 38.9). **Vector** length 89.6, 22.6% of its response variance represented; |z| ≥ 3 in 829 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.3 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +5.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | +6.4 | -0.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +5.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~9% of this change | +5.3 | +3.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.2 | +2.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +0.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.4 | +2.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +2.3 | +3.3 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.6 | -3.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.2 | -7.0 |
|  | [[Trametinib (drug)]] 5 µM |  | -2.9 | -4.4 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.8 | -4.8 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.4 | -3.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -2.3 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | neuronal guanine nucleotide exchange factor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:232,878,701-233,013,256 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARHGEF27 |
| Gene groups (HGNC) | Dbl family Rho GEFs; SH3 domain containing |
| Reactome | 17 pathways, smallest: EPHA-mediated growth cone collapse; NRAGE signals death through JNK; G alpha (12/13) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N5V2](https://www.uniprot.org/uniprotkb/Q8N5V2) (Ephexin-1):

> Acts as a guanine nucleotide exchange factor (GEF) which differentially activates the GTPases RHOA, RAC1 and CDC42. Plays a role in axon guidance regulating ephrin-induced growth cone collapse and dendritic spine morphogenesis. Upon activation by ephrin through EPHA4, the GEF activity switches toward RHOA resulting in its activation. Activated RHOA promotes cone retraction at the expense of RAC1- and CDC42-stimulated growth cone extension (By similarity).

**Summary**, from NCBI Gene [25791](https://www.ncbi.nlm.nih.gov/gene/25791):

> Enables guanyl-nucleotide exchange factor activity. Predicted to be involved in ephrin receptor signaling pathway; negative regulation of dendritic spine morphogenesis; and regulation of actin cytoskeleton organization. Predicted to be located in cytosol. Predicted to be active in postsynapse. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7807](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7807) · Entrez [25791](https://www.ncbi.nlm.nih.gov/gene/25791) · UniProt [Q8N5V2](https://www.uniprot.org/uniprotkb/Q8N5V2) · Ensembl [ENSG00000066248](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000066248)

## Data

Gene col 822: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 822); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 822, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 822]; `tensor/DDL_lfc|DDL_z.npy` [822]; `embed/gene_vectors.npy` [822]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 822 or target_col == 822). Every well: [[NGEF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NGEF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
