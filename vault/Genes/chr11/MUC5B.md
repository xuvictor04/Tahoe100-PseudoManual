---
symbol: "MUC5B"
type: "gene"
col: 3957
ensembl_id: "ENSG00000117983"
name: "mucin 5B, oligomeric mucus/gel-forming"
location: "11p15.5"
module: 44
arm: "+"
pooled_cpm: 4.28
n_lines_expressing: 13
n_dd_up: 15
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 119
direction_downstream: 139
tags: ["gene", "module/044"]
generated_by: "tahoemap"
---

# MUC5B

*mucin 5B, oligomeric mucus/gel-forming* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.19× (z +8.0, q 6e-13, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.23× (z +5.6, q 3e-06, up in 4 of 10 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (LS 180 0.0437×, BT-474 0.0713×, HT-29 0.0432×, KATO III 0.0866×); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (LS 180 0.0295×, HT-29 0.0136×, BT-474 0.0349×; ⚠ cell-cycle shift, explains ~0% of this change); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (KATO III 0.105×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ST6GALNAC1]] (+0.86, fdr 7e-06), [[PPP1R1B]] (+0.85, fdr 7e-06), [[UGT1A1]] (+0.78, fdr 7e-06).
> It is in [[Module 044]], a single-armed module (Defective GALNT12 causes CRCS1).
> Probable direction (from the cell lines, not proof of direct regulation): 119 arrows point to it, the strongest [[BOLA3-DT]] → it (grade B ⚠); 139 go from it, the strongest it → [[FAM83E]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 8 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3957.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.19×** | +8.0 | 6e-13 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.82×** | +7.8 | 2e-12 | 1/6 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.88×** | +7.0 | 4e-10 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.23×** | +5.6 | 3e-06 | 4/10 (NCI-H2347, AsPC-1, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.57×** | +4.5 | 7e-04 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.78×** | +4.5 | 7e-04 | 0/6 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.57×** | +4.1 | 0.003 | 1/9 (NCI-H2347) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **2.19×** | +3.9 | 0.007 | 4/9 (LS 180, KATO III, …) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.71×** | +3.5 | 0.026 | 1/7 (NCI-H2347) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.65×** | +3.5 | 0.026 | 1/10 (CFPAC-1) | top dose only | cell-cycle shift (explains ~18% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | **2.18×** | +3.4 | 0.030 | 0/8 | inconsistent across doses | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.60×** | +3.3 | 0.042 | 0/0 | top dose only | noisy plate (z scaled); position effect removed |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.89×** | +3.1 | 0.072 | 0/9 | inconsistent across doses | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.87×** | +3.1 | 0.083 | 0/6 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.85×** | +3.0 | 0.088 | 0/8 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3957.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (LS 180 0.0437×, BT-474 0.0713×, HT-29 0.0432×, KATO III 0.0866×); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (LS 180 0.0295×, HT-29 0.0136×, BT-474 0.0349×; ⚠ cell-cycle shift, explains ~0% of this change); [[Vinblastine (sulfate) (drug)]] 5 µM in 1 line (KATO III 0.105×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mebendazole (drug)]] 5 µM |  | 0.483× | -3.2 | 0.52 | 2/11 (A549, COLO 205) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3957. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 13.3 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0713× (z -10.1) |
| [[HT-29 (line)]] | alt | 9.75 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0432× (z -10.0) |
| [[KATO III (line)]] | alt | 11.3 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0866× (z -9.6) |
| [[LS 180 (line)]] | wt | 127 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0437× (z -14.9) |
| [[A-172 (line)]] | wt | 0.367 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.248 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.245 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.22 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.459 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.66 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.273 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.472 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.311 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.272 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.286 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.615 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.354 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.260 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.901 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.228 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.357 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.254 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.553 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.310 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.187 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.911 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.201 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.226 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.235 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.266 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 4.43 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.305 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.272 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.304 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.457 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.222 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.342 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 0.629 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.375 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.376 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.329 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.322 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3957), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ST6GALNAC1]] | +0.86 | +0.81 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[PPP1R1B]] | +0.85 | +0.83 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[UGT1A1]] | +0.78 | +0.69 / +0.76 | both halves | 7e-06 | pathway: Diseases of metabolism |
| [[GPX2]] | +0.78 | +0.70 / +0.77 | both halves | 7e-06 |  |
| [[C9orf152]] | +0.77 | +0.77 / +0.76 | both halves | 7e-06 |  |
| [[FXYD3]] | +0.77 | +0.73 / +0.68 | both halves | 7e-06 | same gene group |
| [[PROM2]] | +0.76 | +0.73 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[LGALS4]] | +0.76 | +0.74 / +0.72 | both halves | 7e-06 |  |
| [[PRR15]] | +0.75 | +0.69 / +0.71 | both halves | 7e-06 |  |
| [[PRR15L]] | +0.75 | +0.73 / +0.70 | both halves | 7e-06 |  |
| [[CATSPERB]] | +0.75 | +0.75 / +0.64 | both halves | 7e-06 |  |
| [[SLC6A14]] | +0.74 | +0.68 / +0.70 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*119 arrows, 119 of them with an alert ⚠; grade A 0, B 3, C 116. Shown: the 12 strongest; 107 more arrows (107 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BOLA3-DT]] | B | BOLA3-DT activity lowers MUC5B's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 3.58× higher at baseline in the lines without BOLA3-DT | 0.060 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[SRMS]] | B | SRMS activity raises MUC5B's level | lines that do not express SRMS (14) vs lines expressing it (36) | 1.95× lower at baseline in the lines without SRMS | 0.060 | ⚠ within organs, on part of the lines; also absent: MX1, OAS2, RSAD2 |
| [[PLEKHS1]] | B | PLEKHS1 activity raises MUC5B's level | lines that do not express PLEKHS1 (15) vs lines expressing it (35) | 1.90× lower at baseline in the lines without PLEKHS1 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000261227, CYP4F3, CRYM; maybe low, not absent |
| [[AGR3]] | C | AGR3 activity raises MUC5B's level | lines that do not express AGR3 (42) vs lines expressing it (8) | 9.06× lower at baseline in the lines without AGR3 | 1e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17; co-absent with the target |
| [[TCN1]] | C | TCN1 activity raises MUC5B's level | lines that do not express TCN1 (37) vs lines expressing it (13) | 4.67× lower at baseline in the lines without TCN1 | 2e-04 | ⚠ within organs, on part of the lines; also absent: AGR3, MUC5AC, MUC5B; co-absent with the target |
| [[MUC5AC]] | C | MUC5AC activity raises MUC5B's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 4.58× lower at baseline in the lines without MUC5AC | 3e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3; co-absent with the target |
| [[PIGR]] | C | PIGR activity raises MUC5B's level | lines that do not express PIGR (45) vs lines expressing it (5) | 5.74× lower at baseline in the lines without PIGR | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, TM4SF4, APOB; co-absent with the target |
| [[FGFR2]] | C | FGFR2 activity raises MUC5B's level | lines that do not express FGFR2 (44) vs lines expressing it (6) | 7.55× lower at baseline in the lines without FGFR2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, REG4, APOA2; co-absent with the target |
| [[TM4SF4]] | C | TM4SF4 activity raises MUC5B's level | lines that do not express TM4SF4 (42) vs lines expressing it (8) | 4.27× lower at baseline in the lines without TM4SF4 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PIGR, MUC17, HHLA2; co-absent with the target |
| [[SLC6A14]] | C | SLC6A14 activity raises MUC5B's level | lines that do not express SLC6A14 (39) vs lines expressing it (11) | 4.64× lower at baseline in the lines without SLC6A14 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: DAPP1, MUC5AC, ST6GALNAC1; co-absent with the target |
| [[SLC28A3]] | C | SLC28A3 activity raises MUC5B's level | lines that do not express SLC28A3 (34) vs lines expressing it (16) | 3.34× lower at baseline in the lines without SLC28A3 | 0.001 | ⚠ within organs, on part of the lines; also absent: CFTR, DAPP1, SLC6A14; co-absent with the target |
| [[ST6GALNAC1]] | C | ST6GALNAC1 activity raises MUC5B's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 3.57× lower at baseline in the lines without ST6GALNAC1 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4; co-absent with the target |

### Downstream of this gene

*139 arrows, 139 of them with an alert ⚠; grade A 0, B 33, C 106. Shown: the 12 strongest; 127 more arrows (127 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM83E]] | B | MUC5B activity raises FAM83E's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 3.85× lower at baseline in the lines without MUC5B | 0.001 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[PROM2]] | B | MUC5B activity raises PROM2's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 3.18× lower at baseline in the lines without MUC5B | 0.001 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[STS]] | B | MUC5B activity raises STS's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 3.29× lower at baseline in the lines without MUC5B | 0.003 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[LGALS9]] | B | MUC5B activity raises LGALS9's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 3.61× lower at baseline in the lines without MUC5B | 0.004 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[FZD5]] | B | MUC5B activity raises FZD5's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 1.98× lower at baseline in the lines without MUC5B | 0.004 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[AQP3]] | B | MUC5B activity raises AQP3's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 2.58× lower at baseline in the lines without MUC5B | 0.008 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[BAG1]] | B | MUC5B activity raises BAG1's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 1.78× lower at baseline in the lines without MUC5B | 0.009 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[SLC12A2]] | B | MUC5B activity raises SLC12A2's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 2.13× lower at baseline in the lines without MUC5B | 0.012 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[BOLA3-DT]] | B | MUC5B activity lowers BOLA3-DT's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 1.84× higher at baseline in the lines without MUC5B | 0.013 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[FAM83E]] | B | MUC5B activity weakens FAM83E's drug response | lines that do not express MUC5B (25) vs lines expressing it (11) | (z diff -2.36); strongest at Homoharringtonine 5 µM: 1.58x vs 0.32x (z diff -9.1) | 0.013 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925; target measured in part of the lines; artifact flags |
| [[ARHGEF16]] | B | MUC5B activity raises ARHGEF16's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 2.05× lower at baseline in the lines without MUC5B | 0.013 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |
| [[ABHD11]] | B | MUC5B activity raises ABHD11's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 2.35× lower at baseline in the lines without MUC5B | 0.016 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925 |

## Where it sits

- **Module**: [[Module 044]] — Defective GALNT12 causes CRCS1; 102 genes; every member is in the + arm (projection on the module's main direction 0.801). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.0, 51.2); signed map (63.9, 5.7). **Vector** length 44.9, 16.9% of its response variance represented; |z| ≥ 3 in 289 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Glucuronidation* (reactome, mean cos +0.66 to 4); *Aspirin ADME* (reactome, mean cos +0.66 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.0 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.0 | +5.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.4 | +3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.0 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.3 | +2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +3.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.0 | +1.6 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -1.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.8 | -1.6 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.7 | -0.5 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -1.6 | -0.8 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.3 | +0.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -3.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | mucin 5B, oligomeric mucus/gel-forming |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:1,223,066-1,262,172 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MG1, MUC-5B; previously MUC5 |
| Gene groups (HGNC) | Mucins; MicroRNA protein coding host genes |
| Reactome | 12 pathways, smallest: Defective GALNT12 causes CRCS1; Defective GALNT3 causes HFTC; Defective C1GALT1C1 causes TNPS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HC84](https://www.uniprot.org/uniprotkb/Q9HC84) (Mucin-5B):

> Gel-forming mucin that is thought to contribute to the lubricating and viscoelastic properties of whole saliva and cervical mucus.

**Summary**, from NCBI Gene [727897](https://www.ncbi.nlm.nih.gov/gene/727897):

> This gene encodes a member of the mucin family of proteins, which are highly glycosylated macromolecular components of mucus secretions. This family member is the major gel-forming mucin in mucus. It is a major contributor to the lubricating and viscoelastic properties of whole saliva, normal lung mucus and cervical mucus. This gene has been found to be up-regulated in some human diseases, including sinus mucosa of chronic rhinosinusitis (CRS), CRS with nasal polyposis, chronic obstructive …

**Accessions** — [HGNC:7516](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7516) · Entrez [727897](https://www.ncbi.nlm.nih.gov/gene/727897) · UniProt [Q9HC84](https://www.uniprot.org/uniprotkb/Q9HC84) · Ensembl [ENSG00000117983](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000117983)

## Data

Gene col 3957: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3957); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3957, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3957]; `tensor/DDL_lfc|DDL_z.npy` [3957]; `embed/gene_vectors.npy` [3957]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3957 or target_col == 3957). Every well: [[MUC5B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MUC5B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
