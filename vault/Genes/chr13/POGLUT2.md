---
symbol: "POGLUT2"
type: "gene"
col: 5624
ensembl_id: "ENSG00000134901"
name: "protein O-glucosyltransferase 2"
location: "13q33.1"
module: 65
arm: "+"
pooled_cpm: 5.47
n_lines_expressing: 46
n_dd_up: 20
n_dd_down: 15
n_dd_up_clean: 11
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 3
direction_downstream: 11
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# POGLUT2

*protein O-glucosyltransferase 2* — 13q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.66× (z +20.5, q 0e+00, up in 43 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (3 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.378× (z -13.0, q 9e-36, down in 35 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAPSS1]] (+0.76, fdr 7e-06), [[PRRC1]] (+0.73, fdr 1e-05), [[IDH2]] (+0.72, fdr 7e-06); moves opposite to [[WARS2-AS1]] (-0.72, fdr 1e-05), [[SLC9A8]] (-0.71, fdr 1e-05), [[AKT1S1]] (-0.70, fdr 1e-05).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[FKBP10]] → it (grade B ⚠); 11 go from it, the strongest it → [[GGH]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5624.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.66×** | +20.5 | 0e+00 | 43/43 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.48×** | +20.0 | 0e+00 | 41/41 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.31×** | +19.4 | 0e+00 | 40/41 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.77×** | +13.6 | 9e-40 | 36/42 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **2.48×** | +12.1 | 2e-31 | 33/36 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.79×** | +11.0 | 6e-26 | 30/42 (SW480, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.69×** | +9.8 | 6e-21 | 18/36 (SW480, SHP-77, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **2.05×** | +9.2 | 3e-18 | 18/23 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Brivudine (drug)]] 5 µM |  | **3.21×** | +8.1 | 3e-14 | 22/41 (SW480, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change | **1.88×** | +8.1 | 4e-14 | 4/8 (PANC-1, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.60×** | +6.0 | 9e-08 | 13/37 (SW480, HOP62, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~84% of this change | **1.57×** | +6.0 | 1e-07 | 12/22 (HEC-1-A, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~66% of this change | **1.52×** | +5.1 | 1e-05 | 2/12 (A-172, HOP62) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.46×** | +4.8 | 6e-05 | 13/35 (SW480, C32, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +4.5 | 3e-04 | 16/40 (NCI-H1573, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.25×** | +4.2 | 8e-04 | 5/42 (J82, RKO, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.30×** | +3.5 | 0.017 | 2/41 (HOP62, MIA PaCa-2) | all doses, stronger at high dose | position effect removed |
| [[Raltitrexed (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.033 | 6/41 (NCI-H460, H4, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5624.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.378×** | -13.0 | 9e-36 | 35/42 (NCI-H1573, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.470×** | -10.1 | 2e-21 | 20/35 (SW 900, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.471×** | -10.1 | 2e-21 | 25/41 (NCI-H460, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.640×** | -8.4 | 5e-15 | 22/35 (A-172, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.535×** | -8.0 | 1e-13 | 19/38 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.625×** | -6.3 | 3e-08 | 19/41 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.653×** | -5.7 | 9e-07 | 18/41 (HCT15, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.664×** | -5.5 | 3e-06 | 17/41 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.713×** | -4.5 | 4e-04 | 17/36 (A-172, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.724×** | -4.3 | 9e-04 | 14/40 (A-172, A498, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.732×** | -4.2 | 0.001 | 12/41 (SNU-1, AN3 CA, …) | top dose only |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.745×** | -3.7 | 0.009 | 8/42 (MIA PaCa-2, SW 1088, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.757×** | -3.6 | 0.015 | 11/41 (HepG2/C3A, AN3 CA, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.784×** | -3.3 | 0.045 | 7/41 (LS 180, Panc 03.27, …) | inconsistent across doses |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.845× | -3.2 | 0.054 | 8/42 (CFPAC-1, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.796×** | -3.1 | 0.080 | 9/42 (A-172, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.60 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5624. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 21.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.0586× (z -22.6) |
| [[NCI-H460 (line)]] | wt | 5.02 | 0 | 5 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0479× (z -15.6) |
| [[SW480 (line)]] | alt | 10.1 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.91× (z +10.8) | — |
| [[NCI-H1573 (line)]] | alt | 5.83 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 8.13× (z +9.1) | — |
| [[A498 (line)]] | wt | 11.5 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.243× (z -9.0) |
| [[C-33 A (line)]] | alt | 4.07 | 0 | 1 | — | [[Bestatin (hydrochloride) (drug)]] 5 µM 0.0458× (z -8.5) |
| [[HOP62 (line)]] | alt | 4.98 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0918× (z -10.5) |
| [[Hs 766T (line)]] | wt | 8.22 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.129× (z -8.6) |
| [[HS-578T (line)]] | alt | 5.47 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0988× (z -9.2) |
| [[hTERT-HPNE (line)]] | wt | 6.35 | 0 | 1 | — | [[Captopril (drug)]] 0.05 µM 0.0662× (z -8.9) |
| [[KATO III (line)]] | alt | 4.01 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0873× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 5.78 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.5 µM 0.0639× (z -10.4) |
| [[SHP-77 (line)]] | alt | 23.1 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +8.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[A-427 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.32 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.952 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.51 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.65 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.84 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.02 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.79 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.53 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.03 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.46 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.18 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.16 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.82 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.22 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.71 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5624), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAPSS1]] | +0.76 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[PRRC1]] | +0.73 | +0.73 / +0.56 | both halves | 1e-05 |  |
| [[IDH2]] | +0.72 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[GMCL1]] | +0.72 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[ELP1]] | +0.72 | +0.63 / +0.59 | both halves | 7e-06 |  |
| [[ATG4C]] | +0.72 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[POMGNT2]] | +0.71 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[HACE1]] | +0.70 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[IER3IP1]] | +0.70 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[ARL3]] | +0.69 | +0.57 / +0.58 | both halves | 1e-05 |  |
| [[GLT8D1]] | +0.68 | +0.72 / +0.49 | both halves | 1e-05 |  |
| [[OSTF1]] | +0.68 | +0.66 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WARS2-AS1]] | -0.72 | -0.64 / -0.50 | both halves | 1e-05 |  |
| [[SLC9A8]] | -0.71 | -0.70 / -0.51 | both halves | 1e-05 |  |
| [[AKT1S1]] | -0.70 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[RAB30-DT]] | -0.69 | -0.59 / -0.60 | both halves | 7e-06 |  |
| [[FBXL19-AS1]] | -0.69 | -0.64 / -0.56 | both halves | 1e-05 |  |
| [[ANKLE2]] | -0.69 | -0.48 / -0.68 | both halves | 2e-05 |  |
| [[GTF2H1]] | -0.68 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[ST7L]] | -0.68 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[C11orf58]] | -0.67 | -0.56 / -0.58 | both halves | 1e-05 |  |
| [[CCDC90B-AS1]] | -0.67 | -0.63 / -0.40 | both halves | 4e-05 |  |
| [[RGS5]] | -0.66 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[ATXN7L1]] | -0.66 | -0.68 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FKBP10]] | B | FKBP10 activity raises POGLUT2's level | lines that do not express FKBP10 (10) vs lines expressing it (40) | 1.81× lower at baseline in the lines without FKBP10 | 0.009 | ⚠ within organs, on part of the lines; also absent: MPP2, RAC3, BOLA3-DT |
| [[SV2A]] | B | SV2A activity raises POGLUT2's level | lines that do not express SV2A (17) vs lines expressing it (33) | 1.54× lower at baseline in the lines without SV2A | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000268163, SYT11, SMARCA1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers POGLUT2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GGH]] | C | POGLUT2 activity raises GGH's level | lines that do not express POGLUT2 (4) vs lines expressing it (46) | 2.25× lower at baseline in the lines without POGLUT2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYCP2L, BIVM, DUSP19; maybe low, not absent; its own permutation p |
| [[ATG4C]] | C | POGLUT2 activity raises ATG4C's level | lines that do not express POGLUT2 (4) vs lines expressing it (46) | 1.88× lower at baseline in the lines without POGLUT2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYCP2L, BIVM, DUSP19; maybe low, not absent; its own permutation p |
| [[WRAP53]] | C | POGLUT2 activity raises WRAP53's level | lines that do not express POGLUT2 (4) vs lines expressing it (46) | 1.87× lower at baseline in the lines without POGLUT2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYCP2L, BIVM, DUSP19; maybe low, not absent; its own permutation p |
| [[HACE1]] | C | POGLUT2 activity raises HACE1's level | lines that do not express POGLUT2 (4) vs lines expressing it (46) | 1.87× lower at baseline in the lines without POGLUT2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYCP2L, BIVM, DUSP19; maybe low, not absent; its own permutation p |
| [[NOMO2]] | C | POGLUT2 activity raises NOMO2's level | lines that do not express POGLUT2 (4) vs lines expressing it (46) | 1.55× lower at baseline in the lines without POGLUT2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYCP2L, BIVM, DUSP19; maybe low, not absent; its own permutation p |
| [[MYPOP]] | C | POGLUT2 activity raises MYPOP's level | lines that do not express POGLUT2 (4) vs lines expressing it (46) | 1.51× lower at baseline in the lines without POGLUT2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYCP2L, BIVM, DUSP19; maybe low, not absent; its own permutation p |
| [[P3H4]] | C | POGLUT2 activity raises P3H4's level | lines that do not express POGLUT2 (4) vs lines expressing it (46) | 2.90× lower at baseline in the lines without POGLUT2 | 0.069 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYCP2L, BIVM, DUSP19; maybe low, not absent |
| [[FKBP10]] | C | POGLUT2 activity raises FKBP10's level | lines that do not express POGLUT2 (4) vs lines expressing it (46) | 4.90× lower at baseline in the lines without POGLUT2 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYCP2L, BIVM, DUSP19; maybe low, not absent |
| [[ATXN10]] | C | POGLUT2 activity raises ATXN10's level | lines that do not express POGLUT2 (4) vs lines expressing it (46) | 1.46× lower at baseline in the lines without POGLUT2 | 0.079 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYCP2L, BIVM, DUSP19; maybe low, not absent |
| [[NBPF3]] | C | POGLUT2 activity raises NBPF3's level | lines that do not express POGLUT2 (4) vs lines expressing it (46) | 2.17× lower at baseline in the lines without POGLUT2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYCP2L, BIVM, DUSP19; maybe low, not absent; its own permutation p |
| [[ALS2]] | C | POGLUT2 activity raises ALS2's level | lines that do not express POGLUT2 (4) vs lines expressing it (46) | 1.80× lower at baseline in the lines without POGLUT2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYCP2L, BIVM, DUSP19; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.729). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (4.1, -11.5); signed map (-37.8, -8.0). **Vector** length 75.0, 13.2% of its response variance represented; |z| ≥ 3 in 1,124 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM |  | +3.4 | +19.4 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.4 | +13.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +11.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.8 | +12.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.7 | +20.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.3 | +8.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +0.3 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | +1.1 | -0.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | +1.1 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.8 | -8.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.3 | -4.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.7 | -8.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.0 | -5.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.8 | -5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | +0.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.0 | -3.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.8 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | protein O-glucosyltransferase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q33.1 — chr13:102,784,281-102,799,040 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC5302, EP58; previously KDELC1 |
| Gene groups (HGNC) | Glycosyltransferase family 90 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6UW63](https://www.uniprot.org/uniprotkb/Q6UW63) (Protein O-glucosyltransferase 2):

> Protein glucosyltransferase that catalyzes the transfer of glucose from UDP-glucose to a serine residue within the consensus sequence peptide C-X-N-T-X-G-S-F-X-C. Can also catalyze the transfer of xylose from UDP-xylose but less efficiently. Specifically targets extracellular EGF repeats of proteins such as NOTCH1, NOTCH3, FBN1, FBN2 and LTBP1. May regulate the transport of NOTCH1 and NOTCH3 to the plasma membrane and thereby the Notch signaling pathway.

**Summary**, from NCBI Gene [79070](https://www.ncbi.nlm.nih.gov/gene/79070):

> This gene encodes a protein product localized to the lumen of the endoplasmic reticulum. As a member of the endoplasmic reticulum protein family the encoded protein contains a Lys-Asp-Glu-Leu or KDEL motif located at the extreme C-terminus which prevents all endoplasmic reticulum resident proteins from being secreted. Proteins carrying this motif are bound by a receptor in the Golgi apparatus so that the receptor-ligand complex returns to the endoplasmic reticulum. A processed non-transcribed …

**Accessions** — [HGNC:19350](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19350) · Entrez [79070](https://www.ncbi.nlm.nih.gov/gene/79070) · UniProt [Q6UW63](https://www.uniprot.org/uniprotkb/Q6UW63) · Ensembl [ENSG00000134901](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000134901)

## Data

Gene col 5624: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5624); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5624, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5624]; `tensor/DDL_lfc|DDL_z.npy` [5624]; `embed/gene_vectors.npy` [5624]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5624 or target_col == 5624). Every well: [[POGLUT2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POGLUT2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
