---
symbol: "MCM7"
type: "gene"
col: 9323
ensembl_id: "ENSG00000166508"
name: "minichromosome maintenance complex component 7"
location: "7q22.1"
module: 6
arm: "+"
pooled_cpm: 41.27
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 22
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# MCM7

*minichromosome maintenance complex component 7* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (15 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.44× (z +17.9, q 0e+00, up in 45 of 45 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.21× (z +3.9, q 0.003, up in 20 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.755× (z -5.8, q 4e-06, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCM4]] (+0.79, fdr 7e-06), [[MCM5]] (+0.78, fdr 7e-06), [[MCM2]] (+0.77, fdr 7e-06); moves opposite to [[BLVRB]] (-0.65, fdr 9e-06), [[NDUFB4]] (-0.63, fdr 1e-05), [[SMIM26]] (-0.61, fdr 1e-05, ⚠ SMIM26 in the vector space only through flagged drug-doses), [[RBIS]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 006]] (E2F targets).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[CDC25A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9323.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **3.44×** | +17.9 | 0e+00 | 45/45 (SW480, A549, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.46×** | +17.3 | 0e+00 | 39/41 (LoVo, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **3.01×** | +14.8 | 0e+00 | 41/43 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.31×** | +13.4 | 2e-38 | 42/48 (PANC-1, SW480, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.55×** | +9.0 | 2e-17 | 30/48 (J82, A549, …) | top dose only | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **1.52×** | +8.5 | 1e-15 | 30/48 (NCI-H2347, C32, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.66×** | +7.1 | 1e-10 | 33/47 (C32, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.62×** | +7.0 | 2e-10 | 34/48 (PANC-1, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **1.52×** | +5.9 | 3e-07 | 30/48 (A549, C32, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.44×** | +5.3 | 8e-06 | 28/48 (NCI-H2030, J82, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.43×** | +5.2 | 9e-06 | 25/48 (PANC-1, LoVo, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.41×** | +4.8 | 9e-05 | 22/48 (MIA PaCa-2, SNU-423, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.33×** | +4.2 | 0.001 | 23/48 (NCI-H1792, C32, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~97% of this change | **1.33×** | +4.1 | 0.002 | 24/47 (A549, C32, …) | all doses, stronger at high dose | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.21×** | +3.9 | 0.003 | 20/48 (J82, NCI-H2347, …) | top dose only | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **1.54×** | +3.3 | 0.037 | 11/47 (LoVo, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.069 | 18/48 (NCI-H1792, C32, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9323.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.755×** | -5.8 | 4e-06 | 31/48 (KATO III, SK-MEL-2, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.679×** | -5.4 | 2e-05 | 26/47 (SW480, A-427, …) | rises with dose | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **0.785×** | -5.0 | 1e-04 | 30/48 (RKO, C-33 A, …) | rises with dose | position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.717×** | -4.8 | 2e-04 | 29/48 (RKO, A-427, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.731×** | -4.6 | 6e-04 | 24/48 (LoVo, RKO, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.738×** | -4.4 | 9e-04 | 26/48 (LS 180, C32, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | **0.733×** | -4.3 | 0.002 | 25/48 (LS 180, HCT15, …) | inconsistent across doses | position effect removed |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.815×** | -4.2 | 0.002 | 20/48 (J82, PANC-1, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.758×** | -4.0 | 0.004 | 20/48 (A-427, NCI-H23, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **0.765×** | -3.9 | 0.005 | 19/48 (A498, A-427, …) | two highest doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.765×** | -3.9 | 0.005 | 21/48 (A-427, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.804×** | -3.8 | 0.007 | 22/48 (A-427, SW480, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.765×** | -3.7 | 0.007 | 21/47 (PANC-1, RKO, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.773×** | -3.7 | 0.007 | 22/48 (LS 180, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.778×** | -3.6 | 0.010 | 22/48 (SW1417, KATO III, …) | rises with dose | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.824×** | -3.4 | 0.024 | 15/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.643×** | -3.4 | 0.024 | 18/48 (CHP-212, A498, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.797×** | -3.3 | 0.026 | 16/48 (SW 1088, RKO, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **0.648×** | -3.3 | 0.026 | 19/47 (C-33 A, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.851× | -3.3 | 0.028 | 20/48 (SW480, NCI-H23, …) | all doses, flat | position effect removed |
| [[Neratinib (drug)]] 5 µM |  | **0.815×** | -3.0 | 0.070 | 16/47 (C-33 A, PANC-1, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.50 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9323. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 70.9 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.81× (z +15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Cobimetinib (drug)]] 5 µM 0.408× (z -8.8) |
| [[A498 (line)]] | wt | 60.5 | 3 (3 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 3.48× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.264× (z -12.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 31.4 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.59× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HOP62 (line)]] | alt | 23.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 4.08× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[LoVo (line)]] | wt | 30.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.51× (z +13.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1792 (line)]] | alt | 22.3 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.23× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[PANC-1 (line)]] | alt | 47.2 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.13× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[SNU-423 (line)]] | alt | 27.7 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.71× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HS-578T (line)]] | alt | 27.4 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.72× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 43.1 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.92× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[NCI-H23 (line)]] | alt | 93.2 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.20× (z +12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -11.9) ⚠ cell-cycle shift, explains ~44% of this change |
| [[NCI-H2347 (line)]] | alt | 34.6 | 3 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +13.2) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[NCI-H460 (line)]] | wt | 25.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.68× (z +13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[A-427 (line)]] | wt | 53.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Selinexor (drug)]] 5 µM 0.352× (z -12.2) ⚠ cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 43.2 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +12.1) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[Hs 766T (line)]] | wt | 27.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[HT-29 (line)]] | alt | 35.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.07× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[LOX-IMVI (line)]] | wt | 28.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.04× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[LS 180 (line)]] | wt | 28.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.53× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | [[Selinexor (drug)]] 5 µM 0.368× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 32.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.42× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 67.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.81× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[AZD-7648 (drug)]] 5 µM 0.100× (z -9.1) |
| [[SW1417 (line)]] | alt | 57.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.01× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[BT-474 (line)]] | alt | 44.2 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.41× (z +8.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[C-33 A (line)]] | alt | 66.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.139× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change |
| [[CFPAC-1 (line)]] | alt | 18.8 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +8.8) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[HCT15 (line)]] | alt | 36.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.16× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[HEC-1-A (line)]] | alt | 44.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.36× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[J82 (line)]] | alt | 63.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.41× (z +12.8) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[KATO III (line)]] | alt | 52.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.91× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[NCI-H1573 (line)]] | alt | 18.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.28× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | — |
| [[RKO (line)]] | wt | 73.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.322× (z -9.2) ⚠ cell-cycle shift, would explain all of this change |
| [[RPMI-7951 (line)]] | alt | 32.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.86× (z +8.7) ⚠ cell-cycle shift, explains ~44% of this change | — |
| [[SHP-77 (line)]] | alt | 63.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.01× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | — |
| [[A-172 (line)]] | wt | 30.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 83.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 59.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9323), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM4]] | +0.79 | +0.80 / +0.79 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[MCM5]] | +0.78 | +0.73 / +0.77 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[MCM2]] | +0.77 | +0.79 / +0.75 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[POLE]] | +0.76 | +0.77 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 986 |
| [[MCM3]] | +0.74 | +0.74 / +0.75 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[HELLS]] | +0.74 | +0.70 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 490 |
| [[XRCC2]] | +0.72 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[MCM6]] | +0.72 | +0.71 / +0.72 | both halves | 7e-06 | same gene group; pathway: HALLMARK_E2F_TARGETS; STRING 999 |
| [[FANCG]] | +0.72 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[NCAPH2]] | +0.72 | +0.67 / +0.76 | both halves | 7e-06 |  |
| [[CENPH]] | +0.72 | +0.69 / +0.72 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[TMPO]] | +0.71 | +0.64 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 528 |

## Genes that move opposite

*8 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BLVRB]] | -0.65 | -0.57 / -0.67 | both halves | 9e-06 |  |
| [[NDUFB4]] | -0.63 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.61 | -0.53 / -0.58 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[RBIS]] | -0.61 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[ZFAND2A-DT]] | -0.61 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[NOL7]] ⚠ | -0.60 | -0.42 / -0.61 | both halves | 4e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[COMMD6]] | -0.60 | -0.52 / -0.59 | both halves | 1e-05 |  |
| [[SEC61G]] | -0.59 | -0.48 / -0.57 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CDC25A]] | B | CDC25A activity raises MCM7's level | lines that do not express CDC25A (5) vs lines expressing it (45) | 1.97× lower at baseline in the lines without CDC25A | 0.029 | ⚠ within organs, on part of the lines; also absent: ZNF367, E2F1, ALDH1B1; maybe low, not absent |
| [[E2F2]] | B | E2F2 activity raises MCM7's level | lines that do not express E2F2 (13) vs lines expressing it (37) | 1.69× lower at baseline in the lines without E2F2 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000260498, ABHD11, BRSK2; maybe low, not absent |
| [[CDCA7]] | B | CDCA7 activity raises MCM7's level | lines that do not express CDCA7 (6) vs lines expressing it (44) | 1.79× lower at baseline in the lines without CDCA7 | 0.076 | ⚠ within organs, on part of the lines; also absent: PKMYT1, CHD7, CYP2R1; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises MCM7's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[ZNF367]] | C | ZNF367 activity raises MCM7's level | lines that do not express ZNF367 (4) vs lines expressing it (46) | 2.00× lower at baseline in the lines without ZNF367 | 0.069 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CDC25A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.696). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-36.3, -42.7); signed map (-36.4, -47.3). **Vector** length 130, 41.4% of its response variance represented; |z| ≥ 3 in 1,289 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Homology Directed Repair* (reactome, mean cos +0.54 to 32); *Chromosome Maintenance* (reactome, mean cos +0.52 to 29); *HDR through Homologous Recombination (HRR) or Single Strand Annealing (SSA)* (reactome, mean cos +0.56 to 29).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +7.9 | +14.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +7.1 | +17.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | +7.0 | +17.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +5.3 | +8.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | +3.9 | +7.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.9 | +3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.8 | +2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.8 | +1.4 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +2.6 | +2.0 |
|  | [[Methotrexate (drug)]] 5 µM |  | +2.6 | +1.5 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -5.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~49% of this change | -5.1 | -4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.9 | -3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.3 | -5.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -4.1 | -5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.9 | -3.9 |

## What is on record

|  |  |
|---|---|
| Name | minichromosome maintenance complex component 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,092,233-100,101,940 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CDC47, PPP1R104; previously MCM2 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; MCM family; MicroRNA protein coding host genes; minichromosome maintenance 2-7 complex |
| Hallmark sets | EPITHELIAL_MESENCHYMAL_TRANSITION, E2F_TARGETS, MYC_TARGETS_V1 |
| Reactome | 17 pathways, smallest: Unwinding of DNA; Activation of the pre-replicative complex; DNA strand elongation |
| Matched by | ensembl_id |

**Function**, from UniProt [P33993](https://www.uniprot.org/uniprotkb/P33993) (DNA replication licensing factor MCM7):

> Acts as a component of the MCM2-7 complex (MCM complex) which is the replicative helicase essential for 'once per cell cycle' DNA replication initiation and elongation in eukaryotic cells. Core component of CDC45-MCM-GINS (CMG) helicase, the molecular machine that unwinds template DNA during replication, and around which the replisome is built. The active ATPase sites in the MCM2-7 ring are formed through the interaction surfaces of two neighboring subunits such that a critical structure of a …

**Summary**, from NCBI Gene [4176](https://www.ncbi.nlm.nih.gov/gene/4176):

> The protein encoded by this gene is one of the highly conserved mini-chromosome maintenance proteins (MCM) that are essential for the initiation of eukaryotic genome replication. The hexameric protein complex formed by the MCM proteins is a key component of the pre-replication complex (pre_RC) and may be involved in the formation of replication forks and in the recruitment of other DNA replication related proteins. The MCM complex consisting of this protein and MCM2, 4 and 6 proteins possesses …

**Accessions** — [HGNC:6950](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6950) · Entrez [4176](https://www.ncbi.nlm.nih.gov/gene/4176) · UniProt [P33993](https://www.uniprot.org/uniprotkb/P33993) · Ensembl [ENSG00000166508](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166508)

## Data

Gene col 9323: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9323); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9323, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9323]; `tensor/DDL_lfc|DDL_z.npy` [9323]; `embed/gene_vectors.npy` [9323]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9323 or target_col == 9323). Every well: [[MCM7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCM7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
