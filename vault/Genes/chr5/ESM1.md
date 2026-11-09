---
symbol: "ESM1"
type: "gene"
col: 8916
ensembl_id: "ENSG00000164283"
name: "endothelial cell specific molecule 1"
location: "5q11.2"
module: 19
arm: "+"
pooled_cpm: 14.22
n_lines_expressing: 13
n_dd_up: 8
n_dd_down: 3
n_dd_up_clean: 5
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 11
direction_downstream: 27
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# ESM1

*endothelial cell specific molecule 1* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.66× (z +8.4, q 3e-14, up in 3 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Peretinoin (drug)]] 0.5 µM: 2.23× (z +4.3, q 0.002, up in 7 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Trametinib (drug)]] 5 µM: 0.423× (z -4.5, q 0.004, down in 8 of 10 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC02742]] (+0.78, fdr 7e-06), [[SERPIND1]] (+0.74, fdr 7e-06), [[PDCD1LG2]] (+0.71, fdr 7e-06); moves opposite to [[ROR2]] (-0.46, fdr 1e-04).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[IL13RA2]] → it (grade C ⚠); 27 go from it, the strongest it → [[NEMP2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8916.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.66×** | +8.4 | 3e-14 | 3/6 (LOX-IMVI, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.19×** | +6.1 | 4e-07 | 2/5 (LOX-IMVI, Hs 766T) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Peretinoin (drug)]] 0.5 µM |  | **2.23×** | +4.3 | 0.002 | 7/9 (Hs 766T, NCI-H460, …) | all doses, flat | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.36×** | +4.3 | 0.002 | 1/5 (LOX-IMVI) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Vilanterol (drug)]] 5 µM |  | **1.58×** | +3.5 | 0.053 | 4/9 (LOX-IMVI, NCI-H460, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 5 µM |  | **1.91×** | +3.4 | 0.068 | 7/9 (Hs 766T, LOX-IMVI, …) | all doses, flat | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.85×** | +3.3 | 0.072 | 2/9 (Hs 766T, hTERT-HPNE) | top dose only |  |
| [[Vilanterol (drug)]] 0.5 µM |  | **1.82×** | +3.2 | 0.082 | 4/9 (hTERT-HPNE, NCI-H460, …) | rises with dose | position effect removed |
| [[vincristine (drug)]] 0.5 µM |  | 2.52× | +3.1 | 0.11 | 4/9 (Hs 766T, NCI-H2030, …) | two highest doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.76× | +3.1 | 0.12 | 6/9 (H4, Hs 766T, …) | two highest doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | 1.74× | +3.0 | 0.13 | 1/9 (hTERT-HPNE) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8916.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.423×** | -4.5 | 0.004 | 8/10 (NCI-H460, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.447×** | -4.1 | 0.013 | 7/9 (NCI-H460, Hs 766T, …) | all doses, flat |  |
| [[Belinostat (drug)]] 5 µM |  | **0.490×** | -3.9 | 0.018 | 7/9 (NCI-H460, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Trametinib (drug)]] 0.05 µM |  | 0.642× | -3.4 | 0.10 | 5/9 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.608× | -3.2 | 0.11 | 9/9 (NCI-H460, J82, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 0.593× | -3.2 | 0.11 | 7/9 (NCI-H460, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | 0.662× | -3.2 | 0.11 | 6/9 (NCI-H460, Hs 766T, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.562× | -3.2 | 0.11 | 6/9 (NCI-H460, H4, …) | inconsistent across doses | position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | 0.576× | -3.1 | 0.12 | 7/10 (NCI-H460, LOX-IMVI, …) | all doses, flat | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.573× | -3.1 | 0.13 | 2/9 (NCI-H460, H4) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.05 per unit of S-phase module lfc, +0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8916. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 169 | 0 | 33 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0217× (z -26.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Trametinib (drug)]] 5 µM 0.0112× (z -22.5) |
| [[Hs 766T (line)]] | wt | 39.7 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0305× (z -13.5) |
| [[J82 (line)]] | alt | 11.6 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0622× (z -13.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Tadalafil (drug)]] 5 µM 0.0567× (z -9.4) |
| [[LOX-IMVI (line)]] | wt | 126 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -11.3) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Trametinib (drug)]] 5 µM 0.0730× (z -9.8) |
| [[A-172 (line)]] | wt | 11.9 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0617× (z -8.5) |
| [[RKO (line)]] | wt | 7.25 | 0 | 1 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.0218× (z -9.3) |
| [[A-427 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.51 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.55 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.47 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.94 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.70 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.31 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.55 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 3.81 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.33 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.48 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.65 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.36 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.31 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.86 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.81 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8916), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC02742]] | +0.78 | +0.77 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[SERPIND1]] | +0.74 | +0.66 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[PDCD1LG2]] | +0.71 | +0.72 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[CTNND2]] | +0.68 | +0.70 / +0.58 | both halves | 8e-06 |  |
| [[KCNK2]] | +0.67 | +0.64 / +0.61 | both halves | 7e-06 |  |
| [[GABBR2]] | +0.67 | +0.68 / +0.58 | both halves | 8e-06 | **novel candidate** |
| [[PDE1C]] | +0.65 | +0.57 / +0.59 | both halves | 1e-05 | **novel candidate** |
| [[NCKAP5-AS2]] | +0.65 | +0.66 / +0.51 | both halves | 1e-05 |  |
| [[MARCHF4]] | +0.64 | +0.55 / +0.66 | both halves | 1e-05 |  |
| [[SERPINB11]] | +0.63 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[RAB3B]] | +0.61 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[ADAMTS6]] | +0.61 | +0.62 / +0.61 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ROR2]] | -0.46 | -0.48 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL13RA2]] | C | IL13RA2 activity raises ESM1's level | lines that do not express IL13RA2 (36) vs lines expressing it (14) | 3.63× lower at baseline in the lines without IL13RA2 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286523, LINC02476, PAX3; co-absent with the target |
| [[SLITRK4]] | C | SLITRK4 activity raises ESM1's level | lines that do not express SLITRK4 (36) vs lines expressing it (14) | 2.72× lower at baseline in the lines without SLITRK4 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AJAP1, ENSG00000238054, GLP2R; co-absent with the target |
| [[LNCOG]] | C | LNCOG activity raises ESM1's level | lines that do not express LNCOG (30) vs lines expressing it (20) | 2.95× lower at baseline in the lines without LNCOG | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GYPC, HS3ST3A1, LAMA1; co-absent with the target |
| [[GTF2I-AS1]] | C | GTF2I-AS1 activity raises ESM1's level | lines that do not express GTF2I-AS1 (44) vs lines expressing it (6) | 3.13× lower at baseline in the lines without GTF2I-AS1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, SLC15A5, LINC03000; maybe low, not absent; co-absent with the target |
| [[ADAMTS6]] | C | ADAMTS6 activity raises ESM1's level | lines that do not express ADAMTS6 (25) vs lines expressing it (25) | 2.87× lower at baseline in the lines without ADAMTS6 | 0.028 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: FLI1, PDCD1LG2, TENM2; co-absent with the target |
| [[LINC03000]] | C | LINC03000 activity raises ESM1's level | lines that do not express LINC03000 (44) vs lines expressing it (6) | 3.29× lower at baseline in the lines without LINC03000 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GSG1L2, ENSG00000238054, SYT4; co-absent with the target |
| [[RTN1]] | C | RTN1 activity raises ESM1's level | lines that do not express RTN1 (31) vs lines expressing it (19) | 2.77× lower at baseline in the lines without RTN1 | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC01010, RIT2, ENSG00000289530; co-absent with the target |
| [[CDH11]] | C | CDH11 activity raises ESM1's level | lines that do not express CDH11 (36) vs lines expressing it (14) | 2.23× lower at baseline in the lines without CDH11 | 0.058 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SOX11, ENSG00000253693, ENSG00000238054; co-absent with the target |
| [[PDCD1LG2]] | C | PDCD1LG2 activity raises ESM1's level | lines that do not express PDCD1LG2 (28) vs lines expressing it (22) | 2.60× lower at baseline in the lines without PDCD1LG2 | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ADAMTS12, FN1, APCDD1L; co-absent with the target |
| [[GREM2]] | C | GREM2 activity raises ESM1's level | lines that do not express GREM2 (40) vs lines expressing it (10) | 2.49× lower at baseline in the lines without GREM2 | 0.077 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC03000, GSG1L2, ENSG00000238054; co-absent with the target |
| [[CTNND2]] | C | CTNND2 activity raises ESM1's level | lines that do not express CTNND2 (40) vs lines expressing it (10) | 2.64× lower at baseline in the lines without CTNND2 | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DPP10, GSG1L2, RIT2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*27 arrows, 27 of them with an alert ⚠; grade A 0, B 11, C 16. Shown: the 12 strongest; 15 more arrows (15 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NEMP2]] | B | ESM1 activity raises NEMP2's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 2.87× lower at baseline in the lines without ESM1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865 |
| [[ARHGAP31]] | B | ESM1 activity raises ARHGAP31's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 3.23× lower at baseline in the lines without ESM1 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865 |
| [[DOCK4]] | B | ESM1 activity raises DOCK4's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 2.28× lower at baseline in the lines without ESM1 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865 |
| [[ARHGAP31]] | B | ESM1 activity strengthens ARHGAP31's drug response | lines that do not express ESM1 (27) vs lines expressing it (11) | the lines without ESM1 respond 0.81× as strongly (z diff +1.28); strongest at Trametinib 5 µM: 0.56x vs 0.43x (z diff +2.6) | 0.045 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865; target measured in part of the lines; artifact flags |
| [[CD274]] | B | ESM1 activity raises CD274's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 2.34× lower at baseline in the lines without ESM1 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865 |
| [[SERPIND1]] | B | ESM1 activity raises SERPIND1's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 1.33× lower at baseline in the lines without ESM1 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865 |
| cells under [[Omeprazole (drug)]] 0.05 µM | B | ESM1 activity raises the cells' numbers under Omeprazole 0.05 µM (protects the cells) | lines that do not express ESM1 (37) vs lines expressing it (11) | the lines without ESM1: 0.82× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865 |
| cells under [[Vinblastine (sulfate) (drug)]] 0.05 µM | B | ESM1 activity lowers the cells' numbers under Vinblastine (sulfate) 0.05 µM (makes them more sensitive) | lines that do not express ESM1 (37) vs lines expressing it (11) | the lines without ESM1: 1.18× the cells of the other lines | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865 |
| [[KIFC3]] | B | ESM1 activity raises KIFC3's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 1.67× lower at baseline in the lines without ESM1 | 0.084 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865 |
| cells under [[Vinblastine (sulfate) (drug)]] 5 µM | B | ESM1 activity lowers the cells' numbers under Vinblastine (sulfate) 5 µM (makes them more sensitive) | lines that do not express ESM1 (37) vs lines expressing it (11) | the lines without ESM1: 1.18× the cells of the other lines | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865 |
| [[RAB3B]] | B | ESM1 activity raises RAB3B's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 2.10× lower at baseline in the lines without ESM1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865 |
| [[LNCOG]] | C | ESM1 activity raises LNCOG's level | lines that do not express ESM1 (37) vs lines expressing it (13) | 3.50× lower at baseline in the lines without ESM1 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, DIRAS3, ENSG00000224865; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.609). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.5, 15.5); signed map (42.4, 46.1). **Vector** length 60.1, 24.6% of its response variance represented; |z| ≥ 3 in 422 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +6.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +8.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | +2.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | -0.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | +1.6 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +2.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.5 | +4.3 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.3 | +3.4 |
| fall | [[Trametinib (drug)]] 5 µM |  | -2.6 | -4.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.4 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.8 | -2.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -1.8 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -1.8 | -3.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.6 | -3.2 |

## What is on record

|  |  |
|---|---|
| Name | endothelial cell specific molecule 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.2 — chr5:54,977,867-55,022,671 (-) |
| Ensembl biotype | protein_coding |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NQ30](https://www.uniprot.org/uniprotkb/Q9NQ30) (Endothelial cell-specific molecule 1):

> Involved in angiogenesis; promotes angiogenic sprouting. May have potent implications in lung endothelial cell-leukocyte interactions.

**Summary**, from NCBI Gene [11082](https://www.ncbi.nlm.nih.gov/gene/11082):

> This gene encodes a secreted protein which is mainly expressed in the endothelial cells in human lung and kidney tissues. The expression of this gene is regulated by cytokines, suggesting that it may play a role in endothelium-dependent pathological disorders. The transcript contains multiple polyadenylation and mRNA instability signals. Two transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:3466](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3466) · Entrez [11082](https://www.ncbi.nlm.nih.gov/gene/11082) · UniProt [Q9NQ30](https://www.uniprot.org/uniprotkb/Q9NQ30) · Ensembl [ENSG00000164283](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164283)

## Data

Gene col 8916: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8916); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8916, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8916]; `tensor/DDL_lfc|DDL_z.npy` [8916]; `embed/gene_vectors.npy` [8916]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8916 or target_col == 8916). Every well: [[ESM1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ESM1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
