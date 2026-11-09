---
symbol: "LNX2"
type: "gene"
col: 6313
ensembl_id: "ENSG00000139517"
name: "ligand of numb-protein X 2"
location: "13q12.2"
module: 130
arm: "+"
pooled_cpm: 57.35
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 14
n_dd_up_clean: 13
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/130"]
generated_by: "tahoemap"
---

# LNX2

*ligand of numb-protein X 2* — 13q12.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.64× (z +23.0, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.456× (z -12.7, q 5e-34, down in 30 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.645× (z -7.4, q 2e-11, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TAPT1]] (+0.72, fdr 7e-06), [[TBC1D12]] (+0.67, fdr 1e-05), [[TXNDC16]] (+0.65, fdr 7e-06); moves opposite to [[CLPB]] (-0.74, fdr 7e-06), [[POLR1A]] (-0.65, fdr 1e-05), [[LSG1]] (-0.63, fdr 7e-06).
> It is in [[Module 130]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6313.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.64×** | +23.0 | 0e+00 | 46/48 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.39×** | +20.6 | 0e+00 | 45/49 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.84×** | +9.8 | 2e-20 | 39/47 (RKO, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.70×** | +8.8 | 1e-16 | 34/48 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +8.7 | 3e-16 | 36/50 (C32, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.69×** | +8.7 | 3e-16 | 43/48 (LOX-IMVI, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.67×** | +8.3 | 1e-14 | 37/48 (COLO 205, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +8.1 | 3e-14 | 41/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +6.2 | 4e-08 | 32/47 (COLO 205, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.38×** | +5.3 | 5e-06 | 26/48 (LOX-IMVI, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.32×** | +4.6 | 3e-04 | 24/48 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **1.59×** | +4.0 | 0.002 | 20/49 (LOX-IMVI, RKO, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.25×** | +3.8 | 0.007 | 19/48 (RKO, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.025 | 10/48 (NCI-H2347, SW1417, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.21×** | +3.2 | 0.048 | 19/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6313.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.456×** | -12.7 | 5e-34 | 30/38 (Hs 766T, HT-29, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.477×** | -12.4 | 6e-33 | 36/47 (SW 900, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.461×** | -12.0 | 5e-31 | 34/42 (NCI-H2347, J82, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.645×** | -7.4 | 2e-11 | 35/48 (A-172, AsPC-1, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.837× | -4.3 | 0.002 | 22/48 (HS-578T, SW1417, …) | rises with dose |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.780×** | -4.2 | 0.003 | 23/48 (SW480, RKO, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.786×** | -4.1 | 0.004 | 21/49 (RPMI-7951, A-172, …) | inconsistent across doses |  |
| [[Megestrol (drug)]] 0.05 µM |  | **0.788×** | -4.0 | 0.004 | 25/48 (SW 900, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.788×** | -4.0 | 0.004 | 21/48 (SW 900, SHP-77, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.862× | -3.5 | 0.022 | 15/48 (Hs 766T, NCI-H2347, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~13% of this change | **0.820×** | -3.4 | 0.038 | 23/47 (SW1417, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.821×** | -3.3 | 0.038 | 15/48 (A498, Panc 03.27, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.821×** | -3.3 | 0.038 | 14/49 (HS-578T, A-172, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.821×** | -3.2 | 0.056 | 17/48 (NCI-H2347, SW 900, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.829×** | -3.2 | 0.058 | 17/49 (SW 900, KATO III, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.830×** | -3.1 | 0.058 | 15/48 (A498, Panc 03.27, …) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.833× | -3.1 | 0.069 | 16/49 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.839× | -3.0 | 0.093 | 14/49 (SW 900, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6313. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 95.7 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.97× (z +20.2) | [[Dinaciclib (drug)]] 0.5 µM 0.265× (z -13.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 26.4 | 6 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.61× (z +25.4) | — |
| [[Panc 03.27 (line)]] | alt | 106 | 2 | 4 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +11.1) | [[Dinaciclib (drug)]] 5 µM 0.212× (z -14.2) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 78.0 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +18.8) | [[Dinaciclib (drug)]] 0.5 µM 0.275× (z -17.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 34.3 | 3 | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.01× (z +16.0) | [[Dinaciclib (drug)]] 5 µM 0.250× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.288× (z -10.2) |
| [[C32 (line)]] | wt | 53.9 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.95× (z +16.0) | — |
| [[COLO 205 (line)]] | alt | 193 | 4 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.07× (z +27.0) | [[Dinaciclib (drug)]] 0.5 µM 0.281× (z -12.4) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 67.0 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +13.6) | [[Dinaciclib (drug)]] 5 µM 0.233× (z -12.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 242 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.44× (z +17.1) | [[Dinaciclib (drug)]] 5 µM 0.146× (z -18.1) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 29.8 | 5 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.86× (z +17.6) | — |
| [[A498 (line)]] | wt | 62.2 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.70× (z +14.3) | [[Dinaciclib (drug)]] 5 µM 0.175× (z -13.0) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 65.1 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +11.5) | [[Dinaciclib (drug)]] 5 µM 0.156× (z -15.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.364× (z -8.5) |
| [[Hs 766T (line)]] | wt | 59.8 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.08× (z +13.0) | [[Dinaciclib (drug)]] 5 µM 0.0448× (z -24.8) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 46.8 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.25× (z +16.6) | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -15.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 66.0 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.27× (z +22.4) | [[Dinaciclib (drug)]] 5 µM 0.256× (z -14.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 82.7 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.13× (z +15.8) | [[Dinaciclib (drug)]] 0.05 µM 0.383× (z -8.8) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 89.1 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.86× (z +10.0) | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -22.9) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 43.9 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +17.9) | — |
| [[SW1417 (line)]] | alt | 94.7 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +14.1) | [[Dinaciclib (drug)]] 0.05 µM 0.262× (z -13.1) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 36.2 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +17.6) | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -15.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 37.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +16.2) | — |
| [[A-427 (line)]] | wt | 30.2 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.05× (z +10.3) | — |
| [[A549 (line)]] | wt | 32.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.77× (z +12.9) | — |
| [[CFPAC-1 (line)]] | alt | 41.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +12.3) | [[Dinaciclib (drug)]] 0.5 µM 0.337× (z -10.0) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 101 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.92× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.379× (z -8.9) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 27.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +14.2) | — |
| [[hTERT-HPNE (line)]] | wt | 35.7 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +11.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 43.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.08× (z +14.4) | — |
| [[SNU-1 (line)]] | wt | 47.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.59× (z +12.1) | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -9.5) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 38.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.25× (z +12.7) | — |
| [[SW 900 (line)]] | alt | 77.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -19.5) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 56.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +10.6) | — |
| [[BT-474 (line)]] | alt | 69.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.254× (z -10.0) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 67.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +11.5) | — |
| [[HS-578T (line)]] | alt | 31.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -9.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 22.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +11.3) | — |
| [[RPMI-7951 (line)]] | alt | 27.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +11.6) | — |
| [[SHP-77 (line)]] | alt | 44.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.82× (z +10.6) | — |
| [[SK-MEL-2 (line)]] | alt | 30.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +13.1) | — |
| [[SW 1271 (line)]] | alt | 61.6 | 0 | 1 | — | [[Pasireotide (acetate) (drug)]] 0.5 µM 0.0663× (z -10.0) |
| [[AN3 CA (line)]] | alt | 51.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 38.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 34.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 34.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6313), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*43 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TAPT1]] | +0.72 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[TBC1D12]] | +0.67 | +0.52 / +0.69 | both halves | 1e-05 |  |
| [[TXNDC16]] | +0.65 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[PPP2R5A]] | +0.64 | +0.56 / +0.72 | both halves | 1e-05 |  |
| [[PLEKHA1]] | +0.62 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[ELF2]] | +0.61 | +0.48 / +0.61 | both halves | 2e-05 |  |
| [[PIK3CA]] | +0.60 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[CNOT6L]] | +0.60 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[CMC4]] | +0.60 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[PAIP2B]] | +0.59 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[RSRP1]] | +0.59 | +0.60 / +0.54 | both halves | 1e-05 |  |
| [[ARID4A]] | +0.59 | +0.58 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*57 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CLPB]] | -0.74 | -0.72 / -0.70 | both halves | 7e-06 |  |
| [[POLR1A]] | -0.65 | -0.67 / -0.57 | both halves | 1e-05 |  |
| [[LSG1]] | -0.63 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[EFTUD2]] | -0.63 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[EIPR1]] | -0.62 | -0.69 / -0.59 | both halves | 7e-06 |  |
| [[RRP7BP-1]] | -0.61 | -0.67 / -0.54 | both halves | 1e-05 |  |
| [[TANGO6]] | -0.61 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[NUDC]] | -0.60 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[ZNF8]] | -0.60 | -0.52 / -0.63 | both halves | 1e-05 |  |
| [[UTP11]] | -0.59 | -0.49 / -0.57 | both halves | 1e-05 |  |
| [[NOL10]] | -0.59 | -0.59 / -0.58 | both halves | 7e-06 |  |
| [[CCT2]] | -0.59 | -0.48 / -0.57 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LNX2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TP53]] | C | TP53 activity strengthens LNX2's drug response | recorded loss-of-function mutation of TP53 in 33 lines vs 17 not recorded | the TP53-altered lines respond 0.88× as strongly (z diff +0.27); strongest at Epirubicin (hydrochloride) 5 µM: 1.54x vs 2.33x (z diff +2.5) | 0.709 over the table, 0.045 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 130]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.655). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (2.2, -25.9); signed map (-21.8, 15.9). **Vector** length 99.1, 28.3% of its response variance represented; |z| ≥ 3 in 1,107 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.9 | +20.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +9.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +4.8 | +8.7 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.5 | +2.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.3 | +6.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.0 | +1.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.0 | +1.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[Retinoic acid (drug)]] 5 µM |  | +1.8 | +2.1 |
| fall | [[Auranofin (drug)]] 5 µM |  | -8.0 | -7.4 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -6.0 | -0.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.7 | -12.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -5.4 | -2.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -5.4 | -0.2 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.6 | -1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.4 | +2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | ligand of numb-protein X 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q12.2 — chr13:27,545,913-27,620,529 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC46315; previously PDZRN1 |
| Gene groups (HGNC) | Ring finger proteins; PDZ domain containing; RING finger E3 ubiquitin protein ligases |
| Matched by | ensembl_id |

UniProt [Q8N448](https://www.uniprot.org/uniprotkb/Q8N448) carries no function annotation.

**Summary**, from NCBI Gene [222484](https://www.ncbi.nlm.nih.gov/gene/222484):

> Enables identical protein binding activity. Predicted to be involved in nervous system development. Predicted to act upstream of or within neural precursor cell proliferation and neuron differentiation. Predicted to be located in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20421](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20421) · Entrez [222484](https://www.ncbi.nlm.nih.gov/gene/222484) · UniProt [Q8N448](https://www.uniprot.org/uniprotkb/Q8N448) · Ensembl [ENSG00000139517](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139517)

## Data

Gene col 6313: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6313); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6313, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6313]; `tensor/DDL_lfc|DDL_z.npy` [6313]; `embed/gene_vectors.npy` [6313]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6313 or target_col == 6313). Every well: [[LNX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LNX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
