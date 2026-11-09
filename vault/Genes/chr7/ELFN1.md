---
symbol: "ELFN1"
type: "gene"
col: 13499
ensembl_id: "ENSG00000225968"
name: "extracellular leucine rich repeat and fibronectin type III domain containing 1"
location: "7p22.3"
module: 128
arm: "+"
pooled_cpm: 9.64
n_lines_expressing: 26
n_dd_up: 9
n_dd_down: 3
n_dd_up_clean: 7
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 15
direction_downstream: 35
tags: ["gene", "module/128"]
generated_by: "tahoemap"
---

# ELFN1

*extracellular leucine rich repeat and fibronectin type III domain containing 1* — 7p22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.23× (z +14.2, q 9e-43, up in 11 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.719× (z -4.1, q 0.020, down in 14 of 22 measured lines) ⚠ cell-cycle shift, explains ~25% of this change. The strongest without an alert is [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM: 0.740× (z -3.8, q 0.046, down in 10 of 22 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 4 lines (NCI-H23 0.137×, HS-578T 0.155×, A-172 0.278×, C-33 A 0.259×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 4 lines (C-33 A 0.203×, A-172 0.233×, MIA PaCa-2 0.211×, NCI-H23 0.261×; ⚠ cell-cycle shift, explains ~64% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 0.225×, LOX-IMVI 0.273×; ⚠ toxic; transcription drop); [[Verteporfin (drug)]] 5 µM in 1 line (AN3 CA 0.0631×); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.386×); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (HOP62 0.0769×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CBFA2T3]] (+0.67, fdr 7e-06), [[NFATC1]] (+0.65, fdr 7e-06), [[CHD5]] (+0.65, fdr 7e-06).
> It is in [[Module 128]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[SSC5D]] → it (grade B ⚠); 35 go from it, the strongest it → [[SAMD11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13499.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.23×** | +14.2 | 9e-43 | 11/21 (HS-578T, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.01×** | +12.3 | 2e-32 | 8/22 (SW480, HOP62, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +9.6 | 2e-19 | 6/19 (A549, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +8.5 | 3e-15 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.69×** | +6.0 | 3e-07 | 7/22 (HS-578T, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.56×** | +5.1 | 3e-05 | 5/21 (SW480, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.27×** | +4.2 | 0.002 | 5/23 (A498, C32, …) | top dose only | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.40×** | +4.2 | 0.002 | 10/22 (HS-578T, SK-MEL-2, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.41×** | +4.0 | 0.004 | 0/12 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13499.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 10 here, 6 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 4 lines (NCI-H23 0.137×, HS-578T 0.155×, A-172 0.278×, C-33 A 0.259×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 5 µM in 4 lines (C-33 A 0.203×, A-172 0.233×, MIA PaCa-2 0.211×, NCI-H23 0.261×; ⚠ cell-cycle shift, explains ~64% of this change); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H23 0.225×, LOX-IMVI 0.273×; ⚠ toxic; transcription drop); [[Verteporfin (drug)]] 5 µM in 1 line (AN3 CA 0.0631×); [[Homoharringtonine (drug)]] 5 µM in 1 line (C-33 A 0.386×); [[Glycyrrhizic acid (drug)]] 0.5 µM in 1 line (HOP62 0.0769×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.719×** | -4.1 | 0.020 | 14/22 (NCI-H23, A-172, …) | top dose only |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.740×** | -3.8 | 0.046 | 10/22 (CHP-212, HOP62, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.752×** | -3.6 | 0.070 | 11/22 (A-427, LOX-IMVI, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.780× | -3.1 | 0.22 | 10/22 (PANC-1, LOX-IMVI, …) | rises with dose | composition shift |
| [[Fingolimod (hydrochloride) (drug)]] 0.05 µM |  | 0.781× | -3.1 | 0.22 | 2/22 (SW480, SHP-77) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13499. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 41.1 | 0 | 5 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.137× (z -14.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 30.7 | 1 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.61× (z +9.7) | [[Panobinostat (drug)]] 5 µM 0.233× (z -10.5) ⚠ cell-cycle shift, explains ~64% of this change |
| [[HS-578T (line)]] | alt | 17.1 | 2 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.73× (z +15.8) | [[Panobinostat (drug)]] 0.5 µM 0.155× (z -10.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LOX-IMVI (line)]] | wt | 33.1 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0494× (z -19.9) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 48.4 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.203× (z -10.8) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.386× (z -9.1) |
| [[AN3 CA (line)]] | alt | 51.1 | 0 | 2 | — | [[Verteporfin (drug)]] 5 µM 0.0631× (z -12.3) |
| [[MIA PaCa-2 (line)]] | alt | 30.9 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.211× (z -10.3) ⚠ cell-cycle shift, explains ~64% of this change |
| [[RPMI-7951 (line)]] | alt | 24.6 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.12× (z +12.9) | — |
| [[A-427 (line)]] | wt | 20.9 | 0 | 1 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.251× (z -8.7) ⚠ cell-cycle shift, explains ~25% of this change |
| [[A549 (line)]] | wt | 5.15 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.65× (z +10.2) | — |
| [[HepG2_C3A (line)]] | wt | 4.20 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +9.0) | — |
| [[HOP62 (line)]] | alt | 3.81 | 0 | 1 | — | [[Glycyrrhizic acid (drug)]] 0.5 µM 0.0769× (z -9.0) |
| [[SW480 (line)]] | alt | 2.95 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.15× (z +8.8) | — |
| [[A498 (line)]] | wt | 6.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.901 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.13 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.750 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.761 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.14 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.831 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.17 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.995 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.27 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.34 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.996 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.07 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 6.26 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 56.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.841 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 49.9 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.09 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.82 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.962 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.05 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.29 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13499), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CBFA2T3]] | +0.67 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[NFATC1]] | +0.65 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[CHD5]] | +0.65 | +0.61 / +0.61 | both halves | 7e-06 |  |
| [[ADGRB1]] | +0.61 | +0.55 / +0.62 | both halves | 1e-05 |  |
| [[PALM]] | +0.60 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[KCNQ2]] | +0.58 | +0.50 / +0.57 | both halves | 1e-05 |  |
| [[RFPL1S]] | +0.58 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[GRID1]] | +0.57 | +0.44 / +0.62 | both halves | 3e-05 |  |
| [[LINC00466]] | +0.57 | +0.54 / +0.49 | both halves | 1e-05 |  |
| [[LINC02643]] | +0.57 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[CPEB1]] | +0.56 | +0.60 / +0.46 | both halves | 3e-05 |  |
| [[CDH23]] | +0.55 | +0.53 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 7, C 8. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SSC5D]] | B | SSC5D activity raises ELFN1's level | lines that do not express SSC5D (11) vs lines expressing it (39) | 3.12× lower at baseline in the lines without SSC5D | 0.030 | ⚠ within organs, on part of the lines; also absent: GXYLT2, SLC17A7, GNAZ; maybe low, not absent |
| [[MIR1915HG]] | B | MIR1915HG activity raises ELFN1's level | lines that do not express MIR1915HG (13) vs lines expressing it (37) | 3.09× lower at baseline in the lines without MIR1915HG | 0.039 | ⚠ within organs, on part of the lines; also absent: SOCS2-AS1, NT5M, SOCS2; maybe low, not absent |
| [[CHD5]] | B | CHD5 activity raises ELFN1's level | lines that do not express CHD5 (30) vs lines expressing it (20) | 1.91× lower at baseline in the lines without CHD5 | 0.041 | ⚠ within organs, on part of the lines; also absent: DPYSL5, RET, KIF1A; maybe low, not absent |
| [[CBFA2T3]] | B | CBFA2T3 activity raises ELFN1's level | lines that do not express CBFA2T3 (24) vs lines expressing it (26) | 2.00× lower at baseline in the lines without CBFA2T3 | 0.042 | ⚠ within organs, on part of the lines; also absent: BEGAIN, CHGB, KIF1A |
| [[BEGAIN]] | B | BEGAIN activity raises ELFN1's level | lines that do not express BEGAIN (23) vs lines expressing it (27) | 2.21× lower at baseline in the lines without BEGAIN | 0.043 | ⚠ within organs, on part of the lines; also absent: ROR2, CBFA2T3, FXYD6; maybe low, not absent |
| [[SAMD11]] | B | SAMD11 activity raises ELFN1's level | lines that do not express SAMD11 (13) vs lines expressing it (37) | 3.64× lower at baseline in the lines without SAMD11 | 0.060 | ⚠ within organs, on part of the lines; also absent: TTC28, B4GALNT1, RASSF8-AS1 |
| [[RFPL1S]] | B | RFPL1S activity raises ELFN1's level | lines that do not express RFPL1S (16) vs lines expressing it (34) | 2.51× lower at baseline in the lines without RFPL1S | 0.077 | ⚠ within organs, on part of the lines; also absent: RASSF2, PHF21B, CECR2; maybe low, not absent |
| [[PAX2]] | C | PAX2 activity raises ELFN1's level | lines that do not express PAX2 (33) vs lines expressing it (17) | 3.58× lower at baseline in the lines without PAX2 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PREX2, LINC02643, ADD2; co-absent with the target |
| [[WT1-AS]] | C | WT1-AS activity raises ELFN1's level | lines that do not express WT1-AS (36) vs lines expressing it (14) | 2.74× lower at baseline in the lines without WT1-AS | 0.007 | ⚠ within organs, on part of the lines; also absent: WT1, ZNF677, GCG; co-absent with the target |
| [[PDZD4]] | C | PDZD4 activity raises ELFN1's level | lines that do not express PDZD4 (22) vs lines expressing it (28) | 3.34× lower at baseline in the lines without PDZD4 | 0.033 | ⚠ within organs, on part of the lines; also absent: CECR2, CPEB1, COLEC12; co-absent with the target |
| [[PHF21B]] | C | PHF21B activity raises ELFN1's level | lines that do not express PHF21B (21) vs lines expressing it (29) | 3.14× lower at baseline in the lines without PHF21B | 0.052 | ⚠ within organs, on part of the lines; also absent: JAM3, ADAM23, ADD2; co-absent with the target |
| [[DCLK2]] | C | DCLK2 activity raises ELFN1's level | lines that do not express DCLK2 (17) vs lines expressing it (33) | 3.78× lower at baseline in the lines without DCLK2 | 0.064 | ⚠ within organs, on part of the lines; also absent: LINC03041, HECW2, AFF3; co-absent with the target |

### Downstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 26, C 9. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SAMD11]] | B | ELFN1 activity raises SAMD11's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 3.19× lower at baseline in the lines without ELFN1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[TCF7L1]] | B | ELFN1 activity strengthens TCF7L1's drug response | lines that do not express ELFN1 (15) vs lines expressing it (22) | the lines without ELFN1 respond 0.63× as strongly (z diff +2.70); strongest at Homoharringtonine 5 µM: 0.63x vs 0.41x (z diff +3.9) | 0.010 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547; target measured in part of the lines; artifact flags |
| [[CHD5]] | B | ELFN1 activity raises CHD5's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 2.14× lower at baseline in the lines without ELFN1 | 0.010 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[NINL]] | B | ELFN1 activity raises NINL's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 2.60× lower at baseline in the lines without ELFN1 | 0.014 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[CYS1]] | B | ELFN1 activity raises CYS1's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 1.64× lower at baseline in the lines without ELFN1 | 0.015 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[BRSK2]] | B | ELFN1 activity raises BRSK2's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 1.82× lower at baseline in the lines without ELFN1 | 0.016 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[MIR1915HG]] | B | ELFN1 activity raises MIR1915HG's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 1.76× lower at baseline in the lines without ELFN1 | 0.018 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[PRRT2]] | B | ELFN1 activity raises PRRT2's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 1.92× lower at baseline in the lines without ELFN1 | 0.019 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[EBF4]] | B | ELFN1 activity raises EBF4's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 2.42× lower at baseline in the lines without ELFN1 | 0.020 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[ZBTB46]] | B | ELFN1 activity raises ZBTB46's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 1.57× lower at baseline in the lines without ELFN1 | 0.023 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[KREMEN2]] | B | ELFN1 activity raises KREMEN2's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 1.69× lower at baseline in the lines without ELFN1 | 0.025 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |
| [[SSC5D]] | B | ELFN1 activity raises SSC5D's level | lines that do not express ELFN1 (24) vs lines expressing it (26) | 2.27× lower at baseline in the lines without ELFN1 | 0.026 | ⚠ within organs, on part of the lines; also absent: SORCS2, JAM3, ENSG00000269547 |

## Where it sits

- **Module**: [[Module 128]]; 37 genes; every member is in the + arm (projection on the module's main direction 0.733). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.8, 37.8); signed map (24.7, 24.3). **Vector** length 58.6, 14.0% of its response variance represented; |z| ≥ 3 in 594 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +5.2 | +14.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.3 | +9.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.8 | +4.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.3 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +12.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +1.5 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.1 | +1.6 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.2 | -3.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -1.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.9 | -0.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.7 | -1.8 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -2.1 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -1.1 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -1.9 |
|  | [[Gefitinib (drug)]] 5 µM |  | -1.0 | -2.0 |
|  | [[Bexarotene (drug)]] 0.5 µM |  | -1.0 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | extracellular leucine rich repeat and fibronectin type III domain containing 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 7p22.3 — chr7:1,665,745-1,747,946 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously PPP1R28 |
| Gene groups (HGNC) | Fibronectin type III domain containing; Protein phosphatase 1 regulatory subunits |
| Matched by | ensembl_id |

**Function**, from UniProt [P0C7U0](https://www.uniprot.org/uniprotkb/P0C7U0) (Protein ELFN1):

> Postsynaptic protein that regulates circuit dynamics in the central nervous system by modulating the temporal dynamics of interneuron recruitment. Specifically present in excitatory synapses onto oriens-lacunosum molecular (OLM) interneurons and acts as a regulator of presynaptic release probability to direct the formation of highly facilitating pyramidal-OLM synapses (By similarity). Inhibits phosphatase activity of protein phosphatase 1 (PP1) complexes.

**Summary**, from NCBI Gene [392617](https://www.ncbi.nlm.nih.gov/gene/392617):

> Predicted to enable signaling receptor activity. Predicted to be involved in chemical synaptic transmission and synapse organization. Predicted to act upstream of or within several processes, including synapse assembly; synaptic signaling; and visual perception. Predicted to be located in dendrite and excitatory synapse. Predicted to be active in plasma membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:33154](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:33154) · Entrez [392617](https://www.ncbi.nlm.nih.gov/gene/392617) · UniProt [P0C7U0](https://www.uniprot.org/uniprotkb/P0C7U0) · Ensembl [ENSG00000225968](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000225968)

## Data

Gene col 13499: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13499); `tables/drug_effects.parquet` (14 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13499, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13499]; `tensor/DDL_lfc|DDL_z.npy` [13499]; `embed/gene_vectors.npy` [13499]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13499 or target_col == 13499). Every well: [[ELFN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ELFN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
