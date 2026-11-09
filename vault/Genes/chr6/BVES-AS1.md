---
symbol: "BVES-AS1"
type: "gene"
col: 12792
ensembl_id: "ENSG00000203808"
name: "POPDC1 antisense RNA 1"
location: "6q21"
module: 102
arm: "+"
pooled_cpm: 2.03
n_lines_expressing: 33
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 12
direction_downstream: 2
tags: ["gene", "module/102"]
generated_by: "tahoemap"
---

# BVES-AS1

*POPDC1 antisense RNA 1* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (9 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.51× (z +11.8, q 2e-29, up in 14 of 20 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (2 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.573× (z -5.1, q 2e-04, down in 15 of 28 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Malotilate (drug)]] 5 µM: 0.680× (z -3.5, q 0.064, down in 5 of 27 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (PANC-1 0.211×, A549 0.0842×, NCI-H460 0.132×; ⚠ cell-cycle shift, would explain all of this change); [[Berberine (chloride hydrate) (drug)]] 5 µM in 1 line (AN3 CA 0.187×); [[Digitoxin (drug)]] 5 µM in 1 line (A-427 0.0857×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZNF536]] (+0.58, fdr 1e-05), [[ANKRD7]] (+0.58, fdr 1e-05), [[BASP1-AS1]] (+0.56, fdr 3e-05); moves opposite to [[VIPR1]] (-0.49, fdr 5e-04), [[MIS18A]] (-0.45, fdr 1e-04).
> It is in [[Module 102]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[TBX18]] → it (grade B ⚠); 2 go from it, the strongest it → [[LOXL1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 9 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12792.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.51×** | +11.8 | 2e-29 | 14/20 (NCI-H460, HOP62, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.26×** | +9.9 | 8e-21 | 0/3 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.06×** | +9.8 | 3e-20 | 0/2 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.64×** | +8.8 | 1e-16 | 2/8 (HOP62, NCI-H2347) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.69×** | +6.8 | 1e-09 | 13/27 (NCI-H2347, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.83×** | +5.3 | 1e-05 | 6/16 (NCI-H460, HOP62, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.42×** | +4.5 | 5e-04 | 3/25 (SHP-77, NCI-H460, …) | top dose only | low cells (technical?) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.60×** | +4.1 | 0.003 | 2/12 (SK-MEL-2, NCI-H460) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.85×** | +4.0 | 0.004 | 2/11 (A-427, HOP62) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.84×** | +4.0 | 0.004 | 0/5 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Simotinib (drug)]] 5 µM | ⚠ toxic | **1.56×** | +3.9 | 0.005 | 2/14 (C-33 A, LOX-IMVI) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.47×** | +3.4 | 0.034 | 8/19 (RPMI-7951, SK-MEL-2, …) | inconsistent across doses |  |
| [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | **2.02×** | +3.3 | 0.035 | 0/2 | top dose only | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.46×** | +3.3 | 0.035 | 0/10 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.64×** | +3.2 | 0.050 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.42×** | +3.2 | 0.055 | 9/22 (NCI-H2347, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.27×** | +3.0 | 0.091 | 4/26 (SK-MEL-2, NCI-H1792, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 4 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12792.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (PANC-1 0.211×, A549 0.0842×, NCI-H460 0.132×; ⚠ cell-cycle shift, would explain all of this change); [[Berberine (chloride hydrate) (drug)]] 5 µM in 1 line (AN3 CA 0.187×); [[Digitoxin (drug)]] 5 µM in 1 line (A-427 0.0857×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.573×** | -5.1 | 2e-04 | 15/28 (PANC-1, NCI-H1792, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.646×** | -3.8 | 0.037 | 15/25 (PANC-1, NCI-H23, …) | rises with dose | composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.893× | -3.7 | 0.048 | 8/29 (CFPAC-1, C32, …) | inconsistent across doses |  |
| [[Malotilate (drug)]] 5 µM |  | **0.680×** | -3.5 | 0.064 | 5/27 (A549, Panc 03.27, …) | top dose only |  |
| [[Methotrexate (drug)]] 0.5 µM |  | 0.709× | -3.1 | 0.20 | 2/26 (A-172, NCI-H1573) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.718× | -3.0 | 0.25 | 11/27 (LOX-IMVI, A549, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.44 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12792. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 1.87 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.74× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -10.2) ⚠ cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 5.40 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0857× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 3.04 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0842× (z -10.4) ⚠ cell-cycle shift, would explain all of this change |
| [[AN3 CA (line)]] | alt | 0.784 | 0 | 1 | — | [[Berberine (chloride hydrate) (drug)]] 5 µM 0.187× (z -9.8) |
| [[PANC-1 (line)]] | alt | 7.68 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[A-172 (line)]] | wt | 0.964 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.695 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.10 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.440 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.472 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.418 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.467 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.445 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.442 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 3.78 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.443 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.460 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.74 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.423 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.567 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.45 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.858 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.01 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.648 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.443 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.42 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.432 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.97 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.71 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.499 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.471 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12792), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF536]] | +0.58 | +0.49 / +0.65 | both halves | 1e-05 |  |
| [[ANKRD7]] | +0.58 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[BASP1-AS1]] | +0.56 | +0.57 / +0.44 | both halves | 3e-05 | same gene group |
| [[CCDC3]] | +0.56 | +0.49 / +0.57 | both halves | 1e-05 |  |
| [[BVES]] | +0.56 | +0.47 / +0.56 | both halves | 2e-05 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[HAGLR]] | +0.55 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[TMLHE-AS1]] | +0.55 | +0.58 / +0.42 | both halves | 4e-05 | same gene group |
| [[LINC01122]] | +0.55 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[C12orf56]] | +0.54 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[ADAM23]] | +0.54 | +0.43 / +0.54 | both halves | 3e-05 |  |
| [[LINC02384]] | +0.54 | +0.52 / +0.53 | both halves | 1e-05 |  |
| [[UBE2Q2P13]] | +0.54 | +0.37 / +0.62 | both halves | 9e-05 |  |
| [[LRRN2]] | +0.53 | +0.39 / +0.52 | both halves | 6e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[VIPR1]] | -0.49 | -0.46 / -0.24 | both halves | 5e-04 |  |
| [[MIS18A]] | -0.45 | -0.38 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 6, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TBX18]] | B | TBX18 activity raises BVES-AS1's level | lines that do not express TBX18 (27) vs lines expressing it (23) | 1.71× lower at baseline in the lines without TBX18 | 0.050 | ⚠ within organs, on part of the lines; also absent: SFRP1, LRRK2, ENSG00000286251 |
| [[LOXL1]] | B | LOXL1 activity raises BVES-AS1's level | lines that do not express LOXL1 (18) vs lines expressing it (32) | 1.47× lower at baseline in the lines without LOXL1 | 0.054 | ⚠ within organs, on part of the lines; also absent: B3GALNT1, LOXL1-AS1, ENSG00000255330 |
| [[LRRC36]] | B | LRRC36 activity raises BVES-AS1's level | lines that do not express LRRC36 (16) vs lines expressing it (34) | 1.38× lower at baseline in the lines without LRRC36 | 0.066 | ⚠ within organs, on part of the lines; also absent: DANT2, ANKRD20A21P, MTMR8; maybe low, not absent |
| [[LINC02384]] | B | LINC02384 activity raises BVES-AS1's level | lines that do not express LINC02384 (26) vs lines expressing it (24) | 1.69× lower at baseline in the lines without LINC02384 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000259929, ENSG00000277693, FAM230C; maybe low, not absent |
| [[ZNF626]] | B | ZNF626 activity raises BVES-AS1's level | lines that do not express ZNF626 (28) vs lines expressing it (22) | 1.67× lower at baseline in the lines without ZNF626 | 0.092 | ⚠ within organs, on part of the lines; also absent: ROS1, GDNF, HTRA3 |
| [[BOLA3-DT]] | B | BOLA3-DT activity raises BVES-AS1's level | lines that do not express BOLA3-DT (10) vs lines expressing it (40) | 1.66× lower at baseline in the lines without BOLA3-DT | 0.096 | ⚠ within organs, on part of the lines; also absent: GIHCG, KATNAL1, LIX1L |
| [[CCNYL2]], [[CCNYL2-1]] | C | CCNYL2, CCNYL2-1 activity raises BVES-AS1's level | lines that do not express CCNYL2, CCNYL2-1 (29) vs lines expressing them (21) | 1.86× lower at baseline in the lines without CCNYL2, CCNYL2-1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target; co-absent genes |
| [[GLIS1]] | C | GLIS1 activity raises BVES-AS1's level | lines that do not express GLIS1 (24) vs lines expressing it (26) | 2.02× lower at baseline in the lines without GLIS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: CPEB1, SPOCK1, DZIP1; maybe low, not absent; co-absent with the target |
| [[BVES]] | C | BVES activity raises BVES-AS1's level | lines that do not express BVES (19) vs lines expressing it (31) | 2.40× lower at baseline in the lines without BVES | 0.040 | ⚠ within organs, on part of the lines; also absent: MPDZ, BVES-AS1, DPY19L2; co-absent with the target |
| [[HHIPL2]] | C | HHIPL2 activity raises BVES-AS1's level | lines that do not express HHIPL2 (14) vs lines expressing it (36) | 1.98× lower at baseline in the lines without HHIPL2 | 0.042 | ⚠ within organs, on part of the lines; also absent: PRKD1, BNIP3, SPART; maybe low, not absent; co-absent with the target |
| [[TSHZ3-AS1]] | C | TSHZ3-AS1 activity raises BVES-AS1's level | lines that do not express TSHZ3-AS1 (25) vs lines expressing it (25) | 1.73× lower at baseline in the lines without TSHZ3-AS1 | 0.074 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ADAMTS18, TWIST2, INSYN2B; co-absent with the target |
| [[BEND6]] | C | BEND6 activity raises BVES-AS1's level | lines that do not express BEND6 (14) vs lines expressing it (36) | 2.11× lower at baseline in the lines without BEND6 | 0.079 | ⚠ within organs, on part of the lines; also absent: GNB4, MAP1B, MPDZ; co-absent with the target |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LOXL1]] | B | BVES-AS1 activity raises LOXL1's level | lines that do not express BVES-AS1 (17) vs lines expressing it (33) | 2.00× lower at baseline in the lines without BVES-AS1 | 0.093 | ⚠ within organs, on part of the lines; also absent: BVES, MPDZ, MAP9; maybe low, not absent |
| [[BVES]] | C | BVES-AS1 activity raises BVES's level | lines that do not express BVES-AS1 (17) vs lines expressing it (33) | 4.96× lower at baseline in the lines without BVES-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: BVES, MPDZ, MAP9; maybe low, not absent; co-absent with the target; its own permutation p |

## Where it sits

- **Module**: [[Module 102]] — Neuronal System; 45 genes; every member is in the + arm (projection on the module's main direction 0.534). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (10.1, 34.3); signed map (26.5, 23.0). **Vector** length 34.9, 5.07% of its response variance represented; |z| ≥ 3 in 644 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.2 | +9.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.1 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.1 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +8.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.8 | +6.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +2.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.1 | +0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | +3.4 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~55% of this change | -1.5 | -3.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.3 | -3.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.2 | -3.7 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.0 | -1.0 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -0.9 | -1.8 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -1.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.8 | -1.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.8 | -1.0 |
|  | [[Ranolazine (drug)]] 0.5 µM |  | -0.8 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | POPDC1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6q21 — chr6:105,136,308-105,199,559 (+) |
| Ensembl biotype | lncRNA |
| Also known as | bA99L11.2; previously BVES-AS1, C6orf112 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

UniProt [Q5T3Y7](https://www.uniprot.org/uniprotkb/Q5T3Y7) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:21223](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:21223) · Entrez [154442](https://www.ncbi.nlm.nih.gov/gene/154442) · UniProt [Q5T3Y7](https://www.uniprot.org/uniprotkb/Q5T3Y7) · Ensembl [ENSG00000203808](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000203808)

## Data

Gene col 12792: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12792); `tables/drug_effects.parquet` (23 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12792, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12792]; `tensor/DDL_lfc|DDL_z.npy` [12792]; `embed/gene_vectors.npy` [12792]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12792 or target_col == 12792). Every well: [[BVES-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BVES-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
