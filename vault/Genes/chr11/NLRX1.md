---
symbol: "NLRX1"
type: "gene"
col: 8370
ensembl_id: "ENSG00000160703"
name: "NLR family member X1"
location: "11q23.3"
module: 46
arm: "+"
pooled_cpm: 7.51
n_lines_expressing: 48
n_dd_up: 6
n_dd_down: 19
n_dd_up_clean: 3
n_dd_down_clean: 14
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/046"]
generated_by: "tahoemap"
---

# NLRX1

*NLR family member X1* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Selinexor (drug)]] 5 µM: 1.27× (z +4.4, q 0.006, up in 9 of 43 measured lines) ⚠ cell-cycle shift, explains ~35% of this change. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.22× (z +3.7, q 0.024, up in 12 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.404× (z -11.9, q 5e-30, down in 34 of 45 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC16A14]] (+0.65, fdr 1e-05), [[RNF135]] (+0.64, fdr 3e-05), [[ATP6V0D1-DT]] (+0.61, fdr 1e-05); moves opposite to [[POLR2E]] (-0.52, fdr 0.001, ⚠ not reproduced), [[RSU1]] (-0.51, fdr 1e-04), [[USP9X]] (-0.51, fdr 4e-05), [[CAPZB]] (-0.50, fdr 8e-05).
> It sits in the **+** arm of [[Module 046]] (Chromatin modifying enzymes).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HOXA10]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8370.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **1.27×** | +4.4 | 0.006 | 9/43 (RKO, SW480, …) | rises with dose | low cells (technical?) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.35×** | +4.0 | 0.021 | 5/39 (A-172, A549, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.024 | 12/42 (LS 180, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Neratinib (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.024 | 5/44 (SW480, SW 900, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +3.7 | 0.024 | 8/43 (SW48, KATO III, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.30×** | +3.3 | 0.077 | 11/32 (SW1417, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | 1.27× | +3.1 | 0.15 | 9/45 (KATO III, NCI-H460, …) | two highest doses |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | 1.26× | +3.0 | 0.16 | 0/45 | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 5 with an alert ⚠. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8370.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.404×** | -11.9 | 5e-30 | 34/45 (NCI-H1573, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.421×** | -11.4 | 2e-27 | 30/44 (SW48, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.444×** | -10.7 | 3e-24 | 29/44 (NCI-H1573, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.505×** | -9.0 | 4e-17 | 24/43 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.543×** | -8.0 | 1e-13 | 22/45 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.544×** | -7.7 | 1e-12 | 22/35 (KATO III, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.585×** | -7.0 | 1e-10 | 26/43 (PANC-1, HEC-1-A, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.628×** | -6.1 | 8e-08 | 18/43 (MIA PaCa-2, NCI-H23, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.658×** | -5.5 | 2e-06 | 18/45 (SW480, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.672×** | -5.2 | 1e-05 | 15/40 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.786×** | -4.5 | 4e-04 | 18/40 (NCI-H1573, NCI-H460, …) | top dose only | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.725×** | -4.2 | 0.001 | 15/45 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **0.730×** | -4.1 | 0.002 | 14/28 (LoVo, HEC-1-A, …) | inconsistent across doses | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.731×** | -3.9 | 0.003 | 18/44 (NCI-H1573, PANC-1, …) | top dose only | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.582×** | -3.7 | 0.007 | 8/42 (NCI-H1573, MIA PaCa-2, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.754×** | -3.7 | 0.007 | 14/44 (PANC-1, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.607×** | -3.4 | 0.020 | 8/41 (SHP-77, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.759×** | -3.4 | 0.020 | 11/42 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.782×** | -3.0 | 0.069 | 5/42 (KATO III, SW1417, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8370. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 12.4 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.202× (z -12.4) |
| [[NCI-H1573 (line)]] | alt | 22.0 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0997× (z -22.5) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 0.0898× (z -8.7) |
| [[HEC-1-A (line)]] | alt | 12.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -11.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[SW480 (line)]] | alt | 8.60 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.138× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~56% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.226× (z -9.7) |
| [[A-172 (line)]] | wt | 5.93 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0921× (z -11.2) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 8.60 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.152× (z -8.9) ⚠ cell-cycle shift, explains ~61% of this change |
| [[KATO III (line)]] | alt | 11.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.146× (z -10.5) ⚠ toxic |
| [[LoVo (line)]] | wt | 8.78 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.160× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change |
| [[LS 180 (line)]] | wt | 7.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.73× (z +8.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.139× (z -10.0) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 5.18 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0768× (z -8.7) ⚠ toxic |
| [[SW48 (line)]] | wt | 9.30 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0435× (z -10.7) |
| [[A498 (line)]] | wt | 6.17 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.03 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.75 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.43 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.17 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.31 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.30 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.28 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.91 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.66 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 8.37 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.693 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.19 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8370), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC16A14]] | +0.65 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[RNF135]] | +0.64 | +0.46 / +0.64 | both halves | 3e-05 | pathway: DDX58/IFIH1-mediated induction of interferon-alpha/beta; STRING 635 |
| [[ATP6V0D1-DT]] | +0.61 | +0.53 / +0.59 | both halves | 1e-05 |  |
| [[ZBTB8A]] | +0.60 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[CSTF3-DT]] | +0.59 | +0.56 / +0.47 | both halves | 2e-05 |  |
| [[MTHFS]] | +0.59 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[RWDD3]] | +0.58 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[ZNF563]] | +0.57 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[DCP1B]] | +0.57 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[LINC02256]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[PAQR7]] | +0.57 | +0.39 / +0.61 | both halves | 6e-05 |  |
| [[URGCP]] | +0.57 | +0.46 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POLR2E]] | -0.52 | -0.17 / -0.46 | ⚠ not reproduced | 0.001 |  |
| [[RSU1]] | -0.51 | -0.40 / -0.34 | both halves | 1e-04 |  |
| [[USP9X]] | -0.51 | -0.42 / -0.52 | both halves | 4e-05 |  |
| [[CAPZB]] | -0.50 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[CHML]] | -0.50 | -0.36 / -0.43 | both halves | 1e-04 |  |
| [[SCART1]] | -0.50 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[CORO1C]] | -0.50 | -0.37 / -0.46 | both halves | 8e-05 |  |
| [[G6PD]] | -0.49 | -0.32 / -0.49 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA10]] | B | HOXA10 activity lowers NLRX1's level | lines that do not express HOXA10 (20) vs lines expressing it (30) | 1.14× higher at baseline in the lines without HOXA10 | 0.066 | ⚠ within organs, on part of the lines; also absent: HOXA9, HOXA10-AS, HOXA11 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 046]] — Chromatin modifying enzymes; 97 genes; this gene is in the **+** arm (projection on the module's main direction 0.512). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.30).
- **Nodal map** (x, y) = (-18.5, 24.1); signed map (-9.2, -5.9). **Vector** length 67.2, 11.3% of its response variance represented; |z| ≥ 3 in 863 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +5.4 | +3.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | +4.8 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.4 | +3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.5 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | -0.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +3.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +2.1 | +2.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.9 | +2.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.9 | +2.7 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.9 | -10.7 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.8 | -11.9 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.6 | -11.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.2 | -9.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.0 | -8.0 |
|  | [[Pimozide (drug)]] 5 µM |  | -1.5 | -1.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -7.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | -6.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.4 | -2.0 |
|  | [[Malotilate (drug)]] 0.05 µM |  | -1.3 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | NLR family member X1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:119,166,568-119,184,016 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NOD9, CLR11.3 |
| Gene groups (HGNC) | NLR family |
| Reactome | 25 pathways, smallest: Regulation of NF-kappa B signaling; Negative regulators of DDX58/IFIH1 signaling; TAK1-dependent IKK and NF-kappa-B activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q86UT6](https://www.uniprot.org/uniprotkb/Q86UT6) (NLR family member X1):

> Participates in antiviral signaling. Acts as a negative regulator of MAVS-mediated antiviral responses, through the inhibition of the virus-induced RLH (RIG-like helicase)-MAVS interaction. Instead, promotes autophagy by interacting with TUFM and subsequently recruiting the autophagy-related proteins ATG5 and ATG12. Also regulates MAVS-dependent NLRP3 inflammasome activation to attenuate apoptosis. Has no inhibitory function on NF-kappa-B signaling pathway, but enhances NF-kappa-B and JUN …

**Summary**, from NCBI Gene [79671](https://www.ncbi.nlm.nih.gov/gene/79671):

> The protein encoded by this gene is a member of the NLR family and localizes to the outer mitochondrial membrane. The encoded protein is a regulator of mitochondrial antivirus responses. Three transcript variants encoding the same protein have been found for this gene. [provided by RefSeq, Aug 2013]

**Accessions** — [HGNC:29890](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29890) · Entrez [79671](https://www.ncbi.nlm.nih.gov/gene/79671) · UniProt [Q86UT6](https://www.uniprot.org/uniprotkb/Q86UT6) · Ensembl [ENSG00000160703](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160703)

## Data

Gene col 8370: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8370); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8370, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8370]; `tensor/DDL_lfc|DDL_z.npy` [8370]; `embed/gene_vectors.npy` [8370]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8370 or target_col == 8370). Every well: [[NLRX1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NLRX1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
