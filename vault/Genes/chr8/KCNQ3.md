---
symbol: "KCNQ3"
type: "gene"
col: 11494
ensembl_id: "ENSG00000184156"
name: "potassium voltage-gated channel subfamily Q member 3"
location: "8q24.22"
module: 61
arm: "+"
pooled_cpm: 14.75
n_lines_expressing: 24
n_dd_up: 36
n_dd_down: 8
n_dd_up_clean: 29
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 5
direction_downstream: 6
tags: ["gene", "module/061"]
generated_by: "tahoemap"
---

# KCNQ3

*potassium voltage-gated channel subfamily Q member 3* — 8q24.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 36 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 5.81× (z +27.6, q 0e+00, up in 20 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (none with an alert); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.745× (z -4.6, q 0.002, down in 13 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR4527HG]] (+0.66, fdr 2e-05), [[ERC2]] (+0.63, fdr 7e-06), [[CCDC85A]] (+0.60, fdr 1e-05); moves opposite to [[LRRC27]] (-0.49, fdr 3e-04), [[ALDH6A1]] (-0.45, fdr 5e-05), [[ZNF487]] (-0.43, fdr 3e-04).
> It is in [[Module 061]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[CASP4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 36 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11494.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **5.81×** | +27.6 | 0e+00 | 20/21 (NCI-H460, RKO, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.85×** | +16.4 | 0e+00 | 7/22 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **4.10×** | +15.7 | 0e+00 | 18/21 (NCI-H460, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.59×** | +13.6 | 3e-40 | 3/11 (A498, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.83×** | +11.5 | 9e-29 | 7/21 (HT-29, NCI-H460, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.75×** | +11.2 | 2e-27 | 3/17 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.98×** | +10.7 | 7e-25 | 4/20 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.62×** | +10.7 | 8e-25 | 16/21 (NCI-H460, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.32×** | +8.6 | 4e-16 | 2/14 (NCI-H460, NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.04×** | +7.9 | 2e-13 | 9/21 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.95×** | +7.4 | 6e-12 | 11/21 (NCI-H460, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.72×** | +6.0 | 8e-08 | 7/21 (NCI-H460, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~25% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.41×** | +5.3 | 4e-06 | 8/22 (A498, A549, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +5.3 | 5e-06 | 10/21 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.44×** | +5.2 | 8e-06 | 10/22 (NCI-H23, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +4.5 | 2e-04 | 5/20 (NCI-H460, A498, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.45×** | +4.1 | 0.001 | 10/21 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.001 | 10/21 (NCI-H1573, BT-474, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11494.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.745×** | -4.6 | 0.002 | 13/21 (SHP-77, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.670×** | -4.5 | 0.002 | 11/21 (H4, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.769×** | -4.1 | 0.006 | 11/21 (SHP-77, RKO, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.703×** | -3.9 | 0.010 | 10/21 (SHP-77, H4, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.704×** | -3.9 | 0.010 | 14/21 (H4, SHP-77, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.716×** | -3.7 | 0.018 | 8/21 (SHP-77, BT-474, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.728×** | -3.5 | 0.031 | 12/21 (SHP-77, BT-474, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.737×** | -3.4 | 0.046 | 10/21 (SHP-77, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11494. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 28.5 | 0 | 10 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0242× (z -15.4) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.100× (z -14.0) |
| [[H4 (line)]] | wt | 59.7 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.118× (z -10.7) |
| [[NCI-H23 (line)]] | alt | 10.1 | 3 | 3 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 11.1× (z +12.8) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0507× (z -11.4) |
| [[AsPC-1 (line)]] | alt | 113 | 1 | 3 (1 ⚠) | [[Trametinib (drug)]] 0.05 µM 3.72× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -14.6) |
| [[NCI-H460 (line)]] | wt | 4.42 | 4 | 0 | [[Tucidinostat (drug)]] 5 µM 14.6× (z +14.5) | — |
| [[BT-474 (line)]] | alt | 22.2 | 1 | 2 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 6.90× (z +10.3) | [[Simotinib (drug)]] 5 µM 0.0678× (z -9.8) ⚠ toxic · without an alert: [[Osimertinib (mesylate) (drug)]] 5 µM 0.101× (z -8.7) |
| [[LOX-IMVI (line)]] | wt | 196 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -13.0) |
| [[A549 (line)]] | wt | 20.2 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 6.38× (z +11.6) | — |
| [[COLO 205 (line)]] | alt | 8.98 | 0 | 2 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.114× (z -9.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[crizotinib (drug)]] 5 µM 0.0469× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 24.4 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 4.01× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.317× (z -8.6) |
| [[RKO (line)]] | wt | 14.0 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 14.8× (z +13.3) | — |
| [[A498 (line)]] | wt | 4.61 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.64× (z +10.3) | — |
| [[HT-29 (line)]] | alt | 3.71 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.67× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 5.28 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.42× (z +9.1) | — |
| [[NCI-H2347 (line)]] | alt | 37.6 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.16× (z +11.0) | — |
| [[SK-MEL-2 (line)]] | alt | 26.4 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0826× (z -12.0) |
| [[A-172 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.98 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.76 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.55 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 41.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.68 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.30 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11494), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR4527HG]] | +0.66 | +0.48 / +0.65 | both halves | 2e-05 | **novel candidate** |
| [[ERC2]] | +0.63 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[CCDC85A]] | +0.60 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[RELN]] | +0.53 | +0.45 / +0.48 | both halves | 3e-05 |  |
| [[SNTG2]] | +0.52 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[SNAP91]] | +0.52 | +0.49 / +0.41 | both halves | 4e-05 |  |
| [[PTCHD1]] | +0.51 | +0.37 / +0.49 | both halves | 8e-05 |  |
| [[NYAP2]] | +0.51 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[PLD5]] | +0.51 | +0.35 / +0.58 | both halves | 1e-04 |  |
| [[ENKUR]] | +0.50 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[NRG3]] | +0.50 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[GPM6A]] | +0.50 | +0.45 / +0.51 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC27]] | -0.49 | -0.28 / -0.57 | both halves | 3e-04 |  |
| [[ALDH6A1]] | -0.45 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[ZNF487]] | -0.43 | -0.29 / -0.49 | both halves | 3e-04 |  |
| [[HDAC6]] | -0.43 | -0.39 / -0.45 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers KCNQ3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ACTN2]] | B | ACTN2 activity lowers KCNQ3's level | lines that do not express ACTN2 (17) vs lines expressing it (33) | 1.52× higher at baseline in the lines without ACTN2 | 0.056 | ⚠ within organs, on part of the lines; also absent: ZNF568, LINC03041, RNF182; maybe low, not absent |
| [[SVEP1]] | B | SVEP1 activity lowers KCNQ3's level | lines that do not express SVEP1 (15) vs lines expressing it (35) | 1.55× higher at baseline in the lines without SVEP1 | 0.096 | ⚠ within organs, on part of the lines; also absent: LPAR1, CDH8, ENSG00000253100; maybe low, not absent |
| [[TNC]] | C | TNC activity raises KCNQ3's level | lines that do not express TNC (23) vs lines expressing it (27) | 2.71× lower at baseline in the lines without TNC | 0.032 | ⚠ within organs, on part of the lines; also absent: RDUR, RFX8, ENSG00000287622; co-absent with the target |
| [[SYT9]] | C | SYT9 activity raises KCNQ3's level | lines that do not express SYT9 (35) vs lines expressing it (15) | 2.49× lower at baseline in the lines without SYT9 | 0.093 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NRG3, ZNF732, S100A8; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASP4]] | B | KCNQ3 activity strengthens CASP4's drug response | lines that do not express KCNQ3 (23) vs lines expressing it (21) | the lines without KCNQ3 respond 0.71× as strongly (z diff +2.40); strongest at Harringtonine 5 µM: 0.70x vs 0.46x (z diff +3.6) | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000236212, LINC02360, SLITRK4; target measured in part of the lines; artifact flags |
| [[CASP4]] | B | KCNQ3 activity raises CASP4's level | lines that do not express KCNQ3 (26) vs lines expressing it (24) | 2.07× lower at baseline in the lines without KCNQ3 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000236212, LINC02360, SLITRK4 |
| [[CREB5]] | B | KCNQ3 activity raises CREB5's level | lines that do not express KCNQ3 (26) vs lines expressing it (24) | 2.54× lower at baseline in the lines without KCNQ3 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000236212, LINC02360, SLITRK4 |
| [[NABP1]] | B | KCNQ3 activity raises NABP1's level | lines that do not express KCNQ3 (26) vs lines expressing it (24) | 1.74× lower at baseline in the lines without KCNQ3 | 0.085 | ⚠ within organs, on part of the lines; also absent: ENSG00000236212, LINC02360, SLITRK4 |
| [[MAST4]] | B | KCNQ3 activity raises MAST4's level | lines that do not express KCNQ3 (26) vs lines expressing it (24) | 1.81× lower at baseline in the lines without KCNQ3 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000236212, LINC02360, SLITRK4 |
| [[CPNE4]] | C | KCNQ3 activity raises CPNE4's level | lines that do not express KCNQ3 (26) vs lines expressing it (24) | 2.59× lower at baseline in the lines without KCNQ3 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000236212, LINC02360, SLITRK4; co-absent with the target |

## Where it sits

- **Module**: [[Module 061]] — Neuronal System; 78 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (27.3, 30.7); signed map (32.7, 21.6). **Vector** length 73.8, 19.2% of its response variance represented; |z| ≥ 3 in 758 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +9.3 | +27.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.3 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.7 | +11.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.0 | +8.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +7.7 | +15.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.1 | +5.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.4 | +11.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.9 | +1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.9 | +4.1 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.7 | -3.9 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.2 | -1.0 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.9 | -1.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.9 | -0.4 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.7 | -4.6 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.7 | -4.1 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.6 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | potassium voltage-gated channel subfamily Q member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.22 — chr8:132,120,861-132,481,095 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Kv7.3; previously EBN2 |
| Gene groups (HGNC) | Potassium voltage-gated channels |
| Reactome | 7 pathways, smallest: Voltage gated Potassium channels; Interaction between L1 and Ankyrins; Potassium Channels |
| Matched by | ensembl_id |

**Function**, from UniProt [O43525](https://www.uniprot.org/uniprotkb/O43525) (Potassium voltage-gated channel subfamily KQT member 3):

> Pore-forming subunit of the voltage-gated potassium (Kv) M-channel which is responsible for the M-current, a key controller of neuronal excitability. M-channel is composed of pore-forming subunits KCNQ2 and KCNQ3 assembled as heterotetramers. The native M-current has a slowly activating and deactivating potassium conductance which plays a critical role in determining the subthreshold electrical excitability of neurons as well as the responsiveness to synaptic inputs. M-channel is selectively …

**Summary**, from NCBI Gene [3786](https://www.ncbi.nlm.nih.gov/gene/3786):

> This gene encodes a protein that functions in the regulation of neuronal excitability. The encoded protein forms an M-channel by associating with the products of the related KCNQ2 or KCNQ5 genes, which both encode integral membrane proteins. M-channel currents are inhibited by M1 muscarinic acetylcholine receptors and are activated by retigabine, a novel anti-convulsant drug. Defects in this gene are a cause of benign familial neonatal convulsions type 2 (BFNC2), also known as epilepsy, benign …

**Accessions** — [HGNC:6297](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6297) · Entrez [3786](https://www.ncbi.nlm.nih.gov/gene/3786) · UniProt [O43525](https://www.uniprot.org/uniprotkb/O43525) · Ensembl [ENSG00000184156](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184156)

## Data

Gene col 11494: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11494); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11494, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11494]; `tensor/DDL_lfc|DDL_z.npy` [11494]; `embed/gene_vectors.npy` [11494]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11494 or target_col == 11494). Every well: [[KCNQ3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KCNQ3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
