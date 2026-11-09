---
symbol: "TRAP1"
type: "gene"
col: 4748
ensembl_id: "ENSG00000126602"
name: "TNF receptor associated protein 1"
location: "16p13.3"
module: 18
arm: "+"
pooled_cpm: 59.51
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 18
n_dd_up_clean: 5
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/018"]
generated_by: "tahoemap"
---

# TRAP1

*TNF receptor associated protein 1* — 16p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.12× (z +21.2, q 0e+00, up in 41 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.14× (z +5.0, q 3e-05, up in 9 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.572× (z -22.5, q 0e+00, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CARNMT1]] (+0.77, fdr 7e-06), [[ATAD3A]] (+0.75, fdr 7e-06), [[URB1]] (+0.75, fdr 7e-06); moves opposite to [[ARID4B]] (-0.63, fdr 2e-05), [[WBP4]] (-0.60, fdr 3e-05), [[KANSL1L]] (-0.60, fdr 4e-05).
> It sits in the **+** arm of [[Module 018]] (Nucleotide biosynthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TERT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4748.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.12×** | +21.2 | 0e+00 | 41/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.77×** | +15.5 | 0e+00 | 39/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.65×** | +13.1 | 6e-37 | 32/45 (KATO III, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +9.7 | 6e-20 | 34/48 (AsPC-1, NCI-H460, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.39×** | +9.4 | 8e-19 | 32/48 (NCI-H1573, A-172, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.36×** | +8.7 | 3e-16 | 31/48 (NCI-H1573, A-172, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.26×** | +6.4 | 1e-08 | 23/48 (NCI-H1573, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.14× | +5.0 | 3e-05 | 9/48 (NCI-H2030, LOX-IMVI, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.40×** | +4.9 | 5e-05 | 20/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.38×** | +4.8 | 1e-04 | 16/48 (AsPC-1, PANC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **1.38×** | +4.7 | 1e-04 | 14/48 (MIA PaCa-2, AsPC-1, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.004 | 6/48 (NCI-H460, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.15× | +3.9 | 0.004 | 11/48 (NCI-H1792, SW 900, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | 1.12× | +3.2 | 0.050 | 8/48 (NCI-H1573, HOP62, …) | rises with dose |  |
| [[venetoclax (drug)]] 5 µM |  | **1.24×** | +3.1 | 0.061 | 9/48 (NCI-H460, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | 1.12× | +3.1 | 0.061 | 8/48 (LOX-IMVI, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4748.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.572×** | -22.5 | 0e+00 | 37/48 (PANC-1, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.541×** | -17.5 | 0e+00 | 43/48 (PANC-1, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.589×** | -15.1 | 0e+00 | 35/48 (SNU-1, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.733×** | -12.5 | 7e-34 | 30/48 (RKO, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.699×** | -10.2 | 2e-22 | 30/48 (RKO, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.780×** | -10.1 | 8e-22 | 28/48 (SNU-1, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.712×** | -9.7 | 3e-20 | 29/48 (C32, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.722×** | -9.3 | 1e-18 | 29/48 (C-33 A, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.723×** | -8.9 | 3e-17 | 33/48 (PANC-1, J82, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.750×** | -8.2 | 1e-14 | 26/48 (RKO, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.825×** | -7.8 | 4e-13 | 26/48 (LS 180, LoVo, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.770×** | -7.5 | 4e-12 | 29/48 (SW48, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.613×** | -7.2 | 2e-11 | 25/49 (A498, SW1417, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.792×** | -6.7 | 1e-09 | 22/48 (LoVo, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.668×** | -6.0 | 1e-07 | 22/48 (LoVo, LS 180, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.832×** | -5.1 | 1e-05 | 22/47 (LoVo, C-33 A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4748. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 96.5 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -19.7) |
| [[LoVo (line)]] | wt | 72.6 | 3 (3 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.14× (z +14.5) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.447× (z -10.2) |
| [[NCI-H1573 (line)]] | alt | 48.9 | 6 (6 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.65× (z +13.8) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.424× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 64.6 | 4 (4 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 3.70× (z +18.1) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.504× (z -13.6) |
| [[PANC-1 (line)]] | alt | 64.6 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.314× (z -23.4) |
| [[SW480 (line)]] | alt | 83.5 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.30× (z +16.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.473× (z -14.8) |
| [[MIA PaCa-2 (line)]] | alt | 83.0 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +12.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.401× (z -15.7) |
| [[SNU-1 (line)]] | wt | 78.2 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0592× (z -23.5) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.295× (z -14.3) |
| [[A498 (line)]] | wt | 79.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -18.1) |
| [[HT-29 (line)]] | alt | 42.1 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.78× (z +12.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.503× (z -8.9) |
| [[SW1417 (line)]] | alt | 56.7 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -19.1) |
| [[AsPC-1 (line)]] | alt | 54.9 | 1 (1 ⚠) | 2 | [[c-Kit-IN-1 (drug)]] 0.05 µM 3.02× (z +10.0) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -19.8) |
| [[BT-474 (line)]] | alt | 60.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -14.9) |
| [[C32 (line)]] | wt | 47.6 | 0 | 3 | — | [[Auranofin (drug)]] 5 µM 0.277× (z -10.5) |
| [[HOP62 (line)]] | alt | 34.1 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.48× (z +8.7) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.296× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.410× (z -8.6) |
| [[J82 (line)]] | alt | 62.9 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.461× (z -12.1) |
| [[KATO III (line)]] | alt | 64.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.94× (z +13.7) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 65.0 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.76× (z +13.2) ⚠ toxic; transcription drop | [[Selinexor (drug)]] 5 µM 0.431× (z -11.9) |
| [[SNU-423 (line)]] | alt | 32.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 51.6 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.368× (z -10.7) |
| [[A549 (line)]] | wt | 59.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.69× (z +13.0) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.523× (z -9.1) |
| [[AN3 CA (line)]] | alt | 61.4 | 0 | 2 | — | [[Silodosin (drug)]] 5 µM 0.160× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 31.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.54× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 70.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.48× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.578× (z -10.0) |
| [[Hs 766T (line)]] | wt | 63.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +10.1) ⚠ toxic; transcription drop | — |
| [[LOX-IMVI (line)]] | wt | 50.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.98× (z +10.8) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 47.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +12.6) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 49.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 2.88× (z +9.3) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 5 µM 0.356× (z -9.1) |
| [[SW 900 (line)]] | alt | 35.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.26× (z +9.9) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -9.5) |
| [[SW48 (line)]] | wt | 148 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.443× (z -11.1) |
| [[A-427 (line)]] | wt | 83.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.415× (z -14.2) |
| [[C-33 A (line)]] | alt | 122 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.386× (z -9.4) |
| [[HCT15 (line)]] | alt | 80.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +11.4) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 42.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.01× (z +8.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 48.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.64× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 64.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.439× (z -9.4) |
| [[NCI-H2347 (line)]] | alt | 29.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 66.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.358× (z -10.1) ⚠ toxic; transcription drop |
| [[CHP-212 (line)]] | wt | 80.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 59.7 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 33.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 58.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 34.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4748), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CARNMT1]] | +0.77 | +0.72 / +0.77 | both halves | 7e-06 |  |
| [[ATAD3A]] | +0.75 | +0.74 / +0.69 | both halves | 7e-06 |  |
| [[URB1]] | +0.75 | +0.73 / +0.81 | both halves | 7e-06 |  |
| [[CAD]] | +0.73 | +0.70 / +0.76 | both halves | 7e-06 | STRING 418 |
| [[MYBBP1A]] | +0.71 | +0.71 / +0.70 | both halves | 7e-06 |  |
| [[DKC1]] | +0.70 | +0.72 / +0.66 | both halves | 7e-06 |  |
| [[BOP1]] | +0.70 | +0.65 / +0.65 | both halves | 7e-06 |  |
| [[MDN1]] | +0.69 | +0.67 / +0.75 | both halves | 7e-06 |  |
| [[TCOF1]] | +0.69 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[NSUN2]] | +0.69 | +0.75 / +0.69 | both halves | 7e-06 |  |
| [[ATAD3B]] | +0.68 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[POLR1B]] | +0.68 | +0.72 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARID4B]] | -0.63 | -0.47 / -0.62 | both halves | 2e-05 |  |
| [[WBP4]] | -0.60 | -0.60 / -0.45 | both halves | 3e-05 |  |
| [[KANSL1L]] | -0.60 | -0.54 / -0.41 | both halves | 4e-05 |  |
| [[SUPT7L]] | -0.60 | -0.49 / -0.55 | both halves | 2e-05 |  |
| [[LINC02307]] | -0.59 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[SYNRG]] | -0.59 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[IFNAR1]] | -0.59 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[ZNF846]] | -0.58 | -0.55 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TERT]] | B | TERT activity raises TRAP1's level | lines that do not express TERT (13) vs lines expressing it (37) | 1.33× lower at baseline in the lines without TERT | 0.007 | ⚠ within organs, on part of the lines; also absent: SAMD11, MIR1915HG, LNC-LBCS |
| [[NT5M]] | B | NT5M activity raises TRAP1's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without NT5M | 0.013 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[MCOLN2]] | B | MCOLN2 activity raises TRAP1's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.23× lower at baseline in the lines without MCOLN2 | 0.071 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 018]] — Nucleotide biosynthesis; 197 genes; this gene is in the **+** arm (projection on the module's main direction 0.629). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-11.6, -37.3); signed map (-5.4, -50.9). **Vector** length 127, 37.9% of its response variance represented; |z| ≥ 3 in 1,226 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Nucleotide biosynthesis* (reactome, mean cos +0.64 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +8.6 | +9.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | +5.1 | +9.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +5.0 | +6.4 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +4.4 | +8.7 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +4.1 | +4.9 |
|  | [[EX229 (drug)]] 5 µM |  | +4.0 | +4.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.5 | +2.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.4 | +4.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.1 | +3.9 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -9.8 | -12.5 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.3 | -7.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -6.9 | -8.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.7 | -10.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.5 | -22.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.4 | -5.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.3 | -2.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | -3.8 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | TNF receptor associated protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p13.3 — chr16:3,651,639-3,717,553 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HSP75, HSP90L |
| Gene groups (HGNC) | Heat shock 90kDa proteins |
| Reactome | 3 pathways, smallest: Citric acid cycle (TCA cycle); Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12931](https://www.uniprot.org/uniprotkb/Q12931) (Heat shock protein 75 kDa, mitochondrial):

> Chaperone that expresses an ATPase activity. Involved in maintaining mitochondrial function and polarization, downstream of PINK1 and mitochondrial complex I. Is a negative regulator of mitochondrial respiration able to modulate the balance between oxidative phosphorylation and aerobic glycolysis. The impact of TRAP1 on mitochondrial respiration is probably mediated by modulation of mitochondrial SRC and inhibition of SDHA.

**Summary**, from NCBI Gene [10131](https://www.ncbi.nlm.nih.gov/gene/10131):

> This gene encodes a mitochondrial chaperone protein that is member of the heat shock protein 90 (HSP90) family. The encoded protein has ATPase activity and interacts with tumor necrosis factor type I. This protein may function in regulating cellular stress responses. Alternate splicing results in multiple transcript variants. [provided by RefSeq, Jan 2013]

**Accessions** — [HGNC:16264](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16264) · Entrez [10131](https://www.ncbi.nlm.nih.gov/gene/10131) · UniProt [Q12931](https://www.uniprot.org/uniprotkb/Q12931) · Ensembl [ENSG00000126602](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126602)

## Data

Gene col 4748: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4748); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4748, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4748]; `tensor/DDL_lfc|DDL_z.npy` [4748]; `embed/gene_vectors.npy` [4748]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4748 or target_col == 4748). Every well: [[TRAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
