---
symbol: "GCDH"
type: "gene"
col: 2625
ensembl_id: "ENSG00000105607"
name: "glutaryl-CoA dehydrogenase"
location: "19p13.13"
module: 29
arm: "-"
pooled_cpm: 10.8
n_lines_expressing: 50
n_dd_up: 27
n_dd_down: 1
n_dd_up_clean: 18
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# GCDH

*glutaryl-CoA dehydrogenase* — 19p13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (9 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 12.4× (z +35.4, q 0e+00, up in 47 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.731× (z -4.4, q 0.005, down in 17 of 46 measured lines) ⚠ cell-cycle shift, explains ~26% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 0.181×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change); [[Acetazolamide (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0654×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.174×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SNU-1 0.114×).
> Its strongest partners by |cos| (87 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 13 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASL]] (+0.73, fdr 1e-05), [[INAFM1]] (+0.58, fdr 1e-05), [[NOSIP]] (+0.57, fdr 2e-05); moves opposite to [[DSC3]] (-0.57, fdr 0.001, ⚠ not reproduced), [[RAB11FIP2]] (-0.57, fdr 7e-05), [[NAA50]] (-0.53, fdr 4e-05), [[ARPP19]] (-0.51, fdr 5e-05).
> It sits in the **-** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FZD3]] → it (grade B ⚠); 1 goes from it, the strongest it → [[DERA]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2625.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **12.4×** | +35.4 | 0e+00 | 47/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **10.2×** | +32.7 | 0e+00 | 47/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **7.77×** | +28.8 | 0e+00 | 47/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **3.57×** | +25.3 | 0e+00 | 47/47 (HEC-1-A, LoVo, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.93×** | +13.1 | 7e-37 | 33/45 (SW480, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.04×** | +9.6 | 6e-20 | 33/46 (HEC-1-A, COLO 205, …) | top dose only | cell-cycle shift (explains ~17% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.95×** | +9.0 | 1e-17 | 31/41 (NCI-H2030, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~45% of this change | **1.59×** | +6.5 | 5e-09 | 26/46 (LS 180, SW1417, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +6.5 | 6e-09 | 27/47 (SW480, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +6.3 | 2e-08 | 24/43 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.50×** | +5.7 | 7e-07 | 24/45 (SW480, J82, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.50×** | +5.7 | 8e-07 | 22/47 (LS 180, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change | **1.50×** | +5.4 | 2e-06 | 6/17 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.44×** | +5.1 | 1e-05 | 18/47 (SK-MEL-2, SW480, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.43×** | +5.0 | 2e-05 | 23/47 (LS 180, HEC-1-A, …) | rises with dose | composition shift |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.85×** | +4.5 | 2e-04 | 11/44 (SW480, HEC-1-A, …) | rises with dose | noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +4.2 | 8e-04 | 17/48 (BT-474, HEC-1-A, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.77×** | +4.2 | 8e-04 | 12/48 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.006 | 10/47 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.015 | 9/43 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2625.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (SW480 0.181×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change); [[Acetazolamide (drug)]] 0.5 µM in 1 line (HepG2/C3A 0.0654×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (MIA PaCa-2 0.174×); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SNU-1 0.114×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.731×** | -4.4 | 0.005 | 17/46 (C32, SNU-1, …) | two highest doses |  |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.787× | -3.4 | 0.19 | 7/47 (HS-578T, HCT15, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.45 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2625. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 17.5 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.95× (z +21.4) | — |
| [[SW480 (line)]] | alt | 15.5 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 16.6× (z +23.7) | [[Dinaciclib (drug)]] 5 µM 0.181× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~83% of this change |
| [[A549 (line)]] | wt | 5.37 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 18.2× (z +11.5) | [[Bendamustine (drug)]] 5 µM 0.105× (z -8.6) |
| [[COLO 205 (line)]] | alt | 8.11 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 39.0× (z +13.5) | — |
| [[HOP62 (line)]] | alt | 6.55 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 19.2× (z +13.3) | — |
| [[HS-578T (line)]] | alt | 9.73 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 19.4× (z +14.7) | — |
| [[HT-29 (line)]] | alt | 9.68 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 13.7× (z +12.6) | — |
| [[J82 (line)]] | alt | 11.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.11× (z +13.6) | — |
| [[KATO III (line)]] | alt | 10.8 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 16.5× (z +14.7) | — |
| [[LoVo (line)]] | wt | 10.0 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.50× (z +17.8) | — |
| [[LS 180 (line)]] | wt | 14.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 16.9× (z +16.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 13.6 | 3 | 1 | [[Panobinostat (drug)]] 5 µM 11.5× (z +13.8) | [[Homoharringtonine (drug)]] 0.5 µM 0.174× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 5.47 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 18.2× (z +12.7) | — |
| [[NCI-H2030 (line)]] | alt | 10.2 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 8.13× (z +12.4) | — |
| [[NCI-H460 (line)]] | wt | 7.20 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 14.2× (z +15.8) | — |
| [[Panc 03.27 (line)]] | alt | 15.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 11.9× (z +13.0) | — |
| [[SNU-423 (line)]] | alt | 10.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 18.6× (z +14.7) | — |
| [[SW1417 (line)]] | alt | 20.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 9.12× (z +15.0) | — |
| [[A-172 (line)]] | wt | 8.50 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 14.8× (z +12.9) | — |
| [[A-427 (line)]] | wt | 13.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.43× (z +10.1) | — |
| [[A498 (line)]] | wt | 7.63 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.43× (z +12.5) | — |
| [[AsPC-1 (line)]] | alt | 5.64 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 21.5× (z +12.0) | — |
| [[BT-474 (line)]] | alt | 18.5 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 10.1× (z +14.0) | — |
| [[HCT15 (line)]] | alt | 16.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 12.0× (z +11.5) | — |
| [[HepG2_C3A (line)]] | wt | 9.65 | 2 | 1 | [[Panobinostat (drug)]] 0.5 µM 14.8× (z +9.9) | [[Acetazolamide (drug)]] 0.5 µM 0.0654× (z -10.0) |
| [[Hs 766T (line)]] | wt | 6.38 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 19.7× (z +11.5) | — |
| [[LOX-IMVI (line)]] | wt | 4.91 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 16.2× (z +10.7) | — |
| [[NCI-H1792 (line)]] | alt | 7.47 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 14.0× (z +11.1) | [[Docetaxel (drug)]] 0.05 µM 0.134× (z -8.5) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 11.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.29× (z +11.5) | — |
| [[PANC-1 (line)]] | alt | 9.46 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.54× (z +16.1) | — |
| [[RKO (line)]] | wt | 16.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.66× (z +11.5) | — |
| [[RPMI-7951 (line)]] | alt | 11.8 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 17.9× (z +13.0) | — |
| [[SHP-77 (line)]] | alt | 21.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.32× (z +12.4) | — |
| [[SK-MEL-2 (line)]] | alt | 15.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 11.2× (z +13.5) | — |
| [[SNU-1 (line)]] | wt | 13.2 | 2 | 1 | [[Panobinostat (drug)]] 5 µM 13.7× (z +10.6) | [[Pyridoxine (drug)]] 0.5 µM 0.114× (z -8.8) |
| [[CFPAC-1 (line)]] | alt | 7.12 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.54× (z +11.8) | — |
| [[H4 (line)]] | wt | 9.96 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 22.3× (z +10.2) | — |
| [[hTERT-HPNE (line)]] | wt | 5.88 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 19.6× (z +9.4) | — |
| [[SW 900 (line)]] | alt | 7.31 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 9.79× (z +8.7) | — |
| [[SW48 (line)]] | wt | 14.2 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 14.1× (z +10.3) | — |
| [[C-33 A (line)]] | alt | 8.20 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 11.5× (z +9.3) | — |
| [[C32 (line)]] | wt | 8.87 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.96× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 13.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.49× (z +9.2) | — |
| [[AN3 CA (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2625), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASL]] | +0.73 | +0.54 / +0.68 | both halves | 1e-05 | pathway: Metabolism of amino acids and derivatives |
| [[INAFM1]] | +0.58 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[NOSIP]] | +0.57 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[MIGA2]] | +0.57 | +0.30 / +0.48 | both halves | 2e-04 |  |
| [[ENDOV]] | +0.57 | +0.46 / +0.50 | both halves | 3e-05 |  |
| [[ZNF324]] | +0.56 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[PMM1]] | +0.55 | +0.36 / +0.49 | both halves | 1e-04 |  |
| [[DGAT1]] | +0.55 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[MAPK8IP3]] | +0.53 | +0.35 / +0.39 | both halves | 1e-04 |  |
| [[SLC25A33]] | +0.53 | +0.26 / +0.55 | both halves | 4e-04 |  |
| [[ATG4B]] | +0.52 | +0.19 / +0.49 | ⚠ not reproduced | 8e-04 |  |
| [[ATG2A]] | +0.52 | +0.38 / +0.42 | both halves | 6e-05 |  |
| [[SPOUT1]] | +0.52 | +0.38 / +0.55 | both halves | 6e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DSC3]] | -0.57 | -0.17 / -0.45 | ⚠ not reproduced | 0.001 |  |
| [[RAB11FIP2]] | -0.57 | -0.38 / -0.46 | both halves | 7e-05 |  |
| [[NAA50]] | -0.53 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[TLCD4-RWDD3]] | -0.53 | -0.14 / -0.35 | ⚠ not reproduced | 0.002 |  |
| [[ARPP19]] | -0.51 | -0.39 / -0.55 | both halves | 5e-05 |  |
| [[RAB23]] | -0.51 | -0.38 / -0.40 | both halves | 7e-05 |  |
| [[VBP1]] | -0.50 | -0.24 / -0.41 | both halves | 4e-04 |  |
| [[RAD23B]] | -0.50 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[ERAP1]] | -0.50 | -0.26 / -0.49 | both halves | 4e-04 |  |
| [[ZC3HAV1L]] | -0.49 | -0.50 / -0.42 | both halves | 4e-05 |  |
| [[TMX1]] | -0.49 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[FUCA2]] | -0.48 | -0.37 / -0.43 | both halves | 8e-05 |  |
| [[SETD7]] | -0.48 | -0.38 / -0.31 | both halves | 2e-04 |  |
| [[GALNT7]] | -0.48 | -0.30 / -0.35 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FZD3]] | B | FZD3 activity raises GCDH's level | lines that do not express FZD3 (9) vs lines expressing it (41) | 1.36× lower at baseline in the lines without FZD3 | 0.089 | ⚠ within organs, on part of the lines; also absent: FBXO16, SLC16A10, LINC02456; maybe low, not absent; its own permutation p |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DERA]] | C | GCDH's natural level weakens DERA's drug response | GCDH's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.01; direction not clear | 0.082 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **-** arm (projection on the module's main direction -0.487). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-31.2, -14.5); signed map (-25.9, 12.5). **Vector** length 56.3, 8.80% of its response variance represented; |z| ≥ 3 in 981 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.6 | +35.4 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.1 | +32.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.0 | +25.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.6 | +28.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.0 | +3.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.4 | +1.6 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | +1.4 | +1.5 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +1.4 | +1.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.2 | +6.5 |
| fall | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -5.0 | -4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.9 | -2.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +0.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +2.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.0 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.0 | +4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.9 | -1.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.7 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | glutaryl-CoA dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.13 — chr19:12,891,128-12,915,126 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ACAD5, GCD |
| Gene groups (HGNC) | Acyl-CoA dehydrogenase family; Flavoproteins |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Reactome | 2 pathways, smallest: Lysine catabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92947](https://www.uniprot.org/uniprotkb/Q92947) (Glutaryl-CoA dehydrogenase, mitochondrial):

> Catalyzes the oxidative decarboxylation of glutaryl-CoA to crotonyl-CoA and CO(2) in the degradative pathway of L-lysine, L-hydroxylysine, and L-tryptophan metabolism. It uses electron transfer flavoprotein as its electron acceptor. Isoform Short is inactive.

**Summary**, from NCBI Gene [2639](https://www.ncbi.nlm.nih.gov/gene/2639):

> The protein encoded by this gene belongs to the acyl-CoA dehydrogenase family. It catalyzes the oxidative decarboxylation of glutaryl-CoA to crotonyl-CoA and CO(2) in the degradative pathway of L-lysine, L-hydroxylysine, and L-tryptophan metabolism. It uses electron transfer flavoprotein as its electron acceptor. The enzyme exists in the mitochondrial matrix as a homotetramer of 45-kD subunits. Mutations in this gene result in the metabolic disorder glutaric aciduria type 1, which is also known …

**Accessions** — [HGNC:4189](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4189) · Entrez [2639](https://www.ncbi.nlm.nih.gov/gene/2639) · UniProt [Q92947](https://www.uniprot.org/uniprotkb/Q92947) · Ensembl [ENSG00000105607](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105607)

## Data

Gene col 2625: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2625); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2625, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2625]; `tensor/DDL_lfc|DDL_z.npy` [2625]; `embed/gene_vectors.npy` [2625]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2625 or target_col == 2625). Every well: [[GCDH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GCDH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
