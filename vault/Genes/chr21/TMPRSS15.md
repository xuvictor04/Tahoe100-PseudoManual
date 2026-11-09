---
symbol: "TMPRSS15"
type: "gene"
col: 7824
ensembl_id: "ENSG00000154646"
name: "transmembrane serine protease 15"
location: "21q21.1"
module: 9
arm: "+"
pooled_cpm: 15.59
n_lines_expressing: 9
n_dd_up: 27
n_dd_down: 0
n_dd_up_clean: 16
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 8
direction_downstream: 11
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# TMPRSS15

*transmembrane serine protease 15* — 21q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 27 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.19× (z +13.6, q 2e-39, up in 2 of 4 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.74× (z +12.3, q 4e-32, up in 1 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.357×).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ALPK2]] (+0.65, fdr 3e-05), [[FMN2]] (+0.64, fdr 1e-05), [[B3GALT1]] (+0.63, fdr 1e-05); moves opposite to [[FBXL12]] (-0.44, fdr 9e-05), [[TSHZ3-AS1]] (-0.43, fdr 8e-04, ⚠ one half only (not replicated)), [[DENND2A]] (-0.43, fdr 4e-04), [[A1BG]] (-0.42, fdr 8e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TRIM58]] → it (grade C ⚠); 11 go from it, the strongest it → [[DGKI]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 27 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7824.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.19×** | +13.6 | 2e-39 | 2/4 (HS-578T, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.74×** | +12.3 | 4e-32 | 1/6 (SNU-423) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.52×** | +10.8 | 5e-25 | 2/5 (HS-578T, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.30×** | +9.5 | 3e-19 | 2/4 (HS-578T, SNU-423) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.14×** | +9.3 | 2e-18 | 5/6 (HS-578T, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.86×** | +7.6 | 3e-12 | 4/7 (LOX-IMVI, HS-578T, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.77×** | +4.9 | 8e-05 | 4/5 (LOX-IMVI, HS-578T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.71×** | +4.6 | 3e-04 | 4/6 (LOX-IMVI, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.65×** | +4.3 | 0.001 | 1/5 (SNU-423) | top dose only |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.52×** | +4.2 | 0.002 | 1/3 (HS-578T) | top dose only | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +4.1 | 0.003 | 2/4 (SNU-423, HS-578T) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.59×** | +4.0 | 0.003 | 6/6 (HS-578T, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.57×** | +3.9 | 0.005 | 1/7 (H4) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +3.9 | 0.005 | 2/6 (SNU-423, HS-578T) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.53×** | +3.6 | 0.010 | 0/4 | inconsistent across doses | low cells (technical?); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.81×** | +3.6 | 0.010 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.74×** | +3.4 | 0.021 | 0/4 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Sapanisertib (drug)]] 0.5 µM |  | **1.69×** | +3.2 | 0.038 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.41×** | +3.0 | 0.079 | 2/6 (LOX-IMVI, HS-578T) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.42×** | +2.9 | 0.093 | 2/7 (HS-578T, RPMI-7951) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.59×** | +2.9 | 0.093 | 0/5 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 7824.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (LOX-IMVI 0.357×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.892× | -3.6 | 0.18 | 0/7 | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.659× | -3.3 | 0.19 | 0/6 | inconsistent across doses | position effect removed |
| [[Lucanthone (drug)]] 0.05 µM |  | 0.661× | -3.3 | 0.19 | 0/6 | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | 0.698× | -3.1 | 0.28 | 1/6 (hTERT-HPNE) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, +0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7824. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 23.1 | 3 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 9.44× (z +11.1) | — |
| [[LOX-IMVI (line)]] | wt | 567 | 1 | 1 | [[Homoharringtonine (drug)]] 0.5 µM 3.20× (z +8.8) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -11.1) |
| [[A-172 (line)]] | wt | 1.59 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.958 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.04 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.19 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.87 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 4.26 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.56 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.06 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.03 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.28 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.985 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.44 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.964 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.66 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.952 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.920 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.61 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.26 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.05 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.46 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7824), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALPK2]] | +0.65 | +0.46 / +0.75 | both halves | 3e-05 |  |
| [[FMN2]] | +0.64 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[B3GALT1]] | +0.63 | +0.56 / +0.49 | both halves | 1e-05 | **novel candidate** |
| [[MMP16]] | +0.62 | +0.52 / +0.60 | both halves | 1e-05 |  |
| [[LINC02241]] | +0.62 | +0.64 / +0.60 | both halves | 7e-06 |  |
| [[EPHA5]] | +0.61 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[LINC01029]] | +0.61 | +0.59 / +0.52 | both halves | 1e-05 | **novel candidate** |
| [[PCDH10]] | +0.60 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[MARCHF1]] | +0.59 | +0.49 / +0.51 | both halves | 1e-05 |  |
| [[NCAM2]] | +0.58 | +0.54 / +0.54 | both halves | 1e-05 | STRING 400 |
| [[CPED1]] | +0.58 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[BCHE]] | +0.56 | +0.45 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXL12]] | -0.44 | -0.46 / -0.37 | both halves | 9e-05 |  |
| [[TSHZ3-AS1]] | -0.43 | -0.55 / -0.20 | ⚠ one half (not replicated) | 8e-04 |  |
| [[DENND2A]] | -0.43 | -0.49 / -0.25 | both halves | 4e-04 |  |
| [[A1BG]] | -0.42 | -0.40 / -0.37 | both halves | 8e-05 |  |
| [[THBS2-AS1]] | -0.42 | -0.44 / -0.20 | both halves | 7e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRIM58]] | C | TRIM58 activity raises TMPRSS15's level | lines that do not express TRIM58 (31) vs lines expressing it (19) | 2.40× lower at baseline in the lines without TRIM58 | 0.045 | ⚠ within organs, on part of the lines; also absent: ENSG00000235749, MME, FGF20; co-absent with the target |
| [[DENND2A]] | C | DENND2A activity raises TMPRSS15's level | lines that do not express DENND2A (23) vs lines expressing it (27) | 2.18× lower at baseline in the lines without DENND2A | 0.053 | ⚠ within organs, on part of the lines; also absent: PTPRN, SPARC, BAALC; maybe low, not absent; co-absent with the target |
| [[SERPINB2]] | C | SERPINB2 activity raises TMPRSS15's level | lines that do not express SERPINB2 (36) vs lines expressing it (14) | 2.58× lower at baseline in the lines without SERPINB2 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000254337, TMPRSS15, LINC00824; co-absent with the target |
| [[ABCC9]] | C | ABCC9 activity raises TMPRSS15's level | lines that do not express ABCC9 (28) vs lines expressing it (22) | 2.49× lower at baseline in the lines without ABCC9 | 0.068 | ⚠ within organs, on part of the lines; also absent: WNT5A, PDGFRB, CCL3; maybe low, not absent; co-absent with the target |
| [[SCN3A]] | C | SCN3A activity raises TMPRSS15's level | lines that do not express SCN3A (34) vs lines expressing it (16) | 2.31× lower at baseline in the lines without SCN3A | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CCL3, TRPC4, ENSG00000224865; co-absent with the target |
| [[HMCN1]] | C | HMCN1 activity raises TMPRSS15's level | lines that do not express HMCN1 (26) vs lines expressing it (24) | 2.45× lower at baseline in the lines without HMCN1 | 0.090 | ⚠ within organs, on part of the lines; also absent: EPHA5, EPHA5-AS1, ITGA4; maybe low, not absent; co-absent with the target |
| [[ANGPT1]] | C | ANGPT1 activity raises TMPRSS15's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 2.25× lower at baseline in the lines without ANGPT1 | 0.092 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5; co-absent with the target |
| [[ALPK2]] | C | ALPK2 activity raises TMPRSS15's level | lines that do not express ALPK2 (31) vs lines expressing it (19) | 2.78× lower at baseline in the lines without ALPK2 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: PDGFRB, SPARC, KCNE4; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 0, C 11.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DGKI]] | C | TMPRSS15 activity raises DGKI's level | lines that do not express TMPRSS15 (41) vs lines expressing it (9) | 4.63× lower at baseline in the lines without TMPRSS15 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, ENSG00000224865, ENSG00000222032; co-absent with the target |
| [[LINC02241]] | C | TMPRSS15 activity raises LINC02241's level | lines that do not express TMPRSS15 (41) vs lines expressing it (9) | 7.10× lower at baseline in the lines without TMPRSS15 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, ENSG00000224865, ENSG00000222032; co-absent with the target |
| [[SNAP25]] | C | TMPRSS15 activity raises SNAP25's level | lines that do not express TMPRSS15 (41) vs lines expressing it (9) | 4.80× lower at baseline in the lines without TMPRSS15 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, ENSG00000224865, ENSG00000222032; co-absent with the target |
| [[LCP1]] | C | TMPRSS15 activity raises LCP1's level | lines that do not express TMPRSS15 (41) vs lines expressing it (9) | 2.68× lower at baseline in the lines without TMPRSS15 | 0.057 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, ENSG00000224865, ENSG00000222032; co-absent with the target |
| [[MSR1]] | C | TMPRSS15 activity raises MSR1's level | lines that do not express TMPRSS15 (41) vs lines expressing it (9) | 4.14× lower at baseline in the lines without TMPRSS15 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, ENSG00000224865, ENSG00000222032; co-absent with the target |
| [[COLEC10]] | C | TMPRSS15 activity raises COLEC10's level | lines that do not express TMPRSS15 (41) vs lines expressing it (9) | 3.31× lower at baseline in the lines without TMPRSS15 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, ENSG00000224865, ENSG00000222032; co-absent with the target |
| [[TSHZ3-AS1]] | C | TMPRSS15 activity raises TSHZ3-AS1's level | lines that do not express TMPRSS15 (41) vs lines expressing it (9) | 4.50× lower at baseline in the lines without TMPRSS15 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, ENSG00000224865, ENSG00000222032; co-absent with the target |
| [[COL12A1]] | C | TMPRSS15 activity raises COL12A1's level | lines that do not express TMPRSS15 (41) vs lines expressing it (9) | 6.45× lower at baseline in the lines without TMPRSS15 | 0.086 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, ENSG00000224865, ENSG00000222032; co-absent with the target |
| [[ANGPT1]] | C | TMPRSS15 activity raises ANGPT1's level | lines that do not express TMPRSS15 (41) vs lines expressing it (9) | 3.52× lower at baseline in the lines without TMPRSS15 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, ENSG00000224865, ENSG00000222032; co-absent with the target |
| [[ADAMTS1]] | C | TMPRSS15 activity raises ADAMTS1's level | lines that do not express TMPRSS15 (41) vs lines expressing it (9) | 5.36× lower at baseline in the lines without TMPRSS15 | 0.096 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, ENSG00000224865, ENSG00000222032; co-absent with the target |
| [[VCAM1]] | C | TMPRSS15 activity raises VCAM1's level | lines that do not express TMPRSS15 (41) vs lines expressing it (9) | 4.03× lower at baseline in the lines without TMPRSS15 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000287474, ENSG00000224865, ENSG00000222032; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.566). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.9, 29.4); signed map (38.4, 30.3). **Vector** length 17.5, 4.80% of its response variance represented; |z| ≥ 3 in 155 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +1.4 | +10.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +1.3 | +4.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.3 | +13.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.0 | +9.5 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.4 | +0.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +0.3 | +0.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.3 | +1.5 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.3 | -0.3 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -0.4 | -0.7 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -0.4 | -0.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.4 | -2.1 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.4 | -1.2 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -0.4 | -3.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.4 | -1.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -0.4 | -1.5 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -0.3 | -1.8 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -0.3 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane serine protease 15 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q21.1 — chr21:18,269,116-18,485,879 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ENTK, MGC133046; previously PRSS7 |
| Gene groups (HGNC) | Scavenger receptor cysteine rich domain containing; Type II transmembrane serine proteases; SEA domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [P98073](https://www.uniprot.org/uniprotkb/P98073) (Enteropeptidase):

> Responsible for initiating activation of pancreatic proteolytic proenzymes (trypsin, chymotrypsin and carboxypeptidase A). It catalyzes the conversion of trypsinogen to trypsin which in turn activates other proenzymes including chymotrypsinogen, procarboxypeptidases, and proelastases.

**Summary**, from NCBI Gene [5651](https://www.ncbi.nlm.nih.gov/gene/5651):

> This gene encodes an enzyme that converts the pancreatic proenzyme trypsinogen to trypsin, which activates other proenzymes including chymotrypsinogen and procarboxypeptidases. The precursor protein is cleaved into two chains that form a heterodimer linked by a disulfide bond. This protein is a member of the trypsin family of peptidases. Mutations in this gene cause enterokinase deficiency, a malabsorption disorder characterized by diarrhea and failure to thrive. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:9490](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9490) · Entrez [5651](https://www.ncbi.nlm.nih.gov/gene/5651) · UniProt [P98073](https://www.uniprot.org/uniprotkb/P98073) · Ensembl [ENSG00000154646](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154646)

## Data

Gene col 7824: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7824); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7824, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7824]; `tensor/DDL_lfc|DDL_z.npy` [7824]; `embed/gene_vectors.npy` [7824]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7824 or target_col == 7824). Every well: [[TMPRSS15 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMPRSS15.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
