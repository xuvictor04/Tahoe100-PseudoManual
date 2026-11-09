---
symbol: "ATP6V1E2"
type: "gene"
col: 14702
ensembl_id: "ENSG00000250565"
name: "ATPase H+ transporting V1 subunit E2"
location: "2p21"
module: 10
arm: "+"
pooled_cpm: 12.45
n_lines_expressing: 46
n_dd_up: 20
n_dd_down: 11
n_dd_up_clean: 15
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 16
direction_downstream: 2
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# ATP6V1E2

*ATPase H+ transporting V1 subunit E2* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.11× (z +10.3, q 3e-22, up in 28 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.47× (z +7.6, q 5e-12, up in 21 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.507× (z -9.4, q 3e-18, down in 30 of 43 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FTCDNL1]] (+0.70, fdr 1e-05), [[GNAL]] (+0.65, fdr 1e-05), [[MRAS]] (+0.61, fdr 1e-05); moves opposite to [[IFT122]] (-0.49, fdr 5e-05), [[SIVA1]] (-0.47, fdr 2e-04), [[HAUS3]] (-0.47, fdr 3e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[ANKS1B]] → it (grade B ⚠); 2 go from it, the strongest it → [[HKDC1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14702.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.11×** | +10.3 | 3e-22 | 28/34 (NCI-H1573, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.10×** | +9.5 | 8e-19 | 19/24 (A-172, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +9.0 | 4e-17 | 12/16 (SW480, A-427, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +7.6 | 5e-12 | 21/43 (A549, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.42×** | +6.8 | 1e-09 | 22/43 (SK-MEL-2, HOP62, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.41×** | +6.7 | 2e-09 | 20/44 (SW480, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.47×** | +5.3 | 8e-06 | 17/42 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.42×** | +4.8 | 9e-05 | 16/42 (A-172, NCI-H23, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.39×** | +4.5 | 4e-04 | 12/41 (SW480, HOP62, …) | two highest doses | cell-cycle shift (explains ~6% here) |
| [[Darinaparsin (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.012 | 11/44 (NCI-H23, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.43×** | +3.5 | 0.021 | 9/36 (RPMI-7951, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.29×** | +3.5 | 0.024 | 12/42 (KATO III, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.052 | 9/42 (A549, C32, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.052 | 10/43 (C-33 A, NCI-H23, …) | top dose only |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.27×** | +3.2 | 0.052 | 10/43 (SHP-77, A-427, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.067 | 10/44 (NCI-H23, A-172, …) | two highest doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.36×** | +3.0 | 0.078 | 6/40 (SHP-77, Panc 03.27, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.24×** | +2.9 | 0.098 | 9/38 (BT-474, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.24×** | +2.9 | 0.098 | 9/41 (NCI-H23, SNU-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14702.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.507×** | -9.4 | 3e-18 | 30/43 (NCI-H23, KATO III, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.512×** | -9.3 | 4e-18 | 28/43 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.556×** | -8.1 | 8e-14 | 28/43 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.681×** | -5.3 | 1e-05 | 21/41 (NCI-H23, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.661×** | -4.9 | 1e-04 | 19/42 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.699×** | -4.8 | 2e-04 | 21/42 (PANC-1, A-427, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.582×** | -3.9 | 0.007 | 15/39 (NCI-H23, SNU-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.766×** | -3.7 | 0.015 | 13/42 (A-427, NCI-H661, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.617×** | -3.5 | 0.030 | 12/39 (KATO III, NCI-H2030, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~50% of this change | 0.842× | -3.4 | 0.040 | 22/42 (SHP-77, PANC-1, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.782×** | -3.2 | 0.060 | 8/43 (BT-474, HEC-1-A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.761×** | -3.2 | 0.060 | 15/44 (NCI-H23, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14702. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 58.5 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.163× (z -18.0) |
| [[LoVo (line)]] | wt | 20.2 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.272× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.326× (z -9.6) |
| [[NCI-H2030 (line)]] | alt | 24.7 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.184× (z -11.6) |
| [[PANC-1 (line)]] | alt | 12.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -13.0) ⚠ cell-cycle shift, explains ~50% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.213× (z -10.0) |
| [[A-427 (line)]] | wt | 51.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.352× (z -9.6) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.345× (z -9.4) |
| [[SW48 (line)]] | wt | 17.1 | 0 | 2 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0841× (z -11.1) |
| [[SW480 (line)]] | alt | 8.79 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.269× (z -8.6) |
| [[A-172 (line)]] | wt | 20.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.23× (z +11.4) ⚠ cell-cycle shift, explains ~50% of this change | — |
| [[A549 (line)]] | wt | 16.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -9.5) ⚠ cell-cycle shift, explains ~50% of this change |
| [[C32 (line)]] | wt | 7.80 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0848× (z -9.8) |
| [[HCT15 (line)]] | alt | 7.72 | 0 | 1 | — | [[Arbutin (drug)]] 5 µM 0.0617× (z -9.0) |
| [[HS-578T (line)]] | alt | 6.49 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.124× (z -8.7) |
| [[KATO III (line)]] | alt | 9.02 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.121× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 21.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -11.3) ⚠ cell-cycle shift, explains ~50% of this change |
| [[MIA PaCa-2 (line)]] | alt | 7.42 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0890× (z -11.2) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 27.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -14.1) ⚠ cell-cycle shift, explains ~50% of this change |
| [[SNU-423 (line)]] | alt | 8.51 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0836× (z -11.8) |
| [[A498 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.15 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.22 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.29 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.03 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.96 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.40 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.92 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 9.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.89 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14702), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FTCDNL1]] | +0.70 | +0.78 / +0.53 | both halves | 1e-05 |  |
| [[GNAL]] | +0.65 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[MRAS]] | +0.61 | +0.67 / +0.51 | both halves | 1e-05 |  |
| [[BEND6]] | +0.60 | +0.66 / +0.47 | both halves | 2e-05 |  |
| [[LINC00592]] | +0.58 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[CPEB1]] | +0.57 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[ANKS1B]] | +0.57 | +0.65 / +0.32 | both halves | 2e-04 |  |
| [[ARL14EP-DT]] | +0.57 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[SYT9-AS1]] | +0.56 | +0.62 / +0.45 | both halves | 3e-05 |  |
| [[SNHG26]] | +0.56 | +0.57 / +0.41 | both halves | 4e-05 |  |
| [[CCDC169]] | +0.56 | +0.57 / +0.45 | both halves | 3e-05 |  |
| [[RFPL1S]] | +0.55 | +0.55 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT122]] | -0.49 | -0.52 / -0.39 | both halves | 5e-05 |  |
| [[SIVA1]] | -0.47 | -0.52 / -0.30 | both halves | 2e-04 |  |
| [[HAUS3]] | -0.47 | -0.43 / -0.29 | both halves | 3e-04 |  |
| [[SYNJ1]] | -0.46 | -0.30 / -0.52 | both halves | 2e-04 |  |
| [[MIGA2]] | -0.46 | -0.44 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 15, C 1. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKS1B]] | B | ANKS1B activity raises ATP6V1E2's level | lines that do not express ANKS1B (18) vs lines expressing it (32) | 2.08× lower at baseline in the lines without ANKS1B | 0.003 | ⚠ within organs, on part of the lines; also absent: LHX2, CECR2, HS6ST3 |
| [[MIR1915HG]] | B | MIR1915HG activity raises ATP6V1E2's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 2.07× lower at baseline in the lines without MIR1915HG | 0.008 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[KATNAL2]] | B | KATNAL2 activity raises ATP6V1E2's level | lines that do not express KATNAL2 (8) vs lines expressing it (42) | 2.31× lower at baseline in the lines without KATNAL2 | 0.009 | ⚠ within organs, on part of the lines; also absent: LHFPL6, TTC7B, PRKAR2B; maybe low, not absent |
| [[FAXC]] | B | FAXC activity raises ATP6V1E2's level | lines that do not express FAXC (11) vs lines expressing it (39) | 1.86× lower at baseline in the lines without FAXC | 0.016 | ⚠ within organs, on part of the lines; also absent: NTN1, CYP46A1, CSRP2 |
| [[ANK2]] | B | ANK2 activity raises ATP6V1E2's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.97× lower at baseline in the lines without ANK2 | 0.018 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[FAM78B]] | B | FAM78B activity raises ATP6V1E2's level | lines that do not express FAM78B (15) vs lines expressing it (35) | 2.20× lower at baseline in the lines without FAM78B | 0.024 | ⚠ within organs, on part of the lines; also absent: SEMA6B, ENSG00000260498, TTYH2 |
| [[LINC01088]] | B | LINC01088 activity raises ATP6V1E2's level | lines that do not express LINC01088 (9) vs lines expressing it (41) | 1.82× lower at baseline in the lines without LINC01088 | 0.050 | ⚠ within organs, on part of the lines; also absent: PPP4R4, GPR155, PKIG; maybe low, not absent |
| [[FTCDNL1]] | B | FTCDNL1 activity raises ATP6V1E2's level | lines that do not express FTCDNL1 (11) vs lines expressing it (39) | 2.06× lower at baseline in the lines without FTCDNL1 | 0.052 | ⚠ within organs, on part of the lines; also absent: RHBDL3, SCN8A, DLX1; maybe low, not absent |
| [[ELFN1]] | B | ELFN1 activity raises ATP6V1E2's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 1.78× lower at baseline in the lines without ELFN1 | 0.058 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[FAM184A]] | B | FAM184A activity raises ATP6V1E2's level | lines that do not express FAM184A (13) vs lines expressing it (37) | 1.64× lower at baseline in the lines without FAM184A | 0.072 | ⚠ within organs, on part of the lines; co-occurs with BRAF; also absent: SMAD9, TUBA1A, MAPT; maybe low, not absent |
| [[GRID1]] | B | GRID1 activity raises ATP6V1E2's level | lines that do not express GRID1 (27) vs lines expressing it (23) | 1.48× lower at baseline in the lines without GRID1 | 0.079 | ⚠ within organs, on part of the lines; also absent: LINC02643, EPGN, MSI1; maybe low, not absent |
| [[ANKRD18B]] | B | ANKRD18B activity raises ATP6V1E2's level | lines that do not express ANKRD18B (23) vs lines expressing it (27) | 1.50× lower at baseline in the lines without ANKRD18B | 0.081 | ⚠ within organs, on part of the lines; also absent: ZNF229, SUSD5, HECW2 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HKDC1]] | C | ATP6V1E2 activity lowers HKDC1's level | lines that do not express ATP6V1E2 (4) vs lines expressing it (46) | 13.51× higher at baseline in the lines without ATP6V1E2 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HACE1, CSPG5, NCS1; maybe low, not absent; its own permutation p |
| [[LINC02934]] | C | ATP6V1E2 activity lowers LINC02934's level | lines that do not express ATP6V1E2 (4) vs lines expressing it (46) | 2.13× higher at baseline in the lines without ATP6V1E2 | 0.097 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HACE1, CSPG5, NCS1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.473). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (9.1, 33.7); signed map (38.1, -0.2). **Vector** length 60.7, 9.75% of its response variance represented; |z| ≥ 3 in 890 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +9.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.6 | +9.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.4 | +10.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.3 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.2 | +6.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.4 | +1.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.1 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +1.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.8 | +0.4 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.8 | -9.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | -2.4 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.5 | -4.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.4 | -8.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.3 | -9.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.1 | -1.2 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | -1.0 | -0.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.0 | -1.5 |
|  | [[ERK5-IN-2 (drug)]] 5 µM |  | -0.9 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | ATPase H+ transporting V1 subunit E2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:46,490,750-46,542,577 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC9341, VMA4, ATP6E1; previously ATP6EL2, ATP6V1EL2 |
| Gene groups (HGNC) | V-type ATPase subunits |
| Reactome | 13 pathways, smallest: Insulin receptor recycling; ROS and RNS production in phagocytes; Transferrin endocytosis and recycling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96A05](https://www.uniprot.org/uniprotkb/Q96A05) (V-type proton ATPase subunit E 2):

> Subunit of the V1 complex of vacuolar(H+)-ATPase (V-ATPase), a multisubunit enzyme composed of a peripheral complex (V1) that hydrolyzes ATP and a membrane integral complex (V0) that translocates protons. V-ATPase is responsible for acidifying and maintaining the pH of intracellular compartments and in some cell types, is targeted to the plasma membrane, where it is responsible for acidifying the extracellular environment.

**Summary**, from NCBI Gene [90423](https://www.ncbi.nlm.nih.gov/gene/90423):

> Predicted to enable proton-transporting ATPase activity, rotational mechanism. Predicted to be involved in regulation of macroautophagy. Predicted to act upstream of or within proton transmembrane transport. Predicted to be located in cytosol. Predicted to be part of proton-transporting two-sector ATPase complex, catalytic domain. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:18125](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18125) · Entrez [90423](https://www.ncbi.nlm.nih.gov/gene/90423) · UniProt [Q96A05](https://www.uniprot.org/uniprotkb/Q96A05) · Ensembl [ENSG00000250565](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000250565)

## Data

Gene col 14702: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14702); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14702, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14702]; `tensor/DDL_lfc|DDL_z.npy` [14702]; `embed/gene_vectors.npy` [14702]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14702 or target_col == 14702). Every well: [[ATP6V1E2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP6V1E2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
