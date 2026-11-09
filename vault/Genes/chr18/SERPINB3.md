---
symbol: "SERPINB3"
type: "gene"
col: 644
ensembl_id: "ENSG00000057149"
name: "serpin family B member 3"
location: "18q21.33"
module: 155
arm: "+"
pooled_cpm: 2.83
n_lines_expressing: 12
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 8
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 23
tags: ["gene", "module/155"]
generated_by: "tahoemap"
---

# SERPINB3

*serpin family B member 3* — 18q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 8.58× (z +10.0, q 8e-21, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.84× (z +7.1, q 1e-10, up in 8 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (BT-474 0.00300×, CFPAC-1 0.0191×); [[Selinexor (drug)]] 5 µM in 2 lines (BT-474 0.0225×, CFPAC-1 0.0744×); [[Afatinib (drug)]] 0.5 µM in 1 line (BT-474 0.00321×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERPINB4]] (+0.98, fdr 7e-06, ⚠ same locus), [[S100A9]] (+0.86, fdr 7e-06), [[FGB]] (+0.86, fdr 7e-06), [[S100A8]] (+0.78, fdr 7e-06); moves opposite to [[PGR]] (-0.49, fdr 3e-05).
> It is in [[Module 155]], a single-armed module (MyD88 deficiency (TLR2/4)).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[SERPINB4]] → it (grade C ⚠); 23 go from it, the strongest it → [[NTN4]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 644.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **8.58×** | +10.0 | 8e-21 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.82×** | +8.5 | 4e-15 | 0/4 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.55×** | +8.4 | 8e-15 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.84×** | +7.1 | 1e-10 | 8/9 (Panc 03.27, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.95×** | +5.0 | 6e-05 | 0/4 | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **4.06×** | +4.8 | 1e-04 | 0/3 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.48×** | +4.4 | 9e-04 | 0/4 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.31×** | +4.0 | 0.004 | 0/6 | top dose only |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.77×** | +3.9 | 0.006 | 0/8 | rises with dose |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **2.23×** | +3.9 | 0.006 | 0/5 | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.13×** | +3.6 | 0.014 | 0/5 | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.10×** | +3.6 | 0.016 | 9/9 (Panc 03.27, BT-474, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +3.5 | 0.024 | 0/8 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.76×** | +3.3 | 0.033 | 0/4 | top dose only | noisy plate (z scaled) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **3.53×** | +3.2 | 0.055 | 1/2 (CFPAC-1) | inconsistent across doses | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.92×** | +3.1 | 0.061 | 1/6 (J82) | inconsistent across doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.45×** | +3.1 | 0.063 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.96×** | +3.0 | 0.080 | 0/6 | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 644.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 17 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (BT-474 0.00300×, CFPAC-1 0.0191×); [[Selinexor (drug)]] 5 µM in 2 lines (BT-474 0.0225×, CFPAC-1 0.0744×); [[Afatinib (drug)]] 0.5 µM in 1 line (BT-474 0.00321×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pravastatin (sodium) (drug)]] 5 µM |  | 0.471× | -3.5 | 0.11 | 1/10 (A549) | rises with dose | plate-row cell shift |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.493× | -3.5 | 0.11 | 1/10 (A549) | inconsistent across doses | position effect removed |
| [[Artesunate (drug)]] 0.5 µM |  | 0.496× | -3.4 | 0.11 | 2/9 (NCI-H1573, BT-474) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | 0.522× | -3.2 | 0.21 | 3/10 (BT-474, CFPAC-1, …) | top dose only | position effect removed |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.508× | -3.1 | 0.24 | 1/10 (HT-29) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 644. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 69.5 | 0 | 44 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.00300× (z -20.9) |
| [[CFPAC-1 (line)]] | alt | 40.9 | 0 | 13 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0191× (z -18.3) |
| [[NCI-H1792 (line)]] | alt | 11.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0502× (z -9.8) |
| [[A549 (line)]] | wt | 3.34 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0381× (z -10.1) |
| [[A-172 (line)]] | wt | 0.189 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.149 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.162 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.254 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.196 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.215 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.264 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.338 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.221 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.191 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.216 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.285 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.182 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.263 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.35 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.255 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.223 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.275 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.277 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.156 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.184 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.186 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.202 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.342 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.11 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.186 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.37 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.153 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.215 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.203 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.839 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.179 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.188 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.850 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.252 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.220 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.261 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.251 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.259 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.201 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 644), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPINB4]] | +0.98 | +0.98 / +0.98 | both halves | 7e-06 | same gene group; STRING 999; ⚠ same locus (10.9 kb, same strand: neighbours can correlate without regulation) |
| [[S100A9]] | +0.86 | +0.84 / +0.84 | both halves | 7e-06 | STRING 465 |
| [[FGB]] | +0.86 | +0.79 / +0.84 | both halves | 7e-06 | **novel candidate** |
| [[S100A8]] | +0.78 | +0.77 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[GSDMC]] | +0.75 | +0.73 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[FGG]] | +0.71 | +0.59 / +0.71 | both halves | 7e-06 | **novel candidate** |
| [[ADAM28]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[LINC01440]] | +0.69 | +0.77 / +0.57 | both halves | 9e-06 | **novel candidate** |
| [[FLRT3]] | +0.69 | +0.67 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[C2CD4A]] | +0.69 | +0.68 / +0.62 | both halves | 7e-06 | **novel candidate** |
| [[LINC02015]] | +0.68 | +0.64 / +0.67 | both halves | 7e-06 |  |
| [[CES1]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[CDH3]] | +0.63 | +0.58 / +0.67 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGR]] | -0.49 | -0.46 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 0, C 9.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINB4]] | C | SERPINB4 activity raises SERPINB3's level | lines that do not express SERPINB4 (39) vs lines expressing it (11) | 4.33× lower at baseline in the lines without SERPINB4 | 0.001 | ⚠ within organs, on part of the lines; also absent: SERPINB3, GABRP, S100A9; co-absent with the target |
| [[CP]] | C | CP activity raises SERPINB3's level | lines that do not express CP (39) vs lines expressing it (11) | 2.07× lower at baseline in the lines without CP | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ITIH2, BHMT2, APOB; co-absent with the target |
| [[TMEM163]] | C | TMEM163 activity raises SERPINB3's level | lines that do not express TMEM163 (35) vs lines expressing it (15) | 2.46× lower at baseline in the lines without TMEM163 | 0.031 | ⚠ within organs, on part of the lines; also absent: S100A9, SERPINB4, TRBC2; co-absent with the target |
| [[LINC02015]] | C | LINC02015 activity raises SERPINB3's level | lines that do not express LINC02015 (27) vs lines expressing it (23) | 1.80× lower at baseline in the lines without LINC02015 | 0.047 | ⚠ within organs, on part of the lines; also absent: SYNDIG1, CRLF2, PXDN; co-absent with the target |
| [[C2CD4A]] | C | C2CD4A activity raises SERPINB3's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 2.16× lower at baseline in the lines without C2CD4A | 0.066 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L; co-absent with the target |
| [[S100A9]] | C | S100A9 activity raises SERPINB3's level | lines that do not express S100A9 (42) vs lines expressing it (8) | 4.33× lower at baseline in the lines without S100A9 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, GSDMC, KRT20; co-absent with the target |
| [[TACSTD2]] | C | TACSTD2 activity raises SERPINB3's level | lines that do not express TACSTD2 (34) vs lines expressing it (16) | 2.41× lower at baseline in the lines without TACSTD2 | 0.068 | ⚠ within organs, on part of the lines; also absent: SLC5A1, PRKCH-AS1, KCNE3; co-absent with the target |
| [[DUOX2]] | C | DUOX2 activity raises SERPINB3's level | lines that do not express DUOX2 (32) vs lines expressing it (18) | 1.53× lower at baseline in the lines without DUOX2 | 0.091 | ⚠ within organs, on part of the lines; also absent: MMP7, SLC44A4, MAOB; co-absent with the target |
| [[SERPINB7]] | C | SERPINB7 activity raises SERPINB3's level | lines that do not express SERPINB7 (24) vs lines expressing it (26) | 1.89× lower at baseline in the lines without SERPINB7 | 0.0998 | ⚠ within organs, on part of the lines; also absent: BASP1, DNAH11, SLC16A7; co-absent with the target |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 3, C 20. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NTN4]] | B | SERPINB3 activity raises NTN4's level | lines that do not express SERPINB3 (38) vs lines expressing it (12) | 4.20× lower at baseline in the lines without SERPINB3 | 0.041 | ⚠ within organs, on part of the lines; also absent: SERPINB4, S100A9, FAM83A |
| [[LIMCH1]] | B | SERPINB3 activity raises LIMCH1's level | lines that do not express SERPINB3 (38) vs lines expressing it (12) | 3.02× lower at baseline in the lines without SERPINB3 | 0.043 | ⚠ within organs, on part of the lines; also absent: SERPINB4, S100A9, FAM83A |
| [[LINC01348]] | B | SERPINB3 activity raises LINC01348's level | lines that do not express SERPINB3 (38) vs lines expressing it (12) | 2.08× lower at baseline in the lines without SERPINB3 | 0.054 | ⚠ within organs, on part of the lines; also absent: SERPINB4, S100A9, FAM83A |
| [[ADAM28]] | C | SERPINB3 activity raises ADAM28's level | lines that do not express SERPINB3 (38) vs lines expressing it (12) | 4.62× lower at baseline in the lines without SERPINB3 | 0.004 | ⚠ within organs, on part of the lines; also absent: SERPINB4, S100A9, FAM83A; co-absent with the target |
| [[SERPINB4]] | C | SERPINB3 activity raises SERPINB4's level | lines that do not express SERPINB3 (38) vs lines expressing it (12) | 3.68× lower at baseline in the lines without SERPINB3 | 0.007 | ⚠ within organs, on part of the lines; also absent: SERPINB4, S100A9, FAM83A; co-absent with the target |
| [[TSPAN1]] | C | SERPINB3 activity raises TSPAN1's level | lines that do not express SERPINB3 (38) vs lines expressing it (12) | 2.86× lower at baseline in the lines without SERPINB3 | 0.011 | ⚠ within organs, on part of the lines; also absent: SERPINB4, S100A9, FAM83A; co-absent with the target |
| [[TMC5]] | C | SERPINB3 activity raises TMC5's level | lines that do not express SERPINB3 (38) vs lines expressing it (12) | 2.85× lower at baseline in the lines without SERPINB3 | 0.013 | ⚠ within organs, on part of the lines; also absent: SERPINB4, S100A9, FAM83A; co-absent with the target |
| [[XDH]] | C | SERPINB3 activity raises XDH's level | lines that do not express SERPINB3 (38) vs lines expressing it (12) | 3.20× lower at baseline in the lines without SERPINB3 | 0.021 | ⚠ within organs, on part of the lines; also absent: SERPINB4, S100A9, FAM83A; co-absent with the target |
| [[PDZK1IP1]] | C | SERPINB3 activity raises PDZK1IP1's level | lines that do not express SERPINB3 (38) vs lines expressing it (12) | 2.01× lower at baseline in the lines without SERPINB3 | 0.031 | ⚠ within organs, on part of the lines; also absent: SERPINB4, S100A9, FAM83A; co-absent with the target |
| [[SLC28A3]] | C | SERPINB3 activity raises SLC28A3's level | lines that do not express SERPINB3 (38) vs lines expressing it (12) | 2.52× lower at baseline in the lines without SERPINB3 | 0.031 | ⚠ within organs, on part of the lines; also absent: SERPINB4, S100A9, FAM83A; co-absent with the target |
| [[SERPINB7]] | C | SERPINB3 activity raises SERPINB7's level | lines that do not express SERPINB3 (38) vs lines expressing it (12) | 3.07× lower at baseline in the lines without SERPINB3 | 0.032 | ⚠ within organs, on part of the lines; also absent: SERPINB4, S100A9, FAM83A; co-absent with the target |
| [[ST8SIA6]] | C | SERPINB3 activity raises ST8SIA6's level | lines that do not express SERPINB3 (38) vs lines expressing it (12) | 2.89× lower at baseline in the lines without SERPINB3 | 0.032 | ⚠ within organs, on part of the lines; also absent: SERPINB4, S100A9, FAM83A; co-absent with the target |

## Where it sits

- **Module**: [[Module 155]] — MyD88 deficiency (TLR2/4); 29 genes; every member is in the + arm (projection on the module's main direction 0.911). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.3, 48.4); signed map (54.7, 23.6). **Vector** length 66.4, 30.6% of its response variance represented; |z| ≥ 3 in 405 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *MyD88 deficiency (TLR2/4)* (reactome, mean cos +0.80 to 4); *IRAK4 deficiency (TLR2/4)* (reactome, mean cos +0.80 to 4); *Regulation of TLR by endogenous ligand* (reactome, mean cos +0.80 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +10.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.6 | +8.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.5 | +3.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +8.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +1.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.3 | +3.1 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.1 | +2.8 |
|  | [[Isocorydine (drug)]] 0.5 µM |  | +1.0 | +2.8 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -2.9 | -2.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.6 | -2.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.2 | -1.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.1 | -1.5 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -1.9 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | serpin family B member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 18q21.33 — chr18:63,655,197-63,661,893 (-) |
| Ensembl biotype | protein_coding |
| Also known as | T4-A, HsT1196; previously SCC, SCCA1 |
| Gene groups (HGNC) | Serpin peptidase inhibitors |
| Reactome | 2 pathways, smallest: Neutrophil degranulation; Innate Immune System |
| Matched by | ensembl_id |

**Function**, from UniProt [P29508](https://www.uniprot.org/uniprotkb/P29508) (Serpin B3):

> May act as a papain-like cysteine protease inhibitor to modulate the host immune response against tumor cells. Also functions as an inhibitor of UV-induced apoptosis via suppression of the activity of c-Jun NH(2)-terminal kinase (JNK1).

**Summary**, from NCBI Gene [6317](https://www.ncbi.nlm.nih.gov/gene/6317):

> Enables cysteine-type endopeptidase inhibitor activity and protease binding activity. Located in cytoplasmic vesicle; extracellular exosome; and nucleus. Is active in cytosol. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:10569](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10569) · Entrez [6317](https://www.ncbi.nlm.nih.gov/gene/6317) · UniProt [P29508](https://www.uniprot.org/uniprotkb/P29508) · Ensembl [ENSG00000057149](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000057149)

## Data

Gene col 644: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 644); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 644, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 644]; `tensor/DDL_lfc|DDL_z.npy` [644]; `embed/gene_vectors.npy` [644]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 644 or target_col == 644). Every well: [[SERPINB3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SERPINB3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
