---
symbol: "CEP170B"
type: "gene"
col: 1816
ensembl_id: "ENSG00000099814"
name: "centrosomal protein 170B"
location: "14q32.33"
module: 2
arm: "+"
pooled_cpm: 18.45
n_lines_expressing: 50
n_dd_up: 28
n_dd_down: 5
n_dd_up_clean: 21
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# CEP170B

*centrosomal protein 170B* — 14q32.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.29× (z +9.2, q 2e-17, up in 34 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 2.16× (z +8.5, q 4e-15, up in 42 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.670× (z -4.5, q 0.004, down in 23 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[KLC2]] (+0.68, fdr 7e-06), [[RHBDF1]] (+0.68, fdr 7e-06), [[RNF123]] (+0.67, fdr 7e-06); moves opposite to [[MTF2]] (-0.61, fdr 1e-05), [[ILF3-DT]] (-0.59, fdr 1e-05), [[HOXA5]] (-0.56, fdr 3e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HOXA5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1816.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.29×** | +9.2 | 2e-17 | 34/38 (LoVo, SW1417, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.16×** | +8.5 | 4e-15 | 42/47 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.70×** | +8.3 | 2e-14 | 31/47 (NCI-H1573, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.17×** | +8.1 | 8e-14 | 40/46 (NCI-H460, NCI-H2030, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.06×** | +8.0 | 1e-13 | 38/47 (SW480, Panc 03.27, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.17×** | +7.9 | 2e-13 | 27/35 (SW1417, C32, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.05×** | +7.7 | 2e-12 | 27/32 (NCI-H1792, KATO III, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.97×** | +7.5 | 4e-12 | 37/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~25% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.91×** | +7.2 | 5e-11 | 33/47 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +5.8 | 4e-07 | 25/47 (NCI-H460, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.66×** | +5.6 | 9e-07 | 28/48 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.52×** | +4.6 | 2e-04 | 26/47 (SW480, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.48×** | +4.3 | 7e-04 | 23/47 (SW480, BT-474, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +3.9 | 0.004 | 20/42 (NCI-H1792, C32, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.005 | 22/47 (HOP62, SW480, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +3.7 | 0.007 | 17/47 (CFPAC-1, SW480, …) | top dose only | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.39×** | +3.5 | 0.015 | 17/46 (LoVo, NCI-H1792, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.34×** | +3.3 | 0.031 | 17/47 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.36×** | +3.3 | 0.031 | 17/45 (HS-578T, A-172, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.032 | 15/44 (SW 900, SK-MEL-2, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1816.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.670×** | -4.5 | 0.004 | 23/46 (LoVo, HT-29, …) | two highest doses | cell-cycle shift (explains ~11% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.704×** | -3.8 | 0.045 | 22/46 (HepG2/C3A, Panc 03.27, …) | inconsistent across doses | position effect removed |
| [[Bosentan (hydrate) (drug)]] 0.5 µM |  | **0.720×** | -3.7 | 0.045 | 18/47 (SW48, LS 180, …) | inconsistent across doses | position effect removed |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.545×** | -3.5 | 0.056 | 14/43 (Hs 766T, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.809×** | -3.4 | 0.083 | 20/48 (KATO III, LoVo, …) | two highest doses | position effect removed |
| [[Afatinib (drug)]] 0.05 µM |  | 0.810× | -3.1 | 0.17 | 22/47 (HEC-1-A, BT-474, …) | inconsistent across doses | position effect removed |
| [[Arbutin (drug)]] 5 µM |  | 0.755× | -3.0 | 0.18 | 14/47 (C32, Panc 03.27, …) | top dose only | position effect removed |
| [[Selinexor (drug)]] 5 µM |  | 0.827× | -3.0 | 0.18 | 19/48 (CFPAC-1, AsPC-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.35 per unit of S-phase module lfc, -0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1816. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.60 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.85× (z +9.9) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[SW480 (line)]] | alt | 21.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.67× (z +9.4) | — |
| [[A549 (line)]] | wt | 13.5 | 1 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.39× (z +10.5) ⚠ cell-cycle shift, explains ~42% of this change | — |
| [[AsPC-1 (line)]] | alt | 22.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.72× (z +10.1) | — |
| [[CFPAC-1 (line)]] | alt | 16.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.14× (z +9.3) | — |
| [[HepG2_C3A (line)]] | wt | 15.0 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0631× (z -10.2) |
| [[hTERT-HPNE (line)]] | wt | 12.2 | 0 | 1 | — | [[Vandetanib (drug)]] 0.5 µM 0.0918× (z -9.7) |
| [[NCI-H1573 (line)]] | alt | 18.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.67× (z +10.7) | — |
| [[A-172 (line)]] | wt | 18.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 23.8 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.44 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 33.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.91 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.11 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.40 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 60.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1816), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KLC2]] | +0.68 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[RHBDF1]] | +0.68 | +0.67 / +0.66 | both halves | 7e-06 |  |
| [[RNF123]] | +0.67 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[POLR2J3]] | +0.67 | +0.52 / +0.65 | both halves | 1e-05 |  |
| [[BRD9]] | +0.65 | +0.57 / +0.66 | both halves | 1e-05 |  |
| [[FLII]] | +0.64 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[DBN1]] | +0.64 | +0.58 / +0.66 | both halves | 7e-06 |  |
| [[DMWD]] | +0.64 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[DBNL]] | +0.64 | +0.51 / +0.69 | both halves | 1e-05 |  |
| [[FAAP100]] | +0.63 | +0.58 / +0.67 | both halves | 7e-06 |  |
| [[KIF1C]] | +0.61 | +0.50 / +0.64 | both halves | 1e-05 |  |
| [[MICAL1]] | +0.61 | +0.63 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MTF2]] | -0.61 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[ILF3-DT]] | -0.59 | -0.53 / -0.59 | both halves | 1e-05 |  |
| [[HOXA5]] | -0.56 | -0.45 / -0.61 | both halves | 3e-05 |  |
| [[TRIM7-AS2]] | -0.56 | -0.55 / -0.53 | both halves | 1e-05 |  |
| [[DPM3]] | -0.55 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[AFTPH]] | -0.55 | -0.45 / -0.59 | both halves | 3e-05 |  |
| [[RNF145]] | -0.54 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[SLC11A2]] | -0.52 | -0.48 / -0.50 | both halves | 2e-05 |  |
| [[TRA2A]] | -0.52 | -0.38 / -0.53 | both halves | 6e-05 |  |
| [[MRPL44]] | -0.52 | -0.39 / -0.54 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA5]] | B | HOXA5 activity lowers CEP170B's level | lines that do not express HOXA5 (9) vs lines expressing it (41) | 1.21× higher at baseline in the lines without HOXA5 | 0.075 | ⚠ within organs, on part of the lines; also absent: HOXA3, HOXA6, HOTAIRM1 |
| [[PLEC]] | C | PLEC activity raises CEP170B's level | lines that do not express PLEC (3) vs lines expressing it (47) | 1.59× lower at baseline in the lines without PLEC | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, MYH16, PER3; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.640). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-10.8, -25.7); signed map (-8.6, 30.7). **Vector** length 109, 27.2% of its response variance represented; |z| ≥ 3 in 1,093 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +10.7 | +7.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.9 | +9.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.5 | +7.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +5.3 | +8.5 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.8 | +8.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.3 | +8.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.0 | +3.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.5 | +3.8 |
|  | [[Belumosudil (drug)]] 5 µM |  | +3.1 | +3.5 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +2.6 | +3.2 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.1 | -1.2 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.0 | -1.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -3.8 | -4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -3.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -3.4 | -3.0 |
|  | [[Arbutin (drug)]] 5 µM |  | -2.9 | -3.0 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -2.8 | -3.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.6 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | centrosomal protein 170B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q32.33 — chr14:104,865,268-104,896,747 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FAM68C, Cep170R; previously KIAA0284 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y4F5](https://www.uniprot.org/uniprotkb/Q9Y4F5) (Centrosomal protein of 170 kDa protein B):

> Plays a role in microtubule organization.

**Summary**, from NCBI Gene [283638](https://www.ncbi.nlm.nih.gov/gene/283638):

> Predicted to be located in microtubule. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:20362](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20362) · Entrez [283638](https://www.ncbi.nlm.nih.gov/gene/283638) · UniProt [Q9Y4F5](https://www.uniprot.org/uniprotkb/Q9Y4F5) · Ensembl [ENSG00000099814](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099814)

## Data

Gene col 1816: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1816); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1816, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1816]; `tensor/DDL_lfc|DDL_z.npy` [1816]; `embed/gene_vectors.npy` [1816]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1816 or target_col == 1816). Every well: [[CEP170B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CEP170B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
