---
symbol: "LRP5L"
type: "gene"
col: 1858
ensembl_id: "ENSG00000100068"
name: "LDL receptor related protein 5 like (pseudogene)"
location: "22q11.23"
module: 204
arm: "+"
pooled_cpm: 25.4
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 3
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/204"]
generated_by: "tahoemap"
---

# LRP5L

*LDL receptor related protein 5 like (pseudogene)* — 22q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 2.35× (z +8.6, q 3e-15, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.288× (z -12.6, q 1e-33, down in 43 of 44 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (LS 180 0.0443×, NCI-H2347 0.0608×, SW1417 0.106×, SW48 0.0689×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (LoVo 0.0918×, A498 0.0775×, HEC-1-A 0.0912×, KATO III 0.115×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A549 0.0852×, NCI-H2347 0.141×, SW1417 0.166×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LOX-IMVI 0.299×, C32 0.298×); [[Saquinavir (drug)]] 0.5 µM in 1 line (H4 0.0825×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBTD1]] (+0.68, fdr 1e-05), [[GCSH]] (+0.67, fdr 7e-06), [[USP3]] (+0.66, fdr 1e-05); moves opposite to [[TAF2]] (-0.64, fdr 1e-05), [[ZNF655]] (-0.62, fdr 2e-05), [[CHM]] (-0.62, fdr 1e-05).
> It is in [[Module 204]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1858.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.35×** | +8.6 | 3e-15 | 41/48 (PANC-1, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.29×** | +8.4 | 2e-14 | 39/46 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.15×** | +7.7 | 2e-12 | 39/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.85×** | +6.2 | 6e-08 | 35/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.85×** | +6.2 | 6e-08 | 38/47 (MIA PaCa-2, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.23×** | +6.2 | 6e-08 | 38/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.81×** | +6.0 | 2e-07 | 33/48 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.91×** | +5.6 | 1e-06 | 32/46 (RKO, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.44×** | +5.2 | 1e-05 | 29/48 (SW1417, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.40×** | +4.8 | 8e-05 | 25/48 (NCI-H23, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.59×** | +4.7 | 2e-04 | 30/47 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.59×** | +4.6 | 2e-04 | 30/48 (SNU-423, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.56×** | +4.5 | 3e-04 | 25/46 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.56×** | +4.5 | 3e-04 | 29/48 (SNU-423, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +3.7 | 0.008 | 21/46 (NCI-H460, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.89×** | +3.4 | 0.027 | 20/48 (SNU-423, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.37×** | +3.2 | 0.047 | 17/46 (SNU-423, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.36×** | +3.1 | 0.066 | 23/48 (NCI-H460, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.24×** | +3.0 | 0.073 | 18/48 (SK-MEL-2, SNU-423, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1858.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (LS 180 0.0443×, NCI-H2347 0.0608×, SW1417 0.106×, SW48 0.0689×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 5 lines (LoVo 0.0918×, A498 0.0775×, HEC-1-A 0.0912×, KATO III 0.115×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 3 lines (A549 0.0852×, NCI-H2347 0.141×, SW1417 0.166×; ⚠ toxic; transcription drop); [[Homoharringtonine (drug)]] 5 µM in 2 lines (LOX-IMVI 0.299×, C32 0.298×); [[Saquinavir (drug)]] 0.5 µM in 1 line (H4 0.0825×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.288×** | -12.6 | 1e-33 | 43/44 (LS 180, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.351×** | -10.2 | 7e-22 | 29/35 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.505×** | -6.4 | 3e-08 | 28/40 (A549, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1858. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 24.6 | 5 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 4.28× (z +9.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.05 µM 4.28× (z +9.7) | [[Dinaciclib (drug)]] 0.5 µM 0.254× (z -9.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 23.5 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.17× (z +12.8) | [[Dinaciclib (drug)]] 0.5 µM 0.298× (z -9.5) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 18.1 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +10.1) | [[Dinaciclib (drug)]] 0.5 µM 0.0608× (z -17.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 54.1 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.42× (z +11.8) | [[Dinaciclib (drug)]] 0.5 µM 0.106× (z -15.3) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 43.4 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 0.05 µM 6.20× (z +8.7) | [[Dinaciclib (drug)]] 0.5 µM 0.0689× (z -13.6) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 27.1 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.21× (z +8.9) | — |
| [[A498 (line)]] | wt | 31.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0775× (z -15.6) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 23.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0912× (z -14.1) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 35.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0918× (z -19.2) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 22.6 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.97× (z +9.8) | [[Dinaciclib (drug)]] 0.5 µM 0.0443× (z -19.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 66.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.11× (z +11.4) | [[Dinaciclib (drug)]] 0.5 µM 0.168× (z -12.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 21.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0852× (z -12.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0997× (z -11.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 20.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 12.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.124× (z -9.5) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 17.7 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0825× (z -9.5) |
| [[Hs 766T (line)]] | wt | 17.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.149× (z -8.5) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 24.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.181× (z -8.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.238× (z -8.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -8.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 25.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -13.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 31.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 30.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.212× (z -9.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 24.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0960× (z -13.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 8.86 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 28.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1858), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBTD1]] | +0.68 | +0.69 / +0.54 | both halves | 1e-05 |  |
| [[GCSH]] | +0.67 | +0.69 / +0.58 | both halves | 7e-06 |  |
| [[USP3]] | +0.66 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[PDXP]] | +0.65 | +0.62 / +0.57 | both halves | 9e-06 |  |
| [[AGAP3]] | +0.65 | +0.66 / +0.55 | both halves | 1e-05 |  |
| [[EPB41L4B]] | +0.64 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[PPARGC1B]] | +0.63 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[VGLL4]] | +0.63 | +0.72 / +0.56 | both halves | 1e-05 |  |
| [[SEC61A2]] | +0.62 | +0.68 / +0.54 | both halves | 1e-05 |  |
| [[SSBP4]] | +0.62 | +0.71 / +0.44 | both halves | 3e-05 |  |
| [[PMS2P3-1]] | +0.62 | +0.67 / +0.48 | both halves | 2e-05 |  |
| [[GATA4]] | +0.61 | +0.48 / +0.55 | both halves | 2e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAF2]] | -0.64 | -0.66 / -0.55 | both halves | 1e-05 |  |
| [[ZNF655]] | -0.62 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[CHM]] | -0.62 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[SLC36A4]] | -0.62 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[TOR1AIP1]] | -0.60 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[ZNF268]] | -0.60 | -0.65 / -0.44 | both halves | 3e-05 |  |
| [[ZNF140]] | -0.59 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[C11orf58]] | -0.58 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[FBXO38]] | -0.58 | -0.61 / -0.51 | both halves | 1e-05 |  |
| [[C6orf62]] | -0.58 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[STAMBP]] | -0.58 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[FCF1]] | -0.57 | -0.70 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 204]]; 15 genes; every member is in the + arm (projection on the module's main direction 0.729). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.54; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-7.4, -5.6); signed map (-21.3, 18.1). **Vector** length 77.5, 18.4% of its response variance represented; |z| ≥ 3 in 1,045 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +4.0 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +3.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +3.0 | +3.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +2.9 | +4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.3 | -0.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +0.2 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.7 | -0.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.8 | +5.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | +2.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.8 | +0.7 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.7 | +0.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.6 | -0.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | LDL receptor related protein 5 like (pseudogene) |
| Locus type | pseudogene |
| Location | 22q11.23 — chr22:25,351,612-25,405,274 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | DKFZp434O0213 |
| Matched by | ensembl_id |

UniProt [A4QPB2](https://www.uniprot.org/uniprotkb/A4QPB2) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:25323](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25323) · Entrez [91355](https://www.ncbi.nlm.nih.gov/gene/91355) · UniProt [A4QPB2](https://www.uniprot.org/uniprotkb/A4QPB2) · Ensembl [ENSG00000100068](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100068)

## Data

Gene col 1858: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1858); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1858, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1858]; `tensor/DDL_lfc|DDL_z.npy` [1858]; `embed/gene_vectors.npy` [1858]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1858 or target_col == 1858). Every well: [[LRP5L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LRP5L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
