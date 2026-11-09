---
symbol: "MAP7D2"
type: "gene"
col: 11526
ensembl_id: "ENSG00000184368"
name: "MAP7 domain containing 2"
location: "Xp22.12"
module: 37
arm: "+"
pooled_cpm: 21.5
n_lines_expressing: 47
n_dd_up: 45
n_dd_down: 1
n_dd_up_clean: 35
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 2
tags: ["gene", "module/037"]
generated_by: "tahoemap"
---

# MAP7D2

*MAP7 domain containing 2* — Xp22.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 45 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.68× (z +32.4, q 0e+00, up in 42 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Retinoic acid (drug)]] 0.05 µM: 0.728× (z -3.9, q 0.067, down in 11 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SW480 0.366×, PANC-1 0.322×); [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.219×, NCI-H2347 0.219×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H2347 0.204×, H4 0.161×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change); [[Belumosudil (drug)]] 5 µM in 2 lines (NCI-H1573 0.214×, BT-474 0.101×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (A498 0.350×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLRD1]] (+0.71, fdr 7e-06), [[WDR49]] (+0.71, fdr 7e-06), [[SNX31]] (+0.71, fdr 7e-06); moves opposite to [[BRD7]] (-0.54, fdr 4e-05), [[WDR7]] (-0.53, fdr 1e-04), [[MTMR9]] (-0.52, fdr 1e-05).
> It is in [[Module 037]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[CYP27A1]] → it (grade B ⚠); 2 go from it, the strongest it → [[LINC00640]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 45 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11526.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.68×** | +32.4 | 0e+00 | 42/43 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **6.88×** | +22.4 | 0e+00 | 35/40 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **6.56×** | +21.8 | 0e+00 | 40/43 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.83×** | +17.7 | 0e+00 | 34/44 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **3.51×** | +15.1 | 0e+00 | 35/45 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.51×** | +15.1 | 0e+00 | 34/43 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.63×** | +11.2 | 2e-27 | 31/40 (NCI-H460, LoVo, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **2.45×** | +10.8 | 2e-25 | 26/43 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.36×** | +10.3 | 3e-23 | 33/44 (MIA PaCa-2, NCI-H460, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.27×** | +9.9 | 2e-21 | 31/45 (NCI-H1792, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **2.13×** | +9.1 | 5e-18 | 27/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.05×** | +8.7 | 2e-16 | 33/45 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.57×** | +7.7 | 6e-13 | 24/45 (A-172, SW1417, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +7.7 | 7e-13 | 32/45 (PANC-1, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +7.3 | 9e-12 | 22/39 (MIA PaCa-2, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **3.07×** | +7.1 | 5e-11 | 30/43 (HEC-1-A, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +7.0 | 1e-10 | 20/45 (A549, SNU-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.66×** | +6.1 | 3e-08 | 20/43 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11526.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (SW480 0.366×, PANC-1 0.322×); [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.219×, NCI-H2347 0.219×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H2347 0.204×, H4 0.161×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change); [[Belumosudil (drug)]] 5 µM in 2 lines (NCI-H1573 0.214×, BT-474 0.101×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (A498 0.350×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.728×** | -3.9 | 0.067 | 11/45 (HOP62, COLO 205, …) | inconsistent across doses |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.753× | -3.4 | 0.17 | 16/45 (HOP62, CHP-212, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | 0.772× | -3.1 | 0.26 | 13/42 (HCT15, SNU-423, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | 0.768× | -3.1 | 0.26 | 17/44 (NCI-H1573, BT-474, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11526. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 12.3 | 12 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 24.2× (z +17.7) | — |
| [[A498 (line)]] | wt | 62.6 | 5 (3 ⚠) | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.97× (z +14.5) | [[Ixazomib citrate (drug)]] 5 µM 0.350× (z -10.0) |
| [[MIA PaCa-2 (line)]] | alt | 11.9 | 7 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.68× (z +14.2) | — |
| [[BT-474 (line)]] | alt | 19.8 | 5 (1 ⚠) | 1 | [[Digitoxin (drug)]] 5 µM 17.2× (z +12.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.85× (z +11.6) | [[Belumosudil (drug)]] 5 µM 0.101× (z -9.4) |
| [[LoVo (line)]] | wt | 8.20 | 6 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 14.5× (z +16.9) | — |
| [[SW48 (line)]] | wt | 18.6 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +12.7) | — |
| [[C32 (line)]] | wt | 13.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.9× (z +15.0) | — |
| [[HEC-1-A (line)]] | alt | 41.6 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +12.9) | — |
| [[HS-578T (line)]] | alt | 7.39 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.8× (z +15.2) | — |
| [[SW480 (line)]] | alt | 90.0 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.366× (z -12.2) |
| [[A-172 (line)]] | wt | 8.49 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.6× (z +16.5) | — |
| [[HOP62 (line)]] | alt | 30.6 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.54× (z +15.1) | — |
| [[KATO III (line)]] | alt | 7.66 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.38× (z +12.3) | — |
| [[LOX-IMVI (line)]] | wt | 9.46 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.90× (z +11.7) | — |
| [[NCI-H1792 (line)]] | alt | 10.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.9× (z +12.7) | — |
| [[NCI-H2347 (line)]] | alt | 33.6 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.204× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[Panc 03.27 (line)]] | alt | 12.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.4× (z +15.2) | — |
| [[SW 900 (line)]] | alt | 11.8 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.13× (z +12.8) | — |
| [[SW1417 (line)]] | alt | 5.61 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.1× (z +14.7) | — |
| [[C-33 A (line)]] | alt | 61.3 | 1 | 1 (1 ⚠) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +9.1) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[CFPAC-1 (line)]] | alt | 15.2 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.38× (z +15.0) | — |
| [[COLO 205 (line)]] | alt | 22.6 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.95× (z +10.0) | — |
| [[H4 (line)]] | wt | 27.5 | 1 | 1 (1 ⚠) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 7.78× (z +9.1) | [[Dinaciclib (drug)]] 0.5 µM 0.161× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[HT-29 (line)]] | alt | 7.95 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.25× (z +12.1) | — |
| [[LS 180 (line)]] | wt | 6.74 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 11.9× (z +9.5) | — |
| [[NCI-H2030 (line)]] | alt | 13.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.10× (z +13.1) | — |
| [[NCI-H23 (line)]] | alt | 7.25 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.9× (z +12.4) | — |
| [[PANC-1 (line)]] | alt | 18.9 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.43× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | [[Homoharringtonine (drug)]] 0.5 µM 0.322× (z -9.5) |
| [[RKO (line)]] | wt | 7.04 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.8× (z +11.2) | — |
| [[SNU-423 (line)]] | alt | 14.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.66× (z +14.0) | — |
| [[HCT15 (line)]] | alt | 19.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.27× (z +9.2) | — |
| [[HepG2_C3A (line)]] | wt | 20.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.06× (z +12.3) | — |
| [[Hs 766T (line)]] | wt | 5.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +11.6) | — |
| [[NCI-H1573 (line)]] | alt | 50.8 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.214× (z -10.1) |
| [[SHP-77 (line)]] | alt | 5.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.44× (z +11.0) | — |
| [[SK-MEL-2 (line)]] | alt | 5.95 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.26× (z +10.2) | — |
| [[SNU-1 (line)]] | wt | 11.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 12.2× (z +8.8) | — |
| [[A-427 (line)]] | wt | 4.85 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.97 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.87 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.95 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11526), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLRD1]] | +0.71 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[WDR49]] | +0.71 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[SNX31]] | +0.71 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[CD27-AS1]] | +0.71 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[ADCY10]] | +0.70 | +0.60 / +0.69 | both halves | 7e-06 |  |
| [[LINC02763]] | +0.65 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[CD247]] | +0.65 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[CASS4]] | +0.65 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[C9orf153]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[AS3MT]] | +0.64 | +0.65 / +0.47 | both halves | 2e-05 |  |
| [[TMEM269]] | +0.63 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[LINC02762]] | +0.62 | +0.56 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BRD7]] | -0.54 | -0.48 / -0.42 | both halves | 4e-05 |  |
| [[WDR7]] | -0.53 | -0.35 / -0.40 | both halves | 1e-04 |  |
| [[MTMR9]] | -0.52 | -0.51 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP27A1]] | B | CYP27A1 activity raises MAP7D2's level | lines that do not express CYP27A1 (10) vs lines expressing it (40) | 1.94× lower at baseline in the lines without CYP27A1 | 0.093 | ⚠ within organs, on part of the lines; also absent: RNF217, ENSG00000224905, ESYT3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers MAP7D2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 9.2% of all compounds | 0.095 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC00640]] | C | MAP7D2 activity raises LINC00640's level | lines that do not express MAP7D2 (3) vs lines expressing it (47) | 2.06× lower at baseline in the lines without MAP7D2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LINC01482, TNNI3K, AOAH; maybe low, not absent |
| [[AS3MT]] | C | MAP7D2 activity raises AS3MT's level | lines that do not express MAP7D2 (3) vs lines expressing it (47) | 1.44× lower at baseline in the lines without MAP7D2 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: LINC01482, TNNI3K, AOAH; maybe low, not absent |

## Where it sits

- **Module**: [[Module 037]]; 123 genes; every member is in the + arm (projection on the module's main direction 0.720). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (25.2, -17.4); signed map (11.0, 3.5). **Vector** length 97.4, 23.0% of its response variance represented; |z| ≥ 3 in 1,275 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +32.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +7.2 | +21.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.0 | +22.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +6.1 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +7.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +10.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.8 | +3.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +3.3 | +3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | +7.7 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -6.1 | -3.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.1 | -0.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.0 | -1.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.2 | +0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.0 | -3.1 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.5 | -2.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.4 | -0.9 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.0 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | MAP7 domain containing 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.12 — chrX:20,006,713-20,116,907 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14503 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Microtubule associated protein 7 family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96T17](https://www.uniprot.org/uniprotkb/Q96T17) (MAP7 domain-containing protein 2):

> Microtubule-stabilizing protein that plays a role in the control of cell motility and neurite outgrowth via direct binding to the microtubule (By similarity). Acts as a critical cofactor for kinesin transport. In the proximal axon, regulates kinesin-1 family members, KIF5A, KIF5B and KIF5C recruitment to microtubules and contributes to kinesin-1-mediated transport in the axons (By similarity).

**Summary**, from NCBI Gene [256714](https://www.ncbi.nlm.nih.gov/gene/256714):

> Predicted to enable kinesin binding activity and microtubule binding activity. Predicted to be involved in axon development and microtubule cytoskeleton organization. Predicted to be located in microtubule cytoskeleton; midbody; and neuron projection. Predicted to be active in microtubule cytoskeleton. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:25899](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25899) · Entrez [256714](https://www.ncbi.nlm.nih.gov/gene/256714) · UniProt [Q96T17](https://www.uniprot.org/uniprotkb/Q96T17) · Ensembl [ENSG00000184368](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000184368)

## Data

Gene col 11526: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11526); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11526, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11526]; `tensor/DDL_lfc|DDL_z.npy` [11526]; `embed/gene_vectors.npy` [11526]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11526 or target_col == 11526). Every well: [[MAP7D2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP7D2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
