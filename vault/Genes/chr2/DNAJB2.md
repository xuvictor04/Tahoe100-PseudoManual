---
symbol: "DNAJB2"
type: "gene"
col: 5779
ensembl_id: "ENSG00000135924"
name: "DnaJ heat shock protein family (Hsp40) member B2"
location: "2q35"
module: 12
arm: "+"
pooled_cpm: 24.58
n_lines_expressing: 50
n_dd_up: 22
n_dd_down: 16
n_dd_up_clean: 18
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# DNAJB2

*DnaJ heat shock protein family (Hsp40) member B2* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.09× (z +14.1, q 2e-42, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[PH-797804 (drug)]] 5 µM: 0.394× (z -6.6, q 2e-08, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CREB3]] (+0.66, fdr 1e-05), [[ARVCF]] (+0.64, fdr 7e-06), [[ZFAND2B]] (+0.63, fdr 1e-05); moves opposite to [[RANBP1]] (-0.67, fdr 7e-06), [[MCM3]] (-0.63, fdr 7e-06), [[POLA1]] (-0.62, fdr 7e-06).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5779.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.09×** | +14.1 | 2e-42 | 38/47 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.01×** | +9.5 | 5e-19 | 38/48 (NCI-H2347, A498, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.08×** | +9.4 | 8e-19 | 38/48 (SW1417, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.91×** | +8.8 | 1e-16 | 34/47 (SW1417, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +7.7 | 1e-12 | 33/47 (A-427, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.59×** | +6.3 | 2e-08 | 28/48 (RKO, A-427, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.54×** | +5.9 | 2e-07 | 27/48 (NCI-H460, A-427, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +5.8 | 5e-07 | 26/47 (NCI-H1573, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.51×** | +5.6 | 1e-06 | 28/48 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.51×** | +5.6 | 1e-06 | 29/44 (PANC-1, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~6% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.28×** | +4.7 | 1e-04 | 24/48 (LS 180, HT-29, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.39×** | +4.5 | 3e-04 | 20/48 (HepG2/C3A, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.36×** | +4.2 | 0.001 | 23/47 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.59×** | +3.9 | 0.004 | 16/48 (LS 180, BT-474, …) | all doses, flat | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.008 | 19/47 (HepG2/C3A, HT-29, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.32×** | +3.7 | 0.009 | 17/47 (NCI-H2030, MIA PaCa-2, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.49×** | +3.3 | 0.031 | 11/46 (SNU-423, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5779.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[PH-797804 (drug)]] 5 µM |  | **0.394×** | -6.6 | 2e-08 | 34/47 (C32, Panc 03.27, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.624×** | -6.4 | 4e-08 | 28/48 (A-172, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.636×** | -6.2 | 1e-07 | 31/47 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.647×** | -5.9 | 5e-07 | 30/48 (KATO III, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.442×** | -5.8 | 7e-07 | 28/49 (LOX-IMVI, AsPC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.679×** | -5.3 | 1e-05 | 27/47 (KATO III, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.710×** | -4.5 | 6e-04 | 22/46 (NCI-H1792, A-172, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.758×** | -3.8 | 0.012 | 15/48 (HS-578T, CFPAC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.761×** | -3.7 | 0.013 | 17/47 (HS-578T, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.824×** | -3.7 | 0.014 | 18/48 (SNU-1, BT-474, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.782×** | -3.3 | 0.042 | 18/47 (NCI-H460, RPMI-7951, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.783×** | -3.3 | 0.042 | 12/48 (NCI-H460, NCI-H2030, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.787×** | -3.1 | 0.089 | 16/47 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses |  |
| [[Adenosine (drug)]] 0.5 µM |  | **0.798×** | -3.1 | 0.089 | 6/48 (Hs 766T, SW 900, …) | inconsistent across doses | position effect removed |
| [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | **0.800×** | -3.0 | 0.089 | 6/48 (LS 180, SW48, …) | inconsistent across doses |  |
| [[Loperamide (hydrochloride) (drug)]] 0.5 µM |  | **0.800×** | -3.0 | 0.089 | 5/48 (CFPAC-1, HS-578T, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5779. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 20.5 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.53× (z +13.4) | — |
| [[HT-29 (line)]] | alt | 22.2 | 1 | 2 (2 ⚠) | [[Ixazomib citrate (drug)]] 0.5 µM 3.95× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.182× (z -10.4) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 20.1 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.24× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 24.1 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +11.0) | [[Digitoxin (drug)]] 5 µM 0.186× (z -11.3) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 31.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.59× (z +10.4) | — |
| [[A-172 (line)]] | wt | 49.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.29× (z +9.8) | — |
| [[A498 (line)]] | wt | 19.4 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.92× (z +9.3) | — |
| [[AsPC-1 (line)]] | alt | 29.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.67× (z +16.0) | — |
| [[HOP62 (line)]] | alt | 22.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.38× (z +12.5) | — |
| [[NCI-H2347 (line)]] | alt | 22.2 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.21× (z +9.3) | — |
| [[PANC-1 (line)]] | alt | 15.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.22× (z +11.9) | — |
| [[RKO (line)]] | wt | 19.8 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 5.40× (z +8.9) | — |
| [[SW480 (line)]] | alt | 15.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.58× (z +8.7) | — |
| [[A-427 (line)]] | wt | 19.6 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.89× (z +9.9) | — |
| [[AN3 CA (line)]] | alt | 24.1 | 0 | 1 | — | [[Flumatinib (mesylate) (drug)]] 5 µM 0.0712× (z -8.7) |
| [[C32 (line)]] | wt | 55.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.284× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 31.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.317× (z -8.8) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 15.4 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.06× (z +8.6) | — |
| [[LoVo (line)]] | wt | 13.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.38× (z +13.0) | — |
| [[LOX-IMVI (line)]] | wt | 28.0 | 0 | 1 | — | [[TAK-901 (drug)]] 0.05 µM 0.274× (z -9.3) |
| [[MIA PaCa-2 (line)]] | alt | 17.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +9.0) | — |
| [[NCI-H1792 (line)]] | alt | 23.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0989× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 35.5 | 1 | 0 | [[Harringtonine (drug)]] 5 µM 3.26× (z +8.9) | — |
| [[NCI-H23 (line)]] | alt | 23.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +12.1) | — |
| [[SW 900 (line)]] | alt | 20.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.62× (z +10.5) | — |
| [[A549 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 35.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 31.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 50.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 19.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5779), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CREB3]] | +0.66 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[ARVCF]] | +0.64 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[ZFAND2B]] | +0.63 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[RELA]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[WBP2]] | +0.62 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[GFER]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[ATF4]] | +0.62 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[SNHG32]] | +0.60 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[BRF2]] | +0.60 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[WASHC1]] | +0.60 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[FAM50A]] | +0.58 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[RBMX2]] | +0.58 | +0.63 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RANBP1]] | -0.67 | -0.64 / -0.67 | both halves | 7e-06 |  |
| [[MCM3]] | -0.63 | -0.60 / -0.61 | both halves | 7e-06 |  |
| [[POLA1]] | -0.62 | -0.66 / -0.62 | both halves | 7e-06 |  |
| [[VMA21]] | -0.60 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[GART]] | -0.58 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[C1QBP]] | -0.58 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[NUP155]] | -0.58 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[TFDP1]] | -0.57 | -0.58 / -0.59 | both halves | 7e-06 |  |
| [[NAF1]] | -0.57 | -0.55 / -0.61 | both halves | 1e-05 |  |
| [[DHX15]] | -0.57 | -0.51 / -0.66 | both halves | 1e-05 |  |
| [[MDN1]] | -0.57 | -0.60 / -0.56 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.57 | -0.52 / -0.56 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.582). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-37.3, -15.4); signed map (-4.5, 23.1). **Vector** length 129, 36.6% of its response variance represented; |z| ≥ 3 in 977 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.8 | +14.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +7.6 | +9.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.5 | +9.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.2 | +7.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +7.0 | +8.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +5.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.2 | +6.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.9 | +4.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.5 | +3.1 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -6.6 | -5.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -6.4 | -6.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -5.8 | -6.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -5.7 | -5.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.5 | -5.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.1 | -3.3 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.9 | -3.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -2.4 | -3.0 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -2.4 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | DnaJ heat shock protein family (Hsp40) member B2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:219,279,342-219,286,898 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HSPF3, CMT2T; previously HSJ1 |
| Gene groups (HGNC) | DNAJ (HSP40) heat shock proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [P25686](https://www.uniprot.org/uniprotkb/P25686) (DnaJ homolog subfamily B member 2):

> Functions as a co-chaperone, regulating the substrate binding and activating the ATPase activity of chaperones of the HSP70/heat shock protein 70 family. In parallel, also contributes to the ubiquitin-dependent proteasomal degradation of misfolded proteins. Thereby, may regulate the aggregation and promote the functional recovery of misfolded proteins like HTT, MC4R, PRKN, RHO and SOD1 and be crucial for many biological processes. Isoform 1 which is localized to the endoplasmic reticulum …

**Summary**, from NCBI Gene [3300](https://www.ncbi.nlm.nih.gov/gene/3300):

> This gene is almost exclusively expressed in the brain, mainly in the neuronal layers. It encodes a protein that shows sequence similarity to bacterial DnaJ protein and the yeast homologs. In bacteria, this protein is implicated in protein folding and protein complex dissociation. Alternatively spliced transcript variants encoding different isoforms have been described for this gene. [provided by RefSeq, Jul 2011]

**Accessions** — [HGNC:5228](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5228) · Entrez [3300](https://www.ncbi.nlm.nih.gov/gene/3300) · UniProt [P25686](https://www.uniprot.org/uniprotkb/P25686) · Ensembl [ENSG00000135924](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135924)

## Data

Gene col 5779: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5779); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5779, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5779]; `tensor/DDL_lfc|DDL_z.npy` [5779]; `embed/gene_vectors.npy` [5779]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5779 or target_col == 5779). Every well: [[DNAJB2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DNAJB2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
