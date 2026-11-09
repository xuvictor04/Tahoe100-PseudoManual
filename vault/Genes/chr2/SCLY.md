---
symbol: "SCLY"
type: "gene"
col: 5301
ensembl_id: "ENSG00000132330"
name: "selenocysteine lyase"
location: "2q37.3"
module: 5
arm: "+"
pooled_cpm: 19.71
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 4
n_dd_up_clean: 19
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# SCLY

*selenocysteine lyase* — 2q37.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.38× (z +27.6, q 0e+00, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 0.835× (z -4.8, q 7e-04, down in 21 of 48 measured lines) ⚠ cell-cycle shift, explains ~0% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.661× (z -4.1, q 0.009, down in 13 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAM16]] (+0.66, fdr 7e-06), [[HIRA]] (+0.65, fdr 1e-04), [[ADCY3]] (+0.63, fdr 2e-05); moves opposite to [[NDUFA5]] (-0.60, fdr 2e-04), [[OAZ2]] (-0.58, fdr 3e-05), [[KIDINS220]] (-0.56, fdr 6e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[NT5M]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5301.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.38×** | +27.6 | 0e+00 | 47/48 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.75×** | +26.7 | 0e+00 | 45/47 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **4.07×** | +26.3 | 0e+00 | 46/48 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.42×** | +23.0 | 0e+00 | 46/47 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **2.42×** | +15.9 | 0e+00 | 37/47 (NCI-H460, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.12×** | +14.1 | 5e-43 | 42/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **2.02×** | +12.6 | 2e-34 | 35/45 (NCI-H460, HT-29, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.90×** | +12.0 | 2e-31 | 38/47 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.90×** | +11.5 | 6e-29 | 32/48 (A-172, HT-29, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.53×** | +11.1 | 5e-27 | 30/47 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.75×** | +10.4 | 1e-23 | 32/47 (NCI-H460, HEC-1-A, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.60×** | +8.7 | 1e-16 | 32/47 (MIA PaCa-2, HOP62, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.39×** | +8.7 | 2e-16 | 29/48 (A-172, HOP62, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **2.22×** | +7.8 | 3e-13 | 35/48 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.36×** | +5.7 | 5e-07 | 19/47 (HOP62, A-172, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.67×** | +5.0 | 2e-05 | 18/47 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.27×** | +4.5 | 2e-04 | 13/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.55×** | +4.3 | 6e-04 | 12/46 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **1.47×** | +3.8 | 0.005 | 7/47 (HEC-1-A, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | 1.15× | +3.7 | 0.006 | 14/48 (A-172, HEC-1-A, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5301.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.835× | -4.8 | 7e-04 | 21/48 (A-427, SNU-1, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.629×** | -4.6 | 0.001 | 17/45 (RKO, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.661×** | -4.1 | 0.009 | 13/48 (NCI-H1573, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **0.811×** | -4.0 | 0.010 | 12/47 (RPMI-7951, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **0.814×** | -3.7 | 0.022 | 9/47 (HS-578T, AsPC-1, …) | top dose only | plate-row cell shift |
| [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | 0.844× | -3.2 | 0.12 | 13/47 (HepG2/C3A, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.62 per unit of S-phase module lfc, -0.33 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5301. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 23.7 | 4 | 3 (3 ⚠) | [[Panobinostat (drug)]] 5 µM 3.37× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.276× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 20.5 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.29× (z +17.0) | — |
| [[HEC-1-A (line)]] | alt | 27.3 | 6 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.56× (z +12.3) | — |
| [[HT-29 (line)]] | alt | 14.7 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.02× (z +11.8) | — |
| [[NCI-H460 (line)]] | wt | 23.3 | 6 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.30× (z +16.7) | — |
| [[HOP62 (line)]] | alt | 12.1 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.11× (z +13.8) | — |
| [[SNU-423 (line)]] | alt | 12.5 | 5 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.72× (z +12.8) | — |
| [[SW480 (line)]] | alt | 23.2 | 5 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 5.06× (z +14.3) | — |
| [[A549 (line)]] | wt | 19.1 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.59× (z +14.9) | — |
| [[CFPAC-1 (line)]] | alt | 10.1 | 4 | 0 | [[Panobinostat (drug)]] 0.5 µM 9.54× (z +12.1) | — |
| [[NCI-H1792 (line)]] | alt | 17.0 | 4 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +12.3) | — |
| [[A498 (line)]] | wt | 21.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.49× (z +14.8) | — |
| [[AsPC-1 (line)]] | alt | 8.88 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.30× (z +10.3) | — |
| [[HS-578T (line)]] | alt | 14.9 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 4.29× (z +8.9) | — |
| [[KATO III (line)]] | alt | 12.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.52× (z +10.9) | — |
| [[LoVo (line)]] | wt | 23.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.02× (z +13.1) | — |
| [[LS 180 (line)]] | wt | 22.9 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.82× (z +10.4) | — |
| [[MIA PaCa-2 (line)]] | alt | 23.0 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.24× (z +9.4) | [[Adagrasib (drug)]] 0.05 µM 0.644× (z -9.7) ⚠ position not correctable |
| [[NCI-H1573 (line)]] | alt | 27.2 | 2 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.36× (z +10.2) | [[Dinaciclib (drug)]] 0.5 µM 0.257× (z -11.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H2030 (line)]] | alt | 14.9 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.64× (z +9.6) | [[Dinaciclib (drug)]] 0.05 µM 0.147× (z -12.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[Panc 03.27 (line)]] | alt | 13.0 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.81× (z +10.2) | — |
| [[Hs 766T (line)]] | wt | 11.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.40× (z +9.8) | — |
| [[hTERT-HPNE (line)]] | wt | 10.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.00× (z +9.1) | — |
| [[J82 (line)]] | alt | 14.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.63× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 12.0 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.65× (z +9.4) | — |
| [[RKO (line)]] | wt | 46.0 | 0 | 2 (2 ⚠) | — | [[NG25 (drug)]] 5 µM 0.109× (z -9.8) ⚠ cell-cycle shift, explains ~46% of this change |
| [[RPMI-7951 (line)]] | alt | 15.8 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.42× (z +8.9) | — |
| [[SHP-77 (line)]] | alt | 56.4 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.45× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.162× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 24.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.53× (z +9.7) | — |
| [[A-427 (line)]] | wt | 30.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +8.5) | — |
| [[C-33 A (line)]] | alt | 31.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.153× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 10.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 10.1× (z +8.7) | — |
| [[H4 (line)]] | wt | 11.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.19× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 15.1 | 0 | 1 | — | [[Ciclopirox (drug)]] 5 µM 0.242× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 23.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 30.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.309× (z -8.8) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[NCI-H2347 (line)]] | alt | 6.29 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.13× (z +9.6) | — |
| [[SW 900 (line)]] | alt | 11.9 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 6.73× (z +8.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[AN3 CA (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5301), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAM16]] | +0.66 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[HIRA]] | +0.65 | +0.34 / +0.68 | both halves | 1e-04 |  |
| [[ADCY3]] | +0.63 | +0.48 / +0.65 | both halves | 2e-05 |  |
| [[NDUFAF2]] | +0.62 | +0.61 / +0.55 | both halves | 1e-05 |  |
| [[TMEM181]] | +0.61 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[SRPK1]] | +0.61 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[FOXK2]] | +0.61 | +0.32 / +0.66 | both halves | 1e-04 |  |
| [[ATR]] | +0.60 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[GART]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[TEAD4]] | +0.59 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[PINX1-1]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[LYRM4]] | +0.59 | +0.53 / +0.52 | both halves | 1e-05 | STRING 788 |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NDUFA5]] | -0.60 | -0.31 / -0.59 | both halves | 2e-04 |  |
| [[OAZ2]] | -0.58 | -0.45 / -0.52 | both halves | 3e-05 | pathway: Metabolism of amino acids and derivatives |
| [[KIDINS220]] | -0.56 | -0.38 / -0.51 | both halves | 6e-05 |  |
| [[SF3B1]] | -0.54 | -0.41 / -0.57 | both halves | 4e-05 |  |
| [[MORF4L1]] | -0.54 | -0.57 / -0.55 | both halves | 1e-05 |  |
| [[VWA5A]] | -0.54 | -0.35 / -0.43 | both halves | 1e-04 |  |
| [[BROX]] | -0.53 | -0.33 / -0.61 | both halves | 1e-04 |  |
| [[MAGED2]] | -0.53 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[PMPCB]] | -0.53 | -0.24 / -0.53 | both halves | 4e-04 |  |
| [[DMXL1]] | -0.52 | -0.37 / -0.52 | both halves | 8e-05 |  |
| [[TAB2]] | -0.52 | -0.37 / -0.53 | both halves | 9e-05 |  |
| [[GSN]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NT5M]] | B | NT5M activity raises SCLY's level | lines that do not express NT5M (7) vs lines expressing it (43) | 1.81× lower at baseline in the lines without NT5M | 0.024 | ⚠ within organs, on part of the lines; also absent: GXYLT2, GPR155, PKIG |
| [[TOP2A]] | B | TOP2A activity lowers SCLY's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.0% of all compounds | 0.032 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CHGB]] | B | CHGB activity raises SCLY's level | lines that do not express CHGB (33) vs lines expressing it (17) | 1.53× lower at baseline in the lines without CHGB | 0.050 | ⚠ within organs, on part of the lines; also absent: MAGEA4, SLC6A11, CTNNA2 |
| [[LRRC69]] | C | LRRC69's natural level weakens SCLY's drug response | LRRC69's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.62, reverse +0.29; direction not clear | 0.082 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SLFNL1-AS1]] | C | SLFNL1-AS1 activity raises SCLY's level | lines that do not express SLFNL1-AS1 (4) vs lines expressing it (46) | 1.63× lower at baseline in the lines without SLFNL1-AS1 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CATSPER2P1, FAM182B, ENSG00000287400; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.602). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-6.0, -36.8); signed map (-0.9, -53.5). **Vector** length 74.9, 15.8% of its response variance represented; |z| ≥ 3 in 1,160 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +5.2 | +10.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +26.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~5% of this change | +2.7 | +3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | +2.6 | +15.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +2.6 | +4.3 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +2.4 | +3.6 |
|  | [[EX229 (drug)]] 5 µM |  | +2.3 | +5.0 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.1 | +3.6 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +1.7 | +2.1 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.4 | -4.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.8 | +11.1 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | -3.3 | -4.6 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.0 | -1.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -2.9 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.9 | +3.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.4 | -1.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.9 | -1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[Ixazomib (drug)]] 5 µM |  | -1.8 | -0.1 |

## What is on record

|  |  |
|---|---|
| Name | selenocysteine lyase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.3 — chr2:238,060,924-238,099,413 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SCL |
| Reactome | 3 pathways, smallest: Metabolism of ingested SeMet, Sec, MeSec into H2Se; Selenoamino acid metabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96I15](https://www.uniprot.org/uniprotkb/Q96I15) (Selenocysteine lyase):

> Catalyzes the decomposition of L-selenocysteine to L-alanine and elemental selenium.

**Summary**, from NCBI Gene [51540](https://www.ncbi.nlm.nih.gov/gene/51540):

> Selenocysteine lyase (SCLY; EC 4.4.1.16) catalyzes the pyridoxal 5-prime phosphate-dependent conversion of L-selenocysteine to L-alanine and elemental selenium (Mihara et al., 2000 [PubMed 10692412]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:18161](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18161) · Entrez [51540](https://www.ncbi.nlm.nih.gov/gene/51540) · UniProt [Q96I15](https://www.uniprot.org/uniprotkb/Q96I15) · Ensembl [ENSG00000132330](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132330)

## Data

Gene col 5301: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5301); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5301, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5301]; `tensor/DDL_lfc|DDL_z.npy` [5301]; `embed/gene_vectors.npy` [5301]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5301 or target_col == 5301). Every well: [[SCLY — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCLY.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
