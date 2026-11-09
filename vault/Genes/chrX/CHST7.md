---
symbol: "CHST7"
type: "gene"
col: 7148
ensembl_id: "ENSG00000147119"
name: "carbohydrate sulfotransferase 7"
location: "Xp11.3"
module: 179
arm: "+"
pooled_cpm: 5.78
n_lines_expressing: 49
n_dd_up: 18
n_dd_down: 3
n_dd_up_clean: 14
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/179"]
generated_by: "tahoemap"
---

# CHST7

*carbohydrate sulfotransferase 7* — Xp11.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.72× (z +19.9, q 0e+00, up in 35 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Docetaxel (drug)]] 5 µM: 0.803× (z -4.4, q 0.007, down in 11 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Temsirolimus (drug)]] 0.5 µM in 2 lines (NCI-H460 0.0792×, CFPAC-1 0.101×); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 0.0955×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 0.113×; ⚠ toxic; transcription drop); [[Canagliflozin (drug)]] 5 µM in 1 line (A-172 0.0837×); [[Quinestrol (drug)]] 0.5 µM in 1 line (SW1417 0.0435×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMED7-TICAM2]] (+0.66, fdr 7e-06), [[GOLT1B]] (+0.64, fdr 2e-05), [[TICAM2]] (+0.63, fdr 1e-05); moves opposite to [[YTHDC2]] (-0.62, fdr 7e-05), [[TMEM126B]] (-0.54, fdr 2e-05), [[PIGO]] (-0.54, fdr 1e-04).
> It sits in the **+** arm of [[Module 179]] (RHOA GTPase cycle).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7148.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.72×** | +19.9 | 0e+00 | 35/39 (MIA PaCa-2, SW1417, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.05×** | +10.1 | 2e-21 | 26/46 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.04×** | +10.0 | 3e-21 | 26/40 (MIA PaCa-2, SW480, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.90×** | +8.7 | 6e-16 | 16/29 (NCI-H460, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.82×** | +8.1 | 6e-14 | 16/38 (NCI-H460, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.73×** | +7.7 | 1e-12 | 23/46 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.70×** | +7.5 | 6e-12 | 21/46 (PANC-1, A-172, …) | all doses, flat | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +7.1 | 9e-11 | 22/46 (LOX-IMVI, J82, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.66×** | +7.1 | 9e-11 | 22/46 (PANC-1, J82, …) | all doses, flat | cell-cycle shift (explains ~6% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +5.8 | 3e-07 | 14/37 (NCI-H460, SW480, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.6 | 8e-07 | 16/47 (HOP62, BT-474, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.47×** | +5.4 | 4e-06 | 16/35 (A549, A-172, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.08×** | +5.4 | 4e-06 | 5/12 (PANC-1, NCI-H2030, …) | rises with dose | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +5.2 | 9e-06 | 19/42 (LOX-IMVI, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.78×** | +4.2 | 9e-04 | 7/37 (MIA PaCa-2, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **1.58×** | +3.3 | 0.027 | 5/40 (MIA PaCa-2, A498, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.18× | +3.3 | 0.034 | 8/45 (SW480, hTERT-HPNE, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7148.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 7 here, 3 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Temsirolimus (drug)]] 0.5 µM in 2 lines (NCI-H460 0.0792×, CFPAC-1 0.101×); [[Dinaciclib (drug)]] 5 µM in 1 line (PANC-1 0.0955×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 1 line (HEC-1-A 0.113×; ⚠ toxic; transcription drop); [[Canagliflozin (drug)]] 5 µM in 1 line (A-172 0.0837×); [[Quinestrol (drug)]] 0.5 µM in 1 line (SW1417 0.0435×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Docetaxel (drug)]] 5 µM |  | **0.803×** | -4.4 | 0.007 | 11/47 (SHP-77, SW480, …) | rises with dose |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.747×** | -4.1 | 0.011 | 11/44 (NCI-H23, H4, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.753×** | -3.8 | 0.024 | 11/12 (PANC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belumosudil (drug)]] 5 µM |  | 0.791× | -3.2 | 0.22 | 9/39 (HEC-1-A, C32, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | 0.802× | -3.1 | 0.22 | 5/45 (NCI-H661, AN3 CA, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7148. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 5.44 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.07× (z +8.5) | [[Temsirolimus (drug)]] 0.5 µM 0.0792× (z -13.5) |
| [[SW1417 (line)]] | alt | 2.34 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.94× (z +8.5) | [[Quinestrol (drug)]] 0.5 µM 0.0435× (z -9.7) |
| [[A-172 (line)]] | wt | 6.09 | 0 | 1 | — | [[Canagliflozin (drug)]] 5 µM 0.0837× (z -10.4) |
| [[CFPAC-1 (line)]] | alt | 3.95 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.101× (z -9.1) |
| [[HEC-1-A (line)]] | alt | 8.34 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.113× (z -13.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 6.64 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.123× (z -10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 12.9 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 7.59 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0955× (z -15.8) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 7.39 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.05 µM 0.0746× (z -8.7) |
| [[A-427 (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.49 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 3.57 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.04 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.80 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.49 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 3.19 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.13 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.65 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.95 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.41 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.48 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7148), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMED7-TICAM2]] | +0.66 | +0.59 / +0.62 | both halves | 7e-06 |  |
| [[GOLT1B]] | +0.64 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[TICAM2]] | +0.63 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[PGM3]] | +0.63 | +0.49 / +0.62 | both halves | 1e-05 |  |
| [[DNAJC25]] | +0.61 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[RNF139-DT]] | +0.61 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[CDC20-DT]] | +0.61 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[METTL21EP-1]] | +0.59 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[TBC1D22A-DT]] | +0.59 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[HYPK]] | +0.58 | +0.48 / +0.59 | both halves | 2e-05 |  |
| [[MCEE]] | +0.57 | +0.59 / +0.53 | both halves | 1e-05 |  |
| [[C9orf153]] | +0.57 | +0.37 / +0.60 | both halves | 9e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[YTHDC2]] | -0.62 | -0.38 / -0.58 | both halves | 7e-05 |  |
| [[TMEM126B]] | -0.54 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[PIGO]] | -0.54 | -0.33 / -0.60 | both halves | 1e-04 |  |
| [[OCRL]] | -0.53 | -0.32 / -0.54 | both halves | 2e-04 |  |
| [[GFM1]] | -0.52 | -0.41 / -0.44 | both halves | 4e-05 |  |
| [[VPS13C]] | -0.52 | -0.29 / -0.56 | both halves | 2e-04 |  |
| [[ARAF]] | -0.52 | -0.24 / -0.56 | both halves | 5e-04 |  |
| [[BRD7]] | -0.51 | -0.38 / -0.57 | both halves | 7e-05 |  |
| [[FKTN]] | -0.51 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[VPS50]] | -0.51 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[CCDC113]] | -0.51 | -0.25 / -0.53 | both halves | 4e-04 |  |
| [[STX17]] | -0.50 | -0.35 / -0.53 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CHST7's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.6% of all compounds | 0.017 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 179]] — RHOA GTPase cycle; 22 genes; this gene is in the **+** arm (projection on the module's main direction 0.679). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (18.1, -29.9); signed map (-47.0, 10.7). **Vector** length 55.2, 7.02% of its response variance represented; |z| ≥ 3 in 1,053 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +19.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +10.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +7.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.4 | +5.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +8.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +5.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.0 | +1.6 |
| fall | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -3.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -1.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | +0.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -1.6 | -2.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -0.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.4 | +0.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -1.4 | -1.0 |
|  | [[Docetaxel (drug)]] 5 µM |  | -1.3 | -4.4 |

## What is on record

|  |  |
|---|---|
| Name | carbohydrate sulfotransferase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.3 — chrX:46,573,765-46,598,496 (+) |
| Ensembl biotype | protein_coding |
| Also known as | C6ST-2, C6ST2 |
| Gene groups (HGNC) | Sulfotransferases, membrane bound |
| Reactome | 4 pathways, smallest: CS-GAG biosynthesis; Chondroitin sulfate/dermatan sulfate metabolism; Glycosaminoglycan metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NS84](https://www.uniprot.org/uniprotkb/Q9NS84) (Carbohydrate sulfotransferase 7):

> Sulfotransferase that utilizes 3'-phospho-5'-adenylyl sulfate (PAPS) as sulfonate donor to catalyze the transfer of sulfate to position 6 of non-reducing N-acetylglucosamine (GlcNAc) residues. Preferentially acts on mannose-linked GlcNAc. Also able to catalyze the transfer of sulfate to position 6 of the N-acetylgalactosamine (GalNAc) residue of chondroitin. Also acts on core 2 mucin-type oligosaccharide and N-acetyllactosamine oligomer with a lower efficiency. Has weak or no activity toward …

**Summary**, from NCBI Gene [56548](https://www.ncbi.nlm.nih.gov/gene/56548):

> This gene is a member of the Gal/GalNAc/GlcNAc (galactose/N-acetylgalactosamine/N-acetylglucosamine) 6-O-sulfotransferase (GST) family. Members of this family encode enzymes that catalyze the specific addition of sulfate groups to distinct hydroxyl and amino groups of carbohydrates. The encoded protein catalyzes the sulfation of 6-hydroxyl group of GalNAc in chondroitin. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:13817](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13817) · Entrez [56548](https://www.ncbi.nlm.nih.gov/gene/56548) · UniProt [Q9NS84](https://www.uniprot.org/uniprotkb/Q9NS84) · Ensembl [ENSG00000147119](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147119)

## Data

Gene col 7148: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7148); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7148, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7148]; `tensor/DDL_lfc|DDL_z.npy` [7148]; `embed/gene_vectors.npy` [7148]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7148 or target_col == 7148). Every well: [[CHST7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHST7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
