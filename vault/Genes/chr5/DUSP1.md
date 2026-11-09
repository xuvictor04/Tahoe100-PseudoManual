---
symbol: "DUSP1"
type: "gene"
col: 4159
ensembl_id: "ENSG00000120129"
name: "dual specificity phosphatase 1"
location: "5q35.1"
module: 113
arm: "+"
pooled_cpm: 62.77
n_lines_expressing: 44
n_dd_up: 29
n_dd_down: 8
n_dd_up_clean: 22
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 14
direction_downstream: 10
tags: ["gene", "module/113"]
generated_by: "tahoemap"
---

# DUSP1

*dual specificity phosphatase 1* — 5q35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 29 drug-doses (7 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.38× (z +10.6, q 3e-23, up in 33 of 41 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 4.24× (z +6.5, q 1e-08, up in 34 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.518× (z -8.0, q 6e-13, down in 30 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFP36L1]] (+0.73, fdr 7e-06), [[CEBPB]] (+0.68, fdr 7e-06), [[TIPARP]] (+0.68, fdr 7e-06); moves opposite to [[ZCCHC4]] (-0.49, fdr 1e-04), [[METTL21A]] (-0.46, fdr 1e-04).
> It is in [[Module 113]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[ABLIM3]] → it (grade B ⚠); 10 go from it, the strongest it → [[STK17B]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4159.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **2.38×** | +10.6 | 3e-23 | 33/41 (CFPAC-1, SW 900, …) | rises with dose | composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **3.17×** | +9.0 | 9e-17 | 35/41 (MIA PaCa-2, NCI-H1573, …) | rises with dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **4.24×** | +6.5 | 1e-08 | 34/43 (A549, PANC-1, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **2.00×** | +5.4 | 7e-06 | 27/43 (SW 900, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.86×** | +5.4 | 7e-06 | 26/42 (A549, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +5.4 | 7e-06 | 34/42 (HS-578T, NCI-H2347, …) | rises with dose | position effect removed |
| [[Budesonide (drug)]] 0.05 µM |  | **1.84×** | +5.2 | 1e-05 | 33/42 (SW 900, NCI-H1573, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.79×** | +5.0 | 3e-05 | 32/43 (NCI-H2347, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dexamethasone (drug)]] 5 µM |  | **1.79×** | +5.0 | 4e-05 | 27/42 (SW 900, HS-578T, …) | all doses, flat |  |
| [[Budesonide (drug)]] 0.5 µM |  | **1.76×** | +4.9 | 6e-05 | 28/42 (SW 900, HS-578T, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +4.7 | 1e-04 | 25/41 (MIA PaCa-2, NCI-H460, …) | top dose only | cell-cycle shift (explains ~25% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +4.5 | 3e-04 | 22/42 (A-172, A-427, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.69×** | +4.5 | 3e-04 | 29/42 (NCI-H460, SW 900, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.05 µM |  | **1.65×** | +4.3 | 6e-04 | 27/42 (NCI-H1573, SW 900, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **1.61×** | +4.1 | 0.001 | 26/42 (NCI-H1573, HS-578T, …) | all doses, stronger at high dose |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | **1.59×** | +4.0 | 0.002 | 26/44 (NCI-H1573, SW 900, …) | inconsistent across doses | position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.86×** | +3.8 | 0.005 | 25/42 (A498, CFPAC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **1.55×** | +3.8 | 0.005 | 25/42 (SW 900, HS-578T, …) | all doses, flat |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.53×** | +3.7 | 0.007 | 23/42 (CFPAC-1, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4159.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.518×** | -8.0 | 6e-13 | 30/43 (A498, AsPC-1, …) | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.537×** | -5.4 | 2e-05 | 31/42 (AsPC-1, J82, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.508×** | -5.3 | 3e-05 | 30/42 (SNU-423, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.528×** | -5.0 | 1e-04 | 25/35 (AsPC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.620×** | -4.1 | 0.004 | 30/42 (AsPC-1, SNU-423, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.592×** | -4.1 | 0.004 | 26/43 (hTERT-HPNE, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.733×** | -3.8 | 0.013 | 25/42 (AsPC-1, A498, …) | top dose only |  |
| [[Rifaximin (drug)]] 0.5 µM |  | **0.684×** | -3.3 | 0.074 | 23/42 (AsPC-1, A-172, …) | all doses, flat | position effect removed |
| [[Adenosine (drug)]] 0.5 µM |  | 0.694× | -3.2 | 0.10 | 14/42 (H4, A498, …) | inconsistent across doses | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | 0.777× | -3.1 | 0.12 | 23/42 (CFPAC-1, LS 180, …) | rises with dose | low cells (technical?) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.702× | -3.1 | 0.12 | 16/42 (NCI-H2347, AsPC-1, …) | inconsistent across doses | position effect removed |
| [[Rifaximin (drug)]] 5 µM |  | 0.680× | -3.0 | 0.13 | 22/42 (CFPAC-1, A-172, …) | all doses, flat | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, +0.61 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4159. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 81.1 | 3 (1 ⚠) | 4 | [[Auranofin (drug)]] 5 µM 6.90× (z +12.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.226× (z -13.6) |
| [[NCI-H2347 (line)]] | alt | 107 | 2 (2 ⚠) | 5 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +10.3) ⚠ cell-cycle shift, explains ~47% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.180× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 197 | 2 (2 ⚠) | 4 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.63× (z +10.1) ⚠ cell-cycle shift, explains ~76% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.181× (z -19.2) |
| [[A498 (line)]] | wt | 149 | 2 (2 ⚠) | 3 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 5.22× (z +10.3) ⚠ cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -19.8) |
| [[A549 (line)]] | wt | 148 | 3 (1 ⚠) | 2 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 5.06× (z +11.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.209× (z -16.0) |
| [[HS-578T (line)]] | alt | 79.8 | 1 (1 ⚠) | 4 | [[Harringtonine (drug)]] 5 µM 4.52× (z +8.8) ⚠ cell-cycle shift, explains ~29% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -14.6) |
| [[MIA PaCa-2 (line)]] | alt | 49.2 | 5 (3 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 10.5× (z +12.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 5.80× (z +10.5) | — |
| [[A-427 (line)]] | wt | 20.3 | 3 (2 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 6.24× (z +8.7) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Auranofin (drug)]] 5 µM 5.03× (z +8.5) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -8.8) |
| [[HOP62 (line)]] | alt | 129 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.178× (z -16.3) |
| [[hTERT-HPNE (line)]] | wt | 139 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -17.8) |
| [[NCI-H460 (line)]] | wt | 48.9 | 4 (2 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 6.61× (z +10.5) | — |
| [[SNU-423 (line)]] | alt | 130 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0416× (z -16.7) |
| [[HepG2_C3A (line)]] | wt | 108 | 1 (1 ⚠) | 2 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.01× (z +9.9) ⚠ cell-cycle shift, explains ~76% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -12.0) |
| [[NCI-H1573 (line)]] | alt | 38.8 | 3 (2 ⚠) | 0 | [[Harringtonine (drug)]] 5 µM 13.3× (z +10.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Citalopram (hydrobromide) (drug)]] 0.05 µM 6.25× (z +8.5) | — |
| [[PANC-1 (line)]] | alt | 75.9 | 2 (1 ⚠) | 1 | [[Harringtonine (drug)]] 5 µM 5.66× (z +10.5) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 18.6× (z +10.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -14.3) |
| [[SW 900 (line)]] | alt | 102 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.93× (z +10.9) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Dexamethasone (drug)]] 5 µM 4.65× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 93.2 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 4.62× (z +14.8) ⚠ cell-cycle shift, explains ~47% of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -10.0) |
| [[HT-29 (line)]] | alt | 91.8 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.242× (z -9.8) |
| [[J82 (line)]] | alt | 98.5 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.338× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 16.9 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +8.6) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[SHP-77 (line)]] | alt | 47.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -12.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 38.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.68× (z +9.3) ⚠ cell-cycle shift, explains ~47% of this change | — |
| [[AN3 CA (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.9 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 14.9 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 40.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 49.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 66.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 21.1 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 37.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 89.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 12.8 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 56.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 53.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 14.5 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.2 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 75.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 15.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4159), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFP36L1]] | +0.73 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[CEBPB]] | +0.68 | +0.61 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 465 |
| [[TIPARP]] | +0.68 | +0.67 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[KLF9]] | +0.66 | +0.66 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[IRS2]] | +0.66 | +0.65 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA |
| [[ZFP36]] | +0.64 | +0.66 / +0.60 | both halves | 7e-06 | pathway: HALLMARK_HYPOXIA; STRING 934 |
| [[ZMYND8]] | +0.63 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ZFAND5]] | +0.63 | +0.51 / +0.72 | both halves | 1e-05 |  |
| [[MT1E]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 | pathway: HALLMARK_HYPOXIA |
| [[SNAI2]] | +0.63 | +0.62 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_UV_RESPONSE_DN |
| [[MT1X]] | +0.63 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[TRIB1]] | +0.63 | +0.54 / +0.62 | both halves | 1e-05 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 571 |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZCCHC4]] | -0.49 | -0.34 / -0.49 | both halves | 1e-04 |  |
| [[METTL21A]] | -0.46 | -0.44 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 12, C 2. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABLIM3]] | B | ABLIM3 activity raises DUSP1's level | lines that do not express ABLIM3 (15) vs lines expressing it (35) | 2.43× lower at baseline in the lines without ABLIM3 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: LINC00511, MILR1, TLR4; maybe low, not absent |
| [[ETS2]] | B | ETS2 activity raises DUSP1's level | lines that do not express ETS2 (10) vs lines expressing it (40) | 2.04× lower at baseline in the lines without ETS2 | 0.021 | ⚠ within organs, on part of the lines; also absent: KITLG, FAM107B, LGALS3 |
| [[PDLIM1]] | B | PDLIM1 activity raises DUSP1's level | lines that do not express PDLIM1 (11) vs lines expressing it (39) | 2.79× lower at baseline in the lines without PDLIM1 | 0.024 | ⚠ within organs, on part of the lines; also absent: PCED1B, GPR39, ATP8B1 |
| [[SH3TC1]] | B | SH3TC1 activity raises DUSP1's level | lines that do not express SH3TC1 (10) vs lines expressing it (40) | 2.30× lower at baseline in the lines without SH3TC1 | 0.043 | ⚠ within organs, on part of the lines; also absent: GBP2, NDRG1, RSAD2 |
| [[TOP2A]] | B | TOP2A activity raises DUSP1's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.0% of all compounds | 0.044 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[TSC22D3]] | B | TSC22D3 activity raises DUSP1's level | lines that do not express TSC22D3 (11) vs lines expressing it (39) | 1.73× lower at baseline in the lines without TSC22D3 | 0.044 | ⚠ within organs, on part of the lines; also absent: IL15, IGFBP3, PAG1; maybe low, not absent |
| [[NEDD9]] | B | NEDD9 activity raises DUSP1's level | lines that do not express NEDD9 (16) vs lines expressing it (34) | 1.74× lower at baseline in the lines without NEDD9 | 0.057 | ⚠ within organs, on part of the lines; also absent: ITGA1, LGALS3, DGKG |
| [[NR3C1]] | B | NR3C1 activity raises DUSP1's level | compounds that target NR3C1: 3 of 3 raise it (Betamethasone dipropionate, Budesonide, Dexamethasone) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[HIPK2]] | B | HIPK2 activity raises DUSP1's level | lines that do not express HIPK2 (5) vs lines expressing it (45) | 1.73× lower at baseline in the lines without HIPK2 | 0.067 | ⚠ within organs, on part of the lines; also absent: MARCHF3, ASPH, ENSG00000286533; maybe low, not absent |
| [[DEPP1]] | B | DEPP1 activity raises DUSP1's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 2.31× lower at baseline in the lines without DEPP1 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |
| [[FOXC2]] | B | FOXC2 activity raises DUSP1's level | lines that do not express FOXC2 (33) vs lines expressing it (17) | 2.12× lower at baseline in the lines without FOXC2 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KIRREL3, LINC01411, SIRLNT |
| [[ADRB2]] | B | ADRB2 activity raises DUSP1's level | lines that do not express ADRB2 (23) vs lines expressing it (27) | 1.92× lower at baseline in the lines without ADRB2 | 0.097 | ⚠ within organs, on part of the lines; also absent: GBP5, ADAMTS16, ENSG00000271933 |

### Downstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 9, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[STK17B]] | B | DUSP1 activity raises STK17B's level | lines that do not express DUSP1 (6) vs lines expressing it (44) | 2.38× lower at baseline in the lines without DUSP1 | 0.010 | ⚠ within organs, on part of the lines; also absent: PC, PLD1, DENND3; maybe low, not absent |
| [[METTL21A]] | B | DUSP1 activity strengthens METTL21A's drug response | lines that do not express DUSP1 (6) vs lines expressing it (42) | the lines without DUSP1 respond 0.67× as strongly (z diff +1.44); strongest at Dinaciclib 5 µM: 0.34x vs 1.38x (z diff +9.0) | 0.014 | ⚠ within organs, on part of the lines; also absent: PC, PLD1, DENND3; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[PDLIM1]] | B | DUSP1 activity raises PDLIM1's level | lines that do not express DUSP1 (6) vs lines expressing it (44) | 4.90× lower at baseline in the lines without DUSP1 | 0.027 | ⚠ within organs, on part of the lines; also absent: PC, PLD1, DENND3; maybe low, not absent |
| [[METTL21A]] | B | DUSP1 activity lowers METTL21A's level | lines that do not express DUSP1 (6) vs lines expressing it (44) | 1.49× higher at baseline in the lines without DUSP1 | 0.054 | ⚠ within organs, on part of the lines; also absent: PC, PLD1, DENND3; maybe low, not absent |
| [[B4GALT1]] | B | DUSP1 activity raises B4GALT1's level | lines that do not express DUSP1 (6) vs lines expressing it (44) | 2.25× lower at baseline in the lines without DUSP1 | 0.069 | ⚠ within organs, on part of the lines; also absent: PC, PLD1, DENND3; maybe low, not absent |
| [[SH3BP4]] | B | DUSP1 activity raises SH3BP4's level | lines that do not express DUSP1 (6) vs lines expressing it (44) | 1.97× lower at baseline in the lines without DUSP1 | 0.073 | ⚠ within organs, on part of the lines; also absent: PC, PLD1, DENND3; maybe low, not absent |
| [[AKAP13]] | B | DUSP1 activity raises AKAP13's level | lines that do not express DUSP1 (6) vs lines expressing it (44) | 1.61× lower at baseline in the lines without DUSP1 | 0.081 | ⚠ within organs, on part of the lines; also absent: PC, PLD1, DENND3; maybe low, not absent |
| [[PELI1]] | B | DUSP1 activity raises PELI1's level | lines that do not express DUSP1 (6) vs lines expressing it (44) | 1.86× lower at baseline in the lines without DUSP1 | 0.094 | ⚠ within organs, on part of the lines; also absent: PC, PLD1, DENND3; maybe low, not absent |
| [[NEDD9]] | B | DUSP1 activity raises NEDD9's level | lines that do not express DUSP1 (6) vs lines expressing it (44) | 3.52× lower at baseline in the lines without DUSP1 | 0.099 | ⚠ within organs, on part of the lines; also absent: PC, PLD1, DENND3; maybe low, not absent |
| [[DENND3]] | C | DUSP1 activity raises DENND3's level | lines that do not express DUSP1 (6) vs lines expressing it (44) | 3.04× lower at baseline in the lines without DUSP1 | 0.055 | ⚠ within organs, on part of the lines; also absent: PC, PLD1, DENND3; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 113]] — hypoxia; 43 genes; every member is in the + arm (projection on the module's main direction 0.817). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (28.4, 13.1); signed map (14.4, 30.3). **Vector** length 151, 51.4% of its response variance represented; |z| ≥ 3 in 1,353 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Metallothioneins bind metals* (reactome, mean cos +0.59 to 5); *metallothionein* (control, mean cos +0.59 to 5); *Response to metal ions* (reactome, mean cos +0.59 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Betamethasone dipropionate (drug)]] 5 µM |  | +7.2 | +5.4 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +6.9 | +4.9 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +6.7 | +2.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +5.4 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +6.1 | +4.1 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.7 | -5.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.2 | -8.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.7 | -5.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -4.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.8 | -5.4 |
|  | [[EX229 (drug)]] 5 µM |  | -3.8 | -2.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -2.6 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | -3.4 | -4.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | dual specificity phosphatase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q35.1 — chr5:172,768,096-172,771,195 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HVH1, CL100, MKP-1; previously PTPN10 |
| Gene groups (HGNC) | MAP kinase phosphatases |
| Hallmark sets | UV_RESPONSE_DN, HYPOXIA, TNFA_SIGNALING_VIA_NFKB |
| Reactome | 5 pathways, smallest: RAF-independent MAPK1/3 activation; Negative regulation of MAPK pathway; RAF/MAP kinase cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [P28562](https://www.uniprot.org/uniprotkb/P28562) (Dual specificity protein phosphatase 1):

> Dual specificity phosphatase that dephosphorylates MAP kinase MAPK1/ERK2 on both 'Thr-183' and 'Tyr-185', regulating its activity during the meiotic cell cycle.

**Summary**, from NCBI Gene [1843](https://www.ncbi.nlm.nih.gov/gene/1843):

> The protein encoded by this gene is a phosphatase with dual specificity for tyrosine and threonine. The encoded protein can dephosphorylate MAP kinase MAPK1/ERK2, which results in its involvement in several cellular processes. This protein appears to play an important role in the human cellular response to environmental stress as well as in the negative regulation of cellular proliferation. Finally, the encoded protein can make some solid tumors resistant to both chemotherapy and radiotherapy, …

**Accessions** — [HGNC:3064](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3064) · Entrez [1843](https://www.ncbi.nlm.nih.gov/gene/1843) · UniProt [P28562](https://www.uniprot.org/uniprotkb/P28562) · Ensembl [ENSG00000120129](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120129)

## Data

Gene col 4159: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4159); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4159, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4159]; `tensor/DDL_lfc|DDL_z.npy` [4159]; `embed/gene_vectors.npy` [4159]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4159 or target_col == 4159). Every well: [[DUSP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUSP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
