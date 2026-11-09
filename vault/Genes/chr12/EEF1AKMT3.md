---
symbol: "EEF1AKMT3"
type: "gene"
col: 4433
ensembl_id: "ENSG00000123427"
name: "EEF1A lysine methyltransferase 3"
location: "12q14.1"
module: 15
arm: "+"
pooled_cpm: 7.92
n_lines_expressing: 50
n_dd_up: 4
n_dd_down: 27
n_dd_up_clean: 2
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# EEF1AKMT3

*EEF1A lysine methyltransferase 3* — 12q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.50× (z +7.6, q 2e-11, up in 28 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 27 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.415× (z -16.2, q 0e+00, down in 40 of 45 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.372× (z -12.9, q 1e-35, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01232]] (+0.64, fdr 4e-05), [[BCL2L2-PABPN1]] (+0.63, fdr 3e-05), [[CRYBB2P1]] (+0.63, fdr 7e-06); moves opposite to [[WDR7]] (-0.55, fdr 1e-05), [[IFT88]] (-0.55, fdr 1e-05), [[STK3]] (-0.54, fdr 5e-05).
> It sits in the **+** arm of [[Module 015]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4433.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +7.6 | 2e-11 | 28/43 (NCI-H1573, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.32×** | +5.1 | 8e-05 | 18/47 (A498, A549, …) | rises with dose | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +4.7 | 6e-04 | 11/39 (J82, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.35×** | +4.0 | 0.009 | 7/47 (HOP62, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 30 in all, 10 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 27 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4433.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.415×** | -16.2 | 0e+00 | 40/45 (NCI-H1792, A498, …) | rises with dose | composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.372×** | -12.9 | 1e-35 | 38/48 (NCI-H1792, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.379×** | -12.2 | 9e-32 | 40/46 (NCI-H1792, A498, …) | rises with dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.413×** | -11.5 | 1e-28 | 40/46 (NCI-H1792, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.492×** | -9.2 | 3e-18 | 34/47 (A498, C32, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change | **0.579×** | -7.1 | 1e-10 | 22/40 (NCI-H460, HCT15, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.597×** | -6.7 | 1e-09 | 27/45 (A498, C32, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.617×** | -6.3 | 2e-08 | 22/42 (C32, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.617×** | -6.3 | 2e-08 | 20/48 (SNU-1, SW480, …) | rises with dose | composition shift; position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.603×** | -6.2 | 3e-08 | 20/44 (C32, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.725×** | -5.9 | 2e-07 | 20/47 (NCI-H23, HS-578T, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.424×** | -5.8 | 2e-07 | 23/44 (LOX-IMVI, BT-474, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.669×** | -5.2 | 8e-06 | 21/47 (hTERT-HPNE, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.696×** | -4.7 | 1e-04 | 20/47 (NCI-H1573, C32, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.713×** | -4.4 | 4e-04 | 18/45 (C-33 A, SNU-423, …) | rises with dose |  |
| [[Thymol (drug)]] 5 µM |  | **0.802×** | -4.0 | 0.002 | 11/46 (A-172, A549, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.724×** | -4.0 | 0.002 | 15/44 (NCI-H1792, NCI-H1573, …) | top dose only | position effect removed |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.742×** | -3.9 | 0.003 | 6/47 (COLO 205, SW 1088, …) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.582×** | -3.7 | 0.006 | 16/42 (NCI-H1792, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.757×** | -3.6 | 0.008 | 14/47 (NCI-H1792, NCI-H23, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4433. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 15.2 | 0 | 5 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.121× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 33.0 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -22.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.221× (z -11.0) |
| [[NCI-H460 (line)]] | wt | 6.94 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0852× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.165× (z -9.8) |
| [[A-172 (line)]] | wt | 9.98 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.124× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -8.7) |
| [[A498 (line)]] | wt | 13.4 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -16.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.234× (z -10.2) |
| [[SW480 (line)]] | alt | 6.88 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -13.4) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.213× (z -9.4) |
| [[NCI-H2030 (line)]] | alt | 8.46 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -11.3) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SNU-1 (line)]] | wt | 12.5 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0707× (z -9.7) ⚠ cell-cycle shift, explains ~58% of this change |
| [[A549 (line)]] | wt | 6.32 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -12.2) ⚠ cell-cycle shift, explains ~28% of this change |
| [[AsPC-1 (line)]] | alt | 6.03 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0959× (z -13.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HCT15 (line)]] | alt | 13.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0705× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~47% of this change |
| [[Hs 766T (line)]] | wt | 7.86 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.111× (z -8.7) ⚠ transcription drop |
| [[HS-578T (line)]] | alt | 10.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.286× (z -8.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[hTERT-HPNE (line)]] | wt | 7.31 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0774× (z -9.0) |
| [[MIA PaCa-2 (line)]] | alt | 6.41 | 0 | 1 | — | [[Lumateperone (tosylate) (drug)]] 5 µM 0.241× (z -8.6) |
| [[PANC-1 (line)]] | alt | 5.74 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -8.9) ⚠ cell-cycle shift, explains ~28% of this change |
| [[SNU-423 (line)]] | alt | 9.63 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -10.0) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A-427 (line)]] | wt | 7.52 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.22 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.02 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.62 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.45 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.60 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.40 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.41 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.10 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.51 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.25 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4433), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01232]] | +0.64 | +0.42 / +0.64 | both halves | 4e-05 |  |
| [[BCL2L2-PABPN1]] | +0.63 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[CRYBB2P1]] | +0.63 | +0.64 / +0.64 | both halves | 7e-06 |  |
| [[GOT1-DT]] | +0.62 | +0.37 / +0.56 | both halves | 9e-05 |  |
| [[CAPN10-DT]] | +0.62 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[CRLS1]] | +0.60 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[BCL2L2]] | +0.60 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[LINC00115]] | +0.59 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[RNF139-DT]] | +0.59 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[FAHD2A]] | +0.58 | +0.45 / +0.49 | both halves | 3e-05 |  |
| [[VDAC1P8]] | +0.58 | +0.43 / +0.53 | both halves | 3e-05 |  |
| [[EOLA1]] | +0.57 | +0.56 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR7]] | -0.55 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[IFT88]] | -0.55 | -0.51 / -0.51 | both halves | 1e-05 |  |
| [[STK3]] | -0.54 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[SVIL]] | -0.54 | -0.55 / -0.48 | both halves | 2e-05 |  |
| [[CLEC16A]] | -0.54 | -0.48 / -0.59 | both halves | 2e-05 |  |
| [[KLF2]] | -0.54 | -0.45 / -0.40 | both halves | 4e-05 |  |
| [[RABEP1]] | -0.53 | -0.54 / -0.60 | both halves | 1e-05 |  |
| [[TAF1B]] | -0.53 | -0.50 / -0.49 | both halves | 1e-05 |  |
| [[TRNP1]] | -0.53 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[DHRS2]] | -0.52 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[PBRM1]] | -0.52 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[RABGAP1L]] | -0.52 | -0.43 / -0.48 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.593). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-8.1, 22.7); signed map (1.8, 1.1). **Vector** length 73.9, 12.6% of its response variance represented; |z| ≥ 3 in 1,051 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +7.6 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +4.8 | +5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.4 | +0.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.1 | +0.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +0.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.6 | +1.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.5 | +1.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.4 | +2.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +4.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -4.2 | -12.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | -3.4 | -16.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.0 | -5.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | -6.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.1 | -3.9 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -1.9 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | EEF1A lysine methyltransferase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q14.1 — chr12:57,771,492-57,782,541 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP586D0919; previously FAM119B, METTL21B |
| Gene groups (HGNC) | 7BS protein lysine methyltransferases; Non-histone lysine methyltransferases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96AZ1](https://www.uniprot.org/uniprotkb/Q96AZ1) (EEF1A lysine methyltransferase 3):

> Protein-lysine methyltransferase that selectively mono-, di- and trimethylates 'Lys-165' of the translation elongation factors EEF1A1 and EEF1A2 in an aminoacyl-tRNA and GTP-dependent manner. EEF1A1 methylation by EEF1AKMT3 is dynamic as well as inducible by stress conditions, such as ER-stress, and plays a regulatory role on mRNA translation.

**Summary**, from NCBI Gene [25895](https://www.ncbi.nlm.nih.gov/gene/25895):

> Enables heat shock protein binding activity and protein-lysine N-methyltransferase activity. Involved in peptidyl-lysine methylation. Located in centrosome and cytoplasm. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24936](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24936) · Entrez [25895](https://www.ncbi.nlm.nih.gov/gene/25895) · UniProt [Q96AZ1](https://www.uniprot.org/uniprotkb/Q96AZ1) · Ensembl [ENSG00000123427](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123427)

## Data

Gene col 4433: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4433); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4433, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4433]; `tensor/DDL_lfc|DDL_z.npy` [4433]; `embed/gene_vectors.npy` [4433]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4433 or target_col == 4433). Every well: [[EEF1AKMT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EEF1AKMT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
