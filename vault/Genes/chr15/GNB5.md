---
symbol: "GNB5"
type: "gene"
col: 931
ensembl_id: "ENSG00000069966"
name: "G protein subunit beta 5"
location: "15q21.2"
module: 132
arm: "+"
pooled_cpm: 40.41
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 20
n_dd_up_clean: 5
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/132"]
generated_by: "tahoemap"
---

# GNB5

*G protein subunit beta 5* — 15q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.38× (z +12.5, q 7e-33, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.434× (z -32.2, q 0e+00, down in 45 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FHL1]] (+0.64, fdr 1e-05), [[RNF130]] (+0.62, fdr 1e-05), [[LRRC20]] (+0.62, fdr 1e-05); moves opposite to [[LINS1]] (-0.59, fdr 3e-05), [[EFCAB6]] (-0.59, fdr 3e-05), [[RRP8]] (-0.57, fdr 6e-05).
> It is in [[Module 132]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ASAP3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 931.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +12.5 | 7e-33 | 36/48 (LS 180, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +10.2 | 5e-22 | 26/40 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.39×** | +9.1 | 3e-17 | 29/46 (A498, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.33×** | +7.9 | 6e-13 | 27/48 (LS 180, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.24×** | +5.9 | 5e-07 | 22/48 (LS 180, A498, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +5.4 | 7e-06 | 20/48 (LS 180, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +5.2 | 2e-05 | 13/48 (PANC-1, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | 1.19× | +4.8 | 1e-04 | 20/48 (A498, LS 180, …) | all doses, flat |  |
| [[Radotinib (drug)]] 5 µM |  | 1.13× | +4.6 | 2e-04 | 14/48 (A-172, RKO, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.18× | +4.5 | 3e-04 | 16/48 (SW480, LS 180, …) | inconsistent across doses |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | 1.10× | +3.5 | 0.020 | 3/48 (SW480, LOX-IMVI, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.28×** | +3.5 | 0.020 | 10/48 (A498, CFPAC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.13× | +3.4 | 0.032 | 16/48 (LS 180, A498, …) | top dose only |  |
| [[Trifluridine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.13× | +3.3 | 0.040 | 3/48 (hTERT-HPNE, RKO, …) | rises with dose |  |
| [[Saquinavir (drug)]] 5 µM |  | 1.08× | +3.1 | 0.064 | 4/48 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 931.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.434×** | -32.2 | 0e+00 | 45/48 (PANC-1, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.477×** | -20.2 | 0e+00 | 42/47 (PANC-1, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.464×** | -20.1 | 0e+00 | 42/48 (PANC-1, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.484×** | -19.8 | 0e+00 | 39/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.487×** | -19.6 | 0e+00 | 36/47 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.590×** | -14.4 | 6e-45 | 31/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.639×** | -12.2 | 3e-32 | 31/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.692×** | -10.0 | 9e-22 | 29/48 (PANC-1, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.777×** | -9.7 | 1e-20 | 25/47 (A-427, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.788×** | -9.2 | 2e-18 | 26/48 (SNU-1, A-427, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.564×** | -8.2 | 2e-14 | 30/49 (LOX-IMVI, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.569×** | -8.0 | 4e-14 | 26/48 (NCI-H1573, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~15% of this change | **0.817×** | -5.5 | 2e-06 | 20/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.829×** | -5.1 | 2e-05 | 22/48 (SW 900, SK-MEL-2, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.835× | -4.9 | 4e-05 | 17/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belzutifan (drug)]] 5 µM |  | **0.716×** | -4.7 | 7e-05 | 16/45 (Hs 766T, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.846× | -4.5 | 2e-04 | 16/48 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.906× | -3.8 | 0.004 | 13/48 (A-427, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 931. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 80.3 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -23.3) |
| [[PANC-1 (line)]] | alt | 48.5 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -36.2) |
| [[SNU-1 (line)]] | wt | 70.1 | 0 | 8 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.121× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -12.2) |
| [[LoVo (line)]] | wt | 51.9 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.252× (z -16.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.309× (z -14.3) |
| [[NCI-H1573 (line)]] | alt | 47.2 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.262× (z -19.5) |
| [[A-427 (line)]] | wt | 41.1 | 0 | 5 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -15.1) |
| [[A549 (line)]] | wt | 58.4 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -21.2) |
| [[AsPC-1 (line)]] | alt | 44.2 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -18.3) |
| [[A498 (line)]] | wt | 34.7 | 2 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.15× (z +9.8) ⚠ toxic; transcription drop · without an alert: [[Tucidinostat (drug)]] 5 µM 1.68× (z +9.5) | [[Homoharringtonine (drug)]] 5 µM 0.531× (z -11.3) |
| [[HOP62 (line)]] | alt | 40.7 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.27× (z +8.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.301× (z -18.1) |
| [[Hs 766T (line)]] | wt | 46.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -20.1) |
| [[HT-29 (line)]] | alt | 52.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -25.5) |
| [[J82 (line)]] | alt | 64.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.303× (z -21.8) |
| [[LOX-IMVI (line)]] | wt | 34.1 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.152× (z -17.5) |
| [[Panc 03.27 (line)]] | alt | 30.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -12.9) |
| [[MIA PaCa-2 (line)]] | alt | 21.1 | 0 | 3 | — | [[Harringtonine (drug)]] 0.5 µM 0.168× (z -12.3) |
| [[HCT15 (line)]] | alt | 40.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.342× (z -11.5) |
| [[HS-578T (line)]] | alt | 25.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -14.1) |
| [[NCI-H1792 (line)]] | alt | 31.9 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.188× (z -13.5) |
| [[NCI-H2030 (line)]] | alt | 54.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -20.9) |
| [[NCI-H2347 (line)]] | alt | 24.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.511× (z -9.5) |
| [[RKO (line)]] | wt | 30.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -18.4) |
| [[RPMI-7951 (line)]] | alt | 40.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -14.0) |
| [[SK-MEL-2 (line)]] | alt | 43.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.484× (z -9.4) |
| [[SW48 (line)]] | wt | 44.7 | 0 | 2 | — | [[Harringtonine (drug)]] 0.05 µM 0.215× (z -10.9) |
| [[A-172 (line)]] | wt | 44.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.539× (z -9.4) |
| [[BT-474 (line)]] | alt | 26.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -10.8) |
| [[C32 (line)]] | wt | 38.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 22.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 46.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -11.1) |
| [[LS 180 (line)]] | wt | 10.4 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.70× (z +9.8) | — |
| [[NCI-H23 (line)]] | alt | 31.3 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.255× (z -10.7) |
| [[SNU-423 (line)]] | alt | 32.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -19.1) |
| [[SW 1271 (line)]] | alt | 45.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -10.4) |
| [[SW 900 (line)]] | alt | 36.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.312× (z -9.2) |
| [[SW1417 (line)]] | alt | 32.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.483× (z -9.5) |
| [[AN3 CA (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 38.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 44.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 24.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 931), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FHL1]] | +0.64 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[RNF130]] | +0.62 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[LRRC20]] | +0.62 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[NDRG3]] | +0.62 | +0.61 / +0.46 | both halves | 3e-05 |  |
| [[CAMK2G]] | +0.61 | +0.59 / +0.49 | both halves | 1e-05 | pathway: G alpha (i) signalling events |
| [[TMOD2]] | +0.61 | +0.33 / +0.66 | both halves | 1e-04 |  |
| [[RAB6B]] | +0.61 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[WASF3]] | +0.60 | +0.46 / +0.50 | both halves | 2e-05 | pathway: Leishmania infection |
| [[STX2]] | +0.59 | +0.54 / +0.45 | both halves | 3e-05 |  |
| [[MAPK9]] | +0.59 | +0.53 / +0.53 | both halves | 1e-05 | STRING 656 |
| [[STIMATE]] | +0.59 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[CRLF3]] | +0.58 | +0.49 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINS1]] | -0.59 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[EFCAB6]] | -0.59 | -0.57 / -0.46 | both halves | 3e-05 |  |
| [[RRP8]] | -0.57 | -0.43 / -0.38 | both halves | 6e-05 |  |
| [[TMEM232]] | -0.57 | -0.60 / -0.31 | both halves | 2e-04 |  |
| [[ANKRD17-DT]] | -0.57 | -0.54 / -0.31 | both halves | 2e-04 |  |
| [[FAM200A]] | -0.56 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[PCNX4-DT]] | -0.56 | -0.48 / -0.38 | both halves | 6e-05 |  |
| [[WARS2-AS1]] | -0.56 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[RFX3-DT]] | -0.56 | -0.52 / -0.34 | both halves | 1e-04 |  |
| [[TBCK]] | -0.55 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[AHI1-DT]] | -0.54 | -0.50 / -0.34 | both halves | 1e-04 |  |
| [[FBXO38-DT]] | -0.54 | -0.51 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASAP3]] | B | ASAP3 activity raises GNB5's level | lines that do not express ASAP3 (5) vs lines expressing it (45) | 1.86× lower at baseline in the lines without ASAP3 | 0.071 | ⚠ within organs, on part of the lines; also absent: DPF1, SCML2, CCDC102A; maybe low, not absent |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers GNB5's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[TSPAN33]] | B | TSPAN33 activity raises GNB5's level | lines that do not express TSPAN33 (12) vs lines expressing it (38) | 1.34× lower at baseline in the lines without TSPAN33 | 0.087 | ⚠ within organs, on part of the lines; also absent: SRCIN1, CRACD, GNAZ; maybe low, not absent |
| [[TMOD2]] | B | TMOD2 activity raises GNB5's level | lines that do not express TMOD2 (6) vs lines expressing it (44) | 1.68× lower at baseline in the lines without TMOD2 | 0.098 | ⚠ within organs, on part of the lines; also absent: CCDC102A, CYP46A1, FZD1; maybe low, not absent |
| [[MERTK]] | B | MERTK activity raises GNB5's level | lines that do not express MERTK (9) vs lines expressing it (41) | 1.27× lower at baseline in the lines without MERTK | 0.099 | ⚠ within organs, on part of the lines; also absent: PARD6B, GRHL1, SDHAP3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 132]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.649). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-2.9, -4.3); signed map (-39.3, -9.2). **Vector** length 88.1, 20.0% of its response variance represented; |z| ≥ 3 in 1,199 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.3 | +12.5 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +4.1 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +4.0 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.0 | +7.9 |
|  | [[Brivudine (drug)]] 5 µM |  | +4.0 | +3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.8 | +4.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.3 | +0.8 |
|  | [[Ipatasertib (drug)]] 5 µM |  | +2.2 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -7.7 | -32.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.6 | -20.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -9.7 |
|  | [[Selinexor (drug)]] 5 µM |  | -5.4 | -9.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.2 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.1 | -4.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | -3.0 | -4.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.4 | -1.2 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.1 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit beta 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q21.2 — chr15:52,115,100-52,191,392 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GB5 |
| Gene groups (HGNC) | WD repeat domain containing; G protein subunits beta |
| Reactome | 69 pathways, smallest: G beta:gamma signalling through BTK; Prostacyclin signalling through prostacyclin receptor; G beta:gamma signalling through PLC beta |
| Matched by | ensembl_id |

**Function**, from UniProt [O14775](https://www.uniprot.org/uniprotkb/O14775) (Guanine nucleotide-binding protein subunit beta-5):

> Enhances the GTPase-activating protein (GAP) activity and stability of R7 family regulator of G protein signaling (RGS) proteins, including RGS6, RGS7, RGS9 and RGS11, thereby promoting termination of G protein-mediated signaling downstream of G protein-coupled receptors (GPCRs).; [Isoform Gbeta5L]: Retina-specific isoform that forms a stable complex with RGS9-1 and RGS9BP in photoreceptors. Enhances RGS9-1 GAP activity toward transducin and promotes rapid recovery of rod and cone …

**Summary**, from NCBI Gene [10681](https://www.ncbi.nlm.nih.gov/gene/10681):

> Heterotrimeric guanine nucleotide-binding proteins (G proteins), which integrate signals between receptors and effector proteins, are composed of an alpha, a beta, and a gamma subunit. These subunits are encoded by families of related genes. This gene encodes a beta subunit. Beta subunits are important regulators of alpha subunits, as well as of certain signal transduction receptors and effectors. Alternatively spliced transcript variants encoding different isoforms exist. [provided by RefSeq, …

**Accessions** — [HGNC:4401](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4401) · Entrez [10681](https://www.ncbi.nlm.nih.gov/gene/10681) · UniProt [O14775](https://www.uniprot.org/uniprotkb/O14775) · Ensembl [ENSG00000069966](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000069966)

## Data

Gene col 931: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 931); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 931, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 931]; `tensor/DDL_lfc|DDL_z.npy` [931]; `embed/gene_vectors.npy` [931]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 931 or target_col == 931). Every well: [[GNB5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNB5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
