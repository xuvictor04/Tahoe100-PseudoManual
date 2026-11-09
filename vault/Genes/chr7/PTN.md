---
symbol: "PTN"
type: "gene"
col: 2686
ensembl_id: "ENSG00000105894"
name: "pleiotrophin"
location: "7q33"
module: 66
arm: "+"
pooled_cpm: 8.98
n_lines_expressing: 22
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 21
direction_downstream: 14
tags: ["gene", "module/066"]
generated_by: "tahoemap"
---

# PTN

*pleiotrophin* — 7q33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.55× (z +14.1, q 2e-42, up in 7 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.84× (z +12.6, q 4e-34, up in 10 of 18 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (H4 0.0646×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.0714×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (A498 0.102×; ⚠ toxic); [[Verteporfin (drug)]] 5 µM in 1 line (AN3 CA 0.139×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[THY1]] (+0.65, fdr 4e-05), [[SPARC]] (+0.56, fdr 9e-05), [[LUM]] (+0.55, fdr 3e-05); moves opposite to [[EIF2B4]] (-0.42, fdr 1e-04), [[AP1M2]] (-0.42, fdr 1e-04), [[TMEM120A]] (-0.39, fdr 2e-04).
> It is in [[Module 066]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 14 go from it, the strongest it → [[CD274]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2686.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.55×** | +14.1 | 2e-42 | 7/10 (HS-578T, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.84×** | +12.6 | 4e-34 | 10/18 (HS-578T, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.32×** | +12.5 | 9e-34 | 10/13 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.18×** | +9.4 | 8e-19 | 13/20 (SK-MEL-2, SHP-77, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.27×** | +9.4 | 8e-19 | 10/12 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.87×** | +7.5 | 4e-12 | 7/20 (C32, LOX-IMVI, …) | top dose only | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.90×** | +5.5 | 3e-06 | 10/19 (SK-MEL-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.85×** | +5.0 | 3e-05 | 6/15 (CFPAC-1, HS-578T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +4.6 | 3e-04 | 9/20 (RKO, HS-578T, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.66×** | +4.4 | 7e-04 | 5/8 (HS-578T, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | **1.60×** | +4.0 | 0.004 | 1/15 (SNU-423) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change | **1.58×** | +3.9 | 0.004 | 4/20 (HS-578T, hTERT-HPNE, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.38×** | +3.9 | 0.004 | 6/20 (hTERT-HPNE, A498, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +3.6 | 0.014 | 6/19 (SNU-423, HS-578T, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Bendamustine (drug)]] 5 µM |  | **1.49×** | +3.3 | 0.041 | 1/19 (A-172) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.43×** | +3.1 | 0.076 | 5/20 (SK-MEL-2, SHP-77, …) | inconsistent across doses | cell-cycle shift (explains ~22% here); position effect removed |
| [[Pimozide (drug)]] 0.05 µM |  | **1.43×** | +3.0 | 0.080 | 3/17 (AN3 CA, RKO, …) | inconsistent across doses | low cells (technical?); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2686.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 7 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Bortezomib (drug)]] 0.05 µM in 1 line (H4 0.0646×; ⚠ cell-cycle shift, would explain all of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (A498 0.0714×; ⚠ toxic; transcription drop); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (A498 0.102×; ⚠ toxic); [[Verteporfin (drug)]] 5 µM in 1 line (AN3 CA 0.139×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fluvoxamine (drug)]] 0.5 µM |  | 0.664× | -3.5 | 0.11 | 3/20 (hTERT-HPNE, NCI-H460, …) | inconsistent across doses |  |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.643× | -3.5 | 0.11 | 2/20 (hTERT-HPNE, A-172) | inconsistent across doses |  |
| [[Budesonide (drug)]] 5 µM |  | 0.671× | -3.4 | 0.11 | 8/20 (SNU-423, HS-578T, …) | top dose only |  |
| [[Erythromycin (drug)]] 0.05 µM |  | 0.691× | -3.2 | 0.20 | 3/20 (SW 1088, RPMI-7951, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.47 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2686. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 11.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0714× (z -10.8) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 73.6 | 0 | 2 (1 ⚠) | — | [[Verteporfin (drug)]] 5 µM 0.139× (z -9.3) |
| [[RKO (line)]] | wt | 14.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0957× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~60% of this change |
| [[C32 (line)]] | wt | 2.74 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.2× (z +9.7) ⚠ cell-cycle shift, explains ~56% of this change | — |
| [[H4 (line)]] | wt | 70.4 | 0 | 1 (1 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.0646× (z -13.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HS-578T (line)]] | alt | 130 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.80× (z +10.3) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 13.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.112× (z -8.7) ⚠ toxic; cell-cycle shift, explains ~55% of this change |
| [[A-172 (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.699 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.855 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.952 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.901 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.69 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.980 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.944 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 89.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.891 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.869 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.830 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.761 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.891 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.900 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.60 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.897 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.00 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 334 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.908 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.862 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2686), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THY1]] | +0.65 | +0.41 / +0.73 | both halves | 4e-05 | **novel candidate** |
| [[SPARC]] | +0.56 | +0.36 / +0.60 | both halves | 9e-05 | STRING 817 |
| [[LUM]] | +0.55 | +0.46 / +0.61 | both halves | 3e-05 |  |
| [[CDH2]] | +0.54 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[AGA]] | +0.52 | +0.50 / +0.45 | both halves | 3e-05 |  |
| [[CXCL10]] | +0.51 | +0.49 / +0.46 | both halves | 3e-05 |  |
| [[QPCT]] | +0.49 | +0.34 / +0.52 | both halves | 1e-04 |  |
| [[MOXD1]] | +0.49 | +0.37 / +0.52 | both halves | 9e-05 |  |
| [[GLIPR1]] | +0.49 | +0.44 / +0.49 | both halves | 3e-05 |  |
| [[COL1A1]] | +0.48 | +0.36 / +0.47 | both halves | 9e-05 | STRING 527 |
| [[PPP2R2B]] | +0.47 | +0.33 / +0.45 | both halves | 1e-04 |  |
| [[TMSB4X]] | +0.47 | +0.36 / +0.41 | both halves | 9e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EIF2B4]] | -0.42 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[AP1M2]] | -0.42 | -0.33 / -0.43 | both halves | 1e-04 |  |
| [[TMEM120A]] | -0.39 | -0.34 / -0.32 | both halves | 2e-04 |  |
| [[LRRC47]] | -0.39 | -0.22 / -0.41 | both halves | 6e-04 |  |
| [[SETD6]] | -0.38 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[TSR3]] | -0.37 | -0.40 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 2, C 19. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers PTN's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[CD274]] | B | CD274 activity raises PTN's level | lines that do not express CD274 (18) vs lines expressing it (32) | 3.06× lower at baseline in the lines without CD274 | 0.053 | ⚠ within organs, on part of the lines; also absent: GBP5, IL1B, PDCD1LG2 |
| [[GAP43]] | C | GAP43 activity raises PTN's level | lines that do not express GAP43 (22) vs lines expressing it (28) | 3.70× lower at baseline in the lines without GAP43 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000287622, ENSG00000242880, ENSG00000286540; maybe low, not absent; co-absent with the target |
| [[COL3A1]] | C | COL3A1 activity raises PTN's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 5.39× lower at baseline in the lines without COL3A1 | 0.012 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677; co-absent with the target |
| [[DCT]] | C | DCT activity raises PTN's level | lines that do not express DCT (42) vs lines expressing it (8) | 6.92× lower at baseline in the lines without DCT | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: LHFPL3-AS1, TYR, GTF2I-AS1; co-absent with the target |
| [[SPARC]] | C | SPARC activity raises PTN's level | lines that do not express SPARC (34) vs lines expressing it (16) | 6.87× lower at baseline in the lines without SPARC | 0.015 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ITGA4, MMP2, ENSG00000222032; co-absent with the target |
| [[THY1]] | C | THY1 activity raises PTN's level | lines that do not express THY1 (38) vs lines expressing it (12) | 6.49× lower at baseline in the lines without THY1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: TMPRSS15, DCN, COL11A1; co-absent with the target |
| [[ALPK2]] | C | ALPK2 activity raises PTN's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 5.77× lower at baseline in the lines without ALPK2 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4; co-absent with the target |
| [[CFH]] | C | CFH activity raises PTN's level | lines that do not express CFH (28) vs lines expressing it (22) | 2.62× lower at baseline in the lines without CFH | 0.054 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1; co-absent with the target |
| [[COL1A1]] | C | COL1A1 activity raises PTN's level | lines that do not express COL1A1 (34) vs lines expressing it (16) | 3.01× lower at baseline in the lines without COL1A1 | 0.060 | ⚠ within organs, on part of the lines; also absent: DCN, LAYN, LINC01411; co-absent with the target |
| [[LUM]] | C | LUM activity raises PTN's level | lines that do not express LUM (34) vs lines expressing it (16) | 3.45× lower at baseline in the lines without LUM | 0.061 | ⚠ within organs, on part of the lines; also absent: ITGA11, DCN, IRAG2; co-absent with the target |
| [[KCNT2]] | C | KCNT2 activity raises PTN's level | lines that do not express KCNT2 (25) vs lines expressing it (25) | 2.90× lower at baseline in the lines without KCNT2 | 0.064 | ⚠ within organs, on part of the lines; also absent: TCF4, FGF14, MSC-AS1; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 4, C 10. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD274]] | B | PTN activity raises CD274's level | lines that do not express PTN (28) vs lines expressing it (22) | 2.32× lower at baseline in the lines without PTN | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, SPARC, BAALC |
| [[LINC01358]] | B | PTN activity raises LINC01358's level | lines that do not express PTN (28) vs lines expressing it (22) | 2.17× lower at baseline in the lines without PTN | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, SPARC, BAALC |
| [[FKBP7]] | B | PTN activity raises FKBP7's level | lines that do not express PTN (28) vs lines expressing it (22) | 2.02× lower at baseline in the lines without PTN | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, SPARC, BAALC |
| [[PDE1C]] | B | PTN activity raises PDE1C's level | lines that do not express PTN (28) vs lines expressing it (22) | 2.14× lower at baseline in the lines without PTN | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, SPARC, BAALC |
| [[ECM1]] | C | PTN activity raises ECM1's level | lines that do not express PTN (28) vs lines expressing it (22) | 3.07× lower at baseline in the lines without PTN | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, SPARC, BAALC; co-absent with the target |
| [[VCAM1]] | C | PTN activity raises VCAM1's level | lines that do not express PTN (28) vs lines expressing it (22) | 3.90× lower at baseline in the lines without PTN | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, SPARC, BAALC; co-absent with the target |
| [[FSTL1]] | C | PTN activity raises FSTL1's level | lines that do not express PTN (28) vs lines expressing it (22) | 5.22× lower at baseline in the lines without PTN | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, SPARC, BAALC; co-absent with the target |
| [[C5orf46]] | C | PTN activity raises C5orf46's level | lines that do not express PTN (28) vs lines expressing it (22) | 2.09× lower at baseline in the lines without PTN | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, SPARC, BAALC; co-absent with the target |
| [[TNFRSF11B]] | C | PTN activity raises TNFRSF11B's level | lines that do not express PTN (28) vs lines expressing it (22) | 1.95× lower at baseline in the lines without PTN | 0.024 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, SPARC, BAALC; co-absent with the target |
| [[SPARC]] | C | PTN activity raises SPARC's level | lines that do not express PTN (28) vs lines expressing it (22) | 10.25× lower at baseline in the lines without PTN | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, SPARC, BAALC; co-absent with the target |
| [[MOXD1]] | C | PTN activity raises MOXD1's level | lines that do not express PTN (28) vs lines expressing it (22) | 3.62× lower at baseline in the lines without PTN | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, SPARC, BAALC; co-absent with the target |
| [[FAM133A]] | C | PTN activity raises FAM133A's level | lines that do not express PTN (28) vs lines expressing it (22) | 2.31× lower at baseline in the lines without PTN | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: KCNE4, SPARC, BAALC; co-absent with the target |

## Where it sits

- **Module**: [[Module 066]] — epithelial mesenchymal transition; 74 genes; every member is in the + arm (projection on the module's main direction 0.544). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (56.8, 23.8); signed map (44.7, 21.6). **Vector** length 43.0, 9.60% of its response variance represented; |z| ≥ 3 in 409 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +9.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +5.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.5 | +12.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +1.9 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.8 | +14.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.5 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.2 | +3.9 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.0 | +0.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.0 | +1.3 |
| fall | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, would explain all of this change | -1.7 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.5 | -1.3 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.1 | -1.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.0 | -0.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.0 | -1.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -0.9 | -0.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.9 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | pleiotrophin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7q33 — chr7:137,227,341-137,343,774 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HBNF, HBGF8; previously NEGF1 |
| Gene groups (HGNC) | Receptor ligands |
| Reactome | 3 pathways, smallest: MDK and PTN in ALK signaling; Signaling by ALK; Signaling by Receptor Tyrosine Kinases |
| Matched by | ensembl_id |

**Function**, from UniProt [P21246](https://www.uniprot.org/uniprotkb/P21246) (Pleiotrophin):

> Secreted growth factor that mediates its signal through cell-surface proteoglycan and non-proteoglycan receptors. Binds cell-surface proteoglycan receptor via their chondroitin sulfate (CS) groups. Thereby regulates many processes like cell proliferation, cell survival, cell growth, cell differentiation and cell migration in several tissues namely neuron and bone. Also plays a role in synaptic plasticity and learning-related behavior by inhibiting long-term synaptic potentiation (By …

**Summary**, from NCBI Gene [5764](https://www.ncbi.nlm.nih.gov/gene/5764):

> The protein encoded by this gene is a secreted heparin-binding growth factor. The protein has significant roles in cell growth and survival, cell migration, angiogenesis and tumorigenesis. Alternative splicing and the use of alternative promoters results in multiple transcript variants. [provided by RefSeq, Oct 2016]

**Accessions** — [HGNC:9630](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9630) · Entrez [5764](https://www.ncbi.nlm.nih.gov/gene/5764) · UniProt [P21246](https://www.uniprot.org/uniprotkb/P21246) · Ensembl [ENSG00000105894](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105894)

## Data

Gene col 2686: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2686); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2686, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2686]; `tensor/DDL_lfc|DDL_z.npy` [2686]; `embed/gene_vectors.npy` [2686]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2686 or target_col == 2686). Every well: [[PTN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
