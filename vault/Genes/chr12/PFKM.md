---
symbol: "PFKM"
type: "gene"
col: 7641
ensembl_id: "ENSG00000152556"
name: "phosphofructokinase, muscle"
location: "12q13.11"
module: 25
arm: "+"
pooled_cpm: 14.25
n_lines_expressing: 49
n_dd_up: 21
n_dd_down: 4
n_dd_up_clean: 10
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/025"]
generated_by: "tahoemap"
---

# PFKM

*phosphofructokinase, muscle* — 12q13.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.42× (z +12.9, q 1e-35, up in 34 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.67× (z +7.5, q 8e-12, up in 33 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.718× (z -4.9, q 7e-04, down in 21 of 45 measured lines) ⚠ cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Bergenin (drug)]] 0.5 µM: 0.741× (z -4.4, q 0.002, down in 12 of 45 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Vilanterol (drug)]] 0.05 µM in 1 line (Hs 766T 0.0852×); [[Clotrimazole (drug)]] 0.5 µM in 1 line (H4 0.0895×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.176×; ⚠ cell-cycle shift, explains ~31% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.263×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NONO]] (+0.73, fdr 7e-06), [[RAD23B]] (+0.71, fdr 1e-05), [[MEST]] (+0.69, fdr 1e-05); moves opposite to [[TNRC6C]] (-0.65, fdr 1e-05), [[TMEM258]] (-0.64, fdr 7e-06), [[INAFM1]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 025]] (oxidative phosphorylation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7641.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.42×** | +12.9 | 1e-35 | 34/41 (NCI-H460, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.45×** | +12.6 | 6e-34 | 23/27 (NCI-H460, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.71×** | +7.8 | 9e-13 | 32/47 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.67×** | +7.5 | 8e-12 | 33/46 (C32, A-172, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +7.3 | 4e-11 | 24/36 (J82, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +7.2 | 8e-11 | 28/47 (A-172, Hs 766T, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.55×** | +6.4 | 9e-09 | 29/46 (LoVo, KATO III, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.55×** | +6.4 | 9e-09 | 27/46 (SW480, NCI-H1792, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.45×** | +5.5 | 3e-06 | 20/46 (LS 180, KATO III, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +5.2 | 1e-05 | 25/46 (KATO III, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.39×** | +4.9 | 6e-05 | 20/46 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.27×** | +4.7 | 1e-04 | 17/45 (PANC-1, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.27×** | +4.6 | 2e-04 | 19/47 (LoVo, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.35×** | +4.3 | 6e-04 | 19/46 (HS-578T, LOX-IMVI, …) | rises with dose |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.71×** | +4.1 | 0.002 | 11/36 (A498, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.32×** | +4.1 | 0.002 | 15/46 (C32, HOP62, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **1.70×** | +4.1 | 0.002 | 10/47 (AsPC-1, LS 180, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **1.28×** | +3.7 | 0.008 | 11/47 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM |  | **1.28×** | +3.6 | 0.010 | 21/46 (NCI-H23, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7641.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Vilanterol (drug)]] 0.05 µM in 1 line (Hs 766T 0.0852×); [[Clotrimazole (drug)]] 0.5 µM in 1 line (H4 0.0895×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (SK-MEL-2 0.176×; ⚠ cell-cycle shift, explains ~31% of this change); [[Homoharringtonine (drug)]] 5 µM in 1 line (SHP-77 0.263×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.718×** | -4.9 | 7e-04 | 21/45 (SK-MEL-2, HCT15, …) | inconsistent across doses |  |
| [[Bergenin (drug)]] 0.5 µM |  | **0.741×** | -4.4 | 0.002 | 12/45 (SK-MEL-2, BT-474, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.741×** | -4.4 | 0.002 | 21/45 (BT-474, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Vilanterol (drug)]] 5 µM |  | 0.839× | -3.4 | 0.069 | 13/47 (SW 1088, J82, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.792×** | -3.4 | 0.069 | 14/46 (NCI-H1573, SNU-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.37 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7641. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 22.1 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 4.03× (z +10.7) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.428× (z -9.1) ⚠ cell-cycle shift, explains ~63% of this change |
| [[A-172 (line)]] | wt | 11.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.49× (z +9.7) | — |
| [[A498 (line)]] | wt | 15.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.56× (z +9.2) ⚠ toxic; transcription drop | — |
| [[H4 (line)]] | wt | 13.8 | 0 | 1 | — | [[Clotrimazole (drug)]] 0.5 µM 0.0895× (z -9.9) |
| [[Hs 766T (line)]] | wt | 12.2 | 0 | 1 | — | [[Vilanterol (drug)]] 0.05 µM 0.0852× (z -12.6) |
| [[hTERT-HPNE (line)]] | wt | 10.4 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.0911× (z -9.4) |
| [[J82 (line)]] | alt | 14.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.12× (z +8.9) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 12.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.30× (z +12.0) | — |
| [[SHP-77 (line)]] | alt | 20.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -9.6) |
| [[SK-MEL-2 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.176× (z -9.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[A-427 (line)]] | wt | 5.09 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 37.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.84 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.22 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.74 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.97 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 12.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.38 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 8.31 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 44.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 45.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 19.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7641), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NONO]] | +0.73 | +0.67 / +0.69 | both halves | 7e-06 | same gene group |
| [[RAD23B]] | +0.71 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[MEST]] | +0.69 | +0.57 / +0.69 | both halves | 1e-05 | same gene group |
| [[PRPS1]] | +0.68 | +0.63 / +0.65 | both halves | 7e-06 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[PPP2R1B]] | +0.68 | +0.56 / +0.69 | both halves | 1e-05 | pathway: Glucose metabolism |
| [[IPO8]] | +0.67 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[FECH]] | +0.67 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[DLD]] | +0.67 | +0.58 / +0.72 | both halves | 7e-06 | STRING 421 |
| [[PPT1]] | +0.67 | +0.49 / +0.76 | both halves | 2e-05 |  |
| [[PRDX3]] | +0.67 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[CRYZ]] | +0.66 | +0.50 / +0.67 | both halves | 1e-05 |  |
| [[MAT2A]] | +0.66 | +0.49 / +0.71 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC6C]] | -0.65 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[TMEM258]] | -0.64 | -0.59 / -0.66 | both halves | 7e-06 | same gene group |
| [[INAFM1]] | -0.63 | -0.55 / -0.63 | both halves | 1e-05 |  |
| [[RPL36AL]] ⚠ | -0.62 | -0.61 / -0.61 | both halves | 7e-06 | ⚠ in the vector space only through flagged drug-doses |
| [[EIF1B]] | -0.62 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[TERF2IP]] | -0.62 | -0.47 / -0.63 | both halves | 2e-05 |  |
| [[TPRN]] | -0.60 | -0.34 / -0.66 | both halves | 1e-04 |  |
| [[GCC2]] | -0.60 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[SELENOK]] | -0.60 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[ZBTB7A]] | -0.60 | -0.48 / -0.60 | both halves | 2e-05 |  |
| [[HIC2]] | -0.60 | -0.53 / -0.58 | both halves | 1e-05 |  |
| [[ING2]] | -0.59 | -0.35 / -0.67 | both halves | 1e-04 |  |
| [[RBX1]] | -0.59 | -0.48 / -0.64 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 025]] — oxidative phosphorylation; 171 genes; this gene is in the **+** arm (projection on the module's main direction 0.736). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-26.4, -16.3); signed map (-19.0, -42.6). **Vector** length 88.5, 17.7% of its response variance represented; |z| ≥ 3 in 937 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.8 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.4 | +12.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +7.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +5.7 | +7.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +7.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.1 | +4.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.9 | +4.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.2 | +3.7 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +2.1 | +2.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -2.8 | -4.9 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.5 | -0.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.5 | -3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.2 | -2.2 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | -3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -2.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.8 | -0.8 |
|  | [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | -1.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | phosphofructokinase, muscle |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.11 — chr12:48,105,139-48,146,404 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PFK-1, PPP1R122; previously PFKX |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; MicroRNA protein coding host genes; Phosphofructokinase family |
| Hallmark sets | BILE_ACID_METABOLISM, MYOGENESIS |
| Reactome | 3 pathways, smallest: Glycolysis; Glucose metabolism; Metabolism of carbohydrates and carbohydrate derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [P08237](https://www.uniprot.org/uniprotkb/P08237) (ATP-dependent 6-phosphofructokinase, muscle type):

> Catalyzes the phosphorylation of D-fructose 6-phosphate to fructose 1,6-bisphosphate by ATP, the first committing step of glycolysis.

**Summary**, from NCBI Gene [5213](https://www.ncbi.nlm.nih.gov/gene/5213):

> Three phosphofructokinase isozymes exist in humans: muscle, liver and platelet. These isozymes function as subunits of the mammalian tetramer phosphofructokinase, which catalyzes the phosphorylation of fructose-6-phosphate to fructose-1,6-bisphosphate. Tetramer composition varies depending on tissue type. This gene encodes the muscle-type isozyme. Mutations in this gene have been associated with glycogen storage disease type VII, also known as Tarui disease. Alternatively spliced transcript …

**Accessions** — [HGNC:8877](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8877) · Entrez [5213](https://www.ncbi.nlm.nih.gov/gene/5213) · UniProt [P08237](https://www.uniprot.org/uniprotkb/P08237) · Ensembl [ENSG00000152556](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000152556)

## Data

Gene col 7641: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7641); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7641, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7641]; `tensor/DDL_lfc|DDL_z.npy` [7641]; `embed/gene_vectors.npy` [7641]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7641 or target_col == 7641). Every well: [[PFKM — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PFKM.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
