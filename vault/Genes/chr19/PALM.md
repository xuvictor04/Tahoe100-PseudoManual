---
symbol: "PALM"
type: "gene"
col: 1822
ensembl_id: "ENSG00000099864"
name: "paralemmin"
location: "19p13.3"
module: 128
arm: "+"
pooled_cpm: 8.78
n_lines_expressing: 29
n_dd_up: 12
n_dd_down: 22
n_dd_up_clean: 9
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 18
direction_downstream: 10
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# PALM

*paralemmin* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.89× (z +12.8, q 1e-34, up in 6 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 1.58× (z +8.2, q 6e-14, up in 11 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (7 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.450× (z -9.9, q 2e-20, down in 22 of 26 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CBFA2T3]] (+0.65, fdr 7e-06), [[KCNQ2]] (+0.63, fdr 1e-05), [[JPH3]] (+0.62, fdr 7e-06).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[CHD5]] → it (grade B ⚠); 10 go from it, the strongest it → [[ADAP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1822.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.89×** | +12.8 | 1e-34 | 6/12 (PANC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.68×** | +12.3 | 2e-32 | 11/21 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.58×** | +8.2 | 6e-14 | 11/24 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +7.4 | 2e-11 | 10/17 (NCI-H2030, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.48×** | +4.9 | 1e-04 | 12/26 (HepG2/C3A, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Thymol (drug)]] 0.5 µM |  | **1.36×** | +3.9 | 0.011 | 6/24 (CHP-212, NCI-H1573, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.37×** | +3.8 | 0.011 | 11/26 (NCI-H460, HepG2/C3A, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.28×** | +3.5 | 0.029 | 12/26 (NCI-H460, A-427, …) | all doses, flat | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.47×** | +3.4 | 0.037 | 3/24 (MIA PaCa-2, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Rapamycin (drug)]] 5 µM |  | 1.20× | +3.2 | 0.072 | 7/26 (A498, NCI-H2347, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 0.5 µM |  | **1.28×** | +3.1 | 0.082 | 0/26 | inconsistent across doses |  |
| [[Alpelisib (drug)]] 0.05 µM |  | **1.30×** | +3.1 | 0.082 | 4/26 (NCI-H2030, SNU-423, …) | inconsistent across doses |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.41×** | +3.1 | 0.096 | 4/21 (A-427, A-172, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1822.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.450×** | -9.9 | 2e-20 | 22/26 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.518×** | -8.2 | 7e-14 | 19/26 (MIA PaCa-2, A-427, …) | two highest doses | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.536×** | -7.8 | 2e-12 | 18/26 (LoVo, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.570×** | -7.0 | 4e-10 | 19/26 (NCI-H23, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.566×** | -6.8 | 1e-09 | 18/26 (MIA PaCa-2, A-427, …) | two highest doses | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.587×** | -6.6 | 3e-09 | 18/24 (Hs 766T, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.605×** | -6.2 | 3e-08 | 20/26 (Hs 766T, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.627×** | -5.8 | 5e-07 | 16/26 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.639×** | -5.6 | 2e-06 | 16/26 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.650×** | -5.3 | 5e-06 | 14/26 (A-172, H4, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.681×** | -4.8 | 1e-04 | 11/26 (MIA PaCa-2, A-427, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.768×** | -4.6 | 2e-04 | 12/26 (MIA PaCa-2, SW 900, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~79% of this change | **0.701×** | -4.4 | 5e-04 | 16/26 (MIA PaCa-2, LoVo, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **0.699×** | -4.3 | 8e-04 | 15/25 (MIA PaCa-2, A-427, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.675×** | -3.5 | 0.019 | 9/26 (MIA PaCa-2, NCI-H23, …) | two highest doses | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.565×** | -3.3 | 0.032 | 10/26 (A-427, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.765×** | -3.3 | 0.032 | 5/25 (A-172, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[EX229 (drug)]] 0.05 µM |  | **0.760×** | -3.2 | 0.039 | 9/26 (NCI-H23, NCI-H460, …) | inconsistent across doses |  |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 5 µM |  | **0.832×** | -3.2 | 0.039 | 5/26 (SNU-423, C-33 A, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.593×** | -3.0 | 0.063 | 7/24 (Hs 766T, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.47 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1822. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 47.1 | 0 | 15 (8 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0849× (z -19.3) |
| [[Hs 766T (line)]] | wt | 32.1 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0610× (z -16.4) |
| [[A-427 (line)]] | wt | 22.0 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.139× (z -13.5) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.135× (z -13.2) |
| [[NCI-H23 (line)]] | alt | 14.2 | 0 | 5 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.138× (z -11.0) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.196× (z -8.7) |
| [[SW 900 (line)]] | alt | 7.96 | 0 | 5 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.166× (z -9.5) |
| [[A-172 (line)]] | wt | 58.7 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -11.4) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.335× (z -8.7) |
| [[LoVo (line)]] | wt | 14.9 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -17.7) ⚠ cell-cycle shift, explains ~58% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.224× (z -10.3) |
| [[C-33 A (line)]] | alt | 35.0 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.235× (z -13.0) ⚠ cell-cycle shift, explains ~58% of this change |
| [[Panc 03.27 (line)]] | alt | 4.44 | 0 | 2 (1 ⚠) | — | [[Sulfatinib (drug)]] 5 µM 0.0524× (z -9.1) |
| [[A498 (line)]] | wt | 10.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.47× (z +15.9) | — |
| [[BT-474 (line)]] | alt | 10.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 6.61 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.0× (z +12.7) | — |
| [[NCI-H2030 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.270× (z -9.1) ⚠ cell-cycle shift, explains ~58% of this change |
| [[PANC-1 (line)]] | alt | 5.40 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.51× (z +16.4) | — |
| [[SW480 (line)]] | alt | 6.58 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.156× (z -9.2) |
| [[A549 (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.83 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.966 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 7.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.17 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.15 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.809 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.913 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.896 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.763 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.89 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 7.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.803 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.934 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.932 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1822), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBFA2T3]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[KCNQ2]] | +0.63 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[JPH3]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[ELFN1]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[PRRX2]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[LIMS2]] | +0.58 | +0.55 / +0.61 | both halves | 1e-05 |  |
| [[CECR2]] | +0.57 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[CHD5]] | +0.57 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[FSD1]] | +0.55 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[SHC2]] | +0.55 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[EBF4]] | +0.54 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[TCEA2]] | +0.54 | +0.46 / +0.57 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 8, C 10. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHD5]] | B | CHD5 activity raises PALM's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 2.13× lower at baseline in the lines without CHD5 | 0.031 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[KLKP1-1]] | B | KLKP1-1 activity lowers PALM's level | lines that do not express KLKP1-1 (11) vs lines expressing it (39) | 2.08× higher at baseline in the lines without KLKP1-1 | 0.044 | ⚠ within organs, on part of the lines; also absent: CRISPLD2, ENSG00000286263, MILR1; maybe low, not absent |
| [[PDZD4]] | B | PDZD4 activity raises PALM's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 2.61× lower at baseline in the lines without PDZD4 | 0.056 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12 |
| [[DPYSL5]] | B | DPYSL5 activity strengthens PALM's drug response | lines that do not express DPYSL5 (12) vs lines expressing it (14) | the lines without DPYSL5 respond 0.64× as strongly (z diff +1.08); strongest at Homoharringtonine 0.5 µM: 0.68x vs 0.42x (z diff +3.8) | 0.073 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5; target measured in part of the lines; artifact flags |
| [[BRSK2]] | B | BRSK2 activity raises PALM's level | lines that do not express BRSK2 (14) vs lines expressing it (36) | 1.83× lower at baseline in the lines without BRSK2 | 0.083 | ⚠ within organs, on part of the lines; also absent: KIF26A, APLP1, E2F2; maybe low, not absent |
| [[EBF4]] | B | EBF4 activity raises PALM's level | lines that do not express EBF4 (12) vs lines expressing it (38) | 2.91× lower at baseline in the lines without EBF4 | 0.091 | ⚠ within organs, on part of the lines; also absent: CERCAM, FGD1, DCLK2 |
| [[SLC4A3]] | B | SLC4A3 activity raises PALM's level | lines that do not express SLC4A3 (8) vs lines expressing it (42) | 2.07× lower at baseline in the lines without SLC4A3 | 0.093 | ⚠ within organs, on part of the lines; also absent: SEMA6B, SLC29A4, MYO5A |
| [[SEMA6B]] | B | SEMA6B activity raises PALM's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.87× lower at baseline in the lines without SEMA6B | 0.098 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |
| [[DPYSL5]] | C | DPYSL5 activity raises PALM's level | lines that do not express DPYSL5 (30) vs lines expressing it (20) | 2.57× lower at baseline in the lines without DPYSL5 | 0.018 | ⚠ within organs, on part of the lines; also absent: JPH3, OLFM1, CHD5; co-absent with the target |
| [[MSI1]] | C | MSI1 activity raises PALM's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 3.25× lower at baseline in the lines without MSI1 | 0.019 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B; co-absent with the target |
| [[KIF1A]] | C | KIF1A activity raises PALM's level | lines that do not express KIF1A (34) vs lines expressing it (16) | 3.73× lower at baseline in the lines without KIF1A | 0.028 | ⚠ within organs, on part of the lines; also absent: MAGEA4, ENSG00000289309, KCNH7; co-absent with the target |
| [[LINC02643]] | C | LINC02643 activity raises PALM's level | lines that do not express LINC02643 (38) vs lines expressing it (12) | 3.40× lower at baseline in the lines without LINC02643 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMRN1, GCG, ENSG00000289530; co-absent with the target |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 3, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAP2]] | B | PALM activity raises ADAP2's level | lines that do not express PALM (21) vs lines expressing it (29) | 2.01× lower at baseline in the lines without PALM | 0.042 | ⚠ within organs, on part of the lines; also absent: CACNG4, FXYD6, BEGAIN |
| [[NFATC1]] | B | PALM activity raises NFATC1's level | lines that do not express PALM (21) vs lines expressing it (29) | 2.14× lower at baseline in the lines without PALM | 0.061 | ⚠ within organs, on part of the lines; also absent: CACNG4, FXYD6, BEGAIN |
| [[LRRC4B]] | B | PALM activity raises LRRC4B's level | lines that do not express PALM (21) vs lines expressing it (29) | 1.88× lower at baseline in the lines without PALM | 0.097 | ⚠ within organs, on part of the lines; also absent: CACNG4, FXYD6, BEGAIN |
| [[HES2]] | C | PALM activity raises HES2's level | lines that do not express PALM (21) vs lines expressing it (29) | 1.49× lower at baseline in the lines without PALM | 0.029 | ⚠ within organs, on part of the lines; also absent: CACNG4, FXYD6, BEGAIN; co-absent with the target |
| [[TBX1]] | C | PALM activity raises TBX1's level | lines that do not express PALM (21) vs lines expressing it (29) | 2.04× lower at baseline in the lines without PALM | 0.054 | ⚠ within organs, on part of the lines; also absent: CACNG4, FXYD6, BEGAIN; co-absent with the target |
| [[MSI1]] | C | PALM activity raises MSI1's level | lines that do not express PALM (21) vs lines expressing it (29) | 2.09× lower at baseline in the lines without PALM | 0.057 | ⚠ within organs, on part of the lines; also absent: CACNG4, FXYD6, BEGAIN; co-absent with the target |
| [[CYS1]] | C | PALM activity raises CYS1's level | lines that do not express PALM (21) vs lines expressing it (29) | 1.85× lower at baseline in the lines without PALM | 0.071 | ⚠ within organs, on part of the lines; also absent: CACNG4, FXYD6, BEGAIN; co-absent with the target |
| [[FBXO2]] | C | PALM activity raises FBXO2's level | lines that do not express PALM (21) vs lines expressing it (29) | 2.30× lower at baseline in the lines without PALM | 0.074 | ⚠ within organs, on part of the lines; also absent: CACNG4, FXYD6, BEGAIN; co-absent with the target |
| [[CACNG4]] | C | PALM activity raises CACNG4's level | lines that do not express PALM (21) vs lines expressing it (29) | 2.73× lower at baseline in the lines without PALM | 0.075 | ⚠ within organs, on part of the lines; also absent: CACNG4, FXYD6, BEGAIN; co-absent with the target |
| [[KCNQ2]] | C | PALM activity raises KCNQ2's level | lines that do not express PALM (21) vs lines expressing it (29) | 2.50× lower at baseline in the lines without PALM | 0.086 | ⚠ within organs, on part of the lines; also absent: CACNG4, FXYD6, BEGAIN; co-absent with the target |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.710). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.7, 38.3); signed map (24.4, 24.2). **Vector** length 66.5, 15.9% of its response variance represented; |z| ≥ 3 in 680 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.1 | +12.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +8.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.3 | +12.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +7.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.7 | +4.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.8 | +3.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +3.1 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.7 | +2.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +3.5 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -2.8 | -8.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -9.9 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.6 | -5.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -5.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | -2.0 | -5.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.0 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -4.8 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.9 | -3.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[EX229 (drug)]] 0.05 µM |  | -1.5 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | paralemmin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:708,935-748,329 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0270, PALM1 |
| Gene groups (HGNC) | Paralemmins |
| Matched by | ensembl_id |

**Function**, from UniProt [O75781](https://www.uniprot.org/uniprotkb/O75781) (Paralemmin-1):

> Involved in plasma membrane dynamics and cell process formation. Isoform 1 and isoform 2 are necessary for axonal and dendritic filopodia induction, for dendritic spine maturation and synapse formation in a palmitoylation-dependent manner.

**Summary**, from NCBI Gene [5064](https://www.ncbi.nlm.nih.gov/gene/5064):

> This gene encodes a member of the paralemmin protein family. The product of this gene is a prenylated and palmitoylated phosphoprotein that associates with the cytoplasmic face of plasma membranes and is implicated in plasma membrane dynamics in neurons and other cell types. Several alternatively spliced transcript variants have been identified, but the full-length nature of only two transcript variants has been determined. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:8594](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8594) · Entrez [5064](https://www.ncbi.nlm.nih.gov/gene/5064) · UniProt [O75781](https://www.uniprot.org/uniprotkb/O75781) · Ensembl [ENSG00000099864](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099864)

## Data

Gene col 1822: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1822); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1822, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1822]; `tensor/DDL_lfc|DDL_z.npy` [1822]; `embed/gene_vectors.npy` [1822]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1822 or target_col == 1822). Every well: [[PALM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PALM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
