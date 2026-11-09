---
symbol: "LGR5"
type: "gene"
col: 6289
ensembl_id: "ENSG00000139292"
name: "leucine rich repeat containing G protein-coupled receptor 5"
location: "12q21.1"
module: 55
arm: "+"
pooled_cpm: 28.02
n_lines_expressing: 11
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 39
direction_downstream: 57
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# LGR5

*leucine rich repeat containing G protein-coupled receptor 5* — 12q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.76× (z +11.8, q 2e-29, up in 2 of 9 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (none with an alert); the strongest is [[Artesunate (drug)]] 5 µM: 0.681× (z -4.5, q 0.004, down in 6 of 9 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[BMP4]] (+0.77, fdr 7e-06), [[VSNL1]] (+0.73, fdr 7e-06), [[IL20RA]] (+0.72, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 39 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 57 go from it, the strongest it → [[ZNF703]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6289.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.76×** | +11.8 | 2e-29 | 2/9 (SHP-77, COLO 205) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.88×** | +10.7 | 2e-24 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.36×** | +10.0 | 4e-21 | 1/7 (SW48) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +5.4 | 8e-06 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.87×** | +5.0 | 8e-05 | 4/9 (SW480, SW48, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.75×** | +4.6 | 5e-04 | 0/8 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **1.45×** | +4.3 | 0.001 | 1/9 (SHP-77) | top dose only | composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.61×** | +3.9 | 0.006 | 4/9 (HepG2/C3A, SW480, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +3.9 | 0.007 | 1/9 (SW480) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.57×** | +3.7 | 0.013 | 0/9 | inconsistent across doses | position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.5 | 0.024 | 2/9 (LoVo, HepG2/C3A) | top dose only |  |
| [[Carbamazepine (drug)]] 5 µM |  | **1.53×** | +3.5 | 0.024 | 0/9 | rises with dose | position effect removed |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.48×** | +3.2 | 0.054 | 2/9 (LoVo, LS 180) | inconsistent across doses | position effect removed |
| [[Filgotinib (drug)]] 5 µM |  | **1.46×** | +3.1 | 0.083 | 6/9 (LoVo, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6289.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **0.681×** | -4.5 | 0.004 | 6/9 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~4% here); position effect removed |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.604×** | -4.2 | 0.009 | 3/9 (SW480, LoVo, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.612×** | -4.0 | 0.010 | 3/9 (SW480, COLO 205, …) | top dose only | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | **0.636×** | -3.7 | 0.027 | 3/9 (SW48, SHP-77, …) | rises with dose | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.740×** | -3.5 | 0.052 | 7/9 (HepG2/C3A, CHP-212, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.650×** | -3.4 | 0.060 | 4/9 (LS 180, HepG2/C3A, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6289. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 553 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0911× (z -19.3) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.0442× (z -17.8) |
| [[CHP-212 (line)]] | wt | 498 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0807× (z -12.6) ⚠ cell-cycle shift, explains ~39% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0448× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 115 | 0 | 10 (7 ⚠) | — | [[Daptomycin (drug)]] 5 µM 0.0514× (z -12.8) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0829× (z -10.8) |
| [[LS 180 (line)]] | wt | 73.5 | 0 | 5 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0764× (z -10.7) |
| [[SW480 (line)]] | alt | 32.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0963× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 4.00 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.16 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.15 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.15 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 6.11 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 3.20 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.10 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.78 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.76 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.82 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.87 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.56 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.70 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.45 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 2.13 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.54 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.62 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 2.72 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.46 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.28 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.80 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.41 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.01 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.38 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.67 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.14 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.50 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 3.06 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 3.30 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 13.0 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6289), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[BMP4]] | +0.77 | +0.76 / +0.72 | both halves | 7e-06 | STRING 475 |
| [[VSNL1]] | +0.73 | +0.70 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[IL20RA]] | +0.72 | +0.65 / +0.75 | both halves | 7e-06 |  |
| [[CLRN3]] | +0.72 | +0.66 / +0.73 | both halves | 7e-06 |  |
| [[AXIN2]] | +0.70 | +0.67 / +0.65 | both halves | 7e-06 | pathway: Signaling by WNT; STRING 765 |
| [[NKD1]] | +0.69 | +0.72 / +0.67 | both halves | 7e-06 | STRING 520 |
| [[LINC01622]] | +0.69 | +0.68 / +0.59 | both halves | 7e-06 | **novel candidate** |
| [[EDAR]] | +0.69 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[TFF3]] | +0.68 | +0.64 / +0.59 | both halves | 7e-06 | STRING 480 |
| [[LINC01819]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[GJB1]] | +0.66 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[MYB]] | +0.66 | +0.56 / +0.70 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 2, C 37. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers LGR5's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[TNFRSF14-AS1]] | B | TNFRSF14-AS1 activity raises LGR5's level | lines that do not express TNFRSF14-AS1 (23) vs lines expressing it (27) | 1.71× lower at baseline in the lines without TNFRSF14-AS1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ACSL5, LINC01819, MAOB |
| [[SPON1]] | C | SPON1 activity raises LGR5's level | lines that do not express SPON1 (39) vs lines expressing it (11) | 3.06× lower at baseline in the lines without SPON1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALB1, DSG4, KRT6A; co-absent with the target |
| [[PLA2G2A]] | C | PLA2G2A activity raises LGR5's level | lines that do not express PLA2G2A (41) vs lines expressing it (9) | 4.85× lower at baseline in the lines without PLA2G2A | 0.015 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, CALB1; co-absent with the target |
| [[PEG3]] | C | PEG3 activity raises LGR5's level | lines that do not express PEG3 (41) vs lines expressing it (9) | 1.67× lower at baseline in the lines without PEG3 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: APOB, AFP, APOA1; co-absent with the target |
| [[INPP5D]] | C | INPP5D activity raises LGR5's level | lines that do not express INPP5D (34) vs lines expressing it (16) | 5.02× lower at baseline in the lines without INPP5D | 0.017 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A, TP53; also absent: CLRN3, LINC02964, LGR5; co-absent with the target |
| [[AXIN2]] | C | AXIN2 activity raises LGR5's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 4.47× lower at baseline in the lines without AXIN2 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964; co-absent with the target |
| [[PCK1]] | C | PCK1 activity raises LGR5's level | lines that do not express PCK1 (38) vs lines expressing it (12) | 6.69× lower at baseline in the lines without PCK1 | 0.020 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LGR5, GPX2, CPLX2; co-absent with the target |
| [[REG4]] | C | REG4 activity raises LGR5's level | lines that do not express REG4 (43) vs lines expressing it (7) | 4.55× lower at baseline in the lines without REG4 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, NPSR1, ENSG00000230975; co-absent with the target |
| [[ABO]] | C | ABO activity raises LGR5's level | lines that do not express ABO (32) vs lines expressing it (18) | 3.09× lower at baseline in the lines without ABO | 0.036 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: VWA2, PRSS3, SYK; co-absent with the target |
| [[HNF1A-AS1]] | C | HNF1A-AS1 activity raises LGR5's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 3.94× lower at baseline in the lines without HNF1A-AS1 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent; co-absent with the target |
| [[NPSR1]] | C | NPSR1 activity raises LGR5's level | lines that do not express NPSR1 (42) vs lines expressing it (8) | 4.07× lower at baseline in the lines without NPSR1 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: REG4, MUC17, CDH17; co-absent with the target |

### Downstream of this gene

*57 arrows, 57 of them with an alert ⚠; grade A 0, B 10, C 47. Shown: the 12 strongest; 45 more arrows (45 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF703]] | B | LGR5 activity raises ZNF703's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 2.88× lower at baseline in the lines without LGR5 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573 |
| [[BAMBI]] | B | LGR5 activity raises BAMBI's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 2.93× lower at baseline in the lines without LGR5 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573 |
| [[TSPOAP1-AS1]] | B | LGR5 activity raises TSPOAP1-AS1's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 1.81× lower at baseline in the lines without LGR5 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573 |
| [[ABHD12B]] | B | LGR5 activity raises ABHD12B's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 2.47× lower at baseline in the lines without LGR5 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573 |
| [[KIF26B]] | B | LGR5 activity raises KIF26B's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 3.37× lower at baseline in the lines without LGR5 | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573 |
| [[LDLRAD4]] | B | LGR5 activity raises LDLRAD4's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 3.10× lower at baseline in the lines without LGR5 | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573 |
| [[ZNF503-AS1]] | B | LGR5 activity raises ZNF503-AS1's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 2.51× lower at baseline in the lines without LGR5 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573 |
| [[BCAR3-AS1]] | B | LGR5 activity raises BCAR3-AS1's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 1.99× lower at baseline in the lines without LGR5 | 0.050 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573 |
| [[ZNRF3]] | B | LGR5 activity raises ZNRF3's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 2.58× lower at baseline in the lines without LGR5 | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573 |
| [[PDK4-AS1]] | B | LGR5 activity raises PDK4-AS1's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 2.08× lower at baseline in the lines without LGR5 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573 |
| [[MYB]] | C | LGR5 activity raises MYB's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 3.80× lower at baseline in the lines without LGR5 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573; co-absent with the target |
| [[INPP5D]] | C | LGR5 activity raises INPP5D's level | lines that do not express LGR5 (39) vs lines expressing it (11) | 5.63× lower at baseline in the lines without LGR5 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PCK1, DSG4, ENSG00000260573; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.694). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (24.1, 46.4); signed map (62.7, 13.1). **Vector** length 46.6, 18.9% of its response variance represented; |z| ≥ 3 in 275 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +10.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.4 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +5.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | +2.2 | +4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.0 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +3.5 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.0 | +3.7 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.0 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.0 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.0 | +1.9 |
| fall | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.4 | -2.5 |
|  | [[Artesunate (drug)]] 5 µM |  | -1.4 | -4.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -0.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.2 | -4.2 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.1 | -3.7 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -3.4 |
|  | [[Neratinib (drug)]] 5 µM |  | -1.0 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | leucine rich repeat containing G protein-coupled receptor 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.1 — chr12:71,439,798-71,586,310 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HG38, FEX; previously GPR67, GPR49 |
| Gene groups (HGNC) | G protein-coupled receptors, Class A orphans |
| Reactome | 3 pathways, smallest: Regulation of FZD by ubiquitination; TCF dependent signaling in response to WNT; Signaling by WNT |
| Matched by | ensembl_id |

**Function**, from UniProt [O75473](https://www.uniprot.org/uniprotkb/O75473) (Leucine-rich repeat-containing G protein-coupled receptor 5):

> Receptor for R-spondins that potentiates the canonical Wnt signaling pathway and acts as a stem cell marker of the intestinal epithelium and the hair follicle. Upon binding to R-spondins (RSPO1, RSPO2, RSPO3 or RSPO4), associates with phosphorylated LRP6 and frizzled receptors that are activated by extracellular Wnt receptors, triggering the canonical Wnt signaling pathway to increase expression of target genes. In contrast to classical G protein-coupled receptors, does not activate …

**Summary**, from NCBI Gene [8549](https://www.ncbi.nlm.nih.gov/gene/8549):

> The protein encoded by this gene is a leucine-rich repeat-containing receptor (LGR) and member of the G protein-coupled, 7-transmembrane receptor (GPCR) superfamily. The encoded protein is a receptor for R-spondins and is involved in the canonical Wnt signaling pathway. This protein plays a role in the formation and maintenance of adult intestinal stem cells during postembryonic development. Several transcript variants encoding different isoforms have been found for this gene. [provided by …

**Accessions** — [HGNC:4504](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4504) · Entrez [8549](https://www.ncbi.nlm.nih.gov/gene/8549) · UniProt [O75473](https://www.uniprot.org/uniprotkb/O75473) · Ensembl [ENSG00000139292](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139292)

## Data

Gene col 6289: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6289); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6289, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6289]; `tensor/DDL_lfc|DDL_z.npy` [6289]; `embed/gene_vectors.npy` [6289]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6289 or target_col == 6289). Every well: [[LGR5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LGR5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
