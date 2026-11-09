---
symbol: "MAN1C1"
type: "gene"
col: 3938
ensembl_id: "ENSG00000117643"
name: "mannosidase alpha class 1C member 1"
location: "1p36.11"
module: 9
arm: "+"
pooled_cpm: 5.74
n_lines_expressing: 39
n_dd_up: 22
n_dd_down: 31
n_dd_up_clean: 19
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 15
direction_downstream: 10
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# MAN1C1

*mannosidase alpha class 1C member 1* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 11.5× (z +27.7, q 0e+00, up in 35 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.481× (z -8.3, q 6e-14, down in 21 of 35 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GRIA2]] (+0.69, fdr 7e-06), [[NELL1]] (+0.63, fdr 7e-06), [[EFR3B]] (+0.61, fdr 5e-05); moves opposite to [[ZNF234]] (-0.53, fdr 5e-05), [[ITPA]] (-0.50, fdr 5e-04), [[GPATCH2]] (-0.49, fdr 3e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[LRFN2]] → it (grade B ⚠); 10 go from it, the strongest it → [[FOXO6]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3938.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **11.5×** | +27.7 | 0e+00 | 35/36 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **7.90×** | +23.5 | 0e+00 | 33/35 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Belinostat (drug)]] 5 µM |  | **6.01×** | +20.4 | 0e+00 | 31/35 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.43×** | +16.9 | 0e+00 | 32/35 (SW480, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.78×** | +16.5 | 0e+00 | 29/35 (SW480, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.22×** | +12.8 | 9e-36 | 21/30 (A549, SW480, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Brivudine (drug)]] 5 µM |  | **5.35×** | +10.0 | 2e-21 | 25/34 (SW480, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.09×** | +8.4 | 4e-15 | 18/31 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.90×** | +7.3 | 2e-11 | 17/28 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +6.3 | 2e-08 | 2/7 (HOP62, RPMI-7951) | rises with dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +5.9 | 2e-07 | 13/30 (SW480, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.62×** | +5.5 | 2e-06 | 9/36 (SW480, LoVo, …) | top dose only |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **2.09×** | +4.4 | 5e-04 | 2/26 (SW480, J82) | top dose only | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.44×** | +4.2 | 0.001 | 10/34 (A-172, A-427, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.38×** | +3.7 | 0.008 | 1/15 (SW480) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.033 | 6/33 (LoVo, A-427, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.05 µM |  | **1.36×** | +3.3 | 0.033 | 1/35 (SK-MEL-2) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 31 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3938.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.481×** | -8.3 | 6e-14 | 21/35 (SHP-77, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.485×** | -8.2 | 7e-14 | 21/35 (C32, SHP-77, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.474×** | -8.0 | 3e-13 | 17/32 (SHP-77, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.527×** | -7.3 | 6e-11 | 19/34 (SW 900, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.572×** | -6.3 | 3e-08 | 22/35 (SHP-77, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.583×** | -6.1 | 9e-08 | 18/34 (SHP-77, BT-474, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.593×** | -5.9 | 3e-07 | 18/35 (SHP-77, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.700×** | -5.7 | 9e-07 | 17/36 (SHP-77, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.635×** | -5.1 | 2e-05 | 17/27 (SHP-77, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.640×** | -5.0 | 3e-05 | 12/36 (NCI-H23, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | **0.651×** | -4.7 | 2e-04 | 16/33 (A-427, SHP-77, …) | two highest doses | composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.682×** | -4.3 | 7e-04 | 11/34 (SHP-77, A-427, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.686×** | -4.3 | 9e-04 | 13/28 (SHP-77, A549, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.686×** | -4.1 | 0.002 | 8/36 (SHP-77, J82, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.504×** | -4.1 | 0.002 | 12/33 (SHP-77, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.713×** | -3.8 | 0.005 | 13/32 (C32, A-427, …) | inconsistent across doses |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.532×** | -3.7 | 0.006 | 7/19 (J82, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.732×** | -3.5 | 0.012 | 9/33 (J82, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.55 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3938. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SHP-77 (line)]] | alt | 97.6 | 0 | 25 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0879× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.170× (z -10.8) |
| [[LoVo (line)]] | wt | 10.1 | 1 | 2 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 6.73× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.155× (z -9.1) |
| [[A-427 (line)]] | wt | 8.40 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.104× (z -9.7) ⚠ cell-cycle shift, explains ~58% of this change |
| [[A498 (line)]] | wt | 3.30 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 11.4× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.0653× (z -10.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 26.4 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.193× (z -8.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 6.41 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 8.05× (z +8.8) | [[Digitoxin (drug)]] 5 µM 0.0834× (z -10.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 9.21 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0777× (z -10.1) |
| [[SW480 (line)]] | alt | 4.45 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 13.5× (z +11.1) | — |
| [[A-172 (line)]] | wt | 4.53 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0840× (z -9.2) |
| [[AN3 CA (line)]] | alt | 27.7 | 0 | 1 | — | [[Filgotinib (drug)]] 0.5 µM 0.0754× (z -8.5) |
| [[BT-474 (line)]] | alt | 5.42 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0654× (z -8.6) |
| [[HOP62 (line)]] | alt | 5.55 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0777× (z -9.4) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 1.49 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 47.3× (z +8.9) | — |
| [[SK-MEL-2 (line)]] | alt | 12.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.124× (z -9.1) ⚠ cell-cycle shift, explains ~84% of this change |
| [[A549 (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.948 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.09 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.42 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.52 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.70 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.857 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.80 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.30 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.53 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.60 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.43 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3938), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GRIA2]] | +0.69 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[NELL1]] | +0.63 | +0.59 / +0.67 | both halves | 7e-06 |  |
| [[EFR3B]] | +0.61 | +0.39 / +0.65 | both halves | 5e-05 |  |
| [[TRPM8]] | +0.59 | +0.44 / +0.52 | both halves | 3e-05 |  |
| [[SRRM4]] | +0.57 | +0.64 / +0.51 | both halves | 1e-05 |  |
| [[ASCL1]] | +0.56 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[OLFM1]] | +0.56 | +0.50 / +0.42 | both halves | 4e-05 |  |
| [[CHST8]] | +0.56 | +0.49 / +0.63 | both halves | 1e-05 | pathway: Asparagine N-linked glycosylation |
| [[ESRRG]] | +0.56 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[IGFBP5]] | +0.56 | +0.50 / +0.43 | both halves | 3e-05 |  |
| [[RIT2]] | +0.55 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[DGKB]] | +0.55 | +0.62 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF234]] | -0.53 | -0.41 / -0.40 | both halves | 5e-05 |  |
| [[ITPA]] | -0.50 | -0.24 / -0.49 | both halves | 5e-04 |  |
| [[GPATCH2]] | -0.49 | -0.28 / -0.27 | both halves | 3e-04 |  |
| [[C1orf109]] | -0.47 | -0.29 / -0.34 | both halves | 3e-04 |  |
| [[UQCC1]] | -0.47 | -0.41 / -0.27 | both halves | 3e-04 |  |
| [[FAIM]] | -0.47 | -0.24 / -0.33 | both halves | 5e-04 |  |
| [[PAAF1]] | -0.46 | -0.23 / -0.39 | both halves | 5e-04 |  |
| [[MTRF1]] | -0.46 | -0.31 / -0.21 | both halves | 6e-04 |  |
| [[GTF3C4]] | -0.46 | -0.22 / -0.33 | both halves | 6e-04 |  |
| [[TRMT61B]] | -0.46 | -0.30 / -0.36 | both halves | 2e-04 |  |
| [[C8orf33]] | -0.45 | -0.14 / -0.36 | ⚠ not reproduced | 0.002 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 14, C 1. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LRFN2]] | B | LRFN2 activity raises MAN1C1's level | lines that do not express LRFN2 (35) vs lines expressing it (15) | 3.04× lower at baseline in the lines without LRFN2 | 0.006 | ⚠ within organs, on part of the lines; also absent: MAGEA4, CALCA, PI15; maybe low, not absent |
| [[RET]] | B | RET activity raises MAN1C1's level | lines that do not express RET (28) vs lines expressing it (22) | 2.03× lower at baseline in the lines without RET | 0.011 | ⚠ within organs, on part of the lines; also absent: CHD5, KIF1A, NPTX1 |
| [[LINC02197]] | B | LINC02197 activity raises MAN1C1's level | lines that do not express LINC02197 (35) vs lines expressing it (15) | 2.26× lower at baseline in the lines without LINC02197 | 0.031 | ⚠ within organs, on part of the lines; also absent: RIT2, SNTG1, CALCA; maybe low, not absent |
| [[CALCA]] | B | CALCA activity raises MAN1C1's level | lines that do not express CALCA (45) vs lines expressing it (5) | 4.37× lower at baseline in the lines without CALCA | 0.032 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, CGA, RIT2 |
| [[H19]] | B | H19 activity raises MAN1C1's level | lines that do not express H19 (38) vs lines expressing it (12) | 2.30× lower at baseline in the lines without H19 | 0.033 | ⚠ within organs, on part of the lines; also absent: CALCA, SYT4, CGA |
| [[SYT4]] | B | SYT4 activity raises MAN1C1's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 2.94× lower at baseline in the lines without SYT4 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA |
| [[SEMA6B]] | B | SEMA6B activity raises MAN1C1's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 2.13× lower at baseline in the lines without SEMA6B | 0.049 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[CHGB]] | B | CHGB activity raises MAN1C1's level | lines that do not express CHGB (33) vs lines expressing it (17) | 1.88× lower at baseline in the lines without CHGB | 0.063 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2 |
| [[EFR3B]] | B | EFR3B activity raises MAN1C1's level | lines that do not express EFR3B (10) vs lines expressing it (40) | 2.22× lower at baseline in the lines without EFR3B | 0.074 | ⚠ within organs, on part of the lines; also absent: RTN4RL1, SEPTIN5, NT5M; maybe low, not absent |
| [[RIT2]] | B | RIT2 activity raises MAN1C1's level | lines that do not express RIT2 (44) vs lines expressing it (6) | 3.21× lower at baseline in the lines without RIT2 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, KCNB2, SYT4 |
| [[C14orf132]] | B | C14orf132 activity raises MAN1C1's level | lines that do not express C14orf132 (19) vs lines expressing it (31) | 2.02× lower at baseline in the lines without C14orf132 | 0.081 | ⚠ within organs, on part of the lines; also absent: SLC22A17, ZFP28, ADAMTS7 |
| [[SRRM4]] | B | SRRM4 activity raises MAN1C1's level | lines that do not express SRRM4 (41) vs lines expressing it (9) | 2.76× lower at baseline in the lines without SRRM4 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: KCNB2, RIT2, CALCA; maybe low, not absent |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FOXO6]] | B | MAN1C1 activity raises FOXO6's level | lines that do not express MAN1C1 (11) vs lines expressing it (39) | 1.32× lower at baseline in the lines without MAN1C1 | 0.029 | ⚠ within organs, on part of the lines; also absent: DHRS2; maybe low, not absent |
| [[C14orf132]] | B | MAN1C1 activity raises C14orf132's level | lines that do not express MAN1C1 (11) vs lines expressing it (39) | 2.73× lower at baseline in the lines without MAN1C1 | 0.033 | ⚠ within organs, on part of the lines; also absent: DHRS2; maybe low, not absent |
| [[ACBD7]] | B | MAN1C1 activity raises ACBD7's level | lines that do not express MAN1C1 (11) vs lines expressing it (39) | 1.58× lower at baseline in the lines without MAN1C1 | 0.049 | ⚠ within organs, on part of the lines; also absent: DHRS2; maybe low, not absent |
| [[PDZD7]] | B | MAN1C1 activity raises PDZD7's level | lines that do not express MAN1C1 (11) vs lines expressing it (39) | 1.40× lower at baseline in the lines without MAN1C1 | 0.061 | ⚠ within organs, on part of the lines; also absent: DHRS2; maybe low, not absent |
| [[SEMA6B]] | B | MAN1C1 activity raises SEMA6B's level | lines that do not express MAN1C1 (11) vs lines expressing it (39) | 2.41× lower at baseline in the lines without MAN1C1 | 0.063 | ⚠ within organs, on part of the lines; also absent: DHRS2; maybe low, not absent |
| [[NOVA2]] | B | MAN1C1 activity raises NOVA2's level | lines that do not express MAN1C1 (11) vs lines expressing it (39) | 1.75× lower at baseline in the lines without MAN1C1 | 0.066 | ⚠ within organs, on part of the lines; also absent: DHRS2; maybe low, not absent |
| [[PKNOX2]] | B | MAN1C1 activity raises PKNOX2's level | lines that do not express MAN1C1 (11) vs lines expressing it (39) | 1.56× lower at baseline in the lines without MAN1C1 | 0.078 | ⚠ within organs, on part of the lines; also absent: DHRS2; maybe low, not absent |
| [[TMEM108]] | B | MAN1C1 activity raises TMEM108's level | lines that do not express MAN1C1 (11) vs lines expressing it (39) | 1.44× lower at baseline in the lines without MAN1C1 | 0.087 | ⚠ within organs, on part of the lines; also absent: DHRS2; maybe low, not absent |
| [[TMEM178B]] | B | MAN1C1 activity raises TMEM178B's level | lines that do not express MAN1C1 (11) vs lines expressing it (39) | 3.41× lower at baseline in the lines without MAN1C1 | 0.090 | ⚠ within organs, on part of the lines; also absent: DHRS2; maybe low, not absent |
| [[SLC29A4]] | B | MAN1C1 activity raises SLC29A4's level | lines that do not express MAN1C1 (11) vs lines expressing it (39) | 1.75× lower at baseline in the lines without MAN1C1 | 0.095 | ⚠ within organs, on part of the lines; also absent: DHRS2; maybe low, not absent |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.434). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.7, 36.2); signed map (43.7, 33.8). **Vector** length 62.5, 10.3% of its response variance represented; |z| ≥ 3 in 1,148 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +3.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +6.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +16.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.2 | +1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.4 | +8.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +1.8 |
|  | [[Glycyrrhizic acid (drug)]] 0.05 µM |  | +1.5 | +0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.5 | +10.0 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.4 | +1.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.5 | -8.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | -2.1 | -2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -3.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.9 | +2.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.9 | -8.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | +1.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.8 | -1.5 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -2.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -6.1 |

## What is on record

|  |  |
|---|---|
| Name | mannosidase alpha class 1C member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:25,616,791-25,784,450 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HMIC |
| Gene groups (HGNC) | Mannosidases alpha class 1 |
| Reactome | 8 pathways, smallest: Progressive trimming of alpha-1,2-linked mannose residues from Man9/8/7GlcNAc2 to produce Man5GlcNAc2; N-glycan trimming and elongation in the cis-Golgi; Intra-Golgi traffic |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NR34](https://www.uniprot.org/uniprotkb/Q9NR34) (Mannosyl-oligosaccharide 1,2-alpha-mannosidase IC):

> Involved in the maturation of Asn-linked oligosaccharides. Trim alpha-1,2-linked mannose residues from Man(9)GlcNAc(2) to produce first Man(8)GlcNAc(2) then Man(6)GlcNAc and a small amount of Man(5)GlcNAc.

**Summary**, from NCBI Gene [57134](https://www.ncbi.nlm.nih.gov/gene/57134):

> Predicted to enable mannosyl-oligosaccharide 1,2-alpha-mannosidase activity. Predicted to be involved in ERAD pathway. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19080](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19080) · Entrez [57134](https://www.ncbi.nlm.nih.gov/gene/57134) · UniProt [Q9NR34](https://www.uniprot.org/uniprotkb/Q9NR34) · Ensembl [ENSG00000117643](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117643)

## Data

Gene col 3938: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3938); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3938, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3938]; `tensor/DDL_lfc|DDL_z.npy` [3938]; `embed/gene_vectors.npy` [3938]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3938 or target_col == 3938). Every well: [[MAN1C1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAN1C1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
