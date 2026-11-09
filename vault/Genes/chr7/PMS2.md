---
symbol: "PMS2"
type: "gene"
col: 4346
ensembl_id: "ENSG00000122512"
name: "PMS1 homolog 2, mismatch repair system component"
location: "7p22.1"
module: 20
arm: "+"
pooled_cpm: 15.19
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 12
n_dd_up_clean: 12
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# PMS2

*PMS1 homolog 2, mismatch repair system component* — 7p22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.33× (z +22.4, q 0e+00, up in 40 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.541× (z -11.5, q 7e-28, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SUPV3L1]] (+0.67, fdr 1e-05), [[ZNF343]] (+0.62, fdr 1e-05), [[TSN]] (+0.61, fdr 2e-05); moves opposite to [[IER5]] (-0.61, fdr 2e-05), [[SRSF9]] (-0.58, fdr 1e-05, ⚠ SRSF9 in the vector space only through flagged drug-doses), [[CLEC16A]] (-0.55, fdr 3e-05), [[TUBB4B]] (-0.54, fdr 6e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 9 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4346.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.33×** | +22.4 | 0e+00 | 40/46 (SW1417, HT-29, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.87×** | +11.7 | 3e-29 | 34/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.54×** | +11.3 | 2e-27 | 36/48 (A-172, J82, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +11.2 | 7e-27 | 28/46 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.66×** | +9.4 | 5e-19 | 29/48 (A498, KATO III, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.57×** | +8.4 | 3e-15 | 32/48 (SW480, A-172, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.52×** | +7.8 | 7e-13 | 25/48 (RPMI-7951, A-427, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.40×** | +6.2 | 3e-08 | 18/47 (SW480, KATO III, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~40% of this change | **1.40×** | +6.1 | 7e-08 | 19/42 (J82, CFPAC-1, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +5.2 | 1e-05 | 11/25 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.31×** | +5.1 | 2e-05 | 17/47 (SW1417, CFPAC-1, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.28×** | +4.5 | 3e-04 | 19/48 (Panc 03.27, SW1417, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.26×** | +4.3 | 7e-04 | 12/48 (PANC-1, LS 180, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.002 | 7/47 (KATO III, SW48, …) | rises with dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | 1.16× | +3.9 | 0.003 | 10/48 (PANC-1, NCI-H2030, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.14× | +3.4 | 0.020 | 11/48 (SW1417, HEC-1-A, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **1.20×** | +3.4 | 0.020 | 6/47 (HOP62, NCI-H1792, …) | all doses, flat |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.42×** | +3.4 | 0.020 | 3/47 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **1.40×** | +3.3 | 0.031 | 3/48 (AsPC-1, A-172, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.19× | +3.2 | 0.038 | 6/47 (KATO III, A-172, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.14× | +3.2 | 0.039 | 7/48 (SW480, NCI-H2347, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Afatinib (drug)]] 5 µM |  | **1.22×** | +3.2 | 0.039 | 8/48 (BT-474, SW1417, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4346.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.541×** | -11.5 | 7e-28 | 31/48 (SW480, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.597×** | -9.7 | 1e-19 | 27/46 (LOX-IMVI, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.649×** | -7.8 | 1e-12 | 26/48 (NCI-H460, PANC-1, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.722×** | -6.1 | 1e-07 | 20/47 (SW480, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **0.734×** | -5.8 | 7e-07 | 20/47 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.738×** | -5.5 | 4e-06 | 19/45 (PANC-1, NCI-H460, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **0.814×** | -5.5 | 4e-06 | 24/47 (SNU-423, PANC-1, …) | rises with dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.767×** | -5.0 | 5e-05 | 14/47 (A498, KATO III, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.815×** | -3.8 | 0.008 | 16/47 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.818×** | -3.8 | 0.009 | 7/48 (SNU-423, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.824×** | -3.6 | 0.014 | 15/48 (A498, NCI-H460, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.829×** | -3.5 | 0.020 | 15/47 (Panc 03.27, Hs 766T, …) | two highest doses |  |
| [[Peretinoin (drug)]] 5 µM |  | 0.837× | -3.2 | 0.057 | 6/47 (LoVo, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.24 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4346. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 17.8 | 1 | 3 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.24× (z +9.8) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.311× (z -10.2) |
| [[HT-29 (line)]] | alt | 10.8 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.94× (z +10.9) | [[Digitoxin (drug)]] 5 µM 0.212× (z -8.8) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 7.16 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0871× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.172× (z -8.6) |
| [[PANC-1 (line)]] | alt | 33.2 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.422× (z -8.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.440× (z -8.5) |
| [[SHP-77 (line)]] | alt | 23.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.69× (z +9.1) | [[Digitoxin (drug)]] 5 µM 0.210× (z -10.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 10.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.4× (z +11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.256× (z -10.9) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 26.1 | 0 | 1 | — | [[Drospirenone (drug)]] 0.5 µM 0.0964× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 7.95 | 0 | 1 (1 ⚠) | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.126× (z -9.0) ⚠ cell-cycle shift, explains ~14% of this change |
| [[H4 (line)]] | wt | 21.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.149× (z -8.8) |
| [[HCT15 (line)]] | alt | 16.6 | 0 | 1 | — | [[vincristine (drug)]] 0.5 µM 0.0730× (z -8.9) |
| [[HEC-1-A (line)]] | alt | 10.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.87× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 12.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +8.8) | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.0818× (z -9.6) |
| [[NCI-H1792 (line)]] | alt | 13.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.48× (z +9.3) | — |
| [[Panc 03.27 (line)]] | alt | 12.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.78× (z +10.5) | — |
| [[RPMI-7951 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.173× (z -8.6) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.361× (z -9.0) ⚠ cell-cycle shift, would explain all of this change |
| [[SW1417 (line)]] | alt | 16.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.62× (z +12.0) | — |
| [[SW48 (line)]] | wt | 16.9 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0974× (z -8.9) |
| [[A-172 (line)]] | wt | 18.1 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.05 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.80 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.20 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.09 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 27.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.44 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4346), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUPV3L1]] | +0.67 | +0.51 / +0.67 | both halves | 1e-05 |  |
| [[ZNF343]] | +0.62 | +0.51 / +0.55 | both halves | 1e-05 |  |
| [[TSN]] | +0.61 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[TMEM68]] | +0.61 | +0.53 / +0.56 | both halves | 1e-05 |  |
| [[SDHAF4]] | +0.59 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[STRADB]] | +0.59 | +0.56 / +0.49 | both halves | 1e-05 |  |
| [[PRMT7]] | +0.59 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[TMEM268]] | +0.59 | +0.49 / +0.61 | both halves | 1e-05 |  |
| [[TMEM94]] | +0.59 | +0.35 / +0.58 | both halves | 1e-04 |  |
| [[RPL6]] | +0.58 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[NAXD]] | +0.58 | +0.35 / +0.50 | both halves | 1e-04 |  |
| [[EIF2D]] | +0.58 | +0.43 / +0.58 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IER5]] | -0.61 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[SRSF9]] ⚠ | -0.58 | -0.50 / -0.53 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[CLEC16A]] | -0.55 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[TUBB4B]] | -0.54 | -0.38 / -0.53 | both halves | 6e-05 | pathway: Affinity selection of immunoglobulins |
| [[OLFM2]] | -0.53 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[TRNP1]] | -0.53 | -0.35 / -0.45 | both halves | 1e-04 |  |
| [[ZSWIM6]] | -0.53 | -0.43 / -0.57 | both halves | 3e-05 |  |
| [[GPR153]] | -0.51 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[EXOC6]] | -0.51 | -0.30 / -0.47 | both halves | 2e-04 |  |
| [[LCAT]] | -0.51 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[TIAM1]] | -0.51 | -0.48 / -0.40 | both halves | 5e-05 |  |
| [[C11orf96]] | -0.50 | -0.30 / -0.58 | both halves | 2e-04 |  |
| [[ATP8B5P-1]] | -0.49 | -0.36 / -0.52 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.430). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-15.1, 18.9); signed map (-31.7, -21.0). **Vector** length 72.5, 12.4% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +6.0 | +11.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +22.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | +4.0 | +7.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +2.2 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | +1.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +8.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +3.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.8 | +1.6 |
|  | [[Afatinib (drug)]] 5 µM |  | +1.7 | +3.2 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.4 | -2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -4.5 | -5.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -4.2 | -3.5 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -4.0 | -7.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | +0.9 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.5 | -1.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.5 | -2.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | +3.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -1.3 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | PMS1 homolog 2, mismatch repair system component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.1 — chr7:5,970,925-6,009,130 (-) |
| Ensembl biotype | protein_coding |
| Also known as | H_DJ0042M02.9, HNPCC4, MLH4, PMS-2; previously PMSL2 |
| Gene groups (HGNC) | MutL homologs |
| Hallmark sets | E2F_TARGETS |
| Reactome | 13 pathways, smallest: Diseases of Mismatch Repair (MMR); Mismatch repair (MMR) directed by MSH2:MSH3 (MutSbeta); Mismatch repair (MMR) directed by MSH2:MSH6 (MutSalpha) |
| Matched by | ensembl_id |

**Function**, from UniProt [P54278](https://www.uniprot.org/uniprotkb/P54278) (Mismatch repair endonuclease PMS2):

> Component of the post-replicative DNA mismatch repair system (MMR). Heterodimerizes with MLH1 to form MutL alpha. DNA repair is initiated by MutS alpha (MSH2-MSH6) or MutS beta (MSH2-MSH3) binding to a dsDNA mismatch, then MutL alpha is recruited to the heteroduplex. Assembly of the MutL-MutS-heteroduplex ternary complex in presence of RFC and PCNA is sufficient to activate endonuclease activity of PMS2. It introduces single-strand breaks near the mismatch and thus generates new entry points …

**Summary**, from NCBI Gene [5395](https://www.ncbi.nlm.nih.gov/gene/5395):

> The protein encoded by this gene is a key component of the mismatch repair system that functions to correct DNA mismatches and small insertions and deletions that can occur during DNA replication and homologous recombination. This protein forms heterodimers with the gene product of the mutL homolog 1 (MLH1) gene to form the MutL-alpha heterodimer. The MutL-alpha heterodimer possesses an endonucleolytic activity that is activated following recognition of mismatches and insertion/deletion loops …

**Accessions** — [HGNC:9122](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9122) · Entrez [5395](https://www.ncbi.nlm.nih.gov/gene/5395) · UniProt [P54278](https://www.uniprot.org/uniprotkb/P54278) · Ensembl [ENSG00000122512](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000122512)

## Data

Gene col 4346: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4346); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4346, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4346]; `tensor/DDL_lfc|DDL_z.npy` [4346]; `embed/gene_vectors.npy` [4346]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4346 or target_col == 4346). Every well: [[PMS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PMS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
