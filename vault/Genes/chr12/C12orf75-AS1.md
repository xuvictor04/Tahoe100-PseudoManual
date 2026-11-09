---
symbol: "C12orf75-AS1"
type: "gene"
col: 15055
ensembl_id: "ENSG00000257642"
name: "C12orf75 antisense RNA 1"
location: "12q23.3"
module: 151
arm: "+"
pooled_cpm: 2.64
n_lines_expressing: 28
n_dd_up: 6
n_dd_down: 9
n_dd_up_clean: 1
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 8
direction_downstream: 31
tags: ["gene", "module/151"]
generated_by: "tahoemap"
---

# C12orf75-AS1

*C12orf75 antisense RNA 1* — 12q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 4.37× (z +9.7, q 2e-19, up in 0 of 6 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM: 1.73× (z +3.7, q 0.020, up in 0 of 16 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.364× (z -6.9, q 3e-09, down in 17 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC03004]] (+0.61, fdr 1e-05), [[MARCHF4]] (+0.59, fdr 1e-05), [[SCHIP1]] (+0.58, fdr 1e-05); moves opposite to [[EDN2]] (-0.51, fdr 3e-05), [[FLVCR2]] (-0.48, fdr 3e-05), [[FBXO9]] (-0.44, fdr 5e-05).
> It is in [[Module 151]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[PRSS23]] → it (grade B ⚠); 31 go from it, the strongest it → [[PRSS23]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 7 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15055.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.37×** | +9.7 | 2e-19 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.80×** | +6.1 | 4e-07 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.83×** | +4.1 | 0.007 | 5/20 (A-172, A498, …) | rises with dose | position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.81×** | +4.0 | 0.008 | 7/24 (C32, A498, …) | rises with dose | position effect removed |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.73×** | +3.7 | 0.020 | 0/16 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.69×** | +3.6 | 0.031 | 1/13 (AsPC-1) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 1.94× | +3.2 | 0.10 | 0/8 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.61× | +3.1 | 0.12 | 0/12 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | 1.67× | +3.0 | 0.16 | 2/13 (A-172, A498) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15055.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.364×** | -6.9 | 3e-09 | 17/23 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.416×** | -5.8 | 2e-06 | 15/20 (NCI-H2030, J82, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.436×** | -5.7 | 3e-06 | 16/24 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.476×** | -5.1 | 5e-05 | 10/24 (J82, CFPAC-1, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **0.527×** | -4.4 | 0.001 | 10/24 (HEC-1-A, PANC-1, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.575×** | -3.8 | 0.015 | 13/24 (PANC-1, H4, …) | top dose only | cell-cycle shift (explains ~11% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.590×** | -3.6 | 0.023 | 12/23 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Anethole trithione (drug)]] 5 µM |  | **0.690×** | -3.6 | 0.023 | 5/23 (HOP62, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.411×** | -3.2 | 0.092 | 5/22 (HEC-1-A, LOX-IMVI, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, -0.05 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15055. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 8.39 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0126× (z -15.8) |
| [[J82 (line)]] | alt | 6.48 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0633× (z -12.8) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 0.0371× (z -10.2) |
| [[A498 (line)]] | wt | 4.23 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0719× (z -11.8) ⚠ cell-cycle shift, explains ~22% of this change |
| [[NCI-H2030 (line)]] | alt | 10.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0281× (z -16.2) ⚠ cell-cycle shift, explains ~22% of this change |
| [[A-172 (line)]] | wt | 8.13 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 0.133 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.325 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 3.07 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 0.172 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.178 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.04 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 21.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.213 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.190 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.52 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.265 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.28 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.690 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.62 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.769 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.704 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.92 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.17 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.146 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.193 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.909 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.156 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.777 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 0.886 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.160 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.230 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.02 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.828 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.145 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.203 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.266 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.228 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.221 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.196 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15055), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC03004]] | +0.61 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[MARCHF4]] | +0.59 | +0.50 / +0.62 | both halves | 1e-05 |  |
| [[SCHIP1]] | +0.58 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[KIRREL3]] | +0.57 | +0.58 / +0.56 | both halves | 1e-05 |  |
| [[AADACP1]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ADAM12]] | +0.56 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[PDCD1LG2]] | +0.56 | +0.49 / +0.55 | both halves | 1e-05 |  |
| [[IQCJ-SCHIP1]] | +0.55 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[GLIPR1]] | +0.55 | +0.50 / +0.51 | both halves | 1e-05 |  |
| [[DCBLD2]] | +0.53 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[FRMD4A]] | +0.53 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[UBASH3B]] | +0.53 | +0.43 / +0.54 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EDN2]] | -0.51 | -0.48 / -0.45 | both halves | 3e-05 |  |
| [[FLVCR2]] | -0.48 | -0.43 / -0.50 | both halves | 3e-05 |  |
| [[FBXO9]] | -0.44 | -0.39 / -0.49 | both halves | 5e-05 |  |
| [[RCOR3]] | -0.44 | -0.35 / -0.39 | both halves | 1e-04 |  |
| [[MLLT10]] | -0.44 | -0.26 / -0.44 | both halves | 4e-04 |  |
| [[CEBPD]] | -0.43 | -0.45 / -0.39 | both halves | 6e-05 |  |
| [[BIN1]] | -0.43 | -0.46 / -0.38 | both halves | 7e-05 |  |
| [[TRIP10]] | -0.42 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[ELF2]] | -0.42 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[KLF9]] | -0.42 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[C1RL]] | -0.41 | -0.55 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 3, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRSS23]] | B | PRSS23 activity raises C12orf75-AS1's level | lines that do not express PRSS23 (13) vs lines expressing it (37) | 2.15× lower at baseline in the lines without PRSS23 | 0.082 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: ETS1, TMSB4X, ZNF469; maybe low, not absent |
| [[COL13A1]] | B | COL13A1 activity raises C12orf75-AS1's level | lines that do not express COL13A1 (11) vs lines expressing it (39) | 2.08× lower at baseline in the lines without COL13A1 | 0.086 | ⚠ within organs, on part of the lines; also absent: ERAP2, KIRREL1, TRIM38 |
| [[HDAC6]] | B | HDAC6 activity raises C12orf75-AS1's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[FRMD4A]] | C | FRMD4A activity raises C12orf75-AS1's level | lines that do not express FRMD4A (24) vs lines expressing it (26) | 2.24× lower at baseline in the lines without FRMD4A | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, PTGFR, TNFAIP6; co-absent with the target |
| [[CD44]] | C | CD44 activity raises C12orf75-AS1's level | lines that do not express CD44 (15) vs lines expressing it (35) | 2.29× lower at baseline in the lines without CD44 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: GBP3, CLEC2B, ADAMTS16; co-absent with the target |
| [[GLIPR1]] | C | GLIPR1 activity raises C12orf75-AS1's level | lines that do not express GLIPR1 (21) vs lines expressing it (29) | 2.21× lower at baseline in the lines without GLIPR1 | 0.059 | ⚠ within organs, on part of the lines; also absent: STC1, ENSG00000253891, ENSG00000230615; maybe low, not absent; co-absent with the target |
| [[KIRREL3]] | C | KIRREL3 activity raises C12orf75-AS1's level | lines that do not express KIRREL3 (36) vs lines expressing it (14) | 2.06× lower at baseline in the lines without KIRREL3 | 0.074 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FOXC2, LINC01411, SRGN; co-absent with the target |
| [[STAC]] | C | STAC activity raises C12orf75-AS1's level | lines that do not express STAC (25) vs lines expressing it (25) | 1.98× lower at baseline in the lines without STAC | 0.093 | ⚠ within organs, on part of the lines; also absent: GUCY1B1, ZNF229, DNAH11; co-absent with the target |

### Downstream of this gene

*31 arrows, 31 of them with an alert ⚠; grade A 0, B 19, C 12. Shown: the 12 strongest; 19 more arrows (19 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PRSS23]] | B | C12orf75-AS1 activity raises PRSS23's level | lines that do not express C12orf75-AS1 (22) vs lines expressing it (28) | 3.84× lower at baseline in the lines without C12orf75-AS1 | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1 |
| [[C13orf46]] | B | C12orf75-AS1 activity raises C13orf46's level | lines that do not express C12orf75-AS1 (22) vs lines expressing it (28) | 2.44× lower at baseline in the lines without C12orf75-AS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1 |
| [[COL13A1]] | B | C12orf75-AS1 activity raises COL13A1's level | lines that do not express C12orf75-AS1 (22) vs lines expressing it (28) | 2.81× lower at baseline in the lines without C12orf75-AS1 | 0.040 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1 |
| [[DOCK2]] | B | C12orf75-AS1 activity raises DOCK2's level | lines that do not express C12orf75-AS1 (22) vs lines expressing it (28) | 1.89× lower at baseline in the lines without C12orf75-AS1 | 0.041 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1 |
| [[BACH1]] | B | C12orf75-AS1 activity raises BACH1's level | lines that do not express C12orf75-AS1 (22) vs lines expressing it (28) | 1.78× lower at baseline in the lines without C12orf75-AS1 | 0.053 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1 |
| [[LINC03041]] | B | C12orf75-AS1 activity raises LINC03041's level | lines that do not express C12orf75-AS1 (22) vs lines expressing it (28) | 1.66× lower at baseline in the lines without C12orf75-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1 |
| [[SYNJ2]] | B | C12orf75-AS1 activity raises SYNJ2's level | lines that do not express C12orf75-AS1 (22) vs lines expressing it (28) | 1.76× lower at baseline in the lines without C12orf75-AS1 | 0.060 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1 |
| [[REP15]] | B | C12orf75-AS1 activity raises REP15's level | lines that do not express C12orf75-AS1 (22) vs lines expressing it (28) | 1.33× lower at baseline in the lines without C12orf75-AS1 | 0.062 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1 |
| cells under [[Loperamide (hydrochloride) (drug)]] 0.5 µM | B | C12orf75-AS1 activity lowers the cells' numbers under Loperamide (hydrochloride) 0.5 µM (makes them more sensitive) | lines that do not express C12orf75-AS1 (22) vs lines expressing it (26) | the lines without C12orf75-AS1: 1.18× the cells of the other lines | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1 |
| [[EXT1]] | B | C12orf75-AS1 activity raises EXT1's level | lines that do not express C12orf75-AS1 (22) vs lines expressing it (28) | 1.61× lower at baseline in the lines without C12orf75-AS1 | 0.068 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1 |
| [[RPSAP52]] | B | C12orf75-AS1 activity raises RPSAP52's level | lines that do not express C12orf75-AS1 (22) vs lines expressing it (28) | 2.43× lower at baseline in the lines without C12orf75-AS1 | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1 |
| cells under [[Vortioxetine (drug)]] 0.5 µM | B | C12orf75-AS1 activity lowers the cells' numbers under Vortioxetine 0.5 µM (makes them more sensitive) | lines that do not express C12orf75-AS1 (22) vs lines expressing it (26) | the lines without C12orf75-AS1: 1.21× the cells of the other lines | 0.072 | ⚠ within organs, on part of the lines; also absent: ENSG00000230615, FOXC2, GLIPR1 |

## Where it sits

- **Module**: [[Module 151]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.614). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.4, 12.5); signed map (14.8, 46.5). **Vector** length 47.3, 10.2% of its response variance represented; |z| ≥ 3 in 587 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +1.7 | +6.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +1.6 | +9.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +1.4 | +0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +1.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +0.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.1 | +2.0 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.0 | +2.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +0.8 | +1.0 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -1.8 | -5.8 |
|  | [[Triamcinolone (drug)]] 5 µM |  | -1.5 | -2.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -1.4 | -2.1 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.3 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -1.3 | -2.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.2 | -2.5 |

## What is on record

|  |  |
|---|---|
| Name | C12orf75 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q23.3 — chr12:105,304,867-105,327,017 (-) |
| Ensembl biotype | lncRNA |
| Also known as | KCCAT198 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:55936](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:55936) · Entrez [105369954](https://www.ncbi.nlm.nih.gov/gene/105369954) · Ensembl [ENSG00000257642](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257642)

## Data

Gene col 15055: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15055); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15055, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15055]; `tensor/DDL_lfc|DDL_z.npy` [15055]; `embed/gene_vectors.npy` [15055]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15055 or target_col == 15055). Every well: [[C12orf75-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/C12orf75-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
