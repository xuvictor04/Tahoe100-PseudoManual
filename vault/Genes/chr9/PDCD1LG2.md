---
symbol: "PDCD1LG2"
type: "gene"
col: 12437
ensembl_id: "ENSG00000197646"
name: "programmed cell death 1 ligand 2"
location: "9p24.1"
module: 116
arm: "+"
pooled_cpm: 9.45
n_lines_expressing: 22
n_dd_up: 17
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 32
direction_downstream: 42
tags: ["gene", "module/116"]
generated_by: "tahoemap"
---

# PDCD1LG2

*programmed cell death 1 ligand 2* — 9p24.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.61× (z +9.6, q 3e-19, up in 8 of 16 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.57× (z +6.4, q 2e-08, up in 1 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 0.433× (z -8.4, q 2e-14, down in 18 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ESM1]] (+0.71, fdr 7e-06), [[LINC02742]] (+0.69, fdr 7e-06), [[ADAMTS6]] (+0.65, fdr 7e-06); moves opposite to [[ESYT2]] (-0.47, fdr 8e-05).
> It is in [[Module 116]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 32 arrows point to it, the strongest [[FRMD6]] → it (grade B ⚠); 42 go from it, the strongest it → [[ABL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 7 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12437.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.61×** | +9.6 | 3e-19 | 8/16 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.42×** | +8.6 | 3e-15 | 4/10 (hTERT-HPNE, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +6.4 | 2e-08 | 1/19 (SK-MEL-2) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.96×** | +6.2 | 6e-08 | 3/11 (NCI-H2347, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.70×** | +5.3 | 1e-05 | 11/19 (HS-578T, Panc 03.27, …) | two highest doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **1.99×** | +4.9 | 8e-05 | 7/17 (RPMI-7951, H4, …) | two highest doses | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.39×** | +4.7 | 2e-04 | 8/19 (RPMI-7951, H4, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.56×** | +4.5 | 6e-04 | 8/17 (Panc 03.27, SNU-423, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.4 | 7e-04 | 6/20 (RKO, H4, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.48×** | +4.0 | 0.004 | 10/19 (HS-578T, SK-MEL-2, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.48×** | +3.9 | 0.004 | 11/19 (SK-MEL-2, Panc 03.27, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.45×** | +3.7 | 0.008 | 11/19 (HS-578T, SK-MEL-2, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.42×** | +3.5 | 0.019 | 3/18 (A-172, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.93×** | +3.5 | 0.021 | 0/6 | inconsistent across doses | noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.93×** | +3.5 | 0.021 | 5/13 (HOP62, HS-578T, …) | two highest doses | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.051 | 11/19 (HS-578T, hTERT-HPNE, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +3.0 | 0.079 | 8/19 (A-172, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12437.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.433×** | -8.4 | 2e-14 | 18/20 (NCI-H460, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.499×** | -7.0 | 7e-10 | 14/19 (RKO, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.613×** | -4.9 | 1e-04 | 12/19 (NCI-H460, RKO, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.692×** | -3.7 | 0.029 | 8/18 (H4, SK-MEL-2, …) | two highest doses |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.908× | -3.5 | 0.052 | 2/20 (HOP62, NCI-H1792) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.695×** | -3.4 | 0.066 | 3/18 (NCI-H460, NCI-H2347, …) | inconsistent across doses |  |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.708×** | -3.3 | 0.067 | 5/18 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~9% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12437. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 48.3 | 0 | 13 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0727× (z -26.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0345× (z -24.3) |
| [[RKO (line)]] | wt | 66.2 | 0 | 8 (3 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0281× (z -26.0) ⚠ cell-cycle shift, explains ~37% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0590× (z -21.4) |
| [[J82 (line)]] | alt | 59.1 | 0 | 4 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.191× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 56.3 | 0 | 4 | — | [[Panobinostat (drug)]] 5 µM 0.0637× (z -17.3) |
| [[HOP62 (line)]] | alt | 19.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.158× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 9.53 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.139× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 14.4 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0568× (z -11.5) |
| [[A-172 (line)]] | wt | 6.96 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.75 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.54 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.61 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.90 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.61 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.70 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.08 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.01 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.25 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.08 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12437), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ESM1]] | +0.71 | +0.72 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[LINC02742]] | +0.69 | +0.70 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[ADAMTS6]] | +0.65 | +0.61 / +0.68 | both halves | 7e-06 |  |
| [[FGF5]] | +0.63 | +0.58 / +0.64 | both halves | 8e-06 | same gene group |
| [[STEAP1B-AS1]] | +0.62 | +0.56 / +0.62 | both halves | 1e-05 | **novel candidate** |
| [[MARCHF4]] | +0.62 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[RDUR]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[PSG5]] | +0.61 | +0.61 / +0.52 | both halves | 1e-05 |  |
| [[ROBO4]] | +0.61 | +0.50 / +0.69 | both halves | 1e-05 |  |
| [[PDE1C]] | +0.61 | +0.49 / +0.59 | both halves | 1e-05 |  |
| [[BMPER]] | +0.61 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[CD274]] | +0.60 | +0.45 / +0.65 | both halves | 3e-05 | same gene group; pathway: Co-inhibition by PD-1; STRING 996; ⚠ same locus (40.0 kb, same strand: neighbours can correlate without regulation) |
| [[SRGAP1]] | +0.59 | +0.51 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ESYT2]] | -0.47 | -0.37 / -0.45 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*32 arrows, 32 of them with an alert ⚠; grade A 0, B 4, C 28. Shown: the 12 strongest; 20 more arrows (20 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FRMD6]] | B | FRMD6 activity raises PDCD1LG2's level | lines that do not express FRMD6 (13) vs lines expressing it (37) | 2.81× lower at baseline in the lines without FRMD6 | 0.062 | ⚠ within organs, on part of the lines; also absent: CTSL, OSMR-DT, EVC; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises PDCD1LG2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[SH2D2A]] | B | SH2D2A activity raises PDCD1LG2's level | lines that do not express SH2D2A (20) vs lines expressing it (30) | 1.66× lower at baseline in the lines without SH2D2A | 0.079 | ⚠ within organs, on part of the lines; also absent: IL1R2, SLC17A9, MT1G; maybe low, not absent |
| [[ITGB1-DT]] | B | ITGB1-DT activity raises PDCD1LG2's level | lines that do not express ITGB1-DT (21) vs lines expressing it (29) | 2.37× lower at baseline in the lines without ITGB1-DT | 0.082 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LTBP2, ADTRP; maybe low, not absent |
| [[ADAMTS6]] | C | ADAMTS6 activity raises PDCD1LG2's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 3.65× lower at baseline in the lines without ADAMTS6 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2; co-absent with the target |
| [[LNCOG]] | C | LNCOG activity raises PDCD1LG2's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 4.29× lower at baseline in the lines without LNCOG | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1; co-absent with the target |
| [[LAMA1]] | C | LAMA1 activity raises PDCD1LG2's level | lines that do not express LAMA1 (31) vs lines expressing it (19) | 3.99× lower at baseline in the lines without LAMA1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LNCOG, CCL3, PHACTR1; co-absent with the target |
| [[ESM1]] | C | ESM1 activity raises PDCD1LG2's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 4.05× lower at baseline in the lines without ESM1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865; co-absent with the target |
| [[TCF4]] | C | TCF4 activity raises PDCD1LG2's level | lines that do not express TCF4 (25) vs lines expressing it (25) | 2.84× lower at baseline in the lines without TCF4 | 0.005 | ⚠ within organs, on part of the lines; also absent: KCNT2, APCDD1L, MSC-AS1; co-absent with the target |
| [[CDH13]] | C | CDH13 activity raises PDCD1LG2's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 3.20× lower at baseline in the lines without CDH13 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |
| [[BNC2]] | C | BNC2 activity raises PDCD1LG2's level | lines that do not express BNC2 (21) vs lines expressing it (29) | 3.21× lower at baseline in the lines without BNC2 | 0.008 | ⚠ within organs, on part of the lines; also absent: LINC03041, DPY19L2, RNF182; co-absent with the target |
| [[MIR100HG]] | C | MIR100HG activity raises PDCD1LG2's level | lines that do not express MIR100HG (20) vs lines expressing it (30) | 3.42× lower at baseline in the lines without MIR100HG | 0.008 | ⚠ within organs, on part of the lines; also absent: DOCK10, ADAM12, GFPT2; co-absent with the target |

### Downstream of this gene

*42 arrows, 42 of them with an alert ⚠; grade A 0, B 14, C 28. Shown: the 12 strongest; 30 more arrows (30 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABL2]] | B | PDCD1LG2 activity raises ABL2's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 2.11× lower at baseline in the lines without PDCD1LG2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L |
| [[FRMD6]] | B | PDCD1LG2 activity raises FRMD6's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 3.81× lower at baseline in the lines without PDCD1LG2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L |
| [[RPSAP52]] | B | PDCD1LG2 activity raises RPSAP52's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 2.45× lower at baseline in the lines without PDCD1LG2 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L |
| [[FHAD1]] | B | PDCD1LG2 activity raises FHAD1's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 1.68× lower at baseline in the lines without PDCD1LG2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L |
| [[ETS1]] | B | PDCD1LG2 activity raises ETS1's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 3.05× lower at baseline in the lines without PDCD1LG2 | 0.049 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L |
| [[ARHGAP31]] | B | PDCD1LG2 activity raises ARHGAP31's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 3.05× lower at baseline in the lines without PDCD1LG2 | 0.051 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L |
| [[SCHIP1]] | B | PDCD1LG2 activity raises SCHIP1's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 2.33× lower at baseline in the lines without PDCD1LG2 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L |
| [[STARD13]] | B | PDCD1LG2 activity raises STARD13's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 2.57× lower at baseline in the lines without PDCD1LG2 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L |
| [[PDE4DIPP2]] | B | PDCD1LG2 activity raises PDE4DIPP2's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 2.55× lower at baseline in the lines without PDCD1LG2 | 0.076 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L |
| [[NEMP2]] | B | PDCD1LG2 activity raises NEMP2's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 1.77× lower at baseline in the lines without PDCD1LG2 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L |
| cells under [[Riluzole hydrochloride (drug)]] 0.05 µM | B | PDCD1LG2 activity lowers the cells' numbers under Riluzole hydrochloride 0.05 µM (makes them more sensitive) | lines that do not express PDCD1LG2 (28) vs lines expressing it (20) | the lines without PDCD1LG2: 1.17× the cells of the other lines | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L |
| [[RGMB]] | B | PDCD1LG2 activity raises RGMB's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 1.85× lower at baseline in the lines without PDCD1LG2 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L |

## Where it sits

- **Module**: [[Module 116]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.669). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.7, 15.2); signed map (16.6, 45.9). **Vector** length 69.8, 22.8% of its response variance represented; |z| ≥ 3 in 508 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.5 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +9.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +6.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.7 | +4.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +2.5 | +4.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.3 | +4.9 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM |  | -2.5 | -3.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.4 | -0.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.9 | -2.0 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.8 | -3.7 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -2.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.6 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | programmed cell death 1 ligand 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9p24.1 — chr9:5,510,531-5,571,282 (+) |
| Ensembl biotype | protein_coding |
| Also known as | PD-L2, Btdc, PDL2, bA574F11.2, CD273, B7-DC, B7DC |
| Gene groups (HGNC) | CD molecules; Receptor ligands; Immunoglobulin like domain containing; B7 family |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 6 pathways, smallest: PD-L1(CD274) glycosylation and translocation to plasma membrane; Regulation of PD-L1(CD274) Post-translational modification; Regulation of PD-L1(CD274) expression |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BQ51](https://www.uniprot.org/uniprotkb/Q9BQ51) (Programmed cell death 1 ligand 2):

> Plays a critical role in induction and maintenance of immune tolerance to self. Acts as a ligand for the inhibitory receptor PDCD1/PD-1, inhibiting T-cell proliferation by blocking cell cycle progression and cytokine production.

**Summary**, from NCBI Gene [80380](https://www.ncbi.nlm.nih.gov/gene/80380):

> Enables receptor ligand activity. Involved in negative regulation of T cell receptor signaling pathway; negative regulation of activated T cell proliferation; and negative regulation of cytokine production. Is active in plasma membrane. Biomarker of pulmonary tuberculosis. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:18731](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18731) · Entrez [80380](https://www.ncbi.nlm.nih.gov/gene/80380) · UniProt [Q9BQ51](https://www.uniprot.org/uniprotkb/Q9BQ51) · Ensembl [ENSG00000197646](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197646)

## Data

Gene col 12437: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12437); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12437, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12437]; `tensor/DDL_lfc|DDL_z.npy` [12437]; `embed/gene_vectors.npy` [12437]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12437 or target_col == 12437). Every well: [[PDCD1LG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDCD1LG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
