---
symbol: "GUCY1A1"
type: "gene"
col: 8873
ensembl_id: "ENSG00000164116"
name: "guanylate cyclase 1 soluble subunit alpha 1"
location: "4q32.1"
module: 9
arm: "+"
pooled_cpm: 3.62
n_lines_expressing: 20
n_dd_up: 31
n_dd_down: 0
n_dd_up_clean: 20
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 7
direction_downstream: 8
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# GUCY1A1

*guanylate cyclase 1 soluble subunit alpha 1* — 4q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.26× (z +15.8, q 0e+00, up in 10 of 14 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 4 lines (Hs 766T 0.131×, A498 0.245×, BT-474 0.0978×, SHP-77 0.151×; ⚠ cell-cycle shift, explains ~31% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (Hs 766T 0.101×, A498 0.270×; ⚠ cell-cycle shift, explains ~9% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.164×; ⚠ toxic; transcription drop).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPOCK3]] (+0.63, fdr 1e-05), [[UNC80]] (+0.58, fdr 2e-05), [[MIR325HG]] (+0.57, fdr 2e-05); moves opposite to [[ERRFI1]] (-0.48, fdr 1e-04), [[SEPTIN10]] (-0.47, fdr 1e-04), [[NT5E]] (-0.44, fdr 4e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[LURAP1]] → it (grade B ⚠); 8 go from it, the strongest it → [[PTPN13]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8873.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.26×** | +15.8 | 0e+00 | 10/14 (HEC-1-A, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.32×** | +14.2 | 1e-43 | 3/8 (NCI-H1792, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.78×** | +9.9 | 1e-20 | 1/4 (CFPAC-1) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.92×** | +9.7 | 3e-20 | 2/5 (CFPAC-1, Hs 766T) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.36×** | +9.3 | 1e-18 | 9/17 (NCI-H1792, NCI-H1573, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.73×** | +5.9 | 3e-07 | 2/13 (J82, NCI-H460) | rises with dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.00×** | +5.3 | 8e-06 | 4/16 (A-427, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.99×** | +5.1 | 3e-05 | 4/10 (NCI-H1792, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.83×** | +4.7 | 2e-04 | 3/13 (J82, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.84×** | +4.5 | 4e-04 | 6/14 (Hs 766T, A498, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +4.4 | 5e-04 | 1/11 (LS 180) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **2.77×** | +4.1 | 0.002 | 0/6 | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.70×** | +3.9 | 0.004 | 7/14 (Hs 766T, A498, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.03×** | +3.9 | 0.004 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.68×** | +3.8 | 0.005 | 5/12 (NCI-H1573, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.64×** | +3.8 | 0.005 | 1/12 (BT-474) | inconsistent across doses | low cells (technical?) |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +3.5 | 0.015 | 0/17 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.53×** | +3.3 | 0.030 | 1/14 (SHP-77) | inconsistent across doses | low cells (technical?) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.52×** | +3.2 | 0.034 | 0/16 | inconsistent across doses |  |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM |  | **1.54×** | +3.1 | 0.050 | 0/11 | inconsistent across doses |  |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.48×** | +3.0 | 0.064 | 1/14 (NCI-H1573) | inconsistent across doses |  |
| [[Arbutin (drug)]] 5 µM |  | **1.50×** | +3.0 | 0.065 | 1/15 (BT-474) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 8873.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Panobinostat (drug)]] 0.5 µM in 4 lines (Hs 766T 0.131×, A498 0.245×, BT-474 0.0978×, SHP-77 0.151×; ⚠ cell-cycle shift, explains ~31% of this change); [[Panobinostat (drug)]] 5 µM in 2 lines (Hs 766T 0.101×, A498 0.270×; ⚠ cell-cycle shift, explains ~9% of this change); [[Dinaciclib (drug)]] 0.5 µM in 1 line (SHP-77 0.164×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Lucanthone (drug)]] 0.05 µM |  | 0.660× | -3.0 | 0.81 | 0/17 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8873. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[Hs 766T (line)]] | wt | 35.6 | 1 | 2 (2 ⚠) | [[Trametinib (drug)]] 0.05 µM 3.35× (z +8.6) | [[Panobinostat (drug)]] 5 µM 0.101× (z -11.9) ⚠ cell-cycle shift, explains ~9% of this change |
| [[A498 (line)]] | wt | 20.4 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.245× (z -9.5) ⚠ cell-cycle shift, explains ~31% of this change |
| [[SHP-77 (line)]] | alt | 15.9 | 0 | 2 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.151× (z -8.9) ⚠ cell-cycle shift, explains ~31% of this change |
| [[BT-474 (line)]] | alt | 33.5 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0978× (z -9.2) ⚠ cell-cycle shift, explains ~31% of this change |
| [[HEC-1-A (line)]] | alt | 5.54 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.85× (z +11.8) | — |
| [[NCI-H1792 (line)]] | alt | 3.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.63× (z +8.9) | — |
| [[A-172 (line)]] | wt | 1.04 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 0.354 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.627 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.382 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.435 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.397 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 0.436 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.389 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.432 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.542 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.495 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.461 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.986 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.339 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.07 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.417 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.73 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.303 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.385 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 4.40 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.580 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.973 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.891 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 0.482 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.361 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.348 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.561 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.584 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.416 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.07 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.423 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.783 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.481 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.447 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.358 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8873), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPOCK3]] | +0.63 | +0.63 / +0.55 | both halves | 1e-05 | **novel candidate** |
| [[UNC80]] | +0.58 | +0.55 / +0.47 | both halves | 2e-05 |  |
| [[MIR325HG]] | +0.57 | +0.54 / +0.47 | both halves | 2e-05 |  |
| [[DGKB]] | +0.57 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[TSPAN12]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[LRIG3]] | +0.55 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[SIM1]] | +0.55 | +0.48 / +0.49 | both halves | 2e-05 |  |
| [[LINC01503]] | +0.54 | +0.55 / +0.48 | both halves | 2e-05 |  |
| [[SLC4A4]] | +0.54 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[RARRES1]] | +0.54 | +0.53 / +0.51 | both halves | 1e-05 |  |
| [[LINC02466]] | +0.54 | +0.40 / +0.48 | both halves | 5e-05 |  |
| [[MAPK10]] | +0.54 | +0.57 / +0.45 | both halves | 3e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ERRFI1]] | -0.48 | -0.49 / -0.33 | both halves | 1e-04 |  |
| [[SEPTIN10]] | -0.47 | -0.48 / -0.33 | both halves | 1e-04 |  |
| [[NT5E]] | -0.44 | -0.45 / -0.41 | both halves | 4e-05 |  |
| [[HIF1AN]] | -0.44 | -0.31 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 1, C 6.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LURAP1]] | B | LURAP1 activity raises GUCY1A1's level | lines that do not express LURAP1 (13) vs lines expressing it (37) | 1.38× lower at baseline in the lines without LURAP1 | 0.051 | ⚠ within organs, on part of the lines; also absent: ZG16B; maybe low, not absent |
| [[LINC02438]] | C | LINC02438 activity raises GUCY1A1's level | lines that do not express LINC02438 (36) vs lines expressing it (14) | 1.19× lower at baseline in the lines without LINC02438 | 0.016 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000248515, MSR1, FSTL5; co-absent with the target |
| [[SPINK5]] | C | SPINK5 activity raises GUCY1A1's level | lines that do not express SPINK5 (35) vs lines expressing it (15) | 1.50× lower at baseline in the lines without SPINK5 | 0.021 | ⚠ within organs, on part of the lines; also absent: TFF2, ST6GALNAC1, ENSG00000248588; co-absent with the target |
| [[CDH8]] | C | CDH8 activity raises GUCY1A1's level | lines that do not express CDH8 (28) vs lines expressing it (22) | 1.84× lower at baseline in the lines without CDH8 | 0.052 | ⚠ within organs, on part of the lines; also absent: ZIC1, IGFBP5, PCDH18; maybe low, not absent; co-absent with the target |
| [[DACH1]] | C | DACH1 activity raises GUCY1A1's level | lines that do not express DACH1 (30) vs lines expressing it (20) | 1.73× lower at baseline in the lines without DACH1 | 0.072 | ⚠ within organs, on part of the lines; also absent: FGF20, CSMD3, XKR7; co-absent with the target |
| [[AK4P3]] | C | AK4P3 activity raises GUCY1A1's level | lines that do not express AK4P3 (36) vs lines expressing it (14) | 1.56× lower at baseline in the lines without AK4P3 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: APOA1, ENSG00000232252, TF; co-absent with the target |
| [[KCTD8]] | C | KCTD8 activity raises GUCY1A1's level | lines that do not express KCTD8 (30) vs lines expressing it (20) | 2.20× lower at baseline in the lines without KCTD8 | 0.091 | ⚠ within organs, on part of the lines; also absent: NOL4, DSCAM, IQCA1; co-absent with the target |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 4, C 4.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PTPN13]] | B | GUCY1A1 activity raises PTPN13's level | lines that do not express GUCY1A1 (30) vs lines expressing it (20) | 2.46× lower at baseline in the lines without GUCY1A1 | 0.035 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, TLL1, LINC03046 |
| [[LRIG3]] | B | GUCY1A1 activity raises LRIG3's level | lines that do not express GUCY1A1 (30) vs lines expressing it (20) | 1.89× lower at baseline in the lines without GUCY1A1 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, TLL1, LINC03046 |
| [[MAPK10]] | B | GUCY1A1 activity raises MAPK10's level | lines that do not express GUCY1A1 (30) vs lines expressing it (20) | 2.54× lower at baseline in the lines without GUCY1A1 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, TLL1, LINC03046 |
| [[LINC00578]] | B | GUCY1A1 activity raises LINC00578's level | lines that do not express GUCY1A1 (30) vs lines expressing it (20) | 1.42× lower at baseline in the lines without GUCY1A1 | 0.089 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, TLL1, LINC03046 |
| [[CACNB2]] | C | GUCY1A1 activity raises CACNB2's level | lines that do not express GUCY1A1 (30) vs lines expressing it (20) | 2.34× lower at baseline in the lines without GUCY1A1 | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, TLL1, LINC03046; co-absent with the target |
| [[TLL1]] | C | GUCY1A1 activity raises TLL1's level | lines that do not express GUCY1A1 (30) vs lines expressing it (20) | 2.41× lower at baseline in the lines without GUCY1A1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, TLL1, LINC03046; co-absent with the target |
| [[CCDC85A]] | C | GUCY1A1 activity raises CCDC85A's level | lines that do not express GUCY1A1 (30) vs lines expressing it (20) | 2.69× lower at baseline in the lines without GUCY1A1 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, TLL1, LINC03046; co-absent with the target |
| [[SPINK5]] | C | GUCY1A1 activity raises SPINK5's level | lines that do not express GUCY1A1 (30) vs lines expressing it (20) | 1.85× lower at baseline in the lines without GUCY1A1 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, TLL1, LINC03046; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.557). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (33.3, 39.7); signed map (47.4, 31.4). **Vector** length 39.8, 9.03% of its response variance represented; |z| ≥ 3 in 420 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +15.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.0 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.6 | +14.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +2.7 | +5.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +9.3 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.1 | +3.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +2.6 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.7 | +2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.6 | +4.5 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -1.4 | -0.4 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.3 | -0.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.2 | -1.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~9% of this change | -1.2 | -1.1 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -1.2 | -1.1 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.1 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -0.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.0 | -0.2 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | guanylate cyclase 1 soluble subunit alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q32.1 — chr4:155,666,726-155,737,059 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GC-SA3; previously GUC1A3, GUCY1A3 |
| Gene groups (HGNC) | Soluble guanylate cyclases |
| Hallmark sets | ANDROGEN_RESPONSE, KRAS_SIGNALING_UP |
| Reactome | 5 pathways, smallest: Nitric oxide stimulates guanylate cyclase; Smooth Muscle Contraction; Platelet homeostasis |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02108](https://www.uniprot.org/uniprotkb/Q02108) (Guanylate cyclase soluble subunit alpha-1):

> Alpha subunit of soluble guanylate cyclase (sGC), a key enzyme in nitric oxide (NO) signaling. sGC functions as a heterodimer consisting of one alpha and one beta subunit. It serves as the primary intracellular receptor for NO, which binds to a heme prosthetic group located on the beta subunit. Upon NO binding, sGC catalyzes the conversion of GTP into cyclic GMP (cGMP), thereby transmitting the NO signal into an ubiquitous intracellular second messenger.

**Summary**, from NCBI Gene [2982](https://www.ncbi.nlm.nih.gov/gene/2982):

> Soluble guanylate cyclases are heterodimeric proteins that catalyze the conversion of GTP to 3',5'-cyclic GMP and pyrophosphate. The protein encoded by this gene is an alpha subunit of this complex and it interacts with a beta subunit to form the guanylate cyclase enzyme, which is activated by nitric oxide. Several transcript variants encoding a few different isoforms have been found for this gene. [provided by RefSeq, Jan 2012]

**Accessions** — [HGNC:4685](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4685) · Entrez [2982](https://www.ncbi.nlm.nih.gov/gene/2982) · UniProt [Q02108](https://www.uniprot.org/uniprotkb/Q02108) · Ensembl [ENSG00000164116](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164116)

## Data

Gene col 8873: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8873); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8873, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8873]; `tensor/DDL_lfc|DDL_z.npy` [8873]; `embed/gene_vectors.npy` [8873]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8873 or target_col == 8873). Every well: [[GUCY1A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GUCY1A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
