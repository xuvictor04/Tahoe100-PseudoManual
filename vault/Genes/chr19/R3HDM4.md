---
symbol: "R3HDM4"
type: "gene"
col: 12711
ensembl_id: "ENSG00000198858"
name: "R3H domain containing 4"
location: "19p13.3"
module: 2
arm: "+"
pooled_cpm: 19.26
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 17
n_dd_up_clean: 10
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# R3HDM4

*R3H domain containing 4* — 19p13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 1.76× (z +10.0, q 5e-21, up in 36 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.578× (z -13.8, q 1e-40, down in 40 of 46 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAMTSL5]] (+0.72, fdr 7e-06), [[RNF123]] (+0.68, fdr 1e-05), [[DVL1]] (+0.68, fdr 2e-05); moves opposite to [[HOXA6]] (-0.65, fdr 3e-05), [[PDHX]] (-0.61, fdr 4e-05), [[RPRD2]] (-0.61, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[APLN]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 6 with an alert ⚠; shown: the 15 strongest. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12711.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **1.76×** | +10.0 | 5e-21 | 36/48 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.55×** | +7.8 | 2e-12 | 32/48 (HS-578T, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.57×** | +7.4 | 2e-11 | 20/38 (A498, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.46×** | +6.7 | 3e-09 | 26/47 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.39×** | +5.9 | 4e-07 | 21/41 (LoVo, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.34×** | +5.1 | 4e-05 | 20/47 (AsPC-1, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.31×** | +4.8 | 2e-04 | 18/48 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.20×** | +4.7 | 2e-04 | 19/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.28×** | +4.3 | 9e-04 | 14/42 (C32, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~1% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.26×** | +4.1 | 0.003 | 18/46 (AsPC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.25×** | +3.9 | 0.004 | 16/46 (MIA PaCa-2, AsPC-1, …) | two highest doses | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.25×** | +3.8 | 0.006 | 17/42 (NCI-H460, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.22×** | +3.5 | 0.021 | 13/48 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.029 | 9/47 (LoVo, SW480, …) | two highest doses | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.0 | 0.094 | 14/47 (NCI-H460, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12711.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.578×** | -13.8 | 1e-40 | 40/46 (LoVo, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.698×** | -9.1 | 4e-17 | 32/48 (AsPC-1, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.705×** | -6.2 | 8e-08 | 24/48 (LoVo, LS 180, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.800×** | -4.9 | 1e-04 | 16/48 (SW480, LoVo, …) | rises with dose | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.763×** | -4.8 | 2e-04 | 23/48 (SHP-77, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.817×** | -4.4 | 9e-04 | 16/48 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Radotinib (drug)]] 5 µM |  | 0.844× | -4.3 | 0.002 | 15/48 (LoVo, hTERT-HPNE, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.638×** | -4.2 | 0.002 | 16/48 (LoVo, NCI-H23, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.830×** | -4.1 | 0.003 | 16/48 (SW480, HCT15, …) | all doses, flat | noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **0.792×** | -4.0 | 0.004 | 15/47 (SNU-423, A498, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.795×** | -3.9 | 0.004 | 15/42 (HCT15, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **0.804×** | -3.9 | 0.005 | 13/47 (LoVo, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.803×** | -3.7 | 0.010 | 10/47 (SW480, LoVo, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | 0.834× | -3.6 | 0.011 | 17/48 (SW480, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.824×** | -3.5 | 0.019 | 8/47 (BT-474, C-33 A, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.869× | -3.5 | 0.019 | 13/48 (SW480, LoVo, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12711. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 40.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -11.1) |
| [[SW480 (line)]] | alt | 24.7 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.341× (z -14.7) |
| [[A-427 (line)]] | wt | 16.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.259× (z -8.7) |
| [[AsPC-1 (line)]] | alt | 36.6 | 0 | 1 | — | [[Selinexor (drug)]] 5 µM 0.450× (z -9.5) |
| [[BT-474 (line)]] | alt | 19.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 14.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.334× (z -10.2) |
| [[HT-29 (line)]] | alt | 21.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.229× (z -13.4) |
| [[hTERT-HPNE (line)]] | wt | 14.3 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 5 µM 0.102× (z -9.9) |
| [[LoVo (line)]] | wt | 35.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -15.9) |
| [[LS 180 (line)]] | wt | 19.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -10.1) |
| [[SW1417 (line)]] | alt | 21.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -10.1) |
| [[SW48 (line)]] | wt | 26.7 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.171× (z -9.5) |
| [[A-172 (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 8.87 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12711), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAMTSL5]] | +0.72 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[RNF123]] | +0.68 | +0.54 / +0.59 | both halves | 1e-05 |  |
| [[DVL1]] | +0.68 | +0.66 / +0.48 | both halves | 2e-05 |  |
| [[PPP1R12C]] | +0.65 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[PLEC]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[PITPNM1]] | +0.62 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[ARHGDIA]] | +0.62 | +0.48 / +0.62 | both halves | 2e-05 |  |
| [[FAAP100]] | +0.61 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[NIBAN2]] | +0.61 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[FBRSL1]] | +0.60 | +0.63 / +0.46 | both halves | 3e-05 |  |
| [[GPRIN1]] | +0.60 | +0.51 / +0.38 | both halves | 7e-05 |  |
| [[KIAA0930]] | +0.60 | +0.52 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HOXA6]] | -0.65 | -0.43 / -0.66 | both halves | 3e-05 |  |
| [[PDHX]] | -0.61 | -0.53 / -0.41 | both halves | 4e-05 |  |
| [[RPRD2]] | -0.61 | -0.54 / -0.43 | both halves | 3e-05 |  |
| [[CHD6]] | -0.60 | -0.58 / -0.41 | both halves | 4e-05 |  |
| [[RAF1]] | -0.59 | -0.49 / -0.35 | both halves | 1e-04 |  |
| [[SLC16A14]] | -0.59 | -0.45 / -0.49 | both halves | 3e-05 |  |
| [[WBP11]] | -0.59 | -0.54 / -0.48 | both halves | 2e-05 |  |
| [[MAIP1]] | -0.58 | -0.52 / -0.36 | both halves | 9e-05 |  |
| [[ZCCHC8]] | -0.58 | -0.47 / -0.43 | both halves | 3e-05 |  |
| [[HOXA3]] | -0.57 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[ATP6V0D1-DT]] | -0.57 | -0.40 / -0.55 | both halves | 4e-05 |  |
| [[DNAJC27]] | -0.57 | -0.47 / -0.51 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APLN]] | B | APLN activity lowers R3HDM4's level | lines that do not express APLN (13) vs lines expressing it (37) | 1.36× higher at baseline in the lines without APLN | 0.023 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ZNF675]] | B | ZNF675 activity lowers R3HDM4's level | lines that do not express ZNF675 (5) vs lines expressing it (45) | 1.56× higher at baseline in the lines without ZNF675 | 0.030 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF573, ZNF420 |
| [[MAP2K1]] | B | MAP2K1 activity raises R3HDM4's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.1% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[KLF16]] | C | KLF16's natural level weakens R3HDM4's drug response | KLF16's natural level across 48 lines (lineage-adjusted; a glimpse) | r -0.66, reverse +0.07; direction not clear | 0.037 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.585). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (13.6, -3.6); signed map (-8.0, 30.8). **Vector** length 95.6, 20.0% of its response variance represented; |z| ≥ 3 in 938 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +5.2 | +10.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.0 | +7.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.6 | +6.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +5.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.8 | +2.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +4.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.3 | +1.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +3.4 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +2.1 | +1.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.4 | +2.6 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.5 | -13.8 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.3 | -9.1 |
|  | [[TAK-901 (drug)]] 5 µM |  | -5.5 | -4.2 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -4.1 | -4.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains <1% of this change | -4.0 | -3.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | -4.0 | -6.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | -2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.5 | -1.9 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.2 | -4.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -3.2 | -3.4 |

## What is on record

|  |  |
|---|---|
| Name | R3H domain containing 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.3 — chr19:896,503-913,245 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC16353; previously C19orf22 |
| Matched by | ensembl_id |

UniProt [Q96D70](https://www.uniprot.org/uniprotkb/Q96D70) carries no function annotation.

**Summary**, from NCBI Gene [91300](https://www.ncbi.nlm.nih.gov/gene/91300):

> Predicted to enable nucleic acid binding activity. Predicted to be located in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28270](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28270) · Entrez [91300](https://www.ncbi.nlm.nih.gov/gene/91300) · UniProt [Q96D70](https://www.uniprot.org/uniprotkb/Q96D70) · Ensembl [ENSG00000198858](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198858)

## Data

Gene col 12711: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12711); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12711, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12711]; `tensor/DDL_lfc|DDL_z.npy` [12711]; `embed/gene_vectors.npy` [12711]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12711 or target_col == 12711). Every well: [[R3HDM4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/R3HDM4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
