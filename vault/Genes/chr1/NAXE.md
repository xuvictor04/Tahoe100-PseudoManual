---
symbol: "NAXE"
type: "gene"
col: 8681
ensembl_id: "ENSG00000163382"
name: "NAD(P)HX epimerase"
location: "1q22"
module: 12
arm: "-"
pooled_cpm: 15.84
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 2
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# NAXE

*NAD(P)HX epimerase* — 1q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.50× (z +14.7, q 0e+00, up in 38 of 38 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.72× (z +7.5, q 7e-12, up in 34 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (NCI-H1573 11.8×, NCI-H460 4.49×, PANC-1 5.11×, A-172 4.84×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 5.27×, KATO III 8.22×, SW480 4.14×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 4.13×).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.484× (z -10.1, q 4e-21, down in 36 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (NCI-H460 0.236×, NCI-H2030 0.251×, SHP-77 0.264×, SK-MEL-2 0.188×, …); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.267×); [[Bortezomib (drug)]] 0.05 µM in 1 line (SHP-77 0.131×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (48 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 52 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APRT]] (+0.62, fdr 3e-05), [[SELENON]] (+0.58, fdr 8e-04, ⚠ one half only (not replicated)), [[NME4]] (+0.57, fdr 3e-05), [[SUMF2]] (+0.56, fdr 3e-04); moves opposite to [[STK16]] (-0.55, fdr 1.00, ⚠ one half only (not replicated)), [[GORAB]] (-0.54, fdr 0.003, ⚠ one half only (not replicated)), [[CREB3]] (-0.54, fdr 0.004, ⚠ one half only (not replicated)), [[PPIL4]] (-0.53, fdr 7e-04), [[FBXO38]] (-0.53, fdr 6e-04), [[PAN2]] (-0.53, fdr 4e-04).
> It sits in the **-** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 13 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8681.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 11 lines (NCI-H1573 11.8×, NCI-H460 4.49×, PANC-1 5.11×, A-172 4.84×, …; ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change); [[Dinaciclib (drug)]] 5 µM in 3 lines (NCI-H460 5.27×, KATO III 8.22×, SW480 4.14×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (BT-474 4.13×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **4.50×** | +14.7 | 0e+00 | 38/38 (NCI-H1573, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **3.46×** | +11.7 | 4e-29 | 24/25 (NCI-H460, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.65×** | +8.8 | 2e-16 | 31/32 (NCI-H2030, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +7.5 | 7e-12 | 34/46 (BT-474, SNU-423, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +5.8 | 7e-07 | 26/40 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **1.80×** | +5.7 | 8e-07 | 33/46 (NCI-H460, LS 180, …) | rises with dose | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.77×** | +5.6 | 2e-06 | 31/41 (HS-578T, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **1.71×** | +5.3 | 1e-05 | 30/47 (A498, NCI-H460, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.66×** | +5.0 | 4e-05 | 26/47 (A498, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~80% of this change | **1.52×** | +4.1 | 0.002 | 27/47 (A-172, COLO 205, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **1.52×** | +4.1 | 0.002 | 19/46 (NCI-H460, NCI-H1573, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.008 | 21/46 (NCI-H460, HEC-1-A, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.46×** | +3.7 | 0.009 | 21/46 (NCI-H460, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | **1.43×** | +3.5 | 0.019 | 22/47 (NCI-H460, NCI-H1573, …) | rises with dose | composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~59% of this change | **1.45×** | +3.5 | 0.019 | 19/43 (NCI-H1573, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8681.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 7 lines (NCI-H460 0.236×, NCI-H2030 0.251×, SHP-77 0.264×, SK-MEL-2 0.188×, …); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (A-427 0.267×); [[Bortezomib (drug)]] 0.05 µM in 1 line (SHP-77 0.131×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.484×** | -10.1 | 4e-21 | 36/46 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.520×** | -6.4 | 4e-08 | 29/46 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.51 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8681. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 23.3 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.27× (z +11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -15.1) |
| [[SHP-77 (line)]] | alt | 52.3 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -12.1) |
| [[BT-474 (line)]] | alt | 18.1 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.282× (z -8.9) |
| [[HOP62 (line)]] | alt | 8.68 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.46× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -8.8) |
| [[J82 (line)]] | alt | 13.4 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.40× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | [[Homoharringtonine (drug)]] 5 µM 0.311× (z -9.4) |
| [[SW480 (line)]] | alt | 13.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.14× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[A-172 (line)]] | wt | 19.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.84× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A-427 (line)]] | wt | 39.3 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.267× (z -13.3) |
| [[A498 (line)]] | wt | 15.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[A549 (line)]] | wt | 10.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.20× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[HEC-1-A (line)]] | alt | 19.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[KATO III (line)]] | alt | 13.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.22× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | — |
| [[LoVo (line)]] | wt | 11.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.08× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[LS 180 (line)]] | wt | 16.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.71× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 16.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1573 (line)]] | alt | 9.46 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.8× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H1792 (line)]] | alt | 6.19 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 18.1× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[NCI-H2030 (line)]] | alt | 38.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -12.1) |
| [[PANC-1 (line)]] | alt | 20.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.11× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 12.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -10.4) |
| [[AN3 CA (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.08 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.49 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.63 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.69 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8681), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 15 of them with an alert (⚠; 15 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APRT]] | +0.62 | +0.67 / +0.45 | both halves | 3e-05 |  |
| [[SELENON]] | +0.58 | +0.72 / +0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[NME4]] | +0.57 | +0.59 / +0.43 | both halves | 3e-05 |  |
| [[SUMF2]] | +0.56 | +0.65 / +0.27 | both halves | 3e-04 |  |
| [[HIGD2A]] | +0.55 | +0.68 / +0.36 | both halves | 9e-05 |  |
| [[ILRUN]] | +0.54 | +0.59 / +0.10 | ⚠ one half (not replicated) | 0.003 |  |
| [[TSPO]] | +0.54 | +0.51 / +0.36 | both halves | 9e-05 |  |
| [[TUFM]] | +0.54 | +0.68 / +0.12 | ⚠ one half (not replicated) | 0.002 |  |
| [[PTK2]] | +0.54 | +0.56 / +0.25 | both halves | 4e-04 |  |
| [[C1GALT1C1]] | +0.53 | +0.57 / +0.26 | both halves | 4e-04 |  |
| [[TMEM147]] | +0.53 | +0.59 / +0.46 | both halves | 3e-05 | STRING 487 |
| [[TSPAN17]] | +0.52 | +0.55 / +0.33 | both halves | 1e-04 |  |
| [[CDKN2AIPNL]] | +0.52 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[C20orf27]] | +0.51 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[COPS9]] | +0.51 | +0.63 / +0.35 | both halves | 1e-04 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 37 of them with an alert (⚠; 37 not replicated); shown: the 12 strongest and the 7 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STK16]] | -0.55 | -0.68 / +0.06 | ⚠ one half (not replicated) | 1.00 |  |
| [[GORAB]] | -0.54 | -0.70 / -0.10 | ⚠ one half (not replicated) | 0.003 |  |
| [[CREB3]] | -0.54 | -0.71 / -0.06 | ⚠ one half (not replicated) | 0.004 |  |
| [[SNRNP27]] | -0.54 | -0.66 / -0.14 | ⚠ one half (not replicated) | 0.002 |  |
| [[PPIL4]] | -0.53 | -0.65 / -0.20 | both halves | 7e-04 |  |
| [[FBXO38]] | -0.53 | -0.61 / -0.22 | both halves | 6e-04 |  |
| [[PAN2]] | -0.53 | -0.61 / -0.24 | both halves | 4e-04 |  |
| [[CCDC174]] | -0.53 | -0.68 / -0.12 | ⚠ one half (not replicated) | 0.002 |  |
| [[UBXN4]] | -0.52 | -0.59 / -0.29 | both halves | 3e-04 |  |
| [[AP3D1]] | -0.52 | -0.68 / -0.09 | ⚠ one half (not replicated) | 0.003 |  |
| [[STAMBP]] | -0.51 | -0.61 / -0.27 | both halves | 3e-04 |  |
| [[GOSR1]] | -0.51 | -0.65 / -0.08 | ⚠ one half (not replicated) | 0.003 |  |
| [[GOLGB1]] | -0.49 | -0.62 / -0.21 | both halves | 7e-04 |  |
| [[CCT6P3]] | -0.49 | -0.53 / -0.29 | both halves | 2e-04 |  |
| [[SRRM1]] | -0.49 | -0.59 / -0.27 | both halves | 3e-04 |  |
| [[IK]] | -0.48 | -0.64 / -0.24 | both halves | 5e-04 |  |
| [[YME1L1]] | -0.48 | -0.62 / -0.24 | both halves | 4e-04 |  |
| [[ZNF181]] | -0.47 | -0.54 / -0.25 | both halves | 4e-04 |  |
| [[CRNKL1]] | -0.47 | -0.57 / -0.23 | both halves | 5e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **-** arm (projection on the module's main direction -0.453). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-24.6, -18.2); signed map (-25.7, -37.9). **Vector** length 64.1, 13.0% of its response variance represented; |z| ≥ 3 in 706 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | +5.4 | +5.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | +4.8 | +3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~82% of this change | +4.2 | +3.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | +4.0 | +4.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | +4.0 | +14.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +2.7 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +1.3 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +1.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.2 | +1.8 |
|  | [[Ixazomib (drug)]] 0.05 µM |  | +1.1 | +1.8 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -6.2 | -10.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.7 | -6.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -0.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.3 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -1.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -2.7 |
|  | [[Hydroxyurea (drug)]] 5 µM |  | -1.1 | -2.6 |
|  | [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | NAD(P)HX epimerase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q22 — chr1:156,591,756-156,609,507 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AIBP, MGC119143, MGC119144, MGC119145, YJEFN1; previously APOA1BP |
| Reactome | 3 pathways, smallest: Nicotinate metabolism; Metabolism of water-soluble vitamins and cofactors; Metabolism of vitamins and cofactors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCW5](https://www.uniprot.org/uniprotkb/Q8NCW5) (NAD(P)H-hydrate epimerase):

> Catalyzes the epimerization of the S- and R-forms of NAD(P)HX, a damaged form of NAD(P)H that is a result of enzymatic or heat-dependent hydration (By similarity). This is a prerequisite for the S-specific NAD(P)H-hydrate dehydratase to allow the repair of both epimers of NAD(P)HX (By similarity). Accelerates cholesterol efflux from endothelial cells to high-density lipoprotein (HDL) and thereby regulates angiogenesis.

**Summary**, from NCBI Gene [128240](https://www.ncbi.nlm.nih.gov/gene/128240):

> The product of this gene interacts with apolipoprotein A-I (apoA-I), the major apolipoprotein of high-density lipoproteins (HDLs). It is secreted into some bodily fluids, and its synthesis and secretion are stimulated in vitro by incubating cells with apoA-I. The human genome contains related pseudogenes. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18453](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18453) · Entrez [128240](https://www.ncbi.nlm.nih.gov/gene/128240) · UniProt [Q8NCW5](https://www.uniprot.org/uniprotkb/Q8NCW5) · Ensembl [ENSG00000163382](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163382)

## Data

Gene col 8681: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8681); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8681, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8681]; `tensor/DDL_lfc|DDL_z.npy` [8681]; `embed/gene_vectors.npy` [8681]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8681 or target_col == 8681). Every well: [[NAXE — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAXE.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
