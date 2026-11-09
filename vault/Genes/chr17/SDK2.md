---
symbol: "SDK2"
type: "gene"
col: 911
ensembl_id: "ENSG00000069188"
name: "sidekick cell adhesion molecule 2"
location: "17q25.1"
module: 102
arm: "+"
pooled_cpm: 9.8
n_lines_expressing: 34
n_dd_up: 26
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 12
direction_downstream: 10
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# SDK2

*sidekick cell adhesion molecule 2* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.95× (z +27.5, q 0e+00, up in 27 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.655× (z -6.0, q 1e-06, down in 15 of 28 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CACNB4]] (+0.67, fdr 7e-06), [[MEGF11]] (+0.64, fdr 3e-05), [[CDH23]] (+0.63, fdr 1e-05); moves opposite to [[TMEM254]] (-0.49, fdr 4e-05).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 10 go from it, the strongest it → [[CACNA1C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 911.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.95×** | +27.5 | 0e+00 | 27/30 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.17×** | +22.4 | 0e+00 | 9/14 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.75×** | +22.1 | 0e+00 | 19/26 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.33×** | +17.0 | 0e+00 | 24/30 (PANC-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.78×** | +13.4 | 6e-39 | 11/19 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.27×** | +11.6 | 2e-29 | 23/30 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.20×** | +11.2 | 4e-27 | 22/30 (SW 900, MIA PaCa-2, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **4.02×** | +10.3 | 4e-23 | 18/21 (BT-474, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.83×** | +8.5 | 8e-16 | 17/31 (A549, SW 900, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.87×** | +8.4 | 4e-15 | 17/29 (A549, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.74×** | +7.9 | 2e-13 | 18/29 (PANC-1, SW 900, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.71×** | +7.6 | 1e-12 | 15/30 (A549, CFPAC-1, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.10×** | +7.5 | 3e-12 | 17/30 (A-172, A549, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.61×** | +6.7 | 6e-10 | 17/31 (PANC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.46×** | +5.4 | 2e-06 | 11/30 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +4.5 | 2e-04 | 6/31 (A549, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.29×** | +3.6 | 0.009 | 6/30 (A-427, C-33 A, …) | all doses, stronger at high dose |  |
| [[Cepharanthine (drug)]] 5 µM |  | 1.16× | +3.0 | 0.066 | 9/30 (MIA PaCa-2, AN3 CA, …) | top dose only |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.23×** | +2.9 | 0.089 | 2/30 (A549, SHP-77) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 911.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.655×** | -6.0 | 1e-06 | 15/28 (NCI-H23, C32, …) | inconsistent across doses | cell-cycle shift (explains ~22% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.683×** | -5.4 | 2e-05 | 21/31 (C-33 A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.717×** | -4.7 | 4e-04 | 12/29 (A-427, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | 0.783× | -3.3 | 0.12 | 6/27 (H4, J82, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[ERK5-IN-2 (drug)]] 5 µM |  | 0.655× | -3.1 | 0.19 | 1/32 (A-172) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 911. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 26.1 | 13 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.17× (z +15.9) | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -15.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 80.3 | 0 | 11 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -18.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.263× (z -9.6) |
| [[PANC-1 (line)]] | alt | 4.49 | 8 (3 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 7.22× (z +14.4) | — |
| [[NCI-H23 (line)]] | alt | 48.7 | 1 | 5 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.33× (z +9.7) | [[Homoharringtonine (drug)]] 5 µM 0.0361× (z -38.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.188× (z -13.7) |
| [[NCI-H460 (line)]] | wt | 6.09 | 6 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +19.0) | — |
| [[A-427 (line)]] | wt | 13.1 | 1 | 3 (3 ⚠) | [[Tucidinostat (drug)]] 5 µM 3.82× (z +9.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -10.7) ⚠ cell-cycle shift, explains ~33% of this change |
| [[AN3 CA (line)]] | alt | 124 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0854× (z -21.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.205× (z -9.8) |
| [[SW480 (line)]] | alt | 13.1 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +11.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.282× (z -8.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 16.5 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.42× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 8.46 | 2 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 10.2× (z +10.4) | — |
| [[NCI-H1573 (line)]] | alt | 9.42 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.96× (z +9.6) | — |
| [[NCI-H2030 (line)]] | alt | 7.36 | 1 | 1 | [[Tucidinostat (drug)]] 5 µM 5.17× (z +10.2) | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.121× (z -8.6) |
| [[C-33 A (line)]] | alt | 19.0 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0965× (z -10.9) |
| [[H4 (line)]] | wt | 13.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.86× (z +11.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 5.45 | 1 | 0 | [[Auranofin (drug)]] 5 µM 16.1× (z +11.1) | — |
| [[SHP-77 (line)]] | alt | 55.6 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.261× (z -10.0) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SK-MEL-2 (line)]] | alt | 5.77 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.27× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 2.45 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 30.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.51× (z +12.5) | — |
| [[A498 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.70 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.61 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.00 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.08 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.65 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.96 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.69 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 911), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CACNB4]] | +0.67 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[MEGF11]] | +0.64 | +0.44 / +0.65 | both halves | 3e-05 |  |
| [[CDH23]] | +0.63 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[GRID1]] | +0.62 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[PHF21B]] | +0.62 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[ZNF536]] | +0.62 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[CACNA2D2]] | +0.61 | +0.57 / +0.56 | both halves | 1e-05 |  |
| [[MED12L]] | +0.61 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[LINC00937]] | +0.61 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[CUX2]] | +0.59 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[RASGEF1C]] | +0.57 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[HAGLR]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM254]] | -0.49 | -0.47 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 8, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SDK2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RHBDL3]] | B | RHBDL3 activity raises SDK2's level | lines that do not express RHBDL3 (9) vs lines expressing it (41) | 2.97× lower at baseline in the lines without RHBDL3 | 0.040 | ⚠ within organs, on part of the lines; also absent: PRDM6, DZIP1L, CACNB4; maybe low, not absent |
| [[JAKMIP1]] | B | JAKMIP1 activity raises SDK2's level | lines that do not express JAKMIP1 (27) vs lines expressing it (23) | 2.98× lower at baseline in the lines without JAKMIP1 | 0.053 | ⚠ within organs, on part of the lines; also absent: CHST8, JPH3, GABBR2 |
| [[WIPF3]] | B | WIPF3 activity strengthens SDK2's drug response | lines that do not express WIPF3 (13) vs lines expressing it (19) | the lines without WIPF3 respond 0.45× as strongly (z diff +1.72); strongest at Bortezomib 5 µM: 1.31x vs 5.09x (z diff +3.5) | 0.060 | ⚠ within organs, on part of the lines; also absent: RBM11, EPB41L4A, COL4A3; target measured in part of the lines; artifact flags |
| [[RET]] | B | RET activity raises SDK2's level | lines that do not express RET (28) vs lines expressing it (22) | 2.97× lower at baseline in the lines without RET | 0.061 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[KCNQ2]] | B | KCNQ2 activity raises SDK2's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 2.33× lower at baseline in the lines without KCNQ2 | 0.069 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P |
| [[DGCR5]] | B | DGCR5 activity raises SDK2's level | lines that do not express DGCR5 (8) vs lines expressing it (42) | 3.02× lower at baseline in the lines without DGCR5 | 0.092 | ⚠ within organs, on part of the lines; also absent: CACNA1B; maybe low, not absent |
| [[GRID1]] | B | GRID1 activity raises SDK2's level | lines that do not express GRID1 (27) vs lines expressing it (23) | 2.15× lower at baseline in the lines without GRID1 | 0.094 | ⚠ within organs, on part of the lines; also absent: LINC02643, EPGN, MSI1; maybe low, not absent |
| [[RAB39A]] | C | RAB39A activity raises SDK2's level | lines that do not express RAB39A (20) vs lines expressing it (30) | 4.22× lower at baseline in the lines without RAB39A | 0.013 | ⚠ within organs, on part of the lines; also absent: RBM20, NOVA2, SDK2; maybe low, not absent; co-absent with the target |
| [[MED12L]] | C | MED12L activity raises SDK2's level | lines that do not express MED12L (18) vs lines expressing it (32) | 3.46× lower at baseline in the lines without MED12L | 0.021 | ⚠ within organs, on part of the lines; also absent: SYNGR1, NPTX1, AP3B2; co-absent with the target |
| [[CACNA1H]] | C | CACNA1H activity raises SDK2's level | lines that do not express CACNA1H (23) vs lines expressing it (27) | 3.33× lower at baseline in the lines without CACNA1H | 0.049 | ⚠ within organs, on part of the lines; also absent: LHX2, LMX1B, JPH3; co-absent with the target |
| [[GNAO1]] | C | GNAO1 activity raises SDK2's level | lines that do not express GNAO1 (22) vs lines expressing it (28) | 2.12× lower at baseline in the lines without GNAO1 | 0.096 | ⚠ within organs, on part of the lines; also absent: MGAT5B, KCNG1, SLC6A17; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 4, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CACNA1C]] | B | SDK2 activity raises CACNA1C's level | lines that do not express SDK2 (16) vs lines expressing it (34) | 2.40× lower at baseline in the lines without SDK2 | 0.056 | ⚠ within organs, on part of the lines; also absent: NRIP3, ZNF549, MGAT5B; maybe low, not absent |
| [[CACNA2D2]] | B | SDK2 activity raises CACNA2D2's level | lines that do not express SDK2 (16) vs lines expressing it (34) | 1.80× lower at baseline in the lines without SDK2 | 0.061 | ⚠ within organs, on part of the lines; also absent: NRIP3, ZNF549, MGAT5B; maybe low, not absent |
| [[RNF125]] | B | SDK2 activity lowers RNF125's level | lines that do not express SDK2 (16) vs lines expressing it (34) | 2.19× higher at baseline in the lines without SDK2 | 0.091 | ⚠ within organs, on part of the lines; also absent: NRIP3, ZNF549, MGAT5B; maybe low, not absent |
| [[KCNQ2]] | B | SDK2 activity raises KCNQ2's level | lines that do not express SDK2 (16) vs lines expressing it (34) | 2.26× lower at baseline in the lines without SDK2 | 0.097 | ⚠ within organs, on part of the lines; also absent: NRIP3, ZNF549, MGAT5B; maybe low, not absent |
| [[NRIP3]] | C | SDK2 activity raises NRIP3's level | lines that do not express SDK2 (16) vs lines expressing it (34) | 4.30× lower at baseline in the lines without SDK2 | 0.019 | ⚠ within organs, on part of the lines; also absent: NRIP3, ZNF549, MGAT5B; maybe low, not absent; co-absent with the target |
| [[PDZD4]] | C | SDK2 activity raises PDZD4's level | lines that do not express SDK2 (16) vs lines expressing it (34) | 3.21× lower at baseline in the lines without SDK2 | 0.023 | ⚠ within organs, on part of the lines; also absent: NRIP3, ZNF549, MGAT5B; maybe low, not absent; co-absent with the target |
| [[GNAO1]] | C | SDK2 activity raises GNAO1's level | lines that do not express SDK2 (16) vs lines expressing it (34) | 3.64× lower at baseline in the lines without SDK2 | 0.025 | ⚠ within organs, on part of the lines; also absent: NRIP3, ZNF549, MGAT5B; maybe low, not absent; co-absent with the target |
| [[RAB39A]] | C | SDK2 activity raises RAB39A's level | lines that do not express SDK2 (16) vs lines expressing it (34) | 2.18× lower at baseline in the lines without SDK2 | 0.065 | ⚠ within organs, on part of the lines; also absent: NRIP3, ZNF549, MGAT5B; maybe low, not absent; co-absent with the target |
| [[JAM3]] | C | SDK2 activity raises JAM3's level | lines that do not express SDK2 (16) vs lines expressing it (34) | 5.39× lower at baseline in the lines without SDK2 | 0.086 | ⚠ within organs, on part of the lines; also absent: NRIP3, ZNF549, MGAT5B; maybe low, not absent; co-absent with the target |
| [[PHF21B]] | C | SDK2 activity raises PHF21B's level | lines that do not express SDK2 (16) vs lines expressing it (34) | 4.05× lower at baseline in the lines without SDK2 | 0.093 | ⚠ within organs, on part of the lines; also absent: NRIP3, ZNF549, MGAT5B; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.759). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.1, 36.9); signed map (27.8, 25.1). **Vector** length 78.9, 16.6% of its response variance represented; |z| ≥ 3 in 954 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.2 | +22.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.8 | +22.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.7 | +27.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.3 | +13.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.9 | +17.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.3 | +11.2 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.5 | +7.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | +7.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +2.1 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -3.2 | -4.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.9 | -5.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.5 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.1 | -0.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.1 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.1 | -0.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -1.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | sidekick cell adhesion molecule 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:73,334,384-73,644,445 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ10832, KIAA1514 |
| Gene groups (HGNC) | Fibronectin type III domain containing; I-set domain containing; Sidekick cell adhesion molecule family |
| Reactome | 3 pathways, smallest: Cell-cell junction organization; Cell junction organization; Cell-Cell communication |
| Matched by | ensembl_id |

**Function**, from UniProt [Q58EX2](https://www.uniprot.org/uniprotkb/Q58EX2) (Protein sidekick-2):

> Adhesion molecule that promotes lamina-specific synaptic connections in the retina and is specifically required for the formation of neuronal circuits that detect motion. Acts by promoting formation of synapses between two specific retinal cell types: the retinal ganglion cells W3B-RGCs and the excitatory amacrine cells VG3-ACs. Formation of synapses between these two cells plays a key role in detection of motion. Promotes synaptic connectivity via homophilic interactions.

**Summary**, from NCBI Gene [54549](https://www.ncbi.nlm.nih.gov/gene/54549):

> The protein encoded by this gene is a member of the immunoglobulin superfamily. The protein contains two immunoglobulin domains and thirteen fibronectin type III domains. Fibronectin type III domains are present in both extracellular and intracellular proteins and tandem repeats are known to contain binding sites for DNA, heparin and the cell surface. This protein, and a homologous mouse sequence, are very similar to the Drosophila sidekick gene product but the specific function of this …

**Accessions** — [HGNC:19308](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19308) · Entrez [54549](https://www.ncbi.nlm.nih.gov/gene/54549) · UniProt [Q58EX2](https://www.uniprot.org/uniprotkb/Q58EX2) · Ensembl [ENSG00000069188](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069188)

## Data

Gene col 911: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 911); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 911, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 911]; `tensor/DDL_lfc|DDL_z.npy` [911]; `embed/gene_vectors.npy` [911]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 911 or target_col == 911). Every well: [[SDK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SDK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
