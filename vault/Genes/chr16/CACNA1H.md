---
symbol: "CACNA1H"
type: "gene"
col: 12236
ensembl_id: "ENSG00000196557"
name: "calcium voltage-gated channel subunit alpha1 H"
location: "16p13.3"
module: 132
arm: "+"
pooled_cpm: 6.76
n_lines_expressing: 27
n_dd_up: 7
n_dd_down: 13
n_dd_up_clean: 7
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 11
direction_downstream: 9
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# CACNA1H

*calcium voltage-gated channel subunit alpha1 H* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 2.50× (z +11.5, q 5e-28, up in 13 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (4 with an alert ⚠); the strongest is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 0.492× (z -6.1, q 8e-07, down in 15 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SHANK3]] (+0.65, fdr 1e-05), [[IQSEC1]] (+0.65, fdr 1e-05), [[BRSK2]] (+0.64, fdr 1e-05); moves opposite to [[AHI1-DT]] (-0.50, fdr 3e-04), [[NIFK-AS1]] (-0.49, fdr 3e-04), [[ERCC6L2-AS1]] (-0.49, fdr 4e-04).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[CBFA2T3]] → it (grade B ⚠); 9 go from it, the strongest it → [[SLC48A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12236.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **2.50×** | +11.5 | 5e-28 | 13/24 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.61×** | +8.6 | 3e-15 | 20/24 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.36×** | +7.7 | 3e-12 | 11/23 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.36×** | +7.6 | 3e-12 | 17/23 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.96×** | +6.0 | 2e-07 | 15/24 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.81×** | +5.3 | 1e-05 | 8/24 (NCI-H1573, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +4.0 | 0.006 | 11/23 (SW480, SW 900, …) | top dose only |  |
| [[Budesonide (drug)]] 5 µM |  | 1.41× | +3.1 | 0.16 | 3/24 (A498, NCI-H1573, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12236.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.492×** | -6.1 | 8e-07 | 15/23 (A-172, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.580×** | -4.8 | 4e-04 | 11/24 (C32, A-427, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.603×** | -4.3 | 0.003 | 10/21 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.627×** | -4.0 | 0.010 | 13/19 (HepG2/C3A, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.656×** | -3.7 | 0.021 | 9/20 (C32, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **0.664×** | -3.6 | 0.027 | 7/24 (LOX-IMVI, C32, …) | inconsistent across doses | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~61% of this change | **0.668×** | -3.6 | 0.028 | 12/22 (SW480, PANC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.674×** | -3.5 | 0.033 | 7/23 (HepG2/C3A, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.760×** | -3.4 | 0.037 | 14/20 (C32, KATO III, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.765×** | -3.3 | 0.047 | 12/24 (SK-MEL-2, A-172, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.702×** | -3.1 | 0.090 | 7/23 (NCI-H460, C32, …) | rises with dose |  |
| [[Sulfatinib (drug)]] 5 µM |  | **0.697×** | -3.1 | 0.097 | 8/23 (KATO III, AN3 CA, …) | top dose only | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.698×** | -3.1 | 0.097 | 2/24 (CFPAC-1, C-33 A) | top dose only | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.786× | -3.0 | 0.10 | 8/25 (A-172, PANC-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.23 per unit of S-phase module lfc, -0.36 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12236. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 16.9 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.165× (z -10.7) |
| [[SW480 (line)]] | alt | 13.5 | 1 | 3 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.25× (z +8.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -10.7) |
| [[HepG2_C3A (line)]] | wt | 49.1 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.134× (z -10.6) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -9.9) |
| [[SK-MEL-2 (line)]] | alt | 12.8 | 0 | 3 (1 ⚠) | — | [[Cobimetinib (drug)]] 5 µM 0.0549× (z -10.0) |
| [[A-172 (line)]] | wt | 11.8 | 0 | 2 (1 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0468× (z -11.5) |
| [[KATO III (line)]] | alt | 7.28 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0842× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 3.43 | 0 | 2 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0934× (z -9.3) |
| [[A549 (line)]] | wt | 5.27 | 0 | 1 (1 ⚠) | — | [[Fingolimod (hydrochloride) (drug)]] 5 µM 0.0701× (z -10.0) ⚠ toxic |
| [[AN3 CA (line)]] | alt | 30.8 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0788× (z -8.6) |
| [[A-427 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.518 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.759 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.514 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.73 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.662 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.833 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.859 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.687 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.402 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.77 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.967 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.431 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.65 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.506 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.347 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.449 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.514 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 5.61 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.780 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.612 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12236), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SHANK3]] | +0.65 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[IQSEC1]] | +0.65 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[BRSK2]] | +0.64 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[SDC3]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[IGSF9B]] | +0.62 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[RASGEF1C]] | +0.62 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[PRR5]] | +0.61 | +0.53 / +0.55 | both halves | 1e-05 | pathway: Cellular responses to mechanical stimuli |
| [[GRAMD4]] | +0.61 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[NSMF]] | +0.60 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[R3HDM4]] | +0.58 | +0.44 / +0.47 | both halves | 3e-05 |  |
| [[GNAZ]] | +0.58 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[ZFYVE28]] | +0.58 | +0.53 / +0.38 | both halves | 7e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHI1-DT]] | -0.50 | -0.45 / -0.27 | both halves | 3e-04 |  |
| [[NIFK-AS1]] | -0.49 | -0.43 / -0.29 | both halves | 3e-04 |  |
| [[ERCC6L2-AS1]] | -0.49 | -0.43 / -0.25 | both halves | 4e-04 |  |
| [[RNF170]] | -0.49 | -0.48 / -0.32 | both halves | 2e-04 |  |
| [[DNAI4]] | -0.48 | -0.45 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 4, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CBFA2T3]] | B | CBFA2T3 activity raises CACNA1H's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 2.30× lower at baseline in the lines without CBFA2T3 | 0.028 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers CACNA1H's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers CACNA1H's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[TOP2A]] | B | TOP2A activity raises CACNA1H's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[KIF1A]] | C | KIF1A activity raises CACNA1H's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 3.31× lower at baseline in the lines without KIF1A | 0.001 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7; co-absent with the target |
| [[JAKMIP1]] | C | JAKMIP1 activity raises CACNA1H's level | lines that do not express JAKMIP1 (27) vs lines expressing it (23) | 3.53× lower at baseline in the lines without JAKMIP1 | 0.002 | ⚠ within organs, on part of the lines; also absent: CHST8, JPH3, GABBR2; co-absent with the target |
| [[CHD5]] | C | CHD5 activity raises CACNA1H's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 2.39× lower at baseline in the lines without CHD5 | 0.006 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent; co-absent with the target |
| [[NOVA2]] | C | NOVA2 activity raises CACNA1H's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 2.88× lower at baseline in the lines without NOVA2 | 0.010 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1; co-absent with the target |
| [[KCNQ2]] | C | KCNQ2 activity raises CACNA1H's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 2.24× lower at baseline in the lines without KCNQ2 | 0.011 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P; co-absent with the target |
| [[B4GALNT4]] | C | B4GALNT4 activity raises CACNA1H's level | lines that do not express B4GALNT4 (18) vs lines expressing it (32) | 2.99× lower at baseline in the lines without B4GALNT4 | 0.095 | ⚠ within organs, on part of the lines; also absent: SRRM3, ST6GAL1, KIF26A; co-absent with the target |
| [[ADGRB1]] | C | ADGRB1 activity raises CACNA1H's level | lines that do not express ADGRB1 (18) vs lines expressing it (32) | 2.25× lower at baseline in the lines without ADGRB1 | 0.0999 | ⚠ within organs, on part of the lines; also absent: KSR2, BEGAIN, B4GALNT4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 3, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC48A1]] | B | CACNA1H activity raises SLC48A1's level | lines that do not express CACNA1H (23) vs lines expressing it (27) | 1.39× lower at baseline in the lines without CACNA1H | 0.013 | ⚠ within organs, on part of the lines; also absent: LHX2, LMX1B, JPH3 |
| [[PLCXD1]] | B | CACNA1H activity raises PLCXD1's level | lines that do not express CACNA1H (23) vs lines expressing it (27) | 1.66× lower at baseline in the lines without CACNA1H | 0.066 | ⚠ within organs, on part of the lines; also absent: LHX2, LMX1B, JPH3 |
| [[FBXL16]] | B | CACNA1H activity raises FBXL16's level | lines that do not express CACNA1H (23) vs lines expressing it (27) | 1.55× lower at baseline in the lines without CACNA1H | 0.077 | ⚠ within organs, on part of the lines; also absent: LHX2, LMX1B, JPH3 |
| [[ADGRB1]] | C | CACNA1H activity raises ADGRB1's level | lines that do not express CACNA1H (23) vs lines expressing it (27) | 2.52× lower at baseline in the lines without CACNA1H | 0.015 | ⚠ within organs, on part of the lines; also absent: LHX2, LMX1B, JPH3; co-absent with the target |
| [[KIF1A]] | C | CACNA1H activity raises KIF1A's level | lines that do not express CACNA1H (23) vs lines expressing it (27) | 5.06× lower at baseline in the lines without CACNA1H | 0.020 | ⚠ within organs, on part of the lines; also absent: LHX2, LMX1B, JPH3; co-absent with the target |
| [[GLDC]] | C | CACNA1H activity raises GLDC's level | lines that do not express CACNA1H (23) vs lines expressing it (27) | 2.41× lower at baseline in the lines without CACNA1H | 0.044 | ⚠ within organs, on part of the lines; also absent: LHX2, LMX1B, JPH3; co-absent with the target |
| [[SDK2]] | C | CACNA1H activity raises SDK2's level | lines that do not express CACNA1H (23) vs lines expressing it (27) | 3.33× lower at baseline in the lines without CACNA1H | 0.049 | ⚠ within organs, on part of the lines; also absent: LHX2, LMX1B, JPH3; co-absent with the target |
| [[CHD5]] | C | CACNA1H activity raises CHD5's level | lines that do not express CACNA1H (23) vs lines expressing it (27) | 2.08× lower at baseline in the lines without CACNA1H | 0.095 | ⚠ within organs, on part of the lines; also absent: LHX2, LMX1B, JPH3; co-absent with the target |
| [[KCNQ2]] | C | CACNA1H activity raises KCNQ2's level | lines that do not express CACNA1H (23) vs lines expressing it (27) | 2.28× lower at baseline in the lines without CACNA1H | 0.096 | ⚠ within organs, on part of the lines; also absent: LHX2, LMX1B, JPH3; co-absent with the target |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.705). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.8, 42.4); signed map (-14.6, 42.4). **Vector** length 57.1, 13.5% of its response variance represented; |z| ≥ 3 in 542 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.2 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.5 | +0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +4.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.7 | +0.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.7 | +1.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.3 | +2.9 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -1.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -1.7 | -3.1 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -1.6 | -4.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.5 | -2.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -0.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.2 | -0.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -1.1 | -1.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | calcium voltage-gated channel subunit alpha1 H |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:1,153,103-1,224,169 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Cav3.2 |
| Gene groups (HGNC) | Calcium voltage-gated channel alpha1 subunits |
| Hallmark sets | MYOGENESIS, GLYCOLYSIS |
| Reactome | 9 pathways, smallest: Mechanical load activates signaling by PIEZO1 and integrins in osteocytes; NCAM1 interactions; Smooth Muscle Contraction |
| Matched by | ensembl_id |

**Function**, from UniProt [O95180](https://www.uniprot.org/uniprotkb/O95180) (Voltage-dependent T-type calcium channel subunit alpha-1H):

> Voltage-sensitive calcium channel that gives rise to T-type calcium currents. T-type calcium channels belong to the 'low-voltage activated (LVA)' group. A particularity of this type of channel is an opening at quite negative potentials, and a voltage-dependent inactivation. T-type channels serve pacemaking functions in both central neurons and cardiac nodal cells and support calcium signaling in secretory cells and vascular smooth muscle (Probable). They may also be involved in the modulation …

**Summary**, from NCBI Gene [8912](https://www.ncbi.nlm.nih.gov/gene/8912):

> This gene encodes a T-type member of the alpha-1 subunit family, a protein in the voltage-dependent calcium channel complex. Calcium channels mediate the influx of calcium ions into the cell upon membrane polarization and consist of a complex of alpha-1, alpha-2/delta, beta, and gamma subunits in a 1:1:1:1 ratio. The alpha-1 subunit has 24 transmembrane segments and forms the pore through which ions pass into the cell. There are multiple isoforms of each of the proteins in the complex, either …

**Accessions** — [HGNC:1395](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1395) · Entrez [8912](https://www.ncbi.nlm.nih.gov/gene/8912) · UniProt [O95180](https://www.uniprot.org/uniprotkb/O95180) · Ensembl [ENSG00000196557](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196557)

## Data

Gene col 12236: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12236); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12236, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12236]; `tensor/DDL_lfc|DDL_z.npy` [12236]; `embed/gene_vectors.npy` [12236]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12236 or target_col == 12236). Every well: [[CACNA1H — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CACNA1H.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
