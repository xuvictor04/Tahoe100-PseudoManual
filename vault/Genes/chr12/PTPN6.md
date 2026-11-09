---
symbol: "PTPN6"
type: "gene"
col: 3262
ensembl_id: "ENSG00000111679"
name: "protein tyrosine phosphatase non-receptor type 6"
location: "12p13.31"
module: 38
arm: "+"
pooled_cpm: 21.18
n_lines_expressing: 42
n_dd_up: 12
n_dd_down: 2
n_dd_up_clean: 8
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 3
direction_downstream: 11
tags: ["gene", "module/038"]
generated_by: "tahoemap"
---

# PTPN6

*protein tyrosine phosphatase non-receptor type 6* — 12p13.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 7.71× (z +20.0, q 0e+00, up in 26 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.84× (z +14.5, q 7e-45, up in 37 of 40 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.614× (z -4.8, q 9e-04, down in 21 of 39 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (NCI-H23 0.215×, SW480 0.383×, NCI-H2030 0.347×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H2030 0.175×, NCI-H23 0.243×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.173×, NCI-H23 0.334×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (NCI-H23 0.320×, SW480 0.422×); [[Methotrexate (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0607×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LRRC23]] (+0.70, fdr 7e-06, ⚠ same locus), [[TRIM72]] (+0.66, fdr 7e-06), [[ITGA2B]] (+0.63, fdr 7e-06), [[LDHC]] (+0.62, fdr 1e-05).
> It is in [[Module 038]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ATAD3C]] → it (grade B ⚠); 11 go from it, the strongest it → [[C5AR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 5 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3262.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.71×** | +20.0 | 0e+00 | 26/34 (KATO III, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.84×** | +14.5 | 7e-45 | 37/40 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.51×** | +14.2 | 2e-43 | 22/26 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.27×** | +10.7 | 1e-24 | 19/29 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.43×** | +5.0 | 8e-05 | 24/40 (HOP62, PANC-1, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +4.8 | 2e-04 | 17/39 (HOP62, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.40×** | +4.7 | 3e-04 | 17/38 (LOX-IMVI, C32, …) | top dose only | cell-cycle shift (explains ~18% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.63×** | +4.6 | 3e-04 | 21/33 (SW1417, LoVo, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.56×** | +4.2 | 0.002 | 17/37 (MIA PaCa-2, SW48, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.78×** | +4.0 | 0.004 | 20/37 (A-427, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +3.8 | 0.008 | 21/38 (MIA PaCa-2, HOP62, …) | top dose only | cell-cycle shift (explains ~19% here) |
| [[Lactate (calcium) (drug)]] 5 µM |  | **1.38×** | +3.1 | 0.088 | 7/39 (Panc 03.27, HEC-1-A, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | 1.25× | +3.0 | 0.10 | 15/40 (KATO III, Panc 03.27, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3262.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 5 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Ouabain (Octahydrate) (drug)]] 5 µM in 3 lines (NCI-H23 0.215×, SW480 0.383×, NCI-H2030 0.347×; ⚠ cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 5 µM in 2 lines (NCI-H2030 0.175×, NCI-H23 0.243×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Digitoxin (drug)]] 0.5 µM in 2 lines (NCI-H1573 0.173×, NCI-H23 0.334×); [[Ouabain (Octahydrate) (drug)]] 0.5 µM in 2 lines (NCI-H23 0.320×, SW480 0.422×); [[Methotrexate (drug)]] 0.05 µM in 1 line (HepG2/C3A 0.0607×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.614×** | -4.8 | 9e-04 | 21/39 (NCI-H1573, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.675×** | -3.7 | 0.054 | 23/35 (Panc 03.27, NCI-H2030, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.706× | -3.4 | 0.11 | 19/39 (SW480, NCI-H661, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, +0.06 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3262. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 45.4 | 2 (1 ⚠) | 4 (2 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 12.4× (z +19.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.88× (z +11.7) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.215× (z -12.1) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.320× (z -8.9) |
| [[HOP62 (line)]] | alt | 6.14 | 5 (2 ⚠) | 0 | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 10.2× (z +11.7) | — |
| [[SW480 (line)]] | alt | 42.5 | 3 (3 ⚠) | 2 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 8.15× (z +20.8) ⚠ toxic; transcription drop | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.383× (z -9.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.422× (z -8.5) |
| [[LoVo (line)]] | wt | 26.1 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 20.9× (z +19.3) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 2.66× (z +8.8) | — |
| [[LOX-IMVI (line)]] | wt | 16.9 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 22.2× (z +11.6) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 8.29× (z +11.2) | — |
| [[PANC-1 (line)]] | alt | 10.3 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.49× (z +13.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.88× (z +12.3) | — |
| [[A498 (line)]] | wt | 19.8 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.98× (z +10.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +10.0) | — |
| [[KATO III (line)]] | alt | 35.8 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 13.1× (z +21.0) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 44.4 | 1 | 2 (2 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.175× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 16.3 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.95× (z +10.4) | — |
| [[C32 (line)]] | wt | 13.0 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 23.0× (z +10.8) | — |
| [[HT-29 (line)]] | alt | 20.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.21× (z +12.4) ⚠ toxic; transcription drop | — |
| [[hTERT-HPNE (line)]] | wt | 7.06 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.7× (z +10.1) | — |
| [[NCI-H1573 (line)]] | alt | 36.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.36× (z +8.9) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 0.5 µM 0.173× (z -11.0) |
| [[A-427 (line)]] | wt | 74.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.54× (z +11.0) ⚠ toxic; transcription drop | — |
| [[AsPC-1 (line)]] | alt | 10.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.32× (z +8.7) | — |
| [[HepG2_C3A (line)]] | wt | 16.0 | 0 | 1 | — | [[Methotrexate (drug)]] 0.05 µM 0.0607× (z -10.6) |
| [[LS 180 (line)]] | wt | 26.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.78× (z +13.3) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 5.66 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.62× (z +9.3) | — |
| [[SK-MEL-2 (line)]] | alt | 7.42 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.13× (z +8.5) | — |
| [[SW48 (line)]] | wt | 17.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 12.8× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 3.67 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.68 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 33.8 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.05 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.92 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.13 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.77 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.35 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 9.32 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.96 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 23.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.19 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.61 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 8.35 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.78 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.74 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.92 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 38.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3262), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC23]] | +0.70 | +0.69 / +0.68 | both halves | 7e-06 | ⚠ same locus (32.2 kb, same strand: neighbours can correlate without regulation) |
| [[TRIM72]] | +0.66 | +0.67 / +0.58 | both halves | 7e-06 |  |
| [[ITGA2B]] | +0.63 | +0.59 / +0.66 | both halves | 7e-06 | pathway: Platelet activation, signaling and aggregation |
| [[LDHC]] | +0.62 | +0.65 / +0.50 | both halves | 1e-05 |  |
| [[CPT1C]] | +0.62 | +0.62 / +0.62 | both halves | 7e-06 |  |
| [[DHDH]] | +0.62 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[ARL9]] | +0.61 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[FNDC7]] | +0.61 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[PYGM]] | +0.61 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[AVIL]] | +0.60 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[PHKG1]] | +0.60 | +0.54 / +0.62 | both halves | 1e-05 |  |
| [[SPACDR]] | +0.60 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[PILRA]] | +0.59 | +0.58 / +0.52 | both halves | 1e-05 | STRING 796 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATAD3C]] | B | ATAD3C activity raises PTPN6's level | lines that do not express ATAD3C (17) vs lines expressing it (33) | 3.01× lower at baseline in the lines without ATAD3C | 0.002 | ⚠ within organs, on part of the lines; also absent: SLC52A3, MYH14, SORL1 |
| [[TOP2A]] | B | TOP2A activity lowers PTPN6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.8% of all compounds | 0.010 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HPN]] | B | HPN activity raises PTPN6's level | lines that do not express HPN (6) vs lines expressing it (44) | 1.84× lower at baseline in the lines without HPN | 0.058 | ⚠ within organs, on part of the lines; also absent: NAT14, APBA1; maybe low, not absent |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 11, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C5AR1]] | B | PTPN6 activity raises C5AR1's level | lines that do not express PTPN6 (8) vs lines expressing it (42) | 1.93× lower at baseline in the lines without PTPN6 | 0.034 | ⚠ within organs, on part of the lines; also absent: LMTK3, ENSG00000257252; maybe low, not absent |
| [[SMIM41]] | B | PTPN6 activity raises SMIM41's level | lines that do not express PTPN6 (8) vs lines expressing it (42) | 1.81× lower at baseline in the lines without PTPN6 | 0.040 | ⚠ within organs, on part of the lines; also absent: LMTK3, ENSG00000257252; maybe low, not absent |
| [[CDKL2]] | B | PTPN6 activity raises CDKL2's level | lines that do not express PTPN6 (8) vs lines expressing it (42) | 1.66× lower at baseline in the lines without PTPN6 | 0.047 | ⚠ within organs, on part of the lines; also absent: LMTK3, ENSG00000257252; maybe low, not absent |
| [[CAPN12]] | B | PTPN6 activity raises CAPN12's level | lines that do not express PTPN6 (8) vs lines expressing it (42) | 1.60× lower at baseline in the lines without PTPN6 | 0.047 | ⚠ within organs, on part of the lines; also absent: LMTK3, ENSG00000257252; maybe low, not absent |
| [[PPP1R36]] | B | PTPN6 activity raises PPP1R36's level | lines that do not express PTPN6 (8) vs lines expressing it (42) | 1.54× lower at baseline in the lines without PTPN6 | 0.048 | ⚠ within organs, on part of the lines; also absent: LMTK3, ENSG00000257252; maybe low, not absent |
| [[PYGM]] | B | PTPN6 activity raises PYGM's level | lines that do not express PTPN6 (8) vs lines expressing it (42) | 1.78× lower at baseline in the lines without PTPN6 | 0.053 | ⚠ within organs, on part of the lines; also absent: LMTK3, ENSG00000257252; maybe low, not absent |
| [[ATAD3C]] | B | PTPN6 activity raises ATAD3C's level | lines that do not express PTPN6 (8) vs lines expressing it (42) | 1.87× lower at baseline in the lines without PTPN6 | 0.054 | ⚠ within organs, on part of the lines; also absent: LMTK3, ENSG00000257252; maybe low, not absent |
| [[GRAMD2A]] | B | PTPN6 activity raises GRAMD2A's level | lines that do not express PTPN6 (8) vs lines expressing it (42) | 1.54× lower at baseline in the lines without PTPN6 | 0.061 | ⚠ within organs, on part of the lines; also absent: LMTK3, ENSG00000257252; maybe low, not absent |
| [[NEK8]] | B | PTPN6 activity raises NEK8's level | lines that do not express PTPN6 (8) vs lines expressing it (42) | 1.50× lower at baseline in the lines without PTPN6 | 0.067 | ⚠ within organs, on part of the lines; also absent: LMTK3, ENSG00000257252; maybe low, not absent |
| [[DHDH]] | B | PTPN6 activity raises DHDH's level | lines that do not express PTPN6 (8) vs lines expressing it (42) | 1.85× lower at baseline in the lines without PTPN6 | 0.071 | ⚠ within organs, on part of the lines; also absent: LMTK3, ENSG00000257252; maybe low, not absent |
| [[HPN]] | B | PTPN6 activity raises HPN's level | lines that do not express PTPN6 (8) vs lines expressing it (42) | 1.43× lower at baseline in the lines without PTPN6 | 0.072 | ⚠ within organs, on part of the lines; also absent: LMTK3, ENSG00000257252; maybe low, not absent |

## Where it sits

- **Module**: [[Module 038]]; 122 genes; every member is in the + arm (projection on the module's main direction 0.631). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.28; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.7, -17.1); signed map (15.5, 11.4). **Vector** length 86.1, 21.4% of its response variance represented; |z| ≥ 3 in 732 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.5 | +14.5 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.7 | +14.2 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.7 | +4.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +20.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +3.2 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.0 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.8 | +1.9 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.5 | +3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.4 | +2.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -3.7 | -4.8 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +0.7 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -2.6 | -3.4 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -2.5 | -3.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.4 | +0.2 |
|  | [[Erlotinib (drug)]] 5 µM |  | -2.1 | -2.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.0 | -1.0 |
|  | [[Pralsetinib (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.8 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | protein tyrosine phosphatase non-receptor type 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12p13.31 — chr12:6,946,468-6,961,316 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HCP, HCPH, PTP-1C, SHP-1, SHP1 |
| Gene groups (HGNC) | SH2 domain containing; Protein tyrosine phosphatases non-receptor type |
| Hallmark sets | ALLOGRAFT_REJECTION, INTERFERON_GAMMA_RESPONSE, ESTROGEN_RESPONSE_LATE |
| Reactome | 44 pathways, smallest: CD22 mediated BCR regulation; Co-inhibition by BTLA; Regulation of IFNA/IFNB signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P29350](https://www.uniprot.org/uniprotkb/P29350) (Tyrosine-protein phosphatase non-receptor type 6):

> Tyrosine phosphatase enzyme that plays important roles in controlling immune signaling pathways and fundamental physiological processes such as hematopoiesis. Dephosphorylates and negatively regulate several receptor tyrosine kinases (RTKs) such as EGFR, PDGFR and FGFR, thereby modulating their signaling activities. When recruited to immunoreceptor tyrosine-based inhibitory motif (ITIM)-containing receptors such as immunoglobulin-like transcript 2/LILRB1, programmed cell death protein 1/PDCD1, …

**Summary**, from NCBI Gene [5777](https://www.ncbi.nlm.nih.gov/gene/5777):

> The protein encoded by this gene is a member of the protein tyrosine phosphatase (PTP) family. PTPs are known to be signaling molecules that regulate a variety of cellular processes including cell growth, differentiation, mitotic cycle, and oncogenic transformation. N-terminal part of this PTP contains two tandem Src homolog (SH2) domains, which act as protein phospho-tyrosine binding domains, and mediate the interaction of this PTP with its substrates. This PTP is expressed primarily in …

**Accessions** — [HGNC:9658](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9658) · Entrez [5777](https://www.ncbi.nlm.nih.gov/gene/5777) · UniProt [P29350](https://www.uniprot.org/uniprotkb/P29350) · Ensembl [ENSG00000111679](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111679)

## Data

Gene col 3262: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3262); `tables/drug_effects.parquet` (16 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3262, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3262]; `tensor/DDL_lfc|DDL_z.npy` [3262]; `embed/gene_vectors.npy` [3262]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3262 or target_col == 3262). Every well: [[PTPN6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PTPN6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
