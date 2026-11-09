---
symbol: "SLC39A8"
type: "gene"
col: 6248
ensembl_id: "ENSG00000138821"
name: "solute carrier family 39 member 8"
location: "4q24"
module: 106
arm: "+"
pooled_cpm: 57.26
n_lines_expressing: 38
n_dd_up: 33
n_dd_down: 27
n_dd_up_clean: 26
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 5
direction_downstream: 5
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# SLC39A8

*solute carrier family 39 member 8* — 4q24

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 33 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.97× (z +19.3, q 0e+00, up in 25 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.562× (z -11.6, q 4e-28, down in 22 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC16A7]] (+0.65, fdr 1e-05), [[EFEMP1]] (+0.62, fdr 1e-05), [[B4GALT1]] (+0.62, fdr 1e-05); moves opposite to [[SLC9A3R2]] (-0.52, fdr 3e-05), [[TMCC3]] (-0.51, fdr 3e-05), [[DUSP18]] (-0.47, fdr 4e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[EYA4]] → it (grade B ⚠); 5 go from it, the strongest it → [[LAMB1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 33 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6248.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +19.3 | 0e+00 | 25/37 (A-172, HOP62, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.60×** | +19.2 | 0e+00 | 25/33 (LoVo, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.63×** | +13.9 | 2e-41 | 28/36 (Panc 03.27, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.04×** | +13.8 | 7e-41 | 19/28 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.91×** | +12.1 | 2e-31 | 21/30 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.75×** | +11.3 | 1e-27 | 28/37 (NCI-H2347, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.65×** | +10.1 | 3e-22 | 27/35 (NCI-H1573, A-172, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.44×** | +7.3 | 1e-11 | 16/35 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +7.3 | 2e-11 | 15/38 (C32, HOP62, …) | top dose only | cell-cycle shift (explains ~18% here) |
| [[Budesonide (drug)]] 0.5 µM |  | **1.41×** | +6.9 | 2e-10 | 15/36 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.41×** | +6.9 | 3e-10 | 16/35 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.39×** | +6.1 | 5e-08 | 16/35 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.35×** | +6.0 | 8e-08 | 16/38 (NCI-H1573, H4, …) | inconsistent across doses |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.35×** | +6.0 | 8e-08 | 14/36 (NCI-H1573, HOP62, …) | all doses, flat |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.34×** | +5.9 | 2e-07 | 15/36 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.34×** | +5.7 | 4e-07 | 15/37 (NCI-H1573, NCI-H460, …) | all doses, flat |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.33×** | +5.7 | 4e-07 | 14/35 (NCI-H1573, HT-29, …) | two highest doses |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +5.7 | 4e-07 | 18/36 (NCI-H1573, NCI-H2347, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6248.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.562×** | -11.6 | 4e-28 | 22/36 (NCI-H460, RKO, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.612×** | -9.8 | 2e-20 | 23/36 (A549, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.623×** | -9.5 | 5e-19 | 23/35 (RKO, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.630×** | -9.3 | 3e-18 | 23/36 (NCI-H23, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.749×** | -8.2 | 3e-14 | 22/37 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.666×** | -8.2 | 3e-14 | 25/36 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.681×** | -7.7 | 1e-12 | 24/36 (NCI-H460, RKO, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.689×** | -7.5 | 5e-12 | 22/35 (NCI-H460, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.685×** | -7.3 | 2e-11 | 20/36 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.701×** | -7.1 | 6e-11 | 19/35 (NCI-H23, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.715×** | -6.7 | 1e-09 | 24/35 (NCI-H460, KATO III, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.739×** | -6.1 | 7e-08 | 19/36 (NCI-H460, RKO, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.743×** | -5.7 | 4e-07 | 16/35 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.760×** | -5.5 | 2e-06 | 18/35 (NCI-H460, C32, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.768×** | -5.3 | 5e-06 | 15/35 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.765×** | -4.9 | 3e-05 | 10/35 (NCI-H460, SNU-423, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.782×** | -4.9 | 3e-05 | 12/35 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.22 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6248. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 639 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -18.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.0699× (z -15.5) |
| [[NCI-H1573 (line)]] | alt | 38.2 | 9 | 0 | [[Citalopram (hydrobromide) (drug)]] 0.05 µM 4.85× (z +9.8) | — |
| [[A-172 (line)]] | wt | 25.1 | 4 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.28× (z +10.8) | — |
| [[LoVo (line)]] | wt | 24.0 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.31× (z +13.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 31.3 | 4 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 2.31× (z +9.6) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.28× (z +9.5) | — |
| [[RKO (line)]] | wt | 47.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.158× (z -14.4) |
| [[SW480 (line)]] | alt | 16.8 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.42× (z +11.3) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 0.5 µM 0.314× (z -9.3) |
| [[A549 (line)]] | wt | 55.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -9.1) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.157× (z -8.5) |
| [[HCT15 (line)]] | alt | 15.5 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 10.1× (z +9.5) ⚠ toxic; transcription drop | [[Hydroxyurea (drug)]] 0.05 µM 0.0695× (z -10.1) |
| [[HT-29 (line)]] | alt | 17.8 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 41.3 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 4.36× (z +12.6) | — |
| [[A498 (line)]] | wt | 56.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.74× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 29.0 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 2.41× (z +9.4) | — |
| [[HEC-1-A (line)]] | alt | 21.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 18.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +9.7) | — |
| [[hTERT-HPNE (line)]] | wt | 37.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +10.0) ⚠ cell-cycle shift, would explain all of this change | — |
| [[LS 180 (line)]] | wt | 20.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.15× (z +9.3) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 97.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -9.1) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.286× (z -9.7) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 8.36 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.7 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.00 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 10.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.90 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 53.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 29.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 55.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.05 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 14.0 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.38 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 65.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 66.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 71.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.95 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 11.6 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.03 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 55.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.26 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 37.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6248), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC16A7]] | +0.65 | +0.54 / +0.61 | both halves | 1e-05 | pathway: SLC-mediated transmembrane transport |
| [[EFEMP1]] | +0.62 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[B4GALT1]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[PON2]] | +0.58 | +0.41 / +0.53 | both halves | 4e-05 |  |
| [[ADGRG2]] | +0.56 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[CPS1]] | +0.55 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[RHOBTB1]] | +0.55 | +0.49 / +0.52 | both halves | 1e-05 |  |
| [[IGFBP4]] | +0.53 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[TGFB2]] | +0.52 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[CTSC]] | +0.51 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[PTGFRN]] | +0.51 | +0.45 / +0.47 | both halves | 3e-05 |  |
| [[PDE4D]] | +0.51 | +0.56 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC9A3R2]] | -0.52 | -0.45 / -0.48 | both halves | 3e-05 |  |
| [[TMCC3]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[DUSP18]] | -0.47 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[C11orf68]] | -0.47 | -0.34 / -0.52 | both halves | 1e-04 |  |
| [[DYNLL1]] | -0.45 | -0.29 / -0.43 | both halves | 2e-04 |  |
| [[SIRT7]] | -0.44 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[PLEKHN1]] | -0.44 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[RAP2B]] | -0.43 | -0.29 / -0.43 | both halves | 2e-04 |  |
| [[FMNL1-DT]] | -0.43 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[CSTB]] | -0.42 | -0.43 / -0.36 | both halves | 1e-04 |  |
| [[DEF6]] | -0.42 | -0.32 / -0.40 | both halves | 1e-04 |  |
| [[NECAP2]] | -0.42 | -0.31 / -0.46 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EYA4]] | B | EYA4 activity raises SLC39A8's level | lines that do not express EYA4 (30) vs lines expressing it (20) | 2.59× lower at baseline in the lines without EYA4 | 0.046 | ⚠ within organs, on part of the lines; also absent: SNAP25, BICC1, IL31RA |
| [[RHOBTB1]] | B | RHOBTB1 activity raises SLC39A8's level | lines that do not express RHOBTB1 (8) vs lines expressing it (42) | 2.87× lower at baseline in the lines without RHOBTB1 | 0.049 | ⚠ within organs, on part of the lines; also absent: KLF12, LAMB1, PLCB4 |
| [[LAMB1]] | B | LAMB1 activity raises SLC39A8's level | lines that do not express LAMB1 (7) vs lines expressing it (43) | 2.66× lower at baseline in the lines without LAMB1 | 0.063 | ⚠ within organs, on part of the lines; also absent: TGFBR2, SDC4, VDR |
| [[NR3C1]] | B | NR3C1 activity raises SLC39A8's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 5.9% of all compounds | 0.079 | ⚠ off-target possible; 3 compounds |
| [[GPRIN3]] | B | GPRIN3 activity raises SLC39A8's level | lines that do not express GPRIN3 (35) vs lines expressing it (15) | 2.20× lower at baseline in the lines without GPRIN3 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AKR1B10, ENSG00000230975, ENSG00000237031 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LAMB1]] | B | SLC39A8 activity raises LAMB1's level | lines that do not express SLC39A8 (12) vs lines expressing it (38) | 2.73× lower at baseline in the lines without SLC39A8 | 0.010 | ⚠ within organs, on part of the lines; also absent: PLCB4, PAG1, RGS17 |
| [[RAB27A]] | B | SLC39A8 activity raises RAB27A's level | lines that do not express SLC39A8 (12) vs lines expressing it (38) | 1.85× lower at baseline in the lines without SLC39A8 | 0.049 | ⚠ within organs, on part of the lines; also absent: PLCB4, PAG1, RGS17 |
| [[EYA4]] | B | SLC39A8 activity raises EYA4's level | lines that do not express SLC39A8 (12) vs lines expressing it (38) | 3.83× lower at baseline in the lines without SLC39A8 | 0.051 | ⚠ within organs, on part of the lines; also absent: PLCB4, PAG1, RGS17 |
| [[MGST1]] | B | SLC39A8 activity raises MGST1's level | lines that do not express SLC39A8 (12) vs lines expressing it (38) | 2.28× lower at baseline in the lines without SLC39A8 | 0.052 | ⚠ within organs, on part of the lines; also absent: PLCB4, PAG1, RGS17 |
| [[SLC44A1]] | B | SLC39A8 activity raises SLC44A1's level | lines that do not express SLC39A8 (12) vs lines expressing it (38) | 1.84× lower at baseline in the lines without SLC39A8 | 0.073 | ⚠ within organs, on part of the lines; also absent: PLCB4, PAG1, RGS17 |

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.523). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.7, 19.0); signed map (25.9, 34.4). **Vector** length 108, 28.1% of its response variance represented; |z| ≥ 3 in 1,116 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.8 | +19.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +13.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.5 | +12.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.4 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.0 | +19.2 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +3.3 | +10.1 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +3.2 | +6.0 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +2.9 | +5.7 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +2.9 | +6.9 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.4 | -7.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -4.6 | -7.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.6 | -8.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.5 | -0.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.5 | +1.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.3 | -5.7 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.1 | -6.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.9 | -8.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 39 member 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q24 — chr4:102,251,080-102,431,258 (-) |
| Ensembl biotype | protein_coding |
| Also known as | BIGM103, ZIP8, ZIP-8 |
| Gene groups (HGNC) | Solute carrier family 39 |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 5 pathways, smallest: Zinc influx into cells by the SLC39 gene family; Zinc transporters; Metal ion SLC transporters |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9C0K1](https://www.uniprot.org/uniprotkb/Q9C0K1) (Metal cation symporter ZIP8):

> Electroneutral divalent metal cation:bicarbonate symporter of the plasma membrane mediating the cellular uptake of zinc and manganese, two divalent metal cations important for development, tissue homeostasis and immunity. Transports an electroneutral complex composed of a divalent metal cation and two bicarbonate anions or alternatively a bicarbonate and a selenite anion. Thereby, it also contributes to the cellular uptake of selenium, an essential trace metal and micronutrient. Also imports …

**Summary**, from NCBI Gene [64116](https://www.ncbi.nlm.nih.gov/gene/64116):

> This gene encodes a member of the SLC39 family of solute-carrier genes, which show structural characteristics of zinc transporters. The encoded protein is glycosylated and found in the plasma membrane and mitochondria, and functions in the cellular import of zinc at the onset of inflammation. It is also thought to be the primary transporter of the toxic cation cadmium, which is found in cigarette smoke. Multiple transcript variants encoding different isoforms have been found for this gene. …

**Accessions** — [HGNC:20862](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20862) · Entrez [64116](https://www.ncbi.nlm.nih.gov/gene/64116) · UniProt [Q9C0K1](https://www.uniprot.org/uniprotkb/Q9C0K1) · Ensembl [ENSG00000138821](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138821)

## Data

Gene col 6248: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6248); `tables/drug_effects.parquet` (82 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6248, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6248]; `tensor/DDL_lfc|DDL_z.npy` [6248]; `embed/gene_vectors.npy` [6248]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6248 or target_col == 6248). Every well: [[SLC39A8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC39A8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
