---
symbol: "CGNL1"
type: "gene"
col: 4925
ensembl_id: "ENSG00000128849"
name: "cingulin like 1"
location: "15q21.3"
module: 14
arm: "+"
pooled_cpm: 15.69
n_lines_expressing: 29
n_dd_up: 30
n_dd_down: 25
n_dd_up_clean: 26
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 11
direction_downstream: 17
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# CGNL1

*cingulin like 1* — 15q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.28× (z +24.3, q 0e+00, up in 17 of 26 measured lines).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Doxorubicin (hydrochloride) (drug)]] 5 µM: 0.610× (z -6.9, q 3e-09, down in 16 of 25 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RRAD]] (+0.67, fdr 7e-06), [[NEURL3]] (+0.67, fdr 7e-06), [[ANO9]] (+0.65, fdr 7e-06); moves opposite to [[TIMM23B-AGAP6]] (-0.52, fdr 3e-05), [[EHMT1]] (-0.50, fdr 3e-05), [[UBE3C]] (-0.48, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[ELF3]] → it (grade B ⚠); 17 go from it, the strongest it → [[RND1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4925.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.28×** | +24.3 | 0e+00 | 17/26 (J82, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.00×** | +14.1 | 8e-43 | 15/27 (NCI-H1573, NCI-H2030, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **2.27×** | +11.4 | 9e-28 | 15/25 (J82, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.89×** | +9.2 | 4e-18 | 13/25 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.74×** | +8.0 | 2e-13 | 13/25 (NCI-H2030, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.24×** | +6.1 | 1e-07 | 13/25 (HepG2/C3A, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.54×** | +6.0 | 2e-07 | 10/26 (HS-578T, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.45×** | +5.9 | 2e-07 | 14/27 (HepG2/C3A, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.53×** | +5.9 | 2e-07 | 10/24 (HepG2/C3A, Hs 766T, …) | all doses, stronger at high dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~19% of this change | **1.31×** | +5.4 | 3e-06 | 12/27 (COLO 205, C-33 A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.45×** | +5.4 | 4e-06 | 6/26 (NCI-H1573, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.41×** | +5.0 | 3e-05 | 10/25 (BT-474, SW 900, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.40×** | +4.9 | 4e-05 | 12/25 (A498, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Binimetinib (drug)]] 5 µM |  | **1.38×** | +4.7 | 9e-05 | 7/27 (Hs 766T, HS-578T, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +4.6 | 1e-04 | 9/27 (HepG2/C3A, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.31×** | +4.6 | 2e-04 | 9/27 (HepG2/C3A, SK-MEL-2, …) | rises with dose | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.002 | 7/25 (BT-474, HepG2/C3A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4925.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.610×** | -6.9 | 3e-09 | 16/25 (A-172, COLO 205, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.684×** | -5.5 | 1e-05 | 13/26 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.687×** | -5.4 | 1e-05 | 14/26 (NCI-H1792, SNU-423, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.695×** | -5.3 | 2e-05 | 10/26 (NCI-H1792, CFPAC-1, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.741×** | -4.3 | 0.002 | 13/25 (SNU-423, NCI-H1792, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.817×** | -4.1 | 0.003 | 13/27 (CFPAC-1, Panc 03.27, …) | top dose only |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.752×** | -4.1 | 0.003 | 10/26 (NCI-H2347, A498, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | **0.823×** | -4.0 | 0.005 | 9/26 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.754×** | -3.9 | 0.005 | 4/26 (SW480, NCI-H1573, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.05 µM |  | **0.764×** | -3.9 | 0.005 | 9/27 (BT-474, A498, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.756×** | -3.8 | 0.009 | 10/25 (NCI-H1792, SNU-423, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **0.777×** | -3.7 | 0.012 | 7/26 (NCI-H1792, SNU-423, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.779×** | -3.6 | 0.013 | 7/26 (SW480, NCI-H2030, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.783×** | -3.5 | 0.016 | 4/26 (SW480, NCI-H2030, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.789×** | -3.4 | 0.022 | 12/26 (A549, Panc 03.27, …) | all doses, flat |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.636×** | -3.4 | 0.022 | 9/23 (BT-474, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **0.798×** | -3.3 | 0.033 | 9/24 (J82, NCI-H2347, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4925. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 49.5 | 2 | 6 (5 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +12.4) | [[Dinaciclib (drug)]] 5 µM 0.121× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -9.9) |
| [[SW480 (line)]] | alt | 18.2 | 0 | 8 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.144× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[5-Azacytidine (drug)]] 5 µM 0.208× (z -9.7) |
| [[BT-474 (line)]] | alt | 30.9 | 5 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.62× (z +14.5) | — |
| [[HT-29 (line)]] | alt | 32.0 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -15.2) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.133× (z -12.2) |
| [[SNU-423 (line)]] | alt | 43.0 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +9.6) | [[Clobetasol propionate (drug)]] 0.5 µM 0.184× (z -8.9) |
| [[A498 (line)]] | wt | 80.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +11.3) | — |
| [[J82 (line)]] | alt | 6.87 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +14.9) | — |
| [[NCI-H2347 (line)]] | alt | 35.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +12.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.78× (z +8.6) | — |
| [[CFPAC-1 (line)]] | alt | 61.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -15.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0242× (z -14.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HepG2_C3A (line)]] | wt | 44.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.86× (z +13.1) | — |
| [[Hs 766T (line)]] | wt | 16.2 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.120× (z -12.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 2.44 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 9.10 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.07 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.84 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.48 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.72 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 7.08 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 39.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.57 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.92 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.75 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.71 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.13 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4925), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RRAD]] | +0.67 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[NEURL3]] | +0.67 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[ANO9]] | +0.65 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[CADM1]] | +0.65 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[DMRTA1]] | +0.63 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[TMPRSS3]] | +0.62 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[TNFRSF9]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[BTN2A2]] | +0.62 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[GPRC5B]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[CYRIA]] | +0.61 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[BDKRB2]] | +0.60 | +0.51 / +0.57 | both halves | 1e-05 |  |
| [[NINJ1]] | +0.60 | +0.63 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM23B-AGAP6]] | -0.52 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[EHMT1]] | -0.50 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[UBE3C]] | -0.48 | -0.45 / -0.46 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 8, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF3]] | B | ELF3 activity raises CGNL1's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 2.10× lower at baseline in the lines without ELF3 | 0.025 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[PPFIBP2]] | B | PPFIBP2 activity lowers CGNL1's level | lines that do not express PPFIBP2 (5) vs lines expressing it (45) | 3.75× higher at baseline in the lines without PPFIBP2 | 0.052 | ⚠ within organs, on part of the lines; also absent: LRRC8D |
| [[STAP2]] | B | STAP2 activity raises CGNL1's level | lines that do not express STAP2 (12) vs lines expressing it (38) | 1.42× lower at baseline in the lines without STAP2 | 0.054 | ⚠ within organs, on part of the lines; also absent: GALM, BDH1, ENSG00000263325; maybe low, not absent |
| [[CDKN2A]] | B | CDKN2A activity raises CGNL1's level | lines that do not express CDKN2A (22) vs lines expressing it (28) | 1.48× lower at baseline in the lines without CDKN2A | 0.058 | ⚠ within organs, on part of the lines; co-occurs with CDKN2B; also absent: CDKN2B-AS1, TEX15, APOE |
| [[PGBD5]] | B | PGBD5 activity raises CGNL1's level | lines that do not express PGBD5 (28) vs lines expressing it (22) | 2.15× lower at baseline in the lines without PGBD5 | 0.066 | ⚠ within organs, on part of the lines; also absent: TMEM163, LRRN1, ELAVL2 |
| [[BDKRB2]] | B | BDKRB2 activity raises CGNL1's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 2.73× lower at baseline in the lines without BDKRB2 | 0.073 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[ANO9]] | B | ANO9 activity raises CGNL1's level | lines that do not express ANO9 (22) vs lines expressing it (28) | 1.93× lower at baseline in the lines without ANO9 | 0.077 | ⚠ within organs, on part of the lines; also absent: ELF3, PRAG1, TRIM29 |
| [[NOD2]] | B | NOD2 activity raises CGNL1's level | lines that do not express NOD2 (17) vs lines expressing it (33) | 2.20× lower at baseline in the lines without NOD2 | 0.083 | ⚠ within organs, on part of the lines; also absent: STAT5A, TLR2, BDKRB2 |
| [[GPRC5B]] | C | GPRC5B activity raises CGNL1's level | lines that do not express GPRC5B (27) vs lines expressing it (23) | 2.37× lower at baseline in the lines without GPRC5B | 0.017 | ⚠ within organs, on part of the lines; also absent: PALMD, FYB1, AK5; co-absent with the target |
| [[ELF3-AS1]] | C | ELF3-AS1 activity raises CGNL1's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.88× lower at baseline in the lines without ELF3-AS1 | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent; co-absent with the target |
| [[SSTR2]] | C | SSTR2 activity raises CGNL1's level | lines that do not express SSTR2 (25) vs lines expressing it (25) | 2.13× lower at baseline in the lines without SSTR2 | 0.091 | ⚠ within organs, on part of the lines; also absent: PPP2R2B, DKK3, ENSG00000260517; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 15, C 2. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RND1]] | B | CGNL1 activity raises RND1's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 2.31× lower at baseline in the lines without CGNL1 | 0.007 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |
| [[ATP1B1]] | B | CGNL1 activity raises ATP1B1's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 2.19× lower at baseline in the lines without CGNL1 | 0.014 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |
| [[DMRTA1]] | B | CGNL1 activity raises DMRTA1's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 1.70× lower at baseline in the lines without CGNL1 | 0.017 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |
| [[RHBDL2]] | B | CGNL1 activity raises RHBDL2's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 1.69× lower at baseline in the lines without CGNL1 | 0.031 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |
| [[BMF]] | B | CGNL1 activity raises BMF's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 2.04× lower at baseline in the lines without CGNL1 | 0.032 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |
| [[LITAF]] | B | CGNL1 activity raises LITAF's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 1.80× lower at baseline in the lines without CGNL1 | 0.039 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |
| [[EPB41]] | B | CGNL1 activity raises EPB41's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 1.47× lower at baseline in the lines without CGNL1 | 0.050 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |
| [[ATL1]] | B | CGNL1 activity raises ATL1's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 1.95× lower at baseline in the lines without CGNL1 | 0.051 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |
| [[ELF3]] | B | CGNL1 activity raises ELF3's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 2.28× lower at baseline in the lines without CGNL1 | 0.051 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |
| [[STARD10]] | B | CGNL1 activity raises STARD10's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 1.45× lower at baseline in the lines without CGNL1 | 0.064 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |
| [[NOD2]] | B | CGNL1 activity raises NOD2's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 1.83× lower at baseline in the lines without CGNL1 | 0.073 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |
| [[STAP2]] | B | CGNL1 activity raises STAP2's level | lines that do not express CGNL1 (21) vs lines expressing it (29) | 1.60× lower at baseline in the lines without CGNL1 | 0.081 | ⚠ within organs, on part of the lines; also absent: GPRC5B, SAA4, NSUN7 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.680). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.3, 1.6); signed map (45.8, 10.4). **Vector** length 88.4, 24.3% of its response variance represented; |z| ≥ 3 in 875 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +6.3 | +24.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +14.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.4 | +8.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.7 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.8 | +2.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.5 | +4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.3 | +5.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.1 | +3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +4.0 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | -2.9 | -3.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.8 | -1.5 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.6 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.5 | -5.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.4 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | cingulin like 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.3 — chr15:57,375,967-57,550,717 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14957, JACOP, KIAA1749, PCING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q0VF96](https://www.uniprot.org/uniprotkb/Q0VF96) (Cingulin-like protein 1):

> May be involved in anchoring the apical junctional complex, especially tight junctions, to actin-based cytoskeletons.

**Summary**, from NCBI Gene [84952](https://www.ncbi.nlm.nih.gov/gene/84952):

> This gene encodes a member of the cingulin family. The encoded protein localizes to both adherens and tight cell-cell junctions and mediates junction assembly and maintenance by regulating the activity of the small GTPases RhoA and Rac1. Heterozygous chromosomal rearrangements resulting in association of the promoter for this gene with the aromatase gene are a cause of aromatase excess syndrome. Alternatively spliced transcript variants have been observed for this gene. [provided by RefSeq, Nov …

**Accessions** — [HGNC:25931](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25931) · Entrez [84952](https://www.ncbi.nlm.nih.gov/gene/84952) · UniProt [Q0VF96](https://www.uniprot.org/uniprotkb/Q0VF96) · Ensembl [ENSG00000128849](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128849)

## Data

Gene col 4925: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4925); `tables/drug_effects.parquet` (57 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4925, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4925]; `tensor/DDL_lfc|DDL_z.npy` [4925]; `embed/gene_vectors.npy` [4925]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4925 or target_col == 4925). Every well: [[CGNL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CGNL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
