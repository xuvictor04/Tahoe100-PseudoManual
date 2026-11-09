---
symbol: "CHST14"
type: "gene"
col: 9753
ensembl_id: "ENSG00000169105"
name: "carbohydrate sulfotransferase 14"
location: "15q15.1"
module: 10
arm: "+"
pooled_cpm: 2.09
n_lines_expressing: 47
n_dd_up: 5
n_dd_down: 21
n_dd_up_clean: 1
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 10
direction_downstream: 1
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# CHST14

*carbohydrate sulfotransferase 14* — 15q15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.39× (z +11.4, q 4e-27, up in 2 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.56× (z +5.0, q 7e-05, up in 2 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.428× (z -9.5, q 1e-18, down in 24 of 28 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MIR1915HG]] (+0.58, fdr 3e-05), [[B3GNT9]] (+0.58, fdr 4e-05), [[ANTXR1]] (+0.57, fdr 4e-05); moves opposite to [[PTPRH]] (-0.45, fdr 1e-04), [[KIF16B]] (-0.44, fdr 8e-05), [[MYH14]] (-0.43, fdr 1e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[BOLA3-DT]] → it (grade B ⚠); 1 goes from it, the strongest it → [[DPY19L3-DT]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9753.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.39×** | +11.4 | 4e-27 | 2/3 (A498, HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.70×** | +7.9 | 5e-13 | 6/8 (CFPAC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.14×** | +5.6 | 3e-06 | 3/3 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.56×** | +5.0 | 7e-05 | 2/41 (HEC-1-A, NCI-H2030) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.52×** | +3.4 | 0.083 | 3/9 (PANC-1, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Larotrectinib (drug)]] 0.5 µM |  | 1.50× | +3.2 | 0.11 | 1/31 (LoVo) | two highest doses |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | 1.48× | +3.0 | 0.18 | 3/14 (MIA PaCa-2, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~7% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 1 with an alert ⚠; shown: the 15 strongest. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9753.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.428×** | -9.5 | 1e-18 | 24/28 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.402×** | -6.9 | 7e-10 | 17/33 (NCI-H2030, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.416×** | -6.9 | 7e-10 | 23/38 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.419×** | -6.9 | 8e-10 | 22/42 (NCI-H2030, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.425×** | -6.8 | 1e-09 | 21/39 (A-172, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.432×** | -6.7 | 2e-09 | 18/32 (PANC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.432×** | -6.6 | 2e-09 | 17/29 (Hs 766T, MIA PaCa-2, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.447×** | -6.4 | 1e-08 | 22/42 (J82, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.463×** | -6.1 | 7e-08 | 19/34 (MIA PaCa-2, RPMI-7951, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.486×** | -5.7 | 6e-07 | 19/40 (A-172, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.486×** | -5.4 | 4e-06 | 11/30 (A-172, hTERT-HPNE, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.514×** | -5.3 | 6e-06 | 11/25 (HEC-1-A, A-172, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.528×** | -5.1 | 2e-05 | 15/36 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **0.543×** | -4.6 | 1e-04 | 15/26 (H4, A-172, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.560×** | -4.6 | 2e-04 | 12/41 (NCI-H460, A498, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, -0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9753. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 7.91 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0635× (z -17.5) |
| [[NCI-H2030 (line)]] | alt | 5.25 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0386× (z -11.8) |
| [[NCI-H460 (line)]] | wt | 1.89 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.0200× (z -13.6) |
| [[PANC-1 (line)]] | alt | 3.87 | 0 | 2 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.130× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 2.25 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0369× (z -9.4) |
| [[J82 (line)]] | alt | 3.49 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0613× (z -12.9) |
| [[A-427 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.22 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.791 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.529 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.20 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.60 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.16 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.962 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.969 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.90 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.751 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.76 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.228 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.756 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.314 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.70 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.816 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.33 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.42 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.29 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.52 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.92 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9753), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MIR1915HG]] | +0.58 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[B3GNT9]] | +0.58 | +0.57 / +0.42 | both halves | 4e-05 |  |
| [[ANTXR1]] | +0.57 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[EXO5]] | +0.55 | +0.50 / +0.41 | both halves | 4e-05 |  |
| [[POGLUT3]] | +0.52 | +0.55 / +0.35 | both halves | 1e-04 |  |
| [[FZD1]] | +0.51 | +0.51 / +0.46 | both halves | 2e-05 |  |
| [[TYSND1]] | +0.51 | +0.41 / +0.47 | both halves | 4e-05 |  |
| [[ZFP69]] | +0.51 | +0.51 / +0.44 | both halves | 3e-05 |  |
| [[LOXL1]] | +0.50 | +0.47 / +0.51 | both halves | 2e-05 |  |
| [[MARVELD1]] | +0.50 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[PLPP6]] | +0.49 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[ZNF236]] | +0.49 | +0.44 / +0.36 | both halves | 1e-04 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PTPRH]] | -0.45 | -0.39 / -0.33 | both halves | 1e-04 |  |
| [[KIF16B]] | -0.44 | -0.37 / -0.38 | both halves | 8e-05 |  |
| [[MYH14]] | -0.43 | -0.36 / -0.35 | both halves | 1e-04 |  |
| [[CALN1]] | -0.43 | -0.28 / -0.39 | both halves | 3e-04 |  |
| [[EMC2]] | -0.43 | -0.48 / -0.25 | both halves | 4e-04 |  |
| [[NR6A1]] | -0.41 | -0.37 / -0.36 | both halves | 9e-05 |  |
| [[NEAT1]] | -0.41 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[FUT2]] | -0.41 | -0.46 / -0.22 | both halves | 6e-04 | pathway: Metabolism of carbohydrates and carbohydrate derivatives |
| [[CFDP1]] | -0.40 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[UBE2B]] | -0.40 | -0.47 / -0.27 | both halves | 3e-04 |  |
| [[UBE2H]] | -0.40 | -0.42 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 10, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BOLA3-DT]] | B | BOLA3-DT activity raises CHST14's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 1.72× lower at baseline in the lines without BOLA3-DT | 0.009 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[MIR1915HG]] | B | MIR1915HG activity raises CHST14's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 1.52× lower at baseline in the lines without MIR1915HG | 0.027 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[SEPTIN5]] | B | SEPTIN5 activity raises CHST14's level | lines that do not express SEPTIN5 (12) vs lines expressing it (38) | 1.45× lower at baseline in the lines without SEPTIN5 | 0.029 | ⚠ within organs, on part of the lines; also absent: DCLK2, EBF4, TCF7L1 |
| [[DOCK2]] | B | DOCK2 activity raises CHST14's level | lines that do not express DOCK2 (21) vs lines expressing it (29) | 1.71× lower at baseline in the lines without DOCK2 | 0.032 | ⚠ within organs, on part of the lines; also absent: ADAM12, MSC-AS1, KCTD16; maybe low, not absent |
| [[DZIP1L]] | B | DZIP1L activity raises CHST14's level | lines that do not express DZIP1L (8) vs lines expressing it (42) | 1.83× lower at baseline in the lines without DZIP1L | 0.037 | ⚠ within organs, on part of the lines; also absent: STARD9, CYP46A1, RECK; maybe low, not absent |
| [[FZD1]] | B | FZD1 activity raises CHST14's level | lines that do not express FZD1 (6) vs lines expressing it (44) | 1.66× lower at baseline in the lines without FZD1 | 0.052 | ⚠ within organs, on part of the lines; also absent: TMOD2, SNPH, DNAI1; maybe low, not absent |
| [[LOXL1]] | B | LOXL1 activity raises CHST14's level | lines that do not express LOXL1 (18) vs lines expressing it (32) | 1.30× lower at baseline in the lines without LOXL1 | 0.053 | ⚠ within organs, on part of the lines; also absent: B3GALNT1, LOXL1-AS1, ENSG00000255330 |
| [[ARHGEF25]] | B | ARHGEF25 activity raises CHST14's level | lines that do not express ARHGEF25 (15) vs lines expressing it (35) | 1.57× lower at baseline in the lines without ARHGEF25 | 0.058 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, RASSF8-AS1, CHST10 |
| [[VASH1]] | B | VASH1 activity raises CHST14's level | lines that do not express VASH1 (16) vs lines expressing it (34) | 1.56× lower at baseline in the lines without VASH1 | 0.075 | ⚠ within organs, on part of the lines; also absent: ANTXR1, ADAMTS7, WNT5B |
| [[MYH14]] | B | MYH14 activity lowers CHST14's level | lines that do not express MYH14 (21) vs lines expressing it (29) | 1.53× higher at baseline in the lines without MYH14 | 0.092 | ⚠ within organs, on part of the lines; also absent: ERBB3, EPCAM, FAAH2 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPY19L3-DT]] | C | CHST14 activity raises DPY19L3-DT's level | lines that do not express CHST14 (3) vs lines expressing it (47) | 1.26× lower at baseline in the lines without CHST14 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: DLG4, NECAB2, DMXL2; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.332). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (56.5, 20.3); signed map (42.2, 30.6). **Vector** length 44.4, 5.88% of its response variance represented; |z| ≥ 3 in 969 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +2.6 | +5.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.3 | +11.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +5.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.9 | +0.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.6 | +1.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.0 | +2.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.9 | +2.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +1.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | +0.9 | -1.7 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +0.8 | +2.9 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -2.2 | -5.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.2 | -6.1 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.0 | -5.4 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.9 | -6.9 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.4 | -6.6 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -3.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.1 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | carbohydrate sulfotransferase 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q15.1 — chr15:40,470,984-40,473,158 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HD4ST, D4ST-1; previously D4ST1 |
| Gene groups (HGNC) | Sulfotransferases, membrane bound |
| Reactome | 8 pathways, smallest: Defective CHST14 causes EDS, musculocontractural type; DS-GAG biosynthesis; Chondroitin sulfate/dermatan sulfate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8NCH0](https://www.uniprot.org/uniprotkb/Q8NCH0) (Carbohydrate sulfotransferase 14):

> Catalyzes the transfer of sulfate to position 4 of the N-acetylgalactosamine (GalNAc) residue of dermatan sulfate. Plays a pivotal role in the formation of 4-0-sulfated IdoA blocks in dermatan sulfate. Transfers sulfate to the C-4 hydroxyl of beta1,4-linked GalNAc that is substituted with an alpha-linked iduronic acid (IdoUA) at the C-3 hydroxyl. Transfers sulfate more efficiently to GalNAc residues in -IdoUA-GalNAc-IdoUA- than in -GlcUA-GalNAc-GlcUA-sequences. Has preference for partially …

**Summary**, from NCBI Gene [113189](https://www.ncbi.nlm.nih.gov/gene/113189):

> This gene encodes a member of the HNK-1 family of sulfotransferases. The encoded protein transfers sulfate to the C-4 hydroxyl of N-acetylgalactosamine residues in dermatan sulfate. Mutations in this gene have been associated with adducted thumb-clubfoot syndrome.[provided by RefSeq, Mar 2010]

**Accessions** — [HGNC:24464](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24464) · Entrez [113189](https://www.ncbi.nlm.nih.gov/gene/113189) · UniProt [Q8NCH0](https://www.uniprot.org/uniprotkb/Q8NCH0) · Ensembl [ENSG00000169105](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169105)

## Data

Gene col 9753: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9753); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9753, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9753]; `tensor/DDL_lfc|DDL_z.npy` [9753]; `embed/gene_vectors.npy` [9753]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9753 or target_col == 9753). Every well: [[CHST14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CHST14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
