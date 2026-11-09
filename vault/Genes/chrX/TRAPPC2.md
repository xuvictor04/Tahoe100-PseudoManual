---
symbol: "TRAPPC2"
type: "gene"
col: 12212
ensembl_id: "ENSG00000196459"
name: "trafficking protein particle complex subunit 2"
location: "Xp22.2"
module: 183
arm: "+"
pooled_cpm: 15.49
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 5
n_dd_up_clean: 19
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/183"]
generated_by: "tahoemap"
---

# TRAPPC2

*trafficking protein particle complex subunit 2* — Xp22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (5 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 1.56× (z +9.6, q 3e-19, up in 33 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.722× (z -7.1, q 9e-10, down in 21 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JKAMP]] (+0.68, fdr 7e-06), [[USP30]] (+0.68, fdr 7e-06), [[RTCA]] (+0.67, fdr 1e-05); moves opposite to [[DPH1-AS1]] (-0.58, fdr 3e-05), [[DGKH]] (-0.57, fdr 1e-05), [[ITPRIPL2]] (-0.57, fdr 3e-05).
> It is in [[Module 183]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12212.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.56×** | +9.6 | 3e-19 | 33/47 (NCI-H1792, BT-474, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.60×** | +9.6 | 3e-19 | 29/47 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.53×** | +9.2 | 5e-18 | 33/47 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +8.2 | 5e-14 | 22/48 (NCI-H2347, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.44×** | +7.9 | 3e-13 | 23/47 (MIA PaCa-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.42×** | +7.5 | 4e-12 | 22/48 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +7.5 | 4e-12 | 25/47 (HEC-1-A, COLO 205, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.40×** | +7.3 | 2e-11 | 26/46 (Hs 766T, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +7.1 | 7e-11 | 12/30 (KATO III, A549, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.33×** | +6.2 | 3e-08 | 16/48 (MIA PaCa-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.33×** | +6.1 | 5e-08 | 19/42 (HS-578T, A-172, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.31×** | +5.8 | 4e-07 | 17/46 (A-427, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Brivudine (drug)]] 5 µM |  | **1.55×** | +5.0 | 3e-05 | 3/48 (NCI-H460, SW1417, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.7 | 1e-04 | 11/31 (SW480, KATO III, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | 1.16× | +4.6 | 2e-04 | 14/48 (AsPC-1, A498, …) | top dose only | low cells (technical?) |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.34×** | +4.6 | 2e-04 | 7/44 (SW480, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.23×** | +4.6 | 2e-04 | 7/48 (Panc 03.27, LoVo, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.25×** | +3.5 | 0.013 | 8/45 (NCI-H1573, SW1417, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.16× | +3.2 | 0.033 | 3/47 (LS 180, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12212.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.722×** | -7.1 | 9e-10 | 21/48 (NCI-H460, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.725×** | -6.7 | 6e-09 | 20/43 (NCI-H460, SHP-77, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.776×** | -5.5 | 7e-06 | 16/46 (BT-474, SW1417, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | **0.819×** | -4.3 | 0.002 | 13/46 (NCI-H460, BT-474, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.709×** | -3.9 | 0.010 | 10/45 (C32, NCI-H2347, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~10% of this change | 0.837× | -3.9 | 0.010 | 12/46 (J82, NCI-H2347, …) | two highest doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 0.848× | -3.6 | 0.027 | 11/47 (AN3 CA, NCI-H460, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~14% of this change | 0.858× | -3.3 | 0.058 | 9/48 (NCI-H460, A549, …) | all doses, stronger at high dose |  |
| [[Gallic acid (hydrate) (drug)]] 5 µM |  | 0.898× | -3.3 | 0.058 | 10/48 (HCT15, Hs 766T, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12212. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AN3 CA (line)]] | alt | 27.7 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.5 µM 0.0782× (z -9.7) |
| [[COLO 205 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.159× (z -13.2) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.338× (z -10.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.137× (z -11.3) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 14.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.185× (z -10.6) ⚠ toxic; cell-cycle shift, explains ~45% of this change |
| [[NCI-H460 (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.489× (z -9.4) ⚠ cell-cycle shift, would explain all of this change |
| [[SHP-77 (line)]] | alt | 13.5 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.202× (z -8.8) |
| [[SNU-1 (line)]] | wt | 11.8 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0778× (z -9.3) |
| [[SW 900 (line)]] | alt | 9.86 | 0 | 1 | — | [[Cepharanthine (drug)]] 5 µM 0.260× (z -9.2) |
| [[A-172 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.69 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.66 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.20 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.47 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.86 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 20.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 27.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12212), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JKAMP]] | +0.68 | +0.68 / +0.60 | both halves | 7e-06 |  |
| [[USP30]] | +0.68 | +0.63 / +0.60 | both halves | 7e-06 |  |
| [[RTCA]] | +0.67 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[GNPDA2]] | +0.65 | +0.73 / +0.53 | both halves | 1e-05 |  |
| [[UNC45A]] | +0.62 | +0.46 / +0.67 | both halves | 3e-05 |  |
| [[BCL9]] | +0.62 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[MINDY3]] | +0.61 | +0.58 / +0.57 | both halves | 1e-05 |  |
| [[OSBPL7]] | +0.61 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[STARD3NL]] | +0.61 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[FBXO44]] | +0.60 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[MKRN2]] | +0.60 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[CGRRF1]] | +0.60 | +0.57 / +0.58 | both halves | 9e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DPH1-AS1]] | -0.58 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[DGKH]] | -0.57 | -0.49 / -0.54 | both halves | 1e-05 |  |
| [[ITPRIPL2]] | -0.57 | -0.45 / -0.56 | both halves | 3e-05 |  |
| [[PKNOX1]] | -0.55 | -0.52 / -0.43 | both halves | 3e-05 |  |
| [[ASXL2]] | -0.53 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[HIVEP1]] | -0.53 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[PPIEL-1]] | -0.53 | -0.45 / -0.46 | both halves | 3e-05 |  |
| [[BAZ1A]] | -0.53 | -0.39 / -0.51 | both halves | 6e-05 |  |
| [[HIVEP2]] | -0.51 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[SEMA4A]] | -0.51 | -0.44 / -0.48 | both halves | 3e-05 |  |
| [[WARS2-AS1]] | -0.50 | -0.35 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 183]]; 21 genes; every member is in the + arm (projection on the module's main direction 0.753). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.3, -9.8); signed map (-30.8, -9.5). **Vector** length 61.6, 8.88% of its response variance represented; |z| ≥ 3 in 780 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +5.0 | +9.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.7 | +7.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.5 | +9.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.4 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.3 | +7.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +8.2 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.9 | +4.6 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.9 | +2.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.7 | +2.5 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | -2.9 | -2.0 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.3 | -5.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~7% of this change | -2.2 | -4.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.2 | -6.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +2.2 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -3.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -2.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.4 | -0.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -1.0 |
|  | [[Acetohexamide (drug)]] 5 µM |  | -1.1 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | trafficking protein particle complex subunit 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp22.2 — chrX:13,712,244-13,734,635 (-) |
| Ensembl biotype | protein_coding |
| Also known as | TRS20, SEDT, MIP-2A, ZNF547L, hYP38334; previously SEDL |
| Gene groups (HGNC) | Trafficking protein particle complex subunits |
| Reactome | 8 pathways, smallest: COPII-mediated vesicle transport; RAB GEFs exchange GTP for GDP on RABs; Rab regulation of trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [P0DI81](https://www.uniprot.org/uniprotkb/P0DI81) (Trafficking protein particle complex subunit 2):

> Prevents transcriptional repression and induction of cell death by ENO1 (By similarity). May play a role in vesicular transport from endoplasmic reticulum to Golgi.

**Summary**, from NCBI Gene [6399](https://www.ncbi.nlm.nih.gov/gene/6399):

> The protein encoded by this gene is thought to be part of a large multi-subunit complex involved in the targeting and fusion of endoplasmic reticulum-to-Golgi transport vesicles with their acceptor compartment. In addition, the encoded protein can bind c-myc promoter-binding protein 1 and block its transcriptional repression capability. Mutations in this gene are a cause of spondyloepiphyseal dysplasia tarda (SEDT). A processed pseudogene of this gene is located on chromosome 19, and other …

**Accessions** — [HGNC:23068](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23068) · Entrez [6399](https://www.ncbi.nlm.nih.gov/gene/6399) · UniProt [P0DI81](https://www.uniprot.org/uniprotkb/P0DI81) · Ensembl [ENSG00000196459](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196459)

## Data

Gene col 12212: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12212); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12212, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12212]; `tensor/DDL_lfc|DDL_z.npy` [12212]; `embed/gene_vectors.npy` [12212]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12212 or target_col == 12212). Every well: [[TRAPPC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TRAPPC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
