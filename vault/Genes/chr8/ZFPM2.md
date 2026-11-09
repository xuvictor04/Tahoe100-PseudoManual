---
symbol: "ZFPM2"
type: "gene"
col: 9879
ensembl_id: "ENSG00000169946"
name: "zinc finger protein, FOG family member 2"
location: "8q23"
module: 75
arm: "+"
pooled_cpm: 26.89
n_lines_expressing: 35
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 9
direction_downstream: 6
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# ZFPM2

*zinc finger protein, FOG family member 2* — 8q23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.97× (z +33.5, q 0e+00, up in 25 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.792× (z -4.0, q 0.030, down in 8 of 32 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 4 lines (HS-578T 0.213×, SW480 0.290×, LOX-IMVI 0.263×, hTERT-HPNE 0.237×; ⚠ cell-cycle shift, explains ~8% of this change); [[Belinostat (drug)]] 5 µM in 4 lines (LOX-IMVI 0.265×, SW480 0.322×, H4 0.183×, HS-578T 0.280×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (LOX-IMVI 0.214×, SW480 0.281×, HS-578T 0.238×; ⚠ cell-cycle shift, explains ~48% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CACNA1E]] (+0.64, fdr 1e-05), [[PLXNC1]] (+0.63, fdr 2e-05), [[LINC01933]] (+0.63, fdr 1e-05); moves opposite to [[WDR5]] (-0.53, fdr 8e-05), [[CABIN1]] (-0.52, fdr 2e-04), [[MTMR12]] (-0.52, fdr 2e-04).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[ROBO2]] → it (grade B ⚠); 6 go from it, the strongest it → [[SLC35F1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9879.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.97×** | +33.5 | 0e+00 | 25/31 (A498, RKO, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.95×** | +26.3 | 0e+00 | 25/32 (NCI-H2030, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.32×** | +20.4 | 0e+00 | 24/33 (C32, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.69×** | +17.0 | 0e+00 | 25/32 (A498, SNU-423, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.36×** | +14.7 | 0e+00 | 17/32 (A498, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.00×** | +11.9 | 9e-31 | 20/30 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.96×** | +11.6 | 3e-29 | 21/31 (C32, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.74×** | +9.5 | 2e-19 | 12/28 (SW 900, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.77×** | +9.4 | 2e-19 | 15/31 (A498, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +8.8 | 1e-16 | 11/22 (HEC-1-A, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +8.6 | 6e-16 | 11/26 (C32, SW 900, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +8.2 | 1e-14 | 14/33 (A498, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +8.0 | 6e-14 | 12/32 (RKO, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.53×** | +7.1 | 7e-11 | 16/31 (SK-MEL-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **1.43×** | +5.9 | 1e-07 | 6/32 (A498, SW 900, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.32×** | +4.7 | 9e-05 | 12/32 (C32, A498, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.29×** | +4.4 | 3e-04 | 9/32 (BT-474, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +3.8 | 0.004 | 6/31 (HOP62, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9879.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 7 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 5 µM in 4 lines (HS-578T 0.213×, SW480 0.290×, LOX-IMVI 0.263×, hTERT-HPNE 0.237×; ⚠ cell-cycle shift, explains ~8% of this change); [[Belinostat (drug)]] 5 µM in 4 lines (LOX-IMVI 0.265×, SW480 0.322×, H4 0.183×, HS-578T 0.280×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 3 lines (LOX-IMVI 0.214×, SW480 0.281×, HS-578T 0.238×; ⚠ cell-cycle shift, explains ~48% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.792×** | -4.0 | 0.030 | 8/32 (SNU-423, RPMI-7951, …) | two highest doses |  |
| [[Vilanterol (drug)]] 5 µM |  | 0.882× | -3.1 | 0.39 | 4/33 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | 0.712× | -3.1 | 0.39 | 8/31 (LOX-IMVI, SW480, …) | top dose only | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9879. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 10.1 | 7 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.4× (z +22.3) | — |
| [[C32 (line)]] | wt | 21.4 | 7 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.14× (z +14.4) | — |
| [[hTERT-HPNE (line)]] | wt | 139 | 1 | 4 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.09× (z +13.4) | [[Panobinostat (drug)]] 5 µM 0.237× (z -9.5) ⚠ cell-cycle shift, explains ~8% of this change |
| [[LOX-IMVI (line)]] | wt | 120 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.214× (z -12.6) ⚠ cell-cycle shift, explains ~48% of this change |
| [[NCI-H460 (line)]] | wt | 9.46 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.09× (z +15.8) | — |
| [[SW480 (line)]] | alt | 54.2 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.281× (z -11.3) ⚠ cell-cycle shift, explains ~48% of this change |
| [[HS-578T (line)]] | alt | 309 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.78× (z +10.6) | [[Panobinostat (drug)]] 5 µM 0.213× (z -11.3) ⚠ cell-cycle shift, explains ~8% of this change |
| [[NCI-H2030 (line)]] | alt | 7.70 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.8× (z +17.5) | — |
| [[HEC-1-A (line)]] | alt | 11.3 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.36× (z +14.8) | — |
| [[HOP62 (line)]] | alt | 27.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.86× (z +14.3) | — |
| [[SK-MEL-2 (line)]] | alt | 29.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.84× (z +13.0) | — |
| [[BT-474 (line)]] | alt | 11.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.26× (z +11.1) | — |
| [[NCI-H1792 (line)]] | alt | 7.45 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.4× (z +15.2) | — |
| [[PANC-1 (line)]] | alt | 15.1 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +13.8) | — |
| [[RKO (line)]] | wt | 7.03 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 19.6× (z +16.0) | — |
| [[SHP-77 (line)]] | alt | 7.11 | 2 | 0 | [[Auranofin (drug)]] 5 µM 13.9× (z +10.0) | — |
| [[SNU-423 (line)]] | alt | 40.1 | 2 | 0 | [[Auranofin (drug)]] 5 µM 20.2× (z +16.4) | — |
| [[SW 900 (line)]] | alt | 8.88 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.96× (z +12.2) | — |
| [[A549 (line)]] | wt | 6.81 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.06× (z +12.3) | — |
| [[H4 (line)]] | wt | 71.0 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.183× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 26.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.54× (z +11.4) | — |
| [[NCI-H1573 (line)]] | alt | 8.17 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 7.56× (z +13.0) | — |
| [[SW1417 (line)]] | alt | 48.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.46× (z +9.0) | — |
| [[A-172 (line)]] | wt | 6.66 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.75 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.39 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.25 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 5.54 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.87 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 6.22 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.94 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.77 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 5.26 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.65 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.86 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 305 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.21 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.80 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9879), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CACNA1E]] | +0.64 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[PLXNC1]] | +0.63 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[LINC01933]] | +0.63 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[HDAC2-AS2]] | +0.63 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[FBXO38-DT]] | +0.61 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[HTR2C]] | +0.61 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[SLC35F1]] | +0.61 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[LINC01033]] | +0.61 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[SLC8A1-AS1]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[RERGL]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[XKR4]] | +0.60 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[GRM8]] | +0.60 | +0.52 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR5]] | -0.53 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[CABIN1]] | -0.52 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[MTMR12]] | -0.52 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[CDK5RAP1]] | -0.52 | -0.51 / -0.37 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 8, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ROBO2]] | B | ROBO2 activity raises ZFPM2's level | lines that do not express ROBO2 (38) vs lines expressing it (12) | 3.14× lower at baseline in the lines without ROBO2 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, GCG, LINC01205 |
| [[CDK15]] | B | CDK15 activity raises ZFPM2's level | lines that do not express CDK15 (28) vs lines expressing it (22) | 2.56× lower at baseline in the lines without CDK15 | 0.032 | ⚠ within organs, on part of the lines; also absent: POU3F2, PTGFR, NTM; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers ZFPM2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SOCS2-AS1]] | B | SOCS2-AS1 activity raises ZFPM2's level | lines that do not express SOCS2-AS1 (13) vs lines expressing it (37) | 2.76× lower at baseline in the lines without SOCS2-AS1 | 0.038 | ⚠ within organs, on part of the lines; also absent: SOCS2, MIR1915HG, SHOX2 |
| [[PTPRN]] | B | PTPRN activity raises ZFPM2's level | lines that do not express PTPRN (31) vs lines expressing it (19) | 2.21× lower at baseline in the lines without PTPRN | 0.044 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: SPARC, PAX3, PHACTR1 |
| [[FBN2]] | B | FBN2 activity raises ZFPM2's level | lines that do not express FBN2 (31) vs lines expressing it (19) | 2.24× lower at baseline in the lines without FBN2 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZEB2, ENSG00000289884, ABI3BP; maybe low, not absent |
| [[NHSL2]] | B | NHSL2 activity raises ZFPM2's level | lines that do not express NHSL2 (24) vs lines expressing it (26) | 2.16× lower at baseline in the lines without NHSL2 | 0.069 | ⚠ within organs, on part of the lines; also absent: S1PR3, TWIST2, FBXL7; maybe low, not absent |
| [[PRKG1]] | B | PRKG1 activity raises ZFPM2's level | lines that do not express PRKG1 (23) vs lines expressing it (27) | 2.03× lower at baseline in the lines without PRKG1 | 0.095 | ⚠ within organs, on part of the lines; also absent: NTNG1, CAMK4, DSCAM; maybe low, not absent |
| [[GPR158]] | C | GPR158 activity raises ZFPM2's level | lines that do not express GPR158 (20) vs lines expressing it (30) | 2.17× lower at baseline in the lines without GPR158 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000259929, P2RX7, LINC02968; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC35F1]] | B | ZFPM2 activity raises SLC35F1's level | lines that do not express ZFPM2 (15) vs lines expressing it (35) | 1.88× lower at baseline in the lines without ZFPM2 | 0.051 | ⚠ within organs, on part of the lines; also absent: ZNF883, EVC, TRIM9; maybe low, not absent |
| [[SYT16]] | B | ZFPM2 activity raises SYT16's level | lines that do not express ZFPM2 (15) vs lines expressing it (35) | 1.90× lower at baseline in the lines without ZFPM2 | 0.062 | ⚠ within organs, on part of the lines; also absent: ZNF883, EVC, TRIM9; maybe low, not absent |
| [[CABIN1]] | B | ZFPM2 activity raises CABIN1's level | lines that do not express ZFPM2 (15) vs lines expressing it (35) | 1.41× lower at baseline in the lines without ZFPM2 | 0.092 | ⚠ within organs, on part of the lines; also absent: ZNF883, EVC, TRIM9; maybe low, not absent |
| [[LINC02981]] | B | ZFPM2 activity raises LINC02981's level | lines that do not express ZFPM2 (15) vs lines expressing it (35) | 1.56× lower at baseline in the lines without ZFPM2 | 0.092 | ⚠ within organs, on part of the lines; also absent: ZNF883, EVC, TRIM9; maybe low, not absent |
| [[CACNA2D1]] | B | ZFPM2 activity raises CACNA2D1's level | lines that do not express ZFPM2 (15) vs lines expressing it (35) | 3.75× lower at baseline in the lines without ZFPM2 | 0.099 | ⚠ within organs, on part of the lines; also absent: ZNF883, EVC, TRIM9; maybe low, not absent |
| [[GPR158]] | C | ZFPM2 activity raises GPR158's level | lines that do not express ZFPM2 (15) vs lines expressing it (35) | 2.91× lower at baseline in the lines without ZFPM2 | 0.018 | ⚠ within organs, on part of the lines; also absent: ZNF883, EVC, TRIM9; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.651). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (24.5, 26.8); signed map (35.9, 14.1). **Vector** length 86.6, 20.6% of its response variance represented; |z| ≥ 3 in 774 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.0 | +8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.5 | +33.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.5 | +9.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.6 | +17.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.6 | +26.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.9 | +20.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.1 | +8.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.0 | +3.5 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.4 | -0.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.1 | -4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -2.0 | +1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.9 | -1.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.9 | -3.1 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein, FOG family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q23 — chr8:104,590,733-105,804,539 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PRDM19, FOG2, hFOG-2, ZNF89B |
| Gene groups (HGNC) | Zinc fingers C2H2-type; PR/SET domain family; Zinc fingers FOG C2HC-type; Putative lysine methyltransferases |
| Hallmark sets | COMPLEMENT |
| Reactome | 3 pathways, smallest: Transcriptional regulation of testis differentiation; Factors involved in megakaryocyte development and platelet production; Hemostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WW38](https://www.uniprot.org/uniprotkb/Q8WW38) (Zinc finger protein ZFPM2):

> Transcription regulator that plays a central role in heart morphogenesis and development of coronary vessels from epicardium, by regulating genes that are essential during cardiogenesis. Essential cofactor that acts via the formation of a heterodimer with transcription factors of the GATA family GATA4, GATA5 and GATA6. Such heterodimer can both activate or repress transcriptional activity, depending on the cell and promoter context. Also required in gonadal differentiation, possibly be …

**Summary**, from NCBI Gene [23414](https://www.ncbi.nlm.nih.gov/gene/23414):

> The zinc finger protein encoded by this gene is a widely expressed member of the FOG family of transcription factors. The family members modulate the activity of GATA family proteins, which are important regulators of hematopoiesis and cardiogenesis in mammals. It has been demonstrated that the protein can both activate and down-regulate expression of GATA-target genes, suggesting different modulation in different promoter contexts. A related mRNA suggests an alternatively spliced product but …

**Accessions** — [HGNC:16700](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16700) · Entrez [23414](https://www.ncbi.nlm.nih.gov/gene/23414) · UniProt [Q8WW38](https://www.uniprot.org/uniprotkb/Q8WW38) · Ensembl [ENSG00000169946](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169946)

## Data

Gene col 9879: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9879); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9879, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9879]; `tensor/DDL_lfc|DDL_z.npy` [9879]; `embed/gene_vectors.npy` [9879]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9879 or target_col == 9879). Every well: [[ZFPM2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZFPM2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
