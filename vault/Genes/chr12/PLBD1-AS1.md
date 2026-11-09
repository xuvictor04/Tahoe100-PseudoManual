---
symbol: "PLBD1-AS1"
type: "gene"
col: 15007
ensembl_id: "ENSG00000256751"
name: "PLBD1 antisense RNA 1"
location: "12p13.1-p12.3"
module: 10
arm: "+"
pooled_cpm: 2.32
n_lines_expressing: 29
n_dd_up: 24
n_dd_down: 2
n_dd_up_clean: 16
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# PLBD1-AS1

*PLBD1 antisense RNA 1* — 12p13.1-p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.42× (z +19.9, q 0e+00, up in 12 of 17 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.547× (z -4.7, q 0.001, down in 17 of 24 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.0964×, PANC-1 0.172×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 2 lines (PANC-1 0.147×, J82 0.0450×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (PANC-1 0.0170×; ⚠ cell-cycle shift, explains ~38% of this change); [[Vilanterol (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0590×).
> Its strongest partners by |cos| (75 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 26 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GUCY2C-AS1]] (+0.78, fdr 1e-05, ⚠ same locus), [[ZNF747]] (+0.77, fdr 5e-05), [[PCNX4-DT]] (+0.74, fdr 4e-05), [[TMEM202-AS1]] (+0.73, fdr 8e-05); moves opposite to [[PBX4]] (-0.65, fdr 2e-04), [[SLC27A1]] (-0.64, fdr 8e-04, ⚠ one half only (not replicated)), [[TMEM120B]] (-0.64, fdr 6e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[PKD2L2-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15007.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.42×** | +19.9 | 0e+00 | 12/17 (LoVo, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.26×** | +13.3 | 6e-38 | 1/3 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.87×** | +12.4 | 3e-33 | 12/19 (SW480, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **2.30×** | +9.8 | 2e-20 | 16/26 (LoVo, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.54×** | +9.7 | 2e-20 | 3/5 (NCI-H2347, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.82×** | +8.6 | 6e-16 | 5/7 (NCI-H1792, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.59×** | +7.6 | 2e-12 | 7/18 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.68×** | +6.1 | 6e-08 | 7/26 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.92×** | +5.2 | 1e-05 | 8/15 (Panc 03.27, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.73×** | +4.6 | 3e-04 | 1/12 (SW480) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.75×** | +4.5 | 4e-04 | 8/21 (NCI-H2347, A-427, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.70×** | +4.4 | 5e-04 | 3/20 (SW480, NCI-H2347, …) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.73×** | +4.4 | 5e-04 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +4.3 | 8e-04 | 4/18 (SW480, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.98×** | +4.1 | 0.002 | 1/4 (MIA PaCa-2) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.51×** | +3.4 | 0.022 | 2/15 (LoVo, PANC-1) | inconsistent across doses | low cells (technical?) |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.54×** | +3.4 | 0.022 | 1/23 (NCI-H2347) | inconsistent across doses |  |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.47×** | +3.2 | 0.039 | 1/19 (SK-MEL-2) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.47×** | +3.2 | 0.040 | 2/22 (PANC-1, J82) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.050 | 4/27 (LoVo, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **1.42×** | +2.9 | 0.090 | 1/11 (NCI-H2347) | inconsistent across doses | low cells (technical?) |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.45×** | +2.9 | 0.099 | 2/13 (PANC-1, Hs 766T) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15007.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 5 µM in 2 lines (MIA PaCa-2 0.0964×, PANC-1 0.172×; ⚠ toxic; transcription drop); [[Digitoxin (drug)]] 0.5 µM in 2 lines (PANC-1 0.147×, J82 0.0450×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 1 line (PANC-1 0.0170×; ⚠ cell-cycle shift, explains ~38% of this change); [[Vilanterol (drug)]] 0.5 µM in 1 line (Panc 03.27 0.0590×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.547×** | -4.7 | 0.001 | 17/24 (PANC-1, J82, …) | inconsistent across doses | cell-cycle shift (explains ~23% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.619×** | -4.0 | 0.016 | 14/25 (LoVo, MIA PaCa-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 0.664× | -3.4 | 0.11 | 5/27 (AN3 CA, HT-29, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | 0.672× | -3.3 | 0.11 | 6/26 (LoVo, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | 0.675× | -3.3 | 0.11 | 13/27 (LoVo, PANC-1, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15007. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 6.55 | 0 | 3 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0170× (z -19.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.147× (z -9.2) |
| [[J82 (line)]] | alt | 3.58 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 8.88× (z +9.6) | [[Digitoxin (drug)]] 0.5 µM 0.0450× (z -9.0) |
| [[HOP62 (line)]] | alt | 0.822 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.7× (z +8.5) | — |
| [[KATO III (line)]] | alt | 4.82 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.64× (z +8.8) | — |
| [[LoVo (line)]] | wt | 7.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +15.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0964× (z -10.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 5.24 | 0 | 1 | — | [[Vilanterol (drug)]] 0.5 µM 0.0590× (z -9.2) |
| [[SK-MEL-2 (line)]] | alt | 5.80 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.76× (z +9.6) | — |
| [[A-172 (line)]] | wt | 0.304 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.79 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.248 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.437 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.54 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.79 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.347 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.944 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.436 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.269 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.347 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 0.486 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.305 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.357 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.741 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.409 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.536 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.265 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.321 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.53 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.89 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.359 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.06 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.529 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.465 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.09 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 0.352 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.462 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.573 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.06 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.930 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15007), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 23 of them with an alert (⚠; 22 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GUCY2C-AS1]] | +0.78 | +0.81 / +0.51 | both halves | 1e-05 | same gene group; ⚠ same locus (41.5 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF747]] | +0.77 | +0.76 / +0.39 | both halves | 5e-05 |  |
| [[PCNX4-DT]] | +0.74 | +0.72 / +0.42 | both halves | 4e-05 |  |
| [[TMEM202-AS1]] | +0.73 | +0.72 / +0.37 | both halves | 8e-05 | same gene group |
| [[ANKRD31]] | +0.72 | +0.75 / +0.39 | both halves | 5e-05 |  |
| [[IQCH-AS1]] | +0.72 | +0.68 / +0.44 | both halves | 3e-05 | same gene group |
| [[RBM26-AS1]] | +0.72 | +0.70 / +0.36 | both halves | 9e-05 | same gene group |
| [[PATL2]] | +0.71 | +0.75 / +0.25 | both halves | 4e-04 |  |
| [[F8]] | +0.70 | +0.75 / +0.25 | both halves | 4e-04 |  |
| [[ZC2HC1C]] | +0.70 | +0.70 / +0.44 | both halves | 3e-05 |  |
| [[MMADHC-DT]] | +0.70 | +0.65 / +0.26 | both halves | 4e-04 |  |
| [[OXA1L-DT]] | +0.69 | +0.68 / +0.30 | both halves | 2e-04 |  |
| [[KRCC1]] | +0.69 | +0.70 / +0.31 | both halves | 2e-04 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 3 of them with an alert (⚠; 3 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PBX4]] | -0.65 | -0.62 / -0.31 | both halves | 2e-04 |  |
| [[SLC27A1]] | -0.64 | -0.57 / -0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[TMEM120B]] | -0.64 | -0.64 / -0.21 | both halves | 6e-04 |  |
| [[PCMT1]] | -0.63 | -0.59 / -0.16 | ⚠ one half (not replicated) | 0.001 |  |
| [[YIF1B]] | -0.63 | -0.60 / -0.06 | ⚠ one half (not replicated) | 0.004 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PLBD1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PKD2L2-DT]] | B | PLBD1-AS1 activity raises PKD2L2-DT's level | lines that do not express PLBD1-AS1 (21) vs lines expressing it (29) | 1.74× lower at baseline in the lines without PLBD1-AS1 | 0.031 | ⚠ within organs, on part of the lines; also absent: PLBD1, LINC01357, ANO1; maybe low, not absent |
| [[ZNF391]] | B | PLBD1-AS1 activity raises ZNF391's level | lines that do not express PLBD1-AS1 (21) vs lines expressing it (29) | 1.60× lower at baseline in the lines without PLBD1-AS1 | 0.035 | ⚠ within organs, on part of the lines; also absent: PLBD1, LINC01357, ANO1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.798). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (5.3, 13.9); signed map (27.0, -12.4). **Vector** length 42.8, 7.75% of its response variance represented; |z| ≥ 3 in 618 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.9 | +9.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +19.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.5 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +9.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +6.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.4 | +2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.1 | +4.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.9 | +0.7 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~36% of this change | -2.3 | -4.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.1 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | -1.9 | -3.3 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.8 | -0.1 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | -1.7 | -3.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.1 | +0.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.0 | -3.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -0.8 | -1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.8 | -2.1 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -0.6 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | PLBD1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12p13.1-p12.3 — chr12:14,567,393-14,624,191 (+) |
| Ensembl biotype | lncRNA |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:51143](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:51143) · Entrez [101928290](https://www.ncbi.nlm.nih.gov/gene/101928290) · Ensembl [ENSG00000256751](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000256751)

## Data

Gene col 15007: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15007); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15007, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15007]; `tensor/DDL_lfc|DDL_z.npy` [15007]; `embed/gene_vectors.npy` [15007]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15007 or target_col == 15007). Every well: [[PLBD1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLBD1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
