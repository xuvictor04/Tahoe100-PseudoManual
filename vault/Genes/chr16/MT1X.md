---
symbol: "MT1X"
type: "gene"
col: 11900
ensembl_id: "ENSG00000187193"
name: "metallothionein 1X"
location: "16q13"
module: 113
arm: "+"
pooled_cpm: 132.29
n_lines_expressing: 45
n_dd_up: 23
n_dd_down: 21
n_dd_up_clean: 22
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# MT1X

*metallothionein 1X* — 16q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (1 with an alert ⚠); the strongest is [[Betamethasone dipropionate (drug)]] 5 µM: 4.09× (z +7.5, q 3e-11, up in 41 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.289× (z -9.9, q 3e-20, down in 42 of 44 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MT2A]] (+0.91, fdr 7e-06), [[ANGPTL4]] (+0.80, fdr 7e-06), [[MT1E]] (+0.78, fdr 7e-06); moves opposite to [[GALNT7]] (-0.60, fdr 3e-05), [[BBOX1-AS1]] (-0.59, fdr 1e-05), [[CRPPA]] (-0.59, fdr 4e-05).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[NR3C1]] → it (grade B ⚠); 3 go from it, the strongest it → [[SEC14L2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 1 with an alert ⚠; shown: the 15 strongest. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11900.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **4.09×** | +7.5 | 3e-11 | 41/44 (A498, NCI-H1792, …) | all doses, stronger at high dose | position effect removed |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **3.77×** | +7.4 | 4e-11 | 31/43 (A498, NCI-H1792, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **3.71×** | +7.3 | 6e-11 | 31/43 (A498, NCI-H1792, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **3.38×** | +6.8 | 2e-09 | 29/43 (A498, SNU-423, …) | all doses, flat | position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **3.19×** | +6.4 | 1e-08 | 31/43 (A498, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **3.83×** | +6.2 | 6e-08 | 30/43 (A498, NCI-H1792, …) | all doses, stronger at high dose | noisy plate (z scaled); position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | **3.03×** | +6.2 | 6e-08 | 28/43 (A498, NCI-H1792, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 5 µM |  | **3.01×** | +6.1 | 7e-08 | 28/43 (A498, SW 900, …) | all doses, flat |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.80×** | +5.7 | 6e-07 | 36/43 (hTERT-HPNE, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~13% here); position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **2.77×** | +5.7 | 9e-07 | 28/43 (A498, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **2.60×** | +5.3 | 6e-06 | 28/43 (A498, NCI-H1792, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **2.58×** | +5.3 | 7e-06 | 29/43 (A498, SW 900, …) | top dose only | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **1.94×** | +5.2 | 9e-06 | 28/43 (A498, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Econazole (drug)]] 5 µM |  | **2.52×** | +5.1 | 1e-05 | 29/43 (A498, SW 900, …) | top dose only | position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **2.45×** | +5.0 | 3e-05 | 27/43 (A498, SNU-423, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11900.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.289×** | -9.9 | 3e-20 | 42/44 (A549, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.327×** | -6.0 | 4e-07 | 38/43 (C32, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.528×** | -5.1 | 7e-05 | 35/43 (C32, SK-MEL-2, …) | top dose only | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.569×** | -4.5 | 9e-04 | 32/43 (A549, J82, …) | rises with dose | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.443×** | -4.4 | 0.001 | 33/45 (SK-MEL-2, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.232×** | -4.3 | 0.002 | 36/43 (A-172, SK-MEL-2, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.480×** | -4.1 | 0.003 | 28/43 (H4, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.474×** | -4.0 | 0.004 | 33/42 (SK-MEL-2, A-172, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.494×** | -3.8 | 0.008 | 27/42 (H4, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.487×** | -3.8 | 0.010 | 33/43 (SK-MEL-2, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.529×** | -3.6 | 0.016 | 26/43 (H4, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.530×** | -3.6 | 0.016 | 29/43 (A549, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.532×** | -3.6 | 0.016 | 34/43 (KATO III, RKO, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.522×** | -3.5 | 0.017 | 22/38 (CFPAC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.546×** | -3.4 | 0.024 | 24/43 (Panc 03.27, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 5 µM |  | **0.358×** | -3.0 | 0.084 | 28/44 (SK-MEL-2, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.568×** | -3.0 | 0.091 | 34/43 (LoVo, LS 180, …) | inconsistent across doses | position effect removed |
| [[RMC-6236 (drug)]] 5 µM |  | **0.367×** | -2.9 | 0.091 | 24/43 (A-172, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[crizotinib (drug)]] 5 µM |  | **0.586×** | -2.9 | 0.100 | 24/43 (HepG2/C3A, HOP62, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.60 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11900. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 59.1 | 19 | 1 (1 ⚠) | [[Clobetasol propionate (drug)]] 0.05 µM 20.1× (z +13.4) | [[Selinexor (drug)]] 5 µM 0.240× (z -9.0) ⚠ cell-cycle shift, explains ~47% of this change |
| [[SW 900 (line)]] | alt | 118 | 11 | 1 | [[Clobetasol propionate (drug)]] 0.05 µM 8.92× (z +11.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.187× (z -12.0) |
| [[NCI-H1792 (line)]] | alt | 64.8 | 11 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 14.7× (z +11.5) | — |
| [[SNU-423 (line)]] | alt | 129 | 11 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.65× (z +11.2) | — |
| [[AsPC-1 (line)]] | alt | 41.1 | 8 | 0 | [[Clobetasol propionate (drug)]] 0.5 µM 10.6× (z +9.5) | — |
| [[H4 (line)]] | wt | 288 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0527× (z -13.5) |
| [[hTERT-HPNE (line)]] | wt | 46.5 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.64× (z +13.3) | — |
| [[PANC-1 (line)]] | alt | 35.6 | 7 | 0 | [[Clobetasol propionate (drug)]] 0.05 µM 8.05× (z +10.5) | — |
| [[SK-MEL-2 (line)]] | alt | 170 | 0 | 7 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0859× (z -14.8) |
| [[HS-578T (line)]] | alt | 263 | 3 | 3 | [[Betamethasone dipropionate (drug)]] 5 µM 8.24× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.137× (z -13.5) |
| [[A549 (line)]] | wt | 388 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0613× (z -19.2) |
| [[Hs 766T (line)]] | wt | 188 | 5 | 0 | [[Betamethasone dipropionate (drug)]] 5 µM 9.37× (z +9.5) | — |
| [[CFPAC-1 (line)]] | alt | 533 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0903× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -10.5) |
| [[NCI-H1573 (line)]] | alt | 175 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -13.2) |
| [[A-172 (line)]] | wt | 211 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -13.7) |
| [[C32 (line)]] | wt | 169 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.125× (z -13.0) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.130× (z -12.7) |
| [[J82 (line)]] | alt | 490 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 83.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.65× (z +9.4) | — |
| [[NCI-H2030 (line)]] | alt | 161 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 23.8× (z +21.2) | — |
| [[Panc 03.27 (line)]] | alt | 102 | 2 | 1 | [[Phenylephrine (hydrochloride) (drug)]] 5 µM 7.01× (z +8.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.147× (z -12.0) |
| [[SHP-77 (line)]] | alt | 74.0 | 3 | 0 | [[Betamethasone dipropionate (drug)]] 5 µM 11.8× (z +9.1) | — |
| [[HOP62 (line)]] | alt | 182 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 11.0× (z +14.9) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -9.4) |
| [[SW 1088 (line)]] | alt | 447 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0311× (z -10.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -10.4) |
| [[BT-474 (line)]] | alt | 44.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0677× (z -9.2) ⚠ toxic |
| [[COLO 205 (line)]] | alt | 82.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0997× (z -8.7) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 130 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -11.1) |
| [[HepG2_C3A (line)]] | wt | 96.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -9.5) |
| [[MIA PaCa-2 (line)]] | alt | 331 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -9.0) |
| [[RPMI-7951 (line)]] | alt | 78.0 | 1 | 0 | [[Clobetasol propionate (drug)]] 0.5 µM 7.09× (z +8.5) | — |
| [[SW48 (line)]] | wt | 154 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.185× (z -9.7) |
| [[SW480 (line)]] | alt | 87.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +10.3) | — |
| [[A-427 (line)]] | wt | 11.6 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.6 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 16.3 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 18.4 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 46.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 60.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 125 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 110 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 95.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 48.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 72.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.0 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 143 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 39.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 88.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 47.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11900), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 5 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MT2A]] | +0.91 | +0.87 / +0.88 | both halves | 7e-06 | same gene group; pathway: Metallothioneins bind metals; STRING 866 |
| [[ANGPTL4]] | +0.80 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[MT1E]] | +0.78 | +0.71 / +0.83 | both halves | 7e-06 | same gene group; pathway: Metallothioneins bind metals; STRING 798 |
| [[MT1F]] | +0.77 | +0.69 / +0.78 | both halves | 7e-06 | same gene group; pathway: Metallothioneins bind metals; STRING 995; ⚠ same locus (21.8 kb, same strand: neighbours can correlate without regulation) |
| [[MT1A]] | +0.76 | +0.63 / +0.77 | both halves | 7e-06 | same gene group; pathway: Metallothioneins bind metals; STRING 677; ⚠ same locus (42.4 kb, same strand: neighbours can correlate without regulation) |
| [[ID1]] | +0.76 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[TANC2]] | +0.75 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[ZMYND8]] | +0.72 | +0.75 / +0.68 | both halves | 7e-06 |  |
| [[SAA1]] | +0.70 | +0.57 / +0.79 | both halves | 9e-06 |  |
| [[GLRX]] | +0.68 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[TLR2]] | +0.66 | +0.70 / +0.69 | both halves | 7e-06 |  |
| [[HS3ST3B1]] | +0.65 | +0.63 / +0.73 | both halves | 7e-06 |  |
| [[ERGIC1]] | +0.64 | +0.60 / +0.50 | both halves | 1e-05 |  |
| [[CEBPB]] | +0.63 | +0.54 / +0.76 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNT7]] | -0.60 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[BBOX1-AS1]] | -0.59 | -0.50 / -0.57 | both halves | 1e-05 |  |
| [[CRPPA]] | -0.59 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[C5orf15]] | -0.57 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[EIF4G2]] | -0.56 | -0.34 / -0.46 | both halves | 1e-04 |  |
| [[EDIL3-DT]] | -0.56 | -0.53 / -0.37 | both halves | 8e-05 |  |
| [[MATN2]] | -0.55 | -0.44 / -0.41 | both halves | 4e-05 |  |
| [[ERAP1]] | -0.55 | -0.36 / -0.46 | both halves | 1e-04 |  |
| [[MOB1A]] | -0.54 | -0.42 / -0.48 | both halves | 4e-05 |  |
| [[RCN1]] | -0.54 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[PRTFDC1]] | -0.54 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[HDAC2-AS2]] | -0.53 | -0.42 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR3C1]] | B | NR3C1 activity raises MT1X's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 3.1% of all compounds | 0.032 | ⚠ off-target possible; 3 compounds |
| [[TOP2A]] | B | TOP2A activity raises MT1X's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.3% of all compounds | 0.036 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NIBAN2]] | B | NIBAN2 activity raises MT1X's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 3.60× lower at baseline in the lines without NIBAN2 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[SH3TC1]] | B | SH3TC1 activity raises MT1X's level | lines that do not express SH3TC1 (10) vs lines expressing it (40) | 2.33× lower at baseline in the lines without SH3TC1 | 0.088 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[MT2A]] | C | MT2A activity raises MT1X's level | lines that do not express MT2A (9) vs lines expressing it (41) | 4.14× lower at baseline in the lines without MT2A | 0.009 | ⚠ within organs, on part of the lines; also absent: ENSG00000289942, TRAF1, MT1X; co-absent with the target |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SEC14L2]] | B | MT1X activity raises SEC14L2's level | lines that do not express MT1X (5) vs lines expressing it (45) | 2.32× lower at baseline in the lines without MT1X | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: RABGEF1P3, KIFC3, ENSG00000255031; its own permutation p |
| [[ARL4A]] | B | MT1X activity lowers ARL4A's level | lines that do not express MT1X (5) vs lines expressing it (45) | 2.34× higher at baseline in the lines without MT1X | 0.089 | ⚠ within organs, on part of the lines; co-absent genes; also absent: RABGEF1P3, KIFC3, ENSG00000255031; its own permutation p |
| [[MT2A]] | C | MT1X activity raises MT2A's level | lines that do not express MT1X (5) vs lines expressing it (45) | 6.97× lower at baseline in the lines without MT1X | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: RABGEF1P3, KIFC3, ENSG00000255031; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.876). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.6, 13.3); signed map (14.5, 31.6). **Vector** length 159, 59.0% of its response variance represented; |z| ≥ 3 in 1,593 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (hallmark, mean cos +0.61 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +8.8 | +5.7 |
|  | [[Belinostat (drug)]] 5 µM |  | +8.6 | +4.4 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +8.0 | +7.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +7.8 | +3.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.7 | +4.8 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +7.6 | +6.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +7.6 | +6.8 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | +7.5 | +5.7 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -9.7 | -3.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -9.2 | -3.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -8.6 | -2.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -8.6 | -6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -8.5 | -9.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -6.8 | -4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | -6.1 | -3.6 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | -4.8 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.5 | -3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.5 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | metallothionein 1X |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16q13 — chr16:56,682,470-56,684,196 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MT-1l; previously MT1 |
| Gene groups (HGNC) | Metallothioneins |
| Reactome | 3 pathways, smallest: Metallothioneins bind metals; Response to metal ions; Cellular responses to stimuli |
| Matched by | ensembl_id |

**Function**, from UniProt [P80297](https://www.uniprot.org/uniprotkb/P80297) (Metallothionein-1X):

> Metallothioneins have a high content of cysteine residues that bind various heavy metals; these proteins are transcriptionally regulated by both heavy metals and glucocorticoids. May be involved in FAM168A anti-apoptotic signaling.

**Summary**, from NCBI Gene [4501](https://www.ncbi.nlm.nih.gov/gene/4501):

> Predicted to enable copper ion binding activity and zinc ion binding activity. Involved in cellular response to cadmium ion; cellular response to erythropoietin; and cellular response to zinc ion. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:7405](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7405) · Entrez [4501](https://www.ncbi.nlm.nih.gov/gene/4501) · UniProt [P80297](https://www.uniprot.org/uniprotkb/P80297) · Ensembl [ENSG00000187193](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000187193)

## Data

Gene col 11900: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11900); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11900, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11900]; `tensor/DDL_lfc|DDL_z.npy` [11900]; `embed/gene_vectors.npy` [11900]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11900 or target_col == 11900). Every well: [[MT1X — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MT1X.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
