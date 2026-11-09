---
symbol: "ULBP3"
type: "gene"
col: 5159
ensembl_id: "ENSG00000131019"
name: "UL16 binding protein 3"
location: "6q25.1"
module: 15
arm: "-"
pooled_cpm: 7.67
n_lines_expressing: 47
n_dd_up: 26
n_dd_down: 3
n_dd_up_clean: 15
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 2
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# ULBP3

*UL16 binding protein 3* — 6q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.50× (z +16.6, q 0e+00, up in 39 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 0.462× (z -5.4, q 5e-05, down in 16 of 39 measured lines).
> Its strongest partners by |cos| (91 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 9 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAJB1]] (+0.61, fdr 3e-05), [[CBR1]] (+0.61, fdr 4e-05), [[LPAR3]] (+0.59, fdr 2e-05); moves opposite to [[RNF170]] (-0.59, fdr 2e-04), [[AMY2B]] (-0.55, fdr 2e-04), [[ZNF862]] (-0.55, fdr 3e-04).
> It sits in the **-** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PNMA2]] → it (grade B ⚠); 2 go from it, the strongest it → [[USP49]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5159.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.50×** | +16.6 | 0e+00 | 39/44 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **3.22×** | +15.5 | 0e+00 | 39/44 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.03×** | +13.3 | 7e-38 | 32/45 (NCI-H460, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **2.69×** | +13.1 | 3e-37 | 32/41 (SW480, RKO, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **2.62×** | +12.8 | 3e-35 | 40/44 (PANC-1, LoVo, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **2.42×** | +11.3 | 2e-27 | 10/16 (KATO III, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.26×** | +10.8 | 2e-25 | 34/44 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | **1.98×** | +9.0 | 1e-17 | 16/26 (KATO III, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +8.0 | 5e-14 | 24/33 (KATO III, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +7.6 | 1e-12 | 21/43 (A498, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.78×** | +7.1 | 6e-11 | 13/21 (SW480, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.74×** | +7.0 | 2e-10 | 20/39 (HOP62, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.57×** | +6.0 | 9e-08 | 17/42 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.55×** | +5.8 | 2e-07 | 20/44 (KATO III, RKO, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.35×** | +5.6 | 9e-07 | 17/38 (LS 180, AsPC-1, …) | rises with dose | composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.15×** | +5.3 | 4e-06 | 14/41 (PANC-1, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.42×** | +4.7 | 9e-05 | 15/39 (LS 180, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.42×** | +4.6 | 1e-04 | 14/41 (SW1417, HOP62, …) | rises with dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.59×** | +3.2 | 0.035 | 3/39 (HEC-1-A, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.05 µM |  | **1.26×** | +3.0 | 0.059 | 3/42 (PANC-1, SHP-77, …) | inconsistent across doses | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **1.52×** | +2.9 | 0.078 | 8/36 (HT-29, SW480, …) | top dose only | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5159.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.462×** | -5.4 | 5e-05 | 16/39 (NCI-H460, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.549×** | -4.2 | 0.009 | 15/36 (NCI-H460, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.794×** | -3.6 | 0.065 | 12/44 (SNU-1, LoVo, …) | two highest doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.839× | -3.3 | 0.14 | 16/38 (PANC-1, RKO, …) | top dose only |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.934× | -3.1 | 0.20 | 4/45 (AsPC-1, NCI-H2347, …) | inconsistent across doses |  |
| [[MK-3903 (drug)]] 5 µM |  | 0.642× | -3.1 | 0.20 | 6/36 (MIA PaCa-2, SW48, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5159. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 5.38 | 3 (1 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 6.76× (z +9.9) | — |
| [[SW480 (line)]] | alt | 16.4 | 3 | 0 | [[Auranofin (drug)]] 5 µM 3.79× (z +11.3) | — |
| [[HEC-1-A (line)]] | alt | 16.9 | 1 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.76× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.185× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H460 (line)]] | wt | 8.84 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.24× (z +10.0) | — |
| [[SW48 (line)]] | wt | 21.4 | 0 | 2 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0950× (z -9.9) |
| [[A-172 (line)]] | wt | 4.08 | 0 | 1 | — | [[Menadione (drug)]] 0.5 µM 0.0786× (z -9.4) |
| [[A-427 (line)]] | wt | 6.09 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0867× (z -11.0) ⚠ cell-cycle shift, would explain all of this change |
| [[C-33 A (line)]] | alt | 8.02 | 0 | 1 | — | [[Erlotinib (drug)]] 0.05 µM 0.0478× (z -10.2) |
| [[KATO III (line)]] | alt | 15.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.09× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 9.82 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.135× (z -10.0) |
| [[NCI-H1573 (line)]] | alt | 4.49 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0878× (z -8.8) |
| [[NCI-H23 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.165× (z -9.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 17.2 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.68× (z +9.7) | — |
| [[A498 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.14 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.75 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.844 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.00 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 5.84 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.27 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.93 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.44 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.21 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.06 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.42 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.56 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5159), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*64 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAJB1]] | +0.61 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[CBR1]] | +0.61 | +0.41 / +0.58 | both halves | 4e-05 |  |
| [[LPAR3]] | +0.59 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[ALAS1]] | +0.58 | +0.41 / +0.61 | both halves | 4e-05 |  |
| [[SEPTIN6]] | +0.58 | +0.37 / +0.51 | both halves | 9e-05 |  |
| [[RPAP3]] | +0.57 | +0.42 / +0.59 | both halves | 4e-05 |  |
| [[DGKG]] | +0.57 | +0.42 / +0.58 | both halves | 4e-05 |  |
| [[MOCS2]] | +0.56 | +0.39 / +0.58 | both halves | 5e-05 |  |
| [[MOCS1]] | +0.56 | +0.25 / +0.52 | both halves | 4e-04 |  |
| [[ZNF483]] | +0.56 | +0.33 / +0.67 | both halves | 1e-04 |  |
| [[TOX2]] | +0.55 | +0.41 / +0.49 | both halves | 4e-05 |  |
| [[SNX10]] | +0.54 | +0.38 / +0.52 | both halves | 7e-05 |  |

## Genes that move opposite

*36 of its nearest partners move opposite, 8 of them with an alert (⚠; 8 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNF170]] | -0.59 | -0.31 / -0.54 | both halves | 2e-04 |  |
| [[AMY2B]] | -0.55 | -0.30 / -0.36 | both halves | 2e-04 |  |
| [[ZNF862]] | -0.55 | -0.28 / -0.50 | both halves | 3e-04 |  |
| [[PPM1B]] | -0.54 | -0.42 / -0.53 | both halves | 4e-05 |  |
| [[PRANCR]] | -0.54 | -0.33 / -0.31 | both halves | 2e-04 |  |
| [[CDK19]] | -0.53 | -0.40 / -0.48 | both halves | 5e-05 |  |
| [[KIAA2026]] | -0.53 | -0.39 / -0.50 | both halves | 6e-05 |  |
| [[ATAD2B]] | -0.53 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[ASH1L]] | -0.53 | -0.25 / -0.56 | both halves | 4e-04 |  |
| [[OARD1]] | -0.52 | -0.13 / -0.55 | ⚠ one half (not replicated) | 0.002 |  |
| [[DICER1-AS1]] | -0.52 | -0.19 / -0.42 | ⚠ not reproduced | 8e-04 |  |
| [[PCMTD1]] | -0.51 | -0.43 / -0.46 | both halves | 3e-05 |  |
| [[LEMD3]] | -0.51 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[NDUFAF6]] | -0.50 | -0.42 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PNMA2]] | B | PNMA2 activity raises ULBP3's level | lines that do not express PNMA2 (16) vs lines expressing it (34) | 1.32× lower at baseline in the lines without PNMA2 | 0.086 | ⚠ within organs, on part of the lines; also absent: MCOLN3, CACNG6, SELENOM |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[USP49]] | C | ULBP3 activity lowers USP49's level | lines that do not express ULBP3 (3) vs lines expressing it (47) | 2.03× higher at baseline in the lines without ULBP3 | 0.073 | ⚠ few lines (3 vs 47); across organs; also absent: SPDL1, ARHGAP10, CDC20; maybe low, not absent |
| [[CCDC112]] | C | ULBP3 activity raises CCDC112's level | lines that do not express ULBP3 (3) vs lines expressing it (47) | 2.03× lower at baseline in the lines without ULBP3 | 0.099 | ⚠ few lines (3 vs 47); across organs; also absent: SPDL1, ARHGAP10, CDC20; maybe low, not absent |

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **-** arm (projection on the module's main direction -0.493). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-0.6, 20.1); signed map (-19.9, 38.6). **Vector** length 75.6, 13.3% of its response variance represented; |z| ≥ 3 in 1,127 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.0 | +13.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.1 | +13.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.1 | +6.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | +4.6 | +11.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~54% of this change | +4.1 | +9.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +2.3 | +4.6 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.7 | +5.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.5 | +2.1 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -4.4 | -1.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.3 | -3.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -3.4 | -0.7 |
|  | [[TAK-901 (drug)]] 5 µM |  | -3.1 | -5.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.9 | -4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -1.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.6 | -3.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.6 | -1.2 |
|  | [[RMC-6236 (drug)]] 5 µM |  | -1.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | UL16 binding protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q25.1 — chr6:150,061,053-150,069,121 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RAET1N |
| Gene groups (HGNC) | Retinoic acid early transcript 1 family |
| Reactome | 2 pathways, smallest: Immunoregulatory interactions between a Lymphoid and a non-Lymphoid cell; Adaptive Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZM4](https://www.uniprot.org/uniprotkb/Q9BZM4) (UL16-binding protein 3):

> Binds and activates the KLRK1/NKG2D receptor, mediating natural killer cell cytotoxicity.

**Summary**, from NCBI Gene [79465](https://www.ncbi.nlm.nih.gov/gene/79465):

> The protein encoded by this gene is one of several related ligands of the KLRK1/NKG2D receptor, which is found in primary NK cells. Binding of these ligands to the receptor activates several signal transduction pathways, including the JAK2, STAT5, and ERK pathways. The encoded protein is expressed solubly and on the surface of many tumor cells, making it potentially an important target for therapeutics. [provided by RefSeq, Nov 2015]

**Accessions** — [HGNC:14895](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14895) · Entrez [79465](https://www.ncbi.nlm.nih.gov/gene/79465) · UniProt [Q9BZM4](https://www.uniprot.org/uniprotkb/Q9BZM4) · Ensembl [ENSG00000131019](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000131019)

## Data

Gene col 5159: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5159); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5159, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5159]; `tensor/DDL_lfc|DDL_z.npy` [5159]; `embed/gene_vectors.npy` [5159]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5159 or target_col == 5159). Every well: [[ULBP3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ULBP3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
