---
symbol: "MINPP1"
type: "gene"
col: 2879
ensembl_id: "ENSG00000107789"
name: "multiple inositol-polyphosphate phosphatase 1"
location: "10q23.2"
module: 20
arm: "+"
pooled_cpm: 15.57
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 10
n_dd_up_clean: 13
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# MINPP1

*multiple inositol-polyphosphate phosphatase 1* — 10q23.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.69× (z +14.4, q 3e-44, up in 45 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.618× (z -7.0, q 1e-09, down in 29 of 45 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.701× (z -5.2, q 4e-05, down in 23 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CUL2]] (+0.63, fdr 1e-05), [[SKP2]] (+0.63, fdr 1e-05), [[MRPL19]] (+0.63, fdr 1e-05); moves opposite to [[TCF25]] (-0.60, fdr 1e-05), [[LRCH3]] (-0.60, fdr 2e-05), [[OFD1]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2879.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.69×** | +14.4 | 3e-44 | 45/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.44×** | +13.0 | 3e-36 | 45/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.32×** | +12.2 | 4e-32 | 39/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.83×** | +8.8 | 2e-16 | 38/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.48×** | +6.9 | 5e-10 | 26/43 (SW480, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **2.36×** | +6.5 | 7e-09 | 28/47 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **2.22×** | +6.1 | 1e-07 | 29/47 (PANC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.34×** | +6.0 | 2e-07 | 25/47 (NCI-H460, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +5.6 | 1e-06 | 25/47 (LoVo, J82, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~38% of this change | **1.38×** | +4.5 | 4e-04 | 17/42 (HS-578T, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.35×** | +4.4 | 6e-04 | 18/46 (MIA PaCa-2, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.23×** | +4.3 | 0.001 | 15/46 (HS-578T, SW480, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.31×** | +3.9 | 0.004 | 14/47 (LS 180, CFPAC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.30×** | +3.8 | 0.005 | 12/46 (SW480, Hs 766T, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **1.26×** | +3.4 | 0.029 | 15/45 (RPMI-7951, A-172, …) | rises with dose |  |
| [[AZD-7648 (drug)]] 5 µM |  | **1.54×** | +3.3 | 0.035 | 7/43 (LS 180, HOP62, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +3.1 | 0.074 | 11/46 (A498, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.25×** | +3.0 | 0.082 | 11/46 (A-172, SW1417, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2879.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.618×** | -7.0 | 1e-09 | 29/45 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.897× | -5.2 | 4e-05 | 11/47 (LoVo, NCI-H23, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.701×** | -5.2 | 4e-05 | 23/47 (HepG2/C3A, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.731×** | -4.6 | 6e-04 | 20/40 (NCI-H1792, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **0.679×** | -4.0 | 0.006 | 18/45 (SW48, LoVo, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **0.682×** | -4.0 | 0.006 | 12/46 (SW480, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.763×** | -4.0 | 0.006 | 17/46 (NCI-H1573, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.767×** | -3.7 | 0.013 | 10/27 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.796×** | -3.4 | 0.047 | 19/46 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.726×** | -3.3 | 0.047 | 18/44 (HepG2/C3A, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.785×** | -3.3 | 0.052 | 13/33 (HS-578T, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.26 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2879. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 19.0 | 3 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.83× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.309× (z -9.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 17.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 3.57× (z +10.0) | — |
| [[A-427 (line)]] | wt | 16.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -11.3) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1792 (line)]] | alt | 26.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.134× (z -12.7) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 21.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.263× (z -11.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 14.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.08× (z +8.5) | — |
| [[H4 (line)]] | wt | 16.4 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.114× (z -8.7) |
| [[Hs 766T (line)]] | wt | 12.8 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.152× (z -9.8) |
| [[HS-578T (line)]] | alt | 11.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.119× (z -10.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 15.1 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -10.8) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.175× (z -10.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 17.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.218× (z -8.5) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 24.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.220× (z -9.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.261× (z -8.5) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.954 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 18.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.61 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 24.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2879), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*81 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CUL2]] | +0.63 | +0.64 / +0.51 | both halves | 1e-05 | same gene group |
| [[SKP2]] | +0.63 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[MRPL19]] | +0.63 | +0.64 / +0.50 | both halves | 1e-05 |  |
| [[STARD7]] | +0.62 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[PAFAH1B2]] | +0.62 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[POMGNT2]] | +0.61 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[PGAM1]] | +0.60 | +0.55 / +0.45 | both halves | 3e-05 | STRING 911 |
| [[PYURF]] | +0.60 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[SDHAF3]] | +0.60 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[ABHD10]] | +0.58 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[PHB1]] | +0.58 | +0.57 / +0.39 | both halves | 6e-05 |  |
| [[DLAT]] | +0.58 | +0.58 / +0.50 | both halves | 1e-05 |  |

## Genes that move opposite

*19 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TCF25]] | -0.60 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[LRCH3]] | -0.60 | -0.63 / -0.47 | both halves | 2e-05 |  |
| [[OFD1]] | -0.58 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[FAM193A]] | -0.58 | -0.51 / -0.56 | both halves | 1e-05 |  |
| [[CDK3]] | -0.56 | -0.45 / -0.47 | both halves | 3e-05 |  |
| [[LCAT]] | -0.55 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[SPAG5-AS1]] | -0.54 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[CATSPERG]] | -0.54 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[TMEM91]] | -0.53 | -0.45 / -0.42 | both halves | 4e-05 |  |
| [[TRNAU1AP]] | -0.52 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[CHMP4A]] | -0.52 | -0.41 / -0.46 | both halves | 4e-05 |  |
| [[MFSD2B]] | -0.52 | -0.41 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.424). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-10.9, -13.1); signed map (-36.5, -19.9). **Vector** length 69.0, 11.7% of its response variance represented; |z| ≥ 3 in 1,016 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.2 | +6.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.9 | +6.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +3.5 | +6.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.9 | +2.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +1.8 | +1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | +3.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +1.5 | +2.4 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +1.5 | +2.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.5 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.8 | -2.8 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -7.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | -3.3 | +4.3 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.1 | -5.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.0 | -4.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -3.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.0 | -4.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | -1.8 | -2.0 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -1.7 | -2.4 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -1.7 | -4.0 |

## What is on record

|  |  |
|---|---|
| Name | multiple inositol-polyphosphate phosphatase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.2 — chr10:87,504,875-87,553,461 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MIPP |
| Gene groups (HGNC) | Phosphoinositide phosphatases; MicroRNA protein coding host genes |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 1 pathways, smallest: Inositol phosphate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNW1](https://www.uniprot.org/uniprotkb/Q9UNW1) (Multiple inositol polyphosphate phosphatase 1):

> Multiple inositol polyphosphate phosphatase that hydrolyzes 1D-myo-inositol 1,3,4,5,6-pentakisphosphate (InsP5[2OH]) and 1D-myo-inositol hexakisphosphate (InsP6) to a range of less phosphorylated inositol phosphates. This regulates the availability of these various small molecule second messengers and metal chelators which control many aspects of cell physiology. Has a weak in vitro activity towards 1D-myo-inositol 1,4,5-trisphosphate which is unlikely to be physiologically relevant. By …

**Summary**, from NCBI Gene [9562](https://www.ncbi.nlm.nih.gov/gene/9562):

> This gene encodes multiple inositol polyphosphate phosphatase; an enzyme that removes 3-phosphate from inositol phosphate substrates. It is the only enzyme known to hydrolzye inositol pentakisphosphate and inositol hexakisphosphate. This enzyme also converts 2,3 bisphosphoglycerate (2,3-BPG) to 2-phosphoglycerate; an activity formerly thought to be exclusive to 2,3-BPG synthase/2-phosphatase (BPGM) in the Rapoport-Luebering shunt of the glycolytic pathway.[provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:7102](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7102) · Entrez [9562](https://www.ncbi.nlm.nih.gov/gene/9562) · UniProt [Q9UNW1](https://www.uniprot.org/uniprotkb/Q9UNW1) · Ensembl [ENSG00000107789](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000107789)

## Data

Gene col 2879: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2879); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2879, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2879]; `tensor/DDL_lfc|DDL_z.npy` [2879]; `embed/gene_vectors.npy` [2879]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2879 or target_col == 2879). Every well: [[MINPP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MINPP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
