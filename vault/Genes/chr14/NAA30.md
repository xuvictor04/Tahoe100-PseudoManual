---
symbol: "NAA30"
type: "gene"
col: 6362
ensembl_id: "ENSG00000139977"
name: "N-alpha-acetyltransferase 30, NatC catalytic subunit"
location: "14q22.3"
module: 12
arm: "+"
pooled_cpm: 35.91
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 3
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/012"]
generated_by: "tahoemap"
---

# NAA30

*N-alpha-acetyltransferase 30, NatC catalytic subunit* — 14q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.67× (z +12.8, q 1e-34, up in 38 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.639× (z -11.1, q 5e-26, down in 31 of 46 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (A549 0.113×, SHP-77 0.145×, NCI-H1573 0.191×, MIA PaCa-2 0.227×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HCT15 0.109×, SW48 0.213×, NCI-H460 0.399×, CFPAC-1 0.433×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.343×, HS-578T 0.252×; ⚠ toxic; transcription drop); [[Atazanavir (sulfate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0891×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RP9]] (+0.71, fdr 7e-06), [[C18orf21]] (+0.69, fdr 7e-06), [[MRPS31]] (+0.68, fdr 7e-06); moves opposite to [[ATP2A2]] (-0.64, fdr 7e-06), [[HNRNPA3]] (-0.61, fdr 1e-05), [[SMG1P3]] (-0.59, fdr 1e-05).
> It sits in the **+** arm of [[Module 012]] (mRNA Splicing - Major Pathway).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6362.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.67×** | +12.8 | 1e-34 | 38/47 (NCI-H23, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.43×** | +12.7 | 2e-34 | 34/47 (PANC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.49×** | +9.9 | 1e-20 | 33/48 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.40×** | +8.1 | 6e-14 | 33/48 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **1.80×** | +7.6 | 2e-12 | 28/49 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.26×** | +5.8 | 5e-07 | 20/48 (HEC-1-A, A-427, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.22×** | +4.6 | 3e-04 | 15/48 (CFPAC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.41×** | +4.4 | 6e-04 | 15/48 (NCI-H1573, KATO III, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +4.4 | 8e-04 | 16/47 (SW1417, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | 1.18× | +4.2 | 0.001 | 17/48 (NCI-H23, PANC-1, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.2 | 0.001 | 18/48 (AsPC-1, BT-474, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | 1.19× | +4.2 | 0.001 | 18/47 (SW1417, KATO III, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.17× | +3.7 | 0.010 | 12/47 (NCI-H460, SW48, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | 1.15× | +3.6 | 0.014 | 8/47 (NCI-H2030, HOP62, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.15× | +3.5 | 0.016 | 12/47 (SNU-423, NCI-H2030, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.025 | 11/46 (NCI-H460, C-33 A, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6362.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 8 lines (A549 0.113×, SHP-77 0.145×, NCI-H1573 0.191×, MIA PaCa-2 0.227×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 4 lines (HCT15 0.109×, SW48 0.213×, NCI-H460 0.399×, CFPAC-1 0.433×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (NCI-H2030 0.343×, HS-578T 0.252×; ⚠ toxic; transcription drop); [[Atazanavir (sulfate) (drug)]] 0.5 µM in 1 line (SW 1271 0.0891×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.639×** | -11.1 | 5e-26 | 31/46 (HCT15, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.705×** | -8.4 | 2e-14 | 23/38 (A549, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.733×** | -7.1 | 2e-10 | 22/41 (NCI-H2030, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.939× | -5.2 | 4e-05 | 4/49 (COLO 205, SW 1271, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, +0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6362. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 22.4 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.62× (z +14.7) | — |
| [[HEC-1-A (line)]] | alt | 33.3 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.54× (z +14.0) | — |
| [[NCI-H1573 (line)]] | alt | 40.3 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +10.5) | [[Dinaciclib (drug)]] 5 µM 0.191× (z -16.0) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 66.9 | 1 | 2 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 2.33× (z +9.1) | [[Dinaciclib (drug)]] 0.05 µM 0.343× (z -11.1) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 28.5 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 1.91× (z +8.8) | — |
| [[HCT15 (line)]] | alt | 42.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -15.2) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 27.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.26× (z +10.2) | [[Dinaciclib (drug)]] 0.05 µM 0.337× (z -8.8) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 31.9 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.73× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.227× (z -12.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 55.6 | 2 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.79× (z +11.2) | — |
| [[NCI-H2347 (line)]] | alt | 40.0 | 0 | 2 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.526× (z -10.7) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-1 (line)]] | wt | 36.0 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.214× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~15% of this change |
| [[A549 (line)]] | wt | 34.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.113× (z -18.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 32.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.277× (z -9.3) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 52.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.433× (z -9.8) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 20.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.252× (z -9.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 23.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -10.8) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 32.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.257× (z -9.0) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 36.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.313× (z -9.8) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 31.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.399× (z -10.2) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 46.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.350× (z -9.9) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 60.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -18.3) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 54.2 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 0.5 µM 0.0891× (z -9.5) |
| [[SW 900 (line)]] | alt | 40.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.335× (z -8.8) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 53.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.213× (z -11.5) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 24.2 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 38.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 37.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 37.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 35.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 24.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 47.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 28.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 51.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6362), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RP9]] | +0.71 | +0.70 / +0.71 | both halves | 7e-06 |  |
| [[C18orf21]] | +0.69 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[MRPS31]] | +0.68 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[DPF2]] | +0.68 | +0.61 / +0.73 | both halves | 7e-06 |  |
| [[PDRG1]] | +0.66 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[PHAX]] | +0.66 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[RBMX2]] | +0.66 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[ASB8]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[NSMCE3]] | +0.65 | +0.57 / +0.66 | both halves | 9e-06 |  |
| [[SNHG11]] | +0.64 | +0.55 / +0.65 | both halves | 1e-05 |  |
| [[CCDC174]] | +0.64 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ELOF1]] | +0.63 | +0.60 / +0.58 | both halves | 8e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP2A2]] | -0.64 | -0.59 / -0.66 | both halves | 7e-06 |  |
| [[HNRNPA3]] | -0.61 | -0.51 / -0.63 | both halves | 1e-05 |  |
| [[SMG1P3]] | -0.59 | -0.49 / -0.65 | both halves | 1e-05 |  |
| [[RBBP7]] | -0.57 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[FAM81A]] | -0.56 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[ITGB1]] | -0.55 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[EMB]] | -0.55 | -0.43 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 012]] — mRNA Splicing - Major Pathway; 215 genes; this gene is in the **+** arm (projection on the module's main direction 0.721). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.28).
- **Nodal map** (x, y) = (-39.2, -9.0); signed map (-15.1, -7.8). **Vector** length 79.7, 14.6% of its response variance represented; |z| ≥ 3 in 788 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +4.8 | +9.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.5 | +12.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +5.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | +3.6 | +3.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.1 | +8.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.3 | +3.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +2.3 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +3.4 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +0.2 |
| fall | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.3 | -7.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.8 | -11.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.7 | -8.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -2.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.8 | -1.7 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.6 | -2.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -1.5 | -0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.3 | -2.1 |
|  | [[Encorafenib (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Methotrexate (drug)]] 5 µM |  | -1.2 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | N-alpha-acetyltransferase 30, NatC catalytic subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q22.3 — chr14:57,390,544-57,415,906 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35355, MAK3, Mak3p; previously C14orf35, NAT12 |
| Gene groups (HGNC) | N-alpha-acetyltransferase subunits; GCN5 related N-acetyltransferases |
| Reactome | 4 pathways, smallest: Retrograde transport at the Trans-Golgi-Network; Intra-Golgi and retrograde Golgi-to-ER traffic; Membrane Trafficking |
| Matched by | ensembl_id |

**Function**, from UniProt [Q147X3](https://www.uniprot.org/uniprotkb/Q147X3) (N-alpha-acetyltransferase 30):

> Catalytic subunit of the N-terminal acetyltransferase C (NatC) complex. Catalyzes acetylation of the N-terminal methionine residues of peptides beginning with Met-Leu-Ala and Met-Leu-Gly. N-terminal acetylation protects proteins from ubiquitination and degradation by the N-end rule pathway. Necessary for the lysosomal localization and function of ARL8B sugeesting that ARL8B is a NatC substrate.

**Summary**, from NCBI Gene [122830](https://www.ncbi.nlm.nih.gov/gene/122830):

> Enables protein-N-terminal amino-acid acetyltransferase activity. Involved in protein stabilization. Located in cytosol and nucleus. Part of NatC complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19844](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19844) · Entrez [122830](https://www.ncbi.nlm.nih.gov/gene/122830) · UniProt [Q147X3](https://www.uniprot.org/uniprotkb/Q147X3) · Ensembl [ENSG00000139977](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139977)

## Data

Gene col 6362: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6362); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6362, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6362]; `tensor/DDL_lfc|DDL_z.npy` [6362]; `embed/gene_vectors.npy` [6362]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6362 or target_col == 6362). Every well: [[NAA30 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NAA30.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
