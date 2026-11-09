---
symbol: "MYCBP"
type: "gene"
col: 13174
ensembl_id: "ENSG00000214114"
name: "MYC binding protein"
location: "1p34.3"
module: 6
arm: "+"
pooled_cpm: 9.57
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 4
n_dd_up_clean: 1
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# MYCBP

*MYC binding protein* — 1p34.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 5.73× (z +15.1, q 0e+00, up in 32 of 32 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.51× (z +5.3, q 9e-06, up in 30 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (PANC-1 6.19×, LoVo 7.01×, SW480 5.28×, LS 180 6.09×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change); [[Dinaciclib (drug)]] 5 µM in 6 lines (LS 180 7.43×, HT-29 8.65×, PANC-1 5.12×, SW480 4.59×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.513× (z -6.0, q 1e-06, down in 28 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUBG1]] (+0.69, fdr 1e-05), [[LSM4]] (+0.68, fdr 1e-05), [[GINS2]] (+0.68, fdr 1e-05); moves opposite to [[GPRASP3]] (-0.61, fdr 1e-05), [[SNHG32]] (-0.61, fdr 3e-05), [[ATF4]] (-0.61, fdr 4e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 13 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13174.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 9 lines (PANC-1 6.19×, LoVo 7.01×, SW480 5.28×, LS 180 6.09×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change); [[Dinaciclib (drug)]] 5 µM in 6 lines (LS 180 7.43×, HT-29 8.65×, PANC-1 5.12×, SW480 4.59×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **5.73×** | +15.1 | 0e+00 | 32/32 (PANC-1, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **4.86×** | +13.7 | 3e-40 | 17/17 (LS 180, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **3.46×** | +10.3 | 9e-23 | 25/25 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **2.29×** | +7.5 | 1e-11 | 43/47 (HOP62, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.76×** | +7.2 | 7e-11 | 29/43 (NCI-H1792, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **2.20×** | +7.1 | 1e-10 | 40/47 (SW480, HOP62, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | **2.14×** | +6.9 | 6e-10 | 39/47 (NCI-H460, HOP62, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +5.3 | 9e-06 | 30/48 (A-172, A549, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~48% of this change | **1.77×** | +5.2 | 2e-05 | 23/41 (Panc 03.27, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.59×** | +4.2 | 0.002 | 22/43 (SW 900, LoVo, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.52×** | +3.6 | 0.015 | 19/43 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~92% of this change | **1.50×** | +3.5 | 0.021 | 16/44 (NCI-H460, SNU-423, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~63% of this change | **1.45×** | +3.2 | 0.051 | 16/38 (CFPAC-1, MIA PaCa-2, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~91% of this change | **1.28×** | +3.1 | 0.071 | 16/48 (NCI-H1792, Hs 766T, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13174.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.513×** | -6.0 | 1e-06 | 28/41 (A498, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.713×** | -4.3 | 0.006 | 24/43 (NCI-H23, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.644×** | -3.9 | 0.016 | 20/45 (NCI-H1573, C32, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.750×** | -3.6 | 0.041 | 21/48 (RPMI-7951, KATO III, …) | all doses, stronger at high dose |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.507× | -3.1 | 0.22 | 10/48 (HCT15, SW480, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.571× | -3.0 | 0.22 | 9/48 (NCI-H2030, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.92 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13174. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 15.9 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 7.43× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | [[Homoharringtonine (drug)]] 5 µM 0.312× (z -9.0) |
| [[A498 (line)]] | wt | 12.1 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.132× (z -11.7) |
| [[HOP62 (line)]] | alt | 7.25 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.04× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[LOX-IMVI (line)]] | wt | 7.56 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 11.4× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[PANC-1 (line)]] | alt | 11.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.19× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[SW 900 (line)]] | alt | 7.21 | 0 | 2 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0859× (z -9.3) |
| [[SW480 (line)]] | alt | 12.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.28× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[A549 (line)]] | wt | 5.32 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.4× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[HT-29 (line)]] | alt | 12.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.65× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[KATO III (line)]] | alt | 13.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.72× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[LoVo (line)]] | wt | 10.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.01× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 6.82 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.7× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H1792 (line)]] | alt | 5.66 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.9× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H23 (line)]] | alt | 13.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 7.18 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.57× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[Panc 03.27 (line)]] | alt | 14.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -10.1) |
| [[A-172 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.61 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.85 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.15 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.00 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.56 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.07 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.19 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13174), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBG1]] | +0.69 | +0.73 / +0.54 | both halves | 1e-05 |  |
| [[LSM4]] | +0.68 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[GINS2]] | +0.68 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[PGP]] | +0.67 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[NUDT1]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[XRCC3]] | +0.64 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[TCF19]] | +0.62 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[GPAA1]] | +0.62 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[SNRNP25]] | +0.62 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[BRI3BP]] | +0.62 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[HAT1]] | +0.61 | +0.62 / +0.48 | both halves | 2e-05 |  |
| [[CDK2]] | +0.61 | +0.69 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRASP3]] | -0.61 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[SNHG32]] | -0.61 | -0.81 / -0.43 | both halves | 3e-05 |  |
| [[ATF4]] | -0.61 | -0.76 / -0.41 | both halves | 4e-05 |  |
| [[ZNF385C]] | -0.59 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[EIF1]] | -0.59 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[SNHG8]] | -0.59 | -0.71 / -0.43 | both halves | 4e-05 |  |
| [[ZNF286B]] | -0.58 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[RRAGB]] | -0.57 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[TCEANC]] | -0.56 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[CIRBP]] | -0.56 | -0.65 / -0.31 | both halves | 2e-04 |  |
| [[C1orf43]] | -0.55 | -0.55 / -0.37 | both halves | 8e-05 |  |
| [[N4BP2L1]] | -0.55 | -0.59 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MYCBP's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EPHA10]] | B | EPHA10 activity raises MYCBP's level | lines that do not express EPHA10 (19) vs lines expressing it (31) | 1.35× lower at baseline in the lines without EPHA10 | 0.089 | ⚠ within organs, on part of the lines; also absent: LSR, OCLN, ENTPD2 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.593). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-33.4, -41.1); signed map (-36.7, -40.9). **Vector** length 64.2, 12.5% of its response variance represented; |z| ≥ 3 in 770 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Inhibition of replication initiation of damaged DNA by RB1/E2F1* (reactome, mean cos +0.50 to 6).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +4.4 | +15.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | +3.8 | +13.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +3.3 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | +3.2 | +10.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~76% of this change | +3.1 | +6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +5.3 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.5 | +2.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | +1.2 | +1.7 |
|  | [[Berbamine (drug)]] 0.05 µM |  | +1.1 | +1.9 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | +1.0 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.4 | -6.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -3.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -3.2 | -3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -2.9 | -4.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | -2.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -2.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.8 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | MYC binding protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.3 — chr1:38,862,493-38,873,368 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AMY-1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q99417](https://www.uniprot.org/uniprotkb/Q99417) (c-Myc-binding protein):

> May control the transcriptional activity of MYC. Stimulates the activation of E box-dependent transcription by MYC.

**Summary**, from NCBI Gene [26292](https://www.ncbi.nlm.nih.gov/gene/26292):

> The protein encoded by this gene binds to the N-terminus of the oncogenic protein C-MYC, enhancing the ability of C-MYC to activate E box-dependent transcription. The encoded protein is normally found in the cytoplasm, but it translocates to the nucleus during S phase of the cell cycle and associates with C-MYC. This protein may be involved in spermatogenesis. This gene can be silenced by microRNA-22. Two transcript variants, one protein-coding and the other probably not protein-coding, have …

**Accessions** — [HGNC:7554](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7554) · Entrez [26292](https://www.ncbi.nlm.nih.gov/gene/26292) · UniProt [Q99417](https://www.uniprot.org/uniprotkb/Q99417) · Ensembl [ENSG00000214114](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214114)

## Data

Gene col 13174: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13174); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13174, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13174]; `tensor/DDL_lfc|DDL_z.npy` [13174]; `embed/gene_vectors.npy` [13174]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13174 or target_col == 13174). Every well: [[MYCBP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MYCBP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
