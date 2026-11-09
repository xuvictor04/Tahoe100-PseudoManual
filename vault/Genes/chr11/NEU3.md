---
symbol: "NEU3"
type: "gene"
col: 8484
ensembl_id: "ENSG00000162139"
name: "neuraminidase 3"
location: "11q13.4"
module: 38
arm: "+"
pooled_cpm: 28.61
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 10
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# NEU3

*neuraminidase 3* — 11q13.4

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.56× (z +9.7, q 1e-19, up in 35 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.754× (z -4.4, q 0.006, down in 21 of 43 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 0.776× (z -3.8, q 0.040, down in 20 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H1573 0.100×, A-427 0.248×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.179×, LS 180 0.200×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RPMI-7951 0.200×, SHP-77 0.326×; ⚠ toxic; transcription drop); [[Doxycycline (monohydrate) (drug)]] 0.05 µM in 1 line (SW48 0.0617×); [[Belumosudil (drug)]] 5 µM in 1 line (J82 0.263×); [[Pimozide (drug)]] 0.05 µM in 1 line (CHP-212 0.0945×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EOGT]] (+0.66, fdr 1e-05), [[VWCE]] (+0.65, fdr 1e-05), [[ADCY10P1]] (+0.63, fdr 1e-05); moves opposite to [[PPP4R1]] (-0.52, fdr 2e-05), [[HSF2]] (-0.50, fdr 5e-05), [[CEP162]] (-0.49, fdr 1e-04).
> It is in [[Module 038]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 10 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8484.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +9.7 | 1e-19 | 35/48 (AsPC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.73×** | +8.1 | 1e-13 | 34/47 (AsPC-1, SW1417, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.65×** | +7.4 | 2e-11 | 27/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.58×** | +7.1 | 2e-10 | 30/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +6.8 | 9e-10 | 27/48 (HT-29, A-172, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.52×** | +6.5 | 7e-09 | 31/48 (SW480, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **1.47×** | +5.9 | 2e-07 | 28/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **2.01×** | +5.6 | 1e-06 | 29/47 (NCI-H1573, Panc 03.27, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.29×** | +5.5 | 2e-06 | 24/47 (NCI-H2347, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.42×** | +5.4 | 4e-06 | 27/47 (NCI-H460, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.37×** | +4.8 | 7e-05 | 26/48 (NCI-H2347, AsPC-1, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.36×** | +4.7 | 1e-04 | 26/48 (COLO 205, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.33×** | +4.4 | 4e-04 | 23/48 (LoVo, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.21×** | +4.1 | 0.001 | 20/48 (NCI-H2347, CFPAC-1, …) | top dose only | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.31×** | +4.1 | 0.001 | 22/47 (NCI-H1573, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.7 | 0.008 | 16/47 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.18× | +3.6 | 0.011 | 16/48 (A-172, A-427, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.51×** | +3.3 | 0.025 | 8/47 (MIA PaCa-2, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8484.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H1573 0.100×, A-427 0.248×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (LoVo 0.179×, LS 180 0.200×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (RPMI-7951 0.200×, SHP-77 0.326×; ⚠ toxic; transcription drop); [[Doxycycline (monohydrate) (drug)]] 0.05 µM in 1 line (SW48 0.0617×); [[Belumosudil (drug)]] 5 µM in 1 line (J82 0.263×); [[Pimozide (drug)]] 0.05 µM in 1 line (CHP-212 0.0945×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.754×** | -4.4 | 0.006 | 21/43 (RPMI-7951, SHP-77, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | **0.776×** | -3.8 | 0.040 | 20/48 (J82, NCI-H1573, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.869× | -3.1 | 0.35 | 15/48 (LoVo, LOX-IMVI, …) | top dose only |  |
| [[Radotinib (drug)]] 5 µM |  | 0.873× | -3.0 | 0.37 | 15/48 (RKO, SNU-423, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8484. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 10.9 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.30× (z +10.4) | — |
| [[LoVo (line)]] | wt | 22.3 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.92× (z +10.1) | [[Dinaciclib (drug)]] 5 µM 0.179× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 69.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 5.71× (z +12.4) | [[Dinaciclib (drug)]] 0.05 µM 0.100× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 16.0 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.36× (z +8.9) | — |
| [[A-427 (line)]] | wt | 38.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.248× (z -10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CHP-212 (line)]] | wt | 28.0 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0945× (z -9.2) |
| [[COLO 205 (line)]] | alt | 18.7 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.102× (z -8.6) |
| [[HT-29 (line)]] | alt | 22.1 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.54× (z +9.2) | — |
| [[J82 (line)]] | alt | 21.2 | 0 | 1 | — | [[Belumosudil (drug)]] 5 µM 0.263× (z -10.2) |
| [[LS 180 (line)]] | wt | 21.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.200× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 16.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.66× (z +11.5) | — |
| [[RPMI-7951 (line)]] | alt | 24.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.200× (z -10.0) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 47.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.326× (z -9.5) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 49.2 | 0 | 1 (1 ⚠) | — | [[Allantoin (drug)]] 0.05 µM 0.0894× (z -8.7) ⚠ transcription drop |
| [[SW48 (line)]] | wt | 18.0 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 0.05 µM 0.0617× (z -10.5) |
| [[A498 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 34.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 21.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 38.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 44.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 65.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 36.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 38.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8484), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EOGT]] | +0.66 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[VWCE]] | +0.65 | +0.53 / +0.68 | both halves | 1e-05 |  |
| [[ADCY10P1]] | +0.63 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[CCDC168]] | +0.63 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[RRH]] | +0.61 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[CCDC62]] | +0.60 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[KLRA1P]] | +0.60 | +0.46 / +0.59 | both halves | 2e-05 |  |
| [[IDI2-AS1]] | +0.59 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[TICAM2]] | +0.58 | +0.50 / +0.49 | both halves | 1e-05 |  |
| [[SURF4]] | +0.58 | +0.46 / +0.53 | both halves | 2e-05 |  |
| [[GABRR2]] | +0.58 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[TMED7-TICAM2]] | +0.57 | +0.47 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP4R1]] | -0.52 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[HSF2]] | -0.50 | -0.47 / -0.40 | both halves | 5e-05 |  |
| [[CEP162]] | -0.49 | -0.38 / -0.36 | both halves | 1e-04 |  |
| [[TTBK2]] | -0.49 | -0.38 / -0.30 | both halves | 2e-04 |  |
| [[PLAAT3]] | -0.49 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[OSBPL9]] | -0.48 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[NPEPPS]] | -0.48 | -0.49 / -0.46 | both halves | 3e-05 |  |
| [[KRAS]] | -0.48 | -0.44 / -0.43 | both halves | 4e-05 |  |
| [[TBC1D19]] | -0.47 | -0.40 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.591). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (30.4, -17.3); signed map (13.6, 8.6). **Vector** length 86.8, 18.4% of its response variance represented; |z| ≥ 3 in 935 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | +5.8 | +8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +6.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.3 | +6.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | +3.2 | +5.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.1 | +7.4 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +2.3 | +2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +2.7 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +1.9 | +2.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.8 | +2.1 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.0 | -2.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | -0.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.8 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | -1.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | +0.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.1 | -3.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.6 | +0.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.5 | -3.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | neuraminidase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q13.4 — chr11:74,988,279-75,018,893 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Neuraminidases |
| Reactome | 8 pathways, smallest: Glycosphingolipid catabolism; Sialic acid metabolism; Glycosphingolipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UQ49](https://www.uniprot.org/uniprotkb/Q9UQ49) (Sialidase-3):

> Exo-alpha-sialidase that catalyzes the hydrolytic cleavage of the terminal sialic acid (N-acetylneuraminic acid, Neu5Ac) of a glycan moiety in the catabolism of glycolipids, glycoproteins and oligosaccharides. Displays high catalytic efficiency for gangliosides including alpha-(2->3)-sialylated GD1a and GM3 and alpha-(2->8)-sialylated GD3. Plays a role in the regulation of transmembrane signaling through the modulation of ganglioside content of the lipid bilayer and by direct interaction with …

**Summary**, from NCBI Gene [10825](https://www.ncbi.nlm.nih.gov/gene/10825):

> This gene product belongs to a family of glycohydrolytic enzymes which remove sialic acid residues from glycoproteins and glycolipids. It is localized in the plasma membrane, and its activity is specific for gangliosides. It may play a role in modulating the ganglioside content of the lipid bilayer. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:7760](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7760) · Entrez [10825](https://www.ncbi.nlm.nih.gov/gene/10825) · UniProt [Q9UQ49](https://www.uniprot.org/uniprotkb/Q9UQ49) · Ensembl [ENSG00000162139](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000162139)

## Data

Gene col 8484: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8484); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8484, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8484]; `tensor/DDL_lfc|DDL_z.npy` [8484]; `embed/gene_vectors.npy` [8484]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8484 or target_col == 8484). Every well: [[NEU3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NEU3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
