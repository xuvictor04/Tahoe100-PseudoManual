---
symbol: "SEPTIN7P2"
type: "gene"
col: 13220
ensembl_id: "ENSG00000214765"
name: "septin 7 pseudogene 2"
location: "7p12.3"
module: 49
arm: "+"
pooled_cpm: 24.18
n_lines_expressing: 50
n_dd_up: 12
n_dd_down: 7
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# SEPTIN7P2

*septin 7 pseudogene 2* — 7p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.57× (z +7.7, q 7e-12, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.565× (z -9.4, q 3e-18, down in 24 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.755× (z -4.8, q 3e-04, down in 18 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TUBE1]] (+0.64, fdr 9e-06), [[SACM1L]] (+0.64, fdr 1e-05), [[RINT1]] (+0.62, fdr 1e-05); moves opposite to [[ZNF407]] (-0.62, fdr 1e-05), [[TRIP12]] (-0.53, fdr 3e-05), [[KRT8P12]] (-0.53, fdr 6e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13220.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.57×** | +7.7 | 7e-12 | 30/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.56×** | +7.6 | 7e-12 | 35/48 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.34×** | +7.1 | 2e-10 | 28/47 (SW480, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +6.6 | 6e-09 | 27/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +5.9 | 3e-07 | 25/47 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.40×** | +5.5 | 3e-06 | 20/43 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.35×** | +5.2 | 2e-05 | 16/48 (NCI-H2030, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~18% of this change | **1.32×** | +4.5 | 5e-04 | 16/48 (PANC-1, MIA PaCa-2, …) | all doses, flat |  |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.18× | +4.0 | 0.004 | 11/48 (H4, HT-29, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.25×** | +3.9 | 0.006 | 12/48 (LOX-IMVI, PANC-1, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.53×** | +3.8 | 0.007 | 4/48 (SW480, AsPC-1, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.23×** | +3.5 | 0.018 | 11/48 (MIA PaCa-2, J82, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.055 | 6/48 (AsPC-1, LOX-IMVI, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13220.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.565×** | -9.4 | 3e-18 | 24/34 (A498, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.615×** | -8.3 | 2e-14 | 26/39 (A498, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.755×** | -4.8 | 3e-04 | 18/48 (A498, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.825×** | -4.6 | 5e-04 | 21/47 (A498, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.773×** | -4.1 | 0.005 | 19/37 (A498, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.795×** | -3.9 | 0.008 | 11/48 (Panc 03.27, HT-29, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 0.862× | -3.6 | 0.027 | 12/48 (Panc 03.27, A498, …) | rises with dose |  |
| [[Megestrol (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.825×** | -3.3 | 0.072 | 8/48 (Hs 766T, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13220. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 62.5 | 0 | 9 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.148× (z -19.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.225× (z -14.9) |
| [[SW480 (line)]] | alt | 50.2 | 5 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.02× (z +11.3) | [[Dinaciclib (drug)]] 0.5 µM 0.389× (z -10.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 30.2 | 0 | 3 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.403× (z -10.3) |
| [[AsPC-1 (line)]] | alt | 23.1 | 0 | 3 (3 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0497× (z -20.9) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 34.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.106× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~15% of this change |
| [[COLO 205 (line)]] | alt | 11.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -8.7) |
| [[Hs 766T (line)]] | wt | 21.2 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0678× (z -16.6) ⚠ transcription drop; cell-cycle shift, would explain all of this change |
| [[KATO III (line)]] | alt | 25.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.131× (z -14.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 22.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.240× (z -10.5) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 35.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +10.6) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.361× (z -9.5) |
| [[SHP-77 (line)]] | alt | 31.5 | 0 | 2 (2 ⚠) | — | [[AZD2858 (drug)]] 0.5 µM 0.102× (z -11.8) ⚠ toxic |
| [[A-427 (line)]] | wt | 16.2 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.41× (z +10.6) | — |
| [[C32 (line)]] | wt | 25.5 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.65× (z +9.3) | — |
| [[HCT15 (line)]] | alt | 12.3 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.116× (z -9.3) |
| [[HepG2_C3A (line)]] | wt | 13.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.119× (z -9.3) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 54.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.505× (z -8.5) |
| [[J82 (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -9.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 22.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.264× (z -8.8) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 14.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.43× (z +10.3) | — |
| [[NCI-H2030 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.104× (z -14.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 19.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.157× (z -11.7) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 28.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.311× (z -9.2) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 25.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 20.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 44.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 28.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13220), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBE1]] | +0.64 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[SACM1L]] | +0.64 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[RINT1]] | +0.62 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[CCZ1]] | +0.61 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[OXNAD1]] | +0.61 | +0.52 / +0.61 | both halves | 1e-05 |  |
| [[GPR180]] | +0.61 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[ANAPC5]] | +0.59 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[SLC30A5]] | +0.59 | +0.55 / +0.58 | both halves | 1e-05 |  |
| [[PRMT9]] | +0.59 | +0.55 / +0.52 | both halves | 1e-05 |  |
| [[CNEP1R1]] | +0.59 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[PARP2]] | +0.59 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[SEPTIN7P14]] | +0.58 | +0.55 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF407]] | -0.62 | -0.58 / -0.50 | both halves | 1e-05 |  |
| [[TRIP12]] | -0.53 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[KRT8P12]] | -0.53 | -0.38 / -0.54 | both halves | 6e-05 |  |
| [[C6orf120]] | -0.52 | -0.34 / -0.42 | both halves | 1e-04 |  |
| [[LINC01088]] | -0.52 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[RFX3]] | -0.51 | -0.35 / -0.47 | both halves | 1e-04 |  |
| [[ASXL2]] | -0.51 | -0.48 / -0.38 | both halves | 7e-05 |  |
| [[PPP1R1C]] | -0.51 | -0.30 / -0.57 | both halves | 2e-04 |  |
| [[MYOSLID]] | -0.50 | -0.34 / -0.48 | both halves | 1e-04 |  |
| [[RNF32]] | -0.50 | -0.37 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.621). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.5, -14.1); signed map (-36.9, -14.8). **Vector** length 81.1, 15.3% of its response variance represented; |z| ≥ 3 in 907 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Radotinib (drug)]] 5 µM |  | +3.0 | +2.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.9 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.3 | +5.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +1.8 | +6.6 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +1.7 | +2.0 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +1.6 | +0.7 |
|  | [[Flumatinib (mesylate) (drug)]] 5 µM |  | +1.6 | +1.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -2.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.3 | -9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.0 | -8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.6 | -4.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.1 | -2.7 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.1 | -2.5 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.0 | -2.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.7 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | septin 7 pseudogene 2 |
| Locus type | pseudogene |
| Location | 7p12.3 — chr7:45,736,787-45,765,812 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | DKFZp313J1114; previously SEPT7B, SEPT13, SEPT7P2 |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [641977](https://www.ncbi.nlm.nih.gov/gene/641977):

> Septins, such as SEPT13, are conserved GTP-binding proteins that function as dynamic, regulatable scaffolds for the recruitment of other proteins. They are involved in membrane dynamics, vesicle trafficking, apoptosis, and cytoskeleton remodeling, as well as infection, neurodegeneration, and neoplasia (Hall et al., 2005 [PubMed 15915442]).[supplied by OMIM, Jul 2008]

**Accessions** — [HGNC:32339](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:32339) · Entrez [641977](https://www.ncbi.nlm.nih.gov/gene/641977) · Ensembl [ENSG00000214765](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214765)

## Data

Gene col 13220: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13220); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13220, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13220]; `tensor/DDL_lfc|DDL_z.npy` [13220]; `embed/gene_vectors.npy` [13220]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13220 or target_col == 13220). Every well: [[SEPTIN7P2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SEPTIN7P2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
