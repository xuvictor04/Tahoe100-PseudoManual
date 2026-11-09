---
symbol: "EDAR"
type: "gene"
col: 5790
ensembl_id: "ENSG00000135960"
name: "ectodysplasin A receptor"
location: "2q13"
module: 55
arm: "+"
pooled_cpm: 10.88
n_lines_expressing: 14
n_dd_up: 11
n_dd_down: 6
n_dd_up_clean: 4
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 55
direction_downstream: 82
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# EDAR

*ectodysplasin A receptor* — 2q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.71× (z +8.8, q 8e-16, up in 0 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.35× (z +3.8, q 0.015, up in 0 of 12 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.647× (z -3.9, q 0.030, down in 9 of 12 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IL20RA]] (+0.85, fdr 7e-06), [[LINC01819]] (+0.84, fdr 7e-06), [[SKAP1]] (+0.84, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 55 arrows point to it, the strongest [[BAMBI]] → it (grade B ⚠); 82 go from it, the strongest it → [[TLDC2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 7 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5790.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.71×** | +8.8 | 8e-16 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.80×** | +8.7 | 8e-16 | 0/7 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.54×** | +7.6 | 6e-12 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +4.1 | 0.006 | 0/12 | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.58×** | +4.0 | 0.006 | 0/10 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.8 | 0.015 | 0/12 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.53×** | +3.7 | 0.015 | 0/12 | top dose only | position effect removed |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.26×** | +3.7 | 0.017 | 0/5 | inconsistent across doses | noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +3.6 | 0.021 | 2/12 (HCT15, CFPAC-1) | rises with dose |  |
| [[Arbutin (drug)]] 0.05 µM |  | **1.48×** | +3.2 | 0.071 | 5/12 (KATO III, LS 180, …) | inconsistent across doses |  |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | **1.29×** | +3.2 | 0.071 | 1/12 (CFPAC-1) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 1 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5790.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.647×** | -3.9 | 0.030 | 9/12 (SW48, LS 180, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.648×** | -3.8 | 0.030 | 11/12 (SW480, SW1417, …) | rises with dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Mebendazole (drug)]] 5 µM |  | **0.642×** | -3.8 | 0.030 | 5/12 (LS 180, LoVo, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.660×** | -3.7 | 0.033 | 11/12 (SW480, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.673×** | -3.5 | 0.051 | 10/12 (SW480, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Tirabrutinib (drug)]] 0.05 µM |  | **0.670×** | -3.3 | 0.097 | 0/12 | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.776× | -3.2 | 0.12 | 6/12 (SW48, SW1417, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.713× | -3.0 | 0.19 | 7/12 (SW48, KATO III, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5790. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 53.2 | 0 | 19 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0757× (z -21.2) |
| [[SW48 (line)]] | wt | 171 | 0 | 13 (8 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0778× (z -16.8) |
| [[KATO III (line)]] | alt | 28.4 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.110× (z -15.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.143× (z -13.5) |
| [[LS 180 (line)]] | wt | 15.5 | 0 | 9 (6 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0111× (z -17.3) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0961× (z -12.7) |
| [[SW1417 (line)]] | alt | 93.4 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.137× (z -14.8) |
| [[HEC-1-A (line)]] | alt | 54.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.248× (z -12.5) |
| [[COLO 205 (line)]] | alt | 28.0 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0581× (z -13.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0590× (z -13.6) |
| [[LoVo (line)]] | wt | 6.83 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -9.7) |
| [[A-172 (line)]] | wt | 1.03 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.867 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.799 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 7.81 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.978 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.965 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 5.54 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 7.48 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.987 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.894 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.23 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.819 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.10 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.843 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.935 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.966 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.959 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.14 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.794 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.895 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.890 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.18 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5790), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IL20RA]] | +0.85 | +0.85 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[LINC01819]] | +0.84 | +0.84 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[SKAP1]] | +0.84 | +0.85 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[BMP4]] | +0.83 | +0.83 / +0.75 | both halves | 7e-06 | STRING 627 |
| [[CLRN3]] | +0.82 | +0.82 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[VWA2]] | +0.80 | +0.81 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[EPS8L3]] | +0.80 | +0.79 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[HNF4A]] | +0.79 | +0.79 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[GPX2]] | +0.79 | +0.79 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[C9orf152]] | +0.79 | +0.72 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[GJB1]] | +0.77 | +0.71 / +0.74 | both halves | 7e-06 |  |
| [[TMEM139]] | +0.77 | +0.72 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*55 arrows, 55 of them with an alert ⚠; grade A 0, B 1, C 54. Shown: the 12 strongest; 43 more arrows (43 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BAMBI]] | B | BAMBI activity raises EDAR's level | lines that do not express BAMBI (16) vs lines expressing it (34) | 1.59× lower at baseline in the lines without BAMBI | 0.057 | ⚠ within organs, on part of the lines; also absent: PPARGC1A, ACKR3, CADPS2; maybe low, not absent |
| [[LINC01819]] | C | LINC01819 activity raises EDAR's level | lines that do not express LINC01819 (29) vs lines expressing it (21) | 3.88× lower at baseline in the lines without LINC01819 | 0.005 | ⚠ within organs, on part of the lines; also absent: MOGAT3, LGR6, A1CF; maybe low, not absent; co-absent with the target |
| [[EPS8L3]] | C | EPS8L3 activity raises EDAR's level | lines that do not express EPS8L3 (35) vs lines expressing it (15) | 6.97× lower at baseline in the lines without EPS8L3 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC02964, EDAR, HNF4A; co-absent with the target |
| [[HPGD]] | C | HPGD activity raises EDAR's level | lines that do not express HPGD (30) vs lines expressing it (20) | 3.55× lower at baseline in the lines without HPGD | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000251584, IL20RA, SDR16C5; co-absent with the target |
| [[HNF4A]] | C | HNF4A activity raises EDAR's level | lines that do not express HNF4A (34) vs lines expressing it (16) | 4.50× lower at baseline in the lines without HNF4A | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, GCNT3, LINC02964; co-absent with the target |
| [[USH1C]] | C | USH1C activity raises EDAR's level | lines that do not express USH1C (34) vs lines expressing it (16) | 5.08× lower at baseline in the lines without USH1C | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, CLRN3, HHLA2; co-absent with the target |
| [[IL20RA]] | C | IL20RA activity raises EDAR's level | lines that do not express IL20RA (33) vs lines expressing it (17) | 4.62× lower at baseline in the lines without IL20RA | 0.016 | ⚠ within organs, on part of the lines; also absent: SLC6A20, EDAR, KLK10; co-absent with the target |
| [[C1orf116]] | C | C1orf116 activity raises EDAR's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 5.12× lower at baseline in the lines without C1orf116 | 0.016 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target |
| [[C6orf132]] | C | C6orf132 activity raises EDAR's level | lines that do not express C6orf132 (27) vs lines expressing it (23) | 3.79× lower at baseline in the lines without C6orf132 | 0.019 | ⚠ within organs, on part of the lines; also absent: PCSK9, RNF223, CDH1; co-absent with the target |
| [[GPR35]] | C | GPR35 activity raises EDAR's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 4.02× lower at baseline in the lines without GPR35 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent; co-absent with the target |
| [[MPZL2]] | C | MPZL2 activity raises EDAR's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 4.43× lower at baseline in the lines without MPZL2 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14; co-absent with the target |
| [[KLK6]] | C | KLK6 activity raises EDAR's level | lines that do not express KLK6 (34) vs lines expressing it (16) | 5.38× lower at baseline in the lines without KLK6 | 0.021 | ⚠ within organs, on part of the lines; also absent: EPS8L3, KLK7, TRIM15; co-absent with the target |

### Downstream of this gene

*82 arrows, 82 of them with an alert ⚠; grade A 0, B 15, C 67. Shown: the 12 strongest; 70 more arrows (70 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TLDC2]] | B | EDAR activity raises TLDC2's level | lines that do not express EDAR (36) vs lines expressing it (14) | 2.99× lower at baseline in the lines without EDAR | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, KLK10, DSG3 |
| [[BAMBI]] | B | EDAR activity raises BAMBI's level | lines that do not express EDAR (36) vs lines expressing it (14) | 2.85× lower at baseline in the lines without EDAR | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, KLK10, DSG3 |
| [[LINC02254]] | B | EDAR activity raises LINC02254's level | lines that do not express EDAR (36) vs lines expressing it (14) | 2.01× lower at baseline in the lines without EDAR | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, KLK10, DSG3 |
| [[ARHGEF16]] | B | EDAR activity raises ARHGEF16's level | lines that do not express EDAR (36) vs lines expressing it (14) | 3.23× lower at baseline in the lines without EDAR | 0.034 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, KLK10, DSG3 |
| [[STXBP6]] | B | EDAR activity raises STXBP6's level | lines that do not express EDAR (36) vs lines expressing it (14) | 2.58× lower at baseline in the lines without EDAR | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, KLK10, DSG3 |
| [[TJP2]] | B | EDAR activity raises TJP2's level | lines that do not express EDAR (36) vs lines expressing it (14) | 3.23× lower at baseline in the lines without EDAR | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, KLK10, DSG3 |
| [[BAIAP2L2]] | B | EDAR activity raises BAIAP2L2's level | lines that do not express EDAR (36) vs lines expressing it (14) | 3.12× lower at baseline in the lines without EDAR | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, KLK10, DSG3 |
| [[ARHGEF34P]] | B | EDAR activity raises ARHGEF34P's level | lines that do not express EDAR (36) vs lines expressing it (14) | 3.58× lower at baseline in the lines without EDAR | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, KLK10, DSG3 |
| [[DLG3]] | B | EDAR activity raises DLG3's level | lines that do not express EDAR (36) vs lines expressing it (14) | 3.35× lower at baseline in the lines without EDAR | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, KLK10, DSG3 |
| [[MROH7]] | B | EDAR activity raises MROH7's level | lines that do not express EDAR (36) vs lines expressing it (14) | 2.86× lower at baseline in the lines without EDAR | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, KLK10, DSG3 |
| [[NOSTRIN]] | B | EDAR activity raises NOSTRIN's level | lines that do not express EDAR (36) vs lines expressing it (14) | 3.16× lower at baseline in the lines without EDAR | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, KLK10, DSG3 |
| [[VILL]] | B | EDAR activity raises VILL's level | lines that do not express EDAR (36) vs lines expressing it (14) | 2.48× lower at baseline in the lines without EDAR | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: EPS8L3, KLK10, DSG3 |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.892). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.2, 47.5); signed map (63.4, 11.3). **Vector** length 77.2, 36.9% of its response variance represented; |z| ≥ 3 in 418 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +8.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.0 | +8.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +7.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +3.6 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +1.9 | +3.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.4 | +2.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.7 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.0 | +1.3 |
|  | [[AZD-7648 (drug)]] 0.5 µM |  | +1.0 | +2.0 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -1.9 | -3.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.7 | -3.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.6 | -3.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.5 | -3.0 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.4 | -2.0 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.2 | -1.2 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -1.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ectodysplasin A receptor |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q13 — chr2:108,894,471-108,989,372 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ED5, EDA3, ED1R, EDA1R; previously ED3, DL |
| Gene groups (HGNC) | Tumor necrosis factor receptor superfamily |
| Hallmark sets | KRAS_SIGNALING_DN |
| Reactome | 3 pathways, smallest: TNFs bind their physiological receptors; TNFR2 non-canonical NF-kB pathway; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UNE0](https://www.uniprot.org/uniprotkb/Q9UNE0) (Tumor necrosis factor receptor superfamily member EDAR):

> Receptor for EDA isoform A1, but not for EDA isoform A2. Mediates the activation of NF-kappa-B and JNK. May promote caspase-independent cell death.

**Summary**, from NCBI Gene [10913](https://www.ncbi.nlm.nih.gov/gene/10913):

> This gene encodes a member of the tumor necrosis factor receptor family. The encoded transmembrane protein is a receptor for the soluble ligand ectodysplasin A, and can activate the nuclear factor-kappaB, JNK, and caspase-independent cell death pathways. It is required for the development of hair, teeth, and other ectodermal derivatives. Mutations in this gene result in autosomal dominant and recessive forms of hypohidrotic ectodermal dysplasia. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:2895](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2895) · Entrez [10913](https://www.ncbi.nlm.nih.gov/gene/10913) · UniProt [Q9UNE0](https://www.uniprot.org/uniprotkb/Q9UNE0) · Ensembl [ENSG00000135960](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135960)

## Data

Gene col 5790: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5790); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5790, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5790]; `tensor/DDL_lfc|DDL_z.npy` [5790]; `embed/gene_vectors.npy` [5790]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5790 or target_col == 5790). Every well: [[EDAR — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EDAR.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
