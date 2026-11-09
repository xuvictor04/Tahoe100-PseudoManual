---
symbol: "RGS6"
type: "gene"
col: 11319
ensembl_id: "ENSG00000182732"
name: "regulator of G protein signaling 6"
location: "14q24.2"
module: 8
arm: "+"
pooled_cpm: 14.19
n_lines_expressing: 28
n_dd_up: 21
n_dd_down: 5
n_dd_up_clean: 18
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 25
direction_downstream: 5
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# RGS6

*regulator of G protein signaling 6* — 14q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.37× (z +20.6, q 0e+00, up in 14 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.667× (z -4.6, q 0.002, down in 13 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DNAH6]] (+0.65, fdr 1e-05), [[TMEM45B]] (+0.64, fdr 8e-06), [[PDE11A]] (+0.63, fdr 7e-06).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[ZNF503-AS1]] → it (grade B ⚠); 5 go from it, the strongest it → [[SIPA1L2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11319.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.37×** | +20.6 | 0e+00 | 14/24 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.90×** | +18.0 | 0e+00 | 12/22 (hTERT-HPNE, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.67×** | +16.6 | 0e+00 | 20/25 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.41×** | +14.7 | 0e+00 | 10/22 (NCI-H460, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.88×** | +12.2 | 5e-32 | 7/14 (CFPAC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.45×** | +10.7 | 8e-25 | 15/24 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.29×** | +9.9 | 3e-21 | 17/25 (NCI-H460, LoVo, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.08×** | +8.1 | 3e-14 | 7/17 (SW1417, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.71×** | +6.4 | 1e-08 | 12/23 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.45×** | +6.3 | 2e-08 | 7/25 (LoVo, SW48, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +5.4 | 4e-06 | 3/22 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.58×** | +5.3 | 6e-06 | 5/21 (LoVo, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **1.54×** | +5.0 | 3e-05 | 9/24 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.50×** | +4.8 | 6e-05 | 8/24 (NCI-H2030, C32, …) | two highest doses | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.44×** | +4.3 | 6e-04 | 11/25 (NCI-H460, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.41×** | +4.1 | 0.002 | 7/23 (HS-578T, SW48, …) | inconsistent across doses |  |
| [[Entrectinib (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.026 | 3/24 (SNU-423, KATO III, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.32×** | +3.2 | 0.047 | 12/23 (NCI-H2030, LS 180, …) | two highest doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11319.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.667×** | -4.6 | 0.002 | 13/23 (COLO 205, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.713×** | -3.9 | 0.027 | 12/24 (COLO 205, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.728×** | -3.8 | 0.027 | 9/23 (SW48, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.735×** | -3.7 | 0.032 | 10/25 (HCT15, NCI-H2030, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.752×** | -3.4 | 0.070 | 10/25 (COLO 205, HCT15, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11319. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 197 | 0 | 15 (8 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0239× (z -24.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0820× (z -23.4) |
| [[HCT15 (line)]] | alt | 110 | 0 | 10 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0543× (z -14.3) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.0607× (z -13.2) |
| [[NCI-H460 (line)]] | wt | 7.06 | 8 (1 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 9.30× (z +14.4) | — |
| [[LS 180 (line)]] | wt | 42.6 | 0 | 5 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.154× (z -11.0) ⚠ cell-cycle shift, explains ~89% of this change |
| [[LoVo (line)]] | wt | 20.3 | 2 | 2 | [[Tucidinostat (drug)]] 5 µM 4.36× (z +11.8) | [[Digitoxin (drug)]] 0.5 µM 0.140× (z -10.7) |
| [[BT-474 (line)]] | alt | 123 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.103× (z -11.3) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 16.1 | 0 | 2 (2 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.0627× (z -11.8) ⚠ transcription drop; cell-cycle shift, explains ~0% of this change |
| [[RPMI-7951 (line)]] | alt | 11.8 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 6.41× (z +9.1) | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0537× (z -10.2) |
| [[CFPAC-1 (line)]] | alt | 4.23 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.51× (z +9.2) | — |
| [[HS-578T (line)]] | alt | 7.22 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.2× (z +11.0) | — |
| [[hTERT-HPNE (line)]] | wt | 7.56 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.5× (z +11.3) | — |
| [[NCI-H1573 (line)]] | alt | 49.0 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.245× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 36.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.173× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 4.39 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.4× (z +10.6) | — |
| [[SW48 (line)]] | wt | 73.6 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.0796× (z -9.8) |
| [[A-172 (line)]] | wt | 3.09 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.53 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.08 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 3.06 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.87 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.34 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 2.97 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 2.63 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.30 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.00 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.70 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 6.53 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 34.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.35 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.63 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.39 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.22 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 5.56 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.86 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.96 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11319), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DNAH6]] | +0.65 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[TMEM45B]] | +0.64 | +0.58 / +0.61 | both halves | 8e-06 |  |
| [[PDE11A]] | +0.63 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[FLRT3]] | +0.63 | +0.62 / +0.55 | both halves | 1e-05 |  |
| [[SLC28A3]] | +0.62 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[TMEM184A]] | +0.62 | +0.58 / +0.42 | both halves | 4e-05 |  |
| [[ITGB6]] | +0.61 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[LINC02253]] | +0.61 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[SPATA6L]] | +0.60 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[NPSR1-AS1]] | +0.60 | +0.57 / +0.48 | both halves | 2e-05 |  |
| [[SLC35F1]] | +0.59 | +0.58 / +0.50 | both halves | 1e-05 |  |
| [[STS]] | +0.59 | +0.48 / +0.43 | both halves | 3e-05 | same gene group |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 18, C 7. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF503-AS1]] | B | ZNF503-AS1 activity raises RGS6's level | lines that do not express ZNF503-AS1 (20) vs lines expressing it (30) | 3.09× lower at baseline in the lines without ZNF503-AS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: ENSG00000253671, ELF3, LINC02147; maybe low, not absent |
| [[LINC01456]] | B | LINC01456 activity raises RGS6's level | lines that do not express LINC01456 (42) vs lines expressing it (8) | 3.05× lower at baseline in the lines without LINC01456 | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, CALCA, S100A8 |
| [[TOP2A]] | B | TOP2A activity lowers RGS6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SYK]] | B | SYK activity raises RGS6's level | lines that do not express SYK (30) vs lines expressing it (20) | 3.34× lower at baseline in the lines without SYK | 0.029 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |
| [[TMEM125]] | B | TMEM125 activity raises RGS6's level | lines that do not express TMEM125 (33) vs lines expressing it (17) | 3.93× lower at baseline in the lines without TMEM125 | 0.029 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: GRHL2, ATP2C2, ST14 |
| [[TSPAN1]] | B | TSPAN1 activity raises RGS6's level | lines that do not express TSPAN1 (26) vs lines expressing it (24) | 2.74× lower at baseline in the lines without TSPAN1 | 0.030 | ⚠ within organs, on part of the lines; also absent: TRIM29, CDH1, IRF6 |
| [[IL1RN]] | B | IL1RN activity raises RGS6's level | lines that do not express IL1RN (27) vs lines expressing it (23) | 2.90× lower at baseline in the lines without IL1RN | 0.031 | ⚠ within organs, on part of the lines; also absent: KRT16, SGPP2, SLC44A4 |
| [[MPZL2]] | B | MPZL2 activity raises RGS6's level | lines that do not express MPZL2 (29) vs lines expressing it (21) | 2.80× lower at baseline in the lines without MPZL2 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, IRF6, ST14 |
| [[CEACAM5]] | B | CEACAM5 activity raises RGS6's level | lines that do not express CEACAM5 (39) vs lines expressing it (11) | 4.93× lower at baseline in the lines without CEACAM5 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, ENSG00000267881 |
| [[TNNT2]] | B | TNNT2 activity raises RGS6's level | lines that do not express TNNT2 (29) vs lines expressing it (21) | 2.85× lower at baseline in the lines without TNNT2 | 0.044 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: CDH1, ATP2C2, ST14 |
| [[CAPN14]] | B | CAPN14 activity raises RGS6's level | lines that do not express CAPN14 (16) vs lines expressing it (34) | 1.99× lower at baseline in the lines without CAPN14 | 0.051 | ⚠ within organs, on part of the lines; also absent: CFAP46, EBF2, GAS7; maybe low, not absent |
| [[SAMD5]] | B | SAMD5 activity raises RGS6's level | lines that do not express SAMD5 (15) vs lines expressing it (35) | 2.26× lower at baseline in the lines without SAMD5 | 0.057 | ⚠ within organs, on part of the lines; also absent: ENSG00000287976, ENSG00000227681, TSPAN7 |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SIPA1L2]] | B | RGS6 activity raises SIPA1L2's level | lines that do not express RGS6 (22) vs lines expressing it (28) | 2.68× lower at baseline in the lines without RGS6 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, LIPG, RERG; maybe low, not absent |
| [[LINC02694]] | B | RGS6 activity raises LINC02694's level | lines that do not express RGS6 (22) vs lines expressing it (28) | 1.32× lower at baseline in the lines without RGS6 | 0.094 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, LIPG, RERG; maybe low, not absent |
| [[PPP1R3B-DT]] | B | RGS6 activity raises PPP1R3B-DT's level | lines that do not express RGS6 (22) vs lines expressing it (28) | 1.91× lower at baseline in the lines without RGS6 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, LIPG, RERG; maybe low, not absent |
| [[ADAM28]] | C | RGS6 activity raises ADAM28's level | lines that do not express RGS6 (22) vs lines expressing it (28) | 2.70× lower at baseline in the lines without RGS6 | 0.034 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, LIPG, RERG; maybe low, not absent; co-absent with the target |
| [[TARID]] | C | RGS6 activity raises TARID's level | lines that do not express RGS6 (22) vs lines expressing it (28) | 2.53× lower at baseline in the lines without RGS6 | 0.079 | ⚠ within organs, on part of the lines; also absent: ENSG00000272297, LIPG, RERG; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.586). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (22.1, 57.1); signed map (58.0, 10.4). **Vector** length 75.4, 19.1% of its response variance represented; |z| ≥ 3 in 706 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.2 | +12.2 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.2 | +14.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +8.3 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.0 | +16.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +7.8 | +18.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.4 | +6.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +3.1 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +1.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +1.9 |
| fall | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -2.5 | -0.7 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.6 | -1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -2.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.6 | -0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.5 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | regulator of G protein signaling 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q24.2 — chr14:71,932,429-72,566,530 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Regulators of G-protein signaling; MicroRNA protein coding host genes; DEP domain containing |
| Reactome | 6 pathways, smallest: Cooperation of PDCL (PhLP1) and TRiC/CCT in G-protein beta folding; Chaperonin-mediated protein folding; Protein folding |
| Matched by | ensembl_id |

**Function**, from UniProt [P49758](https://www.uniprot.org/uniprotkb/P49758) (Regulator of G protein signaling 6):

> Regulates G protein-coupled receptor signaling cascades. Inhibits signal transduction by increasing the GTPase activity of G protein alpha subunits, thereby driving them into their inactive GDP-bound form. The RGS6/GNB5 dimer enhances GNAO1 GTPase activity.

**Summary**, from NCBI Gene [9628](https://www.ncbi.nlm.nih.gov/gene/9628):

> This gene encodes a member of the RGS (regulator of G protein signaling) family of proteins, which are defined by the presence of a RGS domain that confers the GTPase-activating activity of these proteins toward certain G alpha subunits. This protein also belongs to a subfamily of RGS proteins characterized by the presence of DEP and GGL domains, the latter a G beta 5-interacting domain. The RGS proteins negatively regulate G protein signaling, and may modulate neuronal, cardiovascular, …

**Accessions** — [HGNC:10002](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10002) · Entrez [9628](https://www.ncbi.nlm.nih.gov/gene/9628) · UniProt [P49758](https://www.uniprot.org/uniprotkb/P49758) · Ensembl [ENSG00000182732](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000182732)

## Data

Gene col 11319: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11319); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11319, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11319]; `tensor/DDL_lfc|DDL_z.npy` [11319]; `embed/gene_vectors.npy` [11319]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11319 or target_col == 11319). Every well: [[RGS6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RGS6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
