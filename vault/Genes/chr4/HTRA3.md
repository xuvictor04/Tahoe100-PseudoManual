---
symbol: "HTRA3"
type: "gene"
col: 10006
ensembl_id: "ENSG00000170801"
name: "HtrA serine peptidase 3"
location: "4p16.1"
module: 167
arm: "+"
pooled_cpm: 2.7
n_lines_expressing: 19
n_dd_up: 13
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 12
direction_downstream: 37
tags: ["gene", "module/167"]
generated_by: "tahoemap"
---

# HTRA3

*HtrA serine peptidase 3* — 4p16.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.00× (z +8.6, q 4e-15, up in 2 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 5.31× (z +8.0, q 2e-13, up in 7 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.101×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.154×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (NCI-H1792 0.112×; ⚠ cell-cycle shift, explains ~48% of this change); [[Dihydroartemisinin (drug)]] 0.5 µM in 1 line (SNU-423 0.0570×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DCN]] (+0.62, fdr 2e-05), [[PTGFR]] (+0.60, fdr 2e-05), [[C1R]] (+0.59, fdr 1e-05); moves opposite to [[RASSF3]] (-0.43, fdr 1e-04), [[CSF2]] (-0.41, fdr 1e-04), [[GJC1]] (-0.39, fdr 1e-04).
> It is in [[Module 167]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[SRRM3]] → it (grade B ⚠); 37 go from it, the strongest it → [[SVEP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10006.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.00×** | +8.6 | 4e-15 | 2/6 (HOP62, HS-578T) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **9.35×** | +8.5 | 6e-15 | 1/3 (HOP62) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **5.31×** | +8.0 | 2e-13 | 7/11 (SW480, SNU-423, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.42×** | +7.3 | 5e-11 | 0/2 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.88×** | +4.6 | 4e-04 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.56×** | +4.5 | 7e-04 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~4% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **2.42×** | +4.2 | 0.002 | 1/8 (SNU-423) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.24×** | +3.9 | 0.008 | 0/8 | top dose only | cell-cycle shift (explains ~3% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.74×** | +3.7 | 0.012 | 1/14 (HOP62) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.66×** | +3.7 | 0.013 | 0/7 | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.71×** | +3.6 | 0.016 | 1/10 (SW480) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.09×** | +3.5 | 0.020 | 0/8 | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +3.3 | 0.044 | 1/11 (NCI-H2030) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10006.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H1792 0.101×); [[Homoharringtonine (drug)]] 5 µM in 1 line (NCI-H1792 0.154×); [[Ixazomib citrate (drug)]] 5 µM in 1 line (NCI-H1792 0.112×; ⚠ cell-cycle shift, explains ~48% of this change); [[Dihydroartemisinin (drug)]] 0.5 µM in 1 line (SNU-423 0.0570×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.458× | -3.1 | 0.41 | 1/14 (NCI-H1792) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 5 µM |  | 0.303× | -3.0 | 0.41 | 1/13 (Hs 766T) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10006. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 79.5 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.101× (z -13.2) |
| [[SNU-423 (line)]] | alt | 3.69 | 0 | 1 | — | [[Dihydroartemisinin (drug)]] 0.5 µM 0.0570× (z -8.6) |
| [[A-172 (line)]] | wt | 0.139 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.101 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.125 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.20 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.210 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.196 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.132 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.137 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.213 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.332 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.144 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.144 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.154 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.432 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.24 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.167 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.26 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.703 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.131 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.151 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.166 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.125 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.102 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.197 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.742 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.31 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.360 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.130 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.208 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.144 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.157 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.180 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.144 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.242 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.235 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.120 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.141 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.836 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10006), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DCN]] | +0.62 | +0.72 / +0.48 | both halves | 2e-05 | **novel candidate** |
| [[PTGFR]] | +0.60 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[C1R]] | +0.59 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[CD38]] | +0.58 | +0.51 / +0.59 | both halves | 1e-05 | **novel candidate** |
| [[BICC1]] | +0.55 | +0.44 / +0.52 | both halves | 3e-05 | **novel candidate** |
| [[SLCO2A1]] | +0.55 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[LOX]] | +0.54 | +0.49 / +0.46 | both halves | 2e-05 |  |
| [[ABCA6]] | +0.54 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[IRAK3]] | +0.53 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[HTR1F]] | +0.53 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[RNF175]] | +0.52 | +0.54 / +0.44 | both halves | 3e-05 |  |
| [[CCN4]] | +0.52 | +0.48 / +0.42 | both halves | 4e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RASSF3]] | -0.43 | -0.48 / -0.36 | both halves | 1e-04 |  |
| [[CSF2]] | -0.41 | -0.38 / -0.34 | both halves | 1e-04 |  |
| [[GJC1]] | -0.39 | -0.41 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 1, C 11.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SRRM3]] | B | SRRM3 activity lowers HTRA3's level | lines that do not express SRRM3 (17) vs lines expressing it (33) | 1.88× higher at baseline in the lines without SRRM3 | 0.008 | ⚠ within organs, on part of the lines; also absent: B4GALNT4, KIF26A, SEPTIN3; maybe low, not absent |
| [[HTR1F]] | C | HTR1F activity raises HTRA3's level | lines that do not express HTR1F (34) vs lines expressing it (16) | 2.50× lower at baseline in the lines without HTR1F | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MGP, TIMP3, AEBP1; maybe low, not absent; co-absent with the target |
| [[MGP]] | C | MGP activity raises HTRA3's level | lines that do not express MGP (35) vs lines expressing it (15) | 2.39× lower at baseline in the lines without MGP | 0.013 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TIMP3, HTR1F, AEBP1; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises HTRA3's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 2.45× lower at baseline in the lines without APCDD1L | 0.043 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[GPR173]] | C | GPR173 activity raises HTRA3's level | lines that do not express GPR173 (30) vs lines expressing it (20) | 2.13× lower at baseline in the lines without GPR173 | 0.046 | ⚠ within organs, on part of the lines; also absent: ITGA11, LUM, IRAG2; co-absent with the target |
| [[LOX]] | C | LOX activity raises HTRA3's level | lines that do not express LOX (31) vs lines expressing it (19) | 2.33× lower at baseline in the lines without LOX | 0.049 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411; co-absent with the target |
| [[PAPPA]] | C | PAPPA activity raises HTRA3's level | lines that do not express PAPPA (33) vs lines expressing it (17) | 2.64× lower at baseline in the lines without PAPPA | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: HTRA3, MSC-AS1, PDGFRB; co-absent with the target |
| [[IRAK3]] | C | IRAK3 activity raises HTRA3's level | lines that do not express IRAK3 (36) vs lines expressing it (14) | 2.06× lower at baseline in the lines without IRAK3 | 0.065 | ⚠ within organs, on part of the lines; also absent: IRAG2, TRBC2, CXCL5; co-absent with the target |
| [[PDGFRA]] | C | PDGFRA activity raises HTRA3's level | lines that do not express PDGFRA (29) vs lines expressing it (21) | 1.93× lower at baseline in the lines without PDGFRA | 0.066 | ⚠ within organs, on part of the lines; also absent: LRCH2, MAGI2-AS3, THY1; co-absent with the target |
| [[ITGB3]] | C | ITGB3 activity raises HTRA3's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 2.02× lower at baseline in the lines without ITGB3 | 0.071 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130; co-absent with the target |
| [[RNF175]] | C | RNF175 activity raises HTRA3's level | lines that do not express RNF175 (30) vs lines expressing it (20) | 2.12× lower at baseline in the lines without RNF175 | 0.075 | ⚠ within organs, on part of the lines; also absent: SCG2, ENSG00000266450, MIR493HG; co-absent with the target |
| [[PTGFR]] | C | PTGFR activity raises HTRA3's level | lines that do not express PTGFR (28) vs lines expressing it (22) | 2.04× lower at baseline in the lines without PTGFR | 0.076 | ⚠ within organs, on part of the lines; also absent: ITGA4, FRMD4A, LOX; co-absent with the target |

### Downstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 17, C 20. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SVEP1]] | B | HTRA3 activity raises SVEP1's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 2.55× lower at baseline in the lines without HTRA3 | 0.006 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |
| [[TMEM45A]] | B | HTRA3 activity raises TMEM45A's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 3.17× lower at baseline in the lines without HTRA3 | 0.011 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |
| [[FAM20C]] | B | HTRA3 activity raises FAM20C's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 3.56× lower at baseline in the lines without HTRA3 | 0.022 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |
| [[NIM1K]] | B | HTRA3 activity raises NIM1K's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 1.97× lower at baseline in the lines without HTRA3 | 0.038 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |
| [[SLC14A2]] | B | HTRA3 activity raises SLC14A2's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 1.83× lower at baseline in the lines without HTRA3 | 0.041 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |
| [[KCTD16]] | B | HTRA3 activity raises KCTD16's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 3.93× lower at baseline in the lines without HTRA3 | 0.047 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |
| [[CYP26B1]] | B | HTRA3 activity raises CYP26B1's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 1.88× lower at baseline in the lines without HTRA3 | 0.054 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |
| [[RASSF3]] | B | HTRA3 activity lowers RASSF3's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 1.31× higher at baseline in the lines without HTRA3 | 0.060 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |
| cells under [[Naproxen (drug)]] 5 µM | B | HTRA3 activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express HTRA3 (31) vs lines expressing it (17) | the lines without HTRA3: 0.85× the cells of the other lines | 0.071 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |
| cells under [[Malotilate (drug)]] 0.05 µM | B | HTRA3 activity raises the cells' numbers under Malotilate 0.05 µM (protects the cells) | lines that do not express HTRA3 (31) vs lines expressing it (17) | the lines without HTRA3: 0.81× the cells of the other lines | 0.073 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |
| [[B3GNT9]] | B | HTRA3 activity raises B3GNT9's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 1.59× lower at baseline in the lines without HTRA3 | 0.074 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |
| [[CCN4]] | B | HTRA3 activity raises CCN4's level | lines that do not express HTRA3 (31) vs lines expressing it (19) | 1.86× lower at baseline in the lines without HTRA3 | 0.076 | ⚠ within organs, on part of the lines; also absent: PAPPA, LUM, LAYN |

## Where it sits

- **Module**: [[Module 167]]; 25 genes; every member is in the + arm (projection on the module's main direction 0.552). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (52.3, 21.6); signed map (28.1, 45.0). **Vector** length 29.7, 7.27% of its response variance represented; |z| ≥ 3 in 297 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +8.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +7.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.2 | +8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +2.6 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.0 | +2.8 |
|  | [[Budesonide (drug)]] 0.5 µM |  | +0.9 | +0.8 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +0.8 | +2.0 |
| fall | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.8 | -0.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.7 | -1.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.7 | -1.9 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.6 | -3.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.6 | -0.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -0.6 | -1.7 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.6 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | HtrA serine peptidase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4p16.1 — chr4:8,269,754-8,307,098 (+) |
| Ensembl biotype | protein_coding |
| Also known as | Tasp, Prsp |
| Gene groups (HGNC) | PDZ domain containing; HtrA serine protease family |
| Matched by | ensembl_id |

**Function**, from UniProt [P83110](https://www.uniprot.org/uniprotkb/P83110) (Serine protease HTRA3):

> Serine protease that cleaves beta-casein/CSN2 as well as several extracellular matrix (ECM) proteoglycans such as decorin/DCN, biglycan/BGN and fibronectin/FN1. Inhibits signaling mediated by TGF-beta family proteins possibly indirectly by degradation of these ECM proteoglycans (By similarity). May act as a tumor suppressor. Negatively regulates, in vitro, trophoblast invasion during placental development and may be involved in the development of the placenta in vivo. May also have a role in …

**Summary**, from NCBI Gene [94031](https://www.ncbi.nlm.nih.gov/gene/94031):

> Enables endopeptidase activity; identical protein binding activity; and serine-type peptidase activity. Involved in proteolysis. Predicted to be located in extracellular region. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:30406](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30406) · Entrez [94031](https://www.ncbi.nlm.nih.gov/gene/94031) · UniProt [P83110](https://www.uniprot.org/uniprotkb/P83110) · Ensembl [ENSG00000170801](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000170801)

## Data

Gene col 10006: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10006); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10006, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10006]; `tensor/DDL_lfc|DDL_z.npy` [10006]; `embed/gene_vectors.npy` [10006]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10006 or target_col == 10006). Every well: [[HTRA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HTRA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
