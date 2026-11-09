---
symbol: "NET1"
type: "gene"
col: 10433
ensembl_id: "ENSG00000173848"
name: "neuroepithelial cell transforming 1"
location: "10p15.1"
module: 31
arm: "+"
pooled_cpm: 112.48
n_lines_expressing: 46
n_dd_up: 20
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 6
direction_downstream: 2
tags: ["gene", "module/031"]
generated_by: "tahoemap"
---

# NET1

*neuroepithelial cell transforming 1* — 10p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.83× (z +14.5, q 1e-44, up in 32 of 44 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 4.37× (z +13.0, q 2e-36, up in 41 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.541× (z -14.7, q 0e+00, down in 34 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LASTR]] (+0.64, fdr 9e-06), [[RIPK4]] (+0.55, fdr 4e-05), [[IRF6]] (+0.54, fdr 3e-05); moves opposite to [[ARIH2]] (-0.56, fdr 1e-05), [[MROH1]] (-0.52, fdr 6e-05), [[TMEM11-DT]] (-0.50, fdr 3e-05).
> It is in [[Module 031]], a single-armed module (Formation of the cornified envelope).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[WNT7A]] → it (grade B ⚠); 2 go from it, the strongest it → [[PCDH1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 13 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10433.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.83×** | +14.5 | 1e-44 | 32/44 (HT-29, A498, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.37×** | +13.0 | 2e-36 | 41/45 (RKO, HEC-1-A, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~11% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.80×** | +9.6 | 2e-19 | 33/44 (NCI-H460, A498, …) | all doses, stronger at high dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.73×** | +9.3 | 3e-18 | 32/44 (NCI-H460, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **2.78×** | +9.0 | 2e-17 | 33/44 (HEC-1-A, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +7.9 | 2e-13 | 30/44 (HT-29, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.58×** | +7.7 | 1e-12 | 30/44 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.52×** | +7.1 | 9e-11 | 24/43 (NCI-H460, NCI-H1792, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.50×** | +6.5 | 4e-09 | 22/43 (NCI-H1792, LoVo, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.37×** | +5.2 | 9e-06 | 21/44 (NCI-H1792, HT-29, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.36×** | +5.2 | 9e-06 | 23/44 (NCI-H460, A-427, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +5.1 | 2e-05 | 21/44 (NCI-H23, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.29×** | +4.3 | 8e-04 | 19/44 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | **1.26×** | +3.9 | 0.004 | 17/44 (NCI-H460, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.8 | 0.005 | 20/43 (SNU-1, SW480, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.026 | 17/44 (SNU-1, SW480, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10433.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.541×** | -14.7 | 0e+00 | 34/45 (LS 180, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.504×** | -11.2 | 1e-26 | 32/37 (LS 180, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.694×** | -6.0 | 4e-07 | 28/43 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.716×** | -5.7 | 2e-06 | 26/43 (SNU-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Budesonide (drug)]] 0.5 µM |  | **0.790×** | -4.0 | 0.006 | 18/44 (Hs 766T, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.856× | -3.7 | 0.016 | 18/44 (SNU-1, SW1417, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.804×** | -3.7 | 0.016 | 19/44 (NCI-H2347, Panc 03.27, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.853× | -3.7 | 0.018 | 21/45 (SW480, HepG2/C3A, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.831×** | -3.2 | 0.099 | 15/43 (Hs 766T, NCI-H2347, …) | all doses, flat |  |
| [[ULK-101 (drug)]] 0.05 µM |  | 0.825× | -3.1 | 0.11 | 11/45 (Hs 766T, SNU-423, …) | inconsistent across doses |  |
| [[Hydroxyfasudil (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.835× | -3.1 | 0.11 | 9/44 (NCI-H1792, HEC-1-A, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10433. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-1 (line)]] | wt | 639 | 2 | 9 (7 ⚠) | [[Homoharringtonine (drug)]] 0.05 µM 2.49× (z +9.6) | [[Dinaciclib (drug)]] 5 µM 0.111× (z -22.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.257× (z -20.4) |
| [[NCI-H460 (line)]] | wt | 46.8 | 10 (8 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.62× (z +16.8) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.41× (z +9.6) | — |
| [[LS 180 (line)]] | wt | 250 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0662× (z -28.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -25.5) |
| [[NCI-H2347 (line)]] | alt | 325 | 0 | 8 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.216× (z -19.4) |
| [[SW1417 (line)]] | alt | 372 | 2 (1 ⚠) | 5 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.15× (z +11.3) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 5.41× (z +9.3) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -21.2) |
| [[SW480 (line)]] | alt | 181 | 1 | 6 (4 ⚠) | [[TAK-901 (drug)]] 5 µM 4.37× (z +10.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.309× (z -21.9) |
| [[CFPAC-1 (line)]] | alt | 488 | 0 | 6 (4 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.146× (z -25.0) |
| [[Hs 766T (line)]] | wt | 164 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -18.2) |
| [[A498 (line)]] | wt | 45.2 | 4 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +14.5) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 3.42× (z +10.2) | — |
| [[AsPC-1 (line)]] | alt | 138 | 2 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +13.1) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.91× (z +9.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.363× (z -13.0) |
| [[HEC-1-A (line)]] | alt | 97.1 | 2 | 2 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 6.68× (z +10.4) | [[Dinaciclib (drug)]] 5 µM 0.245× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.475× (z -10.9) |
| [[HT-29 (line)]] | alt | 88.7 | 3 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +15.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 2.43× (z +10.4) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.560× (z -9.6) |
| [[KATO III (line)]] | alt | 133 | 2 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.35× (z +9.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.28× (z +9.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -17.7) |
| [[NCI-H1792 (line)]] | alt | 78.6 | 4 (4 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.39× (z +10.3) ⚠ cell-cycle shift, explains ~39% of this change | — |
| [[Panc 03.27 (line)]] | alt | 179 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -23.6) |
| [[RKO (line)]] | wt | 62.0 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +13.7) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 18.4× (z +10.6) | — |
| [[A-427 (line)]] | wt | 35.9 | 2 (1 ⚠) | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.5× (z +9.9) | [[Selinexor (drug)]] 5 µM 0.410× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 98.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.18× (z +10.0) ⚠ cell-cycle shift, explains ~42% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.380× (z -12.6) |
| [[MIA PaCa-2 (line)]] | alt | 93.8 | 2 (2 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 3.25× (z +10.8) ⚠ cell-cycle shift, explains ~38% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.321× (z -15.4) |
| [[A-172 (line)]] | wt | 40.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.95× (z +8.7) ⚠ cell-cycle shift, explains ~42% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.182× (z -14.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 185 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.343× (z -14.8) |
| [[J82 (line)]] | alt | 74.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +10.8) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[LoVo (line)]] | wt | 97.9 | 1 (1 ⚠) | 1 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +10.5) ⚠ cell-cycle shift, explains ~39% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.253× (z -20.8) |
| [[NCI-H23 (line)]] | alt | 40.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.53× (z +9.7) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 8.95× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 113 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -12.9) |
| [[AN3 CA (line)]] | alt | 107 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.194× (z -9.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 56.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.301× (z -8.5) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 155 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.183× (z -18.9) |
| [[HOP62 (line)]] | alt | 56.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -11.4) |
| [[LOX-IMVI (line)]] | wt | 48.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +12.9) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[NCI-H2030 (line)]] | alt | 72.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.21× (z +9.5) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[SNU-423 (line)]] | alt | 65.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -9.3) |
| [[SW 900 (line)]] | alt | 54.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.238× (z -10.2) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 51.6 | 1 | 0 | [[TAK-901 (drug)]] 0.05 µM 5.06× (z +9.9) | — |
| [[BT-474 (line)]] | alt | 77.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 67.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.2 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.2 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 26.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 113 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 94.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 54.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 27.2 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 60.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 36.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10433), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LASTR]] | +0.64 | +0.61 / +0.57 | both halves | 9e-06 |  |
| [[RIPK4]] | +0.55 | +0.41 / +0.57 | both halves | 4e-05 |  |
| [[IRF6]] | +0.54 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[RHPN2]] | +0.54 | +0.38 / +0.45 | both halves | 6e-05 | pathway: RHOA GTPase cycle |
| [[CYP2S1]] | +0.53 | +0.46 / +0.55 | both halves | 3e-05 |  |
| [[ATP8B1]] | +0.53 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[PLS1]] | +0.53 | +0.46 / +0.47 | both halves | 3e-05 |  |
| [[DLG3]] | +0.53 | +0.50 / +0.50 | both halves | 1e-05 |  |
| [[GCOM1]] | +0.53 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[KRT19]] | +0.53 | +0.53 / +0.36 | both halves | 9e-05 |  |
| [[PCDH1]] | +0.52 | +0.47 / +0.46 | both halves | 3e-05 |  |
| [[HS3ST1]] | +0.52 | +0.47 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARIH2]] | -0.56 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[MROH1]] | -0.52 | -0.38 / -0.56 | both halves | 6e-05 |  |
| [[TMEM11-DT]] | -0.50 | -0.43 / -0.43 | both halves | 3e-05 |  |
| [[LINC00862]] | -0.50 | -0.47 / -0.38 | both halves | 7e-05 |  |
| [[GLYR1]] | -0.49 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[NR2C2]] | -0.49 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[RUFY3]] | -0.49 | -0.39 / -0.46 | both halves | 5e-05 |  |
| [[POU6F1]] | -0.48 | -0.41 / -0.32 | both halves | 2e-04 |  |
| [[TRNT1]] | -0.48 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[PRDM10]] | -0.48 | -0.31 / -0.36 | both halves | 2e-04 |  |
| [[GARS1-DT]] | -0.48 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[ZBTB8OS]] | -0.47 | -0.42 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNT7A]] | B | WNT7A activity raises NET1's level | lines that do not express WNT7A (39) vs lines expressing it (11) | 2.54× lower at baseline in the lines without WNT7A | 0.008 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6 |
| [[LASTR]] | B | LASTR activity raises NET1's level | lines that do not express LASTR (22) vs lines expressing it (28) | 2.49× lower at baseline in the lines without LASTR | 0.026 | ⚠ within organs, on part of the lines; also absent: TINAGL1, PCSK9, ANXA3; maybe low, not absent |
| [[INAVA]] | B | INAVA activity raises NET1's level | lines that do not express INAVA (29) vs lines expressing it (21) | 2.26× lower at baseline in the lines without INAVA | 0.037 | ⚠ within organs, on part of the lines; co-absent genes; also absent: CDH1, MAL2, B3GNT3 |
| [[ELF3]] | B | ELF3 activity raises NET1's level | lines that do not express ELF3 (23) vs lines expressing it (27) | 2.16× lower at baseline in the lines without ELF3 | 0.055 | ⚠ within organs, on part of the lines; also absent: RASSF6, GOLT1A, LAMA3 |
| [[IRF6]] | B | IRF6 activity raises NET1's level | lines that do not express IRF6 (31) vs lines expressing it (19) | 2.32× lower at baseline in the lines without IRF6 | 0.065 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[WNT7A]] | B | WNT7A activity weakens NET1's drug response | lines that do not express WNT7A (35) vs lines expressing it (10) | the lines without WNT7A respond 1.38× as strongly (z diff -1.27); strongest at Digitoxin 5 µM: 1.52x vs 0.89x (z diff -4.6) | 0.099 | ⚠ within organs, on part of the lines; also absent: KRT5, GSDMC, CST6; target measured in part of the lines; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PCDH1]] | C | NET1 activity raises PCDH1's level | lines that do not express NET1 (4) vs lines expressing it (46) | 3.49× lower at baseline in the lines without NET1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: NPEPPSP1; maybe low, not absent; its own permutation p |
| [[PRDM10]] | C | NET1 activity lowers PRDM10's level | lines that do not express NET1 (4) vs lines expressing it (46) | 1.48× higher at baseline in the lines without NET1 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: NPEPPSP1; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 031]] — Formation of the cornified envelope; 141 genes; every member is in the + arm (projection on the module's main direction 0.454). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.22; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (15.6, 61.6); signed map (53.8, 9.1). **Vector** length 111, 31.2% of its response variance represented; |z| ≥ 3 in 1,151 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +4.3 | +5.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | +4.2 | +3.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.0 | +7.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.9 | +3.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | +2.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +3.4 | +3.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.6 | +1.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | -0.5 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.5 | -14.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~63% of this change | -5.2 | +3.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | -4.9 | +9.3 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -6.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~59% of this change | -4.3 | +4.3 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -3.1 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.0 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -3.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -2.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -2.3 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | neuroepithelial cell transforming 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10p15.1 — chr10:5,412,557-5,459,056 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ARHGEF8, NET1A |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 12 pathways, smallest: NRAGE signals death through JNK; G alpha (12/13) signalling events; RHOB GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q7Z628](https://www.uniprot.org/uniprotkb/Q7Z628) (Neuroepithelial cell-transforming gene 1 protein):

> Acts as a guanine nucleotide exchange factor (GEF) for RhoA GTPase. May be involved in activation of the SAPK/JNK pathway Stimulates genotoxic stress-induced RHOB activity in breast cancer cells leading to their cell death.

**Summary**, from NCBI Gene [10276](https://www.ncbi.nlm.nih.gov/gene/10276):

> This gene is part of the family of Rho guanine nucleotide exchange factors. Members of this family activate Rho proteins by catalyzing the exchange of GDP for GTP. The protein encoded by this gene interacts with RhoA within the cell nucleus and may play a role in repairing DNA damage after ionizing radiation. Pseudogenes of this gene are located on the long arms of chromosomes 1, 7 and 18. Alternative splicing results in multiple transcript variants that encode different protein isoforms. …

**Accessions** — [HGNC:14592](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14592) · Entrez [10276](https://www.ncbi.nlm.nih.gov/gene/10276) · UniProt [Q7Z628](https://www.uniprot.org/uniprotkb/Q7Z628) · Ensembl [ENSG00000173848](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173848)

## Data

Gene col 10433: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10433); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10433, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10433]; `tensor/DDL_lfc|DDL_z.npy` [10433]; `embed/gene_vectors.npy` [10433]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10433 or target_col == 10433). Every well: [[NET1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NET1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
