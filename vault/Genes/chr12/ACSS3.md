---
symbol: "ACSS3"
type: "gene"
col: 3191
ensembl_id: "ENSG00000111058"
name: "acyl-CoA synthetase short chain family member 3"
location: "12q21.31"
module: 19
arm: "+"
pooled_cpm: 8.17
n_lines_expressing: 19
n_dd_up: 15
n_dd_down: 6
n_dd_up_clean: 10
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 8
direction_downstream: 6
tags: ["gene", "module/019"]
generated_by: "tahoemap"
---

# ACSS3

*acyl-CoA synthetase short chain family member 3* — 12q21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.38× (z +21.3, q 0e+00, up in 8 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.623× (z -4.8, q 7e-04, down in 13 of 16 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PAX3]] (+0.66, fdr 9e-06), [[RTN1]] (+0.64, fdr 1e-05), [[CDH7]] (+0.61, fdr 2e-05).
> It is in [[Module 019]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 6 go from it, the strongest it → [[TCF4]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3191.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.38×** | +21.3 | 0e+00 | 8/14 (BT-474, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.55×** | +12.9 | 1e-35 | 2/14 (SNU-423, CFPAC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.42×** | +8.6 | 1e-15 | 1/10 (J82) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.07×** | +6.9 | 9e-10 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.54×** | +6.2 | 5e-08 | 3/16 (BT-474, HOP62, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.85×** | +6.0 | 1e-07 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +5.7 | 9e-07 | 11/16 (NCI-H2347, CFPAC-1, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.68×** | +5.3 | 9e-06 | 4/16 (BT-474, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.66×** | +5.2 | 1e-05 | 8/16 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.59×** | +4.6 | 3e-04 | 3/13 (BT-474, SHP-77, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.53×** | +4.4 | 7e-04 | 7/16 (HOP62, CFPAC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.53×** | +4.3 | 7e-04 | 7/16 (hTERT-HPNE, HOP62, …) | two highest doses |  |
| [[Sunitinib (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.7 | 0.009 | 1/15 (HOP62) | top dose only | position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.44×** | +3.7 | 0.009 | 0/12 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Verteporfin (drug)]] 5 µM |  | **1.39×** | +3.2 | 0.052 | 1/15 (HOP62) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3191.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.623×** | -4.8 | 7e-04 | 13/16 (HepG2/C3A, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~1% here) |
| [[Diphenhydramine (drug)]] 0.05 µM |  | **0.606×** | -4.7 | 7e-04 | 2/16 (SNU-423, NCI-H2347) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.639×** | -4.6 | 1e-03 | 7/16 (NCI-H460, SK-MEL-2, …) | two highest doses | cell-cycle shift (explains ~2% here) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.686×** | -3.8 | 0.018 | 9/16 (SK-MEL-2, LOX-IMVI, …) | two highest doses |  |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.690×** | -3.8 | 0.018 | 0/16 | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.706×** | -3.5 | 0.037 | 7/16 (NCI-H460, SK-MEL-2, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, -0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3191. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 28.1 | 0 | 10 (7 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0233× (z -21.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.123× (z -11.8) |
| [[SK-MEL-2 (line)]] | alt | 129 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.144× (z -20.0) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -15.9) |
| [[HepG2_C3A (line)]] | wt | 133 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -13.0) ⚠ cell-cycle shift, explains ~14% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.204× (z -9.6) |
| [[LOX-IMVI (line)]] | wt | 26.6 | 0 | 4 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.111× (z -10.6) ⚠ cell-cycle shift, explains ~9% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.152× (z -9.1) |
| [[H4 (line)]] | wt | 39.2 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.196× (z -10.1) ⚠ cell-cycle shift, explains ~14% of this change |
| [[BT-474 (line)]] | alt | 3.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 26.6× (z +11.5) | — |
| [[NCI-H2347 (line)]] | alt | 7.22 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.98× (z +9.0) | — |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 1 (1 ⚠) | — | [[Anethole trithione (drug)]] 5 µM 0.162× (z -11.2) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 1.36 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.45 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 2.04 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.29 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.29 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.65 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.11 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.42 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.06 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.46 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.86 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.20 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.32 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.39 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.11 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.37 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.13 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3191), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 5 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PAX3]] | +0.66 | +0.65 / +0.57 | both halves | 9e-06 | **novel candidate** |
| [[RTN1]] | +0.64 | +0.52 / +0.54 | both halves | 1e-05 | same gene group |
| [[CDH7]] | +0.61 | +0.47 / +0.47 | both halves | 2e-05 |  |
| [[ST8SIA4]] | +0.61 | +0.42 / +0.61 | both halves | 4e-05 | same gene group |
| [[GREM2]] | +0.60 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[LINC00461]] | +0.60 | +0.43 / +0.57 | both halves | 3e-05 |  |
| [[KCNK2]] | +0.60 | +0.51 / +0.52 | both halves | 1e-05 |  |
| [[CHL1]] | +0.59 | +0.53 / +0.41 | both halves | 4e-05 |  |
| [[ADGRD1]] | +0.59 | +0.55 / +0.43 | both halves | 3e-05 |  |
| [[FENDRR]] | +0.58 | +0.48 / +0.46 | both halves | 3e-05 |  |
| [[CTNND2]] | +0.57 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[CCDC102B]] | +0.57 | +0.48 / +0.54 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 1, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ACSS3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PGR]] | C | PGR activity raises ACSS3's level | lines that do not express PGR (36) vs lines expressing it (14) | 2.02× lower at baseline in the lines without PGR | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: DPP10, PDE3A, KCNB2; maybe low, not absent; co-absent with the target |
| [[BCHE]] | C | BCHE activity raises ACSS3's level | lines that do not express BCHE (35) vs lines expressing it (15) | 3.06× lower at baseline in the lines without BCHE | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[CDH7]] | C | CDH7 activity raises ACSS3's level | lines that do not express CDH7 (35) vs lines expressing it (15) | 2.41× lower at baseline in the lines without CDH7 | 0.029 | ⚠ within organs, on part of the lines; also absent: KCNH5, ENSG00000260958, FUT9; co-absent with the target |
| [[DPP10]] | C | DPP10 activity raises ACSS3's level | lines that do not express DPP10 (40) vs lines expressing it (10) | 2.05× lower at baseline in the lines without DPP10 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SYT4, RIT2, LINC03000; maybe low, not absent; co-absent with the target |
| [[KCNH5]] | C | KCNH5 activity raises ACSS3's level | lines that do not express KCNH5 (36) vs lines expressing it (14) | 2.71× lower at baseline in the lines without KCNH5 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ASCL1, ENSG00000260958, UNC5D; co-absent with the target |
| [[DOK6]] | C | DOK6 activity raises ACSS3's level | lines that do not express DOK6 (30) vs lines expressing it (20) | 2.48× lower at baseline in the lines without DOK6 | 0.082 | ⚠ within organs, on part of the lines; also absent: NEFM, PI15, KCNH5; co-absent with the target |
| [[PAPPA2]] | C | PAPPA2 activity raises ACSS3's level | lines that do not express PAPPA2 (28) vs lines expressing it (22) | 2.00× lower at baseline in the lines without PAPPA2 | 0.094 | ⚠ within organs, on part of the lines; also absent: COL19A1, KCNH5, KCNK2; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TCF4]] | C | ACSS3 activity raises TCF4's level | lines that do not express ACSS3 (31) vs lines expressing it (19) | 3.74× lower at baseline in the lines without ACSS3 | 0.015 | ⚠ within organs, on part of the lines; also absent: NTNG1, ENSG00000289884, HOPX; co-absent with the target |
| [[ADGRB3]] | C | ACSS3 activity raises ADGRB3's level | lines that do not express ACSS3 (31) vs lines expressing it (19) | 4.38× lower at baseline in the lines without ACSS3 | 0.020 | ⚠ within organs, on part of the lines; also absent: NTNG1, ENSG00000289884, HOPX; co-absent with the target |
| [[FGF14]] | C | ACSS3 activity raises FGF14's level | lines that do not express ACSS3 (31) vs lines expressing it (19) | 2.82× lower at baseline in the lines without ACSS3 | 0.060 | ⚠ within organs, on part of the lines; also absent: NTNG1, ENSG00000289884, HOPX; co-absent with the target |
| [[LIN7A]] | C | ACSS3 activity raises LIN7A's level | lines that do not express ACSS3 (31) vs lines expressing it (19) | 2.74× lower at baseline in the lines without ACSS3 | 0.074 | ⚠ within organs, on part of the lines; also absent: NTNG1, ENSG00000289884, HOPX; co-absent with the target |
| [[PGR]] | C | ACSS3 activity raises PGR's level | lines that do not express ACSS3 (31) vs lines expressing it (19) | 1.79× lower at baseline in the lines without ACSS3 | 0.077 | ⚠ within organs, on part of the lines; also absent: NTNG1, ENSG00000289884, HOPX; co-absent with the target |
| [[SLITRK4]] | C | ACSS3 activity raises SLITRK4's level | lines that do not express ACSS3 (31) vs lines expressing it (19) | 1.57× lower at baseline in the lines without ACSS3 | 0.095 | ⚠ within organs, on part of the lines; also absent: NTNG1, ENSG00000289884, HOPX; co-absent with the target |

## Where it sits

- **Module**: [[Module 019]] — Neuronal System; 196 genes; every member is in the + arm (projection on the module's main direction 0.577). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.17; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (46.8, 35.9); signed map (41.9, 42.5). **Vector** length 49.8, 14.2% of its response variance represented; |z| ≥ 3 in 421 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.0 | +21.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.9 | +12.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.1 | +6.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +5.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.7 | +2.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +6.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.0 | +1.4 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +1.0 | +4.3 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.4 | -1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -1.3 | -2.8 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -1.2 | -3.5 |
|  | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.0 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | -2.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.1 | -2.4 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | acyl-CoA synthetase short chain family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q21.31 — chr12:80,936,414-81,261,210 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ21963 |
| Gene groups (HGNC) | Acyl-CoA synthetase family; MicroRNA protein coding host genes |
| Reactome | 8 pathways, smallest: Synthesis of Ketone Bodies; Ketone body metabolism; Epigenetic regulation of adipogenesis genes by MLL3 and MLL4 complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H6R3](https://www.uniprot.org/uniprotkb/Q9H6R3) (Acyl-CoA synthetase short-chain family member 3, mitochondrial):

> Catalyzes the synthesis of acetyl-CoA from short-chain fatty acids. Propionate is the preferred substrate. Can utilize acetate and butyrate with a much lower affinity (By similarity).

**Summary**, from NCBI Gene [79611](https://www.ncbi.nlm.nih.gov/gene/79611):

> Enables propionate-CoA ligase activity. Predicted to be involved in ketone body biosynthetic process. Located in mitochondrial matrix. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24723](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24723) · Entrez [79611](https://www.ncbi.nlm.nih.gov/gene/79611) · UniProt [Q9H6R3](https://www.uniprot.org/uniprotkb/Q9H6R3) · Ensembl [ENSG00000111058](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111058)

## Data

Gene col 3191: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3191); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3191, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3191]; `tensor/DDL_lfc|DDL_z.npy` [3191]; `embed/gene_vectors.npy` [3191]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3191 or target_col == 3191). Every well: [[ACSS3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ACSS3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
