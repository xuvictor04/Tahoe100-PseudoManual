---
symbol: "HLA-DRB1"
type: "gene"
col: 12134
ensembl_id: "ENSG00000196126"
name: "major histocompatibility complex, class II, DR beta 1"
location: "6p21.32"
module: 8
arm: "+"
pooled_cpm: 5.81
n_lines_expressing: 14
n_dd_up: 14
n_dd_down: 0
n_dd_up_clean: 5
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 18
direction_downstream: 26
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# HLA-DRB1

*major histocompatibility complex, class II, DR beta 1* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 6.61× (z +11.4, q 2e-27, up in 1 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 2.51× (z +8.2, q 4e-14, up in 8 of 11 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (CFPAC-1 0.236×, NCI-H2030 0.109×, C32 0.240×, SW1417 0.113×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H2030 0.113×, CFPAC-1 0.252×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HLA-DRA]] (+0.71, fdr 7e-06), [[WFDC2]] (+0.65, fdr 7e-06), [[LRG1]] (+0.64, fdr 8e-05); moves opposite to [[MCM3AP]] (-0.51, fdr 1e-04), [[INO80E]] (-0.48, fdr 1e-04), [[GTF2H3]] (-0.45, fdr 1e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 18 arrows point to it, the strongest [[HLA-DRA]] → it (grade C ⚠); 26 go from it, the strongest it → [[B2M]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 9 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12134.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **6.61×** | +11.4 | 2e-27 | 1/3 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.07×** | +11.4 | 2e-27 | 2/5 (C32, SW 900) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.51×** | +8.2 | 4e-14 | 8/11 (KATO III, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.73×** | +7.7 | 2e-12 | 1/3 (C32) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.35×** | +5.4 | 9e-06 | 8/10 (SW1417, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +4.5 | 6e-04 | 2/5 (NCI-H2030, CFPAC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.02×** | +4.4 | 8e-04 | 2/7 (SW 900, C32) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +4.3 | 0.001 | 1/10 (SW 900) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.82×** | +3.6 | 0.018 | 0/8 | top dose only | cell-cycle shift (explains ~15% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **2.93×** | +3.5 | 0.023 | 0/3 | top dose only | noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.051 | 0/11 | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~31% of this change | **1.67×** | +3.2 | 0.063 | 2/5 (KATO III, CFPAC-1) | inconsistent across doses | low cells (technical?) |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +3.1 | 0.072 | 1/8 (NCI-H2030) | top dose only |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.63×** | +3.1 | 0.085 | 1/11 (KATO III) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12134.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (CFPAC-1 0.236×, NCI-H2030 0.109×, C32 0.240×, SW1417 0.113×; ⚠ cell-cycle shift, explains ~0% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 2 lines (NCI-H2030 0.113×, CFPAC-1 0.252×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.559× | -3.4 | 0.36 | 3/11 (Panc 03.27, RPMI-7951, …) | inconsistent across doses |  |
| [[Pravastatin (sodium) (drug)]] 0.5 µM |  | 0.601× | -3.2 | 0.36 | 1/11 (A549) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.591× | -3.1 | 0.39 | 0/11 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12134. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 115 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -13.6) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.252× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 12.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.109× (z -13.3) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.113× (z -9.3) |
| [[C32 (line)]] | wt | 90.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -12.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 4.11 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -9.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.383 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.422 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.936 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 1.89 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 0.850 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.378 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.638 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.544 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 4.41 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.385 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.467 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.646 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.484 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.430 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.98 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.369 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 0.399 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.588 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.334 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.293 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.402 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.909 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.13 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.503 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 3.21 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.311 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.374 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.61 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.450 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.480 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.475 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.466 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 1.93 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.391 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.450 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.317 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12134), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 3 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HLA-DRA]] | +0.71 | +0.71 / +0.71 | both halves | 7e-06 | same gene group; pathway: Affinity selection of immunoglobulins; STRING 999 |
| [[WFDC2]] | +0.65 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[LRG1]] | +0.64 | +0.37 / +0.67 | both halves | 8e-05 |  |
| [[CD74]] | +0.63 | +0.65 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 995 |
| [[AGT]] | +0.61 | +0.44 / +0.55 | both halves | 3e-05 |  |
| [[SAA4]] | +0.60 | +0.41 / +0.63 | both halves | 4e-05 |  |
| [[LCN2]] | +0.59 | +0.41 / +0.60 | both halves | 4e-05 |  |
| [[LYPD5]] | +0.58 | +0.31 / +0.58 | both halves | 2e-04 |  |
| [[SLPI]] | +0.58 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[STEAP4]] | +0.57 | +0.39 / +0.59 | both halves | 5e-05 |  |
| [[FGA]] | +0.56 | +0.53 / +0.46 | both halves | 3e-05 |  |
| [[CARD14]] | +0.56 | +0.38 / +0.58 | both halves | 6e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM3AP]] | -0.51 | -0.33 / -0.57 | both halves | 1e-04 | pathway: Affinity selection of immunoglobulins |
| [[INO80E]] | -0.48 | -0.34 / -0.45 | both halves | 1e-04 |  |
| [[GTF2H3]] | -0.45 | -0.35 / -0.42 | both halves | 1e-04 |  |
| [[MTHFSD]] | -0.43 | -0.31 / -0.45 | both halves | 2e-04 |  |
| [[DNAJC11]] | -0.43 | -0.33 / -0.47 | both halves | 1e-04 |  |
| [[EXOSC6]] | -0.43 | -0.27 / -0.44 | both halves | 3e-04 | pathway: Affinity selection of immunoglobulins |
| [[DLG5]] | -0.43 | -0.35 / -0.47 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 0, C 18. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-DRA]] | C | HLA-DRA activity raises HLA-DRB1's level | lines that do not express HLA-DRA (39) vs lines expressing it (11) | 4.90× lower at baseline in the lines without HLA-DRA | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: HLA-DRB1, SOX10, ENSG00000287530; co-absent with the target |
| [[FGB]] | C | FGB activity raises HLA-DRB1's level | lines that do not express FGB (42) vs lines expressing it (8) | 3.32× lower at baseline in the lines without FGB | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGA, FGG, ITIH2; co-absent with the target |
| [[FGA]] | C | FGA activity raises HLA-DRB1's level | lines that do not express FGA (43) vs lines expressing it (7) | 3.87× lower at baseline in the lines without FGA | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, ITIH2, FGG; co-absent with the target |
| [[ITIH2]] | C | ITIH2 activity raises HLA-DRB1's level | lines that do not express ITIH2 (42) vs lines expressing it (8) | 2.57× lower at baseline in the lines without ITIH2 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: AFP, FGA, APOH; co-absent with the target |
| [[KRT23]] | C | KRT23 activity raises HLA-DRB1's level | lines that do not express KRT23 (40) vs lines expressing it (10) | 2.56× lower at baseline in the lines without KRT23 | 0.006 | ⚠ within organs, on part of the lines; also absent: PROM1, HSD17B2, GABRP; co-absent with the target |
| [[FGG]] | C | FGG activity raises HLA-DRB1's level | lines that do not express FGG (42) vs lines expressing it (8) | 2.73× lower at baseline in the lines without FGG | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGB, FGA, APOB; co-absent with the target |
| [[AGT]] | C | AGT activity raises HLA-DRB1's level | lines that do not express AGT (33) vs lines expressing it (17) | 1.54× lower at baseline in the lines without AGT | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: AMBP, RIT2, SOX11; co-absent with the target |
| [[STEAP4]] | C | STEAP4 activity raises HLA-DRB1's level | lines that do not express STEAP4 (38) vs lines expressing it (12) | 2.39× lower at baseline in the lines without STEAP4 | 0.018 | ⚠ within organs, on part of the lines; also absent: ADGRF1, WFDC2, SLC5A1; co-absent with the target |
| [[C3]] | C | C3 activity raises HLA-DRB1's level | lines that do not express C3 (32) vs lines expressing it (18) | 1.61× lower at baseline in the lines without C3 | 0.035 | ⚠ within organs, on part of the lines; also absent: TNFSF14, CP, CARD11; co-absent with the target |
| [[WFDC2]] | C | WFDC2 activity raises HLA-DRB1's level | lines that do not express WFDC2 (38) vs lines expressing it (12) | 2.37× lower at baseline in the lines without WFDC2 | 0.042 | ⚠ within organs, on part of the lines; also absent: STEAP4, CLIC5, ADGRF1; co-absent with the target |
| [[SMIM2-AS1]] | C | SMIM2-AS1 activity raises HLA-DRB1's level | lines that do not express SMIM2-AS1 (37) vs lines expressing it (13) | 2.62× lower at baseline in the lines without SMIM2-AS1 | 0.055 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ATP10B, CFTR, TRIM31; maybe low, not absent; co-absent with the target |
| [[RHEX]] | C | RHEX activity raises HLA-DRB1's level | lines that do not express RHEX (43) vs lines expressing it (7) | 1.99× lower at baseline in the lines without RHEX | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000286546, TIMD4, APOB; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 10, C 16. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[B2M]] | B | HLA-DRB1 activity raises B2M's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 1.92× lower at baseline in the lines without HLA-DRB1 | 0.003 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP |
| [[STAT3]] | B | HLA-DRB1 activity raises STAT3's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 1.37× lower at baseline in the lines without HLA-DRB1 | 0.016 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP |
| [[SAA4]] | B | HLA-DRB1 activity raises SAA4's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 1.67× lower at baseline in the lines without HLA-DRB1 | 0.016 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP |
| [[BCL2L15]] | B | HLA-DRB1 activity raises BCL2L15's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 1.86× lower at baseline in the lines without HLA-DRB1 | 0.017 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP |
| [[SAA2]] | B | HLA-DRB1 activity raises SAA2's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 2.25× lower at baseline in the lines without HLA-DRB1 | 0.021 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP |
| [[SAA2-SAA4]] | B | HLA-DRB1 activity raises SAA2-SAA4's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 1.87× lower at baseline in the lines without HLA-DRB1 | 0.029 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP |
| [[GTF2H3]] | B | HLA-DRB1 activity lowers GTF2H3's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 1.32× higher at baseline in the lines without HLA-DRB1 | 0.034 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP |
| [[CFB]] | B | HLA-DRB1 activity raises CFB's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 1.91× lower at baseline in the lines without HLA-DRB1 | 0.050 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP |
| [[PCOLCE]] | B | HLA-DRB1 activity raises PCOLCE's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 1.97× lower at baseline in the lines without HLA-DRB1 | 0.089 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP |
| [[CST3]] | B | HLA-DRB1 activity raises CST3's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 1.54× lower at baseline in the lines without HLA-DRB1 | 0.091 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP |
| [[HLA-DRA]] | C | HLA-DRB1 activity raises HLA-DRA's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 3.74× lower at baseline in the lines without HLA-DRB1 | 0.004 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP; co-absent with the target |
| [[KRT23]] | C | HLA-DRB1 activity raises KRT23's level | lines that do not express HLA-DRB1 (36) vs lines expressing it (14) | 2.46× lower at baseline in the lines without HLA-DRB1 | 0.007 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, FGA, GABRP; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.509). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.8, 54.9); signed map (61.4, -2.5). **Vector** length 22.1, 5.01% of its response variance represented; |z| ≥ 3 in 194 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +2.6 | +8.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.0 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +1.0 | +4.3 |
|  | [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | +0.8 | +3.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +0.7 | +1.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +0.7 | +0.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +0.7 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +0.6 | +1.0 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.2 | -2.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -1.0 | -2.1 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -0.8 | -2.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -0.8 | +1.3 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -0.7 | -0.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -0.5 | -1.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -0.5 | -0.6 |

## What is on record

|  |  |
|---|---|
| Name | major histocompatibility complex, class II, DR beta 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:32,577,902-32,589,848 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HLA-DR1B |
| Gene groups (HGNC) | Histocompatibility complex; C1-set domain containing |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Reactome | 15 pathways, smallest: Translocation of ZAP-70 to Immunological synapse; Phosphorylation of CD3 and TCR zeta chains; Generation of second messenger molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [P01911](https://www.uniprot.org/uniprotkb/P01911) (HLA class II histocompatibility antigen, DRB1 beta chain):

> A beta chain of antigen-presenting major histocompatibility complex class II (MHCII) molecule. In complex with the alpha chain HLA-DRA, displays antigenic peptides on professional antigen presenting cells (APCs) for recognition by alpha-beta T cell receptor (TCR) on HLA-DRB1-restricted CD4-positive T cells. This guides antigen-specific T-helper effector functions, both antibody-mediated immune response and macrophage activation, to ultimately eliminate the infectious agents and transformed …

**Summary**, from NCBI Gene [3123](https://www.ncbi.nlm.nih.gov/gene/3123):

> HLA-DRB1 belongs to the HLA class II beta chain paralogs. The class II molecule is a heterodimer consisting of an alpha (DRA) and a beta chain (DRB), both anchored in the membrane. It plays a central role in the immune system by presenting peptides derived from extracellular proteins. Class II molecules are expressed in antigen presenting cells. The beta chain is approximately 26-28 kDa. It is encoded by 6 exons. Exon one encodes the leader peptide; exons 2 and 3 encode the two extracellular …

**Accessions** — [HGNC:4948](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4948) · Entrez [3123](https://www.ncbi.nlm.nih.gov/gene/3123) · UniProt [P01911](https://www.uniprot.org/uniprotkb/P01911) · Ensembl [ENSG00000196126](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196126)

## Data

Gene col 12134: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12134); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12134, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12134]; `tensor/DDL_lfc|DDL_z.npy` [12134]; `embed/gene_vectors.npy` [12134]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12134 or target_col == 12134). Every well: [[HLA-DRB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HLA-DRB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
