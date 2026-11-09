---
symbol: "SCPEP1"
type: "gene"
col: 4250
ensembl_id: "ENSG00000121064"
name: "serine carboxypeptidase 1"
location: "17q22"
module: 45
arm: "+"
pooled_cpm: 15.34
n_lines_expressing: 50
n_dd_up: 43
n_dd_down: 5
n_dd_up_clean: 33
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/045"]
generated_by: "tahoemap"
---

# SCPEP1

*serine carboxypeptidase 1* — 17q22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (10 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 5.77× (z +23.6, q 0e+00, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 0.905× (z -4.7, q 0.002, down in 11 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Peretinoin (drug)]] 5 µM: 0.718× (z -4.3, q 0.005, down in 17 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CAT]] (+0.75, fdr 7e-06), [[TMEM9]] (+0.74, fdr 7e-06), [[ATP6V1A]] (+0.70, fdr 7e-06); moves opposite to [[AGO2]] (-0.66, fdr 7e-06), [[TLNRD1]] (-0.60, fdr 1e-05), [[ITPRIPL2]] (-0.58, fdr 2e-05).
> It sits in the **+** arm of [[Module 045]] (Iron uptake and transport).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[MPP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 10 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4250.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **5.77×** | +23.6 | 0e+00 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.17×** | +22.1 | 0e+00 | 47/48 (PANC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **4.64×** | +20.7 | 0e+00 | 46/48 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.61×** | +12.9 | 4e-36 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.39×** | +11.7 | 1e-29 | 41/47 (HOP62, KATO III, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.16×** | +10.4 | 3e-23 | 37/48 (HOP62, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.63×** | +9.3 | 1e-18 | 30/48 (NCI-H23, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +9.1 | 4e-18 | 35/48 (A-172, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.05×** | +9.1 | 4e-18 | 36/48 (A498, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.51×** | +8.8 | 5e-17 | 40/48 (PANC-1, NCI-H460, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.96×** | +8.7 | 1e-16 | 30/44 (NCI-H2030, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.89×** | +8.6 | 5e-16 | 35/46 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.56×** | +8.5 | 9e-16 | 30/48 (RKO, LS 180, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +7.7 | 7e-13 | 35/48 (HT-29, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~52% of this change | **1.66×** | +6.9 | 2e-10 | 19/35 (A498, LoVo, …) | all doses, flat | composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +5.4 | 2e-06 | 25/48 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **1.30×** | +5.0 | 1e-05 | 22/48 (RPMI-7951, RKO, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4250.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -4.7 | 0.002 | 11/48 (SNU-1, COLO 205, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.718×** | -4.3 | 0.005 | 17/47 (A-172, C32, …) | rises with dose |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.732×** | -4.2 | 0.005 | 12/48 (SW 900, CHP-212, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.757×** | -3.7 | 0.027 | 17/48 (SW 900, NCI-H460, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.782×** | -3.3 | 0.098 | 20/48 (KATO III, C32, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.5 µM |  | **0.710×** | -3.3 | 0.098 | 15/47 (SHP-77, CHP-212, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.5 µM |  | 0.797× | -3.0 | 0.19 | 14/46 (SNU-1, SW480, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4250. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 17.0 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 5.05× (z +9.9) | — |
| [[KATO III (line)]] | alt | 15.6 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 7.92× (z +12.6) | — |
| [[NCI-H23 (line)]] | alt | 12.5 | 3 | 1 (1 ⚠) | [[Panobinostat (drug)]] 0.5 µM 5.33× (z +8.9) | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.144× (z -9.9) ⚠ cell-cycle shift, explains ~45% of this change |
| [[NCI-H460 (line)]] | wt | 19.5 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 4.62× (z +11.7) | — |
| [[SW480 (line)]] | alt | 11.1 | 4 | 0 | [[Panobinostat (drug)]] 5 µM 6.44× (z +12.6) | — |
| [[A-427 (line)]] | wt | 16.1 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.97× (z +10.9) | — |
| [[A498 (line)]] | wt | 21.7 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.27× (z +11.9) | — |
| [[A549 (line)]] | wt | 11.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 8.50× (z +10.8) | — |
| [[CFPAC-1 (line)]] | alt | 14.8 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 5.85× (z +11.6) | — |
| [[HEC-1-A (line)]] | alt | 13.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 5.99× (z +11.5) | — |
| [[HT-29 (line)]] | alt | 4.18 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 15.6× (z +9.5) | — |
| [[LoVo (line)]] | wt | 8.28 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 9.48× (z +12.3) | — |
| [[LOX-IMVI (line)]] | wt | 10.2 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.52× (z +10.5) | — |
| [[MIA PaCa-2 (line)]] | alt | 11.2 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 12.4× (z +11.4) | — |
| [[NCI-H2030 (line)]] | alt | 13.3 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.32× (z +9.8) | — |
| [[PANC-1 (line)]] | alt | 18.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.42× (z +16.7) | — |
| [[SNU-423 (line)]] | alt | 12.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.77× (z +10.1) | — |
| [[SW1417 (line)]] | alt | 11.5 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.73× (z +10.3) | — |
| [[AN3 CA (line)]] | alt | 44.5 | 0 | 2 | — | [[Hydroxyurea (drug)]] 0.05 µM 0.0712× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 26.3 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.56× (z +8.5) | — |
| [[J82 (line)]] | alt | 16.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.72× (z +8.5) | — |
| [[LS 180 (line)]] | wt | 8.48 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 7.89× (z +9.3) | — |
| [[NCI-H2347 (line)]] | alt | 11.1 | 2 | 0 | [[Panobinostat (drug)]] 0.5 µM 6.71× (z +10.7) | — |
| [[Panc 03.27 (line)]] | alt | 10.8 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 7.35× (z +9.1) | — |
| [[A-172 (line)]] | wt | 35.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.43× (z +9.5) | — |
| [[BT-474 (line)]] | alt | 9.41 | 1 | 0 | [[Panobinostat (drug)]] 0.5 µM 10.6× (z +8.7) | — |
| [[COLO 205 (line)]] | alt | 15.1 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.93× (z +8.9) | — |
| [[H4 (line)]] | wt | 22.1 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.158× (z -8.9) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 9.59 | 0 | 1 | — | [[Torkinib (drug)]] 0.05 µM 0.0390× (z -11.0) |
| [[HepG2_C3A (line)]] | wt | 5.17 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 18.1× (z +8.8) | — |
| [[NCI-H1792 (line)]] | alt | 19.2 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.71× (z +10.0) | — |
| [[SK-MEL-2 (line)]] | alt | 11.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.89× (z +8.5) | — |
| [[AsPC-1 (line)]] | alt | 4.35 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 66.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 24.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 28.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 52.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.75 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4250), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAT]] | +0.75 | +0.62 / +0.78 | both halves | 7e-06 |  |
| [[TMEM9]] | +0.74 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[ATP6V1A]] | +0.70 | +0.76 / +0.70 | both halves | 7e-06 |  |
| [[USP30]] | +0.67 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[GNPDA2]] | +0.66 | +0.60 / +0.72 | both halves | 7e-06 |  |
| [[PGAP1]] | +0.65 | +0.57 / +0.69 | both halves | 8e-06 |  |
| [[DNASE2]] | +0.64 | +0.63 / +0.55 | both halves | 1e-05 |  |
| [[NDRG3]] | +0.64 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[COPS4]] | +0.64 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[CTSD]] | +0.63 | +0.60 / +0.53 | both halves | 1e-05 |  |
| [[ASAH1]] | +0.62 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[SCP2]] | +0.62 | +0.66 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AGO2]] | -0.66 | -0.65 / -0.61 | both halves | 7e-06 |  |
| [[TLNRD1]] | -0.60 | -0.58 / -0.54 | both halves | 1e-05 |  |
| [[ITPRIPL2]] | -0.58 | -0.47 / -0.61 | both halves | 2e-05 |  |
| [[ST7L]] | -0.57 | -0.38 / -0.56 | both halves | 7e-05 |  |
| [[EXOSC6]] | -0.57 | -0.49 / -0.47 | both halves | 2e-05 |  |
| [[MYH3]] | -0.57 | -0.42 / -0.49 | both halves | 4e-05 |  |
| [[KCNJ14]] | -0.57 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[REXO1]] | -0.56 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[CFAP161]] | -0.56 | -0.46 / -0.49 | both halves | 2e-05 |  |
| [[ZNF800]] | -0.56 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[CYREN]] | -0.56 | -0.35 / -0.53 | both halves | 1e-04 |  |
| [[MIRLET7IHG]] | -0.56 | -0.46 / -0.52 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 3, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MPP1]] | B | MPP1 activity raises SCPEP1's level | lines that do not express MPP1 (7) vs lines expressing it (43) | 1.88× lower at baseline in the lines without MPP1 | 0.044 | ⚠ within organs, on part of the lines; also absent: ZNF566, ELOVL5, PALM2AKAP2 |
| [[GXYLT2]] | B | GXYLT2 activity raises SCPEP1's level | lines that do not express GXYLT2 (11) vs lines expressing it (39) | 1.64× lower at baseline in the lines without GXYLT2 | 0.056 | ⚠ within organs, on part of the lines; also absent: TMEM145, SLC17A7, FAM171B |
| [[SYNGR1]] | B | SYNGR1 activity raises SCPEP1's level | lines that do not express SYNGR1 (12) vs lines expressing it (38) | 1.81× lower at baseline in the lines without SYNGR1 | 0.074 | ⚠ within organs, on part of the lines; also absent: TTC7B, RASSF8, EML1 |
| [[GSTM4]] | C | GSTM4 activity raises SCPEP1's level | lines that do not express GSTM4 (4) vs lines expressing it (46) | 2.21× lower at baseline in the lines without GSTM4 | 0.007 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: LINC00888, KIF3C, GGH; maybe low, not absent |
| [[SMARCD3]] | C | SMARCD3 activity raises SCPEP1's level | lines that do not express SMARCD3 (3) vs lines expressing it (47) | 3.04× lower at baseline in the lines without SMARCD3 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; co-occurs with ERBB3; also absent: MYBL2, PBK, AURKB; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 045]] — Iron uptake and transport; 102 genes; this gene is in the **+** arm (projection on the module's main direction 0.750). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-0.2, -8.7); signed map (-30.7, -7.1). **Vector** length 90.1, 21.8% of its response variance represented; |z| ≥ 3 in 1,183 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Regulation of MITF-M-dependent genes involved in lysosome biogenesis and autophagy* (reactome, mean cos +0.54 to 4).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +5.0 | +11.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.0 | +10.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.3 | +9.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +4.1 | +5.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +7.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | +8.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.8 | +4.5 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.0 | -0.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.8 | -0.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -3.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +2.6 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -3.9 | +9.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -3.1 | -2.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.0 | -1.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.9 | -4.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.8 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | serine carboxypeptidase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q22 — chr17:56,978,129-57,006,768 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RISC |
| Gene groups (HGNC) | M14 carboxypeptidases |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HB40](https://www.uniprot.org/uniprotkb/Q9HB40) (Retinoid-inducible serine carboxypeptidase):

> May be involved in vascular wall and kidney homeostasis.

**Summary**, from NCBI Gene [59342](https://www.ncbi.nlm.nih.gov/gene/59342):

> Predicted to enable serine-type carboxypeptidase activity. Predicted to be involved in negative regulation of blood pressure and retinoic acid metabolic process. Predicted to act upstream of or within blood vessel diameter maintenance. Located in extracellular exosome. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:29507](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29507) · Entrez [59342](https://www.ncbi.nlm.nih.gov/gene/59342) · UniProt [Q9HB40](https://www.uniprot.org/uniprotkb/Q9HB40) · Ensembl [ENSG00000121064](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000121064)

## Data

Gene col 4250: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4250); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4250, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4250]; `tensor/DDL_lfc|DDL_z.npy` [4250]; `embed/gene_vectors.npy` [4250]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4250 or target_col == 4250). Every well: [[SCPEP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SCPEP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
