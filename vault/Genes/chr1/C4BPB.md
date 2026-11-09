---
symbol: "C4BPB"
type: "gene"
col: 4462
ensembl_id: "ENSG00000123843"
name: "complement component 4 binding protein beta"
location: "1q32.1"
module: 73
arm: "+"
pooled_cpm: 15.27
n_lines_expressing: 13
n_dd_up: 22
n_dd_down: 16
n_dd_up_clean: 14
n_dd_down_clean: 12
in_vector_space: true
direction_upstream: 66
direction_downstream: 94
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# C4BPB

*complement component 4 binding protein beta* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.40× (z +14.8, q 0e+00, up in 3 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.58× (z +13.3, q 5e-38, up in 2 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.569× (z -5.6, q 9e-06, down in 10 of 11 measured lines) ⚠ cell-cycle shift, explains ~28% of this change. The strongest without an alert is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.600× (z -4.7, q 6e-04, down in 1 of 11 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NPSR1]] (+0.81, fdr 7e-06), [[MUC17]] (+0.76, fdr 7e-06), [[HEPH]] (+0.75, fdr 7e-06).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 66 arrows point to it, the strongest [[MMP28]] → it (grade B ⚠); 94 go from it, the strongest it → [[LINC02580]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4462.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.40×** | +14.8 | 0e+00 | 3/9 (J82, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.58×** | +13.3 | 5e-38 | 2/10 (J82, HepG2/C3A) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.40×** | +8.4 | 1e-14 | 2/8 (J82, HCT15) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.40×** | +8.0 | 1e-13 | 1/8 (J82) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.13×** | +5.6 | 2e-06 | 2/6 (AsPC-1, J82) | top dose only | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +5.3 | 1e-05 | 1/10 (J82) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.60×** | +4.6 | 3e-04 | 2/10 (J82, KATO III) | top dose only | cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.91×** | +4.6 | 3e-04 | 2/10 (HepG2/C3A, J82) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.53×** | +4.2 | 0.002 | 4/11 (LS 180, KATO III, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.52×** | +4.0 | 0.004 | 1/11 (J82) | top dose only | cell-cycle shift (explains ~0% here) |
| [[BAY1125976 (drug)]] 0.5 µM |  | **1.68×** | +3.7 | 0.013 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.027 | 0/11 | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.4 | 0.027 | 1/10 (J82) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Saquinavir (drug)]] 0.05 µM |  | **1.38×** | +3.2 | 0.051 | 1/11 (J82) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.051 | 3/11 (KATO III, LS 180, …) | two highest doses |  |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.57×** | +3.2 | 0.053 | 0/11 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Sulfatinib (drug)]] 5 µM |  | **1.39×** | +3.1 | 0.062 | 0/11 | top dose only |  |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.36×** | +3.1 | 0.069 | 1/10 (HCT15) | inconsistent across doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **1.52×** | +3.0 | 0.088 | 2/10 (LS 180, LoVo) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.50×** | +2.9 | 0.099 | 1/10 (LoVo) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Dorzolamide (hydrochloride) (drug)]] 0.5 µM |  | **1.34×** | +2.9 | 0.099 | 0/11 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4462.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.569×** | -5.6 | 9e-06 | 10/11 (LoVo, Hs 766T, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.600×** | -4.7 | 6e-04 | 1/11 (LoVo) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.629×** | -4.6 | 6e-04 | 9/11 (LoVo, HT-29, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.650×** | -4.3 | 0.002 | 3/11 (SW48, HCT15, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.651×** | -4.3 | 0.002 | 7/11 (HepG2/C3A, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~10% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.655×** | -4.2 | 0.002 | 5/11 (HepG2/C3A, Hs 766T, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.658×** | -4.2 | 0.002 | 11/11 (LoVo, AsPC-1, …) | all doses, flat | position effect removed |
| [[Clopidogrel (drug)]] 0.5 µM |  | **0.666×** | -4.1 | 0.003 | 0/11 | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | **0.658×** | -3.9 | 0.007 | 0/11 | inconsistent across doses |  |
| [[Brivudine (drug)]] 5 µM |  | **0.496×** | -3.5 | 0.028 | 7/11 (LoVo, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.714×** | -3.4 | 0.036 | 2/11 (HepG2/C3A, J82) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.717×** | -3.4 | 0.038 | 2/11 (KATO III, HCT15) | top dose only | position effect removed |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.725×** | -3.2 | 0.052 | 0/11 | two highest doses |  |
| [[Artesunate (drug)]] 5 µM |  | **0.804×** | -3.1 | 0.075 | 2/11 (J82, HCT15) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Lucanthone (drug)]] 0.05 µM |  | **0.722×** | -3.0 | 0.092 | 0/11 | inconsistent across doses | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | **0.743×** | -3.0 | 0.099 | 0/11 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.34 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4462. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 29.3 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.197× (z -12.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.237× (z -11.3) |
| [[AsPC-1 (line)]] | alt | 61.9 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -14.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.218× (z -10.7) |
| [[Hs 766T (line)]] | wt | 235 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -19.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.115× (z -13.2) |
| [[LoVo (line)]] | wt | 137 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0427× (z -23.3) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -17.3) |
| [[LS 180 (line)]] | wt | 18.0 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.177× (z -9.3) ⚠ cell-cycle shift, explains ~43% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.323× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 53.6 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.139× (z -11.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[HCT15 (line)]] | alt | 24.6 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.251× (z -8.5) ⚠ cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 30.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.24× (z +8.7) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 9.92 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.40 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 6.43 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.32 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.38 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.26 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.50 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.58 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.21 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.22 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4462), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NPSR1]] | +0.81 | +0.83 / +0.70 | both halves | 7e-06 |  |
| [[MUC17]] | +0.76 | +0.71 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[HEPH]] | +0.75 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[SLC6A20]] | +0.75 | +0.73 / +0.68 | both halves | 7e-06 |  |
| [[MYO7B]] | +0.74 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[CALB1]] | +0.74 | +0.70 / +0.66 | both halves | 7e-06 |  |
| [[GCNT3]] | +0.72 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[EPS8L3]] | +0.71 | +0.68 / +0.72 | both halves | 7e-06 |  |
| [[TPRXL]] | +0.71 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[HSD17B2]] | +0.70 | +0.72 / +0.57 | both halves | 8e-06 | **novel candidate** |
| [[CLIC5]] | +0.70 | +0.59 / +0.75 | both halves | 7e-06 |  |
| [[TOX3]] | +0.68 | +0.65 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*66 arrows, 66 of them with an alert ⚠; grade A 0, B 6, C 60. Shown: the 12 strongest; 54 more arrows (54 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MMP28]] | B | MMP28 activity raises C4BPB's level | lines that do not express MMP28 (27) vs lines expressing it (23) | 1.45× lower at baseline in the lines without MMP28 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000285743, LINC02582, LINP1; maybe low, not absent |
| [[HTR1D]] | B | HTR1D activity raises C4BPB's level | lines that do not express HTR1D (15) vs lines expressing it (35) | 2.34× lower at baseline in the lines without HTR1D | 0.066 | ⚠ within organs, on part of the lines; also absent: A4GALT, ZNF185, PAPSS2; maybe low, not absent |
| [[LOXL1-AS1]] | B | LOXL1-AS1 activity lowers C4BPB's level | lines that do not express LOXL1-AS1 (14) vs lines expressing it (36) | 3.60× higher at baseline in the lines without LOXL1-AS1 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: BEX4, ENSG00000255330, LOXL1 |
| [[LDLRAD4]] | B | LDLRAD4 activity raises C4BPB's level | lines that do not express LDLRAD4 (23) vs lines expressing it (27) | 1.58× lower at baseline in the lines without LDLRAD4 | 0.085 | ⚠ within organs, on part of the lines; also absent: TTTY14, NLGN4X, ENSG00000260958 |
| [[WIPF1]] | B | WIPF1 activity lowers C4BPB's level | lines that do not express WIPF1 (16) vs lines expressing it (34) | 3.95× higher at baseline in the lines without WIPF1 | 0.088 | ⚠ within organs, on part of the lines; also absent: BVES-AS1, GNB4, POPDC3 |
| [[SHROOM3]] | B | SHROOM3 activity raises C4BPB's level | lines that do not express SHROOM3 (19) vs lines expressing it (31) | 1.80× lower at baseline in the lines without SHROOM3 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TERT; also absent: RHOV, ELF3, PLUT |
| [[LINC02582]] | C | LINC02582 activity raises C4BPB's level | lines that do not express LINC02582 (41) vs lines expressing it (9) | 5.19× lower at baseline in the lines without LINC02582 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, ENSG00000250920, ENSG00000230975; co-absent with the target |
| [[REG4]] | C | REG4 activity raises C4BPB's level | lines that do not express REG4 (43) vs lines expressing it (7) | 6.79× lower at baseline in the lines without REG4 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |
| [[FXYD3]] | C | FXYD3 activity raises C4BPB's level | lines that do not express FXYD3 (34) vs lines expressing it (16) | 3.96× lower at baseline in the lines without FXYD3 | 0.005 | ⚠ within organs, on part of the lines; also absent: CEACAM6, TMEM30B, TMPRSS2; co-absent with the target |
| [[GPA33]] | C | GPA33 activity raises C4BPB's level | lines that do not express GPA33 (41) vs lines expressing it (9) | 6.11× lower at baseline in the lines without GPA33 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PHGR1, NPSR1, CDH17; co-absent with the target |
| [[MUC2]] | C | MUC2 activity raises C4BPB's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 5.57× lower at baseline in the lines without MUC2 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4; co-absent with the target |
| [[KLK10]] | C | KLK10 activity raises C4BPB's level | lines that do not express KLK10 (34) vs lines expressing it (16) | 4.48× lower at baseline in the lines without KLK10 | 0.008 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, HS3ST1, IRF6; co-absent with the target |

### Downstream of this gene

*94 arrows, 94 of them with an alert ⚠; grade A 0, B 26, C 68. Shown: the 12 strongest; 82 more arrows (82 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02580]] | B | C4BPB activity raises LINC02580's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 2.34× lower at baseline in the lines without C4BPB | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[INPP1]] | B | C4BPB activity raises INPP1's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 3.63× lower at baseline in the lines without C4BPB | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[KLF3]] | B | C4BPB activity raises KLF3's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 2.52× lower at baseline in the lines without C4BPB | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[LMO7]] | B | C4BPB activity raises LMO7's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 4.84× lower at baseline in the lines without C4BPB | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[SDCBP2]] | B | C4BPB activity raises SDCBP2's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 4.27× lower at baseline in the lines without C4BPB | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[PITX1]] | B | C4BPB activity raises PITX1's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 2.53× lower at baseline in the lines without C4BPB | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[KLF5]] | B | C4BPB activity raises KLF5's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 5.19× lower at baseline in the lines without C4BPB | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[SEPTIN9-DT]] | B | C4BPB activity raises SEPTIN9-DT's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 2.33× lower at baseline in the lines without C4BPB | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[TACR3-AS1]] | B | C4BPB activity raises TACR3-AS1's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 2.34× lower at baseline in the lines without C4BPB | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[WIPF1]] | B | C4BPB activity lowers WIPF1's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 4.72× higher at baseline in the lines without C4BPB | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[IL22RA1]] | B | C4BPB activity raises IL22RA1's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 3.05× lower at baseline in the lines without C4BPB | 0.028 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |
| [[MMP28]] | B | C4BPB activity raises MMP28's level | lines that do not express C4BPB (37) vs lines expressing it (13) | 2.08× lower at baseline in the lines without C4BPB | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, LINC02964, REG4 |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.788). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (19.3, 50.7); signed map (65.0, 7.8). **Vector** length 49.5, 19.3% of its response variance represented; |z| ≥ 3 in 293 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.2 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.8 | +14.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +8.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +2.8 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +3.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +2.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.2 | +1.7 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.1 | +2.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.6 | -4.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.3 | -4.3 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.3 | -3.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.0 | -3.4 |
|  | [[Encorafenib (drug)]] 5 µM |  | -1.0 | -2.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.9 | -1.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -0.9 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | complement component 4 binding protein beta |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:207,088,860-207,099,993 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously C4BP |
| Gene groups (HGNC) | Sushi domain containing; Complement system regulators and receptors |
| Hallmark sets | UV_RESPONSE_UP, COMPLEMENT |
| Reactome | 7 pathways, smallest: Regulation of Complement cascade; Complement cascade; Dengue virus activates/modulates innate and adaptive immune responses |
| Matched by | ensembl_id |

**Function**, from UniProt [P20851](https://www.uniprot.org/uniprotkb/P20851) (C4b-binding protein beta chain):

> Controls the classical pathway of complement activation. It binds as a cofactor to C3b/C4b inactivator (C3bINA), which then hydrolyzes the complement fragment C4b. It also accelerates the degradation of the C4bC2a complex (C3 convertase) by dissociating the complement fragment C2a. It also interacts with anticoagulant protein S and with serum amyloid P component. The beta chain binds protein S.

**Summary**, from NCBI Gene [725](https://www.ncbi.nlm.nih.gov/gene/725):

> This gene encodes a member of a superfamily of proteins composed predominantly of tandemly arrayed short consensus repeats of approximately 60 amino acids. A single, unique beta-chain encoded by this gene assembles with seven identical alpha-chains into the predominant isoform of C4b-binding protein, a multimeric protein that controls activation of the complement cascade through the classical pathway. C4b-binding protein has a regulatory role in the coagulation system also, mediated through the …

**Accessions** — [HGNC:1328](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1328) · Entrez [725](https://www.ncbi.nlm.nih.gov/gene/725) · UniProt [P20851](https://www.uniprot.org/uniprotkb/P20851) · Ensembl [ENSG00000123843](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000123843)

## Data

Gene col 4462: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4462); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4462, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4462]; `tensor/DDL_lfc|DDL_z.npy` [4462]; `embed/gene_vectors.npy` [4462]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4462 or target_col == 4462). Every well: [[C4BPB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C4BPB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
