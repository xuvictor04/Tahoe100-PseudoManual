---
symbol: "TUT1"
type: "gene"
col: 7334
ensembl_id: "ENSG00000149016"
name: "terminal uridylyl transferase 1, U6 snRNA-specific"
location: "11q12.3"
module: 170
arm: "+"
pooled_cpm: 9.6
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/170"]
generated_by: "tahoemap"
---

# TUT1

*terminal uridylyl transferase 1, U6 snRNA-specific* — 11q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.56× (z +19.4, q 0e+00, up in 43 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.669× (z -5.9, q 2e-06, down in 19 of 33 measured lines) ⚠ toxic; transcription drop.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.116×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 0.267×; ⚠ toxic; transcription drop); [[Chlorhexidine (diacetate) (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0438×); [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (HCT15 0.0984×); [[Bosentan (hydrate) (drug)]] 0.05 µM in 1 line (COLO 205 0.0838×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF7]] (+0.64, fdr 3e-05), [[METTL25B]] (+0.63, fdr 1e-05), [[ELP3]] (+0.62, fdr 1e-05); moves opposite to [[MAPK9]] (-0.52, fdr 2e-04), [[STAU2]] (-0.51, fdr 1e-04), [[SFXN5]] (-0.50, fdr 6e-05).
> It sits in the **+** arm of [[Module 170]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7334.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.56×** | +19.4 | 0e+00 | 43/45 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.46×** | +13.2 | 4e-37 | 36/42 (NCI-H1573, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **3.89×** | +10.4 | 6e-23 | 38/46 (PANC-1, LoVo, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~2% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.95×** | +9.8 | 2e-20 | 32/47 (LOX-IMVI, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.96×** | +9.4 | 4e-19 | 35/46 (AsPC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **1.87×** | +9.1 | 7e-18 | 35/47 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.85×** | +9.0 | 2e-17 | 29/47 (MIA PaCa-2, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.63×** | +7.4 | 1e-11 | 25/43 (SW480, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +6.1 | 7e-08 | 20/40 (SW1417, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.31×** | +5.6 | 1e-06 | 23/44 (AsPC-1, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +5.2 | 8e-06 | 22/46 (NCI-H460, A-427, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.38×** | +4.7 | 1e-04 | 15/41 (NCI-H460, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.37×** | +4.4 | 5e-04 | 15/45 (HOP62, SW480, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.20× | +3.7 | 0.007 | 14/48 (PANC-1, J82, …) | top dose only | low cells (technical?); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.7 | 0.008 | 12/45 (NCI-H460, SNU-1, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.015 | 11/46 (PANC-1, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~11% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7334.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 1 line (NCI-H2030 0.116×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SW480 0.267×; ⚠ toxic; transcription drop); [[Chlorhexidine (diacetate) (drug)]] 0.5 µM in 1 line (hTERT-HPNE 0.0438×); [[Fluvoxamine (maleate) (drug)]] 0.5 µM in 1 line (HCT15 0.0984×); [[Bosentan (hydrate) (drug)]] 0.05 µM in 1 line (COLO 205 0.0838×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.669×** | -5.9 | 2e-06 | 19/33 (SW480, HS-578T, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | 0.777× | -3.5 | 0.11 | 10/17 (SW480, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Busulfan (drug)]] 5 µM |  | 0.847× | -3.4 | 0.11 | 8/48 (Hs 766T, AN3 CA, …) | inconsistent across doses |  |
| [[Carbamazepine (drug)]] 5 µM |  | 0.796× | -3.3 | 0.12 | 5/47 (NCI-H2347, A-172, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | 0.864× | -3.0 | 0.24 | 13/48 (RPMI-7951, SW1417, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7334. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 8.99 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.74× (z +11.2) | — |
| [[NCI-H2030 (line)]] | alt | 13.2 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.02× (z +12.2) | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -12.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[PANC-1 (line)]] | alt | 14.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.91× (z +11.3) | — |
| [[A549 (line)]] | wt | 8.70 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.17× (z +9.0) | — |
| [[COLO 205 (line)]] | alt | 8.15 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.0838× (z -8.7) |
| [[HCT15 (line)]] | alt | 11.2 | 0 | 1 | — | [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.0984× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 6.72 | 0 | 1 | — | [[Chlorhexidine (diacetate) (drug)]] 0.5 µM 0.0438× (z -10.0) |
| [[LoVo (line)]] | wt | 8.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +10.5) | — |
| [[NCI-H460 (line)]] | wt | 5.99 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +10.0) | — |
| [[SW480 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.267× (z -10.8) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 7.25 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.82 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.69 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 6.55 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.11 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.57 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.55 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.68 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.05 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.80 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7334), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF7]] | +0.64 | +0.68 / +0.46 | both halves | 3e-05 |  |
| [[METTL25B]] | +0.63 | +0.69 / +0.49 | both halves | 1e-05 |  |
| [[ELP3]] | +0.62 | +0.66 / +0.50 | both halves | 1e-05 |  |
| [[KCTD18]] | +0.62 | +0.67 / +0.57 | both halves | 1e-05 |  |
| [[ZNF18]] | +0.62 | +0.70 / +0.61 | both halves | 7e-06 |  |
| [[ZNF550]] | +0.62 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[SEPSECS]] | +0.61 | +0.65 / +0.57 | both halves | 9e-06 |  |
| [[RUSF1]] | +0.60 | +0.58 / +0.43 | both halves | 3e-05 |  |
| [[GIN1]] | +0.60 | +0.67 / +0.47 | both halves | 2e-05 |  |
| [[PYM1]] | +0.60 | +0.64 / +0.49 | both halves | 1e-05 |  |
| [[ZNF230]] | +0.60 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[TJAP1]] | +0.59 | +0.63 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK9]] | -0.52 | -0.66 / -0.29 | both halves | 2e-04 |  |
| [[STAU2]] | -0.51 | -0.43 / -0.33 | both halves | 1e-04 |  |
| [[SFXN5]] | -0.50 | -0.39 / -0.54 | both halves | 6e-05 |  |
| [[PTK2]] | -0.50 | -0.57 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers TUT1's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.4% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 170]]; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.694). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-29.4, 0.2); signed map (-13.3, -14.9). **Vector** length 61.5, 9.05% of its response variance represented; |z| ≥ 3 in 1,017 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.8 | +13.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +19.4 |
|  | [[TAK-901 (drug)]] 5 µM |  | +3.1 | +10.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.7 | +7.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.6 | +9.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.9 | +3.7 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +1.6 | +2.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | +1.3 | +2.7 |
|  | [[Vortioxetine (drug)]] 0.5 µM |  | +1.2 | +0.4 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.5 | -0.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.4 | -5.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.2 | -2.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -3.2 | -1.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.2 | -3.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -1.5 | -0.2 |
|  | [[Adagrasib (drug)]] 5 µM |  | -1.5 | -2.7 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[EX229 (drug)]] 5 µM |  | -1.4 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | terminal uridylyl transferase 1, U6 snRNA-specific |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.3 — chr11:62,575,045-62,591,637 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22347, FLJ22267, FLJ21850, PAPD2, TUTase, TENT1; previously RBM21 |
| Gene groups (HGNC) | RNA binding motif containing; Non-canonical poly(A) polymerases; Terminal nucleotidyltransferases |
| Reactome | 4 pathways, smallest: mRNA Polyadenylation; mRNA 3'-end processing; Processing of Capped Intron-Containing Pre-mRNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6E5](https://www.uniprot.org/uniprotkb/Q9H6E5) (Speckle targeted PIP5K1A-regulated poly(A) polymerase):

> Poly(A) polymerase that creates the 3'-poly(A) tail of specific pre-mRNAs. Localizes to nuclear speckles together with PIP5K1A and mediates polyadenylation of a select set of mRNAs, such as HMOX1. In addition to polyadenylation, it is also required for the 3'-end cleavage of pre-mRNAs: binds to the 3'UTR of targeted pre-mRNAs and promotes the recruitment and assembly of the CPSF complex on the 3'UTR of pre-mRNAs. In addition to adenylyltransferase activity, also has uridylyltransferase …

**Summary**, from NCBI Gene [64852](https://www.ncbi.nlm.nih.gov/gene/64852):

> This gene encodes a nucleotidyl transferase that functions as both a terminal uridylyltransferase and a nuclear poly(A) polymerase. The encoded enzyme specifically adds and removes nucleotides from the 3' end of small nuclear RNAs and select mRNAs and may function in controlling gene expression and cell proliferation.[provided by RefSeq, Apr 2009]

**Accessions** — [HGNC:26184](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26184) · Entrez [64852](https://www.ncbi.nlm.nih.gov/gene/64852) · UniProt [Q9H6E5](https://www.uniprot.org/uniprotkb/Q9H6E5) · Ensembl [ENSG00000149016](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000149016)

## Data

Gene col 7334: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7334); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7334, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7334]; `tensor/DDL_lfc|DDL_z.npy` [7334]; `embed/gene_vectors.npy` [7334]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7334 or target_col == 7334). Every well: [[TUT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
