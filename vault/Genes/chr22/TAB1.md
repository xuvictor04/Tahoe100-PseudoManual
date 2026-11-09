---
symbol: "TAB1"
type: "gene"
col: 1927
ensembl_id: "ENSG00000100324"
name: "TGF-beta activated kinase 1 (MAP3K7) binding protein 1"
location: "22q13.1"
module: 64
arm: "+"
pooled_cpm: 14.5
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 27
n_dd_up_clean: 5
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# TAB1

*TGF-beta activated kinase 1 (MAP3K7) binding protein 1* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[Ponatinib (drug)]] 5 µM: 1.38× (z +5.3, q 7e-05, up in 19 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (12 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.452× (z -13.0, q 8e-36, down in 34 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.487× (z -11.8, q 1e-29, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CIAO3]] (+0.72, fdr 7e-06), [[CDK5RAP1]] (+0.68, fdr 7e-06), [[LRIG2]] (+0.67, fdr 1e-05); moves opposite to [[LINC00393]] (-0.57, fdr 2e-05), [[CTNNA1]] (-0.56, fdr 3e-05), [[YWHAZ]] (-0.55, fdr 3e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ZNF594-DT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1927.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.38×** | +5.3 | 7e-05 | 19/48 (PANC-1, KATO III, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.011 | 7/46 (SW480, C32, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.081 | 16/48 (KATO III, SNU-423, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.081 | 9/47 (PANC-1, KATO III, …) | rises with dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.23×** | +3.4 | 0.081 | 8/47 (A498, A-172, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1927.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.452×** | -13.0 | 8e-36 | 34/46 (HCT15, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.587×** | -12.3 | 2e-32 | 34/47 (SK-MEL-2, LoVo, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.487×** | -11.8 | 1e-29 | 40/48 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.518×** | -10.8 | 7e-25 | 37/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.591×** | -8.6 | 8e-16 | 34/47 (SK-MEL-2, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.601×** | -8.3 | 7e-15 | 27/41 (C32, NCI-H460, …) | all doses, flat | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.640×** | -7.3 | 2e-11 | 27/46 (NCI-H460, SNU-423, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~28% of this change | **0.656×** | -6.6 | 2e-09 | 28/45 (HS-578T, NCI-H460, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **0.677×** | -6.1 | 5e-08 | 15/26 (C32, NCI-H1792, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.489×** | -6.1 | 5e-08 | 25/48 (PANC-1, SNU-423, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.773×** | -5.9 | 1e-07 | 24/46 (Hs 766T, NCI-H460, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.686×** | -5.9 | 2e-07 | 25/47 (C-33 A, NCI-H460, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | **0.699×** | -5.4 | 3e-06 | 17/35 (MIA PaCa-2, HS-578T, …) | all doses, flat | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.717×** | -5.2 | 7e-06 | 20/46 (HS-578T, HOP62, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.741×** | -4.9 | 4e-05 | 18/47 (C32, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.620×** | -4.1 | 0.001 | 16/44 (A-172, LOX-IMVI, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.807×** | -3.5 | 0.013 | 17/48 (C32, NCI-H661, …) | rises with dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.670×** | -3.4 | 0.016 | 15/45 (MIA PaCa-2, RKO, …) | top dose only | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.685×** | -3.2 | 0.030 | 9/45 (Hs 766T, NCI-H2030, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Sinomenine (drug)]] 0.5 µM |  | **0.830×** | -3.0 | 0.055 | 7/48 (SW 1271, CFPAC-1, …) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.833×** | -2.9 | 0.089 | 5/48 (NCI-H2347, NCI-H1792, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 0.5 µM |  | 0.839× | -2.9 | 0.089 | 11/48 (SW 1271, KATO III, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1927. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 15.4 | 0 | 10 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.224× (z -11.9) |
| [[C32 (line)]] | wt | 26.6 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0692× (z -17.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.221× (z -10.0) |
| [[PANC-1 (line)]] | alt | 13.0 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.243× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.261× (z -11.3) |
| [[BT-474 (line)]] | alt | 12.6 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.164× (z -9.2) |
| [[MIA PaCa-2 (line)]] | alt | 16.2 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0871× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change · without an alert: [[PF-06260933 (drug)]] 5 µM 0.0502× (z -9.9) |
| [[SW480 (line)]] | alt | 18.6 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.232× (z -12.8) |
| [[A-172 (line)]] | wt | 9.96 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.152× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[HepG2_C3A (line)]] | wt | 12.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0617× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Bosentan (hydrate) (drug)]] 5 µM 0.133× (z -8.9) |
| [[HS-578T (line)]] | alt | 14.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0824× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H1792 (line)]] | alt | 15.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change |
| [[SK-MEL-2 (line)]] | alt | 22.8 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -16.3) ⚠ cell-cycle shift, explains ~36% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.251× (z -8.8) |
| [[C-33 A (line)]] | alt | 29.5 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -8.8) |
| [[HCT15 (line)]] | alt | 23.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0394× (z -18.0) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.228× (z -10.1) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 19.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.314× (z -9.8) |
| [[J82 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.158× (z -10.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 19.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.271× (z -9.8) |
| [[LoVo (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.273× (z -12.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[LS 180 (line)]] | wt | 14.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.162× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change |
| [[NCI-H1573 (line)]] | alt | 18.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -10.5) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H23 (line)]] | alt | 19.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.102× (z -14.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 15.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -8.9) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SNU-1 (line)]] | wt | 20.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.171× (z -8.6) |
| [[SNU-423 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -11.7) ⚠ cell-cycle shift, explains ~36% of this change |
| [[SW 900 (line)]] | alt | 7.99 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0950× (z -9.2) ⚠ toxic |
| [[A-427 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.99 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.76 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1927), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CIAO3]] | +0.72 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[CDK5RAP1]] | +0.68 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[LRIG2]] | +0.67 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[AP3S2]] | +0.67 | +0.56 / +0.69 | both halves | 1e-05 |  |
| [[MTFMT]] | +0.65 | +0.60 / +0.65 | both halves | 7e-06 | STRING 419 |
| [[DDX55]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[ZNF74]] | +0.64 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[ZSWIM9]] | +0.64 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[FCSK]] | +0.63 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[ORC5]] | +0.62 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[HEATR6]] | +0.61 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[RBSN]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 | pathway: Toll Like Receptor 9 (TLR9) Cascade |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00393]] | -0.57 | -0.49 / -0.46 | both halves | 2e-05 |  |
| [[CTNNA1]] | -0.56 | -0.43 / -0.64 | both halves | 3e-05 |  |
| [[YWHAZ]] | -0.55 | -0.46 / -0.60 | both halves | 3e-05 | pathway: SARS-CoV-2 Infection |
| [[YES1]] | -0.55 | -0.46 / -0.58 | both halves | 3e-05 |  |
| [[LINC02798]] | -0.55 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[HIVEP2-DT]] | -0.54 | -0.42 / -0.59 | both halves | 4e-05 |  |
| [[SLC12A2]] | -0.54 | -0.51 / -0.46 | both halves | 3e-05 |  |
| [[CCDC144CP]] | -0.54 | -0.39 / -0.53 | both halves | 5e-05 |  |
| [[ARL5B]] | -0.54 | -0.46 / -0.55 | both halves | 2e-05 |  |
| [[DPYS]] | -0.53 | -0.46 / -0.49 | both halves | 3e-05 |  |
| [[CCNT2-AS1]] | -0.53 | -0.35 / -0.52 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF594-DT]] | B | ZNF594-DT activity raises TAB1's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.39× lower at baseline in the lines without ZNF594-DT | 0.017 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |
| [[CCDC144CP]] | B | CCDC144CP activity raises TAB1's level | lines that do not express CCDC144CP (7) vs lines expressing it (43) | 1.44× lower at baseline in the lines without CCDC144CP | 0.078 | ⚠ within organs, on part of the lines; also absent: SNX10, CPPED1, GPLD1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.325). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-35.1, -8.3); signed map (-16.8, -13.8). **Vector** length 62.5, 9.87% of its response variance represented; |z| ≥ 3 in 978 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.5 | +2.9 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.7 | +2.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +5.3 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +2.9 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.0 | +3.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | +3.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.8 | -8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~39% of this change | -3.4 | -5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | -3.2 | -8.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.1 | -5.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | +0.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.4 | -3.4 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.3 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | TGF-beta activated kinase 1 (MAP3K7) binding protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:39,399,778-39,437,060 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously MAP3K7IP1 |
| Reactome | 47 pathways, smallest: IRAK2 mediated activation of TAK1 complex; Alpha-protein kinase 1 signaling pathway; TICAM1,TRAF6-dependent induction of TAK1 complex |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15750](https://www.uniprot.org/uniprotkb/Q15750) (TGF-beta-activated kinase 1 and MAP3K7-binding protein 1):

> Key adapter protein that plays an essential role in JNK and NF-kappa-B activation and pro-inflammatory cytokines production in response to stimulation with TLRs and cytokines. Mechanistically, associates with the catalytic domain of MAP3K7/TAK1 to trigger MAP3K7/TAK1 autophosphorylation leading to its full activation. Similarly, associates with MAPK14 and triggers its autophosphorylation and subsequent activation. In turn, MAPK14 phosphorylates TAB1 and inhibits MAP3K7/TAK1 activation in a …

**Summary**, from NCBI Gene [10454](https://www.ncbi.nlm.nih.gov/gene/10454):

> The protein encoded by this gene was identified as a regulator of the MAP kinase kinase kinase MAP3K7/TAK1, which is known to mediate various intracellular signaling pathways, such as those induced by TGF beta, interleukin 1, and WNT-1. This protein interacts and thus activates TAK1 kinase. It has been shown that the C-terminal portion of this protein is sufficient for binding and activation of TAK1, while a portion of the N-terminus acts as a dominant-negative inhibitor of TGF beta, suggesting …

**Accessions** — [HGNC:18157](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18157) · Entrez [10454](https://www.ncbi.nlm.nih.gov/gene/10454) · UniProt [Q15750](https://www.uniprot.org/uniprotkb/Q15750) · Ensembl [ENSG00000100324](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100324)

## Data

Gene col 1927: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1927); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1927, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1927]; `tensor/DDL_lfc|DDL_z.npy` [1927]; `embed/gene_vectors.npy` [1927]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1927 or target_col == 1927). Every well: [[TAB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TAB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
