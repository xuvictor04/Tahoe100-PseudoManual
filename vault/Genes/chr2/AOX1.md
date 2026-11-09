---
symbol: "AOX1"
type: "gene"
col: 6158
ensembl_id: "ENSG00000138356"
name: "aldehyde oxidase 1"
location: "2q33.1"
module: 53
arm: "+"
pooled_cpm: 7.88
n_lines_expressing: 33
n_dd_up: 27
n_dd_down: 7
n_dd_up_clean: 19
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 7
direction_downstream: 33
tags: ["gene", "module/053"]
generated_by: "tahoemap"
---

# AOX1

*aldehyde oxidase 1* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 5.00× (z +25.4, q 0e+00, up in 25 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.668× (z -4.2, q 0.016, down in 13 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TG]] (+0.63, fdr 1e-05), [[SLC2A14]] (+0.61, fdr 1e-05), [[SVEP1]] (+0.59, fdr 1e-05); moves opposite to [[PSMD9]] (-0.53, fdr 6e-05), [[ARMC9]] (-0.49, fdr 5e-05), [[PDE8A]] (-0.47, fdr 2e-04).
> It is in [[Module 053]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[CALCRL]] → it (grade B ⚠); 33 go from it, the strongest it → [[ACTR3-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6158.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **5.00×** | +25.4 | 0e+00 | 25/28 (RPMI-7951, A498, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.64×** | +13.9 | 3e-41 | 8/12 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **3.18×** | +12.9 | 9e-36 | 15/20 (HOP62, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **2.09×** | +11.6 | 7e-29 | 15/26 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.06×** | +11.5 | 1e-28 | 8/12 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.70×** | +10.6 | 2e-24 | 15/23 (A-172, HS-578T, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.93×** | +10.4 | 3e-23 | 18/30 (A-172, PANC-1, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.58×** | +10.2 | 2e-22 | 18/23 (HOP62, C32, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.19×** | +8.7 | 2e-16 | 12/27 (A-172, HEC-1-A, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.63×** | +7.7 | 1e-12 | 21/30 (HOP62, PANC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.94×** | +7.4 | 9e-12 | 17/28 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.87×** | +6.9 | 2e-10 | 15/26 (RKO, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Triamcinolone (drug)]] 5 µM |  | **1.45×** | +5.8 | 4e-07 | 12/29 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.60×** | +5.2 | 7e-06 | 11/31 (J82, LOX-IMVI, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.62×** | +5.2 | 9e-06 | 6/24 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.53×** | +4.7 | 7e-05 | 9/26 (hTERT-HPNE, NCI-H1573, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.003 | 10/29 (NCI-H1573, A498, …) | two highest doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.41×** | +3.6 | 0.010 | 7/29 (A-172, J82, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.013 | 11/28 (LOX-IMVI, A498, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.035 | 3/29 (SK-MEL-2, AN3 CA, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6158.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.668×** | -4.2 | 0.016 | 13/28 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.704×** | -4.0 | 0.016 | 14/29 (NCI-H460, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Pentagastrin (drug)]] 0.05 µM |  | **0.707×** | -3.9 | 0.016 | 5/28 (HEC-1-A, BT-474, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.806×** | -3.5 | 0.059 | 7/31 (LOX-IMVI, A-172, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.723×** | -3.5 | 0.059 | 14/26 (SK-MEL-2, NCI-H460, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.562×** | -3.4 | 0.065 | 8/15 (NCI-H460, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |
| [[Balsalazide (sodium hydrate) (drug)]] 0.05 µM |  | **0.752×** | -3.2 | 0.099 | 4/29 (HEC-1-A, C-33 A, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.762× | -3.1 | 0.14 | 12/25 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.828× | -3.1 | 0.14 | 4/31 (NCI-H661, Hs 766T, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6158. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 32.4 | 3 (2 ⚠) | 5 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.67× (z +14.5) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 6.98× (z +11.5) | [[Panobinostat (drug)]] 0.5 µM 0.147× (z -10.4) ⚠ cell-cycle shift, explains ~73% of this change |
| [[PANC-1 (line)]] | alt | 8.71 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.219× (z -10.2) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.220× (z -9.2) |
| [[HOP62 (line)]] | alt | 16.7 | 2 | 0 | [[Dexamethasone (drug)]] 0.05 µM 5.37× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 81.2 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.02× (z +12.2) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.54× (z +9.9) | — |
| [[NCI-H23 (line)]] | alt | 7.94 | 0 | 2 | — | [[Ipatasertib (drug)]] 0.5 µM 0.0419× (z -9.7) |
| [[A498 (line)]] | wt | 2.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.73× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 3.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.6× (z +8.5) | — |
| [[HS-578T (line)]] | alt | 5.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.78× (z +8.8) | — |
| [[J82 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0699× (z -10.7) ⚠ transcription drop; cell-cycle shift, explains ~73% of this change |
| [[NCI-H2030 (line)]] | alt | 8.22 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.5 µM 0.0705× (z -9.8) |
| [[NCI-H460 (line)]] | wt | 17.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.236× (z -10.1) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 11.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.74× (z +9.6) | — |
| [[A-172 (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.91 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.69 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 5.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 38.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.35 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6158), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TG]] | +0.63 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[SLC2A14]] | +0.61 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[SVEP1]] | +0.59 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[FNDC7]] | +0.59 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[CFLAR-AS1]] | +0.57 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[STXBP5-AS1]] | +0.57 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[PIGV]] | +0.56 | +0.65 / +0.30 | both halves | 2e-04 |  |
| [[WAKMAR2]] | +0.56 | +0.61 / +0.35 | both halves | 1e-04 |  |
| [[TRIM72]] | +0.55 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[CLCN4]] | +0.55 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[ROS1]] | +0.55 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[SLC2A9]] | +0.55 | +0.54 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD9]] | -0.53 | -0.55 / -0.39 | both halves | 6e-05 |  |
| [[ARMC9]] | -0.49 | -0.42 / -0.40 | both halves | 5e-05 |  |
| [[PDE8A]] | -0.47 | -0.58 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 4, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CALCRL]] | B | CALCRL activity raises AOX1's level | lines that do not express CALCRL (18) vs lines expressing it (32) | 2.15× lower at baseline in the lines without CALCRL | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000259363, NRG1, SPOCK3 |
| [[TOP2A]] | B | TOP2A activity lowers AOX1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CLCN4]] | B | CLCN4 activity lowers AOX1's level | lines that do not express CLCN4 (7) vs lines expressing it (43) | 2.19× higher at baseline in the lines without CLCN4 | 0.060 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PSMB5]] | B | PSMB5 activity raises AOX1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[GLIPR1]] | C | GLIPR1 activity raises AOX1's level | lines that do not express GLIPR1 (21) vs lines expressing it (29) | 2.72× lower at baseline in the lines without GLIPR1 | 0.056 | ⚠ within organs, on part of the lines; also absent: STC1, ENSG00000253891, ENSG00000230615; maybe low, not absent; co-absent with the target |
| [[DNAH11]] | C | DNAH11 activity raises AOX1's level | lines that do not express DNAH11 (23) vs lines expressing it (27) | 2.21× lower at baseline in the lines without DNAH11 | 0.071 | ⚠ within organs, on part of the lines; also absent: STAC, TWIST2, BASP1; co-absent with the target |
| [[ALPK2]] | C | ALPK2 activity raises AOX1's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 2.49× lower at baseline in the lines without ALPK2 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4; co-absent with the target |

### Downstream of this gene

*33 arrows, 33 of them with an alert ⚠; grade A 0, B 32, C 1. Shown: the 12 strongest; 21 more arrows (21 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ACTR3-AS1]] | B | AOX1 activity raises ACTR3-AS1's level | lines that do not express AOX1 (17) vs lines expressing it (33) | 1.84× lower at baseline in the lines without AOX1 | 0.002 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[MPP4]] | B | AOX1 activity raises MPP4's level | lines that do not express AOX1 (17) vs lines expressing it (33) | 2.14× lower at baseline in the lines without AOX1 | 0.004 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[AXDND1]] | B | AOX1 activity raises AXDND1's level | lines that do not express AOX1 (17) vs lines expressing it (33) | 1.71× lower at baseline in the lines without AOX1 | 0.008 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[CFAP58]] | B | AOX1 activity raises CFAP58's level | lines that do not express AOX1 (17) vs lines expressing it (33) | 1.50× lower at baseline in the lines without AOX1 | 0.008 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| cells under [[Berbamine (dihydrochloride) (drug)]] 0.5 µM | B | AOX1 activity raises the cells' numbers under Berbamine (dihydrochloride) 0.5 µM (protects the cells) | lines that do not express AOX1 (17) vs lines expressing it (31) | the lines without AOX1: 0.85× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[TG]] | B | AOX1 activity raises TG's level | lines that do not express AOX1 (17) vs lines expressing it (33) | 1.53× lower at baseline in the lines without AOX1 | 0.022 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[USP50]] | B | AOX1 activity raises USP50's level | lines that do not express AOX1 (17) vs lines expressing it (33) | 1.44× lower at baseline in the lines without AOX1 | 0.022 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| cells under [[Imiquimod (hydrochloride) (drug)]] 5 µM | B | AOX1 activity lowers the cells' numbers under Imiquimod (hydrochloride) 5 µM (makes them more sensitive) | lines that do not express AOX1 (17) vs lines expressing it (31) | the lines without AOX1: 1.27× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| cells under [[Pravastatin (sodium) (drug)]] 5 µM | B | AOX1 activity raises the cells' numbers under Pravastatin (sodium) 5 µM (protects the cells) | lines that do not express AOX1 (17) vs lines expressing it (31) | the lines without AOX1: 0.86× the cells of the other lines | 0.033 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| cells under [[Fumaric acid (drug)]] 5 µM | B | AOX1 activity raises the cells' numbers under Fumaric acid 5 µM (protects the cells) | lines that do not express AOX1 (17) vs lines expressing it (31) | the lines without AOX1: 0.85× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| cells under [[Amsacrine (drug)]] 5 µM | B | AOX1 activity lowers the cells' numbers under Amsacrine 5 µM (makes them more sensitive) | lines that do not express AOX1 (17) vs lines expressing it (31) | the lines without AOX1: 1.08× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |
| [[ITGA10]] | B | AOX1 activity raises ITGA10's level | lines that do not express AOX1 (17) vs lines expressing it (33) | 2.05× lower at baseline in the lines without AOX1 | 0.046 | ⚠ within organs, on part of the lines; also absent: KCNG1, TTC28, ARHGEF6; maybe low, not absent |

## Where it sits

- **Module**: [[Module 053]]; 88 genes; every member is in the + arm (projection on the module's main direction 0.484). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (26.5, 21.5); signed map (25.0, 12.7). **Vector** length 72.7, 16.2% of its response variance represented; |z| ≥ 3 in 846 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.0 | +13.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +25.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | +6.3 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.9 | +11.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +7.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +10.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +8.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.7 | +3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.4 | +3.6 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.8 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | -0.6 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -4.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.2 | +1.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -1.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | aldehyde oxidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:200,586,014-200,677,064 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AO, AOH1 |
| Gene groups (HGNC) | Flavoproteins; Xanthine dehydrogenase/aldehyde oxidase family |
| Hallmark sets | XENOBIOTIC_METABOLISM |
| Reactome | 3 pathways, smallest: Vitamin B6 activation to pyridoxal phosphate; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q06278](https://www.uniprot.org/uniprotkb/Q06278) (Aldehyde oxidase):

> Primarily catalyzes oxidation reactions of a broad range of drug and xenobiotic substrates and participates in their metabolism through oxidative biotransformation. Oxidizes at least three structural types of substrates: aldehydes such as benzaldehyde, retinal, pyridoxal, and vanillin; aromatic azaheterocyclic compounds such as phthalazine, quinazoline and phenanthridine; and quaternary azaheterocyclic compounds such as 1-methylnicotinamide and nicotine imine. Converts aldehydes to carboxylic …

**Summary**, from NCBI Gene [316](https://www.ncbi.nlm.nih.gov/gene/316):

> Aldehyde oxidase produces hydrogen peroxide and, under certain conditions, can catalyze the formation of superoxide. Aldehyde oxidase is a candidate gene for amyotrophic lateral sclerosis. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:553](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:553) · Entrez [316](https://www.ncbi.nlm.nih.gov/gene/316) · UniProt [Q06278](https://www.uniprot.org/uniprotkb/Q06278) · Ensembl [ENSG00000138356](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138356)

## Data

Gene col 6158: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6158); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6158, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6158]; `tensor/DDL_lfc|DDL_z.npy` [6158]; `embed/gene_vectors.npy` [6158]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6158 or target_col == 6158). Every well: [[AOX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AOX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
