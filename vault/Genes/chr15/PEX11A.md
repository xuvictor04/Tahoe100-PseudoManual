---
symbol: "PEX11A"
type: "gene"
col: 9363
ensembl_id: "ENSG00000166821"
name: "peroxisomal biogenesis factor 11 alpha"
location: "15q26.1"
module: 89
arm: "+"
pooled_cpm: 7.81
n_lines_expressing: 48
n_dd_up: 15
n_dd_down: 16
n_dd_up_clean: 13
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/089"]
generated_by: "tahoemap"
---

# PEX11A

*peroxisomal biogenesis factor 11 alpha* — 15q26.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (2 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 1.53× (z +5.0, q 3e-04, up in 17 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (8 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.478× (z -8.2, q 1e-13, down in 24 of 32 measured lines) ⚠ toxic. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.290× (z -7.5, q 1e-11, down in 26 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RWDD3]] (+0.62, fdr 1e-05), [[ALKBH4]] (+0.61, fdr 2e-05), [[POLL]] (+0.60, fdr 1e-05); moves opposite to [[WDR1]] (-0.59, fdr 1e-05), [[GNB1]] (-0.57, fdr 2e-05), [[COTL1]] (-0.56, fdr 2e-05).
> It is in [[Module 089]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 2 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9363.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **1.53×** | +5.0 | 3e-04 | 17/45 (LoVo, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.9 | 3e-04 | 16/41 (NCI-H2030, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.43×** | +4.1 | 0.007 | 14/44 (A498, CFPAC-1, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.42×** | +3.9 | 0.010 | 11/43 (NCI-H1792, CFPAC-1, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.40×** | +3.9 | 0.010 | 13/35 (CFPAC-1, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.31×** | +3.6 | 0.028 | 10/45 (NCI-H23, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | **1.22×** | +3.3 | 0.079 | 10/42 (Hs 766T, A549, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | **1.32×** | +3.2 | 0.079 | 10/44 (NCI-H1573, A498, …) | inconsistent across doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.079 | 8/45 (LoVo, NCI-H1573, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 0.5 µM |  | **1.33×** | +3.2 | 0.079 | 6/44 (NCI-H1792, NCI-H460, …) | inconsistent across doses |  |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.1 | 0.079 | 7/39 (SK-MEL-2, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.1 | 0.079 | 9/44 (HOP62, CFPAC-1, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.21×** | +3.1 | 0.079 | 11/44 (CFPAC-1, NCI-H1792, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.079 | 13/44 (SW480, BT-474, …) | inconsistent across doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **1.30×** | +3.1 | 0.079 | 9/43 (NCI-H1792, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 8 with an alert ⚠; shown: the 15 strongest. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9363.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.478×** | -8.2 | 1e-13 | 24/32 (NCI-H2030, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.290×** | -7.5 | 1e-11 | 26/41 (NCI-H460, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.633×** | -7.5 | 1e-11 | 28/43 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.294×** | -7.4 | 2e-11 | 30/44 (NCI-H1792, A549, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.540×** | -7.1 | 1e-10 | 23/45 (NCI-H460, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.626×** | -5.4 | 5e-06 | 19/29 (SW480, LS 180, …) | inconsistent across doses | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.651×** | -5.0 | 5e-05 | 19/39 (NCI-H460, SW480, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.650×** | -4.8 | 1e-04 | 18/45 (NCI-H1792, SW 900, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.697×** | -4.0 | 0.004 | 19/44 (NCI-H460, SNU-423, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.721×** | -3.8 | 0.009 | 18/44 (PANC-1, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.736×** | -3.6 | 0.020 | 18/44 (LS 180, HCT15, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | **0.734×** | -3.3 | 0.042 | 13/23 (HT-29, NCI-H1573, …) | inconsistent across doses | composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.752×** | -3.3 | 0.042 | 15/44 (HT-29, SK-MEL-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.757×** | -3.2 | 0.050 | 17/41 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.759×** | -3.2 | 0.053 | 9/46 (NCI-H460, H4, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9363. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.12 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.276× (z -11.9) |
| [[NCI-H1792 (line)]] | alt | 18.3 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.119× (z -11.4) |
| [[C32 (line)]] | wt | 8.34 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -12.9) |
| [[HT-29 (line)]] | alt | 12.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.104× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[LS 180 (line)]] | wt | 19.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0711× (z -15.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -11.7) |
| [[SNU-423 (line)]] | alt | 4.18 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -8.6) |
| [[COLO 205 (line)]] | alt | 11.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.113× (z -8.7) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 7.62 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.0877× (z -9.9) |
| [[NCI-H1573 (line)]] | alt | 10.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.186× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[NCI-H2030 (line)]] | alt | 8.02 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0946× (z -11.0) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 7.61 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -10.8) |
| [[PANC-1 (line)]] | alt | 8.27 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.187× (z -10.1) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 5.19 | 0 | 1 | — | [[Azithromycin (hydrate) (drug)]] 0.05 µM 0.0644× (z -9.1) |
| [[SW 900 (line)]] | alt | 7.06 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0457× (z -10.4) |
| [[SW1417 (line)]] | alt | 6.54 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[SW480 (line)]] | alt | 9.27 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0806× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change |
| [[A-172 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.78 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.38 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.95 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.38 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.52 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 7.71 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.89 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.97 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 8.24 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.32 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.13 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9363), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RWDD3]] | +0.62 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[ALKBH4]] | +0.61 | +0.47 / +0.68 | both halves | 2e-05 |  |
| [[POLL]] | +0.60 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[MRPL32]] | +0.60 | +0.53 / +0.60 | both halves | 1e-05 |  |
| [[LINC02256]] | +0.59 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[HOXA5]] | +0.58 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[ZNF224]] | +0.55 | +0.57 / +0.45 | both halves | 3e-05 | pathway: Epigenetic regulation of gene expression |
| [[SETDB1]] | +0.55 | +0.48 / +0.56 | both halves | 2e-05 | pathway: Epigenetic regulation of gene expression |
| [[MRPL44]] | +0.54 | +0.33 / +0.63 | both halves | 1e-04 |  |
| [[BTN2A1]] | +0.54 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[ZNF419]] | +0.53 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[THAP3]] | +0.53 | +0.36 / +0.56 | both halves | 1e-04 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR1]] | -0.59 | -0.50 / -0.65 | both halves | 1e-05 |  |
| [[GNB1]] | -0.57 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[COTL1]] | -0.56 | -0.48 / -0.49 | both halves | 2e-05 |  |
| [[G6PD]] | -0.54 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[CSRP1]] | -0.54 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[CAPZB]] | -0.52 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[CORO1C]] | -0.52 | -0.46 / -0.55 | both halves | 3e-05 |  |
| [[ACTN1]] | -0.51 | -0.44 / -0.53 | both halves | 3e-05 |  |
| [[EPB41L2]] | -0.50 | -0.45 / -0.51 | both halves | 3e-05 |  |
| [[CD44]] | -0.50 | -0.42 / -0.54 | both halves | 4e-05 | pathway: HALLMARK_ESTROGEN_RESPONSE_EARLY |
| [[TPM4]] | -0.50 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[YWHAZ]] | -0.50 | -0.41 / -0.57 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 089]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.535). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-43.3, 7.6); signed map (-9.3, -12.5). **Vector** length 63.0, 9.84% of its response variance represented; |z| ≥ 3 in 881 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +2.7 | +2.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.6 | +5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +3.1 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.1 | +3.9 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +2.1 | +3.9 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +2.0 | +3.1 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.6 | +1.9 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -4.6 | -5.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -3.7 | +0.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~41% of this change | -3.4 | -3.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.8 | -8.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.8 | -4.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.8 | -2.9 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -1.3 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -3.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | -7.5 |
|  | [[Methotrexate (drug)]] 5 µM |  | -1.2 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | peroxisomal biogenesis factor 11 alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q26.1 — chr15:89,677,764-89,690,783 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PEX11alpha, PEX11α, PMP28, MGC119947, MGC138534 |
| Gene groups (HGNC) | Peroxins |
| Hallmark sets | BILE_ACID_METABOLISM, PEROXISOME, ESTROGEN_RESPONSE_EARLY |
| Reactome | 8 pathways, smallest: Epigenetic regulation of adipogenesis genes by MLL3 and MLL4 complexes; Epigenetic regulation of gene expression by MLL3 and MLL4 complexes; MLL4 and MLL3 complexes regulate expression of PPARG target genes in adipogenesis and hepatic steatosis |
| Matched by | ensembl_id |

**Function**, from UniProt [O75192](https://www.uniprot.org/uniprotkb/O75192) (Peroxisomal membrane protein 11A):

> May be involved in peroxisomal proliferation and may regulate peroxisomes division. May mediate binding of coatomer proteins to the peroxisomal membrane (By similarity). Promotes membrane protrusion and elongation on the peroxisomal surface.

**Summary**, from NCBI Gene [8800](https://www.ncbi.nlm.nih.gov/gene/8800):

> This gene is a member of the PEX11 family, which is composed of membrane elongation factors involved in regulation of peroxisome maintenance and proliferation. This gene product interacts with peroxisomal membrane protein 19 and may respond to outside stimuli to increase peroxisome abundance. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Oct 2012]

**Accessions** — [HGNC:8852](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8852) · Entrez [8800](https://www.ncbi.nlm.nih.gov/gene/8800) · UniProt [O75192](https://www.uniprot.org/uniprotkb/O75192) · Ensembl [ENSG00000166821](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166821)

## Data

Gene col 9363: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9363); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9363, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9363]; `tensor/DDL_lfc|DDL_z.npy` [9363]; `embed/gene_vectors.npy` [9363]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9363 or target_col == 9363). Every well: [[PEX11A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PEX11A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
