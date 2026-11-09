---
symbol: "C1GALT1"
type: "gene"
col: 2754
ensembl_id: "ENSG00000106392"
name: "core 1 synthase, glycoprotein-N-acetylgalactosamine 3-beta-galactosyltransferase 1"
location: "7p22.1-p21.3"
module: 180
arm: "+"
pooled_cpm: 115.41
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 17
n_dd_up_clean: 3
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/180"]
generated_by: "tahoemap"
---

# C1GALT1

*core 1 synthase, glycoprotein-N-acetylgalactosamine 3-beta-galactosyltransferase 1* — 7p22.1-p21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.23× (z +6.5, q 5e-08, up in 29 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (11 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.512× (z -13.9, q 3e-41, down in 44 of 47 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.683× (z -11.7, q 2e-29, down in 31 of 49 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRYBG3]] (+0.62, fdr 7e-06), [[ARFGEF3]] (+0.59, fdr 1e-05), [[PPP2R5B]] (+0.56, fdr 1e-05); moves opposite to [[DNAJB6]] (-0.62, fdr 1e-05), [[PEX6]] (-0.47, fdr 7e-05), [[XNDC1N-ZNF705EP-ALG1L9P]] (-0.45, fdr 7e-05).
> It is in [[Module 180]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2754.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +6.5 | 5e-08 | 29/48 (KATO III, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.28×** | +5.4 | 2e-05 | 31/49 (Panc 03.27, SW48, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.25×** | +4.8 | 3e-04 | 28/48 (PANC-1, H4, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **1.44×** | +4.1 | 0.005 | 23/48 (PANC-1, A498, …) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | 1.18× | +3.7 | 0.026 | 19/50 (AsPC-1, A-172, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | 1.19× | +3.6 | 0.026 | 17/47 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.036 | 18/48 (PANC-1, SW 900, …) | all doses, flat | noisy plate (z scaled) |
| [[Vortioxetine (drug)]] 0.5 µM |  | 1.16× | +3.3 | 0.067 | 12/48 (LOX-IMVI, BT-474, …) | inconsistent across doses |  |
| [[RMC-6236 (drug)]] 5 µM |  | 1.32× | +3.2 | 0.10 | 15/48 (KATO III, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | 1.31× | +3.1 | 0.12 | 17/48 (PANC-1, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | 1.30× | +3.0 | 0.13 | 14/48 (PANC-1, A498, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 17 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2754.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.512×** | -13.9 | 3e-41 | 44/47 (NCI-H1792, C32, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.534×** | -13.6 | 9e-40 | 42/49 (NCI-H1792, SW480, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.516×** | -13.3 | 6e-38 | 39/45 (SK-MEL-2, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.556×** | -12.2 | 4e-32 | 35/43 (KATO III, A-172, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.683×** | -11.7 | 2e-29 | 31/49 (NCI-H1792, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.635×** | -9.9 | 5e-21 | 44/48 (A-172, NCI-H460, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.795×** | -7.0 | 2e-10 | 27/48 (MIA PaCa-2, NCI-H2347, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.738×** | -6.3 | 2e-08 | 27/48 (HEC-1-A, A-172, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.748×** | -6.3 | 2e-08 | 25/48 (C32, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~18% of this change | **0.773×** | -5.3 | 5e-06 | 25/47 (HT-29, C32, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.804×** | -4.7 | 1e-04 | 25/48 (C32, HS-578T, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.941× | -4.5 | 4e-04 | 1/50 (NCI-H2122) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.804×** | -4.5 | 4e-04 | 23/48 (HS-578T, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **0.820×** | -4.3 | 7e-04 | 24/48 (NCI-H460, HOP62, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.693×** | -4.2 | 0.001 | 20/38 (HEC-1-A, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | 0.851× | -3.3 | 0.021 | 14/48 (HS-578T, HEC-1-A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2754. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 183 | 0 | 15 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -16.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.370× (z -12.0) |
| [[HS-578T (line)]] | alt | 153 | 0 | 9 (8 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.297× (z -13.0) ⚠ cell-cycle shift, explains ~23% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.512× (z -10.6) |
| [[A-172 (line)]] | wt | 157 | 0 | 8 (7 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.218× (z -15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.304× (z -12.5) |
| [[NCI-H1792 (line)]] | alt | 238 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.336× (z -22.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.491× (z -14.3) |
| [[PANC-1 (line)]] | alt | 120 | 1 (1 ⚠) | 5 (5 ⚠) | [[c-Kit-IN-1 (drug)]] 0.05 µM 2.37× (z +14.1) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.593× (z -12.0) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 79.3 | 0 | 5 (5 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.0669× (z -18.8) ⚠ toxic |
| [[HT-29 (line)]] | alt | 137 | 2 (2 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +14.3) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.414× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H460 (line)]] | wt | 112 | 0 | 5 (4 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.398× (z -12.1) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 0.465× (z -10.6) |
| [[SK-MEL-2 (line)]] | alt | 187 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0696× (z -28.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -10.5) |
| [[KATO III (line)]] | alt | 261 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.268× (z -18.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.555× (z -12.1) |
| [[LoVo (line)]] | wt | 95.8 | 1 (1 ⚠) | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.79× (z +12.0) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.363× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[MIA PaCa-2 (line)]] | alt | 86.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.201× (z -17.1) ⚠ toxic; transcription drop · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.572× (z -9.1) |
| [[SNU-423 (line)]] | alt | 118 | 0 | 4 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.555× (z -10.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.574× (z -10.0) |
| [[COLO 205 (line)]] | alt | 123 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.312× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.531× (z -9.1) |
| [[SW480 (line)]] | alt | 157 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.329× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[A-427 (line)]] | wt | 82.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.312× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[A549 (line)]] | wt | 103 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.370× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.594× (z -8.7) |
| [[BT-474 (line)]] | alt | 84.6 | 0 | 2 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -9.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.518× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 107 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -11.6) |
| [[H4 (line)]] | wt | 178 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.280× (z -12.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HepG2_C3A (line)]] | wt | 123 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -13.8) |
| [[LOX-IMVI (line)]] | wt | 103 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.450× (z -8.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.593× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 89.5 | 0 | 2 | — | [[Clobetasol propionate (drug)]] 0.05 µM 0.406× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 84.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.450× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H2347 (line)]] | alt | 89.0 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.543× (z -10.9) |
| [[SHP-77 (line)]] | alt | 79.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.251× (z -13.1) ⚠ toxic |
| [[A498 (line)]] | wt | 113 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.500× (z -8.8) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 153 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.423× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HCT15 (line)]] | alt | 88.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -12.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 60.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +9.6) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LS 180 (line)]] | wt | 56.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.98× (z +10.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[NCI-H2030 (line)]] | alt | 125 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.575× (z -9.5) |
| [[SW 1271 (line)]] | alt | 140 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0844× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[SW1417 (line)]] | alt | 182 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.558× (z -11.0) |
| [[SW48 (line)]] | wt | 111 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -14.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 76.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 79.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 56.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 83.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 77.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 116 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 108 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 74.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 96.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 101 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 61.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 139 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 106 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2754), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRYBG3]] | +0.62 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[ARFGEF3]] | +0.59 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[PPP2R5B]] | +0.56 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[XPNPEP1]] | +0.56 | +0.50 / +0.54 | both halves | 1e-05 |  |
| [[GPR160]] | +0.54 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[SLC25A4]] | +0.53 | +0.51 / +0.42 | both halves | 4e-05 |  |
| [[HILPDA]] | +0.53 | +0.52 / +0.51 | both halves | 1e-05 |  |
| [[RAB30]] | +0.52 | +0.35 / +0.49 | both halves | 1e-04 |  |
| [[BNIP3]] | +0.52 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[NGLY1]] | +0.52 | +0.51 / +0.47 | both halves | 2e-05 |  |
| [[TEC]] | +0.52 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[JPT1]] | +0.51 | +0.48 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJB6]] | -0.62 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[PEX6]] | -0.47 | -0.42 / -0.37 | both halves | 7e-05 |  |
| [[XNDC1N-ZNF705EP-ALG1L9P]] | -0.45 | -0.39 / -0.38 | both halves | 7e-05 |  |
| [[CDNF]] | -0.45 | -0.35 / -0.34 | both halves | 1e-04 |  |
| [[C16orf95]] | -0.45 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[FARS2]] | -0.44 | -0.32 / -0.47 | both halves | 2e-04 |  |
| [[MAMDC2-AS1]] | -0.44 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[ITPKB]] | -0.44 | -0.30 / -0.38 | both halves | 2e-04 |  |
| [[SPATA17]] | -0.44 | -0.32 / -0.47 | both halves | 1e-04 |  |
| [[KCTD21-AS1]] | -0.43 | -0.40 / -0.28 | both halves | 3e-04 |  |
| [[XNDC1N]] | -0.43 | -0.37 / -0.34 | both halves | 1e-04 |  |
| [[RPRD1B]] | -0.42 | -0.27 / -0.41 | both halves | 3e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 180]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.587). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (16.7, -15.4); signed map (-37.0, 26.3). **Vector** length 107, 30.9% of its response variance represented; |z| ≥ 3 in 1,261 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +7.0 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.6 | +6.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~14% of this change | +5.7 | +5.4 |
|  | [[venetoclax (drug)]] 5 µM |  | +5.0 | +4.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.6 | +2.0 |
|  | [[TAK-733 (drug)]] 5 µM |  | +4.6 | +2.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.9 | +3.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.0 | -9.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.9 | -13.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.6 | -13.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.2 | -6.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.9 | -1.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -4.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.0 | -2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | core 1 synthase, glycoprotein-N-acetylgalactosamine 3-beta-galactosyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1-p21.3 — chr7:7,156,934-7,248,616 (+) |
| Ensembl biotype | protein_coding |
| Also known as | C1GALT, T-synthase |
| Gene groups (HGNC) | Beta 3-glycosyltransferases |
| Reactome | 6 pathways, smallest: Defective C1GALT1C1 causes TNPS; O-linked glycosylation of mucins; Diseases associated with O-glycosylation of proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NS00](https://www.uniprot.org/uniprotkb/Q9NS00) (Glycoprotein-N-acetylgalactosamine 3-beta-galactosyltransferase 1):

> Glycosyltransferase that generates the core 1 O-glycan Gal-beta1-3GalNAc-alpha1-Ser/Thr (T antigen), which is a precursor for many extended O-glycans in glycoproteins. Plays a central role in many processes, such as angiogenesis, thrombopoiesis and kidney homeostasis development (By similarity).

**Summary**, from NCBI Gene [56913](https://www.ncbi.nlm.nih.gov/gene/56913):

> The protein encoded by this gene generates the common core 1 O-glycan structure, Gal-beta-1-3GalNAc-R, by the transfer of Gal from UDP-Gal to GalNAc-alpha-1-R. Core 1 is a precursor for many extended mucin-type O-glycans on cell surface and secreted glycoproteins. Studies in mice suggest that this gene plays a key role in thrombopoiesis and kidney homeostasis.[provided by RefSeq, Sep 2010]

**Accessions** — [HGNC:24337](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24337) · Entrez [56913](https://www.ncbi.nlm.nih.gov/gene/56913) · UniProt [Q9NS00](https://www.uniprot.org/uniprotkb/Q9NS00) · Ensembl [ENSG00000106392](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000106392)

## Data

Gene col 2754: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2754); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2754, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2754]; `tensor/DDL_lfc|DDL_z.npy` [2754]; `embed/gene_vectors.npy` [2754]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2754 or target_col == 2754). Every well: [[C1GALT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C1GALT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
