---
symbol: "NGLY1"
type: "gene"
col: 7484
ensembl_id: "ENSG00000151092"
name: "N-glycanase 1"
location: "3p24.2"
module: 180
arm: "+"
pooled_cpm: 184.96
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 28
n_dd_up_clean: 3
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/180"]
generated_by: "tahoemap"
---

# NGLY1

*N-glycanase 1* — 3p24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 1.38× (z +4.8, q 0.001, up in 34 of 48 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[PF-06260933 (drug)]] 5 µM: 1.83× (z +4.6, q 0.001, up in 31 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.345× (z -14.9, q 0e+00, down in 40 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.552× (z -12.3, q 2e-32, down in 35 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UBA6]] (+0.76, fdr 7e-06), [[PPP2R5B]] (+0.72, fdr 7e-06), [[ARFGEF3]] (+0.71, fdr 7e-06); moves opposite to [[ZNF644]] (-0.61, fdr 1e-05), [[RPRD1B]] (-0.60, fdr 1e-04), [[JADE2]] (-0.57, fdr 4e-05).
> It is in [[Module 180]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF215]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7484.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +4.8 | 0.001 | 34/48 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.83×** | +4.6 | 0.001 | 31/48 (SHP-77, CFPAC-1, …) | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.31×** | +3.7 | 0.036 | 22/48 (LoVo, LS 180, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.40×** | +3.5 | 0.058 | 30/48 (HEC-1-A, CFPAC-1, …) | two highest doses | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.091 | 29/49 (PANC-1, SW 900, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7484.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.345×** | -14.9 | 0e+00 | 40/44 (HEC-1-A, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.373×** | -14.4 | 2e-44 | 45/49 (HOP62, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.552×** | -12.3 | 2e-32 | 35/48 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.562×** | -11.9 | 2e-30 | 38/49 (A549, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.469×** | -10.6 | 3e-24 | 42/48 (NCI-H1573, A-172, …) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.460×** | -10.5 | 1e-23 | 40/45 (A549, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.526×** | -9.0 | 2e-17 | 40/47 (NCI-H1573, C32, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.555×** | -8.3 | 1e-14 | 42/47 (NCI-H1573, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.571×** | -8.2 | 2e-14 | 33/48 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.630×** | -6.5 | 5e-09 | 39/48 (C-33 A, NCI-H1573, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.767×** | -5.5 | 2e-06 | 34/48 (HOP62, A549, …) | top dose only | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.710×** | -5.0 | 3e-05 | 33/48 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Selinexor (drug)]] 5 µM |  | **0.790×** | -4.8 | 5e-05 | 28/48 (C32, HOP62, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.724×** | -4.7 | 1e-04 | 33/48 (MIA PaCa-2, HOP62, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.730×** | -4.6 | 2e-04 | 33/48 (A-172, HOP62, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.761×** | -4.0 | 0.002 | 28/48 (HepG2/C3A, C32, …) | rises with dose |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.776×** | -3.7 | 0.006 | 31/49 (HOP62, hTERT-HPNE, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.781×** | -3.4 | 0.017 | 27/47 (HOP62, SW48, …) | inconsistent across doses |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.798×** | -3.3 | 0.026 | 25/48 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Pralsetinib (drug)]] 5 µM |  | **0.659×** | -3.2 | 0.035 | 22/49 (LOX-IMVI, HOP62, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.16 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7484. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 445 | 0 | 23 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0826× (z -18.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.0898× (z -17.6) |
| [[HOP62 (line)]] | alt | 517 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.334× (z -13.2) |
| [[A549 (line)]] | wt | 316 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.245× (z -19.7) |
| [[C-33 A (line)]] | alt | 357 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -15.1) |
| [[A-172 (line)]] | wt | 204 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -15.3) |
| [[LOX-IMVI (line)]] | wt | 284 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -18.9) |
| [[NCI-H1792 (line)]] | alt | 445 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.256× (z -19.3) |
| [[SNU-423 (line)]] | alt | 293 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -17.6) |
| [[C32 (line)]] | wt | 166 | 0 | 6 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.212× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.448× (z -11.7) |
| [[HS-578T (line)]] | alt | 202 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.243× (z -20.6) |
| [[LoVo (line)]] | wt | 102 | 3 (3 ⚠) | 2 (2 ⚠) | [[Bortezomib (drug)]] 0.05 µM 2.33× (z +9.8) ⚠ cell-cycle shift, explains ~25% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.421× (z -10.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 236 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.404× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 215 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.263× (z -12.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.438× (z -11.3) |
| [[RPMI-7951 (line)]] | alt | 278 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -13.7) |
| [[SK-MEL-2 (line)]] | alt | 305 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -12.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -9.9) |
| [[CFPAC-1 (line)]] | alt | 156 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.339× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -10.5) |
| [[HEC-1-A (line)]] | alt | 195 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.568× (z -9.4) |
| [[HepG2_C3A (line)]] | wt | 216 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.288× (z -13.6) |
| [[COLO 205 (line)]] | alt | 47.8 | 3 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.49× (z +9.5) ⚠ cell-cycle shift, explains ~6% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.17× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 183 | 0 | 3 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.251× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.294× (z -10.4) |
| [[hTERT-HPNE (line)]] | wt | 296 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.197× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.246× (z -8.9) |
| [[J82 (line)]] | alt | 175 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.294× (z -11.9) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 149 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.342× (z -13.2) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 103 | 1 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.00× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.485× (z -12.5) |
| [[SW48 (line)]] | wt | 172 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -10.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.458× (z -9.2) |
| [[A498 (line)]] | wt | 80.2 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -9.8) |
| [[AN3 CA (line)]] | alt | 213 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -17.8) |
| [[AsPC-1 (line)]] | alt | 121 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.365× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.566× (z -8.7) |
| [[KATO III (line)]] | alt | 111 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.394× (z -10.0) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.545× (z -9.2) |
| [[LS 180 (line)]] | wt | 125 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.215× (z -15.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.542× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 156 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.255× (z -18.9) |
| [[RKO (line)]] | wt | 166 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.460× (z -11.5) |
| [[SNU-1 (line)]] | wt | 177 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.224× (z -12.6) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 120 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.328× (z -10.9) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 147 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -11.8) |
| [[A-427 (line)]] | wt | 103 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.240× (z -14.9) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 99.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.482× (z -9.4) |
| [[Hs 766T (line)]] | wt | 137 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.370× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 92.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.583× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 83.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.293× (z -13.0) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 50.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.548× (z -10.6) |
| [[SHP-77 (line)]] | alt | 146 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.374× (z -9.0) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 349 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.217× (z -8.5) ⚠ transcription drop; cell-cycle shift, explains ~30% of this change |
| [[CHP-212 (line)]] | wt | 157 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 195 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 209 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 148 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7484), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UBA6]] | +0.76 | +0.78 / +0.64 | both halves | 7e-06 |  |
| [[PPP2R5B]] | +0.72 | +0.70 / +0.60 | both halves | 7e-06 |  |
| [[ARFGEF3]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[NDRG1]] | +0.71 | +0.76 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[HILPDA]] | +0.70 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[INSIG2]] | +0.69 | +0.69 / +0.62 | both halves | 7e-06 |  |
| [[FAM210A]] | +0.69 | +0.74 / +0.61 | both halves | 7e-06 |  |
| [[PPFIA1]] | +0.67 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.67 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[UBE2O]] | +0.67 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[NQO2]] | +0.66 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[ANKRD37]] | +0.66 | +0.72 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF644]] | -0.61 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[RPRD1B]] | -0.60 | -0.33 / -0.54 | both halves | 1e-04 |  |
| [[JADE2]] | -0.57 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[PARVA]] | -0.57 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[ZBTB45]] | -0.56 | -0.52 / -0.46 | both halves | 2e-05 |  |
| [[ZNF747]] | -0.56 | -0.60 / -0.31 | both halves | 2e-04 |  |
| [[SCAF8]] | -0.56 | -0.35 / -0.51 | both halves | 1e-04 |  |
| [[PPP3CB-AS1]] | -0.55 | -0.57 / -0.26 | both halves | 4e-04 |  |
| [[FIZ1]] | -0.55 | -0.54 / -0.38 | both halves | 6e-05 |  |
| [[IQCH-AS1]] | -0.55 | -0.61 / -0.27 | both halves | 3e-04 |  |
| [[ZNF362]] | -0.55 | -0.52 / -0.33 | both halves | 1e-04 |  |
| [[POGLUT1]] | -0.54 | -0.62 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF215]] | B | ZNF215 activity raises NGLY1's level | lines that do not express ZNF215 (12) vs lines expressing it (38) | 1.41× lower at baseline in the lines without ZNF215 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000283415, ENSG00000291143 |
| [[CRYBG3]] | C | CRYBG3 activity raises NGLY1's level | lines that do not express CRYBG3 (3) vs lines expressing it (47) | 1.91× lower at baseline in the lines without CRYBG3 | 0.079 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: GPR137B, PAM, DTX3L |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 180]]; 22 genes; every member is in the + arm (projection on the module's main direction 0.824). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (12.6, -15.4); signed map (-36.6, 26.3). **Vector** length 143, 55.5% of its response variance represented; |z| ≥ 3 in 1,522 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +8.5 | +1.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +7.5 | +0.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +7.4 | +0.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.6 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.2 | +2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +4.9 | +4.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.7 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.1 | -1.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.6 | +3.5 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -7.3 | -10.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -7.0 | -9.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -6.5 | -1.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.2 | -2.5 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -5.3 | -5.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.1 | -6.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -5.0 | -2.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.6 | -5.5 |

## What is on record

|  |  |
|---|---|
| Name | N-glycanase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p24.2 — chr3:25,718,944-25,790,039 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ11005, PNG1, PNG-1 |
| Hallmark sets | ANDROGEN_RESPONSE |
| Reactome | 2 pathways, smallest: N-glycan trimming in the ER and Calnexin/Calreticulin cycle; Asparagine N-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96IV0](https://www.uniprot.org/uniprotkb/Q96IV0) (Peptide-N(4)-(N-acetyl-beta-glucosaminyl)asparagine amidase):

> Protein N-glycosidase that mediates deglycosylation of N-linked glycoproteins by cleaving the beta-aspartyl-glucosamine (GlcNAc) of the glycan and the amide side chain of asparagine (Asn), converting Asn to aspartate (Asp). Prefers proteins containing high-mannose over those bearing complex type oligosaccharides. Involved in the degradation of endoplasmic reticulum-associated degradation (ERAD): recognizes misfolded proteins in the endoplasmic reticulum that are exported to the cytosol to be …

**Summary**, from NCBI Gene [55768](https://www.ncbi.nlm.nih.gov/gene/55768):

> This gene encodes an enzyme that catalyzes hydrolysis of an N(4)-(acetyl-beta-D-glucosaminyl) asparagine residue to N-acetyl-beta-D-glucosaminylamine and a peptide containing an aspartate residue. The encoded enzyme may play a role in the proteasome-mediated degradation of misfolded glycoproteins. Multiple transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, Feb 2009]

**Accessions** — [HGNC:17646](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17646) · Entrez [55768](https://www.ncbi.nlm.nih.gov/gene/55768) · UniProt [Q96IV0](https://www.uniprot.org/uniprotkb/Q96IV0) · Ensembl [ENSG00000151092](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151092)

## Data

Gene col 7484: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7484); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7484, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7484]; `tensor/DDL_lfc|DDL_z.npy` [7484]; `embed/gene_vectors.npy` [7484]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7484 or target_col == 7484). Every well: [[NGLY1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NGLY1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
