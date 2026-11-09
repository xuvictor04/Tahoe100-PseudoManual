---
symbol: "NMRK1"
type: "gene"
col: 2801
ensembl_id: "ENSG00000106733"
name: "nicotinamide riboside kinase 1"
location: "9q21.13"
module: 51
arm: "-"
pooled_cpm: 13.54
n_lines_expressing: 49
n_dd_up: 7
n_dd_down: 20
n_dd_up_clean: 7
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/051"]
generated_by: "tahoemap"
---

# NMRK1

*nicotinamide riboside kinase 1* — 9q21.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.89× (z +11.6, q 4e-28, up in 32 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.252× (z -24.9, q 0e+00, down in 43 of 45 measured lines).
> Its strongest partners by |cos| (92 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 8 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPL34-DT]] (+0.55, fdr 3e-05), [[RHCE]] (+0.54, fdr 4e-05), [[CCNO-DT]] (+0.52, fdr 1e-04); moves opposite to [[NCOA5]] (-0.52, fdr 4e-05), [[SMARCB1]] (-0.52, fdr 3e-05), [[FOXRED2]] (-0.50, fdr 6e-05).
> It sits in the **-** arm of [[Module 051]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ANKFN1]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[ERK5-IN-2 (drug)]] 0.5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2801.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.89×** | +11.6 | 4e-28 | 32/43 (Panc 03.27, A549, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +6.2 | 1e-07 | 26/46 (HOP62, SW 900, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.41×** | +4.4 | 0.002 | 16/43 (KATO III, SK-MEL-2, …) | two highest doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.46×** | +4.2 | 0.004 | 13/45 (A-172, A498, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.015 | 13/46 (KATO III, LS 180, …) | two highest doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.033 | 9/47 (A-172, J82, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.30×** | +3.4 | 0.060 | 12/46 (SW 900, NCI-H1573, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | 1.26× | +3.0 | 0.15 | 10/45 (A-172, SW480, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | 1.26× | +3.0 | 0.15 | 8/47 (Hs 766T, SW480, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2801.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.252×** | -24.9 | 0e+00 | 43/45 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.234×** | -18.6 | 0e+00 | 42/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.284×** | -16.1 | 0e+00 | 38/43 (SW480, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.301×** | -15.3 | 0e+00 | 37/43 (HOP62, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.377×** | -12.5 | 2e-33 | 38/46 (SW 900, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.337×** | -11.9 | 6e-31 | 34/44 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.424×** | -11.0 | 5e-26 | 38/46 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.457×** | -10.0 | 1e-21 | 28/45 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.297×** | -8.1 | 3e-14 | 35/45 (NCI-H1792, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.340×** | -7.2 | 3e-11 | 27/41 (SW480, HT-29, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.575×** | -7.0 | 9e-11 | 27/46 (H4, HCT15, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.637×** | -5.7 | 4e-07 | 26/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.602×** | -5.6 | 1e-06 | 20/38 (C32, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.667×** | -5.2 | 1e-05 | 18/46 (Hs 766T, PANC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.735×** | -3.9 | 0.004 | 16/46 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.574×** | -3.7 | 0.008 | 12/41 (LoVo, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.680×** | -3.5 | 0.016 | 9/47 (PANC-1, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.768×** | -3.4 | 0.023 | 13/43 (Hs 766T, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Piroxicam (drug)]] 0.05 µM |  | **0.780×** | -3.1 | 0.046 | 10/47 (LOX-IMVI, NCI-H1573, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.17 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2801. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 17.1 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.182× (z -17.3) |
| [[HOP62 (line)]] | alt | 19.7 | 1 | 7 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.10× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -19.6) |
| [[NCI-H1573 (line)]] | alt | 21.5 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -16.9) |
| [[PANC-1 (line)]] | alt | 16.0 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -18.4) |
| [[SW480 (line)]] | alt | 18.2 | 0 | 7 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.136× (z -17.0) |
| [[J82 (line)]] | alt | 11.5 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.80× (z +8.7) | [[Digitoxin (drug)]] 5 µM 0.124× (z -12.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.243× (z -11.8) |
| [[KATO III (line)]] | alt | 25.0 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.160× (z -13.1) |
| [[HEC-1-A (line)]] | alt | 35.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -17.1) |
| [[NCI-H1792 (line)]] | alt | 18.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -15.6) |
| [[BT-474 (line)]] | alt | 10.0 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0764× (z -11.4) |
| [[HCT15 (line)]] | alt | 31.3 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0813× (z -13.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.185× (z -9.0) |
| [[Hs 766T (line)]] | wt | 24.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -13.0) |
| [[LoVo (line)]] | wt | 15.2 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.180× (z -12.0) |
| [[SNU-423 (line)]] | alt | 6.73 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0679× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.192× (z -9.8) |
| [[A-172 (line)]] | wt | 11.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -10.9) |
| [[A498 (line)]] | wt | 28.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -16.8) |
| [[A549 (line)]] | wt | 7.39 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -10.4) |
| [[COLO 205 (line)]] | alt | 13.4 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0939× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.196× (z -9.8) |
| [[HT-29 (line)]] | alt | 11.6 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.115× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 5.73 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.26× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 6.21 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.37× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.0567× (z -11.0) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 11.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -11.9) |
| [[SW 900 (line)]] | alt | 10.7 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.0342× (z -16.5) |
| [[AsPC-1 (line)]] | alt | 10.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -11.5) |
| [[C32 (line)]] | wt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.205× (z -10.6) |
| [[CFPAC-1 (line)]] | alt | 7.04 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -12.7) |
| [[H4 (line)]] | wt | 8.37 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.0586× (z -9.4) |
| [[HS-578T (line)]] | alt | 7.11 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -12.5) |
| [[NCI-H2030 (line)]] | alt | 8.58 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 5.43 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0957× (z -9.8) |
| [[A-427 (line)]] | wt | 8.84 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.76 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.94 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.72 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.23 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2801), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPL34-DT]] | +0.55 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[RHCE]] | +0.54 | +0.43 / +0.55 | both halves | 4e-05 |  |
| [[CCNO-DT]] | +0.52 | +0.36 / +0.60 | both halves | 1e-04 |  |
| [[CATSPER2P1]] | +0.52 | +0.34 / +0.52 | both halves | 1e-04 |  |
| [[GAPVD1]] | +0.52 | +0.47 / +0.52 | both halves | 2e-05 |  |
| [[BMT2]] | +0.51 | +0.35 / +0.57 | both halves | 1e-04 |  |
| [[DNHD1]] | +0.49 | +0.27 / +0.57 | both halves | 3e-04 |  |
| [[LINC02656]] | +0.48 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[PPP1R32]] | +0.48 | +0.28 / +0.55 | both halves | 3e-04 |  |
| [[CATSPER2P1-1]] | +0.48 | +0.37 / +0.45 | both halves | 8e-05 |  |
| [[RTCA-AS1]] | +0.48 | +0.38 / +0.41 | both halves | 6e-05 |  |
| [[PNPLA8]] | +0.47 | +0.26 / +0.60 | both halves | 4e-04 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCOA5]] | -0.52 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[SMARCB1]] | -0.52 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[FOXRED2]] | -0.50 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[TTC26]] | -0.50 | -0.33 / -0.49 | both halves | 1e-04 |  |
| [[EPC2]] | -0.49 | -0.39 / -0.59 | both halves | 5e-05 |  |
| [[YTHDC2]] | -0.48 | -0.29 / -0.55 | both halves | 2e-04 |  |
| [[AGK]] | -0.47 | -0.22 / -0.58 | both halves | 6e-04 |  |
| [[CEP135]] | -0.45 | -0.34 / -0.47 | both halves | 1e-04 |  |
| [[MIOS]] | -0.45 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[ZNF480]] | -0.45 | -0.32 / -0.47 | both halves | 1e-04 |  |
| [[CRTC1]] | -0.45 | -0.39 / -0.37 | both halves | 9e-05 |  |
| [[EPC1]] | -0.45 | -0.34 / -0.50 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANKFN1]] | B | ANKFN1 activity strengthens NMRK1's drug response | lines that do not express ANKFN1 (7) vs lines expressing it (40) | the lines without ANKFN1 respond 0.74× as strongly (z diff +1.40); strongest at Homoharringtonine 5 µM: 0.52x vs 0.22x (z diff +4.7) | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000214803, LINC00298; maybe low, not absent; target measured in part of the lines; artifact flags |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[ERK5-IN-2 (drug)]] 0.5 µM | C | NMRK1's natural level lowers the cells' numbers under ERK5-IN-2 0.5 µM (makes them more sensitive) | NMRK1's natural level across 47 lines (lineage-adjusted; a glimpse) | r -0.59 | 0.491 over the table, 0.078 within its drug-dose | ⚠ within its drug-dose only (a lead); tissue can mimic it |

## Where it sits

- **Module**: [[Module 051]] — Chromatin modifying enzymes; 89 genes; this gene is in the **-** arm (projection on the module's main direction -0.436). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (3.3, 24.1); signed map (34.0, -3.9). **Vector** length 62.8, 11.2% of its response variance represented; |z| ≥ 3 in 1,089 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.1 | +6.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.7 | +11.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.4 | +1.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.7 | -1.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.7 | +0.8 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.5 | +2.3 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.4 | +1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.3 | +4.2 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -4.1 | -24.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.9 | -11.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.0 | -15.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -2.3 |
|  | [[EX229 (drug)]] 5 µM |  | -1.7 | -3.7 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | -1.1 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | nicotinamide riboside kinase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q21.13 — chr9:75,060,573-75,088,217 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ20559, NRK1, bA235O14.2; previously C9orf95 |
| Gene groups (HGNC) | Nicotinamide riboside kinase family |
| Reactome | 3 pathways, smallest: Nicotinate metabolism; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NWW6](https://www.uniprot.org/uniprotkb/Q9NWW6) (Nicotinamide riboside kinase 1):

> Catalyzes the phosphorylation of nicotinamide riboside (NR) and nicotinic acid riboside (NaR) to form nicotinamide mononucleotide (NMN) and nicotinic acid mononucleotide (NaMN). The enzyme also phosphorylates the antitumor drugs tiazofurin and 3-deazaguanosine.

**Summary**, from NCBI Gene [54981](https://www.ncbi.nlm.nih.gov/gene/54981):

> Nicotinamide adenine dinucleotide (NAD+) is essential for life in all organisms, both as a coenzyme for oxidoreductases and as a source of ADP-ribosyl groups used in various reactions. Nicotinic acid and nicotinamide, collectively known as niacin, are the vitamin precursors of NAD+. Nicotinamide riboside kinases, such as NRK1, function to synthesize NAD+ through nicotinamide mononucleotide using nicotinamide riboside as the precursor (Bieganowski and Brenner, 2004 [PubMed 15137942]).[supplied …

**Accessions** — [HGNC:26057](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26057) · Entrez [54981](https://www.ncbi.nlm.nih.gov/gene/54981) · UniProt [Q9NWW6](https://www.uniprot.org/uniprotkb/Q9NWW6) · Ensembl [ENSG00000106733](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106733)

## Data

Gene col 2801: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2801); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2801, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2801]; `tensor/DDL_lfc|DDL_z.npy` [2801]; `embed/gene_vectors.npy` [2801]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2801 or target_col == 2801). Every well: [[NMRK1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NMRK1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
