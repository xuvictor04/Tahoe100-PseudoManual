---
symbol: "ZNF3"
type: "gene"
col: 9325
ensembl_id: "ENSG00000166526"
name: "zinc finger protein 3"
location: "7q22.1"
module: 149
arm: "+"
pooled_cpm: 25.51
n_lines_expressing: 50
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/149"]
generated_by: "tahoemap"
---

# ZNF3

*zinc finger protein 3* — 7q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (1 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.90× (z +13.5, q 6e-39, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.599× (z -9.4, q 3e-18, down in 22 of 33 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.791× (z -4.5, q 8e-04, down in 18 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 0.193×, A-172 0.170×, LS 180 0.217×, Panc 03.27 0.230×, …; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (NCI-H23 0.0833×, HepG2/C3A 0.101×, A498 0.375×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (AN3 CA 0.101×, SK-MEL-2 0.184×, NCI-H460 0.355×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 0.378×); [[Auranofin (drug)]] 5 µM in 1 line (C32 0.265×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALKBH1]] (+0.82, fdr 7e-06), [[TRIM4]] (+0.75, fdr 7e-06), [[ZNF7]] (+0.75, fdr 7e-06); moves opposite to [[MMGT1]] (-0.62, fdr 7e-06).
> It is in [[Module 149]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9325.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.90×** | +13.5 | 6e-39 | 42/48 (LoVo, PANC-1, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **3.82×** | +13.3 | 5e-38 | 40/47 (PANC-1, RKO, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.50×** | +10.6 | 6e-24 | 33/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +9.0 | 4e-17 | 35/48 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.55×** | +8.0 | 1e-13 | 29/46 (NCI-H1573, KATO III, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +7.2 | 4e-11 | 30/48 (PANC-1, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +5.6 | 1e-06 | 23/48 (HT-29, NCI-H23, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.33×** | +5.1 | 2e-05 | 23/48 (PANC-1, A549, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.37×** | +4.3 | 0.001 | 18/46 (hTERT-HPNE, SNU-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.23×** | +3.9 | 0.005 | 10/47 (AN3 CA, HS-578T, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.005 | 18/48 (NCI-H2347, KATO III, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.22×** | +3.8 | 0.006 | 15/47 (CFPAC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.32×** | +3.8 | 0.007 | 13/48 (PANC-1, LOX-IMVI, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.21×** | +3.6 | 0.012 | 17/48 (NCI-H1573, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.28×** | +3.3 | 0.036 | 6/48 (PANC-1, HT-29, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Thymol (drug)]] 0.5 µM |  | 1.19× | +3.2 | 0.045 | 9/45 (SW480, NCI-H23, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9325.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 6 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 5 lines (PANC-1 0.193×, A-172 0.170×, LS 180 0.217×, Panc 03.27 0.230×, …; ⚠ toxic; transcription drop); [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (NCI-H23 0.0833×, HepG2/C3A 0.101×, A498 0.375×; ⚠ toxic); [[Dinaciclib (drug)]] 0.5 µM in 3 lines (AN3 CA 0.101×, SK-MEL-2 0.184×, NCI-H460 0.355×; ⚠ toxic; transcription drop); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (NCI-H460 0.378×); [[Auranofin (drug)]] 5 µM in 1 line (C32 0.265×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.599×** | -9.4 | 3e-18 | 22/33 (PANC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.605×** | -9.2 | 9e-18 | 37/47 (NCI-H23, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.691×** | -7.0 | 3e-10 | 24/41 (AN3 CA, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.718×** | -5.9 | 7e-07 | 21/40 (NCI-H1573, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.791×** | -4.5 | 8e-04 | 18/48 (NCI-H460, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~3% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.800×** | -4.3 | 0.002 | 19/48 (NCI-H460, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Gefitinib (drug)]] 5 µM |  | 0.852× | -3.1 | 0.18 | 4/48 (NCI-H460, LOX-IMVI, …) | top dose only |  |
| [[Irinotecan (hydrochloride) (drug)]] 0.5 µM |  | 0.855× | -3.0 | 0.19 | 4/48 (HS-578T, C32, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9325. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.0 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.325× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~9% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.378× (z -10.2) |
| [[PANC-1 (line)]] | alt | 24.3 | 4 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.28× (z +18.7) | [[Dinaciclib (drug)]] 5 µM 0.193× (z -18.2) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 37.0 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -9.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.265× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 19.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.18× (z +12.0) | [[Dinaciclib (drug)]] 0.05 µM 0.108× (z -15.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 26.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.170× (z -14.0) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 37.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.90× (z +10.1) | [[Niclosamide (olamine) (drug)]] 5 µM 0.375× (z -10.9) ⚠ toxic |
| [[A549 (line)]] | wt | 20.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -10.9) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 24.0 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.48× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.270× (z -10.7) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 36.1 | 1 | 1 (1 ⚠) | [[PH-797804 (drug)]] 5 µM 7.02× (z +8.7) | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.294× (z -10.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[AN3 CA (line)]] | alt | 57.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.101× (z -12.6) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 24.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.146× (z -9.1) ⚠ toxic |
| [[HepG2_C3A (line)]] | wt | 20.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.101× (z -11.6) ⚠ toxic |
| [[J82 (line)]] | alt | 21.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.266× (z -9.4) ⚠ toxic |
| [[KATO III (line)]] | alt | 33.0 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.56× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 25.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.217× (z -11.5) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 17.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.250× (z -9.0) ⚠ toxic |
| [[NCI-H23 (line)]] | alt | 26.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0833× (z -18.3) ⚠ toxic |
| [[Panc 03.27 (line)]] | alt | 30.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.230× (z -11.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 30.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.184× (z -12.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 16.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 25.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 25.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 36.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9325), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALKBH1]] | +0.82 | +0.83 / +0.76 | both halves | 7e-06 |  |
| [[TRIM4]] | +0.75 | +0.79 / +0.67 | both halves | 7e-06 |  |
| [[ZNF7]] | +0.75 | +0.73 / +0.68 | both halves | 7e-06 | same gene group |
| [[RPP14]] | +0.73 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[ZNF557]] | +0.73 | +0.79 / +0.65 | both halves | 7e-06 | same gene group |
| [[ZNF16]] | +0.73 | +0.64 / +0.72 | both halves | 7e-06 | same gene group |
| [[TTF1]] | +0.73 | +0.81 / +0.63 | both halves | 7e-06 |  |
| [[CCDC174]] | +0.71 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[MRM2]] | +0.71 | +0.71 / +0.68 | both halves | 7e-06 |  |
| [[UBE2J2]] | +0.71 | +0.73 / +0.69 | both halves | 7e-06 |  |
| [[HMGXB4]] | +0.70 | +0.74 / +0.66 | both halves | 7e-06 |  |
| [[ZNF579]] | +0.70 | +0.68 / +0.67 | both halves | 7e-06 | same gene group |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MMGT1]] | -0.62 | -0.59 / -0.61 | both halves | 7e-06 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 149]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.843). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-42.1, 4.3); signed map (-4.9, -14.0). **Vector** length 105, 24.0% of its response variance represented; |z| ≥ 3 in 848 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +10.4 | +13.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +8.1 | +13.3 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.8 | +10.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +9.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.8 | +7.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.7 | +4.3 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | +2.5 | +3.3 |
|  | [[TAK-901 (drug)]] 0.5 µM |  | +2.4 | +3.8 |
|  | [[PH-797804 (drug)]] 0.5 µM |  | +2.3 | +2.6 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.5 | -9.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.0 | -9.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -5.0 | -7.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -4.0 | -5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -2.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.3 | -3.1 |
|  | [[Irinotecan (drug)]] 0.5 µM |  | -2.0 | -2.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | -1.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q22.1 — chr7:100,064,033-100,082,548 (-) |
| Ensembl biotype | protein_coding |
| Also known as | A8-51, KOX25, PP838, FLJ20216, HF.12, Zfp113 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P17036](https://www.uniprot.org/uniprotkb/P17036) (Zinc finger protein 3):

> Involved in cell differentiation and/or proliferation.

**Summary**, from NCBI Gene [7551](https://www.ncbi.nlm.nih.gov/gene/7551):

> Enables identical protein binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:13089](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13089) · Entrez [7551](https://www.ncbi.nlm.nih.gov/gene/7551) · UniProt [P17036](https://www.uniprot.org/uniprotkb/P17036) · Ensembl [ENSG00000166526](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166526)

## Data

Gene col 9325: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9325); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9325, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9325]; `tensor/DDL_lfc|DDL_z.npy` [9325]; `embed/gene_vectors.npy` [9325]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9325 or target_col == 9325). Every well: [[ZNF3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
