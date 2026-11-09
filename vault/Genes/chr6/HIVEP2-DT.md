---
symbol: "HIVEP2-DT"
type: "gene"
col: 13855
ensembl_id: "ENSG00000232618"
name: "HIVEP2 divergent transcript"
location: "6q24.2"
module: 80
arm: "+"
pooled_cpm: 4.51
n_lines_expressing: 48
n_dd_up: 17
n_dd_down: 16
n_dd_up_clean: 11
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/080"]
generated_by: "tahoemap"
---

# HIVEP2-DT

*HIVEP2 divergent transcript* — 6q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.67× (z +17.1, q 0e+00, up in 30 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.381× (z -9.0, q 1e-16, down in 25 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF341-AS1]] (+0.72, fdr 1e-05), [[UBE2D3-AS1]] (+0.71, fdr 1e-05), [[LPXN]] (+0.71, fdr 7e-06); moves opposite to [[HEATR6]] (-0.68, fdr 7e-06), [[MMS19]] (-0.67, fdr 1e-05), [[CDK5RAP1]] (-0.67, fdr 7e-06).
> It is in [[Module 080]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13855.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.67×** | +17.1 | 0e+00 | 30/35 (SNU-423, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.23×** | +15.5 | 0e+00 | 30/35 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.70×** | +13.3 | 3e-38 | 10/12 (PANC-1, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.95×** | +10.1 | 1e-21 | 15/23 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **2.64×** | +8.7 | 4e-16 | 22/39 (PANC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.87×** | +8.3 | 1e-14 | 21/43 (A-427, HOP62, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.45×** | +8.0 | 8e-14 | 4/7 (HOP62, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.23×** | +7.5 | 6e-12 | 19/35 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +5.7 | 8e-07 | 14/31 (HOP62, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.65×** | +4.7 | 2e-04 | 15/40 (A-172, HEC-1-A, …) | top dose only |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.55×** | +4.1 | 0.002 | 12/39 (MIA PaCa-2, SNU-423, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.52×** | +3.8 | 0.008 | 8/33 (HOP62, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.05 µM |  | **1.50×** | +3.8 | 0.008 | 10/43 (PANC-1, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.03×** | +3.5 | 0.022 | 1/9 (SHP-77) | top dose only | noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.02×** | +3.4 | 0.023 | 10/38 (LoVo, RPMI-7951, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.38×** | +3.0 | 0.082 | 5/41 (HEC-1-A, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13855.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.381×** | -9.0 | 1e-16 | 25/43 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.442×** | -7.6 | 7e-12 | 27/43 (A-427, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.502×** | -6.4 | 2e-08 | 19/44 (NCI-H1573, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.507×** | -6.4 | 3e-08 | 22/42 (SW480, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.512×** | -6.3 | 4e-08 | 22/43 (SNU-423, A-427, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.540×** | -5.4 | 5e-06 | 22/38 (SHP-77, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.673×** | -5.2 | 1e-05 | 15/41 (SNU-423, BT-474, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change | **0.613×** | -4.6 | 3e-04 | 19/33 (NCI-H2030, SHP-77, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.654×** | -4.0 | 0.005 | 9/44 (NCI-H2030, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[NG25 (drug)]] 5 µM |  | **0.454×** | -3.9 | 0.007 | 13/29 (SW480, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~6% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.664×** | -3.8 | 0.007 | 18/39 (A549, A-427, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.669×** | -3.8 | 0.008 | 6/40 (NCI-H23, Hs 766T, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **0.675×** | -3.7 | 0.010 | 11/42 (hTERT-HPNE, A498, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | **0.769×** | -3.5 | 0.019 | 10/41 (COLO 205, NCI-H23, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.897× | -3.5 | 0.019 | 9/45 (MIA PaCa-2, NCI-H1573, …) | inconsistent across doses |  |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **0.704×** | -3.2 | 0.055 | 8/34 (SNU-423, AsPC-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.05 µM |  | **0.715×** | -3.1 | 0.055 | 16/43 (C32, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13855. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.103× (z -10.1) |
| [[NCI-H460 (line)]] | wt | 1.33 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 10.4× (z +9.6) | [[5-Azacytidine (drug)]] 5 µM 0.0430× (z -9.0) |
| [[A-172 (line)]] | wt | 2.50 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.0× (z +10.9) | — |
| [[HOP62 (line)]] | alt | 2.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.92× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 3.77 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0454× (z -9.7) |
| [[J82 (line)]] | alt | 2.54 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.71× (z +9.2) | — |
| [[NCI-H2030 (line)]] | alt | 8.13 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0784× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~30% of this change |
| [[PANC-1 (line)]] | alt | 3.03 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.31× (z +10.3) | — |
| [[SHP-77 (line)]] | alt | 8.22 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0473× (z -9.2) |
| [[SNU-423 (line)]] | alt | 8.84 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.0× (z +12.0) | — |
| [[SW480 (line)]] | alt | 4.66 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0942× (z -10.5) |
| [[A-427 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.85 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.93 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.52 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.47 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.16 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.01 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.83 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.904 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.43 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.31 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.15 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13855), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF341-AS1]] | +0.72 | +0.69 / +0.55 | both halves | 1e-05 |  |
| [[UBE2D3-AS1]] | +0.71 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[LPXN]] | +0.71 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[NEK8]] | +0.70 | +0.72 / +0.40 | both halves | 5e-05 |  |
| [[HIVEP2]] | +0.70 | +0.67 / +0.59 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[WAKMAR2]] | +0.69 | +0.70 / +0.42 | both halves | 4e-05 |  |
| [[NANOS3]] | +0.69 | +0.72 / +0.46 | both halves | 3e-05 |  |
| [[LINC02068]] | +0.69 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[GPR137]] | +0.68 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[LINC01348]] | +0.68 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[MZF1-AS1]] | +0.66 | +0.68 / +0.34 | both halves | 1e-04 |  |
| [[LEKR1]] | +0.66 | +0.67 / +0.38 | both halves | 7e-05 |  |
| [[ABCA10]] | +0.66 | +0.67 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HEATR6]] | -0.68 | -0.61 / -0.66 | both halves | 7e-06 |  |
| [[MMS19]] | -0.67 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[CDK5RAP1]] | -0.67 | -0.63 / -0.64 | both halves | 7e-06 |  |
| [[NFRKB]] | -0.66 | -0.66 / -0.49 | both halves | 1e-05 |  |
| [[MKRN2]] | -0.66 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[SLC9A6]] | -0.65 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[ANAPC4]] | -0.65 | -0.65 / -0.58 | both halves | 7e-06 |  |
| [[NBPF3]] | -0.65 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[RNF216P1]] | -0.65 | -0.68 / -0.39 | both halves | 5e-05 |  |
| [[WRAP73]] | -0.64 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[ACTR5]] | -0.64 | -0.67 / -0.42 | both halves | 4e-05 |  |
| [[HACE1]] | -0.64 | -0.60 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers HIVEP2-DT's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.4% of all compounds | 0.015 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ERRFI1-DT]] | B | ERRFI1-DT activity raises HIVEP2-DT's level | lines that do not express ERRFI1-DT (13) vs lines expressing it (37) | 1.48× lower at baseline in the lines without ERRFI1-DT | 0.044 | ⚠ within organs, on part of the lines; also absent: GCAWKR; maybe low, not absent |
| [[RIMS2]] | B | RIMS2 activity raises HIVEP2-DT's level | lines that do not express RIMS2 (23) vs lines expressing it (27) | 1.48× lower at baseline in the lines without RIMS2 | 0.057 | ⚠ within organs, on part of the lines; also absent: TWIST1, SLC6A17, RUNX3 |
| [[LINC01277]] | C | LINC01277 activity raises HIVEP2-DT's level | lines that do not express LINC01277 (4) vs lines expressing it (46) | 1.79× lower at baseline in the lines without LINC01277 | 0.049 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SYNJ2, TMC3-AS1, EPS8; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 080]]; 57 genes; every member is in the + arm (projection on the module's main direction 0.791). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.2, 11.1); signed map (21.8, -4.8). **Vector** length 92.8, 18.9% of its response variance represented; |z| ≥ 3 in 1,198 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.0 | +17.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.6 | +15.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.8 | +13.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.6 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.5 | +10.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.9 | +8.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.7 | +4.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.7 | +1.3 |
|  | [[Abiraterone acetate (drug)]] 0.05 µM |  | +1.4 | +2.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.4 | +0.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -4.0 | -6.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.9 | -9.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -3.6 | -7.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.5 | -6.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.3 | -5.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.8 | -6.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.6 | -2.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.3 | -3.8 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -2.3 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | HIVEP2 divergent transcript |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6q24.2 — chr6:142,946,406-142,957,945 (+) |
| Ensembl biotype | lncRNA |
| Also known as | PILA |
| Gene groups (HGNC) | Divergent transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55724](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55724) · Entrez [107986655](https://www.ncbi.nlm.nih.gov/gene/107986655) · Ensembl [ENSG00000232618](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232618)

## Data

Gene col 13855: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13855); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13855, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13855]; `tensor/DDL_lfc|DDL_z.npy` [13855]; `embed/gene_vectors.npy` [13855]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13855 or target_col == 13855). Every well: [[HIVEP2-DT — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HIVEP2-DT.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
