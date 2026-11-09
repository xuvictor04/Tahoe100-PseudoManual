---
symbol: "ITPRIP"
type: "gene"
col: 7321
ensembl_id: "ENSG00000148841"
name: "inositol 1,4,5-trisphosphate receptor interacting protein"
location: "10q25.1"
module: 174
arm: "+"
pooled_cpm: 32.51
n_lines_expressing: 40
n_dd_up: 15
n_dd_down: 21
n_dd_up_clean: 10
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 10
direction_downstream: 23
tags: ["gene", "module/174"]
generated_by: "tahoemap"
---

# ITPRIP

*inositol 1,4,5-trisphosphate receptor interacting protein* — 10q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 6.75× (z +16.1, q 0e+00, up in 33 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.523× (z -15.1, q 0e+00, down in 32 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DUSP5]] (+0.59, fdr 1e-05), [[PHC2]] (+0.56, fdr 1e-05), [[GBA2]] (+0.56, fdr 2e-05); moves opposite to [[BBOX1-AS1]] (-0.45, fdr 1e-04), [[VBP1]] (-0.45, fdr 1e-04), [[KDM3B]] (-0.44, fdr 2e-04).
> It is in [[Module 174]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[SERPINE1]] → it (grade B ⚠); 23 go from it, the strongest it → [[OSBPL5]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7321.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.75×** | +16.1 | 0e+00 | 33/39 (LOX-IMVI, NCI-H460, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.16×** | +9.7 | 6e-20 | 23/36 (hTERT-HPNE, LOX-IMVI, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +6.4 | 4e-08 | 13/38 (RKO, SW480, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.38×** | +5.2 | 4e-05 | 19/34 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.34×** | +4.8 | 2e-04 | 15/38 (Panc 03.27, Hs 766T, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.44×** | +4.3 | 0.002 | 10/38 (A-172, SK-MEL-2, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.29×** | +4.3 | 0.002 | 13/38 (KATO III, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.29×** | +4.2 | 0.002 | 22/38 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **1.27×** | +4.0 | 0.004 | 15/37 (A-172, RPMI-7951, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.40×** | +4.0 | 0.004 | 8/33 (SW 900, Hs 766T, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +3.9 | 0.004 | 13/38 (A-172, SW480, …) | top dose only |  |
| [[PH-797804 (drug)]] 0.5 µM |  | **1.37×** | +3.7 | 0.011 | 8/36 (A-172, SK-MEL-2, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.22×** | +3.3 | 0.039 | 10/37 (KATO III, LS 180, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.22×** | +3.3 | 0.044 | 7/38 (LS 180, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.065 | 4/38 (SW 900, A-172, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7321.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.523×** | -15.1 | 0e+00 | 32/37 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.575×** | -9.1 | 2e-17 | 24/37 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.559×** | -8.9 | 1e-16 | 22/38 (NCI-H23, NCI-H460, …) | all doses, flat | position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.673×** | -8.4 | 5e-15 | 23/38 (NCI-H23, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.614×** | -8.0 | 1e-13 | 22/39 (NCI-H23, HOP62, …) | all doses, flat | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.672×** | -7.1 | 2e-10 | 22/38 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.644×** | -7.0 | 3e-10 | 20/37 (NCI-H23, HOP62, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.659×** | -6.6 | 3e-09 | 20/37 (NCI-H23, HOP62, …) | all doses, flat | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.663×** | -6.5 | 5e-09 | 20/23 (MIA PaCa-2, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.673×** | -6.3 | 2e-08 | 18/37 (PANC-1, A498, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 5 µM |  | **0.721×** | -5.9 | 2e-07 | 16/38 (NCI-H23, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~11% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.749×** | -5.8 | 4e-07 | 17/38 (NCI-H23, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.910× | -5.8 | 4e-07 | 6/39 (NCI-H23, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.781×** | -5.7 | 4e-07 | 17/38 (HOP62, NCI-H23, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.767×** | -4.2 | 0.001 | 17/37 (LOX-IMVI, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[NG25 (drug)]] 5 µM |  | **0.611×** | -4.2 | 0.001 | 13/35 (HepG2/C3A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~1% here); noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.768×** | -4.1 | 0.001 | 13/37 (NCI-H23, NCI-H460, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7321. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 121 | 2 | 10 (7 ⚠) | [[TAK-901 (drug)]] 5 µM 15.3× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -17.7) |
| [[NCI-H23 (line)]] | alt | 30.7 | 0 | 12 (2 ⚠) | — | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.0982× (z -14.0) |
| [[NCI-H460 (line)]] | wt | 119 | 1 | 10 (5 ⚠) | [[TAK-901 (drug)]] 5 µM 8.22× (z +12.1) | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -27.6) |
| [[A-172 (line)]] | wt | 40.2 | 7 (3 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 36.1× (z +10.9) | [[Dinaciclib (drug)]] 5 µM 0.222× (z -8.5) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 44.0 | 2 (1 ⚠) | 6 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 13.5× (z +9.4) | [[Adagrasib (drug)]] 0.05 µM 0.637× (z -11.2) ⚠ position not correctable · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.252× (z -9.3) |
| [[hTERT-HPNE (line)]] | wt | 103 | 4 (2 ⚠) | 2 (2 ⚠) | [[PH-797804 (drug)]] 5 µM 20.9× (z +12.2) | [[Ixazomib citrate (drug)]] 5 µM 0.230× (z -11.5) ⚠ cell-cycle shift, explains ~70% of this change |
| [[A498 (line)]] | wt | 47.1 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -17.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.395× (z -12.9) |
| [[PANC-1 (line)]] | alt | 64.6 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -18.3) |
| [[A549 (line)]] | wt | 40.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.237× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.451× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 27.3 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 12.7× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.0948× (z -15.8) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 57.2 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 7.46× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.337× (z -9.4) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 51.4 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0963× (z -13.6) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.246× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 29.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -10.5) |
| [[HS-578T (line)]] | alt | 49.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 12.4× (z +11.0) | — |
| [[NCI-H2030 (line)]] | alt | 20.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -16.5) |
| [[RPMI-7951 (line)]] | alt | 76.6 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 19.2× (z +10.6) | — |
| [[AsPC-1 (line)]] | alt | 8.83 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.209× (z -9.5) ⚠ cell-cycle shift, explains ~12% of this change |
| [[COLO 205 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.259× (z -8.6) ⚠ cell-cycle shift, explains ~12% of this change |
| [[Hs 766T (line)]] | wt | 39.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.80× (z +9.0) | — |
| [[KATO III (line)]] | alt | 8.83 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -10.1) |
| [[RKO (line)]] | wt | 38.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 19.9× (z +11.4) | — |
| [[SW48 (line)]] | wt | 19.8 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0818× (z -9.1) |
| [[A-427 (line)]] | wt | 7.19 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.72 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.94 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 6.36 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.07 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.79 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.61 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.57 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.56 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 11.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7321), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DUSP5]] | +0.59 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[PHC2]] | +0.56 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[GBA2]] | +0.56 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[MCTP1]] | +0.55 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[SLC45A1]] | +0.54 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[GLRX]] | +0.53 | +0.48 / +0.53 | both halves | 2e-05 |  |
| [[PTPN12]] | +0.53 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[SPRY4]] | +0.53 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[RGS17]] | +0.53 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[ARHGEF18]] | +0.52 | +0.52 / +0.46 | both halves | 2e-05 |  |
| [[SH3RF3]] | +0.52 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[ANKRD13D]] | +0.51 | +0.54 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BBOX1-AS1]] | -0.45 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[VBP1]] | -0.45 | -0.39 / -0.35 | both halves | 1e-04 |  |
| [[KDM3B]] | -0.44 | -0.45 / -0.29 | both halves | 2e-04 |  |
| [[UBE2A]] | -0.44 | -0.54 / -0.25 | both halves | 4e-04 |  |
| [[TCTA]] | -0.44 | -0.50 / -0.31 | both halves | 2e-04 |  |
| [[MATN2]] | -0.43 | -0.47 / -0.31 | both halves | 2e-04 |  |
| [[UBXN2A]] | -0.43 | -0.49 / -0.31 | both halves | 2e-04 |  |
| [[HACD2]] | -0.41 | -0.44 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINE1]] | B | SERPINE1 activity raises ITPRIP's level | lines that do not express SERPINE1 (27) vs lines expressing it (23) | 3.14× lower at baseline in the lines without SERPINE1 | 0.005 | ⚠ within organs, on part of the lines; also absent: FRMD4A, SIRLNT, ENSG00000230615 |
| [[HS3ST3A1]] | B | HS3ST3A1 activity raises ITPRIP's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 2.61× lower at baseline in the lines without HS3ST3A1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1 |
| [[MT2A]] | B | MT2A activity raises ITPRIP's level | lines that do not express MT2A (9) vs lines expressing it (41) | 2.84× lower at baseline in the lines without MT2A | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000289942, TRAF1, MT1X |
| [[TMEM156]] | B | TMEM156 activity raises ITPRIP's level | lines that do not express TMEM156 (26) vs lines expressing it (24) | 1.96× lower at baseline in the lines without TMEM156 | 0.029 | ⚠ within organs, on part of the lines; also absent: BCL2A1, IL31RA, LHFPL4 |
| [[NPAS2]] | B | NPAS2 activity raises ITPRIP's level | lines that do not express NPAS2 (7) vs lines expressing it (43) | 2.40× lower at baseline in the lines without NPAS2 | 0.030 | ⚠ within organs, on part of the lines |
| [[STC1]] | B | STC1 activity raises ITPRIP's level | lines that do not express STC1 (24) vs lines expressing it (26) | 2.43× lower at baseline in the lines without STC1 | 0.033 | ⚠ within organs, on part of the lines; also absent: ENSG00000253891, MSC-AS1, CLMP |
| [[JCAD]] | B | JCAD activity raises ITPRIP's level | lines that do not express JCAD (20) vs lines expressing it (30) | 1.75× lower at baseline in the lines without JCAD | 0.046 | ⚠ within organs, on part of the lines; also absent: ANKRD33B, FAT4, EFEMP1 |
| [[DUSP5]] | B | DUSP5 activity raises ITPRIP's level | lines that do not express DUSP5 (7) vs lines expressing it (43) | 2.79× lower at baseline in the lines without DUSP5 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000236213, CA13, SLC2A1; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises ITPRIP's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[DAW1]] | B | DAW1 activity raises ITPRIP's level | lines that do not express DAW1 (34) vs lines expressing it (16) | 1.72× lower at baseline in the lines without DAW1 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NEFL, OLR1, ENSG00000255227 |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 23, C 0. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OSBPL5]] | B | ITPRIP activity raises OSBPL5's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 1.67× lower at baseline in the lines without ITPRIP | 0.009 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |
| [[NPAS2]] | B | ITPRIP activity raises NPAS2's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 2.99× lower at baseline in the lines without ITPRIP | 0.015 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |
| [[FMNL2]] | B | ITPRIP activity raises FMNL2's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 2.38× lower at baseline in the lines without ITPRIP | 0.020 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |
| [[HACD2]] | B | ITPRIP activity lowers HACD2's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 1.55× higher at baseline in the lines without ITPRIP | 0.026 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |
| [[PHC2]] | B | ITPRIP activity raises PHC2's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 1.84× lower at baseline in the lines without ITPRIP | 0.028 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |
| [[MT2A]] | B | ITPRIP activity raises MT2A's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 2.63× lower at baseline in the lines without ITPRIP | 0.030 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |
| [[ANGPTL4]] | B | ITPRIP activity raises ANGPTL4's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 2.93× lower at baseline in the lines without ITPRIP | 0.032 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |
| [[GSTO1]] | B | ITPRIP activity raises GSTO1's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 1.95× lower at baseline in the lines without ITPRIP | 0.034 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |
| [[NBPF9]] | B | ITPRIP activity raises NBPF9's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 1.59× lower at baseline in the lines without ITPRIP | 0.040 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |
| [[SLC25A37]] | B | ITPRIP activity raises SLC25A37's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 1.99× lower at baseline in the lines without ITPRIP | 0.043 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |
| [[PHC2]] | B | ITPRIP activity strengthens PHC2's drug response | lines that do not express ITPRIP (10) vs lines expressing it (40) | the lines without ITPRIP respond 0.54× as strongly (z diff +2.46); strongest at Dinaciclib 5 µM: 0.82x vs 0.45x (z diff +3.4) | 0.049 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent; artifact flags |
| [[SERPINE1]] | B | ITPRIP activity raises SERPINE1's level | lines that do not express ITPRIP (10) vs lines expressing it (40) | 5.62× lower at baseline in the lines without ITPRIP | 0.050 | ⚠ within organs, on part of the lines; also absent: C13orf46; maybe low, not absent |

## Where it sits

- **Module**: [[Module 174]]; 23 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (42.7, 6.6); signed map (7.9, 49.5). **Vector** length 109, 26.8% of its response variance represented; |z| ≥ 3 in 1,033 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +4.8 | +16.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.4 | +4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +6.4 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~15% of this change | +3.6 | +3.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +3.1 | +4.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.9 | +9.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.6 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +3.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +4.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -8.2 | -15.1 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.2 | -5.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.2 | -8.4 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~6% of this change | -4.0 | -3.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.0 | -8.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -3.9 | -6.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.9 | -7.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.8 | -8.0 |

## What is on record

|  |  |
|---|---|
| Name | inositol 1,4,5-trisphosphate receptor interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.1 — chr10:104,309,698-104,338,465 (-) |
| Ensembl biotype | protein_coding |
| Also known as | bA127L20.2, DANGER, D1A; previously KIAA1754 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWB1](https://www.uniprot.org/uniprotkb/Q8IWB1) (Inositol 1,4,5-trisphosphate receptor-interacting protein):

> Enhances Ca(2+)-mediated inhibition of inositol 1,4,5-triphosphate receptor (ITPR) Ca(2+) release.

**Summary**, from NCBI Gene [85450](https://www.ncbi.nlm.nih.gov/gene/85450):

> This gene encodes a membrane-associated protein that binds the inositol 1,4,5-trisphosphate receptor (ITPR). The encoded protein enhances the sensitivity of ITPR to intracellular calcium signaling. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:29370](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29370) · Entrez [85450](https://www.ncbi.nlm.nih.gov/gene/85450) · UniProt [Q8IWB1](https://www.uniprot.org/uniprotkb/Q8IWB1) · Ensembl [ENSG00000148841](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148841)

## Data

Gene col 7321: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7321); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7321, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7321]; `tensor/DDL_lfc|DDL_z.npy` [7321]; `embed/gene_vectors.npy` [7321]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7321 or target_col == 7321). Every well: [[ITPRIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITPRIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
