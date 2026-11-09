---
symbol: "ZNF7"
type: "gene"
col: 7220
ensembl_id: "ENSG00000147789"
name: "zinc finger protein 7"
location: "8q24.3"
module: 170
arm: "+"
pooled_cpm: 17.92
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 15
n_dd_up_clean: 7
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/170"]
generated_by: "tahoemap"
---

# ZNF7

*zinc finger protein 7* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 1.35× (z +5.4, q 4e-05, up in 22 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 0.458× (z -13.8, q 9e-41, down in 34 of 41 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.490× (z -12.6, q 2e-34, down in 39 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF3]] (+0.75, fdr 7e-06), [[ZSCAN32]] (+0.71, fdr 7e-06), [[MTG2]] (+0.69, fdr 7e-06); moves opposite to [[HMGN3]] (-0.56, fdr 1e-05), [[ZDHHC20]] (-0.56, fdr 2e-05), [[PLPP2]] (-0.56, fdr 4e-05).
> It sits in the **+** arm of [[Module 170]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[PLPP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7220.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.35×** | +5.4 | 4e-05 | 22/46 (A498, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.67×** | +4.8 | 5e-04 | 16/44 (KATO III, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +4.4 | 0.002 | 14/47 (RKO, NCI-H2347, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.59×** | +4.3 | 0.002 | 16/48 (LoVo, COLO 205, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +4.1 | 0.004 | 18/46 (KATO III, Panc 03.27, …) | top dose only |  |
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.7 | 0.021 | 11/47 (HOP62, NCI-H460, …) | top dose only | position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.022 | 8/47 (NCI-H1573, SW 900, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.20×** | +3.3 | 0.069 | 7/45 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 12 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7220.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.458×** | -13.8 | 9e-41 | 34/41 (LoVo, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.449×** | -13.7 | 5e-40 | 23/30 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.473×** | -12.8 | 4e-35 | 38/44 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.490×** | -12.6 | 2e-34 | 39/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.481×** | -12.0 | 4e-31 | 26/35 (AsPC-1, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.556×** | -10.4 | 2e-23 | 30/46 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.639×** | -7.9 | 2e-13 | 27/47 (H4, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.708×** | -6.1 | 8e-08 | 23/46 (SW480, COLO 205, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.724×** | -5.7 | 8e-07 | 22/46 (A-427, NCI-H23, …) | top dose only | position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.739×** | -5.1 | 2e-05 | 20/47 (NCI-H23, LOX-IMVI, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **0.820×** | -4.9 | 4e-05 | 23/48 (NCI-H460, LS 180, …) | rises with dose |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.674×** | -3.6 | 0.013 | 6/43 (A549, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~19% of this change | **0.816×** | -3.6 | 0.015 | 9/48 (AsPC-1, SW1417, …) | inconsistent across doses | position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.820×** | -3.5 | 0.020 | 14/48 (A-172, SK-MEL-2, …) | inconsistent across doses | position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.714×** | -3.1 | 0.070 | 13/38 (Panc 03.27, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Gefitinib (drug)]] 5 µM |  | 0.839× | -3.1 | 0.074 | 10/48 (NCI-H460, SW 900, …) | top dose only |  |
| [[LJI308 (drug)]] 0.05 µM |  | 0.834× | -3.0 | 0.084 | 6/46 (PANC-1, SNU-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.10 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7220. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 19.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.206× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.259× (z -10.5) |
| [[PANC-1 (line)]] | alt | 20.1 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.118× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.396× (z -8.5) |
| [[A-172 (line)]] | wt | 14.7 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.177× (z -11.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 18.4 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.277× (z -9.8) ⚠ toxic |
| [[A549 (line)]] | wt | 23.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.172× (z -12.9) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 16.6 | 0 | 2 | — | [[Digitoxin (drug)]] 0.5 µM 0.101× (z -10.1) |
| [[HEC-1-A (line)]] | alt | 12.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.149× (z -12.3) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 20.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.142× (z -12.5) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 16.1 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.196× (z -11.4) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[NCI-H2030 (line)]] | alt | 22.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0883× (z -16.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 11.5 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.178× (z -14.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 34.5 | 0 | 2 (2 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.176× (z -13.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 18.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.161× (z -9.7) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 22.3 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.230× (z -9.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 12.2 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.314× (z -9.9) |
| [[AsPC-1 (line)]] | alt | 22.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0931× (z -14.8) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 21.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.145× (z -11.3) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 20.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0819× (z -18.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 15.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -17.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 20.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.187× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 16.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0641× (z -16.6) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 27.3 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.244× (z -10.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H2347 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.283× (z -9.0) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 17.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.227× (z -10.6) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 27.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 15.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7220), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF3]] | +0.75 | +0.73 / +0.68 | both halves | 7e-06 | same gene group |
| [[ZSCAN32]] | +0.71 | +0.71 / +0.62 | both halves | 7e-06 | same gene group |
| [[MTG2]] | +0.69 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[ALKBH1]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[METTL13]] | +0.67 | +0.57 / +0.64 | both halves | 8e-06 |  |
| [[RPUSD2]] | +0.67 | +0.64 / +0.65 | both halves | 7e-06 |  |
| [[BMS1P4]] | +0.67 | +0.65 / +0.61 | both halves | 7e-06 |  |
| [[ZNF557]] | +0.66 | +0.67 / +0.54 | both halves | 1e-05 | same gene group |
| [[ZNF408]] | +0.66 | +0.68 / +0.55 | both halves | 1e-05 | same gene group |
| [[RRN3]] | +0.66 | +0.65 / +0.54 | both halves | 1e-05 |  |
| [[ZBTB49]] | +0.65 | +0.66 / +0.59 | both halves | 7e-06 | same gene group |
| [[RPP14]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HMGN3]] | -0.56 | -0.55 / -0.50 | both halves | 1e-05 |  |
| [[ZDHHC20]] | -0.56 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[PLPP2]] | -0.56 | -0.44 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLPP2]] | B | PLPP2 activity raises ZNF7's level | lines that do not express PLPP2 (8) vs lines expressing it (42) | 1.21× lower at baseline in the lines without PLPP2 | 0.042 | ⚠ within organs, on part of the lines; also absent: MAP3K21, C3orf52, REPS2 |
| [[RTKN2]] | B | RTKN2 activity lowers ZNF7's level | lines that do not express RTKN2 (7) vs lines expressing it (43) | 1.30× higher at baseline in the lines without RTKN2 | 0.084 | ⚠ within organs, on part of the lines; also absent: RUNDC3B, TENT5C, ENSG00000291112 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 170]]; 24 genes; this gene is in the **+** arm (projection on the module's main direction 0.674). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-43.3, 4.5); signed map (-5.2, -14.4). **Vector** length 84.9, 16.4% of its response variance represented; |z| ≥ 3 in 906 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.1 | +4.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.4 | +5.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.3 | +4.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +4.1 | +4.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.4 | +3.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +2.2 | +2.0 |
|  | [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | +1.8 | +3.7 |
| fall | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -6.2 | -12.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -6.0 | -13.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.3 | -13.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.1 | -4.9 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.5 | -10.4 |
|  | [[Gefitinib (drug)]] 5 µM |  | -2.4 | -3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.2 | +0.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -1.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.8 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | zinc finger protein 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:144,827,518-144,847,509 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KOX4, HF.16 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KRAB domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P17097](https://www.uniprot.org/uniprotkb/P17097) (Zinc finger protein 7):

> May be involved in transcriptional regulation.

**Summary**, from NCBI Gene [7553](https://www.ncbi.nlm.nih.gov/gene/7553):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in regulation of transcription by RNA polymerase II. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:13139](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13139) · Entrez [7553](https://www.ncbi.nlm.nih.gov/gene/7553) · UniProt [P17097](https://www.uniprot.org/uniprotkb/P17097) · Ensembl [ENSG00000147789](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000147789)

## Data

Gene col 7220: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7220); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7220, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7220]; `tensor/DDL_lfc|DDL_z.npy` [7220]; `embed/gene_vectors.npy` [7220]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7220 or target_col == 7220). Every well: [[ZNF7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZNF7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
