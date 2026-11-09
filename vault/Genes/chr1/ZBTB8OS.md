---
symbol: "ZBTB8OS"
type: "gene"
col: 10702
ensembl_id: "ENSG00000176261"
name: "tRNA splicing ligase complex subunit 1"
location: "1p35.1"
module: 114
arm: "+"
pooled_cpm: 45.17
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 2
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/114"]
generated_by: "tahoemap"
---

# ZBTB8OS

*tRNA splicing ligase complex subunit 1* — 1p35.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.78× (z +14.6, q 1e-45, up in 39 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.789× (z -4.2, q 0.019, down in 21 of 47 measured lines) ⚠ toxic; cell-cycle shift, explains ~13% of this change. The strongest without an alert is [[Filgotinib (drug)]] 5 µM: 0.811× (z -3.8, q 0.037, down in 16 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RKO 0.211×, C32 0.194×, C-33 A 0.195×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 0.223×, LS 180 0.250×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (C32 0.111×; ⚠ toxic).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[URM1]] (+0.73, fdr 1e-05), [[ZNF529-AS1]] (+0.73, fdr 7e-06), [[ZNF785]] (+0.71, fdr 7e-06); moves opposite to [[THEM6]] (-0.60, fdr 2e-04), [[SSX2IP]] (-0.59, fdr 3e-05), [[CDCA7L]] (-0.58, fdr 1e-04).
> It is in [[Module 114]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10702.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.78×** | +14.6 | 1e-45 | 39/47 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.04×** | +12.8 | 4e-35 | 45/48 (SW480, NCI-H460, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.55×** | +11.0 | 6e-26 | 37/47 (NCI-H460, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.74×** | +9.9 | 6e-21 | 40/48 (LoVo, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +9.2 | 5e-18 | 39/48 (NCI-H460, HS-578T, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.65×** | +9.0 | 2e-17 | 39/48 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.46×** | +6.8 | 1e-09 | 33/47 (A-427, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +6.7 | 1e-09 | 33/48 (NCI-H460, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.47×** | +6.6 | 2e-09 | 32/47 (CFPAC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.51×** | +6.6 | 3e-09 | 39/48 (PANC-1, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +6.2 | 3e-08 | 34/48 (A-427, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.40×** | +6.0 | 1e-07 | 35/48 (NCI-H23, A-427, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.24×** | +5.5 | 2e-06 | 25/48 (Panc 03.27, J82, …) | rises with dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.23×** | +5.2 | 7e-06 | 24/48 (SW1417, SNU-1, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.31×** | +4.3 | 8e-04 | 22/48 (A-427, BT-474, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **1.55×** | +4.1 | 0.001 | 19/49 (HEC-1-A, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.28×** | +3.9 | 0.004 | 22/48 (NCI-H23, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.34×** | +3.7 | 0.006 | 17/48 (HCT15, RPMI-7951, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Triamcinolone (drug)]] 5 µM |  | 1.15× | +3.5 | 0.011 | 12/48 (SW1417, HOP62, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10702.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 4 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.05 µM in 3 lines (RKO 0.211×, C32 0.194×, C-33 A 0.195×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H23 0.223×, LS 180 0.250×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Lonafarnib (drug)]] 5 µM in 1 line (C32 0.111×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~13% of this change | **0.789×** | -4.2 | 0.019 | 21/47 (C32, MIA PaCa-2, …) | top dose only |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.811×** | -3.8 | 0.037 | 16/48 (KATO III, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10702. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 37.4 | 7 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +12.7) | — |
| [[CFPAC-1 (line)]] | alt | 29.2 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +12.6) | — |
| [[LoVo (line)]] | wt | 41.0 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 2.40× (z +9.2) | — |
| [[NCI-H23 (line)]] | alt | 64.9 | 2 | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 2.63× (z +9.7) | [[Dinaciclib (drug)]] 5 µM 0.223× (z -14.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 50.0 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.194× (z -11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[HOP62 (line)]] | alt | 42.4 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.30× (z +10.7) | — |
| [[Hs 766T (line)]] | wt | 50.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.17× (z +9.4) | — |
| [[HS-578T (line)]] | alt | 63.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +10.4) | — |
| [[J82 (line)]] | alt | 40.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +10.5) | — |
| [[SHP-77 (line)]] | alt | 62.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.90× (z +8.6) | — |
| [[SW 900 (line)]] | alt | 41.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +10.8) | — |
| [[A498 (line)]] | wt | 36.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.88× (z +8.5) | — |
| [[AsPC-1 (line)]] | alt | 28.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.74× (z +15.8) | — |
| [[C-33 A (line)]] | alt | 46.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.195× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 60.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +8.6) | — |
| [[HT-29 (line)]] | alt | 50.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.78× (z +9.3) | — |
| [[LS 180 (line)]] | wt | 53.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.250× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 53.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.20× (z +10.8) | — |
| [[NCI-H2030 (line)]] | alt | 43.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.91× (z +8.6) | — |
| [[Panc 03.27 (line)]] | alt | 32.0 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.31× (z +9.2) | — |
| [[PANC-1 (line)]] | alt | 70.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.84× (z +12.0) | — |
| [[RKO (line)]] | wt | 47.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SK-MEL-2 (line)]] | alt | 43.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.353× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SW1417 (line)]] | alt | 33.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +9.9) | — |
| [[SW480 (line)]] | alt | 61.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 2.16× (z +11.2) | — |
| [[A-172 (line)]] | wt | 29.8 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 49.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 53.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 57.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 42.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 43.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 48.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 48.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 32.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 51.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 51.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 61.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10702), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[URM1]] | +0.73 | +0.68 / +0.53 | both halves | 1e-05 | pathway: tRNA processing |
| [[ZNF529-AS1]] | +0.73 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[ZNF785]] | +0.71 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[FBXO28]] | +0.70 | +0.60 / +0.67 | both halves | 7e-06 |  |
| [[PCF11-AS1]] | +0.69 | +0.64 / +0.53 | both halves | 1e-05 |  |
| [[ZNF586]] | +0.68 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[ZCCHC10]] | +0.67 | +0.75 / +0.46 | both halves | 3e-05 |  |
| [[ZNF721]] | +0.67 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[GPN2]] | +0.67 | +0.59 / +0.58 | both halves | 7e-06 |  |
| [[GPALPP1]] | +0.66 | +0.70 / +0.49 | both halves | 1e-05 |  |
| [[TAF11]] | +0.66 | +0.49 / +0.68 | both halves | 1e-05 |  |
| [[VPS13B-DT]] | +0.66 | +0.60 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[THEM6]] | -0.60 | -0.52 / -0.31 | both halves | 2e-04 |  |
| [[SSX2IP]] | -0.59 | -0.56 / -0.43 | both halves | 3e-05 |  |
| [[CDCA7L]] | -0.58 | -0.54 / -0.36 | both halves | 1e-04 |  |
| [[ACTB]] | -0.58 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[SPTBN1]] | -0.56 | -0.60 / -0.53 | both halves | 1e-05 |  |
| [[HLTF]] | -0.55 | -0.51 / -0.32 | both halves | 2e-04 |  |
| [[NIN]] | -0.55 | -0.47 / -0.43 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ZBTB8OS's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.5% of all compounds | 0.026 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ZNF345]] | B | ZNF345 activity raises ZBTB8OS's level | lines that do not express ZNF345 (13) vs lines expressing it (37) | 1.12× lower at baseline in the lines without ZNF345 | 0.054 | ⚠ within organs, on part of the lines; also absent: ZNF790, DNAH14, ZNF606 |
| [[ZNF529-AS1]] | B | ZNF529-AS1 activity raises ZBTB8OS's level | lines that do not express ZNF529-AS1 (8) vs lines expressing it (42) | 1.09× lower at baseline in the lines without ZNF529-AS1 | 0.098 | ⚠ within organs, on part of the lines; also absent: ZNF571, ZNF529, HOMER2 |
| [[SPACA6]] | C | SPACA6 activity raises ZBTB8OS's level | lines that do not express SPACA6 (3) vs lines expressing it (47) | 1.24× lower at baseline in the lines without SPACA6 | 0.073 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: TLE6, ZNF14, ZNF547; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 114]]; 42 genes; every member is in the + arm (projection on the module's main direction 0.772). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.38; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-10.2, 24.8); signed map (1.4, -3.0). **Vector** length 110, 29.0% of its response variance represented; |z| ≥ 3 in 870 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +7.7 | +12.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | +5.9 | +6.6 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +4.9 | +9.2 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.8 | +9.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.5 | +14.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +4.0 | +3.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.7 | +5.2 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.1 | +3.4 |
|  | [[Triamcinolone (drug)]] 5 µM |  | +3.0 | +3.5 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | -5.5 | +3.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~13% of this change | -4.9 | -4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.5 | +2.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~16% of this change | -4.3 | +3.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.7 | -1.1 |
|  | [[Clopidogrel (drug)]] 0.05 µM |  | -2.4 | -1.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.4 | -2.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.2 | -1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.1 | -3.8 |

## What is on record

|  |  |
|---|---|
| Name | tRNA splicing ligase complex subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.1 — chr1:32,600,172-32,650,903 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ARCH; previously ZBTB8OS |
| Gene groups (HGNC) | tRNA splicing ligase complex |
| Reactome | 3 pathways, smallest: tRNA processing in the nucleus; tRNA processing; Metabolism of RNA |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWT0](https://www.uniprot.org/uniprotkb/Q8IWT0) (tRNA splicing ligase complex subunit 1):

> Activation factor of RTCB, the catalytic subunit of the tRNA-splicing ligase complex (tRNA-LC), which is involved in the enzyme-dependent maturation of intron-containing pre-tRNAs. Functions downstream of the tRNA-splicing endonuclease that removes introns, ligating the two generated halves via phosphodiester bond formation. Catalyzes the GTP-dependent activation of RTCB, both proteins forming a composite active site coordinating GTP and metal ions to enable the guanylylation of RTCB a …

**Summary**, from NCBI Gene [339487](https://www.ncbi.nlm.nih.gov/gene/339487):

> Contributes to RNA ligase (GTP) activity and protein guanylyltransferase activity. Involved in IRE1-mediated unfolded protein response; mRNA splicing, via endonucleolytic cleavage and ligation; and tRNA exon ligation. Part of tRNA-splicing ligase complex. Is active in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:24094](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24094) · Entrez [339487](https://www.ncbi.nlm.nih.gov/gene/339487) · UniProt [Q8IWT0](https://www.uniprot.org/uniprotkb/Q8IWT0) · Ensembl [ENSG00000176261](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000176261)

## Data

Gene col 10702: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10702); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10702, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10702]; `tensor/DDL_lfc|DDL_z.npy` [10702]; `embed/gene_vectors.npy` [10702]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10702 or target_col == 10702). Every well: [[ZBTB8OS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ZBTB8OS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
