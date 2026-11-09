---
symbol: "TEX2"
type: "gene"
col: 5868
ensembl_id: "ENSG00000136478"
name: "testis expressed 2"
location: "17q23.3"
module: 35
arm: "-"
pooled_cpm: 29.64
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# TEX2

*testis expressed 2* — 17q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 4.52× (z +30.2, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (none with an alert); the strongest is [[GSK1059615 (drug)]] 0.5 µM: 0.732× (z -4.5, q 0.004, down in 20 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STIMATE]] (+0.66, fdr 7e-06), [[UBE2F]] (+0.65, fdr 1e-05), [[TTL]] (+0.63, fdr 7e-06); moves opposite to [[C11orf71]] (-0.68, fdr 1e-05), [[N4BP2L1]] (-0.65, fdr 3e-05), [[PIGP]] (-0.64, fdr 2e-05).
> It sits in the **-** arm of [[Module 035]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5868.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **4.52×** | +30.2 | 0e+00 | 48/48 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **3.85×** | +27.0 | 0e+00 | 47/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.65×** | +25.9 | 0e+00 | 48/48 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.86×** | +12.4 | 4e-33 | 43/48 (HOP62, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.83×** | +12.1 | 9e-32 | 44/47 (SNU-423, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.43×** | +9.3 | 2e-18 | 41/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.52×** | +8.4 | 4e-15 | 26/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.33×** | +7.9 | 1e-13 | 25/48 (A549, HEC-1-A, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.46×** | +7.6 | 2e-12 | 27/47 (SW480, A-172, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~53% of this change | **1.44×** | +7.0 | 2e-10 | 28/46 (MIA PaCa-2, SNU-423, …) | two highest doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.80×** | +6.1 | 4e-08 | 21/46 (A498, HEC-1-A, …) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.34×** | +5.6 | 1e-06 | 21/47 (A-172, hTERT-HPNE, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.31×** | +5.3 | 4e-06 | 19/48 (NCI-H2347, SNU-423, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +5.1 | 1e-05 | 21/47 (CFPAC-1, SW480, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **1.23×** | +4.0 | 0.002 | 18/47 (A-172, H4, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.21×** | +3.8 | 0.005 | 14/47 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belumosudil (drug)]] 5 µM |  | **1.20×** | +3.5 | 0.013 | 13/47 (RPMI-7951, NCI-H23, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.18× | +3.3 | 0.025 | 6/47 (A498, SNU-423, …) | inconsistent across doses |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 1.18× | +3.3 | 0.026 | 12/47 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Belinostat (drug)]] 0.05 µM |  | 1.17× | +3.1 | 0.048 | 5/47 (A-172, A549, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | 1.16× | +2.9 | 0.080 | 13/48 (A498, NCI-H1573, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5868.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 0.5 µM |  | **0.732×** | -4.5 | 0.004 | 20/48 (LoVo, Panc 03.27, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.862× | -4.3 | 0.004 | 18/48 (SK-MEL-2, C32, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.810×** | -4.2 | 0.004 | 13/48 (SK-MEL-2, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.767×** | -3.8 | 0.020 | 15/45 (MIA PaCa-2, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.776×** | -3.6 | 0.030 | 12/48 (LOX-IMVI, HCT15, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.49 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5868. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 24.6 | 5 (1 ⚠) | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 4.07× (z +13.9) | [[Digitoxin (drug)]] 5 µM 0.352× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[CFPAC-1 (line)]] | alt | 14.5 | 5 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.88× (z +12.7) | — |
| [[A-427 (line)]] | wt | 40.4 | 3 | 1 | [[Belinostat (drug)]] 5 µM 3.12× (z +10.7) | [[Homoharringtonine (drug)]] 0.5 µM 0.392× (z -8.9) |
| [[A549 (line)]] | wt | 23.4 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 5.34× (z +11.2) | — |
| [[HepG2_C3A (line)]] | wt | 43.3 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 4.51× (z +11.2) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0914× (z -17.2) ⚠ toxic; cell-cycle shift, explains ~53% of this change |
| [[NCI-H1573 (line)]] | alt | 17.9 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.71× (z +9.2) | [[Digitoxin (drug)]] 5 µM 0.249× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change |
| [[NCI-H23 (line)]] | alt | 35.3 | 3 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 4.04× (z +11.7) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.198× (z -13.1) ⚠ cell-cycle shift, explains ~65% of this change |
| [[NCI-H2347 (line)]] | alt | 26.0 | 3 | 1 (1 ⚠) | [[Belinostat (drug)]] 5 µM 3.25× (z +10.3) | [[Docetaxel (drug)]] 0.05 µM 0.270× (z -11.5) ⚠ transcription drop; cell-cycle shift, explains ~82% of this change |
| [[SNU-423 (line)]] | alt | 23.3 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.57× (z +12.9) | — |
| [[A-172 (line)]] | wt | 39.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.49× (z +12.1) | — |
| [[A498 (line)]] | wt | 22.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.78× (z +12.8) | — |
| [[AsPC-1 (line)]] | alt | 8.71 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.88× (z +10.3) | — |
| [[COLO 205 (line)]] | alt | 17.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.03× (z +10.1) | — |
| [[HEC-1-A (line)]] | alt | 28.0 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.85× (z +15.4) | — |
| [[HOP62 (line)]] | alt | 24.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.03× (z +14.1) | — |
| [[HS-578T (line)]] | alt | 26.0 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.05× (z +11.9) | — |
| [[HT-29 (line)]] | alt | 18.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.25× (z +12.2) | — |
| [[hTERT-HPNE (line)]] | wt | 20.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 10.3× (z +12.7) | — |
| [[J82 (line)]] | alt | 30.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.80× (z +11.5) | — |
| [[KATO III (line)]] | alt | 28.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.76× (z +12.6) | — |
| [[LoVo (line)]] | wt | 17.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 6.58× (z +14.8) | — |
| [[LOX-IMVI (line)]] | wt | 23.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.13× (z +12.3) | — |
| [[LS 180 (line)]] | wt | 24.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.66× (z +12.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 32.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.55× (z +12.8) | — |
| [[NCI-H1792 (line)]] | alt | 23.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.78× (z +12.2) | — |
| [[NCI-H2030 (line)]] | alt | 21.4 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.66× (z +11.3) | — |
| [[Panc 03.27 (line)]] | alt | 40.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.49× (z +13.7) | — |
| [[PANC-1 (line)]] | alt | 25.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.09× (z +11.0) | — |
| [[RPMI-7951 (line)]] | alt | 16.8 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.94× (z +9.9) | — |
| [[SW 900 (line)]] | alt | 27.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.78× (z +10.9) | — |
| [[SW1417 (line)]] | alt | 39.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.04× (z +13.2) | — |
| [[SW480 (line)]] | alt | 58.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.00× (z +18.2) | — |
| [[C-33 A (line)]] | alt | 53.4 | 1 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.22× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.247× (z -10.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 40.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.33× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 86.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 2.48× (z +8.6) ⚠ toxic; cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.545× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 36.8 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.127× (z -8.5) ⚠ cell-cycle shift, explains ~77% of this change |
| [[H4 (line)]] | wt | 15.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 9.67× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 23.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.21× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 19.5 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.03× (z +8.5) | — |
| [[RKO (line)]] | wt | 35.2 | 1 | 0 | [[Belinostat (drug)]] 5 µM 3.04× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 43.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.06× (z +9.3) | — |
| [[AN3 CA (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 34.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5868), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*55 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STIMATE]] | +0.66 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[UBE2F]] | +0.65 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[TTL]] | +0.63 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[NUP93]] | +0.63 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[LYPLA1]] | +0.62 | +0.53 / +0.45 | both halves | 3e-05 |  |
| [[ABCC10]] | +0.62 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[PPM1F]] | +0.62 | +0.50 / +0.48 | both halves | 2e-05 |  |
| [[AP3M2]] | +0.61 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[GNA12]] | +0.61 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[NTAQ1]] | +0.61 | +0.47 / +0.53 | both halves | 2e-05 |  |
| [[TREX2]] | +0.61 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[XPO5]] | +0.61 | +0.48 / +0.64 | both halves | 2e-05 |  |

## Genes that move opposite

*45 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C11orf71]] | -0.68 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[N4BP2L1]] | -0.65 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[PIGP]] | -0.64 | -0.50 / -0.47 | both halves | 2e-05 |  |
| [[AK9]] | -0.63 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[APOLD1]] | -0.63 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[OSER1-DT]] | -0.62 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[CHMP2B]] | -0.61 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[DNAH12]] | -0.61 | -0.49 / -0.40 | both halves | 5e-05 |  |
| [[GUCY2C-AS1]] | -0.61 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[YTHDC1]] | -0.59 | -0.45 / -0.55 | both halves | 3e-05 |  |
| [[GPBP1]] | -0.59 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[LINC02398]] | -0.58 | -0.36 / -0.38 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **-** arm (projection on the module's main direction -0.550). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-7.0, -26.7); signed map (-44.7, -14.4). **Vector** length 80.7, 17.0% of its response variance represented; |z| ≥ 3 in 1,184 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.6 | +8.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.5 | +12.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.1 | +27.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.0 | +25.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.7 | +30.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.2 | +9.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +2.1 | +3.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.9 | +2.1 |
|  | [[EX229 (drug)]] 5 µM |  | +1.9 | +1.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.8 | +1.8 |
| fall | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.5 | -4.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -3.6 | +3.8 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.6 | -4.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.3 | -0.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | +2.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -3.1 | -0.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | +1.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.9 | -0.8 |
|  | [[Binimetinib (drug)]] 5 µM |  | -2.9 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | testis expressed 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.3 — chr17:64,147,227-64,263,260 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HT008, TMEM96, KIAA1738 |
| Reactome | 4 pathways, smallest: RHOA GTPase cycle; RHO GTPase cycle; Signaling by Rho GTPases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWB9](https://www.uniprot.org/uniprotkb/Q8IWB9) (Testis-expressed protein 2):

> During endoplasmic reticulum (ER) stress or when cellular ceramide levels increase, may induce contacts between the ER and medial-Golgi complex to facilitate non-vesicular transport of ceramides from the ER to the Golgi complex where they are converted to complex sphingolipids, preventing toxic ceramide accumulation.

**Summary**, from NCBI Gene [55852](https://www.ncbi.nlm.nih.gov/gene/55852):

> Predicted to enable lipid binding activity. Predicted to be involved in signal transduction and sphingolipid metabolic process. Predicted to be located in membrane. Predicted to be active in endoplasmic reticulum. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30884](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30884) · Entrez [55852](https://www.ncbi.nlm.nih.gov/gene/55852) · UniProt [Q8IWB9](https://www.uniprot.org/uniprotkb/Q8IWB9) · Ensembl [ENSG00000136478](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136478)

## Data

Gene col 5868: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5868); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5868, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5868]; `tensor/DDL_lfc|DDL_z.npy` [5868]; `embed/gene_vectors.npy` [5868]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5868 or target_col == 5868). Every well: [[TEX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TEX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
