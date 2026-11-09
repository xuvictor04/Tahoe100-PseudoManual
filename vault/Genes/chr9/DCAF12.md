---
symbol: "DCAF12"
type: "gene"
col: 12718
ensembl_id: "ENSG00000198876"
name: "DDB1 and CUL4 associated factor 12"
location: "9p13.3"
module: 171
arm: "+"
pooled_cpm: 26.26
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/171"]
generated_by: "tahoemap"
---

# DCAF12

*DDB1 and CUL4 associated factor 12* — 9p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.95× (z +13.7, q 3e-40, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.797× (z -7.8, q 3e-12, down in 23 of 47 measured lines) ⚠ cell-cycle shift, explains ~13% of this change. The strongest without an alert is [[c-Kit-IN-1 (drug)]] 5 µM: 0.708× (z -4.4, q 0.002, down in 14 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SNX4]] (+0.57, fdr 1e-05), [[MBD2]] (+0.56, fdr 1e-05), [[ZW10]] (+0.56, fdr 3e-05); moves opposite to [[PFN1]] (-0.59, fdr 3e-05), [[DPH1-AS1]] (-0.53, fdr 3e-05), [[LINC01473]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 171]] (Sealing of the nuclear envelope (NE) by ESCRT-III).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12718.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.95×** | +13.7 | 3e-40 | 37/48 (SW480, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.56×** | +11.9 | 2e-30 | 32/45 (SW480, RKO, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.45×** | +9.0 | 6e-17 | 28/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.40×** | +8.1 | 6e-14 | 23/42 (SW480, A-172, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +7.9 | 3e-13 | 23/47 (A-172, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.34×** | +7.0 | 2e-10 | 22/48 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.34×** | +6.9 | 6e-10 | 19/46 (SK-MEL-2, J82, …) | top dose only | cell-cycle shift (explains ~2% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +6.6 | 4e-09 | 22/46 (A549, SW 900, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~14% of this change | **1.29×** | +6.1 | 5e-08 | 21/48 (PANC-1, A-172, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.28×** | +6.0 | 1e-07 | 17/47 (PANC-1, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.26×** | +5.2 | 9e-06 | 16/48 (PANC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.24×** | +5.2 | 1e-05 | 17/46 (AsPC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.16× | +5.0 | 3e-05 | 19/48 (NCI-H1573, SNU-423, …) | rises with dose | low cells (technical?) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.21×** | +4.7 | 1e-04 | 14/45 (RPMI-7951, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.16× | +3.6 | 0.014 | 11/47 (SW480, MIA PaCa-2, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM |  | **1.32×** | +3.5 | 0.017 | 7/45 (A-427, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.16× | +3.4 | 0.020 | 12/47 (LOX-IMVI, BT-474, …) | inconsistent across doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.14× | +3.2 | 0.040 | 5/46 (COLO 205, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12718.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **0.797×** | -7.8 | 3e-12 | 23/47 (NCI-H2347, NCI-H1792, …) | top dose only | composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.827×** | -4.6 | 0.001 | 19/47 (NCI-H2347, LoVo, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.708×** | -4.4 | 0.002 | 14/46 (NCI-H2347, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[TAK-733 (drug)]] 5 µM |  | **0.722×** | -4.1 | 0.005 | 11/46 (NCI-H2347, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.724×** | -4.1 | 0.005 | 9/48 (NCI-H2347, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[EX229 (drug)]] 5 µM |  | **0.727×** | -4.1 | 0.005 | 10/47 (NCI-H2347, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | 0.848× | -4.0 | 0.005 | 16/46 (NCI-H2347, SW48, …) | top dose only |  |
| [[Allantoin (drug)]] 0.5 µM |  | 0.855× | -3.8 | 0.009 | 5/47 (NCI-H460, SNU-1, …) | inconsistent across doses | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.951× | -3.8 | 0.009 | 0/48 | inconsistent across doses |  |
| [[EX229 (drug)]] 0.05 µM |  | 0.865× | -3.3 | 0.048 | 10/48 (C-33 A, SHP-77, …) | all doses, flat |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.878× | -3.2 | 0.077 | 9/47 (NCI-H2347, KATO III, …) | inconsistent across doses |  |
| [[Isocorydine (drug)]] 0.5 µM |  | 0.882× | -3.1 | 0.11 | 9/46 (AsPC-1, Panc 03.27, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12718. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 60.0 | 0 | 10 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -22.8) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.491× (z -9.9) |
| [[SW480 (line)]] | alt | 34.4 | 4 (2 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 5.49× (z +11.9) | — |
| [[AsPC-1 (line)]] | alt | 23.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[COLO 205 (line)]] | alt | 37.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.382× (z -9.8) ⚠ cell-cycle shift, explains ~13% of this change · without an alert: [[venetoclax (drug)]] 5 µM 0.0918× (z -9.0) |
| [[LoVo (line)]] | wt | 31.1 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.43× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.355× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change |
| [[A-172 (line)]] | wt | 20.5 | 1 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.02× (z +8.5) ⚠ cell-cycle shift, explains ~25% of this change | — |
| [[A-427 (line)]] | wt | 16.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.214× (z -10.9) ⚠ toxic |
| [[CHP-212 (line)]] | wt | 33.8 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.0932× (z -8.8) ⚠ cell-cycle shift, explains ~17% of this change |
| [[HT-29 (line)]] | alt | 34.6 | 0 | 1 (1 ⚠) | — | [[Lonafarnib (drug)]] 5 µM 0.149× (z -9.1) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.376× (z -9.4) ⚠ cell-cycle shift, explains ~13% of this change |
| [[NCI-H1792 (line)]] | alt | 14.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -13.0) ⚠ cell-cycle shift, explains ~13% of this change |
| [[NCI-H460 (line)]] | wt | 20.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -9.2) ⚠ cell-cycle shift, explains ~13% of this change |
| [[PANC-1 (line)]] | alt | 25.1 | 1 | 0 | [[Ixazomib citrate (drug)]] 5 µM 2.18× (z +8.9) | — |
| [[SW48 (line)]] | wt | 31.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.177× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~19% of this change |
| [[A498 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 39.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 25.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 33.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 41.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 29.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 32.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 28.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12718), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNX4]] | +0.57 | +0.59 / +0.49 | both halves | 1e-05 |  |
| [[MBD2]] | +0.56 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[ZW10]] | +0.56 | +0.61 / +0.45 | both halves | 3e-05 |  |
| [[WIPI2]] | +0.55 | +0.56 / +0.53 | both halves | 1e-05 | same gene group |
| [[VTI1B]] | +0.55 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[CDC123]] | +0.54 | +0.65 / +0.36 | both halves | 1e-04 |  |
| [[BICRA]] | +0.54 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[SAP30L]] | +0.53 | +0.53 / +0.46 | both halves | 2e-05 |  |
| [[TSFM]] | +0.53 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[COPS7B]] | +0.52 | +0.57 / +0.43 | both halves | 3e-05 |  |
| [[TMEM127]] | +0.52 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[SAMM50]] | +0.52 | +0.62 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PFN1]] | -0.59 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[DPH1-AS1]] | -0.53 | -0.54 / -0.45 | both halves | 3e-05 |  |
| [[LINC01473]] | -0.50 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[C16orf46]] | -0.46 | -0.56 / -0.36 | both halves | 1e-04 |  |
| [[ERCC1]] | -0.45 | -0.50 / -0.38 | both halves | 6e-05 |  |
| [[ZNF280C]] | -0.45 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[ERCC6L2]] | -0.44 | -0.44 / -0.43 | both halves | 3e-05 |  |
| [[NOTCH2NLB]] | -0.44 | -0.44 / -0.37 | both halves | 9e-05 |  |
| [[NBPF10]] | -0.44 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[MTR]] | -0.44 | -0.52 / -0.35 | both halves | 1e-04 |  |
| [[TUBB4B]] | -0.43 | -0.55 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 171]] — Sealing of the nuclear envelope (NE) by ESCRT-III; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.664). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41).
- **Nodal map** (x, y) = (-10.0, -11.7); signed map (-34.5, -17.4). **Vector** length 83.0, 15.0% of its response variance represented; |z| ≥ 3 in 865 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[PH-797804 (drug)]] 5 µM |  | +6.2 | +11.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | +5.7 | +13.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +3.6 | +9.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +3.0 | +5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.8 | +6.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +3.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.2 | +3.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.0 | +1.4 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -7.3 | -7.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -3.6 | -0.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.7 | -4.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.7 | -4.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | -2.6 | -4.0 |
|  | [[EX229 (drug)]] 5 µM |  | -2.5 | -4.1 |
|  | [[TAK-733 (drug)]] 5 µM |  | -2.4 | -4.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -2.2 | -4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.1 | +0.6 |

## What is on record

|  |  |
|---|---|
| Name | DDB1 and CUL4 associated factor 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p13.3 — chr9:34,086,387-34,127,399 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DKFZP434O125, MGC1058, CT102, TCC52; previously KIAA1892, WDR40A |
| Gene groups (HGNC) | WD repeat domain containing; DDB1 and CUL4 associated factors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5T6F0](https://www.uniprot.org/uniprotkb/Q5T6F0) (DDB1- and CUL4-associated factor 12):

> Substrate-recognition component of a DCX (DDB1-CUL4-X-box) E3 ubiquitin-protein ligase complex of the DesCEND (destruction via C-end degrons) pathway, which recognizes a C-degron located at the extreme C terminus of target proteins, leading to their ubiquitination and degradation. The C-degron recognized by the DesCEND pathway is usually a motif of less than ten residues and can be present in full-length proteins, truncated proteins or proteolytically cleaved forms. The DCX(DCAF12) complex …

**Summary**, from NCBI Gene [25853](https://www.ncbi.nlm.nih.gov/gene/25853):

> This gene encodes a WD repeat-containing protein that interacts with the COP9 signalosome, a macromolecular complex that interacts with cullin-RING E3 ligases and regulates their activity by hydrolyzing cullin-Nedd8 conjugates. [provided by RefSeq, Jul 2009]

**Accessions** — [HGNC:19911](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19911) · Entrez [25853](https://www.ncbi.nlm.nih.gov/gene/25853) · UniProt [Q5T6F0](https://www.uniprot.org/uniprotkb/Q5T6F0) · Ensembl [ENSG00000198876](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198876)

## Data

Gene col 12718: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12718); `tables/drug_effects.parquet` (33 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12718, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12718]; `tensor/DDL_lfc|DDL_z.npy` [12718]; `embed/gene_vectors.npy` [12718]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12718 or target_col == 12718). Every well: [[DCAF12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCAF12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
