---
symbol: "CLIC5"
type: "gene"
col: 3406
ensembl_id: "ENSG00000112782"
name: "CLIC family member 5"
location: "6p21.1"
module: 8
arm: "+"
pooled_cpm: 21.67
n_lines_expressing: 13
n_dd_up: 14
n_dd_down: 1
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 153
direction_downstream: 196
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# CLIC5

*CLIC family member 5* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 3.67× (z +11.7, q 5e-29, up in 0 of 9 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.85× (z +8.2, q 5e-14, up in 0 of 11 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.641× (z -4.2, q 0.018, down in 10 of 11 measured lines) ⚠ unreliable plate only.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (LoVo 0.0922×, SW1417 0.190×, HT-29 0.102×, Panc 03.27 0.146×, …); [[Auranofin (drug)]] 5 µM in 4 lines (Panc 03.27 0.0260×, LoVo 0.0897×, HT-29 0.0642×, AsPC-1 0.0832×); [[Panobinostat (drug)]] 5 µM in 2 lines (LoVo 0.0447×, HT-29 0.0919×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMPRSS2]] (+0.85, fdr 7e-06), [[ST14]] (+0.81, fdr 7e-06), [[GCNT3]] (+0.81, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 153 arrows point to it, the strongest [[MTUS1]] → it (grade B ⚠); 196 go from it, the strongest it → [[ANXA11]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3406.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.67×** | +11.7 | 5e-29 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.19×** | +10.9 | 5e-25 | 1/10 (NCI-H2347) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +8.2 | 5e-14 | 0/11 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.06×** | +6.3 | 6e-08 | 2/9 (NCI-H2347, Panc 03.27) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.50×** | +5.4 | 7e-06 | 6/11 (SW480, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.80×** | +5.3 | 1e-05 | 1/11 (NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.56×** | +4.7 | 2e-04 | 7/11 (AsPC-1, LS 180, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +4.4 | 9e-04 | 1/11 (NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.57×** | +4.1 | 0.003 | 0/11 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.55×** | +4.0 | 0.004 | 2/11 (NCI-H2347, CFPAC-1) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Alpelisib (drug)]] 5 µM |  | **2.05×** | +3.5 | 0.022 | 4/10 (LS 180, LoVo, …) | top dose only | noisy plate (z scaled) |
| [[Saquinavir (drug)]] 5 µM |  | **1.30×** | +3.5 | 0.025 | 0/11 | all doses, stronger at high dose | position effect removed |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | **1.28×** | +3.3 | 0.038 | 2/11 (SW1417, SW48) | rises with dose | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **1.41×** | +3.1 | 0.078 | 6/11 (AsPC-1, LoVo, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3406.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 11 here, 5 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 5 lines (LoVo 0.0922×, SW1417 0.190×, HT-29 0.102×, Panc 03.27 0.146×, …); [[Auranofin (drug)]] 5 µM in 4 lines (Panc 03.27 0.0260×, LoVo 0.0897×, HT-29 0.0642×, AsPC-1 0.0832×); [[Panobinostat (drug)]] 5 µM in 2 lines (LoVo 0.0447×, HT-29 0.0919×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.641×** | -4.2 | 0.018 | 10/11 (SW1417, LoVo, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.720× | -3.1 | 0.33 | 7/11 (LoVo, LS 180, …) | inconsistent across doses | cell-cycle shift (explains ~13% here) |
| [[PH-797804 (drug)]] 0.05 µM |  | 0.710× | -3.0 | 0.33 | 0/11 | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | 0.724× | -3.0 | 0.33 | 8/11 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3406. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 319 | 0 | 16 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0355× (z -29.6) ⚠ cell-cycle shift, explains ~5% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.0922× (z -21.1) |
| [[LS 180 (line)]] | wt | 48.9 | 0 | 7 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0704× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.121× (z -12.3) |
| [[HT-29 (line)]] | alt | 111 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.102× (z -15.2) |
| [[AsPC-1 (line)]] | alt | 20.2 | 2 | 1 | [[Trametinib (drug)]] 0.5 µM 6.44× (z +8.8) | [[Auranofin (drug)]] 5 µM 0.0832× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 60.9 | 0 | 3 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0260× (z -17.9) |
| [[SW1417 (line)]] | alt | 98.9 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.190× (z -15.9) |
| [[CFPAC-1 (line)]] | alt | 30.3 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.160× (z -12.2) |
| [[SW480 (line)]] | alt | 14.1 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.171× (z -10.7) ⚠ unreliable plate only · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.240× (z -8.7) |
| [[SW48 (line)]] | wt | 18.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -8.7) ⚠ cell-cycle shift, explains ~5% of this change |
| [[A-172 (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.18 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.95 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.93 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.05 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 3.09 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 2.85 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.78 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.84 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.38 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.25 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.88 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.86 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 2.67 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.90 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3406), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMPRSS2]] | +0.85 | +0.80 / +0.86 | both halves | 7e-06 | **novel candidate** |
| [[ST14]] | +0.81 | +0.75 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[GCNT3]] | +0.81 | +0.82 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[MYO7B]] | +0.80 | +0.77 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[MUC13]] | +0.79 | +0.70 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[SLC6A20]] | +0.78 | +0.83 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[HEPH]] | +0.78 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[POF1B]] | +0.77 | +0.72 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[ADGRF1]] | +0.76 | +0.74 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[ABO]] | +0.76 | +0.78 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[PROM1]] | +0.75 | +0.70 / +0.70 | both halves | 7e-06 |  |
| [[EPS8L3]] | +0.75 | +0.68 / +0.77 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*153 arrows, 153 of them with an alert ⚠; grade A 0, B 11, C 142. Shown: the 12 strongest; 141 more arrows (141 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTUS1]] | B | MTUS1 activity raises CLIC5's level | lines that do not express MTUS1 (17) vs lines expressing it (33) | 2.71× lower at baseline in the lines without MTUS1 | 0.024 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, SHROOM3, ELF3 |
| [[TJP2]] | B | TJP2 activity raises CLIC5's level | lines that do not express TJP2 (10) vs lines expressing it (40) | 2.55× lower at baseline in the lines without TJP2 | 0.042 | ⚠ within organs, on part of the lines; also absent: PYROXD2, NRIP1, ENSG00000235609; maybe low, not absent |
| [[PLEKHG1]] | B | PLEKHG1 activity raises CLIC5's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 2.67× lower at baseline in the lines without PLEKHG1 | 0.045 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[SLC44A3-AS1]] | B | SLC44A3-AS1 activity raises CLIC5's level | lines that do not express SLC44A3-AS1 (13) vs lines expressing it (37) | 2.38× lower at baseline in the lines without SLC44A3-AS1 | 0.046 | ⚠ within organs, on part of the lines; also absent: SLC44A3, CRYBG2, ENSG00000287306; maybe low, not absent |
| [[MUC20]] | B | MUC20 activity raises CLIC5's level | lines that do not express MUC20 (14) vs lines expressing it (36) | 2.61× lower at baseline in the lines without MUC20 | 0.061 | ⚠ within organs, on part of the lines; also absent: MUC12, PRAG1; maybe low, not absent |
| [[RAPGEF5]] | B | RAPGEF5 activity raises CLIC5's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 2.54× lower at baseline in the lines without RAPGEF5 | 0.063 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[SLC44A3]] | B | SLC44A3 activity raises CLIC5's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 2.36× lower at baseline in the lines without SLC44A3 | 0.073 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[B4GALNT3]] | B | B4GALNT3 activity raises CLIC5's level | lines that do not express B4GALNT3 (16) vs lines expressing it (34) | 2.80× lower at baseline in the lines without B4GALNT3 | 0.075 | ⚠ within organs, on part of the lines; also absent: MCF2L, EPHA1, PLEKHG6 |
| [[ELF3-AS1]] | B | ELF3-AS1 activity raises CLIC5's level | lines that do not express ELF3-AS1 (15) vs lines expressing it (35) | 2.54× lower at baseline in the lines without ELF3-AS1 | 0.078 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, EFNA1; maybe low, not absent |
| [[ATP8B1]] | B | ATP8B1 activity raises CLIC5's level | lines that do not express ATP8B1 (14) vs lines expressing it (36) | 2.39× lower at baseline in the lines without ATP8B1 | 0.091 | ⚠ within organs, on part of the lines; also absent: LGALS9, CDA, KRT86 |
| [[SDCBP2]] | B | SDCBP2 activity raises CLIC5's level | lines that do not express SDCBP2 (17) vs lines expressing it (33) | 2.76× lower at baseline in the lines without SDCBP2 | 0.098 | ⚠ within organs, on part of the lines; also absent: KRT16, TRIM29, MPZL2 |
| [[ADGRF1]] | C | ADGRF1 activity raises CLIC5's level | lines that do not express ADGRF1 (35) vs lines expressing it (15) | 6.05× lower at baseline in the lines without ADGRF1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: STEAP4, TMPRSS2, TMPRSS4; co-absent with the target |

### Downstream of this gene

*196 arrows, 196 of them with an alert ⚠; grade A 0, B 59, C 137. Shown: the 12 strongest; 184 more arrows (184 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANXA11]] | B | CLIC5 activity raises ANXA11's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 3.84× lower at baseline in the lines without CLIC5 | 1e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[USP6NL]] | B | CLIC5 activity raises USP6NL's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 2.27× lower at baseline in the lines without CLIC5 | 6e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[ZNF25]] | B | CLIC5 activity lowers ZNF25's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 2.16× higher at baseline in the lines without CLIC5 | 6e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[EPS8L1]] | B | CLIC5 activity raises EPS8L1's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 4.57× lower at baseline in the lines without CLIC5 | 6e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[JUP]] | B | CLIC5 activity raises JUP's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 5.89× lower at baseline in the lines without CLIC5 | 7e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[TNFRSF21]] | B | CLIC5 activity raises TNFRSF21's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 5.35× lower at baseline in the lines without CLIC5 | 8e-04 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[MUC20]] | B | CLIC5 activity raises MUC20's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 3.84× lower at baseline in the lines without CLIC5 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[TJP2]] | B | CLIC5 activity raises TJP2's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 3.77× lower at baseline in the lines without CLIC5 | 0.001 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[LMO7]] | B | CLIC5 activity raises LMO7's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 5.78× lower at baseline in the lines without CLIC5 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[GRHL3]] | B | CLIC5 activity raises GRHL3's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 3.61× lower at baseline in the lines without CLIC5 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[IL22RA1]] | B | CLIC5 activity raises IL22RA1's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 3.38× lower at baseline in the lines without CLIC5 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |
| [[PLEKHA7]] | B | CLIC5 activity raises PLEKHA7's level | lines that do not express CLIC5 (37) vs lines expressing it (13) | 3.27× lower at baseline in the lines without CLIC5 | 0.002 | ⚠ within organs, on part of the lines; also absent: TMPRSS2, KLK11, CLRN3 |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.771). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.5, 53.5); signed map (61.0, 5.4). **Vector** length 68.2, 31.0% of its response variance represented; |z| ≥ 3 in 403 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Dectin-2 family* (reactome, mean cos +0.52 to 5); *O-linked glycosylation of mucins* (reactome, mean cos +0.55 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.2 | +10.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +11.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.4 | +6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.7 | +2.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +1.4 | +1.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.4 | +4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.3 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.1 | +2.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -2.4 | -4.2 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.8 | -1.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.4 | -3.0 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.4 | -2.4 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -1.2 | -2.3 |
|  | [[EX229 (drug)]] 5 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | CLIC family member 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:45,880,827-46,080,348 (-) |
| Ensembl biotype | protein_coding |
| Also known as | DFNB102 |
| Gene groups (HGNC) | CLIC family |
| Reactome | 4 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound by inner hair cells of the cochlea; Sensory processing of sound |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NZA1](https://www.uniprot.org/uniprotkb/Q9NZA1) (Chloride intracellular channel protein 5):

> In the soluble state, catalyzes glutaredoxin-like thiol disulfide exchange reactions with reduced glutathione as electron donor (By similarity). Can insert into membranes and form non-selective ion channels almost equally permeable to Na(+), K(+) and Cl(-). Required for normal hearing. It is necessary for the formation of stereocilia in the inner ear and normal development of the organ of Corti (By similarity). May play a role in the regulation of transepithelial ion absorption and secretion. …

**Summary**, from NCBI Gene [53405](https://www.ncbi.nlm.nih.gov/gene/53405):

> This gene encodes a member of the chloride intracellular channel (CLIC) family of chloride ion channels. The encoded protein associates with actin-based cytoskeletal structures and may play a role in multiple processes including hair cell stereocilia formation, myoblast proliferation and glomerular podocyte and endothelial cell maintenance. Alternatively spliced transcript variants encoding multiple isoforms have been observed for this gene. [provided by RefSeq, Dec 2011]

**Accessions** — [HGNC:13517](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13517) · Entrez [53405](https://www.ncbi.nlm.nih.gov/gene/53405) · UniProt [Q9NZA1](https://www.uniprot.org/uniprotkb/Q9NZA1) · Ensembl [ENSG00000112782](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000112782)

## Data

Gene col 3406: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3406); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3406, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3406]; `tensor/DDL_lfc|DDL_z.npy` [3406]; `embed/gene_vectors.npy` [3406]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3406 or target_col == 3406). Every well: [[CLIC5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLIC5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
