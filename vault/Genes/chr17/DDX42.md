---
symbol: "DDX42"
type: "gene"
col: 12558
ensembl_id: "ENSG00000198231"
name: "DEAD-box helicase 42"
location: "17q23.3"
module: 57
arm: "+"
pooled_cpm: 130.59
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 2
n_dd_up_clean: 5
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/057"]
generated_by: "tahoemap"
---

# DDX42

*DEAD-box helicase 42* — 17q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.16× (z +9.8, q 4e-20, up in 39 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.800× (z -7.8, q 4e-12, down in 27 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (AsPC-1 0.546×, HOP62 0.651×, SK-MEL-2 0.638×, SW480 0.743×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2347 0.619×, CFPAC-1 0.639×; ⚠ cell-cycle shift, explains ~20% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW 900 0.440×, SW48 0.436×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ELP1]] (+0.62, fdr 1e-05), [[UTP18]] (+0.61, fdr 1e-05), [[NUDT21]] (+0.58, fdr 1e-05); moves opposite to [[LETM2]] (-0.51, fdr 5e-05), [[CREM]] (-0.49, fdr 8e-05), [[LINC00944]] (-0.49, fdr 5e-05).
> It sits in the **+** arm of [[Module 057]] (Peroxisomal protein import).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 8 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12558.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.16×** | +9.8 | 4e-20 | 39/49 (SW480, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.85×** | +7.9 | 9e-13 | 33/48 (HEC-1-A, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.33×** | +6.9 | 1e-09 | 30/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +6.4 | 3e-08 | 28/48 (HEC-1-A, MIA PaCa-2, …) | two highest doses | cell-cycle shift (explains ~7% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.29×** | +5.9 | 4e-07 | 29/47 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | 1.18× | +5.6 | 2e-06 | 22/48 (NCI-H1792, A549, …) | two highest doses | composition shift |
| [[Glycyrrhizic acid (drug)]] 0.5 µM |  | 1.17× | +3.9 | 0.009 | 12/48 (A549, C32, …) | inconsistent across doses | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.34×** | +3.7 | 0.015 | 22/45 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.6 | 0.022 | 17/48 (PANC-1, SNU-423, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | 1.15× | +3.3 | 0.046 | 17/48 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~20% of this change | 1.15× | +3.3 | 0.051 | 16/48 (RPMI-7951, PANC-1, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.14× | +3.2 | 0.059 | 12/48 (SW480, Hs 766T, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~12% of this change | 1.13× | +3.1 | 0.093 | 15/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.27×** | +3.0 | 0.095 | 11/49 (A498, SNU-423, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12558.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 4 lines (AsPC-1 0.546×, HOP62 0.651×, SK-MEL-2 0.638×, SW480 0.743×); [[Homoharringtonine (drug)]] 5 µM in 2 lines (NCI-H2347 0.619×, CFPAC-1 0.639×; ⚠ cell-cycle shift, explains ~20% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (SW 900 0.440×, SW48 0.436×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.800×** | -7.8 | 4e-12 | 27/49 (AsPC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.769×** | -6.2 | 2e-07 | 32/47 (MIA PaCa-2, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains <1% of this change | 0.837× | -4.4 | 0.002 | 22/49 (SW480, Hs 766T, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~8% of this change | 0.838× | -4.3 | 0.002 | 23/48 (SW48, NCI-H2347, …) | rises with dose |  |
| [[Adenine (drug)]] 5 µM |  | 0.892× | -4.0 | 0.007 | 5/48 (Hs 766T, HS-578T, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.867× | -3.5 | 0.042 | 20/48 (A-172, HOP62, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.01 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12558. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 115 | 6 (5 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.84× (z +17.7) | — |
| [[LS 180 (line)]] | wt | 103 | 3 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.93× (z +13.4) | — |
| [[SW480 (line)]] | alt | 167 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 1.85× (z +12.4) | — |
| [[HEC-1-A (line)]] | alt | 177 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 3.11× (z +9.6) | — |
| [[KATO III (line)]] | alt | 141 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 4.49× (z +10.4) | — |
| [[NCI-H1573 (line)]] | alt | 88.9 | 2 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 3.70× (z +9.4) | — |
| [[PANC-1 (line)]] | alt | 89.2 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.05× (z +11.5) | — |
| [[SW48 (line)]] | wt | 138 | 1 | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.37× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.436× (z -9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-427 (line)]] | wt | 171 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.555× (z -9.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 142 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.69× (z +10.1) ⚠ cell-cycle shift, explains ~20% of this change | — |
| [[AsPC-1 (line)]] | alt | 108 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.546× (z -11.2) |
| [[CFPAC-1 (line)]] | alt | 128 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.639× (z -8.8) ⚠ cell-cycle shift, explains ~20% of this change |
| [[COLO 205 (line)]] | alt | 121 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.413× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 136 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.651× (z -9.4) |
| [[LoVo (line)]] | wt | 112 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 1.82× (z +9.3) ⚠ toxic | — |
| [[MIA PaCa-2 (line)]] | alt | 152 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.506× (z -9.6) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 81.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +10.2) ⚠ cell-cycle shift, explains ~20% of this change | — |
| [[NCI-H2347 (line)]] | alt | 157 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.619× (z -11.3) ⚠ cell-cycle shift, explains ~20% of this change |
| [[Panc 03.27 (line)]] | alt | 143 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.83× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 138 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.638× (z -8.6) |
| [[SW 900 (line)]] | alt | 153 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.440× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 124 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 181 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 143 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 99.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 204 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 106 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 279 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 140 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 167 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 124 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 89.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 122 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 104 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 134 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 143 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 112 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 96.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 119 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 103 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 93.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 148 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 131 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 112 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 153 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12558), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ELP1]] | +0.62 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[UTP18]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[NUDT21]] | +0.58 | +0.59 / +0.54 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions |
| [[PDHA1]] | +0.57 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[LONP2]] | +0.56 | +0.54 / +0.52 | both halves | 1e-05 |  |
| [[POLR2B]] | +0.56 | +0.50 / +0.55 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions |
| [[URI1]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[DHX16]] | +0.56 | +0.34 / +0.58 | both halves | 1e-04 | pathway: Dengue Virus-Host Interactions; STRING 491 |
| [[RNF20]] | +0.56 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[SNRNP200]] | +0.55 | +0.53 / +0.57 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions; STRING 450 |
| [[PWP1]] | +0.55 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[VTI1B]] | +0.55 | +0.55 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LETM2]] | -0.51 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[CREM]] | -0.49 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[LINC00944]] | -0.49 | -0.44 / -0.39 | both halves | 5e-05 |  |
| [[PHLDA2]] | -0.49 | -0.35 / -0.56 | both halves | 1e-04 |  |
| [[ZNF335]] | -0.48 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[ISG20]] | -0.48 | -0.37 / -0.49 | both halves | 7e-05 |  |
| [[SERTAD1]] | -0.48 | -0.40 / -0.57 | both halves | 5e-05 |  |
| [[BBIP1]] | -0.47 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[S100A11]] | -0.47 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[NPHS1]] | -0.47 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[DNAJC6]] | -0.47 | -0.45 / -0.32 | both halves | 2e-04 |  |
| [[PLA2G4C]] | -0.47 | -0.43 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 057]] — Peroxisomal protein import; 86 genes; this gene is in the **+** arm (projection on the module's main direction 0.568). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-20.1, -45.8); signed map (-23.7, -49.7). **Vector** length 92.4, 22.2% of its response variance represented; |z| ≥ 3 in 881 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +4.5 | -1.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +3.9 | +5.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~20% of this change | +3.6 | +3.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.6 | +1.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.4 | -2.6 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.9 | +1.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.7 | -1.5 |
|  | [[Arbutin (drug)]] 0.05 µM |  | +1.6 | +0.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.6 | -1.0 |
|  | [[Pasireotide (acetate) (drug)]] 0.5 µM |  | +1.5 | +1.0 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.1 | -1.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -5.6 | -3.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~13% of this change | -3.9 | +2.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.8 | -6.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | -3.8 | +3.3 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.2 | -0.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -0.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -2.5 |
|  | [[Infigratinib (drug)]] 5 µM |  | -1.6 | -0.5 |
|  | [[Loperamide (hydrochloride) (drug)]] 5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | DEAD-box helicase 42 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q23.3 — chr17:63,773,603-63,819,317 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RNAHP, RHELP, SF3b125, SF3B8 |
| Gene groups (HGNC) | DEAD-box helicases |
| Reactome | 14 pathways, smallest: mRNA Splicing - Minor Pathway; CHD1 and CHD2 subfamily; CHD chromatin remodelers |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86XP3](https://www.uniprot.org/uniprotkb/Q86XP3) (ATP-dependent RNA helicase DDX42):

> ATP-dependent RNA helicase that binds to partially double-stranded RNAs (dsRNAs) in order to unwind RNA secondary structures. Unwinding is promoted in the presence of single-strand binding proteins. Also mediates RNA duplex formation thereby displacing the single-strand RNA binding protein. ATP and ADP modulate its activity: ATP binding and hydrolysis by DDX42 triggers RNA strand separation, whereas the ADP-bound form of the protein triggers annealing of complementary RNA strands. Required for …

**Summary**, from NCBI Gene [11325](https://www.ncbi.nlm.nih.gov/gene/11325):

> This gene encodes a member of the Asp-Glu-Ala-Asp (DEAD) box protein family. Members of this protein family are putative RNA helicases, and are implicated in a number of cellular processes involving alteration of RNA secondary structure such as translation initiation, nuclear and mitochondrial splicing, and ribosome and spliceosome assembly. Members of this family are believed to be involved in embryogenesis, spermatogenesis, and cellular growth and division. Two transcript variants encoding …

**Accessions** — [HGNC:18676](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18676) · Entrez [11325](https://www.ncbi.nlm.nih.gov/gene/11325) · UniProt [Q86XP3](https://www.uniprot.org/uniprotkb/Q86XP3) · Ensembl [ENSG00000198231](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198231)

## Data

Gene col 12558: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12558); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12558, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12558]; `tensor/DDL_lfc|DDL_z.npy` [12558]; `embed/gene_vectors.npy` [12558]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12558 or target_col == 12558). Every well: [[DDX42 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DDX42.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
