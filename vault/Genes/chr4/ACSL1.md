---
symbol: "ACSL1"
type: "gene"
col: 7559
ensembl_id: "ENSG00000151726"
name: "acyl-CoA synthetase long chain family member 1"
location: "4q35.1"
module: 106
arm: "+"
pooled_cpm: 36.58
n_lines_expressing: 48
n_dd_up: 49
n_dd_down: 2
n_dd_up_clean: 36
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/106"]
generated_by: "tahoemap"
---

# ACSL1

*acyl-CoA synthetase long chain family member 1* — 4q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 49 drug-doses (13 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 2.46× (z +15.1, q 0e+00, up in 41 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.05 µM: 0.756× (z -4.3, q 0.008, down in 21 of 44 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (HepG2/C3A 0.220×, SHP-77 0.246×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.0936×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (KATO III 0.264×; ⚠ position correction uncertain); [[Temsirolimus (drug)]] 0.5 µM in 1 line (HCT15 0.186×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TSC22D3]] (+0.75, fdr 7e-06), [[MAOA]] (+0.75, fdr 7e-06), [[FKBP5]] (+0.67, fdr 7e-06); moves opposite to [[PTHLH]] (-0.60, fdr 8e-06), [[VEGFC]] (-0.59, fdr 1e-05), [[MANCR]] (-0.58, fdr 1e-05).
> It is in [[Module 106]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TRBC2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 63 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 49 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7559.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **2.46×** | +15.1 | 0e+00 | 41/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.40×** | +14.7 | 0e+00 | 41/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ position correction uncertain | **1.82×** | +14.1 | 5e-43 | 33/46 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **2.21×** | +13.3 | 3e-38 | 39/46 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.60×** | +11.1 | 2e-26 | 39/46 (NCI-H2347, LS 180, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +10.5 | 8e-24 | 29/45 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Clobetasol propionate (drug)]] 5 µM | ⚠ position correction uncertain | **1.74×** | +9.3 | 2e-18 | 28/46 (HOP62, SNU-423, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.68×** | +8.7 | 2e-16 | 36/46 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.67×** | +8.6 | 7e-16 | 29/46 (A498, C32, …) | all doses, flat | position effect removed |
| [[Clobetasol propionate (drug)]] 0.5 µM | ⚠ position correction uncertain | **1.60×** | +7.9 | 1e-13 | 26/46 (HOP62, SNU-423, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.39×** | +7.8 | 3e-13 | 24/46 (SNU-423, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM | ⚠ position correction uncertain | **1.58×** | +7.7 | 7e-13 | 25/46 (NCI-H460, HOP62, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **1.51×** | +6.9 | 2e-10 | 24/46 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.51×** | +6.9 | 3e-10 | 32/46 (NCI-H2347, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Budesonide (drug)]] 5 µM |  | **1.50×** | +6.8 | 4e-10 | 25/46 (SNU-423, HOP62, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.48×** | +6.6 | 2e-09 | 22/46 (NCI-H460, SNU-423, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **1.52×** | +6.5 | 3e-09 | 23/44 (HOP62, NCI-H460, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.47×** | +6.4 | 4e-09 | 24/45 (NCI-H460, HOP62, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.47×** | +6.4 | 4e-09 | 23/46 (SNU-423, NCI-H460, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **1.48×** | +6.3 | 1e-08 | 25/46 (SNU-423, NCI-H460, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7559.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 9 here, 8 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 2 lines (HepG2/C3A 0.220×, SHP-77 0.246×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.0936×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (KATO III 0.264×; ⚠ position correction uncertain); [[Temsirolimus (drug)]] 0.5 µM in 1 line (HCT15 0.186×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.05 µM |  | **0.756×** | -4.3 | 0.008 | 21/44 (SW480, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **0.807×** | -3.6 | 0.067 | 13/46 (HepG2/C3A, HS-578T, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.941× | -3.6 | 0.067 | 0/47 | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.05 µM |  | 0.819× | -3.3 | 0.16 | 8/46 (SW 1271, C-33 A, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7559. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 21.8 | 24 (4 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 7.10× (z +15.8) ⚠ position correction uncertain · without an alert: [[Dexamethasone (drug)]] 0.5 µM 6.83× (z +15.5) | — |
| [[NCI-H1573 (line)]] | alt | 13.0 | 23 (3 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 12.6× (z +13.2) ⚠ position correction uncertain · without an alert: [[Citalopram (hydrobromide) (drug)]] 0.05 µM 9.45× (z +11.7) | — |
| [[A498 (line)]] | wt | 59.0 | 20 (3 ⚠) | 0 | [[Triamcinolone (drug)]] 5 µM 2.87× (z +14.3) | — |
| [[NCI-H2347 (line)]] | alt | 37.5 | 20 (4 ⚠) | 0 | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 4.84× (z +12.9) | — |
| [[SNU-423 (line)]] | alt | 56.6 | 19 (3 ⚠) | 0 | [[Triamcinolone (drug)]] 5 µM 4.51× (z +16.7) | — |
| [[HOP62 (line)]] | alt | 14.0 | 18 (4 ⚠) | 0 | [[Clobetasol propionate (drug)]] 5 µM 14.4× (z +16.1) ⚠ position correction uncertain · without an alert: [[Budesonide (drug)]] 5 µM 13.3× (z +15.6) | — |
| [[NCI-H1792 (line)]] | alt | 50.9 | 18 (4 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.5 µM 6.20× (z +12.4) ⚠ position correction uncertain · without an alert: [[Triamcinolone (drug)]] 5 µM 3.63× (z +12.4) | — |
| [[SW 900 (line)]] | alt | 101 | 17 (3 ⚠) | 1 (1 ⚠) | [[Triamcinolone (drug)]] 5 µM 3.21× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.224× (z -10.7) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 20.5 | 14 (4 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +11.8) ⚠ position correction uncertain · without an alert: [[Betamethasone dipropionate (drug)]] 0.5 µM 5.03× (z +10.4) | — |
| [[H4 (line)]] | wt | 22.3 | 13 (4 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 10.0× (z +10.4) ⚠ position correction uncertain · without an alert: [[Budesonide (drug)]] 0.5 µM 8.65× (z +9.7) | — |
| [[RPMI-7951 (line)]] | alt | 30.2 | 13 (3 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 9.26× (z +11.8) ⚠ position correction uncertain · without an alert: [[Dexamethasone (drug)]] 5 µM 8.64× (z +11.5) | — |
| [[hTERT-HPNE (line)]] | wt | 16.5 | 6 (3 ⚠) | 0 | [[Clobetasol propionate (drug)]] 5 µM 8.21× (z +9.1) ⚠ position correction uncertain · without an alert: [[Budesonide (drug)]] 5 µM 7.27× (z +8.6) | — |
| [[LoVo (line)]] | wt | 22.7 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.75× (z +12.3) | — |
| [[HEC-1-A (line)]] | alt | 22.7 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 3.62× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 20.3 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.05× (z +14.2) ⚠ position correction uncertain · without an alert: [[Panobinostat (drug)]] 5 µM 2.96× (z +9.8) | — |
| [[BT-474 (line)]] | alt | 122 | 3 | 0 | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 4.59× (z +9.8) | — |
| [[KATO III (line)]] | alt | 205 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.264× (z -13.0) ⚠ position correction uncertain |
| [[LS 180 (line)]] | wt | 41.2 | 3 | 0 | [[Berbamine (drug)]] 5 µM 2.89× (z +11.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 20.8 | 2 (2 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.48× (z +13.0) ⚠ position correction uncertain | [[Selinexor (drug)]] 5 µM 0.343× (z -9.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 29.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.61× (z +12.8) | — |
| [[COLO 205 (line)]] | alt | 51.2 | 2 | 0 | [[Berbamine (drug)]] 5 µM 3.04× (z +9.1) | — |
| [[HT-29 (line)]] | alt | 31.9 | 2 | 0 | [[Berbamine (drug)]] 5 µM 3.34× (z +11.8) | — |
| [[J82 (line)]] | alt | 26.5 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +14.1) ⚠ position correction uncertain | — |
| [[RKO (line)]] | wt | 51.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.44× (z +11.4) ⚠ position correction uncertain | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0936× (z -20.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 34.6 | 1 | 1 (1 ⚠) | [[Triamcinolone (drug)]] 0.5 µM 3.73× (z +8.5) | [[Dinaciclib (drug)]] 5 µM 0.246× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[C32 (line)]] | wt | 60.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +9.6) ⚠ position correction uncertain | — |
| [[CFPAC-1 (line)]] | alt | 44.9 | 1 (1 ⚠) | 0 | [[Clobetasol propionate (drug)]] 0.5 µM 3.62× (z +8.8) ⚠ position correction uncertain | — |
| [[HCT15 (line)]] | alt | 29.6 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.186× (z -9.5) |
| [[HepG2_C3A (line)]] | wt | 86.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~21% of this change |
| [[NCI-H23 (line)]] | alt | 13.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.136× (z -10.9) ⚠ toxic |
| [[A-172 (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 47.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.05 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.92 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 49.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7559), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TSC22D3]] | +0.75 | +0.74 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[MAOA]] | +0.75 | +0.72 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_FATTY_ACID_METABOLISM |
| [[FKBP5]] | +0.67 | +0.70 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[IRAK3]] | +0.67 | +0.62 / +0.63 | both halves | 7e-06 |  |
| [[KLF9]] | +0.66 | +0.75 / +0.57 | both halves | 1e-05 |  |
| [[PDLIM1]] | +0.66 | +0.56 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[CPD]] | +0.65 | +0.58 / +0.70 | both halves | 8e-06 |  |
| [[STOM]] | +0.65 | +0.65 / +0.65 | both halves | 7e-06 | **novel candidate** |
| [[SAA1]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[B4GALT1]] | +0.63 | +0.57 / +0.63 | both halves | 1e-05 | **novel candidate** |
| [[SAA2]] | +0.62 | +0.59 / +0.61 | both halves | 7e-06 |  |
| [[TMTC1]] | +0.62 | +0.57 / +0.65 | both halves | 9e-06 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTHLH]] | -0.60 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[VEGFC]] | -0.59 | -0.55 / -0.64 | both halves | 1e-05 |  |
| [[MANCR]] | -0.58 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[ANXA10]] | -0.56 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[FZD8]] | -0.56 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[SEMA3A]] | -0.54 | -0.59 / -0.51 | both halves | 1e-05 |  |
| [[TCP10L]] | -0.53 | -0.50 / -0.44 | both halves | 3e-05 |  |
| [[GJA1]] | -0.53 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[LINC00973]] | -0.52 | -0.40 / -0.54 | both halves | 5e-05 |  |
| [[SYNJ2]] | -0.52 | -0.53 / -0.55 | both halves | 1e-05 |  |
| [[PLAU]] | -0.51 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[FST]] | -0.50 | -0.38 / -0.60 | both halves | 6e-05 | pathway: HALLMARK_MYOGENESIS |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRBC2]] | B | TRBC2 activity raises ACSL1's level | lines that do not express TRBC2 (39) vs lines expressing it (11) | 1.38× lower at baseline in the lines without TRBC2 | 0.049 | ⚠ within organs, on part of the lines; also absent: PIGR, MUC6, PSG1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 106]]; 44 genes; every member is in the + arm (projection on the module's main direction 0.779). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.25; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (28.9, 16.0); signed map (17.2, 30.0). **Vector** length 120, 34.2% of its response variance represented; |z| ≥ 3 in 1,666 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Clobetasol propionate (drug)]] 0.05 µM | ⚠ position correction uncertain | +7.5 | +7.7 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +7.3 | +6.4 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM | ⚠ position correction uncertain | +7.2 | +7.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +7.1 | +6.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM | ⚠ position correction uncertain | +6.7 | +9.3 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -3.8 | -1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -0.8 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.4 | -2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.9 | -0.5 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.6 | -0.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.3 | -4.3 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA synthetase long chain family member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q35.1 — chr4:184,755,595-184,826,818 (-) |
| Ensembl biotype | protein_coding |
| Also known as | LACS2, LACS, ACS1, LACS1, FACL1; previously FACL2 |
| Gene groups (HGNC) | Acyl-CoA synthetase family |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME, FATTY_ACID_METABOLISM, MYOGENESIS |
| Reactome | 14 pathways, smallest: Linoleic acid (LA) metabolism; alpha-linolenic (omega3) and linoleic (omega6) acid metabolism; alpha-linolenic acid (ALA) metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P33121](https://www.uniprot.org/uniprotkb/P33121) (Long-chain-fatty-acid--CoA ligase 1):

> Catalyzes the conversion of long-chain fatty acids to their active form fatty acyl-CoAs. May drive cellular fatty acid uptake by metabolic trapping, and regulate the channeling of fatty acids towards specific metabolic pathways such as the generation of energy by beta-oxidation or the synthesis of membrane lipids (Probable). Main fatty acyl-CoA synthetase in the heart, where it provides the fatty acids used for cardiac oxidation (By similarity). Preferentially uses palmitoleate, oleate and …

**Summary**, from NCBI Gene [2180](https://www.ncbi.nlm.nih.gov/gene/2180):

> The protein encoded by this gene is an isozyme of the long-chain fatty-acid-coenzyme A ligase family. Although differing in substrate specificity, subcellular localization, and tissue distribution, all isozymes of this family convert free long-chain fatty acids into fatty acyl-CoA esters, and thereby play a key role in lipid biosynthesis and fatty acid degradation. Several transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Nov 2013]

**Accessions** — [HGNC:3569](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3569) · Entrez [2180](https://www.ncbi.nlm.nih.gov/gene/2180) · UniProt [P33121](https://www.uniprot.org/uniprotkb/P33121) · Ensembl [ENSG00000151726](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151726)

## Data

Gene col 7559: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7559); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7559, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7559]; `tensor/DDL_lfc|DDL_z.npy` [7559]; `embed/gene_vectors.npy` [7559]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7559 or target_col == 7559). Every well: [[ACSL1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACSL1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
