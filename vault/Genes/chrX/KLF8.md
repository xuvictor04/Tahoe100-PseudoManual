---
symbol: "KLF8"
type: "gene"
col: 2240
ensembl_id: "ENSG00000102349"
name: "KLF transcription factor 8"
location: "Xp11.21"
module: 8
arm: "+"
pooled_cpm: 2.43
n_lines_expressing: 23
n_dd_up: 21
n_dd_down: 5
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 10
direction_downstream: 13
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# KLF8

*KLF transcription factor 8* — Xp11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.70× (z +12.7, q 3e-34, up in 1 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[XRK3F2 (drug)]] 0.5 µM: 2.16× (z +4.2, q 0.002, up in 0 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (5 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.543× (z -4.7, q 0.002, down in 8 of 18 measured lines) ⚠ unreliable plate only. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H1573 0.0507×, NCI-H1792 0.169×, RPMI-7951 0.0727×, NCI-H2347 0.296×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (HT-29 0.0344×; ⚠ cell-cycle shift, explains ~36% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H2347 0.127×; ⚠ cell-cycle shift, explains ~60% of this change); [[Sulfatinib (drug)]] 5 µM in 1 line (NCI-H1573 0.0457×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (LS 180 0.0670×).
> Its strongest partners by |cos| (96 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC01456]] (+0.57, fdr 7e-05), [[CATSPERB]] (+0.55, fdr 2e-05), [[SLC28A3]] (+0.54, fdr 4e-05); moves opposite to [[FBXO17]] (-0.40, fdr 2e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[DPP4]] → it (grade B ⚠); 13 go from it, the strongest it → [[BICDL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 9 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2240.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.70×** | +12.7 | 3e-34 | 1/4 (HT-29) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.42×** | +10.4 | 6e-23 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.32×** | +9.1 | 2e-17 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.91×** | +5.8 | 1e-06 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.53×** | +4.6 | 6e-04 | 2/19 (NCI-H1792, BT-474) | all doses, stronger at high dose | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.83×** | +4.4 | 1e-03 | 0/10 | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.80×** | +4.3 | 0.002 | 1/11 (NCI-H23) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.16×** | +4.2 | 0.002 | 0/9 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.47×** | +4.1 | 0.003 | 3/19 (Panc 03.27, KATO III, …) | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.67×** | +3.9 | 0.006 | 2/10 (HT-29, BT-474) | inconsistent across doses | low cells (technical?) |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.66×** | +3.8 | 0.007 | 0/14 | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.8 | 0.007 | 0/20 | top dose only |  |
| [[Pimozide (drug)]] 0.05 µM |  | **1.57×** | +3.4 | 0.030 | 1/11 (HT-29) | inconsistent across doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **1.58×** | +3.3 | 0.033 | 5/14 (RPMI-7951, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.54×** | +3.2 | 0.043 | 3/14 (NCI-H23, RPMI-7951, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.52×** | +3.2 | 0.048 | 1/12 (NCI-H23) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.50×** | +3.1 | 0.070 | 3/13 (NCI-H2347, HOP62, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.50×** | +3.0 | 0.070 | 1/11 (NCI-H1792) | inconsistent across doses |  |
| [[Orlistat (drug)]] 0.05 µM |  | **1.52×** | +2.9 | 0.094 | 0/11 | inconsistent across doses |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.32×** | +2.9 | 0.094 | 0/13 | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2240.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 9 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H1573 0.0507×, NCI-H1792 0.169×, RPMI-7951 0.0727×, NCI-H2347 0.296×; ⚠ cell-cycle shift, would explain all of this change); [[Digitoxin (drug)]] 0.5 µM in 1 line (HT-29 0.0344×; ⚠ cell-cycle shift, explains ~36% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H2347 0.127×; ⚠ cell-cycle shift, explains ~60% of this change); [[Sulfatinib (drug)]] 5 µM in 1 line (NCI-H1573 0.0457×); [[Medroxyprogesterone acetate (drug)]] 0.5 µM in 1 line (LS 180 0.0670×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.543×** | -4.7 | 0.002 | 8/18 (HT-29, hTERT-HPNE, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.544×** | -4.5 | 0.002 | 10/17 (NCI-H1792, NCI-H2347, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.610×** | -3.8 | 0.023 | 14/19 (HT-29, RPMI-7951, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~36% of this change | **0.611×** | -3.8 | 0.023 | 10/17 (HT-29, BT-474, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **0.622×** | -3.6 | 0.032 | 11/18 (NCI-H2347, NCI-H23, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | 0.646× | -3.2 | 0.12 | 3/19 (SHP-77, SW 900, …) | top dose only |  |
| [[Omeprazole (sodium) (drug)]] 0.5 µM |  | 0.673× | -3.0 | 0.19 | 2/18 (KATO III, RPMI-7951) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.49 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2240. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 7.78 | 0 | 4 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0344× (z -12.6) ⚠ cell-cycle shift, explains ~36% of this change |
| [[NCI-H1792 (line)]] | alt | 13.6 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.169× (z -12.7) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H1573 (line)]] | alt | 5.68 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0507× (z -14.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Sulfatinib (drug)]] 5 µM 0.0457× (z -9.9) |
| [[NCI-H2347 (line)]] | alt | 17.5 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.127× (z -12.2) ⚠ cell-cycle shift, explains ~60% of this change |
| [[LS 180 (line)]] | wt | 5.77 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.0670× (z -9.7) |
| [[RPMI-7951 (line)]] | alt | 6.83 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0727× (z -12.4) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.314 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.146 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.420 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.264 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.234 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.213 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.209 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.395 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.251 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.241 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.665 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.510 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.86 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.280 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.934 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.216 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.176 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.318 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.229 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.140 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.296 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.604 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.283 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.14 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.211 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.232 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.205 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.255 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.677 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.877 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 0.316 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2240), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC01456]] | +0.57 | +0.60 / +0.38 | both halves | 7e-05 | **novel candidate** |
| [[CATSPERB]] | +0.55 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[SLC28A3]] | +0.54 | +0.56 / +0.40 | both halves | 4e-05 |  |
| [[TSPAN1]] | +0.54 | +0.42 / +0.40 | both halves | 5e-05 |  |
| [[MGC32805]] | +0.54 | +0.47 / +0.42 | both halves | 4e-05 |  |
| [[PROM2]] | +0.53 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[NSUN7]] | +0.53 | +0.49 / +0.44 | both halves | 3e-05 |  |
| [[RGS6]] | +0.53 | +0.36 / +0.39 | both halves | 1e-04 |  |
| [[ITGB6]] | +0.52 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[TMEM184A]] | +0.52 | +0.45 / +0.43 | both halves | 3e-05 |  |
| [[CEACAM5]] | +0.51 | +0.44 / +0.42 | both halves | 4e-05 |  |
| [[KLHL2P1]] | +0.51 | +0.52 / +0.39 | both halves | 5e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO17]] | -0.40 | -0.34 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 3, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DPP4]] | B | DPP4 activity raises KLF8's level | lines that do not express DPP4 (29) vs lines expressing it (21) | 1.50× lower at baseline in the lines without DPP4 | 0.023 | ⚠ within organs, on part of the lines; also absent: LCN2, INAVA, KLK10 |
| [[PROM2]] | B | PROM2 activity raises KLF8's level | lines that do not express PROM2 (21) vs lines expressing it (29) | 1.87× lower at baseline in the lines without PROM2 | 0.037 | ⚠ within organs, on part of the lines; also absent: FAM83B, GRHL2, ANKRD22; maybe low, not absent |
| [[FRY]] | B | FRY activity raises KLF8's level | lines that do not express FRY (14) vs lines expressing it (36) | 2.06× lower at baseline in the lines without FRY | 0.067 | ⚠ within organs, on part of the lines; also absent: ADGRV1, DTNA, ZNF385B |
| [[ADCY4]] | C | ADCY4 activity raises KLF8's level | lines that do not express ADCY4 (33) vs lines expressing it (17) | 1.87× lower at baseline in the lines without ADCY4 | 0.016 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, SLC5A1, CLIC5; co-absent with the target |
| [[MAL2]] | C | MAL2 activity raises KLF8's level | lines that do not express MAL2 (31) vs lines expressing it (19) | 1.80× lower at baseline in the lines without MAL2 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: RAB25, TMEM125, CDH1; co-absent with the target |
| [[TSPAN1]] | C | TSPAN1 activity raises KLF8's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 1.75× lower at baseline in the lines without TSPAN1 | 0.035 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6; co-absent with the target |
| [[TMEM30B]] | C | TMEM30B activity raises KLF8's level | lines that do not express TMEM30B (35) vs lines expressing it (15) | 1.86× lower at baseline in the lines without TMEM30B | 0.046 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ANKRD22, RAB25; co-absent with the target |
| [[RORC]] | C | RORC activity raises KLF8's level | lines that do not express RORC (30) vs lines expressing it (20) | 1.88× lower at baseline in the lines without RORC | 0.049 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2; co-absent with the target |
| [[GRHL2]] | C | GRHL2 activity raises KLF8's level | lines that do not express GRHL2 (34) vs lines expressing it (16) | 1.86× lower at baseline in the lines without GRHL2 | 0.049 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with CDKN2A; also absent: TMEM30B, RAB25, TMPRSS4; co-absent with the target |
| [[ITGB6]] | C | ITGB6 activity raises KLF8's level | lines that do not express ITGB6 (32) vs lines expressing it (18) | 1.62× lower at baseline in the lines without ITGB6 | 0.090 | ⚠ within organs, on part of the lines; also absent: ST14, TMPRSS2, TMPRSS4; co-absent with the target |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 6, C 7. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BICDL2]] | B | KLF8 activity raises BICDL2's level | lines that do not express KLF8 (27) vs lines expressing it (23) | 2.16× lower at baseline in the lines without KLF8 | 0.038 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, LMO3, ENSG00000259692 |
| [[FAAH2]] | B | KLF8 activity raises FAAH2's level | lines that do not express KLF8 (27) vs lines expressing it (23) | 2.29× lower at baseline in the lines without KLF8 | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, LMO3, ENSG00000259692 |
| [[FBXO17]] | B | KLF8 activity weakens FBXO17's drug response | lines that do not express KLF8 (17) vs lines expressing it (13) | the lines without KLF8 respond 1.41× as strongly (z diff -2.63); strongest at Epirubicin (hydrochloride) 5 µM: 0.42x vs 0.68x (z diff -4.6) | 0.066 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, LMO3, ENSG00000259692; target measured in part of the lines; artifact flags |
| [[SPINT1-AS1]] | B | KLF8 activity raises SPINT1-AS1's level | lines that do not express KLF8 (27) vs lines expressing it (23) | 1.73× lower at baseline in the lines without KLF8 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, LMO3, ENSG00000259692 |
| [[SAMD12-AS1]] | B | KLF8 activity raises SAMD12-AS1's level | lines that do not express KLF8 (27) vs lines expressing it (23) | 2.05× lower at baseline in the lines without KLF8 | 0.095 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, LMO3, ENSG00000259692 |
| [[SPINT1]] | B | KLF8 activity raises SPINT1's level | lines that do not express KLF8 (27) vs lines expressing it (23) | 2.47× lower at baseline in the lines without KLF8 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, LMO3, ENSG00000259692 |
| [[MAL2]] | C | KLF8 activity raises MAL2's level | lines that do not express KLF8 (27) vs lines expressing it (23) | 3.27× lower at baseline in the lines without KLF8 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, LMO3, ENSG00000259692; co-absent with the target |
| [[GRHL2]] | C | KLF8 activity raises GRHL2's level | lines that do not express KLF8 (27) vs lines expressing it (23) | 3.35× lower at baseline in the lines without KLF8 | 0.050 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, LMO3, ENSG00000259692; co-absent with the target |
| [[SYK]] | C | KLF8 activity raises SYK's level | lines that do not express KLF8 (27) vs lines expressing it (23) | 1.93× lower at baseline in the lines without KLF8 | 0.076 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, LMO3, ENSG00000259692; co-absent with the target |
| [[TMEM125]] | C | KLF8 activity raises TMEM125's level | lines that do not express KLF8 (27) vs lines expressing it (23) | 1.73× lower at baseline in the lines without KLF8 | 0.083 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, LMO3, ENSG00000259692; co-absent with the target |
| [[ADGRF1]] | C | KLF8 activity raises ADGRF1's level | lines that do not express KLF8 (27) vs lines expressing it (23) | 2.60× lower at baseline in the lines without KLF8 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, LMO3, ENSG00000259692; co-absent with the target |
| [[TMEM30B]] | C | KLF8 activity raises TMEM30B's level | lines that do not express KLF8 (27) vs lines expressing it (23) | 2.35× lower at baseline in the lines without KLF8 | 0.093 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, LMO3, ENSG00000259692; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.503). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.2, 56.8); signed map (59.5, 7.1). **Vector** length 33.9, 6.33% of its response variance represented; |z| ≥ 3 in 479 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.5 | +2.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.9 | +10.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.9 | +4.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +12.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +2.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.1 | +3.8 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +0.9 | +3.2 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.9 | +2.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.8 | +0.4 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.6 | -0.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -0.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.6 | -1.3 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.6 | -1.3 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.5 | -2.0 |
|  | [[Methotrexate (drug)]] 5 µM |  | -0.5 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | KLF transcription factor 8 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.21 — chrX:56,232,356-56,291,531 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BKLF3, ZNF741, DXS741 |
| Gene groups (HGNC) | Zinc fingers C2H2-type; KLF transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [O95600](https://www.uniprot.org/uniprotkb/O95600) (Krueppel-like factor 8):

> Transcriptional repressor and activator. Binds to CACCC-boxes promoter elements. Also binds the GT-box of cyclin D1 promoter and mediates cell cycle progression at G(1) phase as a downstream target of focal adhesion kinase (FAK).

**Summary**, from NCBI Gene [11279](https://www.ncbi.nlm.nih.gov/gene/11279):

> This gene encodes a protein which is a member of the Sp/KLF family of transcription factors. Members of this family contain a C-terminal DNA-binding domain with three Kruppel-like zinc fingers. The encoded protein is thought to play an important role in the regulation of epithelial to mesenchymal transition, a process which occurs normally during development but also during metastasis. A pseudogene has been identified on chromosome 16. Alternative splicing results in multiple transcript …

**Accessions** — [HGNC:6351](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6351) · Entrez [11279](https://www.ncbi.nlm.nih.gov/gene/11279) · UniProt [O95600](https://www.uniprot.org/uniprotkb/O95600) · Ensembl [ENSG00000102349](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000102349)

## Data

Gene col 2240: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2240); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2240, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2240]; `tensor/DDL_lfc|DDL_z.npy` [2240]; `embed/gene_vectors.npy` [2240]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2240 or target_col == 2240). Every well: [[KLF8 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/KLF8.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
