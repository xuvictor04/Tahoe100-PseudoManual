---
symbol: "IFI6"
type: "gene"
col: 4753
ensembl_id: "ENSG00000126709"
name: "interferon alpha inducible protein 6"
location: "1p35.3"
module: 32
arm: "+"
pooled_cpm: 173.93
n_lines_expressing: 37
n_dd_up: 0
n_dd_down: 48
n_dd_up_clean: 0
n_dd_down_clean: 39
in_vector_space: true
direction_upstream: 38
direction_downstream: 111
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# IFI6

*interferon alpha inducible protein 6* — 1p35.3

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (J82 5.96×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (J82 5.36×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 48 drug-doses (9 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.174× (z -15.1, q 0e+00, down in 33 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFI27]] (+0.93, fdr 7e-06), [[IFITM3]] (+0.91, fdr 7e-06), [[ISG15]] (+0.89, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 38 arrows point to it, the strongest [[SAMD9L]] → it (grade B ⚠); 111 go from it, the strongest it → [[IRF9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4753.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (J82 5.96×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 1 line (J82 5.36×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | 1.77× | +3.4 | 0.37 | 28/34 (PANC-1, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.69× | +3.1 | 0.42 | 25/35 (RKO, NCI-H23, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 9 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 48 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4753.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.174×** | -15.1 | 0e+00 | 33/36 (BT-474, MIA PaCa-2, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.206×** | -13.7 | 3e-40 | 35/35 (A549, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.243×** | -12.3 | 3e-32 | 31/36 (MIA PaCa-2, LoVo, …) | all doses, stronger at high dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.162×** | -10.7 | 8e-25 | 29/34 (SNU-423, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.174×** | -10.7 | 8e-25 | 30/36 (BT-474, C-33 A, …) | top dose only |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.210×** | -9.6 | 1e-19 | 32/35 (BT-474, C-33 A, …) | all doses, stronger at high dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.255×** | -8.4 | 5e-15 | 32/35 (SNU-423, LoVo, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.269×** | -8.0 | 6e-14 | 33/36 (BT-474, C-33 A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.311×** | -7.1 | 6e-11 | 28/35 (C-33 A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.329×** | -6.8 | 6e-10 | 27/35 (RKO, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.310×** | -6.8 | 7e-10 | 34/35 (LoVo, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.358×** | -6.3 | 2e-08 | 25/35 (A549, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.384×** | -5.9 | 2e-07 | 33/35 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.128×** | -5.9 | 2e-07 | 28/36 (MIA PaCa-2, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib (drug)]] 5 µM |  | **0.134×** | -5.7 | 4e-07 | 29/35 (LoVo, C-33 A, …) | top dose only | noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **0.144×** | -5.5 | 1e-06 | 27/35 (RKO, A549, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4753. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 208 | 0 | 20 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0537× (z -20.2) |
| [[BT-474 (line)]] | alt | 328 | 0 | 18 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0413× (z -21.5) |
| [[A549 (line)]] | wt | 221 | 0 | 17 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0400× (z -23.5) |
| [[SNU-423 (line)]] | alt | 270 | 0 | 15 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.00596× (z -28.2) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0769× (z -20.7) |
| [[LoVo (line)]] | wt | 275 | 0 | 14 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.104× (z -16.3) |
| [[NCI-H23 (line)]] | alt | 299 | 0 | 14 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.0867× (z -15.9) |
| [[C-33 A (line)]] | alt | 436 | 0 | 12 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.0952× (z -17.1) |
| [[SHP-77 (line)]] | alt | 239 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -17.0) |
| [[A-172 (line)]] | wt | 249 | 0 | 9 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.149× (z -15.1) |
| [[MIA PaCa-2 (line)]] | alt | 284 | 0 | 9 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.109× (z -17.3) |
| [[HS-578T (line)]] | alt | 343 | 0 | 8 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.111× (z -17.2) |
| [[KATO III (line)]] | alt | 291 | 0 | 8 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.111× (z -16.9) |
| [[SNU-1 (line)]] | wt | 108 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -12.9) |
| [[NCI-H1573 (line)]] | alt | 225 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0941× (z -16.5) |
| [[NCI-H1792 (line)]] | alt | 227 | 0 | 7 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.0998× (z -16.7) |
| [[A498 (line)]] | wt | 128 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -12.6) |
| [[AsPC-1 (line)]] | alt | 185 | 0 | 6 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.133× (z -15.2) |
| [[HepG2_C3A (line)]] | wt | 191 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0831× (z -16.8) |
| [[CHP-212 (line)]] | wt | 98.5 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -11.4) |
| [[COLO 205 (line)]] | alt | 554 | 0 | 4 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.159× (z -14.3) |
| [[C32 (line)]] | wt | 241 | 0 | 3 | — | [[Tofacitinib (drug)]] 5 µM 0.164× (z -13.8) |
| [[CFPAC-1 (line)]] | alt | 305 | 0 | 3 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.161× (z -14.7) |
| [[RPMI-7951 (line)]] | alt | 485 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -13.2) |
| [[SK-MEL-2 (line)]] | alt | 294 | 0 | 3 | — | [[Tofacitinib (drug)]] 5 µM 0.236× (z -11.6) |
| [[J82 (line)]] | alt | 331 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.96× (z +10.1) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 138 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.196× (z -12.5) |
| [[SW1417 (line)]] | alt | 158 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.309× (z -9.7) |
| [[NCI-H2347 (line)]] | alt | 377 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.211× (z -12.0) |
| [[PANC-1 (line)]] | alt | 60.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -13.5) |
| [[SW 900 (line)]] | alt | 213 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.265× (z -10.5) |
| [[A-427 (line)]] | wt | 24.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 33.5 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 41.4 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 17.1 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 22.3 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 220 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 22.4 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 81.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 85.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 43.2 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 40.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 29.0 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 140 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 28.0 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 21.7 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 14.7 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4753), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFI27]] | +0.93 | +0.87 / +0.96 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 882 |
| [[IFITM3]] | +0.91 | +0.85 / +0.93 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 862 |
| [[ISG15]] | +0.89 | +0.83 / +0.90 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 959 |
| [[OAS1]] | +0.88 | +0.82 / +0.90 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 959 |
| [[IFITM1]] | +0.88 | +0.77 / +0.93 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 891 |
| [[USP18]] | +0.88 | +0.85 / +0.90 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 894 |
| [[UBE2L6]] | +0.88 | +0.79 / +0.90 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 697 |
| [[CMPK2]] | +0.87 | +0.83 / +0.89 | both halves | 7e-06 | STRING 733 |
| [[PARP9]] | +0.87 | +0.84 / +0.88 | both halves | 7e-06 | STRING 679 |
| [[BST2]] | +0.86 | +0.77 / +0.89 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 744 |
| [[SP110]] | +0.85 | +0.78 / +0.88 | both halves | 7e-06 | STRING 441 |
| [[IFIT1]] | +0.85 | +0.84 / +0.84 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 932 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*38 arrows, 38 of them with an alert ⚠; grade A 0, B 25, C 13. Shown: the 12 strongest; 26 more arrows (26 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMD9L]] | B | SAMD9L activity raises IFI6's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 2.89× lower at baseline in the lines without SAMD9L | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[IFI27]] | B | IFI27 activity raises IFI6's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 2.99× lower at baseline in the lines without IFI27 | 0.002 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[BATF2]] | B | BATF2 activity raises IFI6's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 2.65× lower at baseline in the lines without BATF2 | 0.003 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[CMPK2]] | B | CMPK2 activity raises IFI6's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 3.69× lower at baseline in the lines without CMPK2 | 0.007 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[CCDC194]] | B | CCDC194 activity raises IFI6's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 2.60× lower at baseline in the lines without CCDC194 | 0.010 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |
| [[IFI44]] | B | IFI44 activity raises IFI6's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.51× lower at baseline in the lines without IFI44 | 0.012 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[BST2]] | B | BST2 activity raises IFI6's level | lines that do not express BST2 (18) vs lines expressing it (32) | 2.82× lower at baseline in the lines without BST2 | 0.015 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[IFI44L]] | B | IFI44L activity raises IFI6's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 2.83× lower at baseline in the lines without IFI44L | 0.016 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[SAMD9]] | B | SAMD9 activity raises IFI6's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 3.06× lower at baseline in the lines without SAMD9 | 0.024 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[EPSTI1]] | B | EPSTI1 activity raises IFI6's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 2.77× lower at baseline in the lines without EPSTI1 | 0.024 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[PARP9]] | B | PARP9 activity raises IFI6's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 4.39× lower at baseline in the lines without PARP9 | 0.024 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[OAS3]] | B | OAS3 activity raises IFI6's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 4.46× lower at baseline in the lines without OAS3 | 0.027 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |

### Downstream of this gene

*111 arrows, 111 of them with an alert ⚠; grade A 0, B 100, C 11. Shown: the 12 strongest; 99 more arrows (99 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRF9]] | B | IFI6 activity raises IRF9's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.84× lower at baseline in the lines without IFI6 | 2e-04 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[REC8]] | B | IFI6 activity raises REC8's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.43× lower at baseline in the lines without IFI6 | 3e-04 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[PARP14]] | B | IFI6 activity raises PARP14's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.76× lower at baseline in the lines without IFI6 | 5e-04 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[HELZ2]] | B | IFI6 activity raises HELZ2's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.77× lower at baseline in the lines without IFI6 | 6e-04 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[PARP9]] | B | IFI6 activity raises PARP9's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 3.63× lower at baseline in the lines without IFI6 | 6e-04 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[OAS3]] | B | IFI6 activity raises OAS3's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 3.75× lower at baseline in the lines without IFI6 | 8e-04 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[USP18]] | B | IFI6 activity raises USP18's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.93× lower at baseline in the lines without IFI6 | 0.001 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[STAT1]] | B | IFI6 activity raises STAT1's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.74× lower at baseline in the lines without IFI6 | 0.001 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[SP110]] | B | IFI6 activity raises SP110's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 3.18× lower at baseline in the lines without IFI6 | 0.001 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[EIF2AK2]] | B | IFI6 activity raises EIF2AK2's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.46× lower at baseline in the lines without IFI6 | 0.002 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[DDX60L]] | B | IFI6 activity raises DDX60L's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 3.30× lower at baseline in the lines without IFI6 | 0.002 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[SHFL]] | B | IFI6 activity raises SHFL's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.27× lower at baseline in the lines without IFI6 | 0.002 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.869). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.9, 52.3); signed map (66.0, 29.8). **Vector** length 151, 63.7% of its response variance represented; |z| ≥ 3 in 1,312 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.75 to 56); *interferon gamma response* (hallmark, mean cos +0.75 to 60); *Interferon gamma signaling* (reactome, mean cos +0.73 to 17).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Cobimetinib (drug)]] 5 µM |  | +4.7 | +3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +1.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.3 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.2 | +2.7 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.9 | -2.3 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.3 | +2.7 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.0 | +2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.8 | +3.1 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -10.8 | -15.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -8.7 | -12.3 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -8.3 | -8.0 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -8.2 | -9.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | -7.8 | -4.6 |

## What is on record

|  |  |
|---|---|
| Name | interferon alpha inducible protein 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:27,666,064-27,672,212 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IFI616, FAM14C, 6-16, IFI-6-16; previously G1P3 |
| Reactome | 4 pathways, smallest: Modulation of host responses by IFN-stimulated genes; Interferon alpha/beta signaling; Interferon Signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P09912](https://www.uniprot.org/uniprotkb/P09912) (Interferon alpha-inducible protein 6):

> Interferon-stimulated protein that plays an important role in innate immune response against a wide variety of viruses. Inhibits flavivirus replication by preventing the formation of virus-induced endoplasmic reticulum membrane invaginations, which are double-membrane vesicles that flaviviruses use for their replication. Has an antiviral activity towards hepatitis C virus/HCV by inhibiting the EGFR signaling pathway, whose activation is required for entry of the virus into cells. Within the …

**Summary**, from NCBI Gene [2537](https://www.ncbi.nlm.nih.gov/gene/2537):

> This gene was first identified as one of the many genes induced by interferon. The encoded protein may play a critical role in the regulation of apoptosis. A minisatellite that consists of 26 repeats of a 12 nucleotide repeating element resembling the mammalian splice donor consensus sequence begins near the end of the second exon. Alternatively spliced transcript variants that encode different isoforms by using the two downstream repeat units as splice donor sites have been described. …

**Accessions** — [HGNC:4054](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4054) · Entrez [2537](https://www.ncbi.nlm.nih.gov/gene/2537) · UniProt [P09912](https://www.uniprot.org/uniprotkb/P09912) · Ensembl [ENSG00000126709](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126709)

## Data

Gene col 4753: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4753); `tables/drug_effects.parquet` (50 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4753, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4753]; `tensor/DDL_lfc|DDL_z.npy` [4753]; `embed/gene_vectors.npy` [4753]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4753 or target_col == 4753). Every well: [[IFI6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFI6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
