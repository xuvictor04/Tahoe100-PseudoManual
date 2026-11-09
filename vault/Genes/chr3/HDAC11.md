---
symbol: "HDAC11"
type: "gene"
col: 8707
ensembl_id: "ENSG00000163517"
name: "histone deacetylase 11"
location: "3p25.1"
module: 159
arm: "+"
pooled_cpm: 8.4
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 28
n_dd_up_clean: 3
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 8
direction_downstream: 599
tags: ["gene", "module/159"]
generated_by: "tahoemap"
---

# HDAC11

*histone deacetylase 11* — 3p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.64× (z +6.9, q 3e-09, up in 8 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 1.37× (z +4.6, q 0.001, up in 9 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.322× (z -23.3, q 0e+00, down in 37 of 41 measured lines).
> Its strongest partners by |cos| (82 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 18 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAST3]] (+0.69, fdr 8e-05), [[ABTB1]] (+0.67, fdr 1e-05), [[ETNK2]] (+0.66, fdr 2e-05); moves opposite to [[ZNF827]] (-0.65, fdr 3e-05), [[MMADHC-DT]] (-0.64, fdr 0.001, ⚠ one half only (not replicated)), [[CRPPA]] (-0.64, fdr 4e-04), [[ZBED5]] (-0.63, fdr 3e-04).
> It is in [[Module 159]], a single-armed module (High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[ETNK2]] → it (grade B ⚠); 599 go from it, the strongest it → [[CDC23]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8707.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.64×** | +6.9 | 3e-09 | 8/16 (HEC-1-A, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.37×** | +4.6 | 0.001 | 9/46 (NCI-H1792, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.32×** | +4.1 | 0.008 | 10/33 (SHP-77, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.31×** | +3.9 | 0.011 | 10/46 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.29×** | +3.8 | 0.019 | 9/46 (SW48, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.57×** | +3.4 | 0.057 | 2/23 (SW1417, Panc 03.27) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.26×** | +3.4 | 0.065 | 8/38 (J82, SW1417, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 1.23× | +3.1 | 0.14 | 9/43 (HOP62, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | 1.24× | +3.1 | 0.14 | 9/42 (NCI-H1573, PANC-1, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8707.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.322×** | -23.3 | 0e+00 | 37/41 (HOP62, LS 180, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.258×** | -19.0 | 0e+00 | 37/44 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.297×** | -17.6 | 0e+00 | 38/46 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.432×** | -17.3 | 0e+00 | 35/42 (SHP-77, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.346×** | -15.4 | 0e+00 | 35/39 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.410×** | -13.0 | 1e-36 | 28/42 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.221×** | -11.5 | 1e-28 | 34/45 (A-172, A498, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.458×** | -11.3 | 6e-28 | 36/46 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.466×** | -11.1 | 8e-27 | 31/44 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.459×** | -10.9 | 7e-26 | 27/39 (A-172, J82, …) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.511×** | -9.4 | 3e-19 | 27/40 (C32, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.299×** | -9.2 | 2e-18 | 29/41 (SNU-423, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.538×** | -9.0 | 9e-18 | 26/44 (NCI-H2030, SHP-77, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.565×** | -8.3 | 4e-15 | 26/46 (NCI-H1792, AsPC-1, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.719×** | -6.8 | 5e-10 | 26/47 (HS-578T, BT-474, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.640×** | -6.5 | 3e-09 | 24/45 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.641×** | -6.1 | 4e-08 | 22/44 (SW1417, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.28 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8707. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.3 | 0 | 10 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0549× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.0837× (z -16.2) |
| [[HOP62 (line)]] | alt | 13.0 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -17.6) |
| [[LS 180 (line)]] | wt | 11.4 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -17.4) |
| [[KATO III (line)]] | alt | 9.84 | 0 | 6 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0732× (z -14.3) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.263× (z -10.8) |
| [[A-172 (line)]] | wt | 15.1 | 0 | 5 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0608× (z -18.3) |
| [[LoVo (line)]] | wt | 12.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -12.8) |
| [[AsPC-1 (line)]] | alt | 16.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.118× (z -15.5) |
| [[Hs 766T (line)]] | wt | 6.15 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0636× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.153× (z -9.9) |
| [[NCI-H1792 (line)]] | alt | 7.68 | 0 | 4 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0180× (z -16.8) |
| [[SW1417 (line)]] | alt | 14.9 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 10.6 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.150× (z -13.3) |
| [[A498 (line)]] | wt | 6.28 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.194× (z -9.1) |
| [[A549 (line)]] | wt | 11.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -14.7) |
| [[C32 (line)]] | wt | 6.45 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0771× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 7.68 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -13.0) |
| [[HepG2_C3A (line)]] | wt | 20.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -11.8) |
| [[HS-578T (line)]] | alt | 7.58 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0559× (z -12.4) |
| [[HT-29 (line)]] | alt | 4.15 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0669× (z -9.9) |
| [[J82 (line)]] | alt | 8.39 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0912× (z -11.7) |
| [[MIA PaCa-2 (line)]] | alt | 5.35 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.186× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 6.95 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.102× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 12.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -14.3) |
| [[PANC-1 (line)]] | alt | 4.29 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -10.2) |
| [[SNU-423 (line)]] | alt | 7.94 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0787× (z -17.3) |
| [[A-427 (line)]] | wt | 6.43 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.122× (z -8.8) |
| [[BT-474 (line)]] | alt | 8.18 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 5.30 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.142× (z -8.5) |
| [[NCI-H23 (line)]] | alt | 5.48 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0704× (z -9.6) |
| [[NCI-H460 (line)]] | wt | 2.86 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0579× (z -11.5) |
| [[SHP-77 (line)]] | alt | 11.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0955× (z -14.3) |
| [[SK-MEL-2 (line)]] | alt | 9.46 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.129× (z -8.5) ⚠ toxic; cell-cycle shift, explains ~34% of this change |
| [[SNU-1 (line)]] | wt | 6.77 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0502× (z -8.9) |
| [[AN3 CA (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.44 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.53 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.39 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.51 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.13 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.58 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.16 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.37 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8707), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*53 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAST3]] | +0.69 | +0.58 / +0.37 | both halves | 8e-05 |  |
| [[ABTB1]] | +0.67 | +0.67 / +0.50 | both halves | 1e-05 |  |
| [[ETNK2]] | +0.66 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[TNK2]] | +0.66 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[STX7]] | +0.65 | +0.56 / +0.42 | both halves | 4e-05 |  |
| [[FKBP1B]] | +0.64 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[GRAMD4]] | +0.63 | +0.56 / +0.43 | both halves | 4e-05 |  |
| [[PBX4]] | +0.63 | +0.47 / +0.45 | both halves | 3e-05 |  |
| [[CRLF3]] | +0.63 | +0.55 / +0.45 | both halves | 3e-05 |  |
| [[FCHSD1]] | +0.63 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[CEP131]] | +0.63 | +0.46 / +0.29 | both halves | 3e-04 |  |
| [[SLC27A1]] | +0.62 | +0.53 / +0.23 | both halves | 5e-04 |  |

## Genes that move opposite

*47 of its nearest partners move opposite, 17 of them with an alert (⚠; 17 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF827]] | -0.65 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[MMADHC-DT]] | -0.64 | -0.56 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[CRPPA]] | -0.64 | -0.52 / -0.24 | both halves | 4e-04 |  |
| [[ZBED5]] | -0.63 | -0.58 / -0.29 | both halves | 3e-04 |  |
| [[PATL2]] | -0.63 | -0.60 / -0.28 | both halves | 3e-04 |  |
| [[ZFP91]] | -0.63 | -0.58 / -0.34 | both halves | 1e-04 |  |
| [[NAALADL2]] | -0.62 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[ATXN7]] | -0.62 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[CCDC90B-AS1]] | -0.62 | -0.56 / -0.18 | ⚠ one half (not replicated) | 9e-04 |  |
| [[MCPH1]] | -0.62 | -0.49 / -0.28 | both halves | 3e-04 |  |
| [[MZF1-AS1]] | -0.62 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[PBLD]] | -0.62 | -0.54 / -0.13 | ⚠ one half (not replicated) | 0.002 |  |
| [[TTC6]] | -0.62 | -0.56 / -0.34 | both halves | 1e-04 |  |
| [[LINC02068]] | -0.62 | -0.56 / -0.38 | both halves | 6e-05 |  |
| [[ZNF462]] | -0.61 | -0.58 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ETNK2]] | B | ETNK2 activity raises HDAC11's level | lines that do not express ETNK2 (11) vs lines expressing it (39) | 1.46× lower at baseline in the lines without ETNK2 | 0.014 | ⚠ within organs, on part of the lines; also absent: DLK2, FBXL2, DUSP15; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises HDAC11's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.8% of all compounds | 0.028 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FKBP1B]] | B | FKBP1B activity raises HDAC11's level | lines that do not express FKBP1B (14) vs lines expressing it (36) | 1.36× lower at baseline in the lines without FKBP1B | 0.036 | ⚠ within organs, on part of the lines; also absent: ENSG00000234139, IGDCC4, C19orf18; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity lowers HDAC11's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[S100A14]] | B | S100A14 activity raises HDAC11's level | lines that do not express S100A14 (33) vs lines expressing it (17) | 1.44× lower at baseline in the lines without S100A14 | 0.072 | ⚠ within organs, on part of the lines; also absent: PRSS8, RAB25, TMPRSS4 |
| [[SLC45A4]] | B | SLC45A4 activity raises HDAC11's level | lines that do not express SLC45A4 (5) vs lines expressing it (45) | 1.15× lower at baseline in the lines without SLC45A4 | 0.084 | ⚠ within organs, on part of the lines; also absent: ARHGEF3; maybe low, not absent |
| [[PTK2B]] | B | PTK2B activity raises HDAC11's level | lines that do not express PTK2B (10) vs lines expressing it (40) | 1.47× lower at baseline in the lines without PTK2B | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[PBX4]] | C | PBX4 activity raises HDAC11's level | lines that do not express PBX4 (3) vs lines expressing it (47) | 2.30× lower at baseline in the lines without PBX4 | 0.022 | ⚠ few lines (3 vs 47); across organs; also absent: BMP8B, KIAA1522, CYB561 |

### Downstream of this gene

*599 arrows, 599 of them with an alert ⚠; grade A 0, B 599, C 0. Shown: the 12 strongest; 587 more arrows (587 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC23]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], HDAC11 activity raises CDC23's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[CMIP]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], HDAC11 activity lowers CMIP's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[CROCCP3]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], HDAC11 activity lowers CROCCP3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[CYB561]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], HDAC11 activity raises CYB561's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[DNAJC2]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], HDAC11 activity raises DNAJC2's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[ENSG00000288899]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], HDAC11 activity raises ENSG00000288899's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[FAM78B]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], HDAC11 activity lowers FAM78B's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[FBXW9]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], HDAC11 activity raises FBXW9's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[FMN1]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], HDAC11 activity lowers FMN1's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[LRRC51]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], HDAC11 activity raises LRRC51's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[MRPS7]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], HDAC11 activity raises MRPS7's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[NCBP3]] | B | [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], HDAC11 activity raises NCBP3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.6% of all compounds | 0.028 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

## Where it sits

- **Module**: [[Module 159]] — High laminar flow shear stress activates signaling by PIEZO1 and PECAM1:CDH5:KDR in endothelial cells; 27 genes; every member is in the + arm (projection on the module's main direction 0.664). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.43; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (3.7, 3.7); signed map (-39.8, -5.5). **Vector** length 80.4, 15.8% of its response variance represented; |z| ≥ 3 in 1,176 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +4.8 | +3.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +4.8 | +4.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.1 | +3.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.8 | +1.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +1.7 | -3.4 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +1.5 | -0.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.4 | +0.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.3 | +3.1 |
| fall | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.9 | -6.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -17.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -10.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.3 | -15.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.0 | -9.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.5 | -4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -9.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | -0.5 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.9 | -5.3 |

## What is on record

|  |  |
|---|---|
| Name | histone deacetylase 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p25.1 — chr3:13,479,724-13,506,424 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Histone deacetylases, class IV |
| Hallmark sets | WNT_BETA_CATENIN_SIGNALING |
| Reactome | 14 pathways, smallest: Notch-HLH transcription pathway; NOTCH signaling regulates gene expression in endothelial stalk cells; NOTCH1 Intracellular Domain Regulates Transcription |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96DB2](https://www.uniprot.org/uniprotkb/Q96DB2) (Histone deacetylase 11):

> Responsible for the deacetylation of lysine residues on the N-terminal part of the core histones (H2A, H2B, H3 and H4). Histone deacetylation gives a tag for epigenetic repression and plays an important role in transcriptional regulation, cell cycle progression and developmental events. Histone deacetylases act via the formation of large multiprotein complexes.

**Summary**, from NCBI Gene [79885](https://www.ncbi.nlm.nih.gov/gene/79885):

> This gene encodes a class IV histone deacetylase. The encoded protein is localized to the nucleus and may be involved in regulating the expression of interleukin 10. Alternative splicing results in multiple transcript variants.[provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:19086](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19086) · Entrez [79885](https://www.ncbi.nlm.nih.gov/gene/79885) · UniProt [Q96DB2](https://www.uniprot.org/uniprotkb/Q96DB2) · Ensembl [ENSG00000163517](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163517)

## Data

Gene col 8707: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8707); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8707, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8707]; `tensor/DDL_lfc|DDL_z.npy` [8707]; `embed/gene_vectors.npy` [8707]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8707 or target_col == 8707). Every well: [[HDAC11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HDAC11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
