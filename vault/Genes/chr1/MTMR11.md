---
symbol: "MTMR11"
type: "gene"
col: 289
ensembl_id: "ENSG00000014914"
name: "myotubularin related protein 11"
location: "1q21.2"
module: 5
arm: "-"
pooled_cpm: 11.33
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 33
n_dd_up_clean: 1
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# MTMR11

*myotubularin related protein 11* — 1q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.57× (z +5.0, q 3e-04, up in 23 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.87×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 33 drug-doses (19 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.408× (z -9.9, q 4e-20, down in 34 of 41 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.427× (z -9.4, q 2e-18, down in 28 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPK3]] (+0.58, fdr 7e-06), [[LRP1]] (+0.55, fdr 1e-05), [[HCN3]] (+0.55, fdr 5e-05); moves opposite to [[WDR4]] (-0.58, fdr 1e-05), [[MECR]] (-0.58, fdr 1e-05), [[FAF1]] (-0.58, fdr 1e-05).
> It sits in the **-** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[CASP10]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 289.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.87×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.57×** | +5.0 | 3e-04 | 23/44 (NCI-H2030, MIA PaCa-2, …) | two highest doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.52×** | +4.2 | 0.009 | 14/44 (NCI-H2030, NCI-H460, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.0 | 0.014 | 5/47 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Pimozide (drug)]] 0.05 µM |  | 1.35× | +3.3 | 0.14 | 12/42 (A549, A-172, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 1.32× | +3.2 | 0.14 | 10/47 (NCI-H23, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 1.22× | +3.2 | 0.14 | 6/47 (LoVo, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 19 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 33 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 19 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 289.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **0.408×** | -9.9 | 4e-20 | 34/41 (HOP62, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.427×** | -9.4 | 2e-18 | 28/42 (KATO III, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.460×** | -8.5 | 3e-15 | 33/47 (SNU-423, CFPAC-1, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.479×** | -8.1 | 7e-14 | 35/45 (NCI-H1573, SNU-1, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.490×** | -7.8 | 5e-13 | 37/45 (RPMI-7951, HS-578T, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.504×** | -7.5 | 4e-12 | 28/46 (CFPAC-1, COLO 205, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.518×** | -7.2 | 3e-11 | 31/46 (COLO 205, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.484×** | -7.2 | 3e-11 | 29/45 (COLO 205, A-172, …) | rises with dose | composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.522×** | -7.1 | 6e-11 | 29/46 (LoVo, NCI-H1792, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **0.527×** | -7.0 | 1e-10 | 30/47 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose | position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.531×** | -7.0 | 2e-10 | 33/46 (NCI-H2347, LOX-IMVI, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.354×** | -6.0 | 1e-07 | 27/46 (COLO 205, SNU-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.685×** | -5.9 | 2e-07 | 24/45 (COLO 205, HT-29, …) | two highest doses | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.586×** | -5.9 | 2e-07 | 26/45 (LOX-IMVI, C32, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~44% of this change | **0.583×** | -5.4 | 3e-06 | 19/37 (NCI-H1792, C32, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.624×** | -5.2 | 8e-06 | 24/44 (HT-29, COLO 205, …) | rises with dose | position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **0.492×** | -4.1 | 0.001 | 21/42 (NCI-H2347, COLO 205, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.508×** | -3.9 | 0.003 | 13/40 (MIA PaCa-2, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.708×** | -3.8 | 0.004 | 17/46 (CFPAC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.786×** | -3.7 | 0.004 | 17/46 (MIA PaCa-2, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.536×** | -3.6 | 0.007 | 14/41 (SNU-1, A549, …) | top dose only | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.750×** | -3.2 | 0.032 | 13/44 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.594×** | -3.0 | 0.051 | 7/44 (LoVo, HEC-1-A, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **0.745×** | -2.9 | 0.061 | 14/44 (MIA PaCa-2, NCI-H460, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.772×** | -2.8 | 0.079 | 12/45 (H4, MIA PaCa-2, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.60 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 289. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 27.4 | 0 | 5 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -11.2) ⚠ cell-cycle shift, explains ~60% of this change |
| [[COLO 205 (line)]] | alt | 44.2 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.136× (z -16.6) ⚠ cell-cycle shift, explains ~60% of this change |
| [[A-172 (line)]] | wt | 23.8 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.157× (z -11.7) ⚠ cell-cycle shift, explains ~54% of this change |
| [[A549 (line)]] | wt | 15.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.298× (z -9.6) ⚠ cell-cycle shift, explains ~60% of this change |
| [[NCI-H1792 (line)]] | alt | 15.8 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0907× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~44% of this change |
| [[RPMI-7951 (line)]] | alt | 12.6 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0819× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~30% of this change |
| [[AsPC-1 (line)]] | alt | 18.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -9.4) ⚠ cell-cycle shift, explains ~60% of this change |
| [[C32 (line)]] | wt | 18.0 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0708× (z -11.9) |
| [[H4 (line)]] | wt | 8.89 | 0 | 1 | — | [[Peretinoin (drug)]] 0.5 µM 0.0701× (z -8.6) |
| [[HCT15 (line)]] | alt | 7.31 | 0 | 1 | — | [[Ataluren (drug)]] 0.5 µM 0.0623× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 8.79 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -9.2) ⚠ cell-cycle shift, explains ~60% of this change |
| [[HOP62 (line)]] | alt | 7.67 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.129× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[HS-578T (line)]] | alt | 6.68 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.105× (z -8.5) ⚠ cell-cycle shift, explains ~33% of this change |
| [[HT-29 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -13.3) ⚠ cell-cycle shift, explains ~60% of this change |
| [[KATO III (line)]] | alt | 6.35 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0749× (z -10.0) |
| [[LoVo (line)]] | wt | 13.9 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.168× (z -10.5) ⚠ unreliable plate only |
| [[MIA PaCa-2 (line)]] | alt | 13.3 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 1.87× (z +10.0) ⚠ position not correctable | — |
| [[NCI-H1573 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.181× (z -9.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[NCI-H2030 (line)]] | alt | 19.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.231× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 16.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.246× (z -10.6) ⚠ cell-cycle shift, explains ~60% of this change |
| [[SNU-1 (line)]] | wt | 28.6 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.166× (z -8.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[SNU-423 (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -8.5) ⚠ cell-cycle shift, explains ~39% of this change |
| [[A-427 (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.80 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.60 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 5.39 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.47 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.74 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 289), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*32 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK3]] | +0.58 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[LRP1]] | +0.55 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[HCN3]] | +0.55 | +0.40 / +0.59 | both halves | 5e-05 |  |
| [[DDR1]] | +0.54 | +0.44 / +0.57 | both halves | 3e-05 |  |
| [[MXD1]] | +0.54 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[OPTN]] | +0.53 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[MICA]] | +0.53 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[MED25]] | +0.52 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[BMF]] | +0.52 | +0.43 / +0.50 | both halves | 3e-05 |  |
| [[NDRG2]] | +0.51 | +0.34 / +0.49 | both halves | 1e-04 |  |
| [[TSC22D4]] | +0.51 | +0.54 / +0.53 | both halves | 1e-05 |  |
| [[ACAA1]] | +0.50 | +0.38 / +0.45 | both halves | 6e-05 |  |

## Genes that move opposite

*68 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR4]] | -0.58 | -0.63 / -0.52 | both halves | 1e-05 |  |
| [[MECR]] | -0.58 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[FAF1]] | -0.58 | -0.63 / -0.53 | both halves | 1e-05 |  |
| [[POLR1A]] | -0.57 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[TSEN2]] | -0.56 | -0.60 / -0.51 | both halves | 1e-05 |  |
| [[URB2]] | -0.56 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[CMSS1]] | -0.56 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[PINX1]] | -0.55 | -0.62 / -0.50 | both halves | 1e-05 |  |
| [[ATR]] | -0.55 | -0.64 / -0.51 | both halves | 1e-05 |  |
| [[NDUFAF2]] | -0.55 | -0.58 / -0.47 | both halves | 2e-05 |  |
| [[GNL3L]] | -0.55 | -0.64 / -0.48 | both halves | 2e-05 |  |
| [[TANGO6]] | -0.53 | -0.57 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 1, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CASP10]] | B | CASP10 activity raises MTMR11's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 1.30× lower at baseline in the lines without CASP10 | 0.069 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[MTHFD1L]] | C | MTHFD1L activity lowers MTMR11's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 2.76× higher at baseline in the lines without MTHFD1L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |
| [[LRP1]] | C | LRP1 activity raises MTMR11's level | lines that do not express LRP1 (3) vs lines expressing it (47) | 2.61× lower at baseline in the lines without LRP1 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OAF, TGFBR3, OSBPL3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **-** arm (projection on the module's main direction -0.549). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-13.3, -36.8); signed map (-10.6, 13.0). **Vector** length 75.3, 14.4% of its response variance represented; |z| ≥ 3 in 1,161 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.6 | +2.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +1.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | -2.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +2.1 | +4.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.0 | +5.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.0 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | -1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +2.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.8 | +2.9 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.5 | -7.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.2 | -8.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -7.1 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.3 | -3.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~47% of this change | -2.3 | -3.6 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -7.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Afatinib (drug)]] 0.5 µM |  | -1.8 | -1.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -1.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | myotubularin related protein 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.2 — chr1:149,928,651-149,936,879 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CRA |
| Gene groups (HGNC) | Myotubularins |
| Matched by | ensembl_id |

UniProt [A4FU01](https://www.uniprot.org/uniprotkb/A4FU01) carries no function annotation.

**Summary**, from NCBI Gene [10903](https://www.ncbi.nlm.nih.gov/gene/10903):

> Located in cytoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24307](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24307) · Entrez [10903](https://www.ncbi.nlm.nih.gov/gene/10903) · UniProt [A4FU01](https://www.uniprot.org/uniprotkb/A4FU01) · Ensembl [ENSG00000014914](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000014914)

## Data

Gene col 289: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 289); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 289, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 289]; `tensor/DDL_lfc|DDL_z.npy` [289]; `embed/gene_vectors.npy` [289]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 289 or target_col == 289). Every well: [[MTMR11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MTMR11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
