---
symbol: "CAMSAP3"
type: "gene"
col: 1164
ensembl_id: "ENSG00000076826"
name: "calmodulin regulated spectrin associated protein family member 3"
location: "19p13.2"
module: 3
arm: "+"
pooled_cpm: 7.09
n_lines_expressing: 34
n_dd_up: 18
n_dd_down: 1
n_dd_up_clean: 14
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 7
direction_downstream: 12
tags: ["gene", "module/003"]
generated_by: "tahoemap"
---

# CAMSAP3

*calmodulin regulated spectrin associated protein family member 3* — 19p13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.19× (z +15.5, q 0e+00, up in 30 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.732× (z -4.0, q 0.035, down in 11 of 26 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 0.162×, LoVo 0.257×, HEC-1-A 0.245×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2347 0.226×, SW48 0.109×); [[Brivudine (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0665×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLHL26]] (+0.68, fdr 1e-05), [[DENND6B]] (+0.63, fdr 1e-05), [[FOXO6]] (+0.62, fdr 1e-05); moves opposite to [[PSME3IP1]] (-0.59, fdr 1e-04), [[ALG8]] (-0.55, fdr 6e-05), [[MCTS1]] (-0.55, fdr 1e-04).
> It sits in the **+** arm of [[Module 003]] (mRNA 3'-end processing).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[BIK]] → it (grade B ⚠); 12 go from it, the strongest it → [[CACFD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1164.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.19×** | +15.5 | 0e+00 | 30/32 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.89×** | +14.1 | 8e-43 | 29/30 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.50×** | +12.2 | 7e-32 | 28/31 (NCI-H2347, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.79×** | +11.0 | 8e-26 | 21/28 (HepG2/C3A, SW480, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.77×** | +10.7 | 9e-25 | 26/31 (NCI-H2347, A498, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +6.4 | 2e-08 | 13/31 (NCI-H2030, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +5.8 | 5e-07 | 13/32 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.28×** | +5.8 | 6e-07 | 7/29 (NCI-H23, HCT15, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +5.5 | 3e-06 | 13/28 (LS 180, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.50×** | +5.4 | 5e-06 | 13/28 (NCI-H2347, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +4.6 | 3e-04 | 8/25 (LoVo, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +4.5 | 3e-04 | 11/28 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.38×** | +4.3 | 7e-04 | 9/26 (HepG2/C3A, LS 180, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +4.0 | 0.002 | 6/26 (NCI-H1573, LS 180, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.008 | 7/28 (HEC-1-A, LoVo, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.45×** | +3.6 | 0.014 | 1/27 (SW480) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.028 | 7/29 (HepG2/C3A, LS 180, …) | top dose only | cell-cycle shift (explains ~14% here); composition shift; position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1164.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 3 lines (SW480 0.162×, LoVo 0.257×, HEC-1-A 0.245×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 2 lines (NCI-H2347 0.226×, SW48 0.109×); [[Brivudine (drug)]] 0.05 µM in 1 line (MIA PaCa-2 0.0665×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.732×** | -4.0 | 0.035 | 11/26 (NCI-H2347, SW48, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Busulfan (drug)]] 5 µM |  | 0.848× | -3.1 | 0.53 | 6/30 (SNU-1, A498, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1164. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 19.2 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.75× (z +10.8) | [[Dinaciclib (drug)]] 5 µM 0.257× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[LS 180 (line)]] | wt | 15.3 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.45× (z +10.4) | — |
| [[SW480 (line)]] | alt | 15.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.05× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.162× (z -15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 8.45 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.151× (z -8.8) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 14.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 21.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.08× (z +13.2) | — |
| [[MIA PaCa-2 (line)]] | alt | 6.59 | 0 | 1 | — | [[Brivudine (drug)]] 0.05 µM 0.0665× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 11.0 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -8.8) |
| [[SW48 (line)]] | wt | 14.3 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.109× (z -8.8) |
| [[A-172 (line)]] | wt | 2.35 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.72 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 8.32 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.40 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.628 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.809 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.871 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.923 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.27 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.820 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.30 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.954 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.92 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1164), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLHL26]] | +0.68 | +0.51 / +0.68 | both halves | 1e-05 |  |
| [[DENND6B]] | +0.63 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[FOXO6]] | +0.62 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[CFD]] | +0.62 | +0.34 / +0.68 | both halves | 1e-04 |  |
| [[PEDS1]] | +0.62 | +0.38 / +0.60 | both halves | 7e-05 |  |
| [[PIP5K1C]] | +0.62 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[LLGL2]] | +0.61 | +0.60 / +0.41 | both halves | 4e-05 |  |
| [[CCDC88B]] | +0.60 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[HDAC5]] | +0.60 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[BAIAP3]] | +0.60 | +0.39 / +0.56 | both halves | 6e-05 |  |
| [[PAOX]] | +0.59 | +0.61 / +0.43 | both halves | 3e-05 |  |
| [[ANO8]] | +0.59 | +0.47 / +0.49 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSME3IP1]] | -0.59 | -0.33 / -0.56 | both halves | 1e-04 |  |
| [[ALG8]] | -0.55 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[MCTS1]] | -0.55 | -0.33 / -0.42 | both halves | 1e-04 |  |
| [[ENOX2]] | -0.55 | -0.38 / -0.32 | both halves | 2e-04 |  |
| [[E2F3]] | -0.55 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[ADAT1]] | -0.54 | -0.38 / -0.39 | both halves | 7e-05 |  |
| [[PRMT3]] | -0.53 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[PIGW]] | -0.53 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[XRCC5]] | -0.53 | -0.48 / -0.54 | both halves | 2e-05 |  |
| [[EXOC4]] | -0.52 | -0.42 / -0.48 | both halves | 4e-05 | same gene group |
| [[TRNT1]] | -0.52 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[TBC1D5]] | -0.52 | -0.37 / -0.47 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BIK]] | B | BIK activity raises CAMSAP3's level | lines that do not express BIK (15) vs lines expressing it (35) | 2.78× lower at baseline in the lines without BIK | 0.049 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3 |
| [[CDC42BPG]] | B | CDC42BPG activity raises CAMSAP3's level | lines that do not express CDC42BPG (19) vs lines expressing it (31) | 2.35× lower at baseline in the lines without CDC42BPG | 0.089 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, PLEKHG6; maybe low, not absent |
| [[BAIAP3]] | B | BAIAP3 activity raises CAMSAP3's level | lines that do not express BAIAP3 (8) vs lines expressing it (42) | 1.29× lower at baseline in the lines without BAIAP3 | 0.089 | ⚠ within organs, on part of the lines; also absent: PPFIA4; maybe low, not absent; its own permutation p |
| [[RASGEF1A]] | B | RASGEF1A activity raises CAMSAP3's level | lines that do not express RASGEF1A (25) vs lines expressing it (25) | 1.50× lower at baseline in the lines without RASGEF1A | 0.0997 | ⚠ within organs, on part of the lines; also absent: ITGB2, ANKRD20A21P, CHGB |
| [[EPHA10]] | C | EPHA10 activity raises CAMSAP3's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 3.49× lower at baseline in the lines without EPHA10 | 0.001 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2; co-absent with the target |
| [[LLGL2]] | C | LLGL2 activity raises CAMSAP3's level | lines that do not express LLGL2 (12) vs lines expressing it (38) | 3.57× lower at baseline in the lines without LLGL2 | 0.022 | ⚠ within organs, on part of the lines; also absent: GRTP1, FGFR4, LSR; co-absent with the target |
| [[SYP]] | C | SYP activity raises CAMSAP3's level | lines that do not express SYP (4) vs lines expressing it (46) | 1.43× lower at baseline in the lines without SYP | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; maybe low, not absent; its own permutation p |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 10, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACFD1]] | B | CAMSAP3 activity raises CACFD1's level | lines that do not express CAMSAP3 (16) vs lines expressing it (34) | 1.51× lower at baseline in the lines without CAMSAP3 | 0.027 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CGN, FGFR4, UNC5A; maybe low, not absent |
| [[BIK]] | B | CAMSAP3 activity raises BIK's level | lines that do not express CAMSAP3 (16) vs lines expressing it (34) | 2.67× lower at baseline in the lines without CAMSAP3 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CGN, FGFR4, UNC5A; maybe low, not absent |
| [[BAIAP3]] | B | CAMSAP3 activity raises BAIAP3's level | lines that do not express CAMSAP3 (16) vs lines expressing it (34) | 1.34× lower at baseline in the lines without CAMSAP3 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CGN, FGFR4, UNC5A; maybe low, not absent |
| [[PSME3]] | B | CAMSAP3 activity raises PSME3's level | lines that do not express CAMSAP3 (16) vs lines expressing it (34) | 1.32× lower at baseline in the lines without CAMSAP3 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CGN, FGFR4, UNC5A; maybe low, not absent |
| [[NRTN]] | B | CAMSAP3 activity weakens NRTN's drug response | lines that do not express CAMSAP3 (11) vs lines expressing it (31) | the lines without CAMSAP3 respond 1.29× as strongly (z diff -0.38); strongest at Idarubicin (hydrochloride) 5 µM: 3.59x vs 1.60x (z diff -3.3) | 0.059 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CGN, FGFR4, UNC5A; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[MAP1S]] | B | CAMSAP3 activity raises MAP1S's level | lines that do not express CAMSAP3 (16) vs lines expressing it (34) | 1.16× lower at baseline in the lines without CAMSAP3 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CGN, FGFR4, UNC5A; maybe low, not absent |
| [[NRTN]] | B | CAMSAP3 activity raises NRTN's level | lines that do not express CAMSAP3 (16) vs lines expressing it (34) | 1.80× lower at baseline in the lines without CAMSAP3 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CGN, FGFR4, UNC5A; maybe low, not absent |
| [[CDC42BPG]] | B | CAMSAP3 activity raises CDC42BPG's level | lines that do not express CAMSAP3 (16) vs lines expressing it (34) | 2.83× lower at baseline in the lines without CAMSAP3 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CGN, FGFR4, UNC5A; maybe low, not absent |
| [[ABHD8]] | B | CAMSAP3 activity raises ABHD8's level | lines that do not express CAMSAP3 (16) vs lines expressing it (34) | 1.28× lower at baseline in the lines without CAMSAP3 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CGN, FGFR4, UNC5A; maybe low, not absent |
| [[RBM38]] | B | CAMSAP3 activity raises RBM38's level | lines that do not express CAMSAP3 (16) vs lines expressing it (34) | 1.90× lower at baseline in the lines without CAMSAP3 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CGN, FGFR4, UNC5A; maybe low, not absent |
| [[EPHA10]] | C | CAMSAP3 activity raises EPHA10's level | lines that do not express CAMSAP3 (16) vs lines expressing it (34) | 2.72× lower at baseline in the lines without CAMSAP3 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CGN, FGFR4, UNC5A; maybe low, not absent; co-absent with the target |
| [[LLGL2]] | C | CAMSAP3 activity raises LLGL2's level | lines that do not express CAMSAP3 (16) vs lines expressing it (34) | 4.51× lower at baseline in the lines without CAMSAP3 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: CGN, FGFR4, UNC5A; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 003]] — mRNA 3'-end processing; 246 genes; this gene is in the **+** arm (projection on the module's main direction 0.486). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (7.9, -3.1); signed map (-27.1, 19.3). **Vector** length 55.2, 10.8% of its response variance represented; |z| ≥ 3 in 586 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +10.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.9 | +5.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.7 | +14.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.6 | +15.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +0.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.4 | +2.1 |
|  | [[Bimiralisib (drug)]] 0.5 µM |  | +1.4 | +1.4 |
| fall | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.8 | -4.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | -1.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -0.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.9 | -2.1 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -1.2 | -1.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.2 | -1.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | calmodulin regulated spectrin associated protein family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.2 — chr19:7,595,863-7,618,304 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Nezha, PPP1R80; previously KIAA1543 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; MicroRNA protein coding host genes; CAMSAP family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P1Y5](https://www.uniprot.org/uniprotkb/Q9P1Y5) (Calmodulin-regulated spectrin-associated protein 3):

> Key microtubule-organizing protein that specifically binds the minus-end of non-centrosomal microtubules and regulates their dynamics and organization. Specifically recognizes growing microtubule minus-ends and autonomously decorates and stabilizes microtubule lattice formed by microtubule minus-end polymerization. Acts on free microtubule minus-ends that are not capped by microtubule-nucleating proteins or other factors and protects microtubule minus-ends from depolymerization. In addition, it …

**Summary**, from NCBI Gene [57662](https://www.ncbi.nlm.nih.gov/gene/57662):

> Enables actin filament binding activity and microtubule minus-end binding activity. Involved in several processes, including establishment of epithelial cell apical/basal polarity; microtubule cytoskeleton organization; and zonula adherens maintenance. Located in cytoplasm; microtubule cytoskeleton; and zonula adherens. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:29307](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29307) · Entrez [57662](https://www.ncbi.nlm.nih.gov/gene/57662) · UniProt [Q9P1Y5](https://www.uniprot.org/uniprotkb/Q9P1Y5) · Ensembl [ENSG00000076826](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000076826)

## Data

Gene col 1164: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1164); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1164, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1164]; `tensor/DDL_lfc|DDL_z.npy` [1164]; `embed/gene_vectors.npy` [1164]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1164 or target_col == 1164). Every well: [[CAMSAP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CAMSAP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
