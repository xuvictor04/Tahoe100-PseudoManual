---
symbol: "HAVCR2"
type: "gene"
col: 5648
ensembl_id: "ENSG00000135077"
name: "hepatitis A virus cellular receptor 2"
location: "5q33.3"
module: 23
arm: "+"
pooled_cpm: 13.2
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/023"]
generated_by: "tahoemap"
---

# HAVCR2

*hepatitis A virus cellular receptor 2* — 5q33.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.94× (z +19.7, q 0e+00, up in 41 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.735× (z -4.0, q 0.040, down in 14 of 48 measured lines) ⚠ cell-cycle shift, explains ~33% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 0.237×; ⚠ toxic; transcription drop); [[Bosentan (hydrate) (drug)]] 0.05 µM in 1 line (H4 0.0599×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (HepG2/C3A 0.107×); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (NCI-H2347 0.208×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDKL3]] (+0.77, fdr 7e-06), [[PRANCR]] (+0.75, fdr 7e-06), [[ZNF547]] (+0.73, fdr 7e-06); moves opposite to [[THEM6]] (-0.60, fdr 1e-04).
> It sits in the **+** arm of [[Module 023]].

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 3 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5648.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.94×** | +19.7 | 0e+00 | 41/45 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.42×** | +10.1 | 2e-21 | 39/48 (SW480, LS 180, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +8.1 | 1e-13 | 25/46 (NCI-H2030, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.84×** | +7.6 | 6e-12 | 31/40 (MIA PaCa-2, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.76×** | +7.3 | 3e-11 | 27/44 (NCI-H2030, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +6.6 | 4e-09 | 14/29 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **1.62×** | +6.2 | 4e-08 | 27/46 (NCI-H23, A-172, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **2.25×** | +5.5 | 3e-06 | 24/43 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.2 | 1e-05 | 21/47 (SW1417, HOP62, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.2 | 0.001 | 21/45 (MIA PaCa-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.34×** | +3.7 | 0.009 | 16/47 (A549, LoVo, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.029 | 10/48 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.032 | 12/48 (A-172, KATO III, …) | top dose only |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | **1.30×** | +3.2 | 0.047 | 8/46 (NCI-H460, NCI-H23, …) | rises with dose |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.28×** | +3.0 | 0.097 | 12/47 (BT-474, A-172, …) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.26×** | +3.0 | 0.097 | 7/46 (LS 180, Panc 03.27, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5648.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 5 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (HEC-1-A 0.237×; ⚠ toxic; transcription drop); [[Bosentan (hydrate) (drug)]] 0.05 µM in 1 line (H4 0.0599×); [[Bosentan (hydrate) (drug)]] 5 µM in 1 line (HepG2/C3A 0.107×); [[Pentoxifylline (drug)]] 0.5 µM in 1 line (NCI-H2347 0.208×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.735×** | -4.0 | 0.040 | 14/48 (HepG2/C3A, hTERT-HPNE, …) | top dose only | composition shift |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 0.781× | -3.2 | 0.23 | 12/48 (COLO 205, CHP-212, …) | all doses, flat |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | 0.783× | -3.2 | 0.23 | 8/48 (NCI-H1573, NCI-H661, …) | all doses, flat |  |
| [[Furosemide (drug)]] 0.5 µM |  | 0.784× | -3.2 | 0.23 | 10/47 (CHP-212, SHP-77, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.31 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5648. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.9 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +12.0) | — |
| [[A549 (line)]] | wt | 17.3 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.99× (z +9.9) | [[Dinaciclib (drug)]] 5 µM 0.249× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 31.7 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +10.7) | [[Dinaciclib (drug)]] 0.05 µM 0.237× (z -10.8) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 11.0 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.45× (z +9.0) | [[AZD2858 (drug)]] 0.5 µM 0.0787× (z -9.2) ⚠ toxic |
| [[MIA PaCa-2 (line)]] | alt | 11.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.90× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 9.38 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.44× (z +15.1) | — |
| [[NCI-H23 (line)]] | alt | 11.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +10.2) | — |
| [[NCI-H460 (line)]] | wt | 8.73 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.67× (z +9.0) | [[Digitoxin (drug)]] 5 µM 0.222× (z -9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~88% of this change |
| [[SW1417 (line)]] | alt | 12.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.61× (z +15.0) | — |
| [[A-172 (line)]] | wt | 11.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +8.7) | — |
| [[A498 (line)]] | wt | 12.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.85× (z +9.2) | — |
| [[BT-474 (line)]] | alt | 13.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.04× (z +9.4) | — |
| [[CFPAC-1 (line)]] | alt | 16.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.23× (z +9.6) | — |
| [[COLO 205 (line)]] | alt | 12.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +9.4) | — |
| [[H4 (line)]] | wt | 14.7 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0599× (z -10.0) |
| [[HepG2_C3A (line)]] | wt | 18.8 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.107× (z -9.8) |
| [[HOP62 (line)]] | alt | 11.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.85× (z +12.3) | — |
| [[HS-578T (line)]] | alt | 15.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.13× (z +10.7) | — |
| [[hTERT-HPNE (line)]] | wt | 10.0 | 0 | 1 | — | [[Palmatine (chloride) (drug)]] 0.5 µM 0.108× (z -8.5) |
| [[LoVo (line)]] | wt | 27.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.44× (z +8.6) | — |
| [[NCI-H2347 (line)]] | alt | 8.07 | 0 | 1 | — | [[Pentoxifylline (drug)]] 0.5 µM 0.208× (z -8.7) |
| [[Panc 03.27 (line)]] | alt | 9.28 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +9.7) | — |
| [[PANC-1 (line)]] | alt | 10.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.31× (z +16.6) | — |
| [[RKO (line)]] | wt | 12.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.03× (z +9.5) | — |
| [[RPMI-7951 (line)]] | alt | 13.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.149× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 8.80 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.71× (z +10.0) | — |
| [[SW48 (line)]] | wt | 10.1 | 0 | 1 | — | [[Vismodegib (drug)]] 0.5 µM 0.0794× (z -8.6) |
| [[A-427 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.04 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 7.18 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 45.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.90 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.77 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.57 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5648), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKL3]] | +0.77 | +0.73 / +0.71 | both halves | 7e-06 |  |
| [[PRANCR]] | +0.75 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[ZNF547]] | +0.73 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[FAM184B]] | +0.73 | +0.61 / +0.67 | both halves | 7e-06 |  |
| [[ZNF213-AS1]] | +0.73 | +0.67 / +0.64 | both halves | 7e-06 |  |
| [[HLA-DMA]] | +0.71 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[PIWIL2]] | +0.71 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[PPP1R42]] | +0.71 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[ANKHD1-DT]] | +0.70 | +0.65 / +0.56 | both halves | 1e-05 |  |
| [[TMEM269]] | +0.70 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[ZNF425]] | +0.70 | +0.66 / +0.60 | both halves | 7e-06 |  |
| [[CFAP53]] | +0.70 | +0.62 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THEM6]] | -0.60 | -0.36 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 023]]; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.725). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.34).
- **Nodal map** (x, y) = (3.2, 18.8); signed map (26.5, -6.6). **Vector** length 91.1, 18.5% of its response variance represented; |z| ≥ 3 in 861 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.6 | +19.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.4 | +10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +5.6 | +6.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +5.0 | +5.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.4 | +7.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.7 | +3.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.7 | +3.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.6 | +3.0 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.5 | -1.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | +0.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.4 | +2.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | +1.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -2.8 | -0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.2 | -3.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -0.3 |
|  | [[Cytarabine (hydrochloride) (drug)]] 0.05 µM |  | -1.9 | -2.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -1.9 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | hepatitis A virus cellular receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q33.3 — chr5:157,085,422-157,142,869 (-) |
| Ensembl biotype | protein_coding |
| Also known as | Tim-3, TIM3, FLJ14428, TIMD3, CD366 |
| Gene groups (HGNC) | V-set domain containing |
| Reactome | 3 pathways, smallest: Interleukin-2 family signaling; Signaling by Interleukins; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8TDQ0](https://www.uniprot.org/uniprotkb/Q8TDQ0) (Hepatitis A virus cellular receptor 2):

> Cell surface receptor implicated in modulating innate and adaptive immune responses. Generally accepted to have an inhibiting function. Reports on stimulating functions suggest that the activity may be influenced by the cellular context and/or the respective ligand. Regulates macrophage activation. Inhibits T-helper type 1 lymphocyte (Th1)-mediated auto- and alloimmune responses and promotes immunological tolerance. In CD8+ cells attenuates TCR-induced signaling, specifically by blocking …

**Summary**, from NCBI Gene [84868](https://www.ncbi.nlm.nih.gov/gene/84868):

> The protein encoded by this gene belongs to the immunoglobulin superfamily, and TIM family of proteins. CD4-positive T helper lymphocytes can be divided into types 1 (Th1) and 2 (Th2) on the basis of their cytokine secretion patterns. Th1 cells are involved in cell-mediated immunity to intracellular pathogens and delayed-type hypersensitivity reactions, whereas, Th2 cells are involved in the control of extracellular helminthic infections and the promotion of atopic and allergic diseases. This …

**Accessions** — [HGNC:18437](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18437) · Entrez [84868](https://www.ncbi.nlm.nih.gov/gene/84868) · UniProt [Q8TDQ0](https://www.uniprot.org/uniprotkb/Q8TDQ0) · Ensembl [ENSG00000135077](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135077)

## Data

Gene col 5648: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5648); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5648, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5648]; `tensor/DDL_lfc|DDL_z.npy` [5648]; `embed/gene_vectors.npy` [5648]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5648 or target_col == 5648). Every well: [[HAVCR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HAVCR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
