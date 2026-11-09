---
symbol: "SAMM50"
type: "gene"
col: 1934
ensembl_id: "ENSG00000100347"
name: "SAMM50 sorting and assembly machinery component"
location: "22q13.31"
module: 171
arm: "+"
pooled_cpm: 20.99
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/171"]
generated_by: "tahoemap"
---

# SAMM50

*SAMM50 sorting and assembly machinery component* — 22q13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.72× (z +14.0, q 1e-41, up in 33 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 1.36× (z +8.0, q 1e-13, up in 23 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.711× (z -12.5, q 4e-33, down in 29 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RTCA]] (+0.71, fdr 7e-06), [[ANAPC10]] (+0.70, fdr 7e-06), [[GFM2]] (+0.67, fdr 7e-06); moves opposite to [[PKNOX1]] (-0.65, fdr 7e-06), [[PFN1]] (-0.59, fdr 1e-05), [[SKIL]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 171]] (Sealing of the nuclear envelope (NE) by ESCRT-III).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1934.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +14.0 | 1e-41 | 33/41 (MIA PaCa-2, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +11.5 | 3e-28 | 21/34 (A549, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | **1.27×** | +8.7 | 7e-16 | 25/48 (HS-578T, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +8.0 | 1e-13 | 23/47 (HOP62, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.36×** | +7.5 | 7e-12 | 26/48 (SNU-423, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.33×** | +6.9 | 5e-10 | 17/37 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.24×** | +5.6 | 2e-06 | 15/47 (HOP62, PANC-1, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +5.3 | 8e-06 | 11/48 (KATO III, HS-578T, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~16% of this change | **1.20×** | +4.7 | 1e-04 | 9/48 (COLO 205, BT-474, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~19% of this change | **1.21×** | +4.7 | 1e-04 | 16/45 (SW 900, J82, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.55×** | +4.6 | 3e-04 | 7/40 (HOP62, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~9% here); noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **1.44×** | +3.8 | 0.007 | 4/45 (PANC-1, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.44×** | +3.8 | 0.007 | 9/48 (SW480, C-33 A, …) | all doses, flat | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.21×** | +3.5 | 0.019 | 8/45 (NCI-H23, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.40×** | +3.5 | 0.020 | 9/45 (LS 180, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 0.5 µM |  | **1.20×** | +3.4 | 0.026 | 5/46 (SW1417, H4, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.13× | +3.1 | 0.056 | 0/47 | top dose only |  |
| [[Sonidegib (drug)]] 0.5 µM |  | 1.18× | +3.1 | 0.061 | 6/47 (LS 180, SW48, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 1.09× | +3.0 | 0.061 | 5/48 (AsPC-1, COLO 205, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | 1.18× | +3.0 | 0.061 | 6/47 (AN3 CA, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | 1.13× | +3.0 | 0.067 | 5/47 (HEC-1-A, LOX-IMVI, …) | all doses, flat |  |
| [[Flumatinib (mesylate) (drug)]] 5 µM |  | 1.12× | +2.9 | 0.089 | 3/47 (RKO, HepG2/C3A, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1934.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.711×** | -12.5 | 4e-33 | 29/47 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.622×** | -11.8 | 6e-30 | 32/48 (PANC-1, A498, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.744×** | -7.7 | 3e-12 | 21/47 (BT-474, HT-29, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.753×** | -7.4 | 2e-11 | 24/46 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.774×** | -6.6 | 4e-09 | 20/48 (NCI-H460, C32, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.861× | -5.5 | 4e-06 | 14/48 (SHP-77, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.813×** | -5.4 | 6e-06 | 18/47 (hTERT-HPNE, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.860× | -3.9 | 0.007 | 17/47 (HepG2/C3A, BT-474, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 0.867× | -3.7 | 0.013 | 17/48 (NCI-H460, KATO III, …) | two highest doses | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.868× | -3.7 | 0.013 | 16/47 (A498, NCI-H661, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.885× | -3.2 | 0.075 | 4/48 (SW480, HS-578T, …) | inconsistent across doses |  |
| [[Fusidic acid (drug)]] 0.5 µM |  | 0.886× | -3.1 | 0.083 | 6/48 (NCI-H1792, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.10 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1934. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 18.4 | 1 (1 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +8.5) ⚠ toxic; transcription drop | [[Harringtonine (drug)]] 0.5 µM 0.323× (z -10.8) |
| [[A-172 (line)]] | wt | 10.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -10.8) |
| [[A498 (line)]] | wt | 20.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -9.7) |
| [[A549 (line)]] | wt | 16.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.99× (z +9.3) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 12.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -10.2) |
| [[HepG2_C3A (line)]] | wt | 23.7 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.192× (z -9.4) |
| [[HS-578T (line)]] | alt | 32.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.468× (z -9.7) |
| [[J82 (line)]] | alt | 15.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.293× (z -12.1) |
| [[LS 180 (line)]] | wt | 32.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.357× (z -8.9) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 17.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.01× (z +9.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 22.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.376× (z -8.5) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 17.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.403× (z -9.5) |
| [[RKO (line)]] | wt | 19.5 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.262× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 22.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -10.5) |
| [[A-427 (line)]] | wt | 19.0 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 16.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 28.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1934), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RTCA]] | +0.71 | +0.76 / +0.67 | both halves | 7e-06 |  |
| [[ANAPC10]] | +0.70 | +0.68 / +0.61 | both halves | 7e-06 |  |
| [[GFM2]] | +0.67 | +0.69 / +0.64 | both halves | 7e-06 |  |
| [[VTI1B]] | +0.66 | +0.60 / +0.64 | both halves | 7e-06 | pathway: Protein localization |
| [[DFFB]] | +0.65 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[MIGA1]] | +0.65 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[ERCC3]] | +0.63 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[NAA20]] | +0.63 | +0.66 / +0.57 | both halves | 9e-06 |  |
| [[ATPAF1]] | +0.63 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[LONP2]] | +0.62 | +0.61 / +0.62 | both halves | 7e-06 | pathway: Protein localization |
| [[COPS7B]] | +0.62 | +0.58 / +0.59 | both halves | 8e-06 |  |
| [[JKAMP]] | +0.61 | +0.69 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKNOX1]] | -0.65 | -0.58 / -0.66 | both halves | 7e-06 |  |
| [[PFN1]] | -0.59 | -0.57 / -0.54 | both halves | 1e-05 |  |
| [[SKIL]] | -0.58 | -0.59 / -0.56 | both halves | 1e-05 |  |
| [[C11orf96]] | -0.56 | -0.52 / -0.54 | both halves | 1e-05 |  |
| [[MIDN]] | -0.54 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[DPH1-AS1]] | -0.54 | -0.61 / -0.41 | both halves | 4e-05 |  |
| [[ERF]] | -0.54 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[RNF19A]] | -0.53 | -0.47 / -0.49 | both halves | 2e-05 |  |
| [[HES1]] | -0.52 | -0.48 / -0.52 | both halves | 2e-05 |  |
| [[KCTD11]] | -0.52 | -0.55 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 171]] — Sealing of the nuclear envelope (NE) by ESCRT-III; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.733). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.41).
- **Nodal map** (x, y) = (-13.4, -13.4); signed map (-32.1, -27.0). **Vector** length 79.7, 14.6% of its response variance represented; |z| ≥ 3 in 778 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | +6.5 | +8.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +5.7 | +7.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.2 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.2 | +14.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.0 | +8.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.6 | +5.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.5 | +5.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.5 | +3.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +1.6 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.9 | -11.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.0 | -12.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.4 | -5.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.3 | -6.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.1 | -7.4 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.4 | -2.5 |
|  | [[Thymol (drug)]] 5 µM |  | -1.1 | -2.6 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.1 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | SAMM50 sorting and assembly machinery component |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.31 — chr22:43,955,442-44,010,531 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CGI-51, TRG-3, YNL026W, OMP85, TOB55, SAM50 |
| Gene groups (HGNC) | Mitochondrial sorting and assembly machinery complex |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 9 pathways, smallest: Cristae formation; Mitochondrial protein import; RAC2 GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y512](https://www.uniprot.org/uniprotkb/Q9Y512) (Sorting and assembly machinery component 50 homolog):

> Plays a crucial role in the maintenance of the structure of mitochondrial cristae and the proper assembly of the mitochondrial respiratory chain complexes. Required for the assembly of TOMM40 into the TOM complex.

**Summary**, from NCBI Gene [25813](https://www.ncbi.nlm.nih.gov/gene/25813):

> This gene encodes a component of the Sorting and Assembly Machinery (SAM) of the mitochondrial outer membrane. The Sam complex functions in the assembly of beta-barrel proteins into the outer mitochondrial membrane.[provided by RefSeq, Jun 2011]

**Accessions** — [HGNC:24276](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24276) · Entrez [25813](https://www.ncbi.nlm.nih.gov/gene/25813) · UniProt [Q9Y512](https://www.uniprot.org/uniprotkb/Q9Y512) · Ensembl [ENSG00000100347](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100347)

## Data

Gene col 1934: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1934); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1934, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1934]; `tensor/DDL_lfc|DDL_z.npy` [1934]; `embed/gene_vectors.npy` [1934]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1934 or target_col == 1934). Every well: [[SAMM50 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SAMM50.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
