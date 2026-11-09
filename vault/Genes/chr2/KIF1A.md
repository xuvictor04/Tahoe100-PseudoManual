---
symbol: "KIF1A"
type: "gene"
col: 5044
ensembl_id: "ENSG00000130294"
name: "kinesin family member 1A"
location: "2q37.3"
module: 132
arm: "+"
pooled_cpm: 26.17
n_lines_expressing: 16
n_dd_up: 32
n_dd_down: 6
n_dd_up_clean: 25
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 16
direction_downstream: 36
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# KIF1A

*kinesin family member 1A* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.76× (z +16.7, q 0e+00, up in 9 of 13 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 2.84× (z +13.2, q 3e-37, up in 8 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Anethole trithione (drug)]] 0.5 µM: 0.720× (z -4.1, q 0.012, down in 0 of 14 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RAB6B]] (+0.65, fdr 1e-05), [[KCNQ2]] (+0.60, fdr 9e-06), [[BRSK2]] (+0.58, fdr 2e-05); moves opposite to [[ANKRD17-DT]] (-0.49, fdr 3e-04), [[DECR1]] (-0.49, fdr 1e-04), [[C2orf42]] (-0.46, fdr 1e-04).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[MAP3K15]] → it (grade B ⚠); 36 go from it, the strongest it → [[GPRIN1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5044.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.76×** | +16.7 | 0e+00 | 9/13 (SHP-77, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.01×** | +13.3 | 4e-38 | 7/13 (SW480, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.84×** | +13.2 | 3e-37 | 8/14 (BT-474, MIA PaCa-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.86×** | +12.2 | 3e-32 | 7/13 (SHP-77, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.79×** | +10.4 | 2e-23 | 4/14 (MIA PaCa-2, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.75×** | +9.9 | 3e-21 | 10/14 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.92×** | +7.7 | 8e-13 | 9/14 (BT-474, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.83×** | +7.6 | 2e-12 | 11/14 (BT-474, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.72×** | +6.9 | 5e-10 | 8/13 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.71×** | +6.7 | 9e-10 | 13/14 (BT-474, NCI-H1573, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.70×** | +6.7 | 1e-09 | 9/14 (NCI-H1573, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **2.07×** | +6.6 | 3e-09 | 0/13 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.55×** | +5.5 | 1e-06 | 8/14 (PANC-1, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.54×** | +5.5 | 2e-06 | 9/14 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.54×** | +5.4 | 2e-06 | 0/13 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.53×** | +5.4 | 2e-06 | 9/14 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.50×** | +5.1 | 1e-05 | 9/14 (PANC-1, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.67×** | +4.6 | 1e-04 | 3/14 (BT-474, NCI-H23, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.27×** | +4.2 | 8e-04 | 6/14 (BT-474, MIA PaCa-2, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5044.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.720×** | -4.1 | 0.012 | 0/14 | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | **0.703×** | -4.1 | 0.012 | 0/14 | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | **0.748×** | -3.7 | 0.049 | 0/14 | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.744×** | -3.4 | 0.083 | 0/14 | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.764×** | -3.4 | 0.084 | 8/14 (PANC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.753×** | -3.3 | 0.095 | 0/14 | inconsistent across doses |  |
| [[Lapatinib ditosylate (drug)]] 0.5 µM |  | 0.699× | -3.2 | 0.11 | 0/14 | inconsistent across doses | noisy plate (z scaled) |
| [[(S)-Crizotinib (drug)]] 0.05 µM |  | 0.764× | -3.1 | 0.13 | 0/14 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5044. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 270 | 9 (2 ⚠) | 1 | [[Ixazomib citrate (drug)]] 0.5 µM 4.49× (z +16.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -9.3) |
| [[PANC-1 (line)]] | alt | 61.7 | 2 | 7 (4 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.61× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.166× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.399× (z -12.4) |
| [[A-427 (line)]] | wt | 89.2 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -24.2) |
| [[MIA PaCa-2 (line)]] | alt | 29.3 | 4 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 8.83× (z +19.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.224× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.355× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 141 | 1 | 5 (4 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 2.34× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -20.8) |
| [[NCI-H1573 (line)]] | alt | 89.2 | 3 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 3.30× (z +10.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -14.5) |
| [[SW 900 (line)]] | alt | 98.4 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.337× (z -13.0) |
| [[SW480 (line)]] | alt | 23.6 | 2 (1 ⚠) | 2 | [[Tucidinostat (drug)]] 5 µM 2.32× (z +9.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -11.3) |
| [[SHP-77 (line)]] | alt | 205 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.53× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.02 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 167 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 148 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.72 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.02 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.78 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 3.80 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.92 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.37 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.75 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.42 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.77 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.14 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.71 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.21 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.46 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5044), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RAB6B]] | +0.65 | +0.55 / +0.59 | both halves | 1e-05 | pathway: Golgi-to-ER retrograde transport |
| [[KCNQ2]] | +0.60 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[BRSK2]] | +0.58 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[PDZD4]] | +0.57 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[JPH3]] | +0.57 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[PRKCZ]] | +0.57 | +0.35 / +0.48 | both halves | 1e-04 |  |
| [[DPYSL5]] | +0.56 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[FADS3]] | +0.56 | +0.36 / +0.53 | both halves | 1e-04 |  |
| [[LZTS3]] | +0.56 | +0.40 / +0.58 | both halves | 5e-05 |  |
| [[NXPE3]] | +0.56 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[JAKMIP1]] | +0.56 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[NFASC]] | +0.55 | +0.55 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRD17-DT]] | -0.49 | -0.39 / -0.26 | both halves | 3e-04 |  |
| [[DECR1]] | -0.49 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[C2orf42]] | -0.46 | -0.34 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 3, C 13. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAP3K15]] | B | MAP3K15 activity raises KIF1A's level | lines that do not express MAP3K15 (19) vs lines expressing it (31) | 2.90× lower at baseline in the lines without MAP3K15 | 0.042 | ⚠ within organs, on part of the lines; also absent: FMNL1-DT, NEXMIF, BARX1 |
| [[ADGRB1]] | B | ADGRB1 activity raises KIF1A's level | lines that do not express ADGRB1 (18) vs lines expressing it (32) | 4.15× lower at baseline in the lines without ADGRB1 | 0.070 | ⚠ within organs, on part of the lines; also absent: KSR2, BEGAIN, B4GALNT4; maybe low, not absent |
| [[SEPTIN3]] | B | SEPTIN3 activity raises KIF1A's level | lines that do not express SEPTIN3 (13) vs lines expressing it (37) | 3.91× lower at baseline in the lines without SEPTIN3 | 0.077 | ⚠ within organs, on part of the lines; also absent: SRRM3, GNG4, SEPTIN5; maybe low, not absent |
| [[CBFA2T3]] | C | CBFA2T3 activity raises KIF1A's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 6.27× lower at baseline in the lines without CBFA2T3 | 0.004 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A; co-absent with the target |
| [[LMX1B]] | C | LMX1B activity raises KIF1A's level | lines that do not express LMX1B (24) vs lines expressing it (26) | 6.37× lower at baseline in the lines without LMX1B | 0.006 | ⚠ within organs, on part of the lines; also absent: JPH3, JAKMIP1, GABBR2; co-absent with the target |
| [[NFASC]] | C | NFASC activity raises KIF1A's level | lines that do not express NFASC (27) vs lines expressing it (23) | 4.85× lower at baseline in the lines without NFASC | 0.006 | ⚠ within organs, on part of the lines; also absent: DPYSL5, JPH3, KIF1A; co-absent with the target |
| [[CHD5]] | C | CHD5 activity raises KIF1A's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 5.38× lower at baseline in the lines without CHD5 | 0.011 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent; co-absent with the target |
| [[KCNQ2]] | C | KCNQ2 activity raises KIF1A's level | lines that do not express KCNQ2 (29) vs lines expressing it (21) | 6.45× lower at baseline in the lines without KCNQ2 | 0.015 | ⚠ within organs, on part of the lines; also absent: KIF1A, SULT4A1, ANKRD20A11P; co-absent with the target |
| [[CACNA1H]] | C | CACNA1H activity raises KIF1A's level | lines that do not express CACNA1H (23) vs lines expressing it (27) | 5.06× lower at baseline in the lines without CACNA1H | 0.020 | ⚠ within organs, on part of the lines; also absent: LHX2, LMX1B, JPH3; co-absent with the target |
| [[JPH3]] | C | JPH3 activity raises KIF1A's level | lines that do not express JPH3 (29) vs lines expressing it (21) | 6.36× lower at baseline in the lines without JPH3 | 0.020 | ⚠ within organs, on part of the lines; also absent: OLFM1, JAKMIP1, GABBR2; maybe low, not absent; co-absent with the target |
| [[CTNNA2]] | C | CTNNA2 activity raises KIF1A's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 4.91× lower at baseline in the lines without CTNNA2 | 0.031 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7; co-absent with the target |
| [[NOVA2]] | C | NOVA2 activity raises KIF1A's level | lines that do not express NOVA2 (23) vs lines expressing it (27) | 4.58× lower at baseline in the lines without NOVA2 | 0.037 | ⚠ within organs, on part of the lines; also absent: RBM20, RAB39A, NPTX1; co-absent with the target |

### Downstream of this gene

*36 arrows, 36 of them with an alert ⚠; grade A 0, B 16, C 20. Shown: the 12 strongest; 24 more arrows (24 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPRIN1]] | B | KIF1A activity raises GPRIN1's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 1.92× lower at baseline in the lines without KIF1A | 0.015 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |
| [[SEPTIN3]] | B | KIF1A activity raises SEPTIN3's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 2.28× lower at baseline in the lines without KIF1A | 0.023 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |
| [[MAPT]] | B | KIF1A activity raises MAPT's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 3.15× lower at baseline in the lines without KIF1A | 0.038 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |
| [[FSD1]] | B | KIF1A activity raises FSD1's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 2.49× lower at baseline in the lines without KIF1A | 0.041 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |
| cells under [[Vemurafenib (drug)]] 5 µM | B | KIF1A activity lowers the cells' numbers under Vemurafenib 5 µM (makes them more sensitive) | lines that do not express KIF1A (34) vs lines expressing it (14) | the lines without KIF1A: 1.19× the cells of the other lines | 0.046 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |
| [[REEP1]] | B | KIF1A activity raises REEP1's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 1.67× lower at baseline in the lines without KIF1A | 0.050 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |
| [[ADGRB1]] | B | KIF1A activity raises ADGRB1's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 2.29× lower at baseline in the lines without KIF1A | 0.053 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |
| [[PCYT2]] | B | KIF1A activity raises PCYT2's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 1.11× lower at baseline in the lines without KIF1A | 0.070 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |
| [[KIF26A]] | B | KIF1A activity raises KIF26A's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 2.82× lower at baseline in the lines without KIF1A | 0.073 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |
| [[MLXIPL]] | B | KIF1A activity raises MLXIPL's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 1.23× lower at baseline in the lines without KIF1A | 0.080 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |
| [[MAST1]] | B | KIF1A activity raises MAST1's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 2.12× lower at baseline in the lines without KIF1A | 0.081 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |
| [[CARMIL2]] | B | KIF1A activity raises CARMIL2's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 1.72× lower at baseline in the lines without KIF1A | 0.081 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7 |

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.684). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.6, 40.2); signed map (25.4, 27.5). **Vector** length 58.7, 18.3% of its response variance represented; |z| ≥ 3 in 445 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +13.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +16.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +12.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +9.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.5 | +6.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +13.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.4 | +6.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +4.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.1 | -2.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.6 | -1.0 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.5 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -2.5 | -1.0 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.3 | +4.1 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.1 | -0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.1 | -0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[Anethole trithione (drug)]] 0.5 µM |  | -0.9 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | kinesin family member 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:240,713,761-240,824,293 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UNC104; previously ATSV, C2orf20, SPG30 |
| Gene groups (HGNC) | Kinesins; Pleckstrin homology domain containing |
| Reactome | 8 pathways, smallest: Kinesins; COPI-dependent Golgi-to-ER retrograde traffic; Golgi-to-ER retrograde transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12756](https://www.uniprot.org/uniprotkb/Q12756) (Kinesin-like protein KIF1A):

> Kinesin motor with a plus-end-directed microtubule motor activity (By similarity). It is required for anterograde axonal transport of synaptic vesicle precursors. Also required for neuronal dense core vesicles (DCVs) transport to the dendritic spines and axons. The interaction calcium-dependent with CALM1 increases vesicle motility and interaction with the scaffolding proteins PPFIA2 and TANC2 recruits DCVs to synaptic sites.

**Summary**, from NCBI Gene [547](https://www.ncbi.nlm.nih.gov/gene/547):

> The protein encoded by this gene is a member of the kinesin family and functions as an anterograde motor protein that transports membranous organelles along axonal microtubules. Mutations at this locus have been associated with spastic paraplegia-30 and hereditary sensory neuropathy IIC. Alternatively spliced transcript variants encoding distinct isoforms have been described. [provided by RefSeq, Apr 2012]

**Accessions** — [HGNC:888](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:888) · Entrez [547](https://www.ncbi.nlm.nih.gov/gene/547) · UniProt [Q12756](https://www.uniprot.org/uniprotkb/Q12756) · Ensembl [ENSG00000130294](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130294)

## Data

Gene col 5044: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5044); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5044, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5044]; `tensor/DDL_lfc|DDL_z.npy` [5044]; `embed/gene_vectors.npy` [5044]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5044 or target_col == 5044). Every well: [[KIF1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KIF1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
