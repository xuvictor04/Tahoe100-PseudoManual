---
symbol: "ATP7A"
type: "gene"
col: 9092
ensembl_id: "ENSG00000165240"
name: "ATPase copper transporting alpha"
location: "Xq21.1"
module: 15
arm: "-"
pooled_cpm: 20.11
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 30
n_dd_up_clean: 11
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ATP7A

*ATPase copper transporting alpha* — Xq21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.05 µM: 1.60× (z +6.2, q 3e-07, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 0.431× (z -10.8, q 2e-24, down in 36 of 43 measured lines) ⚠ toxic. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.512× (z -8.9, q 2e-16, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JUNB]] (+0.67, fdr 7e-06), [[ARL5B]] (+0.65, fdr 7e-06), [[USP9X]] (+0.61, fdr 7e-05); moves opposite to [[SLC35D2]] (-0.60, fdr 1e-05), [[CDK5RAP1]] (-0.60, fdr 7e-06), [[CCT6P3-1]] (-0.60, fdr 1e-05).
> It sits in the **-** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[BHLHE41]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 1 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9092.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.05 µM |  | **1.60×** | +6.2 | 3e-07 | 29/48 (NCI-H460, A-172, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.54×** | +5.7 | 3e-06 | 26/48 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.51×** | +5.4 | 1e-05 | 25/48 (NCI-H460, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.28×** | +4.7 | 4e-04 | 23/48 (NCI-H460, HEC-1-A, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.41×** | +4.5 | 7e-04 | 25/48 (A-172, SNU-423, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.42×** | +4.5 | 8e-04 | 21/48 (A-427, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.25×** | +4.1 | 0.003 | 22/47 (Hs 766T, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.36×** | +4.1 | 0.004 | 23/48 (J82, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.33×** | +3.7 | 0.011 | 20/47 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.012 | 18/48 (NCI-H460, HT-29, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.70×** | +3.7 | 0.013 | 17/48 (NCI-H460, NCI-H1573, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.30×** | +3.4 | 0.028 | 14/43 (A498, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.19× | +3.2 | 0.066 | 11/48 (A549, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9092.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.431×** | -10.8 | 2e-24 | 36/43 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.512×** | -8.9 | 2e-16 | 37/48 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.626×** | -8.8 | 2e-16 | 44/48 (CFPAC-1, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.581×** | -7.2 | 6e-11 | 33/47 (NCI-H460, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.565×** | -7.2 | 8e-11 | 35/47 (HT-29, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.585×** | -7.1 | 8e-11 | 31/45 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.596×** | -6.9 | 4e-10 | 31/48 (HT-29, RPMI-7951, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.634×** | -6.1 | 9e-08 | 30/47 (C32, MIA PaCa-2, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.657×** | -5.4 | 4e-06 | 27/47 (SK-MEL-2, LOX-IMVI, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.675×** | -5.2 | 9e-06 | 25/48 (SK-MEL-2, CFPAC-1, …) | rises with dose |  |
| [[vincristine (drug)]] 5 µM |  | **0.503×** | -4.8 | 9e-05 | 25/43 (Panc 03.27, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.704×** | -4.7 | 1e-04 | 22/48 (PANC-1, LoVo, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.710×** | -4.6 | 2e-04 | 22/48 (C32, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.722×** | -4.4 | 5e-04 | 19/47 (SK-MEL-2, C32, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.736×** | -4.1 | 0.002 | 22/47 (C-33 A, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~14% here); position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | **0.674×** | -3.8 | 0.006 | 19/47 (SK-MEL-2, A-427, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.760×** | -3.7 | 0.008 | 20/48 (PANC-1, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~16% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.760×** | -3.7 | 0.008 | 21/48 (NCI-H23, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.596×** | -3.6 | 0.009 | 15/46 (Hs 766T, SNU-423, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **0.687×** | -3.6 | 0.009 | 13/48 (NCI-H23, RKO, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9092. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 33.4 | 0 | 3 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.157× (z -12.3) |
| [[SW480 (line)]] | alt | 28.2 | 0 | 3 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.283× (z -10.9) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.348× (z -9.4) |
| [[Hs 766T (line)]] | wt | 17.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.13× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.183× (z -8.5) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 18.4 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.124× (z -12.8) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 26.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0911× (z -15.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 20.6 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.287× (z -9.6) ⚠ toxic · without an alert: [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.313× (z -9.3) |
| [[A-172 (line)]] | wt | 11.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +9.1) | — |
| [[A-427 (line)]] | wt | 19.9 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -13.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AsPC-1 (line)]] | alt | 14.9 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +9.2) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[BT-474 (line)]] | alt | 9.51 | 0 | 1 | — | [[Hesperidin (drug)]] 5 µM 0.0699× (z -11.0) |
| [[C32 (line)]] | wt | 26.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +9.1) | — |
| [[CFPAC-1 (line)]] | alt | 21.5 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.360× (z -9.9) |
| [[COLO 205 (line)]] | alt | 29.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.159× (z -10.2) ⚠ toxic |
| [[HCT15 (line)]] | alt | 26.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.156× (z -9.2) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 16.8 | 0 | 1 | — | [[Bisoprolol (hemifumarate) (drug)]] 0.05 µM 0.0989× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 14.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.117× (z -10.2) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 21.5 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 5 µM 0.334× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 13.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 15.9 | 0 | 1 | — | [[vincristine (drug)]] 5 µM 0.0523× (z -8.6) |
| [[SNU-1 (line)]] | wt | 14.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0957× (z -9.6) |
| [[A498 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.28 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 46.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9092), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*45 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUNB]] | +0.67 | +0.61 / +0.64 | both halves | 7e-06 |  |
| [[ARL5B]] | +0.65 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[USP9X]] | +0.61 | +0.38 / +0.63 | both halves | 7e-05 |  |
| [[KLF10]] | +0.60 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[EID1]] | +0.59 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[FOS]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[SKIL]] | +0.59 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[NR4A3]] | +0.57 | +0.59 / +0.50 | both halves | 1e-05 |  |
| [[AHR]] | +0.56 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[EGR1]] | +0.56 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[AFF4]] | +0.56 | +0.44 / +0.58 | both halves | 3e-05 |  |
| [[SF3B1]] | +0.55 | +0.38 / +0.62 | both halves | 6e-05 |  |

## Genes that move opposite

*55 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35D2]] | -0.60 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[CDK5RAP1]] | -0.60 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[CCT6P3-1]] | -0.60 | -0.53 / -0.61 | both halves | 1e-05 |  |
| [[RILPL1]] | -0.59 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[ZNF767P-1]] | -0.58 | -0.51 / -0.65 | both halves | 1e-05 |  |
| [[CAMKK2]] | -0.58 | -0.52 / -0.61 | both halves | 1e-05 |  |
| [[ZNF500]] | -0.58 | -0.48 / -0.61 | both halves | 2e-05 |  |
| [[C8orf76]] | -0.57 | -0.56 / -0.54 | both halves | 1e-05 |  |
| [[EIF4ENIF1]] | -0.57 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[PTPN9]] | -0.56 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[PAM16]] | -0.56 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[MZT2A]] | -0.56 | -0.51 / -0.54 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BHLHE41]] | B | BHLHE41 activity raises ATP7A's level | lines that do not express BHLHE41 (19) vs lines expressing it (31) | 1.30× lower at baseline in the lines without BHLHE41 | 0.039 | ⚠ within organs, on part of the lines; also absent: RAC2, JHY, ENSG00000289600 |
| [[EGR2]] | B | EGR2 activity raises ATP7A's level | lines that do not express EGR2 (7) vs lines expressing it (43) | 1.54× lower at baseline in the lines without EGR2 | 0.089 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **-** arm (projection on the module's main direction -0.399). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-48.9, 14.0); signed map (7.4, 27.5). **Vector** length 99.5, 23.7% of its response variance represented; |z| ≥ 3 in 1,187 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +5.4 | +4.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +4.5 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.0 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +0.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +4.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.2 | +1.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.0 | +2.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.9 | +3.2 |
|  | [[Omeprazole (drug)]] 0.05 µM |  | +1.9 | +2.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -8.2 | -10.8 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -6.4 | -8.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -5.7 | -8.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -5.6 | -7.2 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -5.4 | -7.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -4.1 | -6.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.1 | -5.4 |
|  | [[vincristine (drug)]] 5 µM |  | -3.3 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | ATPase copper transporting alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xq21.1 — chrX:77,910,690-78,050,395 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MNK |
| Gene groups (HGNC) | ATPase copper transporting |
| Hallmark sets | PROTEIN_SECRETION, HYPOXIA |
| Reactome | 10 pathways, smallest: Ion influx/efflux at host-pathogen interface; Antimicrobial peptides; Detoxification of Reactive Oxygen Species |
| Matched by | ensembl_id |

**Function**, from UniProt [Q04656](https://www.uniprot.org/uniprotkb/Q04656) (Copper-transporting ATPase 1):

> ATP-driven copper (Cu(+)) ion pump that plays an important role in intracellular copper ion homeostasis. Within a catalytic cycle, acquires Cu(+) ion from donor protein on the cytoplasmic side of the membrane and delivers it to acceptor protein on the lumenal side. The transfer of Cu(+) ion across the membrane is coupled to ATP hydrolysis and is associated with a transient phosphorylation that shifts the pump conformation from inward-facing to outward-facing state. Under physiological …

**Summary**, from NCBI Gene [538](https://www.ncbi.nlm.nih.gov/gene/538):

> This gene encodes a transmembrane protein that functions in copper transport across membranes. This protein is localized to the trans Golgi network, where it is predicted to supply copper to copper-dependent enzymes in the secretory pathway. It relocalizes to the plasma membrane under conditions of elevated extracellular copper, and functions in the efflux of copper from cells. Mutations in this gene are associated with Menkes disease, X-linked distal spinal muscular atrophy, and occipital horn …

**Accessions** — [HGNC:869](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:869) · Entrez [538](https://www.ncbi.nlm.nih.gov/gene/538) · UniProt [Q04656](https://www.uniprot.org/uniprotkb/Q04656) · Ensembl [ENSG00000165240](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165240)

## Data

Gene col 9092: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9092); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9092, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9092]; `tensor/DDL_lfc|DDL_z.npy` [9092]; `embed/gene_vectors.npy` [9092]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9092 or target_col == 9092). Every well: [[ATP7A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ATP7A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
