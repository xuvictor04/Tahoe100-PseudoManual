---
symbol: "SLC26A2"
type: "gene"
col: 7923
ensembl_id: "ENSG00000155850"
name: "solute carrier family 26 member 2"
location: "5q32"
module: 98
arm: "+"
pooled_cpm: 29.12
n_lines_expressing: 46
n_dd_up: 58
n_dd_down: 10
n_dd_up_clean: 42
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 4
direction_downstream: 7
tags: ["gene", "module/098"]
generated_by: "tahoemap"
---

# SLC26A2

*solute carrier family 26 member 2* — 5q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 58 drug-doses (16 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.93× (z +22.3, q 0e+00, up in 37 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (3 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.336× (z -8.4, q 4e-14, down in 31 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FKBP5]] (+0.63, fdr 7e-06), [[ADAMTS9]] (+0.61, fdr 1e-05), [[STXBP5-AS1]] (+0.59, fdr 1e-05); moves opposite to [[TMOD1]] (-0.57, fdr 4e-05), [[DOK5]] (-0.55, fdr 1e-05), [[GDPD3]] (-0.52, fdr 3e-05).
> It is in [[Module 098]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[MAPK4]] → it (grade B ⚠); 7 go from it, the strongest it → [[SLC35B4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 63 in all, 17 with an alert ⚠; shown: the 15 strongest and the 9 next strongest without an alert. 58 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7923.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.93×** | +22.3 | 0e+00 | 37/43 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.05×** | +16.3 | 0e+00 | 35/39 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.75×** | +14.2 | 9e-44 | 26/28 (A549, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.19×** | +10.6 | 4e-24 | 26/35 (A498, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.70×** | +7.8 | 8e-13 | 28/43 (NCI-H460, SK-MEL-2, …) | all doses, flat |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.44×** | +7.5 | 8e-12 | 29/44 (Hs 766T, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.63×** | +7.1 | 9e-11 | 27/44 (A549, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.61×** | +7.0 | 2e-10 | 22/44 (A549, A498, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.62×** | +6.7 | 9e-10 | 25/43 (Hs 766T, HOP62, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM |  | **1.36×** | +6.3 | 2e-08 | 20/44 (NCI-H460, Panc 03.27, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.35×** | +6.2 | 3e-08 | 22/44 (HEC-1-A, A-172, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.55×** | +6.1 | 4e-08 | 28/44 (Hs 766T, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.49×** | +5.9 | 2e-07 | 23/44 (HOP62, A498, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~33% of this change | **1.50×** | +5.7 | 6e-07 | 19/41 (LoVo, A-172, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.45×** | +5.5 | 2e-06 | 20/43 (NCI-H460, SK-MEL-2, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.48×** | +5.5 | 2e-06 | 20/44 (A549, NCI-H460, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.43×** | +5.2 | 5e-06 | 21/44 (SK-MEL-2, NCI-H460, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.42×** | +5.1 | 8e-06 | 19/44 (A549, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.43×** | +4.9 | 3e-05 | 19/43 (A549, NCI-H460, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.37×** | +4.6 | 9e-05 | 20/43 (A549, NCI-H460, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.37×** | +4.6 | 1e-04 | 21/44 (A549, SK-MEL-2, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.25×** | +4.6 | 1e-04 | 17/44 (A549, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.36×** | +4.5 | 1e-04 | 20/43 (NCI-H460, A549, …) | all doses, flat |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.36×** | +4.5 | 1e-04 | 20/43 (SNU-423, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 3 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7923.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.336×** | -8.4 | 4e-14 | 31/44 (A-427, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.405×** | -6.9 | 1e-09 | 26/44 (SK-MEL-2, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.647×** | -6.4 | 3e-08 | 26/44 (A-427, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.655×** | -6.2 | 7e-08 | 25/44 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.665×** | -6.0 | 2e-07 | 26/43 (C-33 A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.673×** | -5.8 | 6e-07 | 22/43 (C32, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.773×** | -5.4 | 7e-06 | 19/44 (HEC-1-A, SNU-1, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **0.584×** | -4.1 | 0.003 | 13/24 (A-427, LoVo, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.758×** | -4.1 | 0.003 | 18/43 (A-427, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **0.768×** | -3.9 | 0.006 | 11/44 (HEC-1-A, SHP-77, …) | rises with dose |  |
| [[TAK-733 (drug)]] 0.05 µM |  | 0.804× | -3.0 | 0.13 | 7/44 (AN3 CA, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.41 per unit of S-phase module lfc, -0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7923. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 21.2 | 23 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.67× (z +13.6) | — |
| [[NCI-H460 (line)]] | wt | 46.9 | 14 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.35× (z +12.9) | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -9.1) ⚠ cell-cycle shift, explains ~8% of this change |
| [[SK-MEL-2 (line)]] | alt | 103 | 13 | 2 (2 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 5.45× (z +11.5) | [[Bortezomib (drug)]] 0.05 µM 0.192× (z -10.7) ⚠ cell-cycle shift, explains ~24% of this change |
| [[Hs 766T (line)]] | wt | 21.2 | 9 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.96× (z +14.4) | — |
| [[NCI-H1573 (line)]] | alt | 78.7 | 6 | 1 (1 ⚠) | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 8.38× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.228× (z -8.9) ⚠ cell-cycle shift, explains ~8% of this change |
| [[C32 (line)]] | wt | 94.8 | 0 | 5 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.105× (z -10.9) |
| [[A498 (line)]] | wt | 14.0 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +13.7) | — |
| [[SNU-423 (line)]] | alt | 14.7 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.63× (z +11.6) | — |
| [[A-427 (line)]] | wt | 56.5 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 2.73× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[PH-797804 (drug)]] 5 µM 0.0990× (z -10.8) |
| [[PANC-1 (line)]] | alt | 87.5 | 0 | 3 (1 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.338× (z -10.0) |
| [[SW480 (line)]] | alt | 14.2 | 2 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +16.5) | [[Digitoxin (drug)]] 5 µM 0.333× (z -8.7) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 26.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +11.1) | — |
| [[C-33 A (line)]] | alt | 31.3 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.168× (z -10.0) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 14.5 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.34× (z +14.6) | — |
| [[SHP-77 (line)]] | alt | 15.6 | 2 | 0 | [[Dexamethasone (drug)]] 0.05 µM 6.90× (z +8.9) | — |
| [[CFPAC-1 (line)]] | alt | 8.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.07× (z +11.4) | — |
| [[H4 (line)]] | wt | 13.2 | 0 | 1 | — | [[Saquinavir (drug)]] 0.05 µM 0.0748× (z -9.8) |
| [[HEC-1-A (line)]] | alt | 38.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.59× (z +10.4) | — |
| [[HOP62 (line)]] | alt | 14.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.17× (z +13.3) | — |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.64× (z +9.1) | — |
| [[J82 (line)]] | alt | 23.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +8.8) | — |
| [[KATO III (line)]] | alt | 15.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +9.8) | — |
| [[LoVo (line)]] | wt | 33.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +12.3) | — |
| [[NCI-H1792 (line)]] | alt | 8.93 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.42× (z +11.2) | — |
| [[NCI-H23 (line)]] | alt | 31.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 3.20× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[SW1417 (line)]] | alt | 22.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +8.7) | — |
| [[AN3 CA (line)]] | alt | 43.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.84 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 18.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.10 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 9.83 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.00 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 66.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 6.28 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7923), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FKBP5]] | +0.63 | +0.63 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[ADAMTS9]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 | pathway: Diseases of glycosylation |
| [[STXBP5-AS1]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[YAP1]] | +0.59 | +0.56 / +0.44 | both halves | 3e-05 |  |
| [[STK39]] | +0.58 | +0.47 / +0.54 | both halves | 2e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[SIPA1L1]] | +0.57 | +0.46 / +0.55 | both halves | 2e-05 |  |
| [[MAOA]] | +0.57 | +0.57 / +0.61 | both halves | 9e-06 | pathway: Diseases of metabolism |
| [[PTPRG]] | +0.56 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[TOP1]] | +0.56 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[TRMT6]] | +0.56 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[AHNAK]] | +0.55 | +0.52 / +0.44 | both halves | 3e-05 |  |
| [[FOXC2]] | +0.55 | +0.61 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMOD1]] | -0.57 | -0.59 / -0.40 | both halves | 4e-05 |  |
| [[DOK5]] | -0.55 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[GDPD3]] | -0.52 | -0.55 / -0.44 | both halves | 3e-05 |  |
| [[ARID5A]] | -0.51 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[RASA4B]] | -0.50 | -0.45 / -0.36 | both halves | 9e-05 |  |
| [[SEZ6L2]] | -0.50 | -0.54 / -0.35 | both halves | 1e-04 |  |
| [[NMB]] | -0.49 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[PTGIS]] | -0.49 | -0.34 / -0.54 | both halves | 1e-04 |  |
| [[LRP1]] | -0.48 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[MAF]] | -0.48 | -0.43 / -0.46 | both halves | 3e-05 | pathway: HALLMARK_ANDROGEN_RESPONSE |
| [[DBP]] | -0.48 | -0.38 / -0.39 | both halves | 6e-05 |  |
| [[EPB41]] | -0.47 | -0.40 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAPK4]] | B | MAPK4 activity raises SLC26A2's level | lines that do not express MAPK4 (35) vs lines expressing it (15) | 2.11× lower at baseline in the lines without MAPK4 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000289418, SLC15A5, LHFPL3-AS1 |
| [[LDLRAD3]] | B | LDLRAD3 activity raises SLC26A2's level | lines that do not express LDLRAD3 (7) vs lines expressing it (43) | 2.13× lower at baseline in the lines without LDLRAD3 | 0.048 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[KRT7]] | B | KRT7 activity strengthens SLC26A2's drug response | lines that do not express KRT7 (32) vs lines expressing it (12) | the lines without KRT7 respond 0.67× as strongly (z diff +0.89); strongest at Panobinostat 0.5 µM: 1.30x vs 2.05x (z diff +2.2) | 0.065 | ⚠ within organs, on part of the lines; also absent: VSIG1, GSDMC, SERPINB3; target measured in part of the lines; both ways; artifact flags |
| [[CREB3L1]] | B | CREB3L1 activity lowers SLC26A2's level | lines that do not express CREB3L1 (24) vs lines expressing it (26) | 1.67× higher at baseline in the lines without CREB3L1 | 0.087 | ⚠ within organs, on part of the lines; also absent: UGT1A6, UGT1A9, UGT1A1 |

### Downstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC35B4]] | C | SLC26A2 activity raises SLC35B4's level | lines that do not express SLC26A2 (4) vs lines expressing it (46) | 2.34× lower at baseline in the lines without SLC26A2 | 0.014 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MIR4435-2HG, EPB41L2, CEP85L; maybe low, not absent |
| [[MOSMO]] | C | SLC26A2 activity raises MOSMO's level | lines that do not express SLC26A2 (4) vs lines expressing it (46) | 1.48× lower at baseline in the lines without SLC26A2 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MIR4435-2HG, EPB41L2, CEP85L; maybe low, not absent |
| [[CAPN12]] | C | SLC26A2 activity lowers CAPN12's level | lines that do not express SLC26A2 (4) vs lines expressing it (46) | 1.70× higher at baseline in the lines without SLC26A2 | 0.078 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MIR4435-2HG, EPB41L2, CEP85L; maybe low, not absent |
| [[AKAP12]] | C | SLC26A2 activity raises AKAP12's level | lines that do not express SLC26A2 (4) vs lines expressing it (46) | 6.02× lower at baseline in the lines without SLC26A2 | 0.092 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MIR4435-2HG, EPB41L2, CEP85L; maybe low, not absent |
| [[B3GNT5]] | C | SLC26A2 activity lowers B3GNT5's level | lines that do not express SLC26A2 (4) vs lines expressing it (46) | 2.53× higher at baseline in the lines without SLC26A2 | 0.093 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MIR4435-2HG, EPB41L2, CEP85L; maybe low, not absent |
| [[LDLRAD3]] | C | SLC26A2 activity raises LDLRAD3's level | lines that do not express SLC26A2 (4) vs lines expressing it (46) | 2.35× lower at baseline in the lines without SLC26A2 | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MIR4435-2HG, EPB41L2, CEP85L; maybe low, not absent |
| [[CCND3]] | C | SLC26A2 activity lowers CCND3's level | lines that do not express SLC26A2 (4) vs lines expressing it (46) | 2.02× higher at baseline in the lines without SLC26A2 | 0.0997 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: MIR4435-2HG, EPB41L2, CEP85L; maybe low, not absent |

## Where it sits

- **Module**: [[Module 098]]; 48 genes; every member is in the + arm (projection on the module's main direction 0.679). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (31.6, 15.2); signed map (17.5, 33.1). **Vector** length 96.6, 23.8% of its response variance represented; |z| ≥ 3 in 1,351 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Clobetasol propionate (drug)]] 0.05 µM |  | +4.6 | +7.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +4.5 | +4.5 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +4.5 | +3.9 |
|  | [[Dexamethasone (drug)]] 5 µM |  | +4.4 | +2.7 |
|  | [[Budesonide (drug)]] 5 µM |  | +4.2 | +2.8 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.5 | -5.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | -3.0 | -2.5 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | -2.9 | -4.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.7 | -2.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.5 | -1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.5 | -0.4 |
|  | [[Cobimetinib (drug)]] 0.05 µM |  | -2.5 | -0.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.2 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 26 member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q32 — chr5:149,960,758-149,993,455 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DTDST; previously DTD |
| Gene groups (HGNC) | Solute carrier family 26 |
| Hallmark sets | ANDROGEN_RESPONSE, ESTROGEN_RESPONSE_LATE, ESTROGEN_RESPONSE_EARLY |
| Reactome | 12 pathways, smallest: Inorganic anion exchange by SLC26 transporters; Transport and metabolism of PAPS; SLC-mediated transport of inorganic anions |
| Matched by | ensembl_id |

**Function**, from UniProt [P50443](https://www.uniprot.org/uniprotkb/P50443) (Sulfate transporter):

> Sulfate transporter which mediates sulfate uptake into chondrocytes in order to maintain adequate sulfation of proteoglycans which is needed for cartilage development. Mediates electroneutral anion exchange of sulfate ions for oxalate ions and of sulfate and oxalate ions for chloride ions. Mediates exchange of sulfate and oxalate ions for hydroxyl ions and of chloride ions for bromide, iodide and nitrate ions (By similarity). The coupling of sulfate transport to both hydroxyl and chloride ions …

**Summary**, from NCBI Gene [1836](https://www.ncbi.nlm.nih.gov/gene/1836):

> The diastrophic dysplasia sulfate transporter is a transmembrane glycoprotein implicated in the pathogenesis of several human chondrodysplasias. It apparently is critical in cartilage for sulfation of proteoglycans and matrix organization. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10994](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10994) · Entrez [1836](https://www.ncbi.nlm.nih.gov/gene/1836) · UniProt [P50443](https://www.uniprot.org/uniprotkb/P50443) · Ensembl [ENSG00000155850](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000155850)

## Data

Gene col 7923: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7923); `tables/drug_effects.parquet` (74 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7923, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7923]; `tensor/DDL_lfc|DDL_z.npy` [7923]; `embed/gene_vectors.npy` [7923]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7923 or target_col == 7923). Every well: [[SLC26A2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC26A2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
