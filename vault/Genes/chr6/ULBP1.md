---
symbol: "ULBP1"
type: "gene"
col: 3311
ensembl_id: "ENSG00000111981"
name: "UL16 binding protein 1"
location: "6q25.1"
module: 63
arm: "+"
pooled_cpm: 4.46
n_lines_expressing: 35
n_dd_up: 45
n_dd_down: 14
n_dd_up_clean: 40
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 7
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# ULBP1

*UL16 binding protein 1* — 6q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 45 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.92× (z +18.5, q 0e+00, up in 22 of 29 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (2 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.461× (z -7.4, q 6e-11, down in 21 of 33 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CHAC1]] (+0.75, fdr 7e-06), [[ASNS]] (+0.70, fdr 7e-06), [[CLGN]] (+0.70, fdr 7e-06); moves opposite to [[SPG7]] (-0.48, fdr 1e-04).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ANK2]] → it (grade B ⚠); 7 go from it, the strongest it → [[TRIM36]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 45 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3311.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.92×** | +18.5 | 0e+00 | 22/29 (SW480, A549, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Panobinostat (drug)]] 5 µM |  | **4.82×** | +15.0 | 0e+00 | 30/33 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **3.04×** | +15.0 | 0e+00 | 29/33 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.50×** | +14.4 | 1e-44 | 29/32 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.46×** | +8.6 | 8e-16 | 25/32 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.45×** | +8.2 | 2e-14 | 1/6 (NCI-H2030) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **2.31×** | +8.0 | 1e-13 | 22/33 (NCI-H460, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.27×** | +7.8 | 4e-13 | 22/31 (NCI-H23, HCT15, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM |  | **1.78×** | +7.8 | 5e-13 | 26/33 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.30×** | +7.4 | 1e-11 | 2/7 (MIA PaCa-2, HS-578T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.13×** | +7.2 | 3e-11 | 15/32 (SW480, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **2.09×** | +7.0 | 9e-11 | 19/30 (NCI-H2030, LoVo, …) | two highest doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **2.05×** | +6.8 | 3e-10 | 18/33 (NCI-H2030, NCI-H23, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.98×** | +6.5 | 2e-09 | 18/33 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.57×** | +6.1 | 4e-08 | 18/33 (NCI-H2030, BT-474, …) | two highest doses | position effect removed |
| [[Neratinib (drug)]] 5 µM |  | **1.89×** | +6.1 | 5e-08 | 15/33 (A549, NCI-H460, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.82×** | +5.7 | 4e-07 | 17/33 (HCT15, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 2 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3311.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.461×** | -7.4 | 6e-11 | 21/33 (PANC-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.550×** | -5.7 | 3e-06 | 10/24 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.565×** | -5.5 | 8e-06 | 19/33 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.571×** | -5.4 | 9e-06 | 20/33 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.571×** | -5.4 | 9e-06 | 15/32 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.593×** | -5.0 | 5e-05 | 13/33 (PANC-1, LoVo, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.614×** | -4.7 | 2e-04 | 16/31 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.403×** | -4.6 | 4e-04 | 11/26 (PANC-1, H4, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.644×** | -4.2 | 0.002 | 16/33 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.681×** | -3.7 | 0.012 | 11/33 (HT-29, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.682×** | -3.5 | 0.021 | 13/32 (PANC-1, SW 900, …) | all doses, flat | composition shift |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.779×** | -3.4 | 0.032 | 4/33 (Hs 766T, NCI-H23, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.527×** | -3.2 | 0.057 | 10/33 (PANC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~16% here); composition shift; noisy plate (z scaled) |
| [[Naproxen (drug)]] 5 µM |  | **0.715×** | -3.1 | 0.076 | 9/29 (J82, A549, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3311. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 11.5 | 0 | 12 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0420× (z -19.4) |
| [[SW480 (line)]] | alt | 8.99 | 5 | 4 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.39× (z +15.8) | [[Digitoxin (drug)]] 0.5 µM 0.0837× (z -13.9) |
| [[HT-29 (line)]] | alt | 9.31 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0646× (z -17.8) |
| [[NCI-H23 (line)]] | alt | 24.0 | 3 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +10.0) | [[Digitoxin (drug)]] 5 µM 0.194× (z -9.0) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 4.03 | 0 | 2 | — | [[Crizotinib (hydrochloride) (drug)]] 0.5 µM 0.0859× (z -9.6) |
| [[HOP62 (line)]] | alt | 2.17 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.7× (z +11.1) | — |
| [[hTERT-HPNE (line)]] | wt | 2.99 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.6× (z +10.1) | — |
| [[NCI-H460 (line)]] | wt | 2.35 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.95× (z +8.9) | [[Digitoxin (drug)]] 0.05 µM 0.0664× (z -9.6) |
| [[A549 (line)]] | wt | 2.65 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 17.5× (z +12.3) | — |
| [[H4 (line)]] | wt | 14.6 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0838× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 3.19 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0390× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 14.3 | 0 | 1 | — | [[Digitoxin (drug)]] 0.05 µM 0.204× (z -8.6) |
| [[A-172 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.49 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.330 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.717 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.839 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.380 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.863 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.418 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.85 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.944 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.96 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.489 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.74 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.802 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.374 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.771 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.08 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.64 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3311), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CHAC1]] | +0.75 | +0.65 / +0.74 | both halves | 7e-06 |  |
| [[ASNS]] | +0.70 | +0.58 / +0.73 | both halves | 7e-06 |  |
| [[CLGN]] | +0.70 | +0.60 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[ADM2]] | +0.68 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[PCK2]] | +0.68 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[SARS1]] | +0.68 | +0.50 / +0.72 | both halves | 1e-05 |  |
| [[PHGDH]] | +0.68 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[SESN2]] | +0.67 | +0.54 / +0.69 | both halves | 1e-05 |  |
| [[GARS1]] | +0.66 | +0.45 / +0.68 | both halves | 3e-05 |  |
| [[SLC1A4]] | +0.65 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[ERICH2]] | +0.65 | +0.57 / +0.71 | both halves | 1e-05 |  |
| [[CEBPG]] | +0.64 | +0.57 / +0.64 | both halves | 8e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPG7]] | -0.48 | -0.54 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANK2]] | B | ANK2 activity raises ULBP1's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.51× lower at baseline in the lines without ANK2 | 0.066 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[NIBAN1]] | B | NIBAN1 activity raises ULBP1's level | lines that do not express NIBAN1 (11) vs lines expressing it (39) | 1.74× lower at baseline in the lines without NIBAN1 | 0.094 | ⚠ within organs, on part of the lines; also absent: CAV1, FGF2, PCOLCE2 |
| [[ASNSP1]] | B | ASNSP1 activity raises ULBP1's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.90× lower at baseline in the lines without ASNSP1 | 0.0997 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM36]] | B | ULBP1 activity lowers TRIM36's level | lines that do not express ULBP1 (15) vs lines expressing it (35) | 1.30× higher at baseline in the lines without ULBP1 | 0.037 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[CARS1]] | B | ULBP1 activity raises CARS1's level | lines that do not express ULBP1 (15) vs lines expressing it (35) | 1.46× lower at baseline in the lines without ULBP1 | 0.041 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[IARS1]] | B | ULBP1 activity raises IARS1's level | lines that do not express ULBP1 (15) vs lines expressing it (35) | 1.32× lower at baseline in the lines without ULBP1 | 0.052 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[YARS1]] | B | ULBP1 activity raises YARS1's level | lines that do not express ULBP1 (15) vs lines expressing it (35) | 1.46× lower at baseline in the lines without ULBP1 | 0.054 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[XPOT]] | B | ULBP1 activity raises XPOT's level | lines that do not express ULBP1 (15) vs lines expressing it (35) | 1.39× lower at baseline in the lines without ULBP1 | 0.058 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SLC6A9]] | B | ULBP1 activity raises SLC6A9's level | lines that do not express ULBP1 (15) vs lines expressing it (35) | 1.46× lower at baseline in the lines without ULBP1 | 0.069 | ⚠ within organs, on part of the lines; maybe low, not absent |
| cells under [[Naproxen (drug)]] 5 µM | B | ULBP1 activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express ULBP1 (15) vs lines expressing it (33) | the lines without ULBP1: 0.87× the cells of the other lines | 0.095 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.718). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.4, 48.4); signed map (-12.3, 23.8). **Vector** length 70.5, 13.9% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mTORC1 signaling* (hallmark, mean cos +0.53 to 20); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.59 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.59 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +15.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.6 | +8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +7.8 |
|  | [[Artesunate (drug)]] 5 µM |  | +4.0 | +7.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.7 | +8.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.6 | +6.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +3.3 | +6.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.5 | -5.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.4 | -7.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.2 | -4.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.1 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.1 | -5.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.4 | -1.4 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -1.1 | -2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.0 | -2.6 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | -1.0 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | UL16 binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.1 — chr6:149,963,943-149,973,715 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RAET1I |
| Gene groups (HGNC) | Retinoic acid early transcript 1 family |
| Reactome | 2 pathways, smallest: Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZM6](https://www.uniprot.org/uniprotkb/Q9BZM6) (UL16-binding protein 1):

> Binds and activates the KLRK1/NKG2D receptor, mediating natural killer cell cytotoxicity.

**Summary**, from NCBI Gene [80329](https://www.ncbi.nlm.nih.gov/gene/80329):

> The protein encoded by this gene is a ligand of natural killer group 2, member D (NKG2D), an immune system-activating receptor on NK cells and T-cells. Binding of the encoded ligand to NKG2D leads to activation of several signal transduction pathways, including those of JAK2, STAT5, ERK and PI3K kinase/Akt. Also, in cytomegalovirus-infected cells, this ligand binds the UL16 glycoprotein and is prevented from activating the immune system. Three transcript variants encoding different isoforms …

**Accessions** — [HGNC:14893](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14893) · Entrez [80329](https://www.ncbi.nlm.nih.gov/gene/80329) · UniProt [Q9BZM6](https://www.uniprot.org/uniprotkb/Q9BZM6) · Ensembl [ENSG00000111981](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111981)

## Data

Gene col 3311: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3311); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3311, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3311]; `tensor/DDL_lfc|DDL_z.npy` [3311]; `embed/gene_vectors.npy` [3311]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3311 or target_col == 3311). Every well: [[ULBP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ULBP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
