---
symbol: "CARD18"
type: "gene"
col: 14943
ensembl_id: "ENSG00000255501"
name: "caspase recruitment domain family member 18"
location: "11q22.3"
module: 9
arm: "+"
pooled_cpm: 33.28
n_lines_expressing: 6
n_dd_up: 15
n_dd_down: 1
n_dd_up_clean: 11
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 17
direction_downstream: 15
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# CARD18

*caspase recruitment domain family member 18* — 11q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.45× (z +13.9, q 3e-41, up in 1 of 4 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.847× (z -4.6, q 0.002, down in 0 of 4 measured lines) ⚠ position not correctable. The strongest without an alert is [[Larotrectinib (drug)]] 5 µM: 0.729× (z -3.6, q 0.092, down in 3 of 4 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (PANC-1 0.225×, C-33 A 0.240×, SHP-77 0.297×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C-33 A 0.127×, PANC-1 0.185×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.147×, PANC-1 0.196×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CTNNA2]] (+0.66, fdr 1e-05), [[COL11A1]] (+0.59, fdr 7e-06), [[LINC01194]] (+0.58, fdr 1e-04); moves opposite to [[FOXO4]] (-0.38, fdr 4e-04).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 17 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 15 go from it, the strongest it → [[SOBP]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 4 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14943.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.45×** | +13.9 | 3e-41 | 1/4 (hTERT-HPNE) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.27×** | +9.1 | 4e-17 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.81×** | +8.2 | 4e-14 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.68×** | +6.8 | 2e-09 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.23×** | +6.4 | 2e-08 | 0/4 | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **2.04×** | +5.7 | 1e-06 | 0/4 | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.65×** | +5.6 | 2e-06 | 1/4 (SHP-77) | top dose only | cell-cycle shift (explains ~19% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.71×** | +4.3 | 0.001 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~13% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +4.1 | 0.002 | 0/4 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +3.9 | 0.005 | 0/4 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +3.6 | 0.017 | 0/4 | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.82×** | +3.4 | 0.033 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Vitamin K4 (drug)]] 0.05 µM |  | **1.51×** | +3.3 | 0.045 | 0/4 | inconsistent across doses | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.070 | 3/4 (C-33 A, PANC-1, …) | rises with dose | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.47×** | +3.1 | 0.082 | 0/4 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 14943.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 3 lines (PANC-1 0.225×, C-33 A 0.240×, SHP-77 0.297×); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (C-33 A 0.127×, PANC-1 0.185×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 2 lines (C-33 A 0.147×, PANC-1 0.196×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.847× | -4.6 | 0.002 | 0/4 | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 5 µM |  | **0.729×** | -3.6 | 0.092 | 3/4 (C-33 A, SHP-77, …) | top dose only | position effect removed |
| [[Tucatinib (drug)]] 0.5 µM |  | 0.575× | -3.2 | 0.30 | 0/4 | inconsistent across doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14943. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 475 | 0 | 6 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -12.2) |
| [[C-33 A (line)]] | alt | 221 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.127× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.240× (z -10.6) |
| [[SHP-77 (line)]] | alt | 132 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.297× (z -9.9) |
| [[A-172 (line)]] | wt | 2.50 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.85 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.10 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.84 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.32 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.19 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.55 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.68 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.57 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.68 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 3.84 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.54 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.15 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.24 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.30 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.29 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.37 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.70 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 7.05 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.19 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 6.16 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.99 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.29 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.80 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.29 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14943), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CTNNA2]] | +0.66 | +0.53 / +0.71 | both halves | 1e-05 | **novel candidate** |
| [[COL11A1]] | +0.59 | +0.60 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[LINC01194]] | +0.58 | +0.33 / +0.67 | both halves | 1e-04 |  |
| [[KCNQ5]] | +0.57 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[SOBP]] | +0.55 | +0.47 / +0.59 | both halves | 2e-05 | **novel candidate** |
| [[KLHL14]] | +0.54 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[SYT9]] | +0.53 | +0.51 / +0.53 | both halves | 1e-05 |  |
| [[MMRN1]] | +0.52 | +0.39 / +0.51 | both halves | 6e-05 |  |
| [[ZNF677]] | +0.50 | +0.66 / +0.35 | both halves | 1e-04 |  |
| [[TOX]] | +0.50 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[LINC00466]] | +0.50 | +0.45 / +0.44 | both halves | 3e-05 |  |
| [[HERC2P3-1]] | +0.50 | +0.39 / +0.49 | both halves | 5e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FOXO4]] | -0.38 | -0.26 / -0.32 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 2, C 15. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers CARD18's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 3.1% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[MMP16]] | B | MMP16 activity raises CARD18's level | lines that do not express MMP16 (23) vs lines expressing it (27) | 1.49× lower at baseline in the lines without MMP16 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000253553, NCAM2, KCNQ5 |
| [[ASNSP1]] | C | ASNSP1 activity raises CARD18's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 2.30× lower at baseline in the lines without ASNSP1 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15; co-absent with the target |
| [[CTNNA2]] | C | CTNNA2 activity raises CARD18's level | lines that do not express CTNNA2 (33) vs lines expressing it (17) | 2.79× lower at baseline in the lines without CTNNA2 | 0.006 | ⚠ within organs, on part of the lines; also absent: SRRM4, MAGEA4, KCNH7; co-absent with the target |
| [[SYT4]] | C | SYT4 activity raises CARD18's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 2.77× lower at baseline in the lines without SYT4 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA; co-absent with the target |
| [[KCNB2]] | C | KCNB2 activity raises CARD18's level | lines that do not express KCNB2 (43) vs lines expressing it (7) | 2.24× lower at baseline in the lines without KCNB2 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: RIT2, CALCA, SRRM4; maybe low, not absent; co-absent with the target |
| [[PYDC2-AS1]] | C | PYDC2-AS1 activity raises CARD18's level | lines that do not express PYDC2-AS1 (26) vs lines expressing it (24) | 2.26× lower at baseline in the lines without PYDC2-AS1 | 0.017 | ⚠ within organs, on part of the lines; also absent: BCHE, CPED1, CCNYL2; co-absent with the target |
| [[LRFN5]] | C | LRFN5 activity raises CARD18's level | lines that do not express LRFN5 (36) vs lines expressing it (14) | 2.22× lower at baseline in the lines without LRFN5 | 0.018 | ⚠ within organs, on part of the lines; also absent: LINC02267, ENSG00000275016, ASCL1; co-absent with the target |
| [[BMP5]] | C | BMP5 activity raises CARD18's level | lines that do not express BMP5 (38) vs lines expressing it (12) | 3.52× lower at baseline in the lines without BMP5 | 0.022 | ⚠ within organs, on part of the lines; also absent: LINC01035, CPLX2, SCG3; co-absent with the target |
| [[CCNYL2]], [[CCNYL2-1]] | C | CCNYL2, CCNYL2-1 activity raises CARD18's level | lines that do not express CCNYL2, CCNYL2-1 (29) vs lines expressing them (21) | 1.88× lower at baseline in the lines without CCNYL2, CCNYL2-1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target; co-absent genes |
| [[TSPYL5]] | C | TSPYL5 activity raises CARD18's level | lines that do not express TSPYL5 (36) vs lines expressing it (14) | 2.10× lower at baseline in the lines without TSPYL5 | 0.061 | ⚠ within organs, on part of the lines; also absent: ENSG00000241168, LINC02999, LINC01205; co-absent with the target |
| [[KLHL14]] | C | KLHL14 activity raises CARD18's level | lines that do not express KLHL14 (37) vs lines expressing it (13) | 1.99× lower at baseline in the lines without KLHL14 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, MTND1P23, TRIM55; co-absent with the target |

### Downstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 3, C 12. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SOBP]] | B | CARD18 activity raises SOBP's level | lines that do not express CARD18 (44) vs lines expressing it (6) | 6.05× lower at baseline in the lines without CARD18 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000237031, APOB, BMP10 |
| [[HECW2]] | B | CARD18 activity raises HECW2's level | lines that do not express CARD18 (44) vs lines expressing it (6) | 3.84× lower at baseline in the lines without CARD18 | 0.090 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000237031, APOB, BMP10 |
| [[MMP16]] | B | CARD18 activity raises MMP16's level | lines that do not express CARD18 (44) vs lines expressing it (6) | 2.41× lower at baseline in the lines without CARD18 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000237031, APOB, BMP10 |
| [[SYT4]] | C | CARD18 activity raises SYT4's level | lines that do not express CARD18 (44) vs lines expressing it (6) | 4.41× lower at baseline in the lines without CARD18 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000237031, APOB, BMP10; co-absent with the target |
| [[KCNB2]] | C | CARD18 activity raises KCNB2's level | lines that do not express CARD18 (44) vs lines expressing it (6) | 4.35× lower at baseline in the lines without CARD18 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000237031, APOB, BMP10; co-absent with the target |
| [[LRFN2]] | C | CARD18 activity raises LRFN2's level | lines that do not express CARD18 (44) vs lines expressing it (6) | 3.01× lower at baseline in the lines without CARD18 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000237031, APOB, BMP10; co-absent with the target |
| [[LINC01287]] | C | CARD18 activity raises LINC01287's level | lines that do not express CARD18 (44) vs lines expressing it (6) | 2.59× lower at baseline in the lines without CARD18 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000237031, APOB, BMP10; co-absent with the target |
| [[HGF]] | C | CARD18 activity raises HGF's level | lines that do not express CARD18 (44) vs lines expressing it (6) | 3.05× lower at baseline in the lines without CARD18 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000237031, APOB, BMP10; co-absent with the target |
| [[CCNYL2]] | C | CARD18 activity raises CCNYL2's level | lines that do not express CARD18 (44) vs lines expressing it (6) | 1.47× lower at baseline in the lines without CARD18 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000237031, APOB, BMP10; co-absent with the target |
| [[MIR493HG]] | C | CARD18 activity raises MIR493HG's level | lines that do not express CARD18 (44) vs lines expressing it (6) | 4.46× lower at baseline in the lines without CARD18 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000237031, APOB, BMP10; co-absent with the target |
| [[NPFFR2]] | C | CARD18 activity raises NPFFR2's level | lines that do not express CARD18 (44) vs lines expressing it (6) | 3.10× lower at baseline in the lines without CARD18 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000237031, APOB, BMP10; co-absent with the target |
| [[CCNYL2-1]] | C | CARD18 activity raises CCNYL2-1's level | lines that do not express CARD18 (44) vs lines expressing it (6) | 1.21× lower at baseline in the lines without CARD18 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000237031, APOB, BMP10; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.442). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.8, 31.7); signed map (37.9, 35.0). **Vector** length 20.9, 10.1% of its response variance represented; |z| ≥ 3 in 93 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.5 | +6.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.4 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.2 | +8.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.9 | +5.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +0.9 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +0.7 | +1.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +0.6 | +0.2 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.5 | +1.1 |
| fall | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -0.6 | +0.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | -0.5 | -0.3 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.5 | -1.3 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.5 | -0.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.5 | -2.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.5 | -1.1 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -0.4 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | caspase recruitment domain family member 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q22.3 — chr11:105,137,714-105,531,697 (-) |
| Ensembl biotype | protein_coding |
| Also known as | UNQ5804, ICEBERG, pseudo-ICE |
| Gene groups (HGNC) | Caspase recruitment domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P57730](https://www.uniprot.org/uniprotkb/P57730) (Caspase recruitment domain-containing protein 18):

> Inhibits generation of IL-1-beta by interacting with caspase-1 and preventing its association with RIP2. Down-regulates the release of IL1B.

**Summary**, from NCBI Gene [59082](https://www.ncbi.nlm.nih.gov/gene/59082):

> Enables CARD domain binding activity and caspase binding activity. Involved in negative regulation of interleukin-1 beta production. Part of protein-containing complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28861](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28861) · Entrez [59082](https://www.ncbi.nlm.nih.gov/gene/59082) · UniProt [P57730](https://www.uniprot.org/uniprotkb/P57730) · Ensembl [ENSG00000255501](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000255501)

## Data

Gene col 14943: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14943); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14943, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14943]; `tensor/DDL_lfc|DDL_z.npy` [14943]; `embed/gene_vectors.npy` [14943]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14943 or target_col == 14943). Every well: [[CARD18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CARD18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
