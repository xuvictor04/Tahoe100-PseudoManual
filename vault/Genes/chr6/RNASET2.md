---
symbol: "RNASET2"
type: "gene"
col: 370
ensembl_id: "ENSG00000026297"
name: "ribonuclease T2"
location: "6q27"
module: 164
arm: "+"
pooled_cpm: 52.56
n_lines_expressing: 48
n_dd_up: 10
n_dd_down: 23
n_dd_up_clean: 6
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/164"]
generated_by: "tahoemap"
---

# RNASET2

*ribonuclease T2* — 6q27

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.37× (z +7.7, q 8e-12, up in 29 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.408× (z -21.7, q 0e+00, down in 42 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MANBA]] (+0.68, fdr 1e-05), [[HERC3]] (+0.65, fdr 1e-05), [[GGA2]] (+0.64, fdr 1e-05); moves opposite to [[ZNF518B]] (-0.60, fdr 1e-05), [[THAP5]] (-0.60, fdr 1e-05), [[ANKLE2]] (-0.59, fdr 1e-05).
> It is in [[Module 164]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 370.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +7.7 | 8e-12 | 29/45 (LS 180, SW48, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.45×** | +6.4 | 6e-08 | 22/41 (C32, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Radotinib (drug)]] 5 µM |  | **1.24×** | +5.2 | 3e-05 | 21/46 (PANC-1, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change | **1.35×** | +5.0 | 9e-05 | 18/35 (A549, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Ponatinib (drug)]] 5 µM |  | **1.33×** | +4.9 | 9e-05 | 22/46 (PANC-1, NCI-H23, …) | all doses, stronger at high dose |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.39×** | +3.9 | 0.011 | 15/45 (SW48, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.23×** | +3.5 | 0.042 | 16/45 (LS 180, SW48, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.34×** | +3.4 | 0.047 | 9/43 (SW480, LoVo, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.093 | 13/45 (KATO III, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.21×** | +3.1 | 0.094 | 16/47 (LS 180, SW48, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.20× | +3.1 | 0.094 | 13/46 (PANC-1, SNU-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 370.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.408×** | -21.7 | 0e+00 | 42/46 (HepG2/C3A, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.319×** | -18.8 | 0e+00 | 43/46 (HepG2/C3A, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.316×** | -17.4 | 0e+00 | 45/46 (AsPC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.483×** | -12.5 | 2e-33 | 41/46 (HepG2/C3A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.496×** | -12.0 | 3e-31 | 38/46 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.638×** | -7.7 | 1e-12 | 29/45 (HepG2/C3A, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.643×** | -7.6 | 3e-12 | 30/45 (SNU-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.649×** | -7.4 | 1e-11 | 30/45 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.656×** | -7.2 | 4e-11 | 31/46 (SHP-77, HT-29, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.662×** | -7.1 | 9e-11 | 33/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.663×** | -6.8 | 7e-10 | 27/44 (HepG2/C3A, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.761×** | -4.7 | 1e-04 | 20/45 (MIA PaCa-2, LoVo, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.739×** | -4.6 | 2e-04 | 21/46 (A498, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.777×** | -4.3 | 6e-04 | 19/45 (NCI-H460, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 0.841× | -4.2 | 0.001 | 18/47 (NCI-H1792, SNU-1, …) | rises with dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.783×** | -4.2 | 0.001 | 19/45 (MIA PaCa-2, AN3 CA, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.788×** | -4.1 | 0.002 | 17/46 (A498, NCI-H23, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.09 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 370. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 325 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0784× (z -39.4) |
| [[CFPAC-1 (line)]] | alt | 298 | 0 | 10 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0667× (z -37.7) |
| [[AsPC-1 (line)]] | alt | 157 | 5 | 4 (1 ⚠) | [[Budesonide (drug)]] 0.5 µM 2.96× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -28.0) |
| [[HEC-1-A (line)]] | alt | 136 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.322× (z -18.2) |
| [[HT-29 (line)]] | alt | 140 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.140× (z -26.8) |
| [[PANC-1 (line)]] | alt | 15.1 | 2 (2 ⚠) | 4 | [[Panobinostat (drug)]] 5 µM 3.25× (z +9.4) ⚠ cell-cycle shift, explains ~44% of this change | [[Homoharringtonine (drug)]] 5 µM 0.402× (z -10.2) |
| [[A-172 (line)]] | wt | 35.8 | 0 | 5 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.234× (z -11.5) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.267× (z -10.5) |
| [[A498 (line)]] | wt | 126 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -13.5) |
| [[NCI-H460 (line)]] | wt | 28.0 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -19.4) |
| [[SW480 (line)]] | alt | 29.7 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -13.7) |
| [[HCT15 (line)]] | alt | 43.9 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -12.7) |
| [[LoVo (line)]] | wt | 28.6 | 1 | 3 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.55× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -11.9) |
| [[LS 180 (line)]] | wt | 46.1 | 3 (2 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.97× (z +15.8) | [[Harringtonine (drug)]] 5 µM 0.380× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 35.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -13.0) |
| [[NCI-H1792 (line)]] | alt | 53.0 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -18.1) |
| [[SNU-1 (line)]] | wt | 41.0 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0812× (z -14.3) |
| [[SNU-423 (line)]] | alt | 46.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -14.2) |
| [[BT-474 (line)]] | alt | 23.0 | 0 | 2 | — | [[Orlistat (drug)]] 0.05 µM 0.0976× (z -11.3) |
| [[COLO 205 (line)]] | alt | 22.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.121× (z -9.2) |
| [[H4 (line)]] | wt | 17.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0649× (z -10.6) |
| [[Hs 766T (line)]] | wt | 32.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.328× (z -12.5) |
| [[Panc 03.27 (line)]] | alt | 36.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.261× (z -9.5) |
| [[SW1417 (line)]] | alt | 41.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -13.7) |
| [[A-427 (line)]] | wt | 16.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -9.4) |
| [[AN3 CA (line)]] | alt | 61.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -11.9) |
| [[C-33 A (line)]] | alt | 31.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.163× (z -9.5) |
| [[HOP62 (line)]] | alt | 27.4 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.230× (z -10.8) |
| [[HS-578T (line)]] | alt | 20.6 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.215× (z -9.9) |
| [[J82 (line)]] | alt | 21.7 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.200× (z -11.3) |
| [[KATO III (line)]] | alt | 113 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -13.3) |
| [[NCI-H2030 (line)]] | alt | 17.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -8.6) |
| [[NCI-H23 (line)]] | alt | 17.6 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.147× (z -11.0) |
| [[NCI-H2347 (line)]] | alt | 15.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.244× (z -9.5) |
| [[RKO (line)]] | wt | 29.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0836× (z -14.7) |
| [[SHP-77 (line)]] | alt | 37.8 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.301× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 27.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.157× (z -10.5) |
| [[SW48 (line)]] | wt | 98.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +13.8) | — |
| [[A549 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.4 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 370), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*69 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MANBA]] | +0.68 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[HERC3]] | +0.65 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[GGA2]] | +0.64 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[SMAP2]] | +0.63 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[HELZ]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[GMCL1]] | +0.61 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[MED26]] | +0.61 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[GM2A]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 | STRING 461 |
| [[RELCH]] | +0.60 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[POM121]] | +0.58 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[KIAA2013]] | +0.58 | +0.54 / +0.57 | both halves | 1e-05 |  |
| [[MOSPD3]] | +0.58 | +0.46 / +0.65 | both halves | 3e-05 |  |

## Genes that move opposite

*31 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF518B]] | -0.60 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[THAP5]] | -0.60 | -0.51 / -0.61 | both halves | 1e-05 |  |
| [[ANKLE2]] | -0.59 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[ZNF140]] | -0.59 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[SLC36A4]] | -0.58 | -0.49 / -0.52 | both halves | 1e-05 |  |
| [[FKRP]] | -0.57 | -0.50 / -0.66 | both halves | 1e-05 |  |
| [[RAB30-DT]] | -0.57 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[ST7L]] | -0.57 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[RTL6]] | -0.57 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[CPLANE1]] | -0.56 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[ZNF260]] | -0.55 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[CHMP6]] | -0.55 | -0.51 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers RNASET2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[FHIP1A]] | B | FHIP1A activity raises RNASET2's level | lines that do not express FHIP1A (7) vs lines expressing it (43) | 1.63× lower at baseline in the lines without FHIP1A | 0.073 | ⚠ within organs, on part of the lines; also absent: SLC18B1, NIPAL1, TXNIP; maybe low, not absent |
| [[RAB20]] | B | RAB20 activity raises RNASET2's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 2.39× lower at baseline in the lines without RAB20 | 0.081 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 164]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.682). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (8.9, -18.7); signed map (-37.9, 21.7). **Vector** length 90.0, 20.8% of its response variance represented; |z| ≥ 3 in 1,040 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.2 | +7.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.0 | +5.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | +2.9 | +3.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.7 | +2.6 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.7 | -3.7 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +2.2 | +1.5 |
|  | [[Fumaric acid (drug)]] 5 µM |  | +2.1 | +2.0 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +2.1 | +2.3 |
|  | [[Ponatinib (drug)]] 0.05 µM |  | +2.0 | +2.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.4 | -18.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.9 | -17.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -5.5 | -12.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.2 | -4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -21.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.3 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.5 | -3.0 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -2.3 | -3.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | ribonuclease T2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q27 — chr6:166,922,113-166,957,191 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RNASE6PL, FLJ10907, bA514O12.3 |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [O00584](https://www.uniprot.org/uniprotkb/O00584) (Ribonuclease T2):

> Ribonuclease that plays an essential role in innate immune response by recognizing and degrading RNAs from microbial pathogens that are subsequently sensed by TLR8. Cleaves preferentially single-stranded RNA molecules between purine and uridine residues, which critically contributes to the supply of catabolic uridine and the generation of purine-2',3'-cyclophosphate-terminated oligoribonucleotides. In turn, RNase T2 degradation products promote the RNA-dependent activation of TLR8. In …

**Summary**, from NCBI Gene [8635](https://www.ncbi.nlm.nih.gov/gene/8635):

> This ribonuclease gene is a novel member of the Rh/T2/S-glycoprotein class of extracellular ribonucleases. It is a single copy gene that maps to 6q27, a region associated with human malignancies and chromosomal rearrangement. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:21686](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21686) · Entrez [8635](https://www.ncbi.nlm.nih.gov/gene/8635) · UniProt [O00584](https://www.uniprot.org/uniprotkb/O00584) · Ensembl [ENSG00000026297](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000026297)

## Data

Gene col 370: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 370); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 370, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 370]; `tensor/DDL_lfc|DDL_z.npy` [370]; `embed/gene_vectors.npy` [370]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 370 or target_col == 370). Every well: [[RNASET2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RNASET2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
