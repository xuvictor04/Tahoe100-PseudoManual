---
symbol: "GALNT5"
type: "gene"
col: 5879
ensembl_id: "ENSG00000136542"
name: "polypeptide N-acetylgalactosaminyltransferase 5"
location: "2q24.1"
module: 73
arm: "+"
pooled_cpm: 28.95
n_lines_expressing: 23
n_dd_up: 11
n_dd_down: 29
n_dd_up_clean: 6
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 34
direction_downstream: 29
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# GALNT5

*polypeptide N-acetylgalactosaminyltransferase 5* — 2q24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.01× (z +18.5, q 0e+00, up in 16 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.45× (z +7.2, q 6e-11, up in 14 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.423× (z -11.9, q 8e-30, down in 21 of 21 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02474]] (+0.62, fdr 1e-05), [[COL17A1]] (+0.58, fdr 1e-05), [[EHF]] (+0.58, fdr 7e-05); moves opposite to [[CCDC107]] (-0.50, fdr 8e-05), [[DNAAF9]] (-0.47, fdr 4e-04), [[NPHP3]] (-0.47, fdr 1e-04).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 34 arrows point to it, the strongest [[SRPX2]] → it (grade B ⚠); 29 go from it, the strongest it → [[RAB11FIP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5879.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.01×** | +18.5 | 0e+00 | 16/18 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.65×** | +17.9 | 0e+00 | 17/19 (CFPAC-1, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.65×** | +12.5 | 2e-33 | 11/18 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +7.2 | 6e-11 | 14/21 (AsPC-1, LS 180, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.28×** | +4.8 | 2e-04 | 5/21 (SW480, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.36×** | +4.1 | 0.005 | 3/21 (NCI-H2347, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +4.0 | 0.005 | 5/21 (LS 180, LoVo, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Pimitespib (drug)]] 0.05 µM |  | **1.35×** | +3.9 | 0.008 | 6/21 (COLO 205, Hs 766T, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.012 | 6/21 (SNU-423, HT-29, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.18× | +3.2 | 0.081 | 4/21 (NCI-H1792, CFPAC-1, …) | top dose only |  |
| [[AZD-7648 (drug)]] 0.5 µM |  | **1.38×** | +3.1 | 0.081 | 2/21 (HT-29, AsPC-1) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.26×** | +3.1 | 0.081 | 3/21 (CFPAC-1, SW1417, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.17× | +3.1 | 0.083 | 1/21 (hTERT-HPNE) | two highest doses |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 1.24× | +3.0 | 0.11 | 6/21 (COLO 205, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5879.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.423×** | -11.9 | 8e-30 | 21/21 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.428×** | -11.8 | 2e-29 | 21/21 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.501×** | -9.6 | 2e-19 | 21/21 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.554×** | -7.9 | 6e-13 | 16/21 (SW 900, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.592×** | -7.3 | 4e-11 | 13/21 (SNU-1, LoVo, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.603×** | -7.0 | 3e-10 | 8/21 (Hs 766T, NCI-H1792, …) | all doses, flat |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.721×** | -6.4 | 1e-08 | 19/21 (COLO 205, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.643×** | -6.1 | 7e-08 | 20/21 (SNU-1, SW480, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.661×** | -5.7 | 7e-07 | 10/21 (NCI-H2347, Panc 03.27, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.685×** | -5.2 | 9e-06 | 19/21 (SNU-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.687×** | -5.2 | 1e-05 | 19/21 (SNU-1, LoVo, …) | two highest doses | cell-cycle shift (explains ~8% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.712×** | -4.7 | 1e-04 | 16/21 (SW480, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.717×** | -4.6 | 2e-04 | 12/21 (SW480, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.589×** | -3.8 | 0.005 | 13/21 (KATO III, SNU-1, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | **0.762×** | -3.8 | 0.006 | 9/21 (Hs 766T, RPMI-7951, …) | all doses, flat |  |
| [[Artesunate (drug)]] 5 µM |  | **0.826×** | -3.8 | 0.006 | 4/21 (SNU-1, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5879. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 219 | 0 | 13 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0455× (z -22.5) |
| [[SW480 (line)]] | alt | 17.6 | 0 | 10 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0840× (z -18.3) |
| [[LoVo (line)]] | wt | 133 | 0 | 9 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0527× (z -22.5) |
| [[LS 180 (line)]] | wt | 113 | 1 | 8 (2 ⚠) | [[Selinexor (drug)]] 5 µM 2.39× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.0567× (z -21.2) |
| [[NCI-H1792 (line)]] | alt | 43.2 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -20.0) |
| [[COLO 205 (line)]] | alt | 90.9 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.0573× (z -26.4) |
| [[KATO III (line)]] | alt | 184 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0199× (z -31.6) |
| [[NCI-H2347 (line)]] | alt | 94.7 | 2 (2 ⚠) | 3 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 3.01× (z +9.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -17.5) |
| [[AsPC-1 (line)]] | alt | 37.5 | 1 | 3 | [[Selinexor (drug)]] 5 µM 4.94× (z +11.9) | [[Digitoxin (drug)]] 0.5 µM 0.123× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 51.7 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +9.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -18.6) |
| [[Hs 766T (line)]] | wt | 83.4 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0785× (z -16.7) |
| [[SW 900 (line)]] | alt | 32.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -15.3) |
| [[RPMI-7951 (line)]] | alt | 13.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0549× (z -12.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.220× (z -9.4) |
| [[SW1417 (line)]] | alt | 55.4 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -13.2) |
| [[HCT15 (line)]] | alt | 7.65 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0643× (z -8.9) |
| [[HT-29 (line)]] | alt | 10.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.150× (z -9.4) |
| [[hTERT-HPNE (line)]] | wt | 33.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.50× (z +9.3) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 24.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.189× (z -8.5) |
| [[SHP-77 (line)]] | alt | 8.78 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.115× (z -8.5) |
| [[A-172 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.83 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.35 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.68 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.07 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.60 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.82 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.65 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.73 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.00 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.16 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.43 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.76 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.00 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.11 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5879), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02474]] | +0.62 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[COL17A1]] | +0.58 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[EHF]] | +0.58 | +0.63 / +0.37 | both halves | 7e-05 |  |
| [[SLC44A5]] | +0.56 | +0.59 / +0.32 | both halves | 2e-04 |  |
| [[LINC00857]] | +0.55 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[B3GALT5]] | +0.54 | +0.52 / +0.49 | both halves | 1e-05 |  |
| [[CDH17]] | +0.54 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[C4BPB]] | +0.53 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[LGR6]] | +0.53 | +0.58 / +0.47 | both halves | 2e-05 |  |
| [[TPRXL]] | +0.52 | +0.55 / +0.33 | both halves | 1e-04 |  |
| [[TNFSF15]] | +0.52 | +0.45 / +0.40 | both halves | 5e-05 |  |
| [[SLC12A2]] | +0.51 | +0.46 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CCDC107]] | -0.50 | -0.41 / -0.37 | both halves | 8e-05 |  |
| [[DNAAF9]] | -0.47 | -0.50 / -0.25 | both halves | 4e-04 |  |
| [[NPHP3]] | -0.47 | -0.35 / -0.46 | both halves | 1e-04 |  |
| [[RAB11FIP3]] | -0.45 | -0.46 / -0.30 | both halves | 2e-04 |  |
| [[DLK2]] | -0.45 | -0.36 / -0.40 | both halves | 1e-04 |  |
| [[ARID3A]] | -0.45 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[SLC25A37]] | -0.45 | -0.32 / -0.40 | both halves | 2e-04 |  |
| [[MT1X]] | -0.44 | -0.25 / -0.51 | both halves | 4e-04 |  |
| [[PHF20]] | -0.44 | -0.44 / -0.30 | both halves | 2e-04 |  |
| [[MT2A]] | -0.42 | -0.25 / -0.48 | both halves | 4e-04 |  |
| [[SELENOO]] | -0.42 | -0.29 / -0.35 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*34 arrows, 34 of them with an alert ⚠; grade A 0, B 5, C 29. Shown: the 12 strongest; 22 more arrows (22 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRPX2]] | B | SRPX2 activity raises GALNT5's level | lines that do not express SRPX2 (24) vs lines expressing it (26) | 1.43× lower at baseline in the lines without SRPX2 | 0.019 | ⚠ within organs, on part of the lines; also absent: TGFBI, GBP5, FN1 |
| [[EVA1A-AS]] | B | EVA1A-AS activity raises GALNT5's level | lines that do not express EVA1A-AS (22) vs lines expressing it (28) | 2.18× lower at baseline in the lines without EVA1A-AS | 0.025 | ⚠ within organs, on part of the lines; also absent: ENSG00000254979, RFX8, SULT1C2; maybe low, not absent |
| [[SYTL5]] | B | SYTL5 activity raises GALNT5's level | lines that do not express SYTL5 (20) vs lines expressing it (30) | 2.65× lower at baseline in the lines without SYTL5 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: GBP4, LINC00589, ENSG00000227400 |
| [[ARHGAP42]] | B | ARHGAP42 activity raises GALNT5's level | lines that do not express ARHGAP42 (13) vs lines expressing it (37) | 3.70× lower at baseline in the lines without ARHGAP42 | 0.052 | ⚠ within organs, on part of the lines; also absent: C6orf141, BACE2, LINC01348; maybe low, not absent |
| [[VCAN]] | B | VCAN activity raises GALNT5's level | lines that do not express VCAN (28) vs lines expressing it (22) | 1.12× lower at baseline in the lines without VCAN | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01695, ITGA4, LOX |
| [[ACSL5]] | C | ACSL5 activity raises GALNT5's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 4.78× lower at baseline in the lines without ACSL5 | 4e-04 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1; co-absent with the target |
| [[PTPRB]] | C | PTPRB activity raises GALNT5's level | lines that do not express PTPRB (22) vs lines expressing it (28) | 3.10× lower at baseline in the lines without PTPRB | 0.003 | ⚠ within organs, on part of the lines; also absent: PLAAT4, PTPRR, ADGRF4; co-absent with the target |
| [[TNFRSF14-AS1]] | C | TNFRSF14-AS1 activity raises GALNT5's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 3.75× lower at baseline in the lines without TNFRSF14-AS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB; co-absent with the target |
| [[UGT1A1]] | C | UGT1A1 activity raises GALNT5's level | lines that do not express UGT1A1 (36) vs lines expressing it (14) | 5.66× lower at baseline in the lines without UGT1A1 | 0.004 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, NPSR1; co-absent with the target |
| [[UGT1A6]] | C | UGT1A6 activity raises GALNT5's level | lines that do not express UGT1A6 (35) vs lines expressing it (15) | 4.66× lower at baseline in the lines without UGT1A6 | 0.004 | ⚠ within organs, on part of the lines; also absent: UGT1A1, UGT1A9, NPSR1; co-absent with the target |
| [[ADGRF1]] | C | ADGRF1 activity raises GALNT5's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 5.48× lower at baseline in the lines without ADGRF1 | 0.004 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |
| [[PKP1]] | C | PKP1 activity raises GALNT5's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 3.60× lower at baseline in the lines without PKP1 | 0.006 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5; co-absent with the target |

### Downstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 7, C 22. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB11FIP3]] | B | GALNT5 activity lowers RAB11FIP3's level | lines that do not express GALNT5 (27) vs lines expressing it (23) | 1.84× higher at baseline in the lines without GALNT5 | 0.004 | ⚠ within organs, on part of the lines; also absent: IL20RA, HPGD, ICAM2 |
| [[ZNF503-AS1]] | B | GALNT5 activity raises ZNF503-AS1's level | lines that do not express GALNT5 (27) vs lines expressing it (23) | 2.21× lower at baseline in the lines without GALNT5 | 0.007 | ⚠ within organs, on part of the lines; also absent: IL20RA, HPGD, ICAM2 |
| [[TNFRSF21]] | B | GALNT5 activity raises TNFRSF21's level | lines that do not express GALNT5 (27) vs lines expressing it (23) | 3.60× lower at baseline in the lines without GALNT5 | 0.009 | ⚠ within organs, on part of the lines; also absent: IL20RA, HPGD, ICAM2 |
| [[ARHGAP42]] | B | GALNT5 activity raises ARHGAP42's level | lines that do not express GALNT5 (27) vs lines expressing it (23) | 3.06× lower at baseline in the lines without GALNT5 | 0.038 | ⚠ within organs, on part of the lines; also absent: IL20RA, HPGD, ICAM2 |
| [[VCAN]] | B | GALNT5 activity raises VCAN's level | lines that do not express GALNT5 (27) vs lines expressing it (23) | 1.45× lower at baseline in the lines without GALNT5 | 0.051 | ⚠ within organs, on part of the lines; also absent: IL20RA, HPGD, ICAM2 |
| [[FBXO15]] | B | GALNT5 activity lowers FBXO15's level | lines that do not express GALNT5 (27) vs lines expressing it (23) | 1.92× higher at baseline in the lines without GALNT5 | 0.095 | ⚠ within organs, on part of the lines; also absent: IL20RA, HPGD, ICAM2 |
| cells under [[Trifluridine (drug)]] 5 µM | B | GALNT5 activity raises the cells' numbers under Trifluridine 5 µM (protects the cells) | lines that do not express GALNT5 (27) vs lines expressing it (21) | the lines without GALNT5: 0.91× the cells of the other lines | 0.098 | ⚠ within organs, on part of the lines; also absent: IL20RA, HPGD, ICAM2 |
| [[LASTR]] | C | GALNT5 activity raises LASTR's level | lines that do not express GALNT5 (27) vs lines expressing it (23) | 3.06× lower at baseline in the lines without GALNT5 | 0.005 | ⚠ within organs, on part of the lines; also absent: IL20RA, HPGD, ICAM2; co-absent with the target |
| [[PTPRR]] | C | GALNT5 activity raises PTPRR's level | lines that do not express GALNT5 (27) vs lines expressing it (23) | 3.69× lower at baseline in the lines without GALNT5 | 0.010 | ⚠ within organs, on part of the lines; also absent: IL20RA, HPGD, ICAM2; co-absent with the target |
| [[TNFRSF14-AS1]] | C | GALNT5 activity raises TNFRSF14-AS1's level | lines that do not express GALNT5 (27) vs lines expressing it (23) | 2.23× lower at baseline in the lines without GALNT5 | 0.010 | ⚠ within organs, on part of the lines; also absent: IL20RA, HPGD, ICAM2; co-absent with the target |
| [[ACSL5]] | C | GALNT5 activity raises ACSL5's level | lines that do not express GALNT5 (27) vs lines expressing it (23) | 4.66× lower at baseline in the lines without GALNT5 | 0.011 | ⚠ within organs, on part of the lines; also absent: IL20RA, HPGD, ICAM2; co-absent with the target |
| [[UGT1A6]] | C | GALNT5 activity raises UGT1A6's level | lines that do not express GALNT5 (27) vs lines expressing it (23) | 4.22× lower at baseline in the lines without GALNT5 | 0.012 | ⚠ within organs, on part of the lines; also absent: IL20RA, HPGD, ICAM2; co-absent with the target |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.542). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (17.2, 49.2); signed map (67.9, 8.1). **Vector** length 78.9, 23.8% of its response variance represented; |z| ≥ 3 in 709 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.3 | +18.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.1 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.0 | +17.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.2 | +4.8 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.3 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.1 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.1 | +2.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +2.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.6 | +3.2 |
| fall | [[Artesunate (drug)]] 5 µM |  | -2.4 | -3.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -7.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.0 | -7.3 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.9 | -5.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.8 | -3.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.7 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | polypeptide N-acetylgalactosaminyltransferase 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q24.1 — chr2:157,257,705-157,318,491 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GalNAc-T5 |
| Gene groups (HGNC) | Polypeptide N-acetylgalactosaminyltransferases |
| Reactome | 2 pathways, smallest: O-linked glycosylation of mucins; O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z7M9](https://www.uniprot.org/uniprotkb/Q7Z7M9) (Polypeptide N-acetylgalactosaminyltransferase 5):

> Catalyzes the initial reaction in O-linked oligosaccharide biosynthesis, the transfer of an N-acetyl-D-galactosamine residue to a serine or threonine residue on the protein receptor. Has activity toward EA2 peptide substrate, but has a weak activity toward Muc2 or Muc1b substrates (By similarity).

**Summary**, from NCBI Gene [11227](https://www.ncbi.nlm.nih.gov/gene/11227):

> The protein encoded by this gene is a membrane-bound polypeptide N-acetylgalactosaminyltransferase that is found in the Golgi. The encoded protein catalyzes the first step in the mucin-type O-glycosylation of Golgi proteins, transfering an N-acetyl-D-galactosamine residue to a serine or threonine residue on the protein receptor. [provided by RefSeq, Aug 2016]

**Accessions** — [HGNC:4127](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4127) · Entrez [11227](https://www.ncbi.nlm.nih.gov/gene/11227) · UniProt [Q7Z7M9](https://www.uniprot.org/uniprotkb/Q7Z7M9) · Ensembl [ENSG00000136542](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136542)

## Data

Gene col 5879: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5879); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5879, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5879]; `tensor/DDL_lfc|DDL_z.npy` [5879]; `embed/gene_vectors.npy` [5879]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5879 or target_col == 5879). Every well: [[GALNT5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GALNT5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
