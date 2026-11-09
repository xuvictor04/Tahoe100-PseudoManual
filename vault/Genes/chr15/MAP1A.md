---
symbol: "MAP1A"
type: "gene"
col: 9395
ensembl_id: "ENSG00000166963"
name: "microtubule associated protein 1A"
location: "15q15.3"
module: 117
arm: "+"
pooled_cpm: 8.12
n_lines_expressing: 33
n_dd_up: 44
n_dd_down: 4
n_dd_up_clean: 33
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 14
direction_downstream: 17
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# MAP1A

*microtubule associated protein 1A* — 15q15.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 44 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 13.1× (z +22.0, q 0e+00, up in 25 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.05 µM: 0.503× (z -5.9, q 2e-06, down in 17 of 29 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TDO2]] (+0.61, fdr 1e-05), [[B4GALNT1]] (+0.57, fdr 1e-05), [[NXPE3]] (+0.55, fdr 1e-05); moves opposite to [[ENTR1]] (-0.47, fdr 8e-05), [[MECR]] (-0.43, fdr 2e-04), [[EXOSC7]] (-0.42, fdr 1e-04).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 17 go from it, the strongest it → [[CNPY4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 44 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9395.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **13.1×** | +22.0 | 0e+00 | 25/30 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.00×** | +21.6 | 0e+00 | 18/26 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **10.7×** | +20.3 | 0e+00 | 26/30 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **6.79×** | +16.4 | 0e+00 | 26/30 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.49×** | +10.7 | 2e-24 | 26/30 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | **2.95×** | +9.2 | 2e-18 | 15/21 (A498, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | **3.05×** | +9.2 | 4e-18 | 9/11 (A498, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **2.48×** | +7.8 | 6e-13 | 18/29 (CHP-212, A-172, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.40×** | +7.1 | 8e-11 | 16/28 (NCI-H1792, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.80×** | +7.1 | 8e-11 | 15/29 (HT-29, SW480, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **4.76×** | +7.0 | 2e-10 | 22/29 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **2.21×** | +6.5 | 4e-09 | 10/23 (SW480, MIA PaCa-2, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **2.21×** | +6.2 | 2e-08 | 6/13 (A498, SHP-77, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.67×** | +6.2 | 2e-08 | 10/29 (SW480, SW1417, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.00×** | +5.9 | 1e-07 | 16/28 (HT-29, hTERT-HPNE, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +5.9 | 1e-07 | 10/27 (CHP-212, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.97×** | +5.6 | 8e-07 | 18/29 (NCI-H460, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **1.81×** | +5.1 | 1e-05 | 16/26 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.58×** | +4.7 | 6e-05 | 15/29 (NCI-H460, hTERT-HPNE, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9395.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.05 µM |  | **0.503×** | -5.9 | 2e-06 | 17/29 (NCI-H23, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.578×** | -4.7 | 8e-04 | 16/30 (HS-578T, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.683×** | -4.6 | 8e-04 | 15/30 (A-427, CHP-212, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.652×** | -3.6 | 0.038 | 14/27 (A-172, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | 0.680× | -3.3 | 0.11 | 12/30 (SW 1088, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.689× | -3.2 | 0.14 | 15/30 (A-172, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | 0.693× | -3.1 | 0.14 | 17/30 (HS-578T, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.699× | -3.1 | 0.16 | 16/29 (NCI-H23, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.93 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9395. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 3.10 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 52.1× (z +10.7) | — |
| [[A-172 (line)]] | wt | 63.2 | 2 | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 0.05 µM 4.19× (z +9.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.203× (z -11.1) |
| [[PANC-1 (line)]] | alt | 3.01 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 29.7× (z +12.9) | — |
| [[SW480 (line)]] | alt | 2.34 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.4× (z +14.7) | — |
| [[NCI-H1792 (line)]] | alt | 10.2 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 11.9× (z +9.7) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 10.7× (z +9.3) | — |
| [[NCI-H2030 (line)]] | alt | 6.05 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.50× (z +8.8) | [[Naproxen (drug)]] 5 µM 0.0512× (z -10.6) |
| [[A-427 (line)]] | wt | 7.25 | 1 | 1 | [[Panobinostat (drug)]] 5 µM 7.58× (z +8.6) | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0946× (z -10.0) |
| [[hTERT-HPNE (line)]] | wt | 56.4 | 2 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 6.97× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 2.31 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 30.6× (z +13.4) | — |
| [[SW1417 (line)]] | alt | 2.15 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 40.3× (z +9.0) | — |
| [[A498 (line)]] | wt | 7.94 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.64× (z +9.2) | — |
| [[C-33 A (line)]] | alt | 11.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 2.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.3× (z +9.0) | — |
| [[NCI-H460 (line)]] | wt | 18.9 | 1 | 0 | [[Cobimetinib (drug)]] 5 µM 7.29× (z +8.9) | — |
| [[A549 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.50 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.949 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.953 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 79.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.44 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.28 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.889 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.09 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.940 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 6.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 33.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.63 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.08 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9395), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TDO2]] | +0.61 | +0.62 / +0.49 | both halves | 1e-05 | **novel candidate** |
| [[B4GALNT1]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[NXPE3]] | +0.55 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[MLLT11]] | +0.54 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[SSX1]] | +0.54 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[CNPY4]] | +0.54 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[KRT14]] | +0.53 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[HHIPL2]] | +0.53 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[EGF]] | +0.53 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[UCHL1]] | +0.52 | +0.58 / +0.44 | both halves | 3e-05 |  |
| [[CYP4F11]] | +0.52 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[HSP90AA2P]] | +0.52 | +0.51 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENTR1]] | -0.47 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[MECR]] | -0.43 | -0.32 / -0.36 | both halves | 2e-04 |  |
| [[EXOSC7]] | -0.42 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[RPF2]] | -0.42 | -0.41 / -0.28 | both halves | 3e-04 |  |
| [[ADSL]] | -0.42 | -0.36 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 8, C 6. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers MAP1A's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.6% of all compounds | 0.011 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[FBN1]] | B | FBN1 activity raises MAP1A's level | lines that do not express FBN1 (28) vs lines expressing it (22) | 2.74× lower at baseline in the lines without FBN1 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: GYPC, TENM2, ENSG00000280241 |
| [[PDZRN3]] | B | PDZRN3 activity raises MAP1A's level | lines that do not express PDZRN3 (30) vs lines expressing it (20) | 1.89× lower at baseline in the lines without PDZRN3 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000237268, ENSG00000253642, ENSG00000288098 |
| [[PCDH18]] | B | PCDH18 activity raises MAP1A's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 4.11× lower at baseline in the lines without PCDH18 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677 |
| [[TDO2]] | B | TDO2 activity raises MAP1A's level | lines that do not express TDO2 (27) vs lines expressing it (23) | 2.97× lower at baseline in the lines without TDO2 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LAMA1, SCN3A, MSC-AS1 |
| [[DNAJA4]] | B | DNAJA4 activity lowers MAP1A's level | lines that do not express DNAJA4 (22) vs lines expressing it (28) | 2.55× higher at baseline in the lines without DNAJA4 | 0.055 | ⚠ within organs, on part of the lines; also absent: COL17A1, ENSG00000262302, KIAA0040 |
| [[CCDC80]] | B | CCDC80 activity raises MAP1A's level | lines that do not express CCDC80 (21) vs lines expressing it (29) | 2.51× lower at baseline in the lines without CCDC80 | 0.070 | ⚠ within organs, on part of the lines; also absent: ABCC9, WNT5A, ALPK2 |
| [[SSX1]] | B | SSX1 activity raises MAP1A's level | lines that do not express SSX1 (43) vs lines expressing it (7) | 2.30× lower at baseline in the lines without SSX1 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00879, LINC02099, RNF17 |
| [[GLIS1]] | C | GLIS1 activity raises MAP1A's level | lines that do not express GLIS1 (24) vs lines expressing it (26) | 3.58× lower at baseline in the lines without GLIS1 | 0.004 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent; co-absent with the target |
| [[SYT11]] | C | SYT11 activity raises MAP1A's level | lines that do not express SYT11 (25) vs lines expressing it (25) | 3.64× lower at baseline in the lines without SYT11 | 0.013 | ⚠ within organs, on part of the lines; also absent: MAGI2-AS3, GRIA2, CTHRC1; co-absent with the target |
| [[PTPRN]] | C | PTPRN activity raises MAP1A's level | lines that do not express PTPRN (31) vs lines expressing it (19) | 3.68× lower at baseline in the lines without PTPRN | 0.060 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: SPARC, PAX3, PHACTR1; co-absent with the target |
| [[HMCN1]] | C | HMCN1 activity raises MAP1A's level | lines that do not express HMCN1 (26) vs lines expressing it (24) | 3.22× lower at baseline in the lines without HMCN1 | 0.067 | ⚠ within organs, on part of the lines; also absent: EPHA5, EPHA5-AS1, ITGA4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 6, C 11. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CNPY4]] | B | MAP1A activity raises CNPY4's level | lines that do not express MAP1A (17) vs lines expressing it (33) | 1.89× lower at baseline in the lines without MAP1A | 0.006 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent |
| [[TUBA1A]] | B | MAP1A activity raises TUBA1A's level | lines that do not express MAP1A (17) vs lines expressing it (33) | 4.00× lower at baseline in the lines without MAP1A | 0.023 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent |
| [[TTLL7]] | B | MAP1A activity raises TTLL7's level | lines that do not express MAP1A (17) vs lines expressing it (33) | 3.69× lower at baseline in the lines without MAP1A | 0.036 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent |
| cells under [[Ixazomib (drug)]] 0.05 µM | B | MAP1A activity lowers the cells' numbers under Ixazomib 0.05 µM (makes them more sensitive) | lines that do not express MAP1A (17) vs lines expressing it (31) | the lines without MAP1A: 1.19× the cells of the other lines | 0.076 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent |
| cells under [[Minodronic acid (drug)]] 0.5 µM | B | MAP1A activity raises the cells' numbers under Minodronic acid 0.5 µM (protects the cells) | lines that do not express MAP1A (17) vs lines expressing it (31) | the lines without MAP1A: 0.86× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent |
| [[TM2D2]] | B | MAP1A activity lowers TM2D2's level | lines that do not express MAP1A (17) vs lines expressing it (33) | 1.26× higher at baseline in the lines without MAP1A | 0.096 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent |
| [[GLIS1]] | C | MAP1A activity raises GLIS1's level | lines that do not express MAP1A (17) vs lines expressing it (33) | 3.71× lower at baseline in the lines without MAP1A | 0.009 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent; co-absent with the target |
| [[KIAA0408]] | C | MAP1A activity raises KIAA0408's level | lines that do not express MAP1A (17) vs lines expressing it (33) | 3.89× lower at baseline in the lines without MAP1A | 0.037 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent; co-absent with the target |
| [[SPEG]] | C | MAP1A activity raises SPEG's level | lines that do not express MAP1A (17) vs lines expressing it (33) | 3.01× lower at baseline in the lines without MAP1A | 0.045 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent; co-absent with the target |
| [[ATRNL1]] | C | MAP1A activity raises ATRNL1's level | lines that do not express MAP1A (17) vs lines expressing it (33) | 3.51× lower at baseline in the lines without MAP1A | 0.047 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent; co-absent with the target |
| [[SOGA3]] | C | MAP1A activity raises SOGA3's level | lines that do not express MAP1A (17) vs lines expressing it (33) | 3.68× lower at baseline in the lines without MAP1A | 0.049 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent; co-absent with the target |
| [[HMCN1]] | C | MAP1A activity raises HMCN1's level | lines that do not express MAP1A (17) vs lines expressing it (33) | 4.02× lower at baseline in the lines without MAP1A | 0.054 | ⚠ within organs, on part of the lines; also absent: HMCN1, HOXB-AS1, LINC02269; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-4.8, 50.4); signed map (52.4, -14.1). **Vector** length 67.2, 14.2% of its response variance represented; |z| ≥ 3 in 911 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.8 | +5.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.7 | +5.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.0 | +7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | +3.5 | +9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~40% of this change | +3.3 | +9.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +7.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.6 | +7.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.6 | +4.0 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -1.9 | -5.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.7 | +0.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.6 | -0.5 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.5 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -2.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | microtubule associated protein 1A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.3 — chr15:43,510,958-43,531,620 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MAP1L |
| Matched by | ensembl_id |

**Function**, from UniProt [P78559](https://www.uniprot.org/uniprotkb/P78559) (Microtubule-associated protein 1A):

> Structural protein involved in the filamentous cross-bridging between microtubules and other skeletal elements.

**Summary**, from NCBI Gene [4130](https://www.ncbi.nlm.nih.gov/gene/4130):

> This gene encodes a protein that belongs to the microtubule-associated protein family. The proteins of this family are thought to be involved in microtubule assembly, which is an essential step in neurogenesis. The product of this gene is a precursor polypeptide that presumably undergoes proteolytic processing to generate the final MAP1A heavy chain and LC2 light chain. Expression of this gene is almost exclusively in the brain. Studies of the rat microtubule-associated protein 1A gene …

**Accessions** — [HGNC:6835](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6835) · Entrez [4130](https://www.ncbi.nlm.nih.gov/gene/4130) · UniProt [P78559](https://www.uniprot.org/uniprotkb/P78559) · Ensembl [ENSG00000166963](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166963)

## Data

Gene col 9395: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9395); `tables/drug_effects.parquet` (52 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9395, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9395]; `tensor/DDL_lfc|DDL_z.npy` [9395]; `embed/gene_vectors.npy` [9395]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9395 or target_col == 9395). Every well: [[MAP1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
