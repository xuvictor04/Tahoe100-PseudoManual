---
symbol: "MRPL39"
type: "gene"
col: 7829
ensembl_id: "ENSG00000154719"
name: "mitochondrial ribosomal protein L39"
location: "21q21.3"
module: 65
arm: "+"
pooled_cpm: 24.69
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 9
n_dd_up_clean: 6
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/065"]
generated_by: "tahoemap"
---

# MRPL39

*mitochondrial ribosomal protein L39* — 21q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.70× (z +7.9, q 1e-12, up in 35 of 46 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.59× (z +7.5, q 2e-11, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.584× (z -7.8, q 5e-12, down in 20 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.710× (z -5.1, q 5e-05, down in 23 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MTX2]] (+0.71, fdr 7e-06), [[RCHY1]] (+0.68, fdr 7e-06), [[ALG9]] (+0.67, fdr 7e-06); moves opposite to [[KPNA4]] (-0.64, fdr 1e-05), [[ZSWIM6]] (-0.57, fdr 1e-05), [[CRK]] (-0.57, fdr 8e-06).
> It sits in the **+** arm of [[Module 065]] (BBSome-mediated cargo-targeting to cilium).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7829.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +7.9 | 1e-12 | 35/46 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **2.59×** | +7.5 | 2e-11 | 34/48 (A498, A-172, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.64×** | +7.5 | 2e-11 | 35/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.43×** | +5.4 | 9e-06 | 27/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.29×** | +3.9 | 0.011 | 16/48 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.011 | 17/47 (BT-474, SK-MEL-2, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.63×** | +3.8 | 0.011 | 19/46 (HEC-1-A, A-172, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.5 | 0.029 | 19/48 (NCI-H460, Hs 766T, …) | rises with dose | low cells (technical?) |
| [[Radotinib (drug)]] 5 µM |  | 1.17× | +3.3 | 0.055 | 13/48 (PANC-1, AsPC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.24×** | +3.2 | 0.074 | 11/48 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.24×** | +3.2 | 0.074 | 17/47 (A-172, A-427, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | **1.23×** | +3.2 | 0.074 | 17/46 (HS-578T, SW 900, …) | inconsistent across doses | low cells (technical?) |
| [[NG25 (drug)]] 5 µM |  | 1.47× | +3.0 | 0.10 | 7/46 (C32, SW48, …) | top dose only | cell-cycle shift (explains ~24% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7829.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.584×** | -7.8 | 5e-12 | 20/35 (A-172, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.620×** | -7.2 | 2e-10 | 25/43 (BT-474, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.710×** | -5.1 | 5e-05 | 23/48 (SNU-423, RPMI-7951, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.753×** | -4.3 | 0.003 | 21/48 (MIA PaCa-2, AN3 CA, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~4% of this change | **0.828×** | -4.0 | 0.007 | 24/48 (MIA PaCa-2, KATO III, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.771×** | -3.9 | 0.009 | 12/48 (SW480, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **0.793×** | -3.5 | 0.040 | 14/48 (NCI-H1792, SNU-423, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **0.806×** | -3.2 | 0.083 | 11/48 (HS-578T, CHP-212, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.810×** | -3.2 | 0.099 | 13/48 (MIA PaCa-2, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | 0.813× | -3.1 | 0.11 | 10/48 (HEC-1-A, A549, …) | top dose only |  |
| [[(S)-Crizotinib (drug)]] 0.5 µM |  | 0.815× | -3.1 | 0.11 | 11/48 (HepG2/C3A, LOX-IMVI, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 0.05 µM |  | 0.816× | -3.1 | 0.11 | 10/48 (SNU-423, AsPC-1, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 0.817× | -3.0 | 0.11 | 4/48 (HOP62, A498, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.819× | -3.0 | 0.11 | 13/48 (NCI-H460, SNU-423, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7829. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 30.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0843× (z -17.6) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 18.6 | 1 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +9.0) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 0.5 µM 0.176× (z -9.9) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 20.0 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.83× (z +11.2) | — |
| [[RPMI-7951 (line)]] | alt | 28.4 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.143× (z -11.2) ⚠ transcription drop; cell-cycle shift, explains ~36% of this change |
| [[SW480 (line)]] | alt | 27.6 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.50× (z +9.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.570× (z -8.5) ⚠ cell-cycle shift, explains ~4% of this change |
| [[A498 (line)]] | wt | 39.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.98× (z +8.7) | — |
| [[C32 (line)]] | wt | 31.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.245× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 35.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.330× (z -8.7) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 13.3 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -8.6) ⚠ cell-cycle shift, explains ~4% of this change |
| [[LS 180 (line)]] | wt | 27.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.119× (z -14.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 44.4 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.415× (z -10.6) ⚠ cell-cycle shift, explains ~4% of this change |
| [[Panc 03.27 (line)]] | alt | 23.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -10.9) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 22.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 33.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 26.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 40.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 26.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 17.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 29.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7829), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*74 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTX2]] | +0.71 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[RCHY1]] | +0.68 | +0.60 / +0.71 | both halves | 7e-06 |  |
| [[ALG9]] | +0.67 | +0.70 / +0.67 | both halves | 7e-06 |  |
| [[CEPT1]] | +0.65 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[SPATA7]] | +0.65 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[PEX3]] | +0.65 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[SPATA5L1]] | +0.64 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[LRRC40]] | +0.64 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[DUSP11]] | +0.63 | +0.65 / +0.63 | both halves | 7e-06 |  |
| [[NDUFV2]] | +0.63 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[TP53TG1]] | +0.63 | +0.38 / +0.64 | both halves | 6e-05 |  |
| [[LRIG2]] | +0.62 | +0.62 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*26 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KPNA4]] | -0.64 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[ZSWIM6]] | -0.57 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[CRK]] | -0.57 | -0.58 / -0.58 | both halves | 8e-06 |  |
| [[EIF3J]] | -0.55 | -0.58 / -0.52 | both halves | 1e-05 |  |
| [[ETF1]] | -0.55 | -0.45 / -0.52 | both halves | 3e-05 |  |
| [[GATAD2A]] | -0.55 | -0.43 / -0.58 | both halves | 3e-05 |  |
| [[SETX]] | -0.54 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[WNT2B]] | -0.53 | -0.53 / -0.51 | both halves | 1e-05 |  |
| [[LINC02803]] | -0.53 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[VCP]] | -0.53 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[TJP1]] | -0.52 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[RNF32-AS1]] | -0.52 | -0.48 / -0.55 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 065]] — BBSome-mediated cargo-targeting to cilium; 76 genes; this gene is in the **+** arm (projection on the module's main direction 0.691). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-4.8, -10.0); signed map (-30.1, -13.1). **Vector** length 78.1, 15.7% of its response variance represented; |z| ≥ 3 in 729 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.8 | +3.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +2.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.3 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.2 | +0.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~36% of this change | +3.2 | +3.2 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.9 | +3.3 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.7 | +0.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.6 | +3.2 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +2.5 | +1.4 |
| fall | [[Auranofin (drug)]] 5 µM |  | -4.1 | -5.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -2.3 | +0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | +0.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -0.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.2 | -0.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.9 | -1.4 |
|  | [[(S)-Crizotinib (drug)]] 0.5 µM |  | -1.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | mitochondrial ribosomal protein L39 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q21.3 — chr21:25,585,656-25,607,517 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RPML5, MRP-L5, MGC104174, PRED66, PRED22, C21orf92, L39mt, MSTP003 |
| Gene groups (HGNC) | Mitochondrial ribosomal proteins; Large subunit mitochondrial ribosomal proteins |
| Reactome | 6 pathways, smallest: Mitochondrial ribosome-associated quality control; Mitochondrial translation elongation; Mitochondrial translation initiation |
| Matched by | ensembl_id |

UniProt [Q9NYK5](https://www.uniprot.org/uniprotkb/Q9NYK5) carries no function annotation.

**Summary**, from NCBI Gene [54148](https://www.ncbi.nlm.nih.gov/gene/54148):

> Mammalian mitochondrial ribosomal proteins are encoded by nuclear genes and help in protein synthesis within the mitochondrion. Mitochondrial ribosomes (mitoribosomes) consist of a small 28S subunit and a large 39S subunit. They have an estimated 75% protein to rRNA composition compared to prokaryotic ribosomes, where this ratio is reversed. Another difference between mammalian mitoribosomes and prokaryotic ribosomes is that the latter contain a 5S rRNA. Among different species, the proteins …

**Accessions** — [HGNC:14027](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14027) · Entrez [54148](https://www.ncbi.nlm.nih.gov/gene/54148) · UniProt [Q9NYK5](https://www.uniprot.org/uniprotkb/Q9NYK5) · Ensembl [ENSG00000154719](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154719)

## Data

Gene col 7829: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7829); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7829, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7829]; `tensor/DDL_lfc|DDL_z.npy` [7829]; `embed/gene_vectors.npy` [7829]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7829 or target_col == 7829). Every well: [[MRPL39 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MRPL39.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
