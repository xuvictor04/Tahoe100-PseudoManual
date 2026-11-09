---
symbol: "OTUD3"
type: "gene"
col: 9873
ensembl_id: "ENSG00000169914"
name: "OTU deubiquitinase 3"
location: "1p36.13"
module: 126
arm: "+"
pooled_cpm: 31.78
n_lines_expressing: 50
n_dd_up: 30
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# OTUD3

*OTU deubiquitinase 3* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.38× (z +20.0, q 0e+00, up in 46 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (Panc 03.27 0.144×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A498 0.311×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH24]] (+0.58, fdr 1e-05), [[ADCY6]] (+0.54, fdr 6e-05), [[PKDCC]] (+0.52, fdr 3e-05); moves opposite to [[SETX]] (-0.50, fdr 2e-05), [[PAIP2]] (-0.48, fdr 2e-04), [[CSNK1A1]] (-0.47, fdr 4e-05).
> It is in [[Module 126]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 33 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 30 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9873.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.38×** | +20.0 | 0e+00 | 46/48 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.94×** | +10.8 | 6e-25 | 41/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.80×** | +9.5 | 2e-19 | 42/48 (J82, Hs 766T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.73×** | +9.0 | 5e-17 | 40/48 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +8.8 | 2e-16 | 37/48 (CFPAC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +8.7 | 3e-16 | 38/46 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.72×** | +8.5 | 1e-15 | 39/48 (SW480, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +7.4 | 1e-11 | 31/45 (HEC-1-A, PANC-1, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +7.3 | 2e-11 | 37/48 (CFPAC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~24% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.56×** | +7.2 | 3e-11 | 29/48 (MIA PaCa-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.53×** | +7.0 | 2e-10 | 31/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.46×** | +6.1 | 4e-08 | 26/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +5.8 | 2e-07 | 28/48 (HT-29, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **1.98×** | +5.8 | 2e-07 | 27/48 (SW480, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.27×** | +5.5 | 2e-06 | 27/47 (PANC-1, NCI-H2030, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.87×** | +5.3 | 4e-06 | 30/48 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **1.67×** | +4.4 | 4e-04 | 21/45 (Panc 03.27, J82, …) | rises with dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **1.45×** | +4.3 | 4e-04 | 17/48 (NCI-H460, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.62×** | +4.1 | 0.001 | 17/48 (CFPAC-1, HEC-1-A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9873.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 1 line (Panc 03.27 0.144×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.05 µM in 1 line (A498 0.311×; ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[OTS514 (drug)]] 5 µM |  | 0.689× | -3.2 | 0.38 | 9/45 (H4, RPMI-7951, …) | top dose only | noisy plate (z scaled) |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | 0.831× | -3.0 | 0.38 | 11/48 (A498, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9873. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 32.8 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.45× (z +13.0) | — |
| [[SW480 (line)]] | alt | 43.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.49× (z +14.4) | — |
| [[A498 (line)]] | wt | 29.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.311× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[AsPC-1 (line)]] | alt | 23.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.04× (z +10.1) | — |
| [[BT-474 (line)]] | alt | 17.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.29× (z +9.7) | — |
| [[CFPAC-1 (line)]] | alt | 18.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.28× (z +13.8) | — |
| [[HEC-1-A (line)]] | alt | 23.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.42× (z +10.5) | — |
| [[HOP62 (line)]] | alt | 25.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.81× (z +11.9) | — |
| [[Hs 766T (line)]] | wt | 27.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.69× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 48.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +11.9) | — |
| [[HT-29 (line)]] | alt | 24.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +13.9) | — |
| [[hTERT-HPNE (line)]] | wt | 24.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.92× (z +10.3) | — |
| [[J82 (line)]] | alt | 37.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.37× (z +10.2) | — |
| [[LoVo (line)]] | wt | 45.6 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.29× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 48.0 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.67× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 29.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.83× (z +12.5) | — |
| [[NCI-H1573 (line)]] | alt | 24.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.10× (z +15.4) | — |
| [[NCI-H1792 (line)]] | alt | 22.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.48× (z +11.3) | — |
| [[NCI-H23 (line)]] | alt | 37.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.31× (z +9.5) | — |
| [[NCI-H2347 (line)]] | alt | 47.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.23× (z +11.1) | — |
| [[NCI-H460 (line)]] | wt | 22.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.10× (z +13.8) | — |
| [[Panc 03.27 (line)]] | alt | 28.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.144× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RKO (line)]] | wt | 31.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.93× (z +10.0) | — |
| [[RPMI-7951 (line)]] | alt | 25.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.77× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 24.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +11.7) | — |
| [[SNU-1 (line)]] | wt | 33.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.87× (z +9.1) | — |
| [[SNU-423 (line)]] | alt | 17.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.89× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 30.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.34× (z +8.8) | — |
| [[SW1417 (line)]] | alt | 39.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.63× (z +10.3) | — |
| [[A-172 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 31.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 59.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 69.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 56.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 54.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 35.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 27.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9873), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*60 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH24]] | +0.58 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[ADCY6]] | +0.54 | +0.49 / +0.38 | both halves | 6e-05 | pathway: Intracellular signaling by second messengers |
| [[PKDCC]] | +0.52 | +0.62 / +0.44 | both halves | 3e-05 |  |
| [[USP21]] | +0.49 | +0.53 / +0.40 | both halves | 5e-05 | pathway: Deubiquitination |
| [[PPFIBP2]] | +0.49 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[C6orf136]] | +0.48 | +0.43 / +0.45 | both halves | 3e-05 |  |
| [[AJM1]] | +0.46 | +0.39 / +0.27 | both halves | 3e-04 |  |
| [[SEC61A2]] | +0.45 | +0.39 / +0.49 | both halves | 6e-05 |  |
| [[ZNF592]] | +0.44 | +0.46 / +0.43 | both halves | 3e-05 |  |
| [[CASC3]] | +0.44 | +0.40 / +0.42 | both halves | 5e-05 |  |
| [[ILKAP]] | +0.44 | +0.46 / +0.41 | both halves | 4e-05 |  |
| [[REV1]] | +0.43 | +0.43 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*40 of its nearest partners move opposite, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SETX]] | -0.50 | -0.47 / -0.47 | both halves | 2e-05 |  |
| [[PAIP2]] | -0.48 | -0.31 / -0.54 | both halves | 2e-04 |  |
| [[CSNK1A1]] | -0.47 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[KDM5A]] | -0.47 | -0.22 / -0.53 | both halves | 6e-04 |  |
| [[TBC1D15]] | -0.46 | -0.28 / -0.46 | both halves | 3e-04 |  |
| [[LINC-PINT]] | -0.46 | -0.45 / -0.50 | both halves | 3e-05 |  |
| [[ATF6]] | -0.45 | -0.32 / -0.28 | both halves | 3e-04 |  |
| [[FER]] | -0.43 | -0.25 / -0.38 | both halves | 4e-04 |  |
| [[STYXL1]] | -0.43 | -0.23 / -0.50 | both halves | 5e-04 |  |
| [[MIR4435-2HG]] | -0.43 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[WDR26]] | -0.43 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[BACH1]] | -0.43 | -0.43 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.340). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.5, -23.2); signed map (-10.8, -33.6). **Vector** length 57.6, 9.67% of its response variance represented; |z| ≥ 3 in 1,041 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.6 | +7.4 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.4 | +9.5 |
|  | [[venetoclax (drug)]] 5 µM |  | +3.3 | +4.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.0 | +4.7 |
|  | [[EX229 (drug)]] 5 µM |  | +2.5 | +2.9 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +2.3 | +4.3 |
|  | [[TAK-733 (drug)]] 5 µM |  | +2.0 | +2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.9 | +3.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +1.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.4 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.8 | -1.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -1.8 | +3.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | -1.7 | +5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.7 | +5.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.4 | -0.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | OTU deubiquitinase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:19,882,395-19,912,945 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0459, DUBA4 |
| Gene groups (HGNC) | OTU domain containing |
| Reactome | 6 pathways, smallest: Ovarian tumor domain proteases; Regulation of PTEN stability and activity; PTEN Regulation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T2D3](https://www.uniprot.org/uniprotkb/Q5T2D3) (OTU domain-containing protein 3):

> Deubiquitinating enzyme that hydrolyzes 'Lys-6'- and 'Lys-11'-linked polyubiquitin. Also hydrolyzes heterotypic (mixed and branched) and homotypic chains. Important regulator of energy metabolism. Glucose and fatty acids trigger its nuclear translocation by CBP-dependent acetylation. In the nucleus, deubiquitinates and stabilizes the nuclear receptor PPARD regulating the expression of various genes involved in glucose and lipid metabolism and oxidative phosphorylation. Also acts as a negative …

**Summary**, from NCBI Gene [23252](https://www.ncbi.nlm.nih.gov/gene/23252):

> Enables cysteine-type deubiquitinase activity. Involved in cellular response to nutrient levels and protein deubiquitination. Acts upstream of or within negative regulation of phosphatidylinositol 3-kinase/protein kinase B signal transduction; protein deubiquitination; and protein stabilization. Located in cytoplasm. Is active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29038](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29038) · Entrez [23252](https://www.ncbi.nlm.nih.gov/gene/23252) · UniProt [Q5T2D3](https://www.uniprot.org/uniprotkb/Q5T2D3) · Ensembl [ENSG00000169914](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169914)

## Data

Gene col 9873: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9873); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9873, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9873]; `tensor/DDL_lfc|DDL_z.npy` [9873]; `embed/gene_vectors.npy` [9873]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9873 or target_col == 9873). Every well: [[OTUD3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OTUD3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
