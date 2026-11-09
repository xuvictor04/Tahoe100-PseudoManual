---
symbol: "SNRPN"
type: "gene"
col: 4919
ensembl_id: "ENSG00000128739"
name: "small nuclear ribonucleoprotein polypeptide N"
location: "15q11.2"
module: 45
arm: "+"
pooled_cpm: 38.43
n_lines_expressing: 36
n_dd_up: 5
n_dd_down: 14
n_dd_up_clean: 4
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 0
direction_downstream: 13
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# SNRPN

*small nuclear ribonucleoprotein polypeptide N* — 15q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.23× (z +8.4, q 2e-14, up in 19 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.515× (z -26.9, q 0e+00, down in 28 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BEX3]] (+0.62, fdr 1e-05), [[SCPEP1]] (+0.62, fdr 1e-05), [[LMBRD1]] (+0.61, fdr 7e-06); moves opposite to [[GJC1]] (-0.52, fdr 1e-05), [[REXO1]] (-0.51, fdr 2e-05), [[SMIM12]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 13 go from it, the strongest it → cells under [[Bortezomib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4919.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +8.4 | 2e-14 | 19/34 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.34×** | +8.4 | 2e-14 | 19/34 (CFPAC-1, PANC-1, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.23×** | +8.3 | 2e-14 | 18/34 (A-427, J82, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.19× | +5.0 | 7e-05 | 11/34 (C-33 A, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.05× | +4.9 | 1e-04 | 2/34 (MIA PaCa-2, NCI-H23) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +4.8 | 2e-04 | 9/34 (NCI-H1792, NCI-H23, …) | top dose only |  |
| [[Ixazomib (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.020 | 5/34 (CFPAC-1, PANC-1, …) | top dose only | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.020 | 5/32 (A-427, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[LJI308 (drug)]] 0.05 µM |  | 1.13× | +3.4 | 0.045 | 5/34 (hTERT-HPNE, HepG2/C3A, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 0.5 µM |  | 1.18× | +3.4 | 0.045 | 4/34 (A549, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cysteamine (hydrochloride) (drug)]] 0.5 µM |  | 1.12× | +3.2 | 0.077 | 1/34 (MIA PaCa-2) | inconsistent across doses | position effect removed |
| [[Ipatasertib (drug)]] 5 µM |  | 1.22× | +3.0 | 0.12 | 3/34 (SW 900, C32, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 36 in all, 16 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4919.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.515×** | -26.9 | 0e+00 | 28/34 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.434×** | -23.9 | 0e+00 | 28/34 (NCI-H2347, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.470×** | -20.8 | 0e+00 | 28/34 (NCI-H2347, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.565×** | -16.4 | 0e+00 | 26/34 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.671×** | -11.5 | 3e-28 | 25/34 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.705×** | -10.0 | 1e-21 | 21/34 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.806×** | -8.7 | 2e-16 | 16/34 (SW 900, NCI-H1792, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.741×** | -8.6 | 6e-16 | 20/33 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.749×** | -8.3 | 8e-15 | 19/34 (SW 900, SHP-77, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.751×** | -8.2 | 1e-14 | 20/34 (NCI-H2347, SW 900, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.769×** | -7.5 | 3e-12 | 18/34 (NCI-H2347, Panc 03.27, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.778×** | -7.2 | 3e-11 | 17/34 (SW 900, Panc 03.27, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.779×** | -7.2 | 4e-11 | 17/34 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.826×** | -5.3 | 5e-06 | 12/33 (SNU-423, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 0.837× | -5.1 | 1e-05 | 11/33 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.900× | -4.3 | 6e-04 | 8/34 (SW 900, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 0.862× | -4.3 | 6e-04 | 9/33 (RPMI-7951, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Belumosudil (drug)]] 5 µM |  | 0.860× | -4.1 | 9e-04 | 11/34 (MIA PaCa-2, NCI-H661, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | 0.876× | -3.8 | 0.004 | 10/33 (NCI-H460, H4, …) | all doses, stronger at high dose |  |
| [[vincristine (drug)]] 0.05 µM |  | 0.884× | -3.4 | 0.018 | 4/34 (MIA PaCa-2, SW 900, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | 0.889× | -3.2 | 0.030 | 7/33 (MIA PaCa-2, SK-MEL-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.892× | -3.0 | 0.049 | 8/33 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4919. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 66.6 | 0 | 10 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -16.6) |
| [[NCI-H2347 (line)]] | alt | 89.8 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.441× (z -17.4) |
| [[SW 900 (line)]] | alt | 144 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -14.0) |
| [[Panc 03.27 (line)]] | alt | 55.4 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.322× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.387× (z -10.2) |
| [[PANC-1 (line)]] | alt | 49.8 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.411× (z -19.2) |
| [[C32 (line)]] | wt | 54.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.333× (z -15.5) |
| [[NCI-H1792 (line)]] | alt | 48.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.324× (z -11.6) |
| [[SNU-423 (line)]] | alt | 53.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -19.8) |
| [[A549 (line)]] | wt | 36.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.355× (z -9.4) |
| [[CFPAC-1 (line)]] | alt | 57.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -15.1) |
| [[HOP62 (line)]] | alt | 33.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -11.9) |
| [[NCI-H1573 (line)]] | alt | 36.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -16.1) |
| [[NCI-H2030 (line)]] | alt | 37.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.490× (z -10.7) |
| [[SK-MEL-2 (line)]] | alt | 51.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -15.7) |
| [[AN3 CA (line)]] | alt | 64.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.199× (z -8.6) |
| [[C-33 A (line)]] | alt | 55.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 100 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.146× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 89.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.487× (z -9.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HepG2_C3A (line)]] | wt | 52.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.462× (z -8.8) |
| [[HS-578T (line)]] | alt | 28.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -11.2) |
| [[J82 (line)]] | alt | 32.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.501× (z -9.2) |
| [[LOX-IMVI (line)]] | wt | 49.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.366× (z -9.5) |
| [[RPMI-7951 (line)]] | alt | 40.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.318× (z -9.4) |
| [[SW 1271 (line)]] | alt | 104 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.133× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 93.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.02 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.86 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.22 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 36.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 77.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.59 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.02 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.27 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.25 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4919), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BEX3]] | +0.62 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[SCPEP1]] | +0.62 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[LMBRD1]] | +0.61 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ASAH1]] | +0.59 | +0.50 / +0.63 | both halves | 1e-05 |  |
| [[ZC4H2]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[SLC22A17]] | +0.58 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[TRAPPC2]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[GNPDA2]] | +0.57 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[FRG1CP]] | +0.56 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[FBXO44]] | +0.56 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[CMBL]] | +0.55 | +0.42 / +0.54 | both halves | 4e-05 |  |
| [[CROT]] | +0.55 | +0.45 / +0.57 | both halves | 3e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GJC1]] | -0.52 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[REXO1]] | -0.51 | -0.51 / -0.48 | both halves | 2e-05 |  |
| [[SMIM12]] | -0.50 | -0.50 / -0.43 | both halves | 3e-05 |  |
| [[SSUH2]] | -0.49 | -0.49 / -0.45 | both halves | 3e-05 |  |
| [[EPOP]] | -0.49 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[PIWIL4]] | -0.48 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[ETS1]] | -0.48 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[OXTR]] | -0.48 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[CRK]] | -0.48 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[SPG11]] | -0.47 | -0.51 / -0.38 | both halves | 7e-05 |  |
| [[DGKH]] | -0.47 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[ABR]] | -0.47 | -0.41 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 0, C 13. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Bortezomib (drug)]] 5 µM | C | [[ENSG00000214265]], [[SNHG14]], SNRPN activity lowers the cells' numbers under Bortezomib 5 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.69× the cells of the other lines | 0.024 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| cells under [[Erlotinib (drug)]] 0.05 µM | C | [[ENSG00000214265]], [[SNHG14]], SNRPN activity lowers the cells' numbers under Erlotinib 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.24× the cells of the other lines | 0.029 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| cells under [[Pimozide (drug)]] 0.05 µM | C | [[ENSG00000214265]], [[SNHG14]], SNRPN activity lowers the cells' numbers under Pimozide 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.16× the cells of the other lines | 0.036 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| cells under [[Folic acid (drug)]] 5 µM | C | [[ENSG00000214265]], [[SNHG14]], SNRPN activity lowers the cells' numbers under Folic acid 5 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.10× the cells of the other lines | 0.049 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| cells under [[Dihydroartemisinin (drug)]] 5 µM | C | [[ENSG00000214265]], [[SNHG14]], SNRPN activity lowers the cells' numbers under Dihydroartemisinin 5 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.27× the cells of the other lines | 0.051 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| cells under [[Ixazomib citrate (drug)]] 5 µM | C | [[ENSG00000214265]], [[SNHG14]], SNRPN activity lowers the cells' numbers under Ixazomib citrate 5 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.40× the cells of the other lines | 0.054 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| cells under [[Benproperine (phosphate) (drug)]] 0.05 µM | C | [[ENSG00000214265]], [[SNHG14]], SNRPN activity lowers the cells' numbers under Benproperine (phosphate) 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.15× the cells of the other lines | 0.066 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| cells under [[Mifepristone (drug)]] 0.5 µM | C | [[ENSG00000214265]], [[SNHG14]], SNRPN activity raises the cells' numbers under Mifepristone 0.5 µM (protects the cells) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 0.87× the cells of the other lines | 0.075 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| cells under [[Fenofibrate (drug)]] 0.05 µM | C | [[ENSG00000214265]], [[SNHG14]], SNRPN activity lowers the cells' numbers under Fenofibrate 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.21× the cells of the other lines | 0.079 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| cells under [[Furosemide (drug)]] 0.5 µM | C | [[ENSG00000214265]], [[SNHG14]], SNRPN activity lowers the cells' numbers under Furosemide 0.5 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.14× the cells of the other lines | 0.082 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| cells under [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM | C | [[ENSG00000214265]], [[SNHG14]], SNRPN activity lowers the cells' numbers under Trametinib (DMSO_TF solvate) 0.05 µM (makes them more sensitive) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 1.19× the cells of the other lines | 0.084 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |
| cells under [[Apalutamide (drug)]] 0.5 µM | C | [[ENSG00000214265]], [[SNHG14]], SNRPN activity raises the cells' numbers under Apalutamide 0.5 µM (protects the cells) | lines that do not express ENSG00000214265, SNHG14, SNRPN (14) vs lines expressing them (34) | the lines without ENSG00000214265, SNHG14, SNRPN: 0.86× the cells of the other lines | 0.089 | ⚠ tissue-confounded; across organs; co-occurs with APC; also absent: RNF150, CHST10, ENSG00000268163; co-absent genes |

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.647). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-0.3, -9.1); signed map (-30.5, -7.1). **Vector** length 84.3, 19.6% of its response variance represented; |z| ≥ 3 in 800 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.7 | +8.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +8.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +3.3 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.1 | +8.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +2.8 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.3 | +4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | -0.6 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.0 | -23.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -16.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -5.0 | -26.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.8 | -20.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.9 | -11.5 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.7 | -8.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | -4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.1 | -5.1 |

## What is on record

|  |  |
|---|---|
| Name | small nuclear ribonucleoprotein polypeptide N |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q11.2 — chr15:24,823,637-24,978,723 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SMN, SM-D, HCERN3, SNRNP-N, SNURF-SNRPN, RT-LI; previously PWCR |
| Gene groups (HGNC) | Sm spliceosomal proteins |
| Reactome | 13 pathways, smallest: CHD1 and CHD2 subfamily; CHD chromatin remodelers; mRNA Polyadenylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P63162](https://www.uniprot.org/uniprotkb/P63162) (Small nuclear ribonucleoprotein-associated protein N):

> May be involved in tissue-specific alternative RNA processing events.

**Summary**, from NCBI Gene [6638](https://www.ncbi.nlm.nih.gov/gene/6638):

> This gene is located within the Prader-Willi Syndrome critical region on chromosome 15 and is imprinted and expressed from the paternal allele. It encodes a component of the small nuclear ribonucleoprotein complex, which functions in pre-mRNA processing and may contribute to tissue-specific alternative splicing. Alternative promoter use and alternative splicing result in a multitude of transcript variants encoding the same protein. Transcript variants that initiate at the CpG island-associated …

**Accessions** — [HGNC:11164](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11164) · Entrez [6638](https://www.ncbi.nlm.nih.gov/gene/6638) · UniProt [P63162](https://www.uniprot.org/uniprotkb/P63162) · Ensembl [ENSG00000128739](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128739)

## Data

Gene col 4919: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4919); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4919, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4919]; `tensor/DDL_lfc|DDL_z.npy` [4919]; `embed/gene_vectors.npy` [4919]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4919 or target_col == 4919). Every well: [[SNRPN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SNRPN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
