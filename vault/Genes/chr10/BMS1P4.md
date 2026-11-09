---
symbol: "BMS1P4"
type: "gene"
col: 14312
ensembl_id: "ENSG00000242338"
name: "BMS1 pseudogene 4"
location: "10q22.2"
module: 114
arm: "+"
pooled_cpm: 9.96
n_lines_expressing: 50
n_dd_up: 3
n_dd_down: 7
n_dd_up_clean: 2
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# BMS1P4

*BMS1 pseudogene 4* — 10q22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.12× (z +4.4, q 0.008, up in 2 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.5 µM: 1.45× (z +4.1, q 0.008, up in 16 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (5 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.550× (z -6.5, q 5e-08, down in 26 of 38 measured lines) ⚠ toxic. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.583× (z -6.1, q 3e-07, down in 29 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (PANC-1 0.125×, SW1417 0.0777×, Hs 766T 0.0937×, HS-578T 0.0816×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (A-427 0.126×, NCI-H1792 0.0769×, NCI-H460 0.205×; ⚠ toxic); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (NCI-H460 0.173×, PANC-1 0.304×, SW480 0.356×); [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM in 1 line (Hs 766T 0.0558×); [[Monocrotaline (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0637×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RPP14]] (+0.69, fdr 7e-06), [[ZNF3]] (+0.68, fdr 7e-06), [[BMS1P4-1]] (+0.68, fdr 7e-06, ⚠ same locus), [[NDUFAB1]] (+0.67, fdr 7e-06); moves opposite to [[CREG1]] (-0.54, fdr 2e-05), [[CNN3]] (-0.50, fdr 2e-05), [[VPS13A]] (-0.49, fdr 3e-05).
> It is in [[Module 114]], a single-armed module.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 3 with an alert ⚠. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14312.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.12× | +4.4 | 0.008 | 2/48 (HEC-1-A, AsPC-1) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.45×** | +4.1 | 0.008 | 16/46 (LoVo, HOP62, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.67×** | +4.1 | 0.008 | 16/41 (SW1417, MIA PaCa-2, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.9 | 0.014 | 19/38 (NCI-H1792, SW48, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | 1.22× | +3.1 | 0.19 | 14/44 (SHP-77, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 5 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14312.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (PANC-1 0.125×, SW1417 0.0777×, Hs 766T 0.0937×, HS-578T 0.0816×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change); [[Niclosamide (olamine) (drug)]] 5 µM in 3 lines (A-427 0.126×, NCI-H1792 0.0769×, NCI-H460 0.205×; ⚠ toxic); [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (NCI-H460 0.173×, PANC-1 0.304×, SW480 0.356×); [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM in 1 line (Hs 766T 0.0558×); [[Monocrotaline (drug)]] 0.05 µM in 1 line (SK-MEL-2 0.0637×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.550×** | -6.5 | 5e-08 | 26/38 (A-427, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.583×** | -6.1 | 3e-07 | 29/47 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.579×** | -5.9 | 6e-07 | 14/15 (PANC-1, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.567×** | -5.8 | 9e-07 | 17/27 (AsPC-1, SW480, …) | all doses, flat | cell-cycle shift (explains ~5% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.667×** | -4.6 | 5e-04 | 22/46 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.742×** | -3.4 | 0.068 | 17/46 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | **0.751×** | -3.2 | 0.097 | 15/35 (PANC-1, SW1417, …) | all doses, flat | composition shift |
| [[Mebendazole (drug)]] 5 µM |  | 0.749× | -3.2 | 0.11 | 6/48 (NCI-H460, RKO, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14312. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 21.5 | 0 | 5 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.194× (z -14.2) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.356× (z -8.9) |
| [[NCI-H460 (line)]] | wt | 8.76 | 0 | 4 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.165× (z -11.1) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.173× (z -10.8) |
| [[Hs 766T (line)]] | wt | 8.90 | 0 | 3 (1 ⚠) | — | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM 0.0558× (z -13.0) |
| [[PANC-1 (line)]] | alt | 17.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0530× (z -22.3) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.304× (z -9.4) |
| [[AsPC-1 (line)]] | alt | 7.99 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0912× (z -9.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 11.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.126× (z -11.2) ⚠ toxic |
| [[C-33 A (line)]] | alt | 8.04 | 0 | 1 | — | [[Acetazolamide (drug)]] 0.5 µM 0.0731× (z -9.4) |
| [[HS-578T (line)]] | alt | 7.23 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0816× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[LoVo (line)]] | wt | 13.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.256× (z -8.5) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 6.49 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0769× (z -10.2) ⚠ toxic |
| [[NCI-H2347 (line)]] | alt | 8.72 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.232× (z -8.8) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 7.21 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0637× (z -9.7) |
| [[SW1417 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0777× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[SW48 (line)]] | wt | 20.8 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.111× (z -9.8) ⚠ cell-cycle shift, explains ~64% of this change |
| [[A-172 (line)]] | wt | 6.58 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.21 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.28 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 8.56 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.92 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.66 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.55 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 9.05 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.74 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.63 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.73 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.13 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 10.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14312), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RPP14]] | +0.69 | +0.69 / +0.69 | both halves | 7e-06 |  |
| [[ZNF3]] | +0.68 | +0.65 / +0.70 | both halves | 7e-06 |  |
| [[BMS1P4-1]] | +0.68 | +0.66 / +0.77 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[NDUFAB1]] | +0.67 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[MTG2]] | +0.67 | +0.66 / +0.74 | both halves | 7e-06 |  |
| [[ZNF7]] | +0.67 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[ZNF500]] | +0.63 | +0.55 / +0.64 | both halves | 1e-05 |  |
| [[TEFM]] | +0.61 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ZNF16]] | +0.61 | +0.55 / +0.59 | both halves | 1e-05 |  |
| [[NSUN4]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[ZSCAN32]] | +0.60 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[ALKBH1]] | +0.60 | +0.62 / +0.57 | both halves | 1e-05 |  |
| [[ZSCAN25]] | +0.59 | +0.56 / +0.58 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CREG1]] | -0.54 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[CNN3]] | -0.50 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[VPS13A]] | -0.49 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[IDS]] | -0.49 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[HNRNPA1L3]] | -0.49 | -0.38 / -0.58 | both halves | 7e-05 |  |
| [[MLF1]] | -0.48 | -0.54 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.648). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-43.0, 4.7); signed map (-5.1, -14.3). **Vector** length 75.7, 13.6% of its response variance represented; |z| ≥ 3 in 769 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.0 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.9 | +4.1 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | +2.9 | +0.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +3.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +0.2 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | +2.5 | +1.8 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.2 | +2.9 |
|  | [[Belzutifan (drug)]] 5 µM |  | +1.8 | +2.8 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change | -5.2 | -3.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.0 | -5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.4 | -5.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.3 | -6.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.4 | -6.1 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.9 | -2.4 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.9 | -2.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | +0.6 |
|  | [[Malotilate (drug)]] 0.05 µM |  | -1.7 | -2.8 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -1.6 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | BMS1 pseudogene 4 |
| Locus type | pseudogene |
| Location | 10q22.2 — chr10:73,717,115-73,728,580 (-) |
| Ensembl biotype | transcribed_unprocessed_pseudogene |
| Also known as | OTTHUMG00000018478; previously BMS1LP4 |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:23652](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23652) · Entrez [729096](https://www.ncbi.nlm.nih.gov/gene/729096) · Ensembl [ENSG00000242338](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242338)

## Data

Gene col 14312: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14312); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14312, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14312]; `tensor/DDL_lfc|DDL_z.npy` [14312]; `embed/gene_vectors.npy` [14312]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14312 or target_col == 14312). Every well: [[BMS1P4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BMS1P4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
