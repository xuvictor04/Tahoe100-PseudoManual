---
symbol: "L3MBTL4"
type: "gene"
col: 7826
ensembl_id: "ENSG00000154655"
name: "L3MBTL histone methyl-lysine binding protein 4"
location: "18p11.31"
module: 121
arm: "+"
pooled_cpm: 36.55
n_lines_expressing: 24
n_dd_up: 22
n_dd_down: 11
n_dd_up_clean: 19
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 7
direction_downstream: 5
tags: ["gene", "module/121"]
generated_by: "tahoemap"
---

# L3MBTL4

*L3MBTL histone methyl-lysine binding protein 4* — 18p11.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.93× (z +14.2, q 4e-43, up in 16 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (5 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.621× (z -7.2, q 2e-10, down in 15 of 22 measured lines) ⚠ cell-cycle shift, explains ~33% of this change. The strongest without an alert is [[Belinostat (drug)]] 0.5 µM: 0.696× (z -5.5, q 1e-05, down in 15 of 22 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNF180]] (+0.68, fdr 7e-06), [[KCNT2]] (+0.64, fdr 7e-06), [[LINC01117]] (+0.63, fdr 1e-05); moves opposite to [[SNHG30]] (-0.55, fdr 1e-05), [[SHQ1]] (-0.54, fdr 1e-04), [[MLEC]] (-0.51, fdr 4e-05).
> It is in [[Module 121]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[GRIP1]] → it (grade B ⚠); 5 go from it, the strongest it → [[GRIP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7826.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.93×** | +14.2 | 4e-43 | 16/22 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.68×** | +11.3 | 4e-27 | 11/22 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.57×** | +6.9 | 8e-10 | 19/22 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.56×** | +6.8 | 1e-09 | 0/21 | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.55×** | +6.7 | 3e-09 | 11/22 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +6.0 | 2e-07 | 2/22 (NCI-H460, HCT15) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.45×** | +5.5 | 4e-06 | 16/22 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **1.42×** | +5.2 | 2e-05 | 16/21 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.35×** | +4.5 | 5e-04 | 1/17 (NCI-H460) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.34×** | +4.4 | 7e-04 | 13/21 (NCI-H1573, PANC-1, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.003 | 0/22 | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.27×** | +3.7 | 0.010 | 11/22 (SW 900, LoVo, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.031 | 8/22 (A-427, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.18× | +3.4 | 0.031 | 5/22 (C32, SW 900, …) | all doses, flat |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.25×** | +3.2 | 0.044 | 2/22 (NCI-H460, NCI-H1792) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.23×** | +3.2 | 0.044 | 4/22 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.23×** | +3.1 | 0.057 | 9/23 (A-427, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 5 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7826.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.621×** | -7.2 | 2e-10 | 15/22 (J82, A-427, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.696×** | -5.5 | 1e-05 | 15/22 (J82, A-427, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.732×** | -4.7 | 4e-04 | 13/22 (J82, SK-MEL-2, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.725×** | -4.7 | 4e-04 | 17/21 (C32, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.609×** | -3.9 | 0.009 | 13/22 (SK-MEL-2, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.620×** | -3.8 | 0.012 | 10/22 (J82, NCI-H1573, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.620×** | -3.8 | 0.012 | 16/23 (A-427, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.781×** | -3.8 | 0.012 | 13/22 (LoVo, Panc 03.27, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.792×** | -3.5 | 0.025 | 16/22 (SK-MEL-2, LoVo, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.809×** | -3.2 | 0.074 | 11/22 (NCI-H23, J82, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.745×** | -3.2 | 0.074 | 5/22 (PANC-1, J82, …) | inconsistent across doses | noisy plate (z scaled) |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | 0.865× | -3.1 | 0.093 | 1/23 (NCI-H460) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7826. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 182 | 1 | 11 (8 ⚠) | [[Harringtonine (drug)]] 5 µM 3.27× (z +11.0) | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.317× (z -11.2) |
| [[SK-MEL-2 (line)]] | alt | 226 | 0 | 12 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -16.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.433× (z -11.6) |
| [[J82 (line)]] | alt | 80.8 | 1 | 10 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.74× (z +12.1) | [[Panobinostat (drug)]] 0.5 µM 0.157× (z -15.8) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -14.8) |
| [[A-427 (line)]] | wt | 241 | 0 | 9 (7 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -19.5) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 0.100× (z -11.1) |
| [[PANC-1 (line)]] | alt | 33.4 | 3 | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +18.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.373× (z -11.4) |
| [[Panc 03.27 (line)]] | alt | 77.1 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.222× (z -11.1) ⚠ cell-cycle shift, explains ~71% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -10.4) |
| [[C32 (line)]] | wt | 131 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.224× (z -14.7) |
| [[H4 (line)]] | wt | 94.3 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.26× (z +10.3) | [[Dinaciclib (drug)]] 5 µM 0.0464× (z -18.2) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.316× (z -10.1) |
| [[A498 (line)]] | wt | 51.6 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.354× (z -10.4) |
| [[HOP62 (line)]] | alt | 16.9 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.0× (z +20.0) | — |
| [[NCI-H460 (line)]] | wt | 9.92 | 3 | 0 | [[Tucidinostat (drug)]] 5 µM 3.29× (z +10.2) | — |
| [[SNU-423 (line)]] | alt | 76.9 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 42.9 | 1 | 1 (1 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.47× (z +8.6) | [[Dinaciclib (drug)]] 0.5 µM 0.277× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H1792 (line)]] | alt | 147 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.246× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SW 900 (line)]] | alt | 34.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.80× (z +14.3) | — |
| [[NCI-H2030 (line)]] | alt | 12.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.101× (z -10.6) ⚠ toxic |
| [[A-172 (line)]] | wt | 3.21 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.83 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.95 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.38 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.57 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.18 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.78 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.99 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 4.50 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.78 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.11 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.05 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.82 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.03 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.45 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.41 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 35.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.73 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 3.25 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.33 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 44.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.75 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 3.74 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.95 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7826), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF180]] | +0.68 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[KCNT2]] | +0.64 | +0.58 / +0.59 | both halves | 7e-06 | same gene group |
| [[LINC01117]] | +0.63 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[LINC00383]] | +0.62 | +0.45 / +0.66 | both halves | 3e-05 |  |
| [[LINC00882]] | +0.62 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[ARNT2]] | +0.62 | +0.57 / +0.53 | both halves | 1e-05 | same gene group |
| [[LINC01725]] | +0.60 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[MSR1]] | +0.60 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[CPEB1]] | +0.59 | +0.62 / +0.53 | both halves | 1e-05 |  |
| [[ANKS1B]] | +0.58 | +0.59 / +0.47 | both halves | 2e-05 | same gene group |
| [[NLGN1]] | +0.58 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[SOX5]] | +0.58 | +0.37 / +0.66 | both halves | 8e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SNHG30]] | -0.55 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[SHQ1]] | -0.54 | -0.60 / -0.35 | both halves | 1e-04 |  |
| [[MLEC]] | -0.51 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[SDHAP4]] | -0.50 | -0.53 / -0.37 | both halves | 7e-05 |  |
| [[P3H1]] | -0.50 | -0.48 / -0.44 | both halves | 3e-05 |  |
| [[POGLUT2]] | -0.49 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[METTL9]] | -0.49 | -0.52 / -0.42 | both halves | 4e-05 |  |
| [[RNF121]] | -0.49 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[RNASET2]] | -0.48 | -0.48 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 2, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRIP1]] | B | GRIP1 activity raises L3MBTL4's level | lines that do not express GRIP1 (13) vs lines expressing it (37) | 3.66× lower at baseline in the lines without GRIP1 | 0.055 | ⚠ within organs, on part of the lines; also absent: PAX9; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers L3MBTL4's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.6% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds |
| [[LINC02055]] | C | LINC02055 activity raises L3MBTL4's level | lines that do not express LINC02055 (30) vs lines expressing it (20) | 3.02× lower at baseline in the lines without LINC02055 | 0.038 | ⚠ within organs, on part of the lines; also absent: BAGE2, LINC01446, ENSG00000234352; maybe low, not absent; co-absent with the target |
| [[ARNT2-DT]] | C | ARNT2-DT activity raises L3MBTL4's level | lines that do not express ARNT2-DT (27) vs lines expressing it (23) | 3.00× lower at baseline in the lines without ARNT2-DT | 0.039 | ⚠ within organs, on part of the lines; also absent: ARNT2, SOX11, ENSG00000233491; co-absent with the target |
| [[CHMP1B2P]] | C | CHMP1B2P activity raises L3MBTL4's level | lines that do not express CHMP1B2P (31) vs lines expressing it (19) | 3.84× lower at baseline in the lines without CHMP1B2P | 0.042 | ⚠ within organs, on part of the lines; also absent: LINC01242, LINC00648, BHMT2; co-absent with the target |
| [[CNTNAP3]] | C | CNTNAP3 activity raises L3MBTL4's level | lines that do not express CNTNAP3 (25) vs lines expressing it (25) | 2.44× lower at baseline in the lines without CNTNAP3 | 0.057 | ⚠ within organs, on part of the lines; also absent: CNTNAP3C, CNTNAP3B, CNTNAP3P2; co-absent with the target |
| [[LINC01029]] | C | LINC01029 activity raises L3MBTL4's level | lines that do not express LINC01029 (42) vs lines expressing it (8) | 3.60× lower at baseline in the lines without LINC01029 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, LINC00879, OVAAL; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GRIP1]] | B | L3MBTL4 activity raises GRIP1's level | lines that do not express L3MBTL4 (26) vs lines expressing it (24) | 2.30× lower at baseline in the lines without L3MBTL4 | 0.026 | ⚠ within organs, on part of the lines; also absent: FGF14, SNCA, BASP1-AS1 |
| [[TRIM16L-1]] | B | L3MBTL4 activity raises TRIM16L-1's level | lines that do not express L3MBTL4 (26) vs lines expressing it (24) | 1.95× lower at baseline in the lines without L3MBTL4 | 0.036 | ⚠ within organs, on part of the lines; also absent: FGF14, SNCA, BASP1-AS1 |
| [[SNHG30]] | B | L3MBTL4 activity raises SNHG30's level | lines that do not express L3MBTL4 (26) vs lines expressing it (24) | 1.22× lower at baseline in the lines without L3MBTL4 | 0.069 | ⚠ within organs, on part of the lines; also absent: FGF14, SNCA, BASP1-AS1 |
| [[ARNT2]] | C | L3MBTL4 activity raises ARNT2's level | lines that do not express L3MBTL4 (26) vs lines expressing it (24) | 2.90× lower at baseline in the lines without L3MBTL4 | 0.013 | ⚠ within organs, on part of the lines; also absent: FGF14, SNCA, BASP1-AS1; co-absent with the target |
| [[FGF13]] | C | L3MBTL4 activity raises FGF13's level | lines that do not express L3MBTL4 (26) vs lines expressing it (24) | 3.39× lower at baseline in the lines without L3MBTL4 | 0.098 | ⚠ within organs, on part of the lines; also absent: FGF14, SNCA, BASP1-AS1; co-absent with the target |

## Where it sits

- **Module**: [[Module 121]]; 41 genes; every member is in the + arm (projection on the module's main direction 0.709). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (44.9, 27.5); signed map (45.8, 25.9). **Vector** length 84.9, 26.5% of its response variance represented; |z| ≥ 3 in 638 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +7.3 | +14.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.7 | +4.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +6.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +11.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.7 | +6.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +3.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.6 | +4.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.6 | +5.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.4 | +3.4 |
| fall | [[PH-797804 (drug)]] 5 µM |  | -2.8 | -3.9 |
|  | [[TAK-901 (drug)]] 5 µM |  | -2.4 | -3.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -2.3 | -3.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.3 | -2.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -2.6 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -1.9 | -0.9 |
|  | [[Goserelin (acetate) (drug)]] 5 µM |  | -1.8 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | L3MBTL histone methyl-lysine binding protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18p11.31 — chr18:5,954,706-6,415,237 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ35936, HsT1031 |
| Gene groups (HGNC) | Sterile alpha motif domain containing; Zinc fingers C2H2C-type; MBT domain containing; MicroRNA protein coding host genes |
| Hallmark sets | COMPLEMENT |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NA19](https://www.uniprot.org/uniprotkb/Q8NA19) (Lethal(3)malignant brain tumor-like protein 4):

> Putative Polycomb group (PcG) protein. PcG proteins maintain the transcriptionally repressive state of genes, probably via a modification of chromatin, rendering it heritably changed in its expressibility (By similarity).

**Summary**, from NCBI Gene [91133](https://www.ncbi.nlm.nih.gov/gene/91133):

> Predicted to enable chromatin binding activity and histone binding activity. Predicted to be involved in negative regulation of DNA-templated transcription. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26677](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26677) · Entrez [91133](https://www.ncbi.nlm.nih.gov/gene/91133) · UniProt [Q8NA19](https://www.uniprot.org/uniprotkb/Q8NA19) · Ensembl [ENSG00000154655](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154655)

## Data

Gene col 7826: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7826); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7826, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7826]; `tensor/DDL_lfc|DDL_z.npy` [7826]; `embed/gene_vectors.npy` [7826]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7826 or target_col == 7826). Every well: [[L3MBTL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/L3MBTL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
