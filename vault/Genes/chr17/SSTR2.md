---
symbol: "SSTR2"
type: "gene"
col: 11119
ensembl_id: "ENSG00000180616"
name: "somatostatin receptor 2"
location: "17q25.1"
module: 14
arm: "+"
pooled_cpm: 2.74
n_lines_expressing: 25
n_dd_up: 34
n_dd_down: 0
n_dd_up_clean: 19
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 18
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# SSTR2

*somatostatin receptor 2* — 17q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (15 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 5.25× (z +16.2, q 0e+00, up in 12 of 12 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TNFRSF9]] (+0.75, fdr 7e-06), [[MIR155HG]] (+0.61, fdr 1e-05), [[TNFRSF1B]] (+0.61, fdr 1e-05); moves opposite to [[DENND2A]] (-0.53, fdr 4e-05), [[CHUK]] (-0.49, fdr 4e-05), [[SARDH]] (-0.47, fdr 4e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 18 go from it, the strongest it → [[NINJ1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 15 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 15 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11119.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **5.25×** | +16.2 | 0e+00 | 12/12 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **4.03×** | +13.7 | 5e-40 | 17/18 (HOP62, PANC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **6.21×** | +12.7 | 2e-34 | 19/20 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.83×** | +12.2 | 3e-32 | 14/15 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.17×** | +11.3 | 1e-27 | 9/10 (J82, A549, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.03×** | +10.8 | 5e-25 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **4.19×** | +9.9 | 3e-21 | 1/7 (PANC-1) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **4.15×** | +9.9 | 5e-21 | 18/20 (PANC-1, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **3.96×** | +9.5 | 9e-20 | 14/16 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.73×** | +9.1 | 4e-18 | 7/7 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.21×** | +8.1 | 4e-14 | 10/10 (A-172, J82, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.37×** | +7.8 | 3e-13 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.80×** | +7.1 | 5e-11 | 9/12 (HOP62, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.88×** | +7.0 | 8e-11 | 15/17 (J82, HOP62, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.69×** | +6.6 | 2e-09 | 3/6 (J82, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.11×** | +4.1 | 0.001 | 7/11 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.50×** | +4.0 | 0.002 | 4/19 (HOP62, A-172, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.59×** | +3.2 | 0.031 | 4/9 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **1.57×** | +3.1 | 0.035 | 6/12 (SW 900, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.1 | 0.043 | 5/19 (SNU-423, A549, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11119.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Pexidartinib (hydrochloride) (drug)]] 5 µM |  | 0.592× | -3.5 | 0.15 | 2/16 (Panc 03.27, J82) | inconsistent across doses |  |
| [[Malotilate (drug)]] 0.5 µM |  | 0.615× | -3.4 | 0.15 | 0/12 | inconsistent across doses | position effect removed |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.618× | -3.4 | 0.15 | 0/17 | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, +0.18 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11119. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 8.99 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.3× (z +16.5) | — |
| [[A-172 (line)]] | wt | 51.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.52× (z +14.1) | — |
| [[A549 (line)]] | wt | 1.18 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 26.6× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 1.14 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 66.8× (z +9.8) | — |
| [[HOP62 (line)]] | alt | 4.47 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.3× (z +14.1) | — |
| [[PANC-1 (line)]] | alt | 1.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 13.5× (z +9.9) | — |
| [[SNU-423 (line)]] | alt | 8.25 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.9× (z +13.6) | — |
| [[A-427 (line)]] | wt | 0.629 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.298 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.971 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.392 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 0.736 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.318 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.522 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.360 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.774 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.363 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.360 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.411 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.314 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.381 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.420 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.351 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.22 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.576 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.356 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.409 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.936 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.847 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.414 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.11 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.751 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.826 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.367 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.368 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.392 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.351 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11119), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNFRSF9]] | +0.75 | +0.73 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[MIR155HG]] | +0.61 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[TNFRSF1B]] | +0.61 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[TNFAIP6]] | +0.60 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[ELOVL4]] | +0.59 | +0.46 / +0.64 | both halves | 3e-05 |  |
| [[INA]] | +0.58 | +0.60 / +0.49 | both halves | 1e-05 |  |
| [[LINC01273]] | +0.57 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[PAX5]] | +0.57 | +0.57 / +0.54 | both halves | 1e-05 |  |
| [[CD70]] | +0.57 | +0.50 / +0.59 | both halves | 1e-05 |  |
| [[STX11]] | +0.57 | +0.43 / +0.65 | both halves | 3e-05 |  |
| [[PPP4R4]] | +0.57 | +0.54 / +0.56 | both halves | 1e-05 |  |
| [[LINC00958]] | +0.57 | +0.53 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DENND2A]] | -0.53 | -0.59 / -0.42 | both halves | 4e-05 |  |
| [[CHUK]] | -0.49 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[SARDH]] | -0.47 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[DROSHA]] | -0.46 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[MXRA5]] | -0.46 | -0.53 / -0.28 | both halves | 3e-04 |  |
| [[COL5A1]] | -0.45 | -0.51 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 3, C 8.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SSTR2's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SLC35F1]] | B | SLC35F1 activity raises SSTR2's level | lines that do not express SLC35F1 (5) vs lines expressing it (45) | 1.69× lower at baseline in the lines without SLC35F1 | 0.082 | ⚠ within organs, on part of the lines; also absent: CFL2, CNN3, TPST1; maybe low, not absent |
| [[MIR155HG]] | B | MIR155HG activity raises SSTR2's level | lines that do not express MIR155HG (28) vs lines expressing it (22) | 1.47× lower at baseline in the lines without MIR155HG | 0.082 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA |
| [[COL5A1]] | C | COL5A1 activity raises SSTR2's level | lines that do not express COL5A1 (30) vs lines expressing it (20) | 2.50× lower at baseline in the lines without COL5A1 | 0.002 | ⚠ within organs, on part of the lines; also absent: DKK3, ITGA11, IL7R; co-absent with the target |
| [[TNFAIP6]] | C | TNFAIP6 activity raises SSTR2's level | lines that do not express TNFAIP6 (31) vs lines expressing it (19) | 1.85× lower at baseline in the lines without TNFAIP6 | 0.035 | ⚠ within organs, on part of the lines; also absent: GYPC, PLPP4, MAF; co-absent with the target |
| [[ADAMTS2]] | C | ADAMTS2 activity raises SSTR2's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 2.34× lower at baseline in the lines without ADAMTS2 | 0.040 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1; co-absent with the target |
| [[LOX]] | C | LOX activity raises SSTR2's level | lines that do not express LOX (31) vs lines expressing it (19) | 2.25× lower at baseline in the lines without LOX | 0.070 | ⚠ within organs, on part of the lines; also absent: C5orf46, RRAD, LINC01411; co-absent with the target |
| [[LINC02509]] | C | LINC02509 activity raises SSTR2's level | lines that do not express LINC02509 (35) vs lines expressing it (15) | 2.10× lower at baseline in the lines without LINC02509 | 0.078 | ⚠ within organs, on part of the lines; also absent: POSTN, ITGA11, IRAG2; co-absent with the target |
| [[NGFR]] | C | NGFR activity raises SSTR2's level | lines that do not express NGFR (19) vs lines expressing it (31) | 1.88× lower at baseline in the lines without NGFR | 0.084 | ⚠ within organs, on part of the lines; also absent: ZNF829, ZNF568, GNG11; co-absent with the target |
| [[ZNF439]] | C | ZNF439 activity raises SSTR2's level | lines that do not express ZNF439 (21) vs lines expressing it (29) | 1.78× lower at baseline in the lines without ZNF439 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000267383, PPP2R2B, CSF1R; co-absent with the target |
| [[SOX11]] | C | SOX11 activity raises SSTR2's level | lines that do not express SOX11 (37) vs lines expressing it (13) | 2.25× lower at baseline in the lines without SOX11 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: VCAM1, DPP10, RUNX1T1; co-absent with the target |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 7, C 11. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NINJ1]] | B | SSTR2 activity raises NINJ1's level | lines that do not express SSTR2 (25) vs lines expressing it (25) | 2.28× lower at baseline in the lines without SSTR2 | 0.006 | ⚠ within organs, on part of the lines; also absent: PPP2R2B, DKK3, ENSG00000260517 |
| [[DENND2A]] | B | SSTR2 activity raises DENND2A's level | lines that do not express SSTR2 (25) vs lines expressing it (25) | 3.12× lower at baseline in the lines without SSTR2 | 0.013 | ⚠ within organs, on part of the lines; also absent: PPP2R2B, DKK3, ENSG00000260517 |
| [[SLC2A6]] | B | SSTR2 activity raises SLC2A6's level | lines that do not express SSTR2 (25) vs lines expressing it (25) | 1.83× lower at baseline in the lines without SSTR2 | 0.027 | ⚠ within organs, on part of the lines; also absent: PPP2R2B, DKK3, ENSG00000260517 |
| [[TGFB1I1]] | B | SSTR2 activity raises TGFB1I1's level | lines that do not express SSTR2 (25) vs lines expressing it (25) | 2.07× lower at baseline in the lines without SSTR2 | 0.041 | ⚠ within organs, on part of the lines; also absent: PPP2R2B, DKK3, ENSG00000260517 |
| [[NKX3-1]] | B | SSTR2 activity strengthens NKX3-1's drug response | lines that do not express SSTR2 (15) vs lines expressing it (20) | the lines without SSTR2 respond 0.66× as strongly (z diff +2.09); strongest at Homoharringtonine 5 µM: 2.31x vs 7.88x (z diff +5.3) | 0.055 | ⚠ within organs, on part of the lines; also absent: PPP2R2B, DKK3, ENSG00000260517; target measured in part of the lines; artifact flags |
| [[CACNG2]] | B | SSTR2 activity raises CACNG2's level | lines that do not express SSTR2 (25) vs lines expressing it (25) | 1.83× lower at baseline in the lines without SSTR2 | 0.072 | ⚠ within organs, on part of the lines; also absent: PPP2R2B, DKK3, ENSG00000260517 |
| [[DYRK3]] | B | SSTR2 activity raises DYRK3's level | lines that do not express SSTR2 (25) vs lines expressing it (25) | 1.82× lower at baseline in the lines without SSTR2 | 0.087 | ⚠ within organs, on part of the lines; also absent: PPP2R2B, DKK3, ENSG00000260517 |
| [[COL5A1]] | C | SSTR2 activity raises COL5A1's level | lines that do not express SSTR2 (25) vs lines expressing it (25) | 6.54× lower at baseline in the lines without SSTR2 | 0.007 | ⚠ within organs, on part of the lines; also absent: PPP2R2B, DKK3, ENSG00000260517; co-absent with the target |
| [[ZNF439]] | C | SSTR2 activity raises ZNF439's level | lines that do not express SSTR2 (25) vs lines expressing it (25) | 3.69× lower at baseline in the lines without SSTR2 | 0.008 | ⚠ within organs, on part of the lines; also absent: PPP2R2B, DKK3, ENSG00000260517; co-absent with the target |
| [[LOX]] | C | SSTR2 activity raises LOX's level | lines that do not express SSTR2 (25) vs lines expressing it (25) | 7.03× lower at baseline in the lines without SSTR2 | 0.009 | ⚠ within organs, on part of the lines; also absent: PPP2R2B, DKK3, ENSG00000260517; co-absent with the target |
| [[TNFAIP6]] | C | SSTR2 activity raises TNFAIP6's level | lines that do not express SSTR2 (25) vs lines expressing it (25) | 2.27× lower at baseline in the lines without SSTR2 | 0.012 | ⚠ within organs, on part of the lines; also absent: PPP2R2B, DKK3, ENSG00000260517; co-absent with the target |
| [[C11orf96]] | C | SSTR2 activity raises C11orf96's level | lines that do not express SSTR2 (25) vs lines expressing it (25) | 2.28× lower at baseline in the lines without SSTR2 | 0.034 | ⚠ within organs, on part of the lines; also absent: PPP2R2B, DKK3, ENSG00000260517; co-absent with the target |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.586). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (33.5, 29.0); signed map (42.3, 13.6). **Vector** length 47.5, 14.3% of its response variance represented; |z| ≥ 3 in 468 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.8 | +13.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.2 | +7.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.6 | +16.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +2.4 | +11.3 |
|  | [[Harringtonine (drug)]] 5 µM |  | +2.3 | +7.0 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.2 |
|  | [[Amsacrine (drug)]] 5 µM |  | +0.9 | +2.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +0.9 | +2.2 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +0.9 | +2.4 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -1.4 | -1.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.3 | -1.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.3 | -2.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.2 | +0.0 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.0 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | somatostatin receptor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.1 — chr17:73,165,010-73,176,633 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Somatostatin receptors |
| Reactome | 6 pathways, smallest: Peptide ligand-binding receptors; Class A/1 (Rhodopsin-like receptors); G alpha (i) signalling events |
| Matched by | ensembl_id |

**Function**, from UniProt [P30874](https://www.uniprot.org/uniprotkb/P30874) (Somatostatin receptor type 2):

> Receptor for somatostatin-14 and -28. This receptor is coupled via pertussis toxin sensitive G proteins to inhibition of adenylyl cyclase. In addition it stimulates phosphotyrosine phosphatase and PLC via pertussis toxin insensitive as well as sensitive G proteins. Inhibits calcium entry by suppressing voltage-dependent calcium channels. Acts as the functionally dominant somatostatin receptor in pancreatic alpha- and beta-cells where it mediates the inhibitory effect of somatostatin-14 on …

**Summary**, from NCBI Gene [6752](https://www.ncbi.nlm.nih.gov/gene/6752):

> Somatostatin acts at many sites to inhibit the release of many hormones and other secretory proteins. The biologic effects of somatostatin are probably mediated by a family of G protein-coupled receptors that are expressed in a tissue-specific manner. SSTR2 is a member of the superfamily of receptors having seven transmembrane segments and is expressed in highest levels in cerebrum and kidney. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:11331](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11331) · Entrez [6752](https://www.ncbi.nlm.nih.gov/gene/6752) · UniProt [P30874](https://www.uniprot.org/uniprotkb/P30874) · Ensembl [ENSG00000180616](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000180616)

## Data

Gene col 11119: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11119); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11119, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11119]; `tensor/DDL_lfc|DDL_z.npy` [11119]; `embed/gene_vectors.npy` [11119]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11119 or target_col == 11119). Every well: [[SSTR2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SSTR2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
