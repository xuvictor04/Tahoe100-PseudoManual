---
symbol: "ARAP1"
type: "gene"
col: 11838
ensembl_id: "ENSG00000186635"
name: "ArfGAP with RhoGAP domain, ankyrin repeat and PH domain 1"
location: "11q13.4"
module: 34
arm: "+"
pooled_cpm: 57.6
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 29
n_dd_up_clean: 0
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# ARAP1

*ArfGAP with RhoGAP domain, ankyrin repeat and PH domain 1* — 11q13.4

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HS-578T 3.45×, NCI-H1792 2.68×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (20 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 0.517× (z -8.4, q 2e-14, down in 35 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.545× (z -8.3, q 2e-14, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAM8]] (+0.61, fdr 1e-05), [[GNA15]] (+0.61, fdr 1e-05), [[PDE2A]] (+0.58, fdr 1e-05, ⚠ same locus), [[RCN3]] (+0.57, fdr 2e-05); moves opposite to [[USP25]] (-0.52, fdr 1e-05), [[MGST1]] (-0.49, fdr 4e-05), [[MYCBP2]] (-0.49, fdr 3e-05).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ATP2A3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11838.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (HS-578T 3.45×, NCI-H1792 2.68×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | 1.19× | +3.4 | 0.41 | 14/48 (HOP62, PANC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 20 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11838.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.517×** | -8.4 | 2e-14 | 35/44 (NCI-H1792, Panc 03.27, …) | all doses, flat | composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.545×** | -8.3 | 2e-14 | 35/48 (HT-29, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **0.532×** | -8.3 | 2e-14 | 37/47 (NCI-H23, A498, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.533×** | -8.3 | 2e-14 | 38/49 (SW 900, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.577×** | -7.6 | 5e-12 | 36/48 (HT-29, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.565×** | -7.5 | 5e-12 | 38/48 (SW 1271, HOP62, …) | top dose only | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.691×** | -7.2 | 7e-11 | 30/48 (AsPC-1, SW 900, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.605×** | -6.9 | 4e-10 | 34/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.608×** | -6.6 | 3e-09 | 33/48 (AsPC-1, COLO 205, …) | rises with dose | composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.621×** | -6.5 | 4e-09 | 35/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.626×** | -6.4 | 7e-09 | 38/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.638×** | -6.2 | 3e-08 | 34/48 (SNU-423, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~91% of this change | **0.641×** | -6.1 | 5e-08 | 35/48 (NCI-H23, NCI-H1573, …) | all doses, flat | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.652×** | -5.9 | 2e-07 | 38/48 (PANC-1, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.653×** | -5.8 | 2e-07 | 32/48 (HT-29, SNU-423, …) | all doses, stronger at high dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.720×** | -4.5 | 2e-04 | 25/48 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Thymol (drug)]] 5 µM |  | **0.811×** | -4.0 | 0.002 | 24/48 (A-172, HS-578T, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.836× | -3.5 | 0.013 | 19/48 (J82, SNU-423, …) | top dose only | position effect removed |
| [[Sulfatinib (drug)]] 5 µM |  | **0.784×** | -3.2 | 0.033 | 22/48 (CHP-212, J82, …) | top dose only | position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | 0.850× | -3.1 | 0.038 | 17/48 (NCI-H1792, BT-474, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.795×** | -3.1 | 0.038 | 18/48 (MIA PaCa-2, LoVo, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.798×** | -3.1 | 0.043 | 17/48 (H4, HOP62, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 5 µM |  | **0.662×** | -3.0 | 0.064 | 18/48 (Hs 766T, A498, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.807×** | -2.9 | 0.065 | 14/49 (HT-29, NCI-H2347, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.43 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11838. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 100 | 0 | 9 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.293× (z -12.8) ⚠ cell-cycle shift, explains ~25% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.214× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 97.8 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -12.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.330× (z -8.7) |
| [[HT-29 (line)]] | alt | 112 | 0 | 7 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -11.9) |
| [[SNU-423 (line)]] | alt | 103 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.307× (z -12.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 79.0 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.239× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.342× (z -8.9) |
| [[SW480 (line)]] | alt | 71.4 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.265× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[AsPC-1 (line)]] | alt | 84.6 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -17.4) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 78.9 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.410× (z -10.8) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 54.4 | 1 (1 ⚠) | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +9.7) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.05 µM 0.0681× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.260× (z -9.5) |
| [[COLO 205 (line)]] | alt | 86.9 | 0 | 3 (3 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.154× (z -12.2) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H1573 (line)]] | alt | 71.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.218× (z -10.6) |
| [[PANC-1 (line)]] | alt | 53.6 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.319× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[A549 (line)]] | wt | 65.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.247× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.350× (z -9.1) |
| [[C32 (line)]] | wt | 35.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.233× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.271× (z -8.9) |
| [[HOP62 (line)]] | alt | 61.3 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.157× (z -12.6) ⚠ cell-cycle shift, explains ~29% of this change |
| [[Hs 766T (line)]] | wt | 63.0 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -11.2) ⚠ cell-cycle shift, explains ~25% of this change |
| [[HS-578T (line)]] | alt | 35.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +12.0) ⚠ cell-cycle shift, would explain all of this change | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.247× (z -9.3) ⚠ cell-cycle shift, explains ~29% of this change |
| [[Panc 03.27 (line)]] | alt | 72.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.188× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[A498 (line)]] | wt | 45.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.346× (z -9.4) ⚠ toxic; cell-cycle shift, explains ~29% of this change |
| [[AN3 CA (line)]] | alt | 64.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[BT-474 (line)]] | alt | 94.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.327× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[H4 (line)]] | wt | 55.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 44.9 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.255× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 54.6 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -8.7) ⚠ cell-cycle shift, explains ~29% of this change |
| [[KATO III (line)]] | alt | 76.8 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.376× (z -10.3) ⚠ cell-cycle shift, explains ~25% of this change |
| [[LoVo (line)]] | wt | 36.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.350× (z -9.7) |
| [[MIA PaCa-2 (line)]] | alt | 35.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.293× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 28.6 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.363× (z -8.7) |
| [[SHP-77 (line)]] | alt | 58.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.285× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SNU-1 (line)]] | wt | 60.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.134× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SW 1271 (line)]] | alt | 117 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0424× (z -13.0) ⚠ cell-cycle shift, explains ~29% of this change |
| [[A-172 (line)]] | wt | 52.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 40.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 51.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 53.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 35.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 47.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 39.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 37.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 45.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 50.6 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 45.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11838), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAM8]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[GNA15]] | +0.61 | +0.56 / +0.56 | both halves | 1e-05 |  |
| [[PDE2A]] | +0.58 | +0.57 / +0.55 | both halves | 1e-05 | ⚠ same locus (10.5 kb, same strand: neighbours can correlate without regulation) |
| [[RCN3]] | +0.57 | +0.50 / +0.47 | both halves | 2e-05 |  |
| [[NGEF]] | +0.57 | +0.55 / +0.54 | both halves | 1e-05 | pathway: CDC42 GTPase cycle |
| [[CERK]] | +0.56 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[AHDC1]] | +0.55 | +0.67 / +0.35 | both halves | 1e-04 |  |
| [[LRP1]] | +0.55 | +0.59 / +0.46 | both halves | 2e-05 |  |
| [[SEMA3F]] | +0.55 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[OSBPL7]] | +0.55 | +0.61 / +0.41 | both halves | 4e-05 | same gene group |
| [[RAC2]] | +0.54 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[PLEKHG5]] | +0.54 | +0.59 / +0.44 | both halves | 3e-05 | same gene group; pathway: RHOA GTPase cycle |
| [[GIPR]] | +0.54 | +0.55 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP25]] | -0.52 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[MGST1]] | -0.49 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[MYCBP2]] | -0.49 | -0.61 / -0.46 | both halves | 3e-05 |  |
| [[TCF12]] | -0.49 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[CUX1]] | -0.48 | -0.48 / -0.37 | both halves | 8e-05 |  |
| [[NUTM2B-AS1]] | -0.47 | -0.48 / -0.37 | both halves | 9e-05 |  |
| [[ARID1B]] | -0.47 | -0.54 / -0.24 | both halves | 4e-04 |  |
| [[STXBP5]] | -0.47 | -0.45 / -0.44 | both halves | 3e-05 |  |
| [[ATG10]] | -0.46 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[SGMS1]] | -0.45 | -0.49 / -0.34 | both halves | 1e-04 | same gene group |
| [[MBNL1]] | -0.45 | -0.45 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP2A3]] | B | ATP2A3 activity raises ARAP1's level | lines that do not express ATP2A3 (16) vs lines expressing it (34) | 1.26× lower at baseline in the lines without ATP2A3 | 0.0997 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: WBP2NL, BEX4, NSUN7; maybe low, not absent |
| [[TP53]] | C | TP53 activity weakens ARAP1's drug response | recorded loss-of-function mutation of TP53 in 32 lines vs 17 not recorded | the TP53-altered lines respond 1.59× as strongly (z diff -1.95); strongest at Idarubicin (hydrochloride) 5 µM: 0.56x vs 0.86x (z diff -4.5) | 0.847 over the table, 0.066 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.467). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.4, -1.1); signed map (-0.5, 48.4). **Vector** length 90.6, 23.6% of its response variance represented; |z| ≥ 3 in 1,106 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +4.8 | +0.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +4.8 | -1.0 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +4.6 | -1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.1 | +0.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change | +2.9 | -5.5 |
|  | [[Imiquimod (hydrochloride) (drug)]] 0.05 µM |  | +2.2 | +2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | -1.2 |
|  | [[Ipatasertib (drug)]] 0.05 µM |  | +1.9 | +1.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -5.1 | -5.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -4.6 | -6.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.1 | -6.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -3.7 | -6.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~46% of this change | -3.5 | -3.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -3.2 | -2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.1 | -2.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.8 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.7 | -0.7 |
|  | [[Binimetinib (drug)]] 0.05 µM |  | -2.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | ArfGAP with RhoGAP domain, ankyrin repeat and PH domain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:72,685,069-72,793,599 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously CENTD2 |
| Gene groups (HGNC) | ArfGAPs; Ankyrin repeat domain containing; Pleckstrin homology domain containing; Sterile alpha motif domain containing |
| Reactome | 9 pathways, smallest: PTK6 Regulates RTKs and Their Effectors AKT1 and DOK1; Signaling by Non-Receptor Tyrosine Kinases; Signaling by PTK6 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96P48](https://www.uniprot.org/uniprotkb/Q96P48) (Arf-GAP with Rho-GAP domain, ANK repeat and PH domain-containing protein 1):

> Phosphatidylinositol 3,4,5-trisphosphate-dependent GTPase-activating protein that modulates actin cytoskeleton remodeling by regulating ARF and RHO family members. Activated by phosphatidylinositol 3,4,5-trisphosphate (PtdIns(3,4,5)P3) binding and, to a lesser extent, by phosphatidylinositol 3,4-bisphosphate (PtdIns(3,4)P2) binding. Has a preference for ARF1 and ARF5. Positively regulates the ring size of circular dorsal ruffles and promotes macropinocytosis. Acts as a bridging factor in …

**Summary**, from NCBI Gene [116985](https://www.ncbi.nlm.nih.gov/gene/116985):

> The protein encoded by this gene contains SAM, ARF-GAP, RHO-GAP, ankyrin repeat, RAS-associating, and pleckstrin homology (PH) domains. In vitro, this protein displays RHO-GAP and phosphatidylinositol (3,4,5) trisphosphate (PIP3)-dependent ARF-GAP activity. The encoded protein associates with the Golgi, and the ARF-GAP activity mediates changes in the Golgi and the formation of filopodia. It is thought to regulate the cell-specific trafficking of a receptor protein involved in apoptosis. …

**Accessions** — [HGNC:16925](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16925) · Entrez [116985](https://www.ncbi.nlm.nih.gov/gene/116985) · UniProt [Q96P48](https://www.uniprot.org/uniprotkb/Q96P48) · Ensembl [ENSG00000186635](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000186635)

## Data

Gene col 11838: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11838); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11838, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11838]; `tensor/DDL_lfc|DDL_z.npy` [11838]; `embed/gene_vectors.npy` [11838]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11838 or target_col == 11838). Every well: [[ARAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
