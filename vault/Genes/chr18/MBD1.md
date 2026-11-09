---
symbol: "MBD1"
type: "gene"
col: 6560
ensembl_id: "ENSG00000141644"
name: "methyl-CpG binding domain protein 1"
location: "18q21.1"
module: 52
arm: "+"
pooled_cpm: 35.36
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 2
n_dd_up_clean: 15
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/052"]
generated_by: "tahoemap"
---

# MBD1

*methyl-CpG binding domain protein 1* — 18q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (3 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.66× (z +11.7, q 1e-28, up in 44 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.732× (z -5.2, q 1e-04, down in 21 of 38 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (Panc 03.27 0.151×, A549 0.145×, H4 0.241×, SHP-77 0.384×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.215×; ⚠ toxic; transcription drop); [[Saquinavir (drug)]] 0.5 µM in 1 line (CHP-212 0.113×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF558]] (+0.64, fdr 7e-06), [[SZT2]] (+0.62, fdr 1e-05), [[C19orf47]] (+0.56, fdr 4e-05); moves opposite to [[NOTCH2NLR]] (-0.51, fdr 4e-05), [[FCHSD2]] (-0.51, fdr 5e-05), [[PHIP]] (-0.46, fdr 8e-05).
> It sits in the **+** arm of [[Module 052]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[SAMD12]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6560.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.66×** | +11.7 | 1e-28 | 44/49 (NCI-H1573, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.95×** | +11.5 | 5e-28 | 42/48 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.79×** | +10.0 | 3e-21 | 42/48 (SW480, LoVo, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.79×** | +10.0 | 3e-21 | 39/48 (LOX-IMVI, C-33 A, …) | two highest doses | cell-cycle shift (explains ~15% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +9.2 | 3e-18 | 35/47 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.71×** | +9.2 | 4e-18 | 38/48 (LoVo, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~18% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.54×** | +8.4 | 5e-15 | 32/48 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.62×** | +8.3 | 6e-15 | 37/47 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.56×** | +7.6 | 2e-12 | 35/48 (LOX-IMVI, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.50×** | +7.0 | 2e-10 | 35/48 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +6.9 | 3e-10 | 28/48 (MIA PaCa-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +6.7 | 9e-10 | 32/48 (NCI-H1573, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.37×** | +5.4 | 3e-06 | 31/48 (NCI-H1573, SW480, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.35×** | +5.1 | 1e-05 | 25/48 (KATO III, LS 180, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.36×** | +4.9 | 3e-05 | 29/48 (SW480, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.30×** | +4.6 | 2e-04 | 24/47 (NCI-H1573, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6560.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 5 µM in 4 lines (Panc 03.27 0.151×, A549 0.145×, H4 0.241×, SHP-77 0.384×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SNU-1 0.215×; ⚠ toxic; transcription drop); [[Saquinavir (drug)]] 0.5 µM in 1 line (CHP-212 0.113×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.732×** | -5.2 | 1e-04 | 21/38 (Panc 03.27, A549, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.789×** | -4.1 | 0.012 | 22/46 (SNU-1, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Arbutin (drug)]] 5 µM |  | 0.830× | -3.1 | 0.37 | 14/48 (RKO, C32, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.19 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6560. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 53.0 | 8 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 5.63× (z +14.8) | — |
| [[SW480 (line)]] | alt | 25.4 | 5 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 3.64× (z +11.5) | — |
| [[LoVo (line)]] | wt | 39.5 | 4 | 0 | [[Auranofin (drug)]] 5 µM 2.79× (z +10.2) | — |
| [[AsPC-1 (line)]] | alt | 37.1 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.04× (z +14.6) | — |
| [[A549 (line)]] | wt | 23.7 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.35× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.145× (z -14.2) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 47.2 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.81× (z +9.3) | — |
| [[MIA PaCa-2 (line)]] | alt | 34.8 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.61× (z +10.8) | — |
| [[NCI-H23 (line)]] | alt | 38.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.85× (z +13.4) | — |
| [[NCI-H460 (line)]] | wt | 30.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 1.89× (z +9.6) | — |
| [[PANC-1 (line)]] | alt | 27.9 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.01× (z +11.9) | — |
| [[SHP-77 (line)]] | alt | 61.8 | 1 (1 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 2.52× (z +8.7) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.384× (z -8.7) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 28.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.56× (z +12.4) | — |
| [[C-33 A (line)]] | alt | 47.5 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 3.11× (z +8.9) | — |
| [[CHP-212 (line)]] | wt | 36.8 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.113× (z -8.8) |
| [[COLO 205 (line)]] | alt | 25.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.30× (z +11.8) | — |
| [[H4 (line)]] | wt | 47.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.241× (z -9.2) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 39.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.82× (z +10.3) | — |
| [[LOX-IMVI (line)]] | wt | 30.6 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 2.70× (z +9.1) | — |
| [[NCI-H2030 (line)]] | alt | 55.1 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 2.92× (z +8.9) | — |
| [[Panc 03.27 (line)]] | alt | 29.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -14.6) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 34.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -9.4) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 46.5 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.66× (z +9.4) | — |
| [[A-172 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 64.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 18.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 42.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 43.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 45.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 36.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 42.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 32.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6560), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF558]] | +0.64 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[SZT2]] | +0.62 | +0.53 / +0.65 | both halves | 1e-05 |  |
| [[C19orf47]] | +0.56 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[ZNF841]] | +0.56 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[EIF1AD]] | +0.56 | +0.57 / +0.52 | both halves | 1e-05 |  |
| [[SPATA2]] | +0.56 | +0.43 / +0.55 | both halves | 3e-05 |  |
| [[SNIP1]] | +0.55 | +0.47 / +0.62 | both halves | 2e-05 |  |
| [[CHPF2]] | +0.55 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[NOP9]] | +0.55 | +0.51 / +0.49 | both halves | 1e-05 |  |
| [[PPP4C]] | +0.54 | +0.43 / +0.59 | both halves | 3e-05 |  |
| [[ZNF384]] | +0.54 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[CDK9]] | +0.54 | +0.45 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NOTCH2NLR]] | -0.51 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[FCHSD2]] | -0.51 | -0.40 / -0.56 | both halves | 5e-05 |  |
| [[PHIP]] | -0.46 | -0.46 / -0.37 | both halves | 8e-05 |  |
| [[SAMD12]] | -0.46 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[TTC39C]] | -0.45 | -0.43 / -0.37 | both halves | 8e-05 |  |
| [[MAP4K5]] | -0.45 | -0.34 / -0.36 | both halves | 1e-04 |  |
| [[RFK]] | -0.45 | -0.44 / -0.45 | both halves | 3e-05 |  |
| [[PPP1R9A]] | -0.44 | -0.44 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMD12]] | B | SAMD12 activity raises MBD1's level | lines that do not express SAMD12 (20) vs lines expressing it (30) | 1.25× lower at baseline in the lines without SAMD12 | 0.061 | ⚠ within organs, on part of the lines; also absent: MST1R, STYK1, ENSG00000263325 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 052]]; 89 genes; this gene is in the **+** arm (projection on the module's main direction 0.553). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (8.9, -27.7); signed map (-51.6, 2.2). **Vector** length 69.3, 13.3% of its response variance represented; |z| ≥ 3 in 1,021 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +6.5 | +10.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.9 | +11.7 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +3.3 | +2.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +3.2 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +2.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.9 | +8.4 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.6 | +1.3 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | +1.5 | +0.8 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.9 | +2.5 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.1 | +1.6 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -0.3 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -1.9 | -1.4 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.6 | +0.1 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.5 | -1.0 |
|  | [[IQ 1 (drug)]] 0.05 µM |  | -1.3 | -1.2 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -1.3 | -0.2 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.2 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | methyl-CpG binding domain protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.1 — chr18:50,266,882-50,281,774 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PCM1, CXXC3 |
| Gene groups (HGNC) | Zinc fingers CXXC-type; Methyl-CpG binding domain containing |
| Reactome | 3 pathways, smallest: SUMOylation of transcription cofactors; SUMO E3 ligases SUMOylate target proteins; SUMOylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UIS9](https://www.uniprot.org/uniprotkb/Q9UIS9) (Methyl-CpG-binding domain protein 1):

> Transcriptional repressor that binds CpG islands in promoters where the DNA is methylated at position 5 of cytosine within CpG dinucleotides. Binding is abolished by the presence of 7-mG that is produced by DNA damage by methylmethanesulfonate (MMS). Acts as transcriptional repressor and plays a role in gene silencing by recruiting ATF7IP, which in turn recruits factors such as the histone methyltransferase SETDB1. Probably forms a complex with SETDB1 and ATF7IP that represses transcription and …

**Summary**, from NCBI Gene [4152](https://www.ncbi.nlm.nih.gov/gene/4152):

> The protein encoded by this gene is a member of a family of nuclear proteins related by the presence of a methyl-CpG binding domain (MBD). These proteins are capable of binding specifically to methylated DNA, and some members can also repress transcription from methylated gene promoters. This protein contains multiple domains: MBD at the N-terminus that functions both in binding to methylated DNA and in protein interactions; several CXXC-type zinc finger domains that mediate binding to …

**Accessions** — [HGNC:6916](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6916) · Entrez [4152](https://www.ncbi.nlm.nih.gov/gene/4152) · UniProt [Q9UIS9](https://www.uniprot.org/uniprotkb/Q9UIS9) · Ensembl [ENSG00000141644](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141644)

## Data

Gene col 6560: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6560); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6560, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6560]; `tensor/DDL_lfc|DDL_z.npy` [6560]; `embed/gene_vectors.npy` [6560]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6560 or target_col == 6560). Every well: [[MBD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MBD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
