---
symbol: "NRG3"
type: "gene"
col: 11725
ensembl_id: "ENSG00000185737"
name: "neuregulin 3"
location: "10q23.1"
module: 87
arm: "+"
pooled_cpm: 46.5
n_lines_expressing: 9
n_dd_up: 19
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 11
direction_downstream: 6
tags: ["gene", "module/087"]
generated_by: "tahoemap"
---

# NRG3

*neuregulin 3* — 10q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.83× (z +13.6, q 4e-39, up in 0 of 6 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 0.161×, HS-578T 0.125×; ⚠ cell-cycle shift, explains ~46% of this change); [[Chlorhexidine (diacetate) (drug)]] 5 µM in 1 line (NCI-H2122 0.486×); [[Raltitrexed (drug)]] 5 µM in 1 line (NCI-H2122 0.567×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.196×).
> Its strongest partners by |cos| (93 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAGEA10]] (+0.58, fdr 4e-05), [[MIR3681HG]] (+0.57, fdr 5e-05), [[FGF13]] (+0.57, fdr 2e-05); moves opposite to [[LRRC27]] (-0.41, fdr 3e-04).
> It is in [[Module 087]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[NELL1]] → it (grade B ⚠); 6 go from it, the strongest it → [[RNF17]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11725.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.83×** | +13.6 | 4e-39 | 0/6 | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.53×** | +12.1 | 3e-31 | 6/7 (NCI-H1573, A498, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.67×** | +12.0 | 7e-31 | 1/6 (NCI-H1573) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.63×** | +8.6 | 1e-15 | 0/5 | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.37×** | +7.9 | 2e-13 | 7/7 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.11×** | +6.4 | 2e-08 | 2/6 (BT-474, NCI-H1573) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.72×** | +4.8 | 1e-04 | 0/7 | top dose only | cell-cycle shift (explains ~5% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +4.5 | 4e-04 | 4/7 (CFPAC-1, NCI-H1573, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.63×** | +4.5 | 4e-04 | 0/6 | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.55×** | +4.0 | 0.003 | 5/7 (NCI-H1573, A498, …) | inconsistent across doses | cell-cycle shift (explains ~6% here); position effect removed |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.15×** | +3.7 | 0.012 | 2/6 (NCI-H1573, A498) | rises with dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.73×** | +3.6 | 0.014 | 0/6 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +3.6 | 0.014 | 0/7 | top dose only | cell-cycle shift (explains ~20% here) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.44×** | +3.4 | 0.029 | 0/7 | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | **1.66×** | +3.3 | 0.031 | 0/7 | inconsistent across doses | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.43×** | +3.3 | 0.035 | 1/6 (SK-MEL-2) | inconsistent across doses |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.40×** | +3.1 | 0.056 | 0/7 | inconsistent across doses | position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.57×** | +3.0 | 0.092 | 0/7 | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11725.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 4 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (SK-MEL-2 0.161×, HS-578T 0.125×; ⚠ cell-cycle shift, explains ~46% of this change); [[Chlorhexidine (diacetate) (drug)]] 5 µM in 1 line (NCI-H2122 0.486×); [[Raltitrexed (drug)]] 5 µM in 1 line (NCI-H2122 0.567×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (SK-MEL-2 0.196×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.881× | -3.9 | 0.051 | 0/7 | inconsistent across doses |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.785× | -3.1 | 0.51 | 4/7 (NCI-H1573, SK-MEL-2, …) | rises with dose | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, +0.11 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11725. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 15.6 | 7 (4 ⚠) | 0 | [[Tucidinostat (drug)]] 5 µM 23.1× (z +20.3) | — |
| [[SK-MEL-2 (line)]] | alt | 1,717 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -15.4) ⚠ cell-cycle shift, explains ~46% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.196× (z -13.7) |
| [[NCI-H2122 (line)]] | alt | 29.2 | 0 | 2 (1 ⚠) | — | [[Chlorhexidine (diacetate) (drug)]] 5 µM 0.486× (z -18.2) |
| [[A498 (line)]] | wt | 32.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.33× (z +9.3) | — |
| [[HS-578T (line)]] | alt | 53.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -12.3) ⚠ cell-cycle shift, explains ~46% of this change |
| [[A-172 (line)]] | wt | 5.49 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.43 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.15 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 8.43 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 4.48 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.37 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 4.08 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 387 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.24 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.44 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 4.43 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.37 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 4.65 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 10.6 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.44 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 5.22 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.41 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.71 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.34 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 4.11 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 5.76 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.05 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.53 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 4.30 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 4.98 n.m. | — | — | — | — |
| [[NCI-H23 (line)]] | alt | 5.30 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 3.52 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.22 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 52.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.51 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 4.47 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 4.38 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.62 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.97 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.36 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 5.10 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.10 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 5.35 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 4.87 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 4.07 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 5.07 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 4.67 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11725), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 7 of them with an alert (⚠; 7 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAGEA10]] | +0.58 | +0.52 / +0.42 | both halves | 4e-05 |  |
| [[MIR3681HG]] | +0.57 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[FGF13]] | +0.57 | +0.46 / +0.66 | both halves | 2e-05 | STRING 442 |
| [[COLEC12]] | +0.55 | +0.40 / +0.54 | both halves | 5e-05 |  |
| [[RNF17]] | +0.54 | +0.43 / +0.67 | both halves | 3e-05 |  |
| [[ITGB3]] | +0.53 | +0.42 / +0.50 | both halves | 4e-05 | pathway: MAPK family signaling cascades |
| [[LINC01812]] | +0.53 | +0.45 / +0.51 | both halves | 3e-05 |  |
| [[CCDC152]] | +0.53 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[COL19A1]] | +0.52 | +0.44 / +0.54 | both halves | 3e-05 |  |
| [[COX7B2]] | +0.52 | +0.46 / +0.53 | both halves | 3e-05 |  |
| [[AKAP6]] | +0.52 | +0.34 / +0.46 | both halves | 1e-04 |  |
| [[SETBP1]] | +0.51 | +0.37 / +0.54 | both halves | 7e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LRRC27]] | -0.41 | -0.28 / -0.43 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 1, C 10.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NELL1]] | B | NELL1 activity raises NRG3's level | lines that do not express NELL1 (19) vs lines expressing it (31) | 1.41× lower at baseline in the lines without NELL1 | 0.083 | ⚠ within organs, on part of the lines; also absent: ID4, RBM20, ENSG00000225096; maybe low, not absent |
| [[NAA11]] | C | NAA11 activity raises NRG3's level | lines that do not express NAA11 (39) vs lines expressing it (11) | 4.60× lower at baseline in the lines without NAA11 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CGA, RIT2, ADGRG7; maybe low, not absent; co-absent with the target |
| [[RNF17]] | C | RNF17 activity raises NRG3's level | lines that do not express RNF17 (42) vs lines expressing it (8) | 6.32× lower at baseline in the lines without RNF17 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SSX1, LINC00879, APOD; co-absent with the target |
| [[TSHZ2]] | C | TSHZ2 activity raises NRG3's level | lines that do not express TSHZ2 (29) vs lines expressing it (21) | 1.63× lower at baseline in the lines without TSHZ2 | 0.042 | ⚠ within organs, on part of the lines; also absent: RUNX1T1, PHYHIPL, F5; co-absent with the target |
| [[NTNG1]] | C | NTNG1 activity raises NRG3's level | lines that do not express NTNG1 (33) vs lines expressing it (17) | 3.24× lower at baseline in the lines without NTNG1 | 0.054 | ⚠ within organs, on part of the lines; also absent: ANKRD30A, FUT9, ACSS3; co-absent with the target |
| [[MSRB3-AS1]] | C | MSRB3-AS1 activity raises NRG3's level | lines that do not express MSRB3-AS1 (42) vs lines expressing it (8) | 2.70× lower at baseline in the lines without MSRB3-AS1 | 0.054 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: GCG, LINC01205, COX7B2; co-absent with the target |
| [[LINC00879]] | C | LINC00879 activity raises NRG3's level | lines that do not express LINC00879 (46) vs lines expressing it (4) | 14.85× lower at baseline in the lines without LINC00879 | 0.060 | ⚠ few lines (46 vs 4); within organs, on part of the lines; co-occurs with TP53; also absent: LINC02099, ENSG00000234426, APOB; co-absent with the target; its own permutation p |
| [[COX7B2]] | C | COX7B2 activity raises NRG3's level | lines that do not express COX7B2 (42) vs lines expressing it (8) | 2.53× lower at baseline in the lines without COX7B2 | 0.067 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000285751, GCG, LINC01205; co-absent with the target |
| [[LINC01098]] | C | LINC01098 activity raises NRG3's level | lines that do not express LINC01098 (36) vs lines expressing it (14) | 2.34× lower at baseline in the lines without LINC01098 | 0.072 | ⚠ within organs, on part of the lines; also absent: LINC02109, GREM1, ENSG00000288098; maybe low, not absent; co-absent with the target |
| [[LINC01205]] | C | LINC01205 activity raises NRG3's level | lines that do not express LINC01205 (44) vs lines expressing it (6) | 3.94× lower at baseline in the lines without LINC01205 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: GCG, ENSG00000241168, GPR15; maybe low, not absent; co-absent with the target |
| [[ANKRD20A8P]] | C | ANKRD20A8P activity raises NRG3's level | lines that do not express ANKRD20A8P (38) vs lines expressing it (12) | 2.43× lower at baseline in the lines without ANKRD20A8P | 0.095 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with TP53; also absent: ENSG00000291025, ENSG00000249174, TPTE; co-absent with the target |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 0, C 6.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RNF17]] | C | NRG3 activity raises RNF17's level | lines that do not express NRG3 (41) vs lines expressing it (9) | 3.16× lower at baseline in the lines without NRG3 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC00879, GPR141; co-absent with the target |
| [[NLGN4X]] | C | NRG3 activity raises NLGN4X's level | lines that do not express NRG3 (41) vs lines expressing it (9) | 4.98× lower at baseline in the lines without NRG3 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC00879, GPR141; co-absent with the target |
| [[CCDC152]] | C | NRG3 activity raises CCDC152's level | lines that do not express NRG3 (41) vs lines expressing it (9) | 2.00× lower at baseline in the lines without NRG3 | 0.047 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC00879, GPR141; co-absent with the target |
| [[ANKRD20A8P]] | C | NRG3 activity raises ANKRD20A8P's level | lines that do not express NRG3 (41) vs lines expressing it (9) | 1.92× lower at baseline in the lines without NRG3 | 0.064 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC00879, GPR141; co-absent with the target |
| [[LINGO2]] | C | NRG3 activity raises LINGO2's level | lines that do not express NRG3 (41) vs lines expressing it (9) | 4.64× lower at baseline in the lines without NRG3 | 0.069 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC00879, GPR141; co-absent with the target |
| [[LRAT]] | C | NRG3 activity raises LRAT's level | lines that do not express NRG3 (41) vs lines expressing it (9) | 4.09× lower at baseline in the lines without NRG3 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: S100A8, LINC00879, GPR141; co-absent with the target |

## Where it sits

- **Module**: [[Module 087]]; 51 genes; every member is in the + arm (projection on the module's main direction 0.557). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (46.0, 28.9); signed map (31.5, 37.1). **Vector** length 27.9, 10.1% of its response variance represented; |z| ≥ 3 in 174 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +12.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.0 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.0 | +12.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.8 | +7.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.4 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.5 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +2.8 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.8 | +1.3 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +0.8 | +3.6 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -0.9 | -2.1 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.7 | -1.9 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.7 | -2.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -0.7 | -2.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.7 | -1.9 |
|  | [[Pravastatin (sodium) (drug)]] 5 µM |  | -0.7 | -1.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -0.6 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | neuregulin 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q23.1 — chr10:81,875,194-82,987,179 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Neuregulins |
| Reactome | 27 pathways, smallest: PI3K events in ERBB4 signaling; ERBB2 Activates PTK6 Signaling; SHC1 events in ERBB4 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P56975](https://www.uniprot.org/uniprotkb/P56975) (Pro-neuregulin-3, membrane-bound isoform):

> Direct ligand for the ERBB4 tyrosine kinase receptor. Binding results in ligand-stimulated tyrosine phosphorylation and activation of the receptor. Does not bind to the EGF receptor, ERBB2 or ERBB3 receptors. May be a survival factor for oligodendrocytes.

**Summary**, from NCBI Gene [10718](https://www.ncbi.nlm.nih.gov/gene/10718):

> This gene is a member of the neuregulin gene family. This gene family encodes ligands for the transmembrane tyrosine kinase receptors ERBB3 and ERBB4 - members of the epidermal growth factor receptor family. Ligand binding activates intracellular signaling cascades and the induction of cellular responses including proliferation, migration, differentiation, and survival or apoptosis. This gene encodes neuregulin 3 (NRG3). NRG3 has been shown to activate the tyrosine phosphorylation of its …

**Accessions** — [HGNC:7999](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7999) · Entrez [10718](https://www.ncbi.nlm.nih.gov/gene/10718) · UniProt [P56975](https://www.uniprot.org/uniprotkb/P56975) · Ensembl [ENSG00000185737](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185737)

## Data

Gene col 11725: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11725); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11725, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11725]; `tensor/DDL_lfc|DDL_z.npy` [11725]; `embed/gene_vectors.npy` [11725]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11725 or target_col == 11725). Every well: [[NRG3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NRG3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
