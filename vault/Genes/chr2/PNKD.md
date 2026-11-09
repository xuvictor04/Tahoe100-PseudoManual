---
symbol: "PNKD"
type: "gene"
col: 4836
ensembl_id: "ENSG00000127838"
name: "PNKD metallo-beta-lactamase domain containing"
location: "2q35"
module: 45
arm: "+"
pooled_cpm: 20.48
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# PNKD

*PNKD metallo-beta-lactamase domain containing* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.86× (z +12.2, q 1e-31, up in 37 of 40 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Panobinostat (drug)]] 0.5 µM: 1.65× (z +5.8, q 1e-06, up in 30 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.584× (z -6.3, q 2e-07, down in 27 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AHDC1]] (+0.71, fdr 1e-05), [[THRA]] (+0.71, fdr 7e-06), [[PLEKHH3]] (+0.67, fdr 1e-05); moves opposite to [[ENOX2]] (-0.66, fdr 1e-05), [[LINC01829]] (-0.60, fdr 3e-05), [[ITPRIPL2]] (-0.60, fdr 3e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[NCMAP]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4836.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.86×** | +12.2 | 1e-31 | 37/40 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.69×** | +11.1 | 5e-26 | 27/33 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.65×** | +5.8 | 1e-06 | 30/48 (NCI-H2030, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.57×** | +5.2 | 3e-05 | 25/48 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.54×** | +5.0 | 5e-05 | 34/46 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.7 | 3e-04 | 23/44 (NCI-H1573, SW1417, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **1.48×** | +4.6 | 4e-04 | 25/47 (MIA PaCa-2, NCI-H2030, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.61×** | +4.4 | 7e-04 | 25/37 (LoVo, NCI-H2030, …) | all doses, stronger at high dose | composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.43×** | +4.2 | 0.002 | 23/44 (CFPAC-1, SW1417, …) | inconsistent across doses | low cells (technical?) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +3.4 | 0.040 | 20/48 (RKO, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.53×** | +3.4 | 0.041 | 16/45 (PANC-1, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.33×** | +3.3 | 0.048 | 14/47 (NCI-H460, A498, …) | top dose only |  |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.51×** | +3.3 | 0.048 | 14/47 (AN3 CA, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.50×** | +3.2 | 0.050 | 12/46 (Hs 766T, A498, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.50×** | +3.2 | 0.053 | 14/48 (PANC-1, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.46×** | +3.0 | 0.099 | 11/44 (SHP-77, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 4836.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.584×** | -6.3 | 2e-07 | 27/46 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.684×** | -4.5 | 0.002 | 20/48 (NCI-H460, LoVo, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.684×** | -4.5 | 0.002 | 23/47 (HT-29, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.711×** | -4.0 | 0.009 | 21/47 (KATO III, HT-29, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.808×** | -3.5 | 0.045 | 15/48 (A-427, A498, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.819×** | -3.3 | 0.087 | 22/47 (KATO III, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.715× | -3.1 | 0.13 | 7/47 (LoVo, SW480, …) | inconsistent across doses | noisy plate (z scaled) |
| [[GSK1059615 (drug)]] 5 µM |  | 0.581× | -3.1 | 0.13 | 6/46 (BT-474, KATO III, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.14 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4836. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 25.3 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 7.78× (z +12.6) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 26.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.93× (z +10.6) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 32.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -14.9) |
| [[LoVo (line)]] | wt | 18.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 15.1× (z +17.6) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 30.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.60× (z +13.1) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 12.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.75× (z +10.7) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 26.7 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.18× (z +9.4) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 25.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -13.7) |
| [[A-172 (line)]] | wt | 21.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +8.5) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 20.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.55× (z +9.0) ⚠ toxic; transcription drop | — |
| [[C32 (line)]] | wt | 21.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.40× (z +11.0) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 17.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.202× (z -11.2) |
| [[LS 180 (line)]] | wt | 24.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.14× (z +9.4) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 18.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.32× (z +9.0) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 13.4 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.0613× (z -9.5) |
| [[SW1417 (line)]] | alt | 27.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.95× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 30.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 37.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4836), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*71 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHDC1]] | +0.71 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[THRA]] | +0.71 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[PLEKHH3]] | +0.67 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[TMEM63C]] | +0.64 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[MPND]] | +0.63 | +0.53 / +0.44 | both halves | 3e-05 |  |
| [[TNNI3]] | +0.62 | +0.56 / +0.51 | both halves | 1e-05 |  |
| [[SLC25A23]] | +0.62 | +0.52 / +0.48 | both halves | 2e-05 |  |
| [[OSBPL7]] | +0.62 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[NRTN]] | +0.62 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[MAPK3]] | +0.62 | +0.60 / +0.47 | both halves | 2e-05 | STRING 401 |
| [[GALM]] | +0.61 | +0.46 / +0.58 | both halves | 3e-05 |  |
| [[AGFG2]] | +0.61 | +0.46 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*29 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENOX2]] | -0.66 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[LINC01829]] | -0.60 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[ITPRIPL2]] | -0.60 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[SPOPL-DT]] | -0.60 | -0.52 / -0.51 | both halves | 1e-05 |  |
| [[PRDM5]] | -0.60 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[DNAJC11]] | -0.60 | -0.55 / -0.47 | both halves | 2e-05 |  |
| [[ERCC6L2]] | -0.59 | -0.53 / -0.38 | both halves | 6e-05 |  |
| [[MED1]] | -0.59 | -0.54 / -0.44 | both halves | 3e-05 |  |
| [[AVEN]] | -0.59 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[CPSF2]] | -0.59 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[CSTF3]] | -0.58 | -0.54 / -0.38 | both halves | 7e-05 |  |
| [[TRMT5]] | -0.58 | -0.53 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NCMAP]] | B | NCMAP activity raises PNKD's level | lines that do not express NCMAP (26) vs lines expressing it (24) | 1.31× lower at baseline in the lines without NCMAP | 0.022 | ⚠ within organs, on part of the lines; also absent: TC2N, CRB3, SPINT1-AS1; maybe low, not absent |
| [[LINC00482]] | B | LINC00482 activity raises PNKD's level | lines that do not express LINC00482 (8) vs lines expressing it (42) | 1.27× lower at baseline in the lines without LINC00482 | 0.068 | ⚠ within organs, on part of the lines; also absent: SOX13, SEPTIN9-DT |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.663). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (8.2, -5.2); signed map (-28.0, -5.5). **Vector** length 76.7, 17.2% of its response variance represented; |z| ≥ 3 in 706 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Belinostat (drug)]] 0.5 µM |  | +3.5 | +5.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +12.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | +3.3 | +4.6 |
|  | [[Panobinostat (drug)]] 5 µM |  | +3.1 | +5.2 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +3.0 | +3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.7 | +3.4 |
|  | [[Radotinib (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.8 | +0.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.7 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.7 | -6.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | -2.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.2 | -4.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.1 | -2.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.7 | -4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -3.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.5 | -1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.3 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | PNKD metallo-beta-lactamase domain containing |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:218,269,651-218,346,793 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DYT8, PDC, DKFZp564N1362, FPD1, MR-1, BRP17, FKSG19, TAHCCP2 |
| Gene groups (HGNC) | Mitochondrial respiratory chain complex assembly factors; MBL domain containing glyoxalase 2 subfamily; MicroRNA protein coding host genes |
| Reactome | 3 pathways, smallest: Complex IV assembly; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N490](https://www.uniprot.org/uniprotkb/Q8N490) (Probable thioesterase PNKD):

> Probable thioesterase that may play a role in cellular detoxification processes; it likely acts on a yet-unknown alpha-hydroxythioester substrate (Probable). In vitro, it is able to catalyze the hydrolysis of S-D-lactoyl-glutathione to form glutathione and D-lactic acid at very low rate, though this reaction is not physiologically relevant in vivo.; [Isoform 2]: Involved in the mitochondrial complex IV biogenesis.

**Summary**, from NCBI Gene [25953](https://www.ncbi.nlm.nih.gov/gene/25953):

> This gene is thought to play a role in the regulation of myofibrillogenesis. Mutations in this gene have been associated with the movement disorder paroxysmal non-kinesigenic dyskinesia. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:9153](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9153) · Entrez [25953](https://www.ncbi.nlm.nih.gov/gene/25953) · UniProt [Q8N490](https://www.uniprot.org/uniprotkb/Q8N490) · Ensembl [ENSG00000127838](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000127838)

## Data

Gene col 4836: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4836); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4836, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4836]; `tensor/DDL_lfc|DDL_z.npy` [4836]; `embed/gene_vectors.npy` [4836]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4836 or target_col == 4836). Every well: [[PNKD — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PNKD.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
