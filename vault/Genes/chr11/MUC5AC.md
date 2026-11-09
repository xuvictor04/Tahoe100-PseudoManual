---
symbol: "MUC5AC"
type: "gene"
col: 13250
ensembl_id: "ENSG00000215182"
name: "mucin 5AC, oligomeric mucus/gel-forming"
location: "11p15.5"
module: 155
arm: "+"
pooled_cpm: 15.28
n_lines_expressing: 11
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 25
direction_downstream: 39
tags: ["gene", "module/155"]
generated_by: "tahoemap"
---

# MUC5AC

*mucin 5AC, oligomeric mucus/gel-forming* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.48× (z +10.6, q 1e-23, up in 7 of 9 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 5.58× (z +8.6, q 1e-15, up in 2 of 9 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 0.0620×; ⚠ cell-cycle shift, explains ~32% of this change); [[Neratinib (drug)]] 0.5 µM in 1 line (BT-474 0.0144×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LS 180 0.0761×; ⚠ cell-cycle shift, explains ~31% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MUC2]] (+0.79, fdr 7e-06, ⚠ same locus), [[LINC01440]] (+0.68, fdr 7e-06), [[CEACAM5]] (+0.66, fdr 7e-06), [[CAPN8]] (+0.66, fdr 7e-06); moves opposite to [[LMO3]] (-0.45, fdr 2e-04), [[PGR]] (-0.42, fdr 6e-05), [[PRLR]] (-0.39, fdr 1e-04).
> It is in [[Module 155]], a single-armed module (MyD88 deficiency (TLR2/4)).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[AQP3]] → it (grade B ⚠); 39 go from it, the strongest it → [[AQP3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13250.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **4.48×** | +10.6 | 1e-23 | 7/9 (CFPAC-1, HepG2/C3A, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **7.10×** | +9.8 | 3e-20 | 4/7 (HT-29, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **7.27×** | +9.6 | 2e-19 | 3/7 (HT-29, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **5.58×** | +8.6 | 1e-15 | 2/9 (Panc 03.27, CFPAC-1) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.80×** | +7.3 | 4e-11 | 5/7 (HT-29, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **3.20×** | +5.6 | 2e-06 | 6/9 (A549, HepG2/C3A, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.55×** | +4.7 | 2e-04 | 1/9 (KATO III) | top dose only |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **3.33×** | +4.3 | 0.001 | 0/7 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **2.28×** | +4.1 | 0.002 | 5/9 (HepG2/C3A, A549, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.75×** | +4.0 | 0.004 | 1/9 (Panc 03.27) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.65×** | +3.6 | 0.018 | 3/9 (BT-474, Hs 766T, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +3.5 | 0.020 | 1/8 (Hs 766T) | top dose only | cell-cycle shift (explains ~21% here); position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **2.41×** | +3.1 | 0.073 | 2/9 (Hs 766T, LS 180) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cyclosporin A (drug)]] 0.5 µM |  | **1.85×** | +3.1 | 0.086 | 5/9 (A549, HT-29, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13250.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 1 line (LS 180 0.0620×; ⚠ cell-cycle shift, explains ~32% of this change); [[Neratinib (drug)]] 0.5 µM in 1 line (BT-474 0.0144×); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (LS 180 0.0761×; ⚠ cell-cycle shift, explains ~31% of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Encorafenib (drug)]] 5 µM |  | 0.317× | -3.0 | 0.42 | 1/9 (BT-474) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.22 per unit of S-phase module lfc, +0.75 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13250. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 39.6 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.68× (z +9.2) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[BT-474 (line)]] | alt | 27.5 | 0 | 2 (1 ⚠) | — | [[Neratinib (drug)]] 0.5 µM 0.0144× (z -10.6) |
| [[LS 180 (line)]] | wt | 270 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0620× (z -14.4) ⚠ cell-cycle shift, explains ~32% of this change |
| [[CFPAC-1 (line)]] | alt | 71.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 26.0× (z +16.9) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[HepG2_C3A (line)]] | wt | 3.84 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 109× (z +10.9) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[Hs 766T (line)]] | wt | 88.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 8.92× (z +10.4) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[Panc 03.27 (line)]] | alt | 4.37 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 18.5× (z +9.6) ⚠ cell-cycle shift, explains ~32% of this change | — |
| [[A-172 (line)]] | wt | 0.623 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.634 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.539 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.48 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 1.35 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.719 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.561 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 1.05 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 0.661 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.775 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.654 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.981 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.799 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.638 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 102 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.941 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.539 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.880 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.512 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.21 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.621 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.563 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.965 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.979 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.19 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.640 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.701 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.521 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.779 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.822 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.896 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.74 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 0.711 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.817 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.756 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.907 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.907 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13250), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MUC2]] | +0.79 | +0.74 / +0.77 | both halves | 7e-06 | same gene group; pathway: C-type lectin receptors (CLRs); STRING 909; ⚠ same locus (47.4 kb, same strand: neighbours can correlate without regulation) |
| [[LINC01440]] | +0.68 | +0.72 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[CEACAM5]] | +0.66 | +0.58 / +0.60 | both halves | 7e-06 | STRING 630 |
| [[CAPN8]] | +0.66 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[CES1]] | +0.64 | +0.61 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[S100A8]] | +0.62 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[SPTSSB]] | +0.61 | +0.61 / +0.66 | both halves | 7e-06 | **novel candidate** |
| [[CEACAM6]] | +0.61 | +0.51 / +0.59 | both halves | 1e-05 | STRING 534 |
| [[MUC5B]] | +0.56 | +0.52 / +0.44 | both halves | 3e-05 | same gene group; pathway: C-type lectin receptors (CLRs); STRING 988; ⚠ same locus (21.9 kb, same strand: neighbours can correlate without regulation) |
| [[TSPAN1]] | +0.56 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[SMIM31]] | +0.56 | +0.49 / +0.54 | both halves | 1e-05 |  |
| [[AQP3]] | +0.54 | +0.49 / +0.58 | both halves | 2e-05 |  |
| [[KRT18]] | +0.54 | +0.48 / +0.46 | both halves | 3e-05 | STRING 442 |
| [[SAMD5]] | +0.54 | +0.56 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LMO3]] | -0.45 | -0.50 / -0.30 | both halves | 2e-04 |  |
| [[PGR]] | -0.42 | -0.39 / -0.45 | both halves | 6e-05 |  |
| [[PRLR]] | -0.39 | -0.43 / -0.34 | both halves | 1e-04 |  |
| [[ZNF552]] | -0.38 | -0.45 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 2, C 23. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AQP3]] | B | AQP3 activity raises MUC5AC's level | lines that do not express AQP3 (19) vs lines expressing it (31) | 3.02× lower at baseline in the lines without AQP3 | 0.049 | ⚠ within organs, on part of the lines; also absent: ABCC3, ELF3, CD24; maybe low, not absent |
| [[ABCC3]] | B | ABCC3 activity raises MUC5AC's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 2.78× lower at baseline in the lines without ABCC3 | 0.075 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[MUC2]] | C | MUC2 activity raises MUC5AC's level | lines that do not express MUC2 (42) vs lines expressing it (8) | 11.75× lower at baseline in the lines without MUC2 | 0.002 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000230975, ENSG00000248588, DSG4; co-absent with the target |
| [[MUC5B]] | C | MUC5B activity raises MUC5AC's level | lines that do not express MUC5B (37) vs lines expressing it (13) | 7.15× lower at baseline in the lines without MUC5B | 0.003 | ⚠ within organs, on part of the lines; also absent: DAPP1, AGR3, ENSG00000259925; co-absent with the target |
| [[P2RY2]] | C | P2RY2 activity raises MUC5AC's level | lines that do not express P2RY2 (27) vs lines expressing it (23) | 4.03× lower at baseline in the lines without P2RY2 | 0.006 | ⚠ within organs, on part of the lines; also absent: C6orf132, FAM83B, RNF223; co-absent with the target |
| [[PI3]] | C | PI3 activity raises MUC5AC's level | lines that do not express PI3 (27) vs lines expressing it (23) | 3.14× lower at baseline in the lines without PI3 | 0.008 | ⚠ within organs, on part of the lines; also absent: IL33, LINC01133, IL1A; co-absent with the target |
| [[ST6GALNAC1]] | C | ST6GALNAC1 activity raises MUC5AC's level | lines that do not express ST6GALNAC1 (37) vs lines expressing it (13) | 6.69× lower at baseline in the lines without ST6GALNAC1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, SLC44A4, STEAP4; co-absent with the target |
| [[TFF1]] | C | TFF1 activity raises MUC5AC's level | lines that do not express TFF1 (31) vs lines expressing it (19) | 5.62× lower at baseline in the lines without TFF1 | 0.008 | ⚠ within organs, on part of the lines; also absent: TOX3, CEACAM5, MUC5AC; co-absent with the target |
| [[CEACAM6]] | C | CEACAM6 activity raises MUC5AC's level | lines that do not express CEACAM6 (37) vs lines expressing it (13) | 7.42× lower at baseline in the lines without CEACAM6 | 0.009 | ⚠ within organs, on part of the lines; also absent: DAPP1, TMPRSS2, CDH17; co-absent with the target |
| [[C2CD4A]] | C | C2CD4A activity raises MUC5AC's level | lines that do not express C2CD4A (38) vs lines expressing it (12) | 5.91× lower at baseline in the lines without C2CD4A | 0.012 | ⚠ within organs, on part of the lines; also absent: CEACAM5, AGR3, PRR15L; co-absent with the target |
| [[SERPINB4]] | C | SERPINB4 activity raises MUC5AC's level | lines that do not express SERPINB4 (39) vs lines expressing it (11) | 4.03× lower at baseline in the lines without SERPINB4 | 0.019 | ⚠ within organs, on part of the lines; also absent: SERPINB3, GABRP, S100A9; co-absent with the target |
| [[GSDMC]] | C | GSDMC activity raises MUC5AC's level | lines that do not express GSDMC (42) vs lines expressing it (8) | 5.17× lower at baseline in the lines without GSDMC | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, S100A9, DAPP1; co-absent with the target |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 12, C 27. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AQP3]] | B | MUC5AC activity raises AQP3's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 3.86× lower at baseline in the lines without MUC5AC | 8e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3 |
| [[ABCC3]] | B | MUC5AC activity raises ABCC3's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 4.10× lower at baseline in the lines without MUC5AC | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3 |
| [[TNFRSF21]] | B | MUC5AC activity raises TNFRSF21's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 4.10× lower at baseline in the lines without MUC5AC | 0.031 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3 |
| [[ADAP1]] | B | MUC5AC activity raises ADAP1's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 2.06× lower at baseline in the lines without MUC5AC | 0.036 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3 |
| [[KRT8]] | B | MUC5AC activity raises KRT8's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 3.49× lower at baseline in the lines without MUC5AC | 0.042 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3 |
| [[KRT18]] | B | MUC5AC activity raises KRT18's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 3.57× lower at baseline in the lines without MUC5AC | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3 |
| [[TMEM184A]] | B | MUC5AC activity raises TMEM184A's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 2.25× lower at baseline in the lines without MUC5AC | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3 |
| [[CYP2S1]] | B | MUC5AC activity raises CYP2S1's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 3.42× lower at baseline in the lines without MUC5AC | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3 |
| [[EPHA2]] | B | MUC5AC activity raises EPHA2's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 2.51× lower at baseline in the lines without MUC5AC | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3 |
| [[AGRN]] | B | MUC5AC activity raises AGRN's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 1.48× lower at baseline in the lines without MUC5AC | 0.079 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3 |
| [[CEMIP]] | B | MUC5AC activity raises CEMIP's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 3.92× lower at baseline in the lines without MUC5AC | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3 |
| [[LINC01503]] | B | MUC5AC activity raises LINC01503's level | lines that do not express MUC5AC (39) vs lines expressing it (11) | 2.65× lower at baseline in the lines without MUC5AC | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SLC6A14, GABRP, AGR3 |

## Where it sits

- **Module**: [[Module 155]] — MyD88 deficiency (TLR2/4); 29 genes; every member is in the + arm (projection on the module's main direction 0.617). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.6, 48.9); signed map (55.7, 23.0). **Vector** length 37.3, 15.2% of its response variance represented; |z| ≥ 3 in 194 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Antimicrobial peptides* (reactome, mean cos +0.51 to 3).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.3 | +9.6 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +2.8 | +10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.7 | +9.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.5 | +7.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~33% of this change | +2.1 | +5.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.8 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.0 | +2.2 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +0.9 | +2.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +0.8 | +8.6 |
| fall | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.0 | -0.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -0.9 | -0.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.8 | -1.9 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.8 | +0.3 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -0.8 | -0.8 |
|  | [[EX229 (drug)]] 5 µM |  | -0.7 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | mucin 5AC, oligomeric mucus/gel-forming |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:1,157,953-1,201,138 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MUC5 |
| Gene groups (HGNC) | Mucins |
| Reactome | 12 pathways, smallest: Defective GALNT12 causes CRCS1; Defective GALNT3 causes HFTC; Defective C1GALT1C1 causes TNPS |
| Matched by | ensembl_id |

**Function**, from UniProt [P98088](https://www.uniprot.org/uniprotkb/P98088) (Mucin-5AC):

> Gel-forming glycoprotein of gastric and respiratory tract epithelia that protects the mucosa from infection and chemical damage by binding to inhaled microorganisms and particles that are subsequently removed by the mucociliary system. Interacts with H.pylori in the gastric epithelium, Barrett's esophagus as well as in gastric metaplasia of the duodenum (GMD).

**Summary**, from NCBI Gene [4586](https://www.ncbi.nlm.nih.gov/gene/4586):

> Predicted to be an extracellular matrix structural constituent. Predicted to act upstream of or within maintenance of lens transparency. Located in mucus layer and obsolete extracellular space. Implicated in dry eye syndrome. Biomarker of several diseases, including Sjogren's syndrome; biliary tract disease (multiple); cystic fibrosis; eye disease (multiple); and pancreatic cancer (multiple). [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:7515](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7515) · Entrez [4586](https://www.ncbi.nlm.nih.gov/gene/4586) · UniProt [P98088](https://www.uniprot.org/uniprotkb/P98088) · Ensembl [ENSG00000215182](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215182)

## Data

Gene col 13250: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13250); `tables/drug_effects.parquet` (15 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13250, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13250]; `tensor/DDL_lfc|DDL_z.npy` [13250]; `embed/gene_vectors.npy` [13250]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13250 or target_col == 13250). Every well: [[MUC5AC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MUC5AC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
