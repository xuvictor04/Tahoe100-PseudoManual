---
symbol: "TNFRSF9"
type: "gene"
col: 549
ensembl_id: "ENSG00000049249"
name: "TNF receptor superfamily member 9"
location: "1p36.23"
module: 14
arm: "+"
pooled_cpm: 7.3
n_lines_expressing: 30
n_dd_up: 48
n_dd_down: 19
n_dd_up_clean: 32
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 9
direction_downstream: 17
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# TNFRSF9

*TNF receptor superfamily member 9* — 1p36.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 48 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 36.6× (z +50.7, q 0e+00, up in 25 of 25 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (none with an alert); the strongest is [[Betamethasone dipropionate (drug)]] 0.5 µM: 0.509× (z -6.7, q 9e-09, down in 12 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SSTR2]] (+0.75, fdr 7e-06), [[RRAD]] (+0.72, fdr 7e-06), [[MIR155HG]] (+0.69, fdr 7e-06).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 17 go from it, the strongest it → [[NINJ1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 16 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 48 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 549.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **36.6×** | +50.7 | 0e+00 | 25/25 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **21.5×** | +29.4 | 0e+00 | 25/26 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **15.7×** | +27.4 | 0e+00 | 24/25 (A-172, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **7.37×** | +19.9 | 0e+00 | 26/28 (A549, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **6.45×** | +18.6 | 0e+00 | 26/28 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **3.53×** | +17.8 | 0e+00 | 24/27 (SW 900, Hs 766T, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **5.18×** | +16.4 | 0e+00 | 25/27 (A549, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **4.84×** | +15.7 | 0e+00 | 25/27 (A498, HS-578T, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.00×** | +11.0 | 4e-26 | 25/28 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.73×** | +10.0 | 7e-22 | 21/25 (SW 900, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.98×** | +9.6 | 4e-20 | 13/25 (HOP62, J82, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.66×** | +9.4 | 4e-19 | 3/14 (A549, A498, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.37×** | +8.6 | 4e-16 | 22/28 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.14×** | +7.6 | 2e-12 | 17/25 (HOP62, A-172, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **3.87×** | +7.1 | 7e-11 | 19/25 (A549, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.60×** | +6.6 | 2e-09 | 12/27 (HOP62, J82, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.87×** | +6.3 | 1e-08 | 10/26 (A-172, A498, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, none with an alert; shown: the 15 strongest. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 549.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.509×** | -6.7 | 9e-09 | 12/25 (A498, A549, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.526×** | -6.4 | 4e-08 | 17/25 (A549, HS-578T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **0.569×** | -5.6 | 3e-06 | 18/25 (A549, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.579×** | -5.5 | 7e-06 | 15/27 (HS-578T, SNU-423, …) | all doses, flat |  |
| [[Budesonide (drug)]] 5 µM |  | **0.583×** | -5.4 | 7e-06 | 19/28 (A549, HS-578T, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.584×** | -5.4 | 7e-06 | 14/25 (HS-578T, HEC-1-A, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.585×** | -5.4 | 7e-06 | 16/25 (A549, HS-578T, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.592×** | -5.2 | 1e-05 | 17/27 (HS-578T, A549, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.594×** | -5.2 | 1e-05 | 12/25 (A498, NCI-H2347, …) | top dose only |  |
| [[Econazole (drug)]] 5 µM |  | **0.648×** | -4.3 | 8e-04 | 13/27 (NCI-H2347, A498, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.651×** | -4.3 | 9e-04 | 13/25 (RPMI-7951, HS-578T, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.660×** | -4.2 | 0.002 | 12/25 (HS-578T, A549, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.05 µM |  | **0.689×** | -3.7 | 0.008 | 11/26 (A498, A549, …) | all doses, flat |  |
| [[Quinestrol (drug)]] 5 µM |  | **0.770×** | -3.7 | 0.009 | 10/27 (A549, SW 1088, …) | rises with dose | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.682×** | -3.5 | 0.015 | 12/25 (A549, A498, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.54 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 549. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 15.8 | 7 | 2 | [[Homoharringtonine (drug)]] 5 µM 24.7× (z +22.6) | [[Clobetasol propionate (drug)]] 0.05 µM 0.163× (z -9.1) |
| [[PANC-1 (line)]] | alt | 2.58 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 74.7× (z +22.0) | — |
| [[HS-578T (line)]] | alt | 42.0 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +24.9) | — |
| [[MIA PaCa-2 (line)]] | alt | 26.6 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 17.5× (z +22.2) | [[Dinaciclib (drug)]] 5 µM 0.0953× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[A-172 (line)]] | wt | 14.7 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 37.4× (z +23.7) | — |
| [[A498 (line)]] | wt | 15.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.2× (z +23.8) | — |
| [[HOP62 (line)]] | alt | 14.4 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 62.1× (z +26.5) | — |
| [[CFPAC-1 (line)]] | alt | 4.80 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 76.1× (z +21.1) | — |
| [[HEC-1-A (line)]] | alt | 2.34 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 53.5× (z +15.5) | — |
| [[hTERT-HPNE (line)]] | wt | 8.15 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 41.1× (z +15.5) | — |
| [[J82 (line)]] | alt | 12.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 65.4× (z +21.7) | — |
| [[NCI-H2347 (line)]] | alt | 20.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.9× (z +21.2) | — |
| [[Panc 03.27 (line)]] | alt | 6.89 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 43.6× (z +20.2) | — |
| [[RPMI-7951 (line)]] | alt | 16.1 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 15.6× (z +15.7) | [[Clobetasol propionate (drug)]] 0.5 µM 0.105× (z -9.1) |
| [[SNU-423 (line)]] | alt | 17.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 46.4× (z +24.0) | — |
| [[SW 900 (line)]] | alt | 9.78 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 41.6× (z +18.7) | — |
| [[HepG2_C3A (line)]] | wt | 4.54 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 99.2× (z +13.6) | — |
| [[NCI-H1573 (line)]] | alt | 2.00 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 39.5× (z +12.2) | — |
| [[NCI-H1792 (line)]] | alt | 12.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.7× (z +16.8) | — |
| [[H4 (line)]] | wt | 27.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +10.3) | — |
| [[HCT15 (line)]] | alt | 3.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 20.9× (z +10.4) | — |
| [[Hs 766T (line)]] | wt | 7.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.2× (z +16.3) | — |
| [[SHP-77 (line)]] | alt | 5.68 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.45× (z +9.1) | — |
| [[SK-MEL-2 (line)]] | alt | 2.19 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 83.9× (z +8.5) | — |
| [[A-427 (line)]] | wt | 0.663 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.27 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.926 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.676 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.881 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.15 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.737 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.627 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.819 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.01 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.55 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 549), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SSTR2]] | +0.75 | +0.73 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[RRAD]] | +0.72 | +0.69 / +0.66 | both halves | 7e-06 |  |
| [[MIR155HG]] | +0.69 | +0.60 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[NEURL3]] | +0.68 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[TRAF1]] | +0.66 | +0.59 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_IL2_STAT5_SIGNALING; STRING 984 |
| [[SLAMF7]] | +0.66 | +0.58 / +0.67 | both halves | 8e-06 | same gene group; STRING 510 |
| [[SERPINB7]] | +0.65 | +0.62 / +0.65 | both halves | 7e-06 |  |
| [[CD274]] | +0.63 | +0.64 / +0.59 | both halves | 7e-06 | same gene group; STRING 899 |
| [[CGNL1]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[CSF2]] | +0.62 | +0.54 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_IL2_STAT5_SIGNALING; STRING 681 |
| [[AKR1B1]] | +0.62 | +0.55 / +0.67 | both halves | 1e-05 |  |
| [[GATM]] | +0.62 | +0.60 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity lowers TNFRSF9's level | compounds that target NR3C1: 3 of 3 lower it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 2.8% of all compounds | 0.028 | ⚠ off-target possible; 3 compounds |
| [[NINJ1]] | B | NINJ1 activity raises TNFRSF9's level | lines that do not express NINJ1 (5) vs lines expressing it (45) | 2.98× lower at baseline in the lines without NINJ1 | 0.052 | ⚠ within organs, on part of the lines; also absent: FAM102A, ZMIZ1, MBNL2; maybe low, not absent |
| [[ADGRG1]] | B | ADGRG1 activity raises TNFRSF9's level | lines that do not express ADGRG1 (12) vs lines expressing it (38) | 2.43× lower at baseline in the lines without ADGRG1 | 0.080 | ⚠ within organs, on part of the lines; also absent: LGALS3, PDGFB, ENSG00000249526 |
| [[GBP5]] | C | GBP5 activity raises TNFRSF9's level | lines that do not express GBP5 (24) vs lines expressing it (26) | 3.61× lower at baseline in the lines without GBP5 | 0.007 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, EDNRA, CHSY3; co-absent with the target |
| [[ROR1-AS1]] | C | ROR1-AS1 activity raises TNFRSF9's level | lines that do not express ROR1-AS1 (26) vs lines expressing it (24) | 3.08× lower at baseline in the lines without ROR1-AS1 | 0.009 | ⚠ within organs, on part of the lines; also absent: LINC01705, COL4A2, ADAMTS9-AS2; co-absent with the target |
| [[RRAD]] | C | RRAD activity raises TNFRSF9's level | lines that do not express RRAD (31) vs lines expressing it (19) | 2.84× lower at baseline in the lines without RRAD | 0.046 | ⚠ within organs, on part of the lines; also absent: LOX, IL6, EDNRA; co-absent with the target |
| [[LINC02605]] | C | LINC02605 activity raises TNFRSF9's level | lines that do not express LINC02605 (15) vs lines expressing it (35) | 2.70× lower at baseline in the lines without LINC02605 | 0.052 | ⚠ within organs, on part of the lines; also absent: ENSG00000285744, FAR2, ENSG00000285517; co-absent with the target |
| [[SHISAL1]] | C | SHISAL1 activity raises TNFRSF9's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 2.72× lower at baseline in the lines without SHISAL1 | 0.085 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11; co-absent with the target |
| [[TNFAIP6]] | C | TNFAIP6 activity raises TNFRSF9's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 3.03× lower at baseline in the lines without TNFAIP6 | 0.092 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 8, C 9. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NINJ1]] | B | TNFRSF9 activity raises NINJ1's level | lines that do not express TNFRSF9 (20) vs lines expressing it (30) | 2.50× lower at baseline in the lines without TNFRSF9 | 0.024 | ⚠ within organs, on part of the lines; also absent: GBP5, DKK3, CDH2 |
| [[BHLHE40]] | B | TNFRSF9 activity raises BHLHE40's level | lines that do not express TNFRSF9 (20) vs lines expressing it (30) | 1.71× lower at baseline in the lines without TNFRSF9 | 0.037 | ⚠ within organs, on part of the lines; also absent: GBP5, DKK3, CDH2 |
| [[RASSF5]] | B | TNFRSF9 activity raises RASSF5's level | lines that do not express TNFRSF9 (20) vs lines expressing it (30) | 1.76× lower at baseline in the lines without TNFRSF9 | 0.039 | ⚠ within organs, on part of the lines; also absent: GBP5, DKK3, CDH2 |
| [[TRAF1]] | B | TNFRSF9 activity raises TRAF1's level | lines that do not express TNFRSF9 (20) vs lines expressing it (30) | 2.98× lower at baseline in the lines without TNFRSF9 | 0.051 | ⚠ within organs, on part of the lines; also absent: GBP5, DKK3, CDH2 |
| [[CADM1]] | B | TNFRSF9 activity raises CADM1's level | lines that do not express TNFRSF9 (20) vs lines expressing it (30) | 3.59× lower at baseline in the lines without TNFRSF9 | 0.067 | ⚠ within organs, on part of the lines; also absent: GBP5, DKK3, CDH2 |
| [[NEURL3]] | B | TNFRSF9 activity raises NEURL3's level | lines that do not express TNFRSF9 (20) vs lines expressing it (30) | 2.03× lower at baseline in the lines without TNFRSF9 | 0.068 | ⚠ within organs, on part of the lines; also absent: GBP5, DKK3, CDH2 |
| [[MARCKS]] | B | TNFRSF9 activity raises MARCKS's level | lines that do not express TNFRSF9 (20) vs lines expressing it (30) | 3.27× lower at baseline in the lines without TNFRSF9 | 0.083 | ⚠ within organs, on part of the lines; also absent: GBP5, DKK3, CDH2 |
| [[RPLP0P2]] | B | TNFRSF9 activity raises RPLP0P2's level | lines that do not express TNFRSF9 (20) vs lines expressing it (30) | 1.61× lower at baseline in the lines without TNFRSF9 | 0.086 | ⚠ within organs, on part of the lines; also absent: GBP5, DKK3, CDH2 |
| [[CD40]] | C | TNFRSF9 activity raises CD40's level | lines that do not express TNFRSF9 (20) vs lines expressing it (30) | 3.92× lower at baseline in the lines without TNFRSF9 | 0.010 | ⚠ within organs, on part of the lines; also absent: GBP5, DKK3, CDH2; co-absent with the target |
| [[PLAU]] | C | TNFRSF9 activity raises PLAU's level | lines that do not express TNFRSF9 (20) vs lines expressing it (30) | 4.24× lower at baseline in the lines without TNFRSF9 | 0.013 | ⚠ within organs, on part of the lines; also absent: GBP5, DKK3, CDH2; co-absent with the target |
| [[LINC02605]] | C | TNFRSF9 activity raises LINC02605's level | lines that do not express TNFRSF9 (20) vs lines expressing it (30) | 2.45× lower at baseline in the lines without TNFRSF9 | 0.038 | ⚠ within organs, on part of the lines; also absent: GBP5, DKK3, CDH2; co-absent with the target |
| [[ROR1-AS1]] | C | TNFRSF9 activity raises ROR1-AS1's level | lines that do not express TNFRSF9 (20) vs lines expressing it (30) | 2.99× lower at baseline in the lines without TNFRSF9 | 0.038 | ⚠ within organs, on part of the lines; also absent: GBP5, DKK3, CDH2; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.684). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.9, 1.8); signed map (42.3, 12.4). **Vector** length 91.5, 26.3% of its response variance represented; |z| ≥ 3 in 917 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +17.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.3 | +29.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +10.0 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.2 | +15.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.2 | +27.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.9 | +6.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +2.7 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +3.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +2.8 |
| fall | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.5 | -4.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.2 | -6.4 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -3.1 | -5.2 |
|  | [[Budesonide (drug)]] 5 µM |  | -3.1 | -5.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -3.1 | -4.2 |

## What is on record

|  |  |
|---|---|
| Name | TNF receptor superfamily member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.23 — chr1:7,915,871-7,943,165 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD137, 4-1BB; previously ILA |
| Gene groups (HGNC) | CD molecules; Tumor necrosis factor receptor superfamily |
| Hallmark sets | INFLAMMATORY_RESPONSE, IL2_STAT5_SIGNALING, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 3 pathways, smallest: TNFs bind their physiological receptors; TNFR2 non-canonical NF-kB pathway; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q07011](https://www.uniprot.org/uniprotkb/Q07011) (Tumor necrosis factor receptor superfamily member 9):

> Receptor for TNFSF9/4-1BBL. Conveys a signal that enhances CD8(+) T-cell survival, cytotoxicity, and mitochondrial activity, thereby promoting immunity against viruses and tumors (Probable).

**Summary**, from NCBI Gene [3604](https://www.ncbi.nlm.nih.gov/gene/3604):

> The protein encoded by this gene is a member of the TNF-receptor superfamily. This receptor contributes to the clonal expansion, survival, and development of T cells. It can also induce proliferation in peripheral monocytes, enhance T cell apoptosis induced by TCR/CD3 triggered activation, and regulate CD28 co-stimulation to promote Th1 cell responses. The expression of this receptor is induced by lymphocyte activation. TRAF adaptor proteins have been shown to bind to this receptor and …

**Accessions** — [HGNC:11924](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11924) · Entrez [3604](https://www.ncbi.nlm.nih.gov/gene/3604) · UniProt [Q07011](https://www.uniprot.org/uniprotkb/Q07011) · Ensembl [ENSG00000049249](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000049249)

## Data

Gene col 549: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 549); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 549, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 549]; `tensor/DDL_lfc|DDL_z.npy` [549]; `embed/gene_vectors.npy` [549]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 549 or target_col == 549). Every well: [[TNFRSF9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TNFRSF9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
