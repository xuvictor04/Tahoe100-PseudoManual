---
symbol: "CCDC88C"
type: "gene"
col: 291
ensembl_id: "ENSG00000015133"
name: "coiled-coil and HOOK domain protein 88C"
location: "14q32.11-q32.12"
module: 18
arm: "+"
pooled_cpm: 31.63
n_lines_expressing: 42
n_dd_up: 6
n_dd_down: 11
n_dd_up_clean: 3
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 8
direction_downstream: 3
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# CCDC88C

*coiled-coil and HOOK domain protein 88C* — 14q32.11-q32.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[EX229 (drug)]] 5 µM: 1.57× (z +5.8, q 3e-06, up in 14 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.535× (z -22.0, q 0e+00, down in 32 of 40 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PPARGC1B]] (+0.70, fdr 7e-06), [[TMEM201]] (+0.69, fdr 1e-05), [[FXN]] (+0.68, fdr 1e-05); moves opposite to [[ATP6V1G1]] (-0.59, fdr 1e-05), [[ZNF490]] (-0.59, fdr 3e-05), [[GTF2IRD2]] (-0.55, fdr 7e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[HDAC6]] → it (grade B ⚠); 3 go from it, the strongest it → [[PRXL2B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 7 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 291.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[EX229 (drug)]] 5 µM |  | **1.57×** | +5.8 | 3e-06 | 14/40 (NCI-H460, SW1417, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +5.5 | 1e-05 | 16/40 (NCI-H460, A549, …) | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **1.47×** | +5.0 | 1e-04 | 10/40 (NCI-H1792, NCI-H2347, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.22×** | +4.9 | 1e-04 | 17/40 (NCI-H1792, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.20×** | +4.5 | 7e-04 | 14/40 (COLO 205, NCI-H1573, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.19× | +4.2 | 0.002 | 6/40 (NCI-H1573, KATO III, …) | inconsistent across doses |  |
| [[Roxadustat (drug)]] 5 µM |  | 1.18× | +4.0 | 0.004 | 9/40 (PANC-1, A-172, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | 1.16× | +3.7 | 0.013 | 12/39 (LoVo, SW480, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | 1.11× | +3.7 | 0.015 | 7/40 (NCI-H1792, AsPC-1, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.021 | 6/38 (NCI-H460, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | 1.16× | +3.5 | 0.022 | 11/38 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.10× | +3.4 | 0.034 | 9/40 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~11% of this change | 1.14× | +3.1 | 0.072 | 7/36 (COLO 205, SHP-77, …) | inconsistent across doses | low cells (technical?) |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.14× | +3.0 | 0.10 | 2/40 (A-172, NCI-H1792) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 291.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.535×** | -22.0 | 0e+00 | 32/40 (MIA PaCa-2, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.544×** | -14.6 | 1e-45 | 26/40 (RKO, SW48, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.640×** | -11.1 | 2e-26 | 23/40 (SNU-1, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.707×** | -8.6 | 9e-16 | 24/40 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.721×** | -8.2 | 4e-14 | 20/39 (SW48, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | **0.831×** | -6.5 | 6e-09 | 20/40 (PANC-1, Panc 03.27, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.775×** | -6.0 | 2e-07 | 17/40 (PANC-1, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.857× | -5.4 | 4e-06 | 17/39 (PANC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 0.834× | -4.5 | 4e-04 | 14/40 (HOP62, SW48, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -4.5 | 4e-04 | 15/40 (KATO III, NCI-H2347, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.830×** | -4.5 | 4e-04 | 17/40 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | 0.838× | -4.4 | 5e-04 | 16/40 (HT-29, KATO III, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.721×** | -4.3 | 9e-04 | 13/40 (A-427, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | 0.846× | -4.2 | 0.001 | 15/40 (RKO, PANC-1, …) | top dose only |  |
| [[GSK1059615 (drug)]] 5 µM |  | **0.727×** | -4.1 | 0.001 | 8/39 (HEC-1-A, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | 0.903× | -3.6 | 0.010 | 9/40 (PANC-1, RKO, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.906× | -3.5 | 0.014 | 10/40 (PANC-1, SNU-1, …) | rises with dose |  |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.879× | -3.2 | 0.031 | 9/40 (LS 180, SW1417, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.885× | -3.0 | 0.053 | 7/40 (RKO, A549, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.17 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 291. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 67.1 | 0 | 9 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -18.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.245× (z -14.3) |
| [[RKO (line)]] | wt | 64.6 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0903× (z -23.3) |
| [[SNU-1 (line)]] | wt | 56.4 | 0 | 6 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.258× (z -13.8) |
| [[MIA PaCa-2 (line)]] | alt | 35.4 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -27.0) |
| [[SW48 (line)]] | wt | 88.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -15.7) |
| [[NCI-H460 (line)]] | wt | 21.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.253× (z -12.4) |
| [[Panc 03.27 (line)]] | alt | 71.5 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.552× (z -8.9) |
| [[A-172 (line)]] | wt | 11.0 | 0 | 2 | — | [[Doxycycline (monohydrate) (drug)]] 5 µM 0.155× (z -10.2) |
| [[A-427 (line)]] | wt | 33.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -13.5) |
| [[AN3 CA (line)]] | alt | 61.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.140× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 30.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.327× (z -10.0) |
| [[NCI-H2030 (line)]] | alt | 39.7 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -19.0) |
| [[NCI-H23 (line)]] | alt | 22.3 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -11.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.190× (z -11.2) |
| [[BT-474 (line)]] | alt | 68.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -12.1) |
| [[Hs 766T (line)]] | wt | 29.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.377× (z -10.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HT-29 (line)]] | alt | 33.4 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.237× (z -12.3) |
| [[J82 (line)]] | alt | 15.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.350× (z -10.0) |
| [[KATO III (line)]] | alt | 57.9 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.331× (z -11.1) |
| [[LoVo (line)]] | wt | 39.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 45.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.435× (z -10.1) |
| [[SW1417 (line)]] | alt | 24.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.430× (z -10.2) |
| [[SW480 (line)]] | alt | 45.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.623× (z -9.1) |
| [[A498 (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.58 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 54.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.43 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.47 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.67 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 47.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 47.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.84 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.81 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 6.36 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 291), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPARGC1B]] | +0.70 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[TMEM201]] | +0.69 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[FXN]] | +0.68 | +0.71 / +0.56 | both halves | 1e-05 |  |
| [[TCOF1]] | +0.67 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[ASIC1]] | +0.67 | +0.68 / +0.57 | both halves | 9e-06 |  |
| [[EBPL]] | +0.67 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[PPAT]] | +0.66 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[LRRC20]] | +0.66 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[WNK2]] | +0.66 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[MCOLN2]] | +0.66 | +0.57 / +0.58 | both halves | 9e-06 |  |
| [[TARBP1]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[AKAP1]] | +0.65 | +0.58 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V1G1]] | -0.59 | -0.59 / -0.49 | both halves | 1e-05 |  |
| [[ZNF490]] | -0.59 | -0.60 / -0.44 | both halves | 3e-05 |  |
| [[GTF2IRD2]] | -0.55 | -0.58 / -0.38 | both halves | 7e-05 |  |
| [[SYNRG]] | -0.55 | -0.65 / -0.39 | both halves | 6e-05 |  |
| [[FMO4]] | -0.55 | -0.48 / -0.35 | both halves | 1e-04 |  |
| [[ZNF189]] | -0.54 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[ZNF506]] | -0.54 | -0.57 / -0.33 | both halves | 1e-04 |  |
| [[TRAPPC6B]] | -0.53 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[USP34-DT]] | -0.53 | -0.54 / -0.40 | both halves | 5e-05 |  |
| [[CPEB4]] | -0.53 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[NFU1]] | -0.53 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[TOX4]] | -0.53 | -0.60 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 2, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC6]] | B | HDAC6 activity lowers CCDC88C's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[WNK2]] | B | WNK2 activity raises CCDC88C's level | lines that do not express WNK2 (16) vs lines expressing it (34) | 2.85× lower at baseline in the lines without WNK2 | 0.082 | ⚠ within organs, on part of the lines; also absent: NUP210, SLC27A2, CHDH |
| [[NUP210]] | C | NUP210 activity raises CCDC88C's level | lines that do not express NUP210 (13) vs lines expressing it (37) | 3.40× lower at baseline in the lines without NUP210 | 0.015 | ⚠ within organs, on part of the lines; also absent: PRR36, NEBL, FAM169A; co-absent with the target |
| [[ABCA3]] | C | ABCA3 activity raises CCDC88C's level | lines that do not express ABCA3 (9) vs lines expressing it (41) | 3.24× lower at baseline in the lines without ABCA3 | 0.022 | ⚠ within organs, on part of the lines; also absent: SLC37A1, CCDC88C, GRTP1; maybe low, not absent; co-absent with the target |
| [[GPD1L]] | C | GPD1L activity raises CCDC88C's level | lines that do not express GPD1L (4) vs lines expressing it (46) | 2.13× lower at baseline in the lines without GPD1L | 0.036 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ZBED3, DNMT3B, MYBL2; maybe low, not absent |
| [[JAG2]] | C | JAG2 activity raises CCDC88C's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 3.31× lower at baseline in the lines without JAG2 | 0.038 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent; co-absent with the target |
| [[RNFT2]] | C | RNFT2 activity raises CCDC88C's level | lines that do not express RNFT2 (3) vs lines expressing it (47) | 3.73× lower at baseline in the lines without RNFT2 | 0.084 | ⚠ few lines (3 vs 47); across organs; also absent: ARHGEF37, CSRP1-AS1, DBNDD1; maybe low, not absent |
| [[CHD7]] | C | CHD7 activity raises CCDC88C's level | lines that do not express CHD7 (3) vs lines expressing it (47) | 3.61× lower at baseline in the lines without CHD7 | 0.099 | ⚠ few lines (3 vs 47); across organs; also absent: GDPD1, ENSG00000287975, PIM2 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRXL2B]] | B | CCDC88C activity raises PRXL2B's level | lines that do not express CCDC88C (8) vs lines expressing it (42) | 1.71× lower at baseline in the lines without CCDC88C | 0.063 | ⚠ within organs, on part of the lines; also absent: SPTBN2, NUP210, NOXA1 |
| [[RNF125]] | B | CCDC88C activity raises RNF125's level | lines that do not express CCDC88C (8) vs lines expressing it (42) | 2.04× lower at baseline in the lines without CCDC88C | 0.076 | ⚠ within organs, on part of the lines; also absent: SPTBN2, NUP210, NOXA1 |
| [[AKAP1]] | B | CCDC88C activity raises AKAP1's level | lines that do not express CCDC88C (8) vs lines expressing it (42) | 1.90× lower at baseline in the lines without CCDC88C | 0.086 | ⚠ within organs, on part of the lines; also absent: SPTBN2, NUP210, NOXA1 |

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.660). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-9.4, -39.2); signed map (-7.0, -55.4). **Vector** length 98.3, 23.1% of its response variance represented; |z| ≥ 3 in 828 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.1 | +5.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | +4.0 | +4.9 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +3.7 | +3.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | +3.3 | +4.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.3 | +3.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.1 | +5.0 |
|  | [[EX229 (drug)]] 5 µM |  | +2.7 | +5.8 |
|  | [[Bentamapimod (drug)]] 0.05 µM |  | +2.3 | +2.7 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.1 | +2.0 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.0 | -22.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -4.3 | -6.5 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.3 | -14.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.2 | -5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.9 | -2.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.9 | -4.2 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -2.7 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -3.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.2 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil and HOOK domain protein 88C |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.11-q32.12 — chr14:91,271,323-91,417,844 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DAPLE, HkRP2, SCA40; previously KIAA1509 |
| Gene groups (HGNC) | HOOK related protein family |
| Reactome | 3 pathways, smallest: Negative regulation of TCF-dependent signaling by DVL-interacting proteins; TCF dependent signaling in response to WNT; Signaling by WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9P219](https://www.uniprot.org/uniprotkb/Q9P219) (Protein Daple):

> Required for activation of guanine nucleotide-binding proteins (G proteins) during non-canonical Wnt signaling. Binds to ligand-activated Wnt receptor FZD7, displacing DVL1 from the FZD7 receptor and leading to inhibition of canonical Wnt signaling. Acts as a non-receptor guanine nucleotide exchange factor by also binding to guanine nucleotide-binding protein G(i) alpha (Gi-alpha) subunits, leading to their activation. Binding to Gi-alpha subunits displaces the beta and gamma subunits from the …

**Summary**, from NCBI Gene [440193](https://www.ncbi.nlm.nih.gov/gene/440193):

> This gene encodes a ubiquitously expressed coiled-coil domain-containing protein that interacts with the dishevelled protein and is a negative regulator of the Wnt signalling pathway. The protein encoded by this gene has a PDZ-domain binding motif in its C-terminus with which it interacts with the dishevelled protein. Dishevelled is a scaffold protein involved in the regulation of the Wnt signaling pathway. The Wnt signaling pathway plays an important role in embryonic development, tissue …

**Accessions** — [HGNC:19967](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19967) · Entrez [440193](https://www.ncbi.nlm.nih.gov/gene/440193) · UniProt [Q9P219](https://www.uniprot.org/uniprotkb/Q9P219) · Ensembl [ENSG00000015133](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000015133)

## Data

Gene col 291: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 291); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 291, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 291]; `tensor/DDL_lfc|DDL_z.npy` [291]; `embed/gene_vectors.npy` [291]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 291 or target_col == 291). Every well: [[CCDC88C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC88C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
