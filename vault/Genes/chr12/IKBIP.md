---
symbol: "IKBIP"
type: "gene"
col: 9240
ensembl_id: "ENSG00000166130"
name: "IKBKB interacting protein"
location: "12q23.1"
module: 40
arm: "+"
pooled_cpm: 93.05
n_lines_expressing: 46
n_dd_up: 1
n_dd_down: 25
n_dd_up_clean: 1
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 5
direction_downstream: 6
tags: ["gene", "module/040"]
generated_by: "tahoemap"
---

# IKBIP

*IKBKB interacting protein* — 12q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (none with an alert); the strongest is [[GSK1059615 (drug)]] 0.5 µM: 1.43× (z +3.7, q 0.065, up in 24 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (LoVo 5.45×, RKO 4.61×, NCI-H460 2.73×, SW48 6.77×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 2.40×; ⚠ cell-cycle shift, explains ~0% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (RKO 2.18×).
> Pooled over the cell lines (median), lowered significantly by 25 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.352× (z -21.4, q 0e+00, down in 41 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[APAF1]] (+0.65, fdr 7e-06, ⚠ same locus), [[POLH]] (+0.65, fdr 1e-05), [[SPICE1]] (+0.63, fdr 9e-06), [[POM121C]] (+0.60, fdr 7e-06); moves opposite to [[PIGO]] (-0.60, fdr 1e-05), [[POGK]] (-0.57, fdr 1e-05), [[N6AMT1]] (-0.54, fdr 1e-05).
> It sits in the **+** arm of [[Module 040]] (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[LAD1]] → it (grade B ⚠); 6 go from it, the strongest it → [[CEP85L]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9240.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 7 lines (LoVo 5.45×, RKO 4.61×, NCI-H460 2.73×, SW48 6.77×, …; ⚠ cell-cycle shift, explains ~0% of this change); [[Epirubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H460 2.40×; ⚠ cell-cycle shift, explains ~0% of this change); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (RKO 2.18×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.43×** | +3.7 | 0.065 | 24/44 (A498, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.7 | 0.065 | 23/45 (LoVo, RKO, …) | top dose only |  |
| [[Arbutin (drug)]] 5 µM |  | 1.27× | +3.4 | 0.14 | 24/44 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | 1.16× | +3.1 | 0.32 | 15/44 (PANC-1, C32, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 9 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9240.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.352×** | -21.4 | 0e+00 | 41/44 (AsPC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.400×** | -12.7 | 1e-34 | 40/44 (AsPC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.486×** | -10.4 | 3e-23 | 35/44 (AsPC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.513×** | -9.6 | 7e-20 | 37/44 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.543×** | -8.8 | 1e-16 | 34/44 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.625×** | -6.8 | 1e-09 | 38/44 (HOP62, A-172, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.631×** | -6.6 | 3e-09 | 35/44 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.597×** | -6.5 | 5e-09 | 37/44 (HOP62, A-172, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.641×** | -6.4 | 9e-09 | 31/44 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.702×** | -5.0 | 3e-05 | 27/44 (NCI-H460, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.743×** | -4.3 | 1e-03 | 24/44 (NCI-H460, HS-578T, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.753×** | -4.1 | 0.002 | 25/44 (PANC-1, A-172, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.724×** | -4.1 | 0.002 | 27/43 (LOX-IMVI, HEC-1-A, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.769×** | -3.8 | 0.007 | 25/44 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.929× | -3.7 | 0.008 | 0/46 | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.790×** | -3.4 | 0.024 | 23/44 (HCT15, HS-578T, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.639×** | -3.4 | 0.025 | 23/45 (A-172, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.646×** | -3.3 | 0.030 | 19/44 (Hs 766T, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9240. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 181 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -34.1) |
| [[A-172 (line)]] | wt | 189 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -29.0) |
| [[H4 (line)]] | wt | 208 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -24.3) |
| [[A498 (line)]] | wt | 156 | 0 | 6 | — | [[Panobinostat (drug)]] 5 µM 0.376× (z -13.5) |
| [[HS-578T (line)]] | alt | 135 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -27.6) |
| [[hTERT-HPNE (line)]] | wt | 191 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -21.8) |
| [[NCI-H460 (line)]] | wt | 96.4 | 2 (2 ⚠) | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +15.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -19.8) |
| [[C32 (line)]] | wt | 104 | 1 (1 ⚠) | 4 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +12.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -15.7) |
| [[J82 (line)]] | alt | 134 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -21.6) |
| [[NCI-H1573 (line)]] | alt | 44.7 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.167× (z -13.4) |
| [[RPMI-7951 (line)]] | alt | 170 | 0 | 5 | — | [[Harringtonine (drug)]] 5 µM 0.247× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 153 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0730× (z -36.2) |
| [[Hs 766T (line)]] | wt | 134 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -17.4) |
| [[NCI-H1792 (line)]] | alt | 122 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -20.7) |
| [[A549 (line)]] | wt | 140 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.331× (z -10.4) |
| [[HCT15 (line)]] | alt | 100 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -14.1) |
| [[LoVo (line)]] | wt | 69.0 | 1 (1 ⚠) | 2 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.45× (z +20.4) ⚠ cell-cycle shift, explains ~0% of this change | [[Niclosamide (olamine) (drug)]] 5 µM 0.285× (z -10.1) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.331× (z -8.9) |
| [[RKO (line)]] | wt | 59.1 | 2 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.61× (z +16.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.18× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.377× (z -10.5) |
| [[SW 900 (line)]] | alt | 94.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.304× (z -14.7) |
| [[CFPAC-1 (line)]] | alt | 68.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -20.9) |
| [[HEC-1-A (line)]] | alt | 76.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -13.7) |
| [[HepG2_C3A (line)]] | wt | 51.7 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.51× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.358× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 122 | 1 (1 ⚠) | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.89× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.352× (z -13.7) |
| [[MIA PaCa-2 (line)]] | alt | 105 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.266× (z -12.4) |
| [[PANC-1 (line)]] | alt | 82.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -15.0) |
| [[SNU-1 (line)]] | wt | 87.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -14.8) |
| [[SW 1088 (line)]] | alt | 184 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -15.3) |
| [[C-33 A (line)]] | alt | 78.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.181× (z -12.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 94.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.126× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 26.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.316× (z -10.8) |
| [[NCI-H2030 (line)]] | alt | 64.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -16.5) |
| [[NCI-H23 (line)]] | alt | 160 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.413× (z -8.6) |
| [[NCI-H2347 (line)]] | alt | 59.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.482× (z -10.5) |
| [[SK-MEL-2 (line)]] | alt | 99.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -16.6) |
| [[SNU-423 (line)]] | alt | 101 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -18.1) |
| [[SW48 (line)]] | wt | 31.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.77× (z +13.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW480 (line)]] | alt | 54.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.398× (z -13.2) |
| [[A-427 (line)]] | wt | 73.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 79.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.3 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 22.6 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 20.0 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 62.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 83.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 81.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 20.6 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 33.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9240), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APAF1]] | +0.65 | +0.66 / +0.69 | both halves | 7e-06 | STRING 649; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[POLH]] | +0.65 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[SPICE1]] | +0.63 | +0.72 / +0.57 | both halves | 9e-06 |  |
| [[POM121C]] | +0.60 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[OST4]] | +0.60 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[SRP54]] | +0.60 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[ZNF654]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[GMCL1]] | +0.59 | +0.67 / +0.62 | both halves | 7e-06 |  |
| [[PRKRIP1]] | +0.59 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[MON2]] | +0.59 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[MINDY2]] | +0.58 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[SLC35E1]] | +0.58 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[GLTP]] | +0.57 | +0.56 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGO]] | -0.60 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[POGK]] | -0.57 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[N6AMT1]] | -0.54 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[FKTN]] | -0.54 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[BCL7B]] | -0.54 | -0.44 / -0.61 | both halves | 3e-05 |  |
| [[LAD1]] | -0.53 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[ATXN7L2]] | -0.53 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[TRIM16]] | -0.53 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[SYT14]] | -0.52 | -0.58 / -0.38 | both halves | 6e-05 |  |
| [[PSMD11]] | -0.52 | -0.60 / -0.50 | both halves | 1e-05 | pathway: Interleukin-1 family signaling |
| [[EWSR1]] | -0.50 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[PUF60]] | -0.50 | -0.49 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAD1]] | B | LAD1 activity lowers IKBIP's level | lines that do not express LAD1 (30) vs lines expressing it (20) | 2.38× higher at baseline in the lines without LAD1 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ST14, KDF1 |
| [[LGALS1]] | B | LGALS1 activity raises IKBIP's level | lines that do not express LGALS1 (12) vs lines expressing it (38) | 2.69× lower at baseline in the lines without LGALS1 | 0.011 | ⚠ within organs, on part of the lines; also absent: EMP3, AXL, VIM |
| [[MISP]] | B | MISP activity lowers IKBIP's level | lines that do not express MISP (23) vs lines expressing it (27) | 1.89× higher at baseline in the lines without MISP | 0.057 | ⚠ within organs, on part of the lines; also absent: GRB7, KRT18, MYO5B |
| [[P3H1]] | C | P3H1 activity raises IKBIP's level | lines that do not express P3H1 (4) vs lines expressing it (46) | 3.31× lower at baseline in the lines without P3H1 | 0.045 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CEP112, TIMP2, CNTNAP1; maybe low, not absent |
| [[CEP85L]] | C | CEP85L activity raises IKBIP's level | lines that do not express CEP85L (4) vs lines expressing it (46) | 3.97× lower at baseline in the lines without CEP85L | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ATP8B3, SOAT1, SPAG17; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CEP85L]] | C | IKBIP activity raises CEP85L's level | lines that do not express IKBIP (4) vs lines expressing it (46) | 5.34× lower at baseline in the lines without IKBIP | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SOAT1, NKAIN1, CEP85L; maybe low, not absent; co-absent with the target; its own permutation p |
| [[POM121]] | C | IKBIP activity raises POM121's level | lines that do not express IKBIP (4) vs lines expressing it (46) | 1.65× lower at baseline in the lines without IKBIP | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SOAT1, NKAIN1, CEP85L; maybe low, not absent; its own permutation p |
| [[VKORC1]] | C | IKBIP activity raises VKORC1's level | lines that do not express IKBIP (4) vs lines expressing it (46) | 3.19× lower at baseline in the lines without IKBIP | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SOAT1, NKAIN1, CEP85L; maybe low, not absent; its own permutation p |
| [[POM121C]] | C | IKBIP activity raises POM121C's level | lines that do not express IKBIP (4) vs lines expressing it (46) | 1.72× lower at baseline in the lines without IKBIP | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SOAT1, NKAIN1, CEP85L; maybe low, not absent; its own permutation p |
| [[GPN3]] | C | IKBIP activity raises GPN3's level | lines that do not express IKBIP (4) vs lines expressing it (46) | 1.54× lower at baseline in the lines without IKBIP | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SOAT1, NKAIN1, CEP85L; maybe low, not absent; its own permutation p |
| [[PRKRIP1]] | C | IKBIP activity raises PRKRIP1's level | lines that do not express IKBIP (4) vs lines expressing it (46) | 1.52× lower at baseline in the lines without IKBIP | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SOAT1, NKAIN1, CEP85L; maybe low, not absent |

## Where it sits

- **Module**: [[Module 040]] — Asparagine N-linked glycosylation; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.567). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (7.7, -19.8); signed map (-40.1, 19.2). **Vector** length 124, 42.4% of its response variance represented; |z| ≥ 3 in 967 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.7 | +3.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +0.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.1 | +0.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +0.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.7 | +0.5 |
|  | [[vincristine (drug)]] 0.05 µM |  | +2.2 | +2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +1.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.9 | +0.2 |
|  | [[Terfenadine (drug)]] 5 µM |  | +1.9 | +2.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | +1.7 | +2.9 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -6.3 | -12.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -6.1 | -6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.0 | -6.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.2 | -2.7 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | -4.6 | -6.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.3 | -3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.6 | -4.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.4 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | IKBKB interacting protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q23.1 — chr12:98,613,405-98,645,113 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ31051, IKIP |
| Reactome | 23 pathways, smallest: Regulation of NF-kappa B signaling; TAK1-dependent IKK and NF-kappa-B activation; MyD88 cascade initiated on plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [Q70UQ0](https://www.uniprot.org/uniprotkb/Q70UQ0) (Inhibitor of nuclear factor kappa-B kinase-interacting protein):

> Target of p53/TP53 with pro-apoptotic function.

**Summary**, from NCBI Gene [121457](https://www.ncbi.nlm.nih.gov/gene/121457):

> Predicted to be involved in response to X-ray. Predicted to act upstream of or within several processes, including obsolete negative regulation of NF-kappaB transcription factor activity; response to interleukin-1; and response to tumor necrosis factor. Located in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:26430](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26430) · Entrez [121457](https://www.ncbi.nlm.nih.gov/gene/121457) · UniProt [Q70UQ0](https://www.uniprot.org/uniprotkb/Q70UQ0) · Ensembl [ENSG00000166130](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166130)

## Data

Gene col 9240: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9240); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9240, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9240]; `tensor/DDL_lfc|DDL_z.npy` [9240]; `embed/gene_vectors.npy` [9240]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9240 or target_col == 9240). Every well: [[IKBIP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IKBIP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
