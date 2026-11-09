---
symbol: "NOC2L"
type: "gene"
col: 12069
ensembl_id: "ENSG00000188976"
name: "NOC2 like nucleolar associated transcriptional repressor"
location: "1p36.33"
module: 4
arm: "+"
pooled_cpm: 34.02
n_lines_expressing: 50
n_dd_up: 48
n_dd_down: 2
n_dd_up_clean: 24
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/004"]
generated_by: "tahoemap"
---

# NOC2L

*NOC2 like nucleolar associated transcriptional repressor* — 1p36.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 48 drug-doses (24 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.59× (z +21.1, q 0e+00, up in 48 of 48 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.70× (z +8.8, q 1e-16, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 0.734× (z -4.9, q 5e-04, down in 24 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.179×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MYBBP1A]] (+0.79, fdr 7e-06), [[BOP1]] (+0.77, fdr 7e-06), [[CHID1]] (+0.75, fdr 7e-06); moves opposite to [[ZMYM5]] (-0.65, fdr 1e-05), [[PNRC1]] (-0.63, fdr 1e-05), [[ARID4B]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 004]] (MYC targets v1).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 50 in all, 25 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 48 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 24 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12069.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **3.59×** | +21.1 | 0e+00 | 48/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **3.37×** | +20.0 | 0e+00 | 48/48 (SW480, RKO, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **2.80×** | +17.0 | 0e+00 | 48/48 (SW480, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.72×** | +16.6 | 0e+00 | 42/45 (NCI-H460, SW480, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **2.51×** | +14.6 | 0e+00 | 37/40 (LoVo, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.07×** | +11.1 | 1e-26 | 37/43 (MIA PaCa-2, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.89×** | +10.5 | 1e-23 | 42/48 (NCI-H460, NCI-H1792, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.73×** | +9.1 | 9e-18 | 37/48 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.70×** | +8.8 | 1e-16 | 40/48 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~55% of this change | **1.67×** | +8.5 | 1e-15 | 39/46 (PANC-1, NCI-H2030, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.58×** | +7.5 | 3e-12 | 36/48 (NCI-H460, HOP62, …) | all doses, flat | cell-cycle shift (explains ~19% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.57×** | +7.4 | 5e-12 | 37/48 (PANC-1, HOP62, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.55×** | +7.2 | 3e-11 | 34/48 (MIA PaCa-2, SW480, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.51×** | +6.8 | 4e-10 | 35/47 (LoVo, LS 180, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.47×** | +6.3 | 1e-08 | 28/47 (NCI-H460, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.96×** | +5.8 | 2e-07 | 29/47 (RKO, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +5.6 | 5e-07 | 26/48 (HOP62, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +5.1 | 8e-06 | 26/48 (NCI-H2347, SNU-423, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.80×** | +5.1 | 9e-06 | 25/48 (PANC-1, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **1.76×** | +4.9 | 2e-05 | 26/48 (NCI-H460, HT-29, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.33×** | +4.5 | 1e-04 | 19/48 (NCI-H1792, NCI-H1573, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +4.4 | 2e-04 | 25/48 (NCI-H460, LOX-IMVI, …) | all doses, flat |  |
| [[EX229 (drug)]] 0.05 µM |  | **1.32×** | +4.3 | 3e-04 | 21/48 (LoVo, RKO, …) | all doses, flat | position effect removed |
| [[Abemaciclib (drug)]] 5 µM |  | **1.59×** | +4.0 | 0.001 | 16/48 (SW480, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.57×** | +3.9 | 0.001 | 17/46 (NCI-H1573, NCI-H460, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12069.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (RKO 0.179×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **0.734×** | -4.9 | 5e-04 | 24/47 (SW480, NCI-H23, …) | rises with dose | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.786×** | -4.0 | 0.020 | 18/48 (A-172, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | 0.862× | -3.4 | 0.13 | 15/48 (C-33 A, LoVo, …) | all doses, flat | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | 0.876× | -3.1 | 0.20 | 12/48 (HCT15, J82, …) | rises with dose | position effect removed |
| [[Adagrasib (drug)]] 5 µM |  | 0.825× | -3.1 | 0.20 | 10/48 (A-427, KATO III, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | 0.701× | -3.1 | 0.20 | 9/47 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.58 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12069. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 22.4 | 8 (7 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.38× (z +18.6) ⚠ cell-cycle shift, explains ~84% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 4.36× (z +11.5) | — |
| [[SW480 (line)]] | alt | 38.7 | 7 (7 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.04× (z +14.1) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[HOP62 (line)]] | alt | 27.5 | 6 (6 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.40× (z +12.2) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 41.2 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.96× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[PANC-1 (line)]] | alt | 49.3 | 6 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.00× (z +11.3) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.58× (z +9.7) | — |
| [[KATO III (line)]] | alt | 28.7 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.85× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[LoVo (line)]] | wt | 32.9 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.10× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[NCI-H1573 (line)]] | alt | 24.6 | 5 (5 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.14× (z +12.8) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[LS 180 (line)]] | wt | 34.8 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.60× (z +11.4) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[SNU-423 (line)]] | alt | 18.5 | 4 (4 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.25× (z +11.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HS-578T (line)]] | alt | 43.0 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.95× (z +11.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1792 (line)]] | alt | 23.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.84× (z +11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[NCI-H2347 (line)]] | alt | 30.5 | 3 (3 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.10× (z +12.1) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[RKO (line)]] | wt | 53.0 | 2 (2 ⚠) | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 4.58× (z +12.3) ⚠ cell-cycle shift, explains ~28% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.179× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change |
| [[A498 (line)]] | wt | 26.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.22× (z +9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[A549 (line)]] | wt | 20.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.96× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[CFPAC-1 (line)]] | alt | 30.0 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.49× (z +9.9) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[COLO 205 (line)]] | alt | 17.3 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 7.64× (z +10.1) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[HEC-1-A (line)]] | alt | 37.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.70× (z +11.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[Hs 766T (line)]] | wt | 28.8 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.64× (z +9.7) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2030 (line)]] | alt | 45.4 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.47× (z +9.6) ⚠ cell-cycle shift, explains ~48% of this change | — |
| [[Panc 03.27 (line)]] | alt | 19.7 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.72× (z +10.1) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[SHP-77 (line)]] | alt | 66.7 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 2.86× (z +8.9) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[AsPC-1 (line)]] | alt | 20.8 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.38× (z +9.4) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[BT-474 (line)]] | alt | 29.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.62× (z +8.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[H4 (line)]] | wt | 45.4 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.99× (z +8.5) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[HCT15 (line)]] | alt | 37.9 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.98× (z +8.6) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[HepG2_C3A (line)]] | wt | 31.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.67× (z +8.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[J82 (line)]] | alt | 37.6 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.74× (z +8.8) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H23 (line)]] | alt | 69.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.95× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[SNU-1 (line)]] | wt | 34.0 | 1 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 4.76× (z +9.0) ⚠ cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 43.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 45.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 27.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 24.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 56.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 56.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12069), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYBBP1A]] | +0.79 | +0.80 / +0.78 | both halves | 7e-06 | same gene group; STRING 911 |
| [[BOP1]] | +0.77 | +0.75 / +0.73 | both halves | 7e-06 | STRING 998 |
| [[CHID1]] | +0.75 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[EFTUD2]] | +0.75 | +0.67 / +0.75 | both halves | 7e-06 | STRING 496 |
| [[TCOF1]] | +0.73 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[LAS1L]] | +0.73 | +0.66 / +0.73 | both halves | 7e-06 | STRING 663 |
| [[NOP9]] | +0.72 | +0.72 / +0.67 | both halves | 7e-06 | same gene group; STRING 916 |
| [[ELAC2]] | +0.70 | +0.61 / +0.74 | both halves | 7e-06 | STRING 422 |
| [[URB1]] | +0.70 | +0.67 / +0.72 | both halves | 7e-06 | same gene group; STRING 765 |
| [[E2F4]] | +0.69 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[POLR1A]] | +0.69 | +0.67 / +0.71 | both halves | 7e-06 | STRING 911 |
| [[TBL3]] | +0.68 | +0.69 / +0.67 | both halves | 7e-06 | STRING 985 |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZMYM5]] | -0.65 | -0.54 / -0.65 | both halves | 1e-05 |  |
| [[PNRC1]] | -0.63 | -0.52 / -0.62 | both halves | 1e-05 |  |
| [[ARID4B]] | -0.60 | -0.51 / -0.53 | both halves | 1e-05 |  |
| [[PIGP]] | -0.59 | -0.47 / -0.50 | both halves | 2e-05 |  |
| [[TERF2IP]] | -0.58 | -0.44 / -0.58 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers NOC2L's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.4% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 004]] — MYC targets v1; 245 genes; this gene is in the **+** arm (projection on the module's main direction 0.670). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-18.8, -31.5); signed map (-8.5, -45.7). **Vector** length 79.9, 20.4% of its response variance represented; |z| ≥ 3 in 1,174 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.4 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | +4.2 | +16.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | +4.1 | +14.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.9 | +21.1 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.7 | +20.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.2 | +4.5 |
|  | [[EX229 (drug)]] 5 µM |  | +2.8 | +4.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +5.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | +5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.1 | +4.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | -4.5 | +4.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~78% of this change | -3.3 | +3.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | -1.8 |
|  | [[Adagrasib (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.3 | +6.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.2 | -1.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.9 | -2.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | -4.9 |
|  | [[Terfenadine (drug)]] 5 µM |  | -1.8 | -0.7 |

## What is on record

|  |  |
|---|---|
| Name | NOC2 like nucleolar associated transcriptional repressor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.33 — chr1:944,203-959,309 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP564C186, NET7, NET15, NIR, PPP1R112 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Armadillo like helical domain containing |
| Reactome | 3 pathways, smallest: Regulation of TP53 Activity through Phosphorylation; Regulation of TP53 Activity; Transcriptional Regulation by TP53 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y3T9](https://www.uniprot.org/uniprotkb/Q9Y3T9) (Nucleolar complex protein 2 homolog):

> Acts as an inhibitor of histone acetyltransferase activity; prevents acetylation of all core histones by the EP300/p300 histone acetyltransferase at p53/TP53-regulated target promoters in a histone deacetylases (HDAC)-independent manner. Acts as a transcription corepressor of p53/TP53- and TP63-mediated transactivation of the p21/CDKN1A promoter. Involved in the regulation of p53/TP53-dependent apoptosis. Associates together with TP63 isoform TA*-gamma to the p21/CDKN1A promoter.

**Summary**, from NCBI Gene [26155](https://www.ncbi.nlm.nih.gov/gene/26155):

> Histone modification by histone acetyltransferases (HAT) and histone deacetylases (HDAC) can control major aspects of transcriptional regulation. NOC2L represents a novel HDAC-independent inhibitor of histone acetyltransferase (INHAT) (Hublitz et al., 2005 [PubMed 16322561]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:24517](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24517) · Entrez [26155](https://www.ncbi.nlm.nih.gov/gene/26155) · UniProt [Q9Y3T9](https://www.uniprot.org/uniprotkb/Q9Y3T9) · Ensembl [ENSG00000188976](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188976)

## Data

Gene col 12069: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12069); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12069, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12069]; `tensor/DDL_lfc|DDL_z.npy` [12069]; `embed/gene_vectors.npy` [12069]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12069 or target_col == 12069). Every well: [[NOC2L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NOC2L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
