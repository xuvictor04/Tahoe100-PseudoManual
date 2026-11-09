---
symbol: "COL11A1"
type: "gene"
col: 693
ensembl_id: "ENSG00000060718"
name: "collagen type XI alpha 1 chain"
location: "1p21.1"
module: 9
arm: "+"
pooled_cpm: 21.26
n_lines_expressing: 11
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 15
direction_downstream: 17
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# COL11A1

*collagen type XI alpha 1 chain* — 1p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.77× (z +12.6, q 7e-34, up in 2 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.21× (z +10.7, q 2e-24, up in 1 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.05 µM in 1 line (PANC-1 0.280×); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0801×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UNC5C]] (+0.69, fdr 7e-06), [[NREP]] (+0.65, fdr 9e-06), [[COL3A1]] (+0.61, fdr 7e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 15 arrows point to it, the strongest [[ZNF677]] → it (grade C ⚠); 17 go from it, the strongest it → [[COL3A1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 693.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.77×** | +12.6 | 7e-34 | 2/8 (A-172, C-33 A) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.29×** | +10.9 | 3e-25 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.21×** | +10.7 | 2e-24 | 1/9 (A-172) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.35×** | +9.7 | 3e-20 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +5.9 | 4e-07 | 1/9 (A-172) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.42×** | +4.8 | 2e-04 | 3/9 (A-172, SK-MEL-2, …) | top dose only | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.52×** | +4.6 | 3e-04 | 1/5 (A-172) | top dose only | noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.60×** | +4.5 | 5e-04 | 0/9 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.54×** | +4.0 | 0.004 | 1/8 (A-172) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.53×** | +3.9 | 0.005 | 0/9 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.44×** | +3.5 | 0.024 | 1/9 (SK-MEL-2) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.028 | 0/9 | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +3.3 | 0.043 | 0/9 | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.080 | 1/9 (A-172) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 693.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 0.05 µM in 1 line (PANC-1 0.280×); [[Idarubicin (hydrochloride) (drug)]] 0.5 µM in 1 line (CHP-212 0.0801×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[5-Azacytidine (drug)]] 5 µM |  | 0.697× | -3.4 | 0.39 | 6/9 (SW 1088, hTERT-HPNE, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 693. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 66.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM 0.0801× (z -8.8) |
| [[PANC-1 (line)]] | alt | 172 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.280× (z -9.6) |
| [[A-172 (line)]] | wt | 7.72 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.02 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.81 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 91.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.77 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.46 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.81 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 61.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.66 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.62 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.55 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.57 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3,338 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 150 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.23 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.07 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.03 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.93 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 693), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC5C]] | +0.69 | +0.67 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[NREP]] | +0.65 | +0.57 / +0.60 | both halves | 9e-06 | **novel candidate** |
| [[COL3A1]] | +0.61 | +0.59 / +0.61 | both halves | 7e-06 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 965 |
| [[CARD18]] | +0.59 | +0.60 / +0.58 | both halves | 7e-06 | **novel candidate** |
| [[ROBO1]] | +0.59 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[CDH12]] | +0.59 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[MIR99AHG]] | +0.59 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[COL5A2]] | +0.59 | +0.57 / +0.57 | both halves | 1e-05 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 976 |
| [[ANGPT1]] | +0.58 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[RBMS3]] | +0.56 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[FAP]] | +0.56 | +0.50 / +0.56 | both halves | 1e-05 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 525 |
| [[MMRN1]] | +0.56 | +0.52 / +0.52 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*15 arrows, 15 of them with an alert ⚠; grade A 0, B 0, C 15. Shown: the 12 strongest; 3 more arrows (3 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF677]] | C | ZNF677 activity raises COL11A1's level | lines that do not express ZNF677 (39) vs lines expressing it (11) | 11.29× lower at baseline in the lines without ZNF677 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL11A1, COL3A1, GCG; co-absent with the target |
| [[LINC02240]] | C | LINC02240 activity raises COL11A1's level | lines that do not express LINC02240 (35) vs lines expressing it (15) | 5.70× lower at baseline in the lines without LINC02240 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC02941, CHL1, EDNRB; maybe low, not absent; co-absent with the target |
| [[EDNRB]] | C | EDNRB activity raises COL11A1's level | lines that do not express EDNRB (34) vs lines expressing it (16) | 3.67× lower at baseline in the lines without EDNRB | 0.009 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: COL19A1, AEBP1, COL1A2; co-absent with the target |
| [[LINC02008]] | C | LINC02008 activity raises COL11A1's level | lines that do not express LINC02008 (36) vs lines expressing it (14) | 3.69× lower at baseline in the lines without LINC02008 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: LINC01242, ENSG00000260126, ENSG00000253363; co-absent with the target |
| [[COL3A1]] | C | COL3A1 activity raises COL11A1's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 5.50× lower at baseline in the lines without COL3A1 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677; co-absent with the target |
| [[LINC01098]] | C | LINC01098 activity raises COL11A1's level | lines that do not express LINC01098 (36) vs lines expressing it (14) | 3.29× lower at baseline in the lines without LINC01098 | 0.027 | ⚠ within organs, on part of the lines; also absent: LINC02109, GREM1, ENSG00000288098; maybe low, not absent; co-absent with the target |
| [[CCNYL2]] | C | CCNYL2 activity raises COL11A1's level | lines that do not express CCNYL2 (29) vs lines expressing it (21) | 3.64× lower at baseline in the lines without CCNYL2 | 0.036 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with KRAS; also absent: LINC00839, KC6, MSR1; co-absent with the target |
| [[COL1A2]] | C | COL1A2 activity raises COL11A1's level | lines that do not express COL1A2 (37) vs lines expressing it (13) | 3.71× lower at baseline in the lines without COL1A2 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PKD1L1-AS1, FCRLA, PSG5; co-absent with the target |
| [[MAGI2-AS3]] | C | MAGI2-AS3 activity raises COL11A1's level | lines that do not express MAGI2-AS3 (30) vs lines expressing it (20) | 4.03× lower at baseline in the lines without MAGI2-AS3 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MAGI2, MMP2, SPARC; co-absent with the target |
| [[MEOX2]] | C | MEOX2 activity raises COL11A1's level | lines that do not express MEOX2 (36) vs lines expressing it (14) | 5.20× lower at baseline in the lines without MEOX2 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02566, MMRN1, ENSG00000232252; co-absent with the target |
| [[AK4P3]] | C | AK4P3 activity raises COL11A1's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 4.68× lower at baseline in the lines without AK4P3 | 0.062 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF; co-absent with the target |
| [[PCDH18]] | C | PCDH18 activity raises COL11A1's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 5.11× lower at baseline in the lines without PCDH18 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677; co-absent with the target |

### Downstream of this gene

*17 arrows, 17 of them with an alert ⚠; grade A 0, B 0, C 17. Shown: the 12 strongest; 5 more arrows (5 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL3A1]] | C | COL11A1 activity raises COL3A1's level | lines that do not express COL11A1 (39) vs lines expressing it (11) | 12.15× lower at baseline in the lines without COL11A1 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ZNF677, THY1, LINC02566; co-absent with the target |
| [[CCNYL2]] | C | COL11A1 activity raises CCNYL2's level | lines that do not express COL11A1 (39) vs lines expressing it (11) | 4.52× lower at baseline in the lines without COL11A1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ZNF677, THY1, LINC02566; co-absent with the target |
| [[ZNF677]] | C | COL11A1 activity raises ZNF677's level | lines that do not express COL11A1 (39) vs lines expressing it (11) | 4.68× lower at baseline in the lines without COL11A1 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ZNF677, THY1, LINC02566; co-absent with the target |
| [[GPNMB]] | C | COL11A1 activity raises GPNMB's level | lines that do not express COL11A1 (39) vs lines expressing it (11) | 5.12× lower at baseline in the lines without COL11A1 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ZNF677, THY1, LINC02566; co-absent with the target |
| [[COL1A2]] | C | COL11A1 activity raises COL1A2's level | lines that do not express COL11A1 (39) vs lines expressing it (11) | 8.04× lower at baseline in the lines without COL11A1 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ZNF677, THY1, LINC02566; co-absent with the target |
| [[LINC01098]] | C | COL11A1 activity raises LINC01098's level | lines that do not express COL11A1 (39) vs lines expressing it (11) | 3.32× lower at baseline in the lines without COL11A1 | 0.031 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ZNF677, THY1, LINC02566; co-absent with the target |
| [[LINC00470]] | C | COL11A1 activity raises LINC00470's level | lines that do not express COL11A1 (39) vs lines expressing it (11) | 7.43× lower at baseline in the lines without COL11A1 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ZNF677, THY1, LINC02566; co-absent with the target |
| [[LINC01203]] | C | COL11A1 activity raises LINC01203's level | lines that do not express COL11A1 (39) vs lines expressing it (11) | 2.39× lower at baseline in the lines without COL11A1 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ZNF677, THY1, LINC02566; co-absent with the target |
| [[LINC02240]] | C | COL11A1 activity raises LINC02240's level | lines that do not express COL11A1 (39) vs lines expressing it (11) | 3.65× lower at baseline in the lines without COL11A1 | 0.066 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ZNF677, THY1, LINC02566; co-absent with the target |
| [[CARD18]] | C | COL11A1 activity raises CARD18's level | lines that do not express COL11A1 (39) vs lines expressing it (11) | 3.40× lower at baseline in the lines without COL11A1 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ZNF677, THY1, LINC02566; co-absent with the target |
| [[COL5A2]] | C | COL11A1 activity raises COL5A2's level | lines that do not express COL11A1 (39) vs lines expressing it (11) | 6.17× lower at baseline in the lines without COL11A1 | 0.072 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ZNF677, THY1, LINC02566; co-absent with the target |
| [[LINC02506]] | C | COL11A1 activity raises LINC02506's level | lines that do not express COL11A1 (39) vs lines expressing it (11) | 4.35× lower at baseline in the lines without COL11A1 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ZNF677, THY1, LINC02566; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.547). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (39.3, 31.0); signed map (37.9, 34.3). **Vector** length 27.2, 8.22% of its response variance represented; |z| ≥ 3 in 192 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.9 | +12.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +9.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +10.9 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +1.4 | +4.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.8 | +1.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +0.8 | +2.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.7 | +2.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.6 | +2.3 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.7 | -1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.7 | -2.3 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.7 | -0.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.7 | -3.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | +0.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -0.6 | -0.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | collagen type XI alpha 1 chain |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p21.1 — chr1:102,876,467-103,108,872 (-) |
| Ensembl biotype | protein_coding |
| Also known as | STL2, CO11A1; previously COLL6, DFNA37 |
| Gene groups (HGNC) | Fibrillar collagens |
| Hallmark sets | UV_RESPONSE_DN, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 17 pathways, smallest: Developmental Lineage of Pancreatic Ductal Cells; Developmental Lineage of Pancreatic Endocrine Mid Progenitor Cells; Developmental Cell Lineages of the Endocrine Pancreas |
| Matched by | ensembl_id |

**Function**, from UniProt [P12107](https://www.uniprot.org/uniprotkb/P12107) (Collagen alpha-1(XI) chain):

> May play an important role in fibrillogenesis by controlling lateral growth of collagen II fibrils.

**Summary**, from NCBI Gene [1301](https://www.ncbi.nlm.nih.gov/gene/1301):

> This gene encodes one of the two alpha chains of type XI collagen, a minor fibrillar collagen. Type XI collagen is a heterotrimer but the third alpha chain is a post-translationally modified alpha 1 type II chain. Mutations in this gene are associated with type II Stickler syndrome and with Marshall syndrome. A single-nucleotide polymorphism in this gene is also associated with susceptibility to lumbar disc herniation. Multiple transcript variants have been identified for this gene. [provided …

**Accessions** — [HGNC:2186](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2186) · Entrez [1301](https://www.ncbi.nlm.nih.gov/gene/1301) · UniProt [P12107](https://www.uniprot.org/uniprotkb/P12107) · Ensembl [ENSG00000060718](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000060718)

## Data

Gene col 693: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 693); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 693, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 693]; `tensor/DDL_lfc|DDL_z.npy` [693]; `embed/gene_vectors.npy` [693]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 693 or target_col == 693). Every well: [[COL11A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/COL11A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
