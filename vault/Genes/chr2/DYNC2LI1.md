---
symbol: "DYNC2LI1"
type: "gene"
col: 6113
ensembl_id: "ENSG00000138036"
name: "dynein cytoplasmic 2 light intermediate chain 1"
location: "2p21"
module: 17
arm: "+"
pooled_cpm: 24.69
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 28
n_dd_up_clean: 6
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/017"]
generated_by: "tahoemap"
---

# DYNC2LI1

*dynein cytoplasmic 2 light intermediate chain 1* — 2p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.48× (z +10.1, q 5e-21, up in 40 of 48 measured lines) ⚠ cell-cycle shift, explains ~56% of this change. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.41× (z +6.2, q 2e-07, up in 28 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (10 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.323× (z -20.2, q 0e+00, down in 40 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.326× (z -20.0, q 0e+00, down in 47 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFCAB7]] (+0.76, fdr 7e-06), [[TRAPPC11]] (+0.73, fdr 7e-06), [[FPGT]] (+0.69, fdr 7e-06); moves opposite to [[CFL1]] (-0.63, fdr 1e-05), [[SCHIP1]] (-0.62, fdr 1e-05), [[MAMLD1]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 017]] (Intraflagellar transport).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF594-DT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6113.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.48×** | +10.1 | 5e-21 | 40/48 (RKO, A-172, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ponatinib (drug)]] 5 µM |  | **1.41×** | +6.2 | 2e-07 | 28/48 (LS 180, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **1.36×** | +5.6 | 5e-06 | 20/48 (RKO, KATO III, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.30×** | +4.7 | 4e-04 | 20/48 (KATO III, HOP62, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.30×** | +4.5 | 8e-04 | 20/47 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.25×** | +4.0 | 0.006 | 11/48 (SW 1088, LS 180, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.24×** | +3.9 | 0.007 | 17/47 (HEC-1-A, MIA PaCa-2, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | 1.17× | +3.9 | 0.007 | 16/48 (SW480, HEC-1-A, …) | all doses, flat |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **1.23×** | +3.6 | 0.018 | 11/44 (NCI-H2030, SW1417, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.23×** | +3.5 | 0.024 | 16/48 (MIA PaCa-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.44×** | +3.5 | 0.029 | 10/46 (RKO, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.20×** | +3.3 | 0.040 | 5/48 (NCI-H1573, KATO III, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.13× | +3.3 | 0.048 | 3/48 (A498, CFPAC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~84% of this change | 1.19× | +3.2 | 0.056 | 5/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.13× | +3.1 | 0.063 | 8/48 (LS 180, hTERT-HPNE, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.090 | 5/48 (HEC-1-A, Hs 766T, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6113.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.323×** | -20.2 | 0e+00 | 40/46 (RPMI-7951, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.326×** | -20.0 | 0e+00 | 47/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.417×** | -15.3 | 0e+00 | 39/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.484×** | -12.7 | 1e-34 | 38/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.484×** | -12.4 | 2e-33 | 40/47 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.611×** | -12.4 | 2e-33 | 37/48 (H4, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~81% of this change | **0.657×** | -10.6 | 3e-24 | 30/47 (NCI-H1792, A549, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.344×** | -10.0 | 2e-21 | 40/48 (MIA PaCa-2, SW 900, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.356×** | -9.6 | 3e-20 | 38/47 (SW480, NCI-H1573, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.587×** | -9.5 | 1e-19 | 27/47 (NCI-H460, A549, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.603×** | -9.0 | 1e-17 | 30/48 (NCI-H460, A549, …) | two highest doses | cell-cycle shift (explains ~21% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.614×** | -8.7 | 2e-16 | 35/48 (SW480, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~66% of this change | **0.653×** | -7.3 | 1e-11 | 27/47 (NCI-H1792, NCI-H460, …) | two highest doses | composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **0.682×** | -6.5 | 2e-09 | 30/47 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.686×** | -6.4 | 4e-09 | 24/47 (H4, HS-578T, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.715×** | -6.0 | 8e-08 | 25/48 (HT-29, LoVo, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.789×** | -5.9 | 1e-07 | 23/48 (SNU-423, A-172, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.811×** | -5.3 | 4e-06 | 22/48 (NCI-H23, LOX-IMVI, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.737×** | -5.2 | 5e-06 | 25/48 (A-427, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.764×** | -4.8 | 4e-05 | 21/47 (MIA PaCa-2, H4, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6113. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 31.9 | 0 | 13 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.128× (z -20.6) |
| [[SW480 (line)]] | alt | 31.4 | 0 | 10 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.104× (z -22.0) |
| [[PANC-1 (line)]] | alt | 26.0 | 0 | 6 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.182× (z -17.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.183× (z -17.2) |
| [[A549 (line)]] | wt | 29.9 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -18.9) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.287× (z -10.2) |
| [[HT-29 (line)]] | alt | 24.1 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.183× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.227× (z -11.6) |
| [[SNU-423 (line)]] | alt | 17.5 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -12.8) |
| [[A498 (line)]] | wt | 32.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -12.5) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.432× (z -11.6) |
| [[H4 (line)]] | wt | 30.4 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.108× (z -16.2) |
| [[HCT15 (line)]] | alt | 34.2 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -12.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.134× (z -11.5) |
| [[KATO III (line)]] | alt | 27.4 | 0 | 4 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.181× (z -12.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.223× (z -11.2) |
| [[NCI-H23 (line)]] | alt | 63.5 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.116× (z -21.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 18.5 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0942× (z -17.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.436× (z -8.6) |
| [[A-427 (line)]] | wt | 35.1 | 0 | 3 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.239× (z -11.3) |
| [[HS-578T (line)]] | alt | 23.1 | 0 | 3 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -9.7) |
| [[LoVo (line)]] | wt | 20.1 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.156× (z -14.4) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.341× (z -8.7) |
| [[LS 180 (line)]] | wt | 23.3 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.163× (z -12.7) |
| [[MIA PaCa-2 (line)]] | alt | 31.6 | 0 | 3 (1 ⚠) | — | [[TAK-901 (drug)]] 5 µM 0.0579× (z -10.8) |
| [[NCI-H1792 (line)]] | alt | 35.9 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -19.9) ⚠ cell-cycle shift, explains ~81% of this change |
| [[NCI-H2347 (line)]] | alt | 7.97 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -9.1) ⚠ cell-cycle shift, explains ~81% of this change |
| [[A-172 (line)]] | wt | 26.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.397× (z -10.5) |
| [[LOX-IMVI (line)]] | wt | 21.8 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.117× (z -15.3) |
| [[NCI-H1573 (line)]] | alt | 32.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.245× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.139× (z -8.5) |
| [[SW 900 (line)]] | alt | 19.8 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.125× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.0366× (z -10.1) |
| [[SW48 (line)]] | wt | 20.2 | 0 | 2 (1 ⚠) | — | [[Orlistat (drug)]] 0.05 µM 0.0749× (z -10.4) |
| [[BT-474 (line)]] | alt | 11.9 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.111× (z -9.5) |
| [[C-33 A (line)]] | alt | 26.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.186× (z -8.9) ⚠ toxic |
| [[CFPAC-1 (line)]] | alt | 19.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.234× (z -10.7) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 28.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.216× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 28.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.478× (z -9.6) |
| [[HOP62 (line)]] | alt | 16.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -8.9) |
| [[Hs 766T (line)]] | wt | 13.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.315× (z -8.6) |
| [[hTERT-HPNE (line)]] | wt | 16.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.165× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 19.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.281× (z -8.5) |
| [[RPMI-7951 (line)]] | alt | 26.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0349× (z -20.5) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 23.4 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.262× (z -8.7) |
| [[SNU-1 (line)]] | wt | 20.8 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.129× (z -8.5) |
| [[AN3 CA (line)]] | alt | 22.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.46 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 25.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6113), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB7]] | +0.76 | +0.71 / +0.80 | both halves | 7e-06 |  |
| [[TRAPPC11]] | +0.73 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[FPGT]] | +0.69 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[INTU]] | +0.69 | +0.65 / +0.70 | both halves | 7e-06 | STRING 534 |
| [[USP30]] | +0.69 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[PIGB]] | +0.68 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[WDR11]] | +0.66 | +0.53 / +0.66 | both halves | 1e-05 |  |
| [[ABITRAM]] | +0.65 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[TMEM254]] | +0.65 | +0.48 / +0.73 | both halves | 2e-05 |  |
| [[ZNF594-DT]] | +0.64 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[BBS5]] | +0.64 | +0.53 / +0.66 | both halves | 1e-05 | pathway: Assembly of the 9+0 primary cilium; STRING 586 |
| [[TMLHE]] | +0.64 | +0.56 / +0.67 | both halves | 1e-05 |  |

## Genes that move opposite

*18 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFL1]] | -0.63 | -0.57 / -0.66 | both halves | 1e-05 |  |
| [[SCHIP1]] | -0.62 | -0.53 / -0.66 | both halves | 1e-05 |  |
| [[MAMLD1]] | -0.61 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[TLNRD1]] | -0.61 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[SAXO1]] | -0.60 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[ZDHHC14]] | -0.58 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[GATAD2A]] | -0.58 | -0.63 / -0.57 | both halves | 8e-06 |  |
| [[SNTB2]] | -0.56 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[SNRPB]] | -0.56 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[CCDC71L]] | -0.55 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[TLL2]] | -0.55 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[SPON1-AS1]] | -0.55 | -0.41 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF594-DT]] | B | ZNF594-DT activity raises DYNC2LI1's level | lines that do not express ZNF594-DT (7) vs lines expressing it (43) | 1.49× lower at baseline in the lines without ZNF594-DT | 0.032 | ⚠ within organs, on part of the lines; also absent: ZNF594, SIPA1L2, KCNK15-AS1 |
| [[TOP2A]] | B | TOP2A activity raises DYNC2LI1's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NEK10]] | B | NEK10 activity raises DYNC2LI1's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 1.61× lower at baseline in the lines without NEK10 | 0.062 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 017]] — Intraflagellar transport; 202 genes; this gene is in the **+** arm (projection on the module's main direction 0.712). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-24.2, 0.0); signed map (-20.8, -17.6). **Vector** length 82.0, 19.1% of its response variance represented; |z| ≥ 3 in 1,255 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | +5.7 | +10.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~86% of this change | +4.2 | +5.6 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.7 | +2.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.3 | -2.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +6.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.4 | +2.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.1 | +3.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.8 | +2.4 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.4 | -12.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -6.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.1 | -5.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.0 | -4.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.4 | -5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -8.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.2 | -3.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | -3.1 | -6.5 |

## What is on record

|  |  |
|---|---|
| Name | dynein cytoplasmic 2 light intermediate chain 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p21 — chr2:43,774,039-43,810,010 (+) |
| Ensembl biotype | protein_coding |
| Also known as | D2LIC, LIC3, CGI-60, DKFZP564A033 |
| Gene groups (HGNC) | Dynein 2 complex subunits; Dynein light intermediate chains |
| Reactome | 4 pathways, smallest: Intraflagellar transport; Assembly of the 9+0 primary cilium; Cilium Assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TCX1](https://www.uniprot.org/uniprotkb/Q8TCX1) (Cytoplasmic dynein 2 light intermediate chain 1):

> Acts as one of several non-catalytic accessory components of the cytoplasmic dynein 2 complex (dynein-2 complex), a motor protein complex that drives the movement of cargos along microtubules within cilia and flagella in concert with the intraflagellar transport (IFT) system, facilitating the assembly of these organelles. Involved in the regulation of ciliary length.

**Summary**, from NCBI Gene [51626](https://www.ncbi.nlm.nih.gov/gene/51626):

> This gene encodes a protein that is a component of the dynein-2 microtubule motor protein complex that plays a role in the retrograde transport of cargo in primary cilia via the intraflagellar transport system. This gene is ubiquitously expressed and its protein, which localizes to the axoneme and Golgi apparatus, interacts directly with the cytoplasmic dynein 2 heavy chain 1 protein to form part of the multi-protein dynein-2 complex. Mutations in this gene produce defects in the dynein-2 …

**Accessions** — [HGNC:24595](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24595) · Entrez [51626](https://www.ncbi.nlm.nih.gov/gene/51626) · UniProt [Q8TCX1](https://www.uniprot.org/uniprotkb/Q8TCX1) · Ensembl [ENSG00000138036](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138036)

## Data

Gene col 6113: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6113); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6113, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6113]; `tensor/DDL_lfc|DDL_z.npy` [6113]; `embed/gene_vectors.npy` [6113]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6113 or target_col == 6113). Every well: [[DYNC2LI1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DYNC2LI1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
