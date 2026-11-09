---
symbol: "ANXA2R-OT1"
type: "gene"
col: 10863
ensembl_id: "ENSG00000177738"
name: "ANXA2R overlapping transcript 1"
location: "5p12"
module: 15
arm: "+"
pooled_cpm: 19.39
n_lines_expressing: 49
n_dd_up: 13
n_dd_down: 21
n_dd_up_clean: 8
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ANXA2R-OT1

*ANXA2R overlapping transcript 1* — 5p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.56× (z +29.7, q 0e+00, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.310× (z -19.3, q 0e+00, down in 45 of 47 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAAF10]] (+0.73, fdr 1e-05), [[PBLD]] (+0.70, fdr 2e-04), [[SAP30L-AS1]] (+0.70, fdr 2e-05); moves opposite to [[USP2]] (-0.67, fdr 1e-05), [[STARD5]] (-0.64, fdr 2e-05), [[RALGAPA2]] (-0.64, fdr 3e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10863.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.56×** | +29.7 | 0e+00 | 44/45 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.61×** | +11.2 | 2e-26 | 36/47 (BT-474, SW1417, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +10.3 | 8e-23 | 33/45 (HS-578T, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.74×** | +9.2 | 6e-18 | 28/46 (SW1417, SW480, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +8.0 | 1e-13 | 27/47 (SW480, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.49×** | +6.3 | 3e-08 | 19/42 (NCI-H1573, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +4.7 | 2e-04 | 15/28 (BT-474, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.25×** | +3.7 | 0.015 | 14/39 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.25×** | +3.7 | 0.016 | 7/46 (SNU-423, NCI-H2347, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.24×** | +3.6 | 0.017 | 6/45 (SW480, Hs 766T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.24×** | +3.6 | 0.017 | 12/46 (HS-578T, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~84% of this change | 1.16× | +3.5 | 0.022 | 12/47 (CFPAC-1, SW480, …) | top dose only | low cells (technical?) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **1.22×** | +3.4 | 0.033 | 8/46 (SNU-423, A-427, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.20×** | +3.0 | 0.093 | 10/47 (LoVo, A-427, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10863.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.310×** | -19.3 | 0e+00 | 45/47 (MIA PaCa-2, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.348×** | -17.4 | 0e+00 | 42/47 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.390×** | -15.5 | 0e+00 | 39/46 (HOP62, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.666×** | -9.5 | 5e-19 | 31/47 (A-172, HOP62, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.708×** | -8.0 | 1e-13 | 28/47 (MIA PaCa-2, HOP62, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.658×** | -6.9 | 6e-10 | 27/47 (SNU-423, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.662×** | -6.5 | 5e-09 | 24/47 (SNU-423, PANC-1, …) | rises with dose | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.682×** | -6.3 | 2e-08 | 22/45 (HOP62, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.548×** | -5.2 | 2e-05 | 18/47 (PANC-1, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.567×** | -4.9 | 6e-05 | 15/47 (MIA PaCa-2, C32, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.569×** | -4.8 | 6e-05 | 17/46 (MIA PaCa-2, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.785×** | -4.0 | 0.003 | 17/46 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.796×** | -3.7 | 0.008 | 17/47 (PANC-1, A-172, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.659×** | -3.6 | 0.014 | 13/47 (MIA PaCa-2, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.808×** | -3.5 | 0.018 | 18/46 (MIA PaCa-2, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.668×** | -3.5 | 0.019 | 9/46 (LS 180, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.05 µM |  | **0.821×** | -3.2 | 0.036 | 6/46 (COLO 205, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.12 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10863. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 28.8 | 1 | 8 (5 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +15.8) | [[Panobinostat (drug)]] 5 µM 0.220× (z -15.1) |
| [[MIA PaCa-2 (line)]] | alt | 48.2 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.111× (z -20.3) |
| [[SNU-423 (line)]] | alt | 30.5 | 1 | 5 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.39× (z +9.8) | [[Panobinostat (drug)]] 0.5 µM 0.168× (z -14.0) |
| [[A498 (line)]] | wt | 23.7 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.231× (z -11.8) |
| [[HOP62 (line)]] | alt | 32.0 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.42× (z +9.1) | [[Panobinostat (drug)]] 0.5 µM 0.131× (z -15.0) |
| [[J82 (line)]] | alt | 40.0 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.171× (z -14.0) |
| [[A-172 (line)]] | wt | 39.8 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0739× (z -18.8) |
| [[HT-29 (line)]] | alt | 31.2 | 1 (1 ⚠) | 3 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.27× (z +8.5) ⚠ cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.159× (z -13.2) |
| [[LoVo (line)]] | wt | 7.48 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.52× (z +11.9) | — |
| [[BT-474 (line)]] | alt | 12.3 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.57× (z +15.2) | [[Panobinostat (drug)]] 0.5 µM 0.153× (z -9.3) |
| [[HS-578T (line)]] | alt | 16.4 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.90× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.204× (z -8.6) |
| [[LOX-IMVI (line)]] | wt | 19.5 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.36× (z +10.6) | [[Panobinostat (drug)]] 0.5 µM 0.237× (z -9.0) |
| [[SW480 (line)]] | alt | 8.91 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.50× (z +18.1) | — |
| [[AsPC-1 (line)]] | alt | 14.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.294× (z -9.9) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.180× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 15.5 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.204× (z -9.4) |
| [[NCI-H23 (line)]] | alt | 32.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +15.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.300× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~49% of this change |
| [[NCI-H2347 (line)]] | alt | 23.1 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.200× (z -10.6) |
| [[Panc 03.27 (line)]] | alt | 22.8 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.344× (z -9.5) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SHP-77 (line)]] | alt | 20.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.13× (z +9.9) | [[Dinaciclib (drug)]] 0.05 µM 0.192× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 25.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.156× (z -13.1) ⚠ toxic; cell-cycle shift, explains ~49% of this change |
| [[A549 (line)]] | wt | 10.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.17× (z +9.8) | — |
| [[C-33 A (line)]] | alt | 12.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.33× (z +9.0) | — |
| [[C32 (line)]] | wt | 13.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +9.8) | — |
| [[CFPAC-1 (line)]] | alt | 13.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.58× (z +10.5) | — |
| [[COLO 205 (line)]] | alt | 8.36 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 11.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.06× (z +11.7) | — |
| [[HepG2_C3A (line)]] | wt | 9.51 | 0 | 1 | — | [[Arbutin (drug)]] 5 µM 0.0863× (z -8.8) |
| [[Hs 766T (line)]] | wt | 25.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.25× (z +10.4) | — |
| [[KATO III (line)]] | alt | 5.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.31× (z +8.9) | — |
| [[LS 180 (line)]] | wt | 4.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.61× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 12.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.39× (z +10.5) | — |
| [[NCI-H2030 (line)]] | alt | 22.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.30× (z +12.6) | — |
| [[NCI-H460 (line)]] | wt | 11.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.96× (z +12.4) | — |
| [[NCI-H661 (line)]] | alt | 48.1 | 0 | 1 | — | [[Ritonavir (drug)]] 0.5 µM 0.0517× (z -11.1) |
| [[RPMI-7951 (line)]] | alt | 16.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.147× (z -9.1) |
| [[SW 900 (line)]] | alt | 12.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.62× (z +10.8) | — |
| [[SW1417 (line)]] | alt | 8.91 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.78× (z +15.1) | — |
| [[AN3 CA (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 54.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.83 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10863), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 9 of them with an alert (⚠; 9 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAAF10]] | +0.73 | +0.54 / +0.54 | both halves | 1e-05 |  |
| [[PBLD]] | +0.70 | +0.31 / +0.55 | both halves | 2e-04 |  |
| [[SAP30L-AS1]] | +0.70 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[GTF3C2-AS2]] | +0.68 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[ZNF460-AS1]] | +0.68 | +0.42 / +0.47 | both halves | 4e-05 |  |
| [[MYLK4]] | +0.67 | +0.31 / +0.46 | both halves | 2e-04 |  |
| [[FKBP14-AS1]] | +0.67 | +0.46 / +0.48 | both halves | 2e-05 |  |
| [[KCTD1]] | +0.67 | +0.56 / +0.40 | both halves | 5e-05 |  |
| [[MSANTD2]] | +0.67 | +0.51 / +0.43 | both halves | 3e-05 |  |
| [[LAMTOR5-AS1]] | +0.67 | +0.43 / +0.43 | both halves | 3e-05 |  |
| [[PNISR-AS1]] | +0.66 | +0.36 / +0.34 | both halves | 1e-04 |  |
| [[SETD1B]] | +0.65 | +0.45 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP2]] | -0.67 | -0.50 / -0.56 | both halves | 1e-05 |  |
| [[STARD5]] | -0.64 | -0.48 / -0.47 | both halves | 2e-05 |  |
| [[RALGAPA2]] | -0.64 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[THEM6]] | -0.63 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[FCHO1]] | -0.63 | -0.44 / -0.36 | both halves | 9e-05 |  |
| [[KCTD17]] | -0.63 | -0.32 / -0.51 | both halves | 2e-04 |  |
| [[ALAD]] | -0.62 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[MPP1]] | -0.59 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[RAB3A]] | -0.58 | -0.40 / -0.23 | both halves | 5e-04 |  |
| [[RHPN2]] | -0.57 | -0.43 / -0.30 | both halves | 2e-04 |  |
| [[ALAS1]] | -0.56 | -0.42 / -0.52 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ANXA2R-OT1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CDK18]] | B | CDK18 activity lowers ANXA2R-OT1's level | lines that do not express CDK18 (9) vs lines expressing it (41) | 1.44× higher at baseline in the lines without CDK18 | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC00511, ABCG2, CYP2J2; maybe low, not absent |
| [[LINC00511]] | B | LINC00511 activity lowers ANXA2R-OT1's level | lines that do not express LINC00511 (12) vs lines expressing it (38) | 1.33× higher at baseline in the lines without LINC00511 | 0.080 | ⚠ within organs, on part of the lines; also absent: ABLIM3, LGALS3, CDK18 |
| [[MCTP2]] | B | MCTP2 activity lowers ANXA2R-OT1's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 1.47× higher at baseline in the lines without MCTP2 | 0.092 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.736). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-3.0, 21.1); signed map (18.6, -4.7). **Vector** length 110, 27.0% of its response variance represented; |z| ≥ 3 in 1,122 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +11.1 | +29.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +8.3 | +10.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.6 | +11.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +9.2 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.0 | +8.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.1 | +1.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.0 | +1.4 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -8.6 | -8.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -8.4 | -17.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | -8.2 | -19.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -6.7 | -15.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.9 | -6.3 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.3 | -3.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.1 | -4.9 |
|  | [[venetoclax (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | -1.7 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | ANXA2R overlapping transcript 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 5p12 — chr5:43,013,060-43,067,452 (-) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Overlapping transcripts |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:48996](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:48996) · Entrez [648987](https://www.ncbi.nlm.nih.gov/gene/648987) · Ensembl [ENSG00000177738](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000177738)

## Data

Gene col 10863: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10863); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10863, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10863]; `tensor/DDL_lfc|DDL_z.npy` [10863]; `embed/gene_vectors.npy` [10863]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10863 or target_col == 10863). Every well: [[ANXA2R-OT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANXA2R-OT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
