---
symbol: "ITPR2-AS1"
type: "gene"
col: 14984
ensembl_id: "ENSG00000256234"
name: "SSPN antisense RNA 1"
location: "12p12.1"
module: 39
arm: "+"
pooled_cpm: 2.67
n_lines_expressing: 46
n_dd_up: 9
n_dd_down: 12
n_dd_up_clean: 6
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 8
direction_downstream: 16
tags: ["gene", "module/039"]
generated_by: "tahoemap"
---

# ITPR2-AS1

*SSPN antisense RNA 1* — 12p12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.84× (z +15.7, q 0e+00, up in 22 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (1 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.321× (z -8.0, q 1e-12, down in 26 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LINC00486]] (+0.74, fdr 1e-05), [[SCUBE2]] (+0.71, fdr 7e-06), [[LINC01934]] (+0.70, fdr 7e-06); moves opposite to [[SLC35A1]] (-0.66, fdr 2e-05), [[HEBP1]] (-0.65, fdr 4e-05), [[L2HGDH]] (-0.64, fdr 2e-05).
> It is in [[Module 039]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[FSIP2-AS1]] → it (grade B ⚠); 16 go from it, the strongest it → [[ITPR2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14984.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.84×** | +15.7 | 0e+00 | 22/28 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.23×** | +7.6 | 8e-12 | 3/5 (HOP62, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.04×** | +7.5 | 8e-12 | 0/3 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.91×** | +7.5 | 8e-12 | 13/27 (A-172, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **2.04×** | +5.0 | 6e-05 | 17/42 (SW480, RKO, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.62×** | +4.8 | 1e-04 | 9/28 (LoVo, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.02×** | +4.6 | 4e-04 | 1/14 (SW480) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +3.4 | 0.053 | 5/38 (A-172, HEC-1-A, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.58×** | +3.2 | 0.082 | 3/22 (J82, HS-578T, …) | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14984.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.321×** | -8.0 | 1e-12 | 26/41 (LOX-IMVI, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.423×** | -6.0 | 5e-07 | 23/36 (NCI-H23, LS 180, …) | two highest doses | cell-cycle shift (explains ~17% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.432×** | -5.4 | 1e-05 | 19/39 (LoVo, C32, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.497×** | -4.9 | 1e-04 | 20/33 (NCI-H23, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Irinotecan (hydrochloride) (drug)]] 5 µM |  | **0.493×** | -4.8 | 2e-04 | 15/36 (C32, NCI-H2030, …) | top dose only | plate-row cell shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.325×** | -4.1 | 0.003 | 14/30 (LoVo, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.529×** | -4.1 | 0.003 | 8/42 (HepG2/C3A, LoVo, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.591×** | -3.7 | 0.016 | 14/38 (KATO III, NCI-H23, …) | inconsistent across doses | cell-cycle shift (explains ~15% here) |
| [[Fumaric acid (drug)]] 5 µM |  | **0.598×** | -3.5 | 0.034 | 8/39 (NCI-H2030, SK-MEL-2, …) | top dose only | plate-row cell shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.629×** | -3.2 | 0.070 | 13/20 (NCI-H23, LoVo, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.635×** | -3.2 | 0.078 | 10/26 (LS 180, HepG2/C3A, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[NG25 (drug)]] 5 µM |  | **0.427×** | -3.1 | 0.088 | 9/24 (RKO, PANC-1, …) | top dose only | cell-cycle shift (explains ~23% here); noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | 0.646× | -3.0 | 0.10 | 17/38 (LoVo, RKO, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14984. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 3.70 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +13.2) | [[Valdecoxib (drug)]] 0.5 µM 0.0808× (z -9.7) |
| [[A-172 (line)]] | wt | 2.46 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 71.1× (z +15.1) | — |
| [[HOP62 (line)]] | alt | 4.97 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +11.9) | — |
| [[LOX-IMVI (line)]] | wt | 4.85 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0352× (z -10.6) |
| [[NCI-H23 (line)]] | alt | 14.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0951× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[SW480 (line)]] | alt | 4.15 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.71× (z +8.5) | — |
| [[A-427 (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 2.08 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.06 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.79 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.373 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.17 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.806 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.335 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.46 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.03 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.23 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.773 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.09 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 7.67 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.14 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.88 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.58 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.19 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.83 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.287 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.34 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.903 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.856 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.13 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.39 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.68 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.36 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.24 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.34 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 0.330 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.18 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14984), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LINC00486]] | +0.74 | +0.78 / +0.55 | both halves | 1e-05 |  |
| [[SCUBE2]] | +0.71 | +0.66 / +0.64 | both halves | 7e-06 |  |
| [[LINC01934]] | +0.70 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[SLC22A1]] | +0.70 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[LINC01191]] | +0.70 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[DPYS]] | +0.70 | +0.69 / +0.60 | both halves | 7e-06 |  |
| [[NEPRO-AS1]] | +0.69 | +0.73 / +0.51 | both halves | 1e-05 | same gene group |
| [[NEK10]] | +0.69 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[SEMA6A-AS1]] | +0.69 | +0.71 / +0.61 | both halves | 7e-06 | same gene group |
| [[SMCO2]] | +0.69 | +0.68 / +0.58 | both halves | 7e-06 |  |
| [[GARIN1B]] | +0.69 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[SSUH2]] | +0.68 | +0.75 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35A1]] | -0.66 | -0.48 / -0.62 | both halves | 2e-05 |  |
| [[HEBP1]] | -0.65 | -0.71 / -0.42 | both halves | 4e-05 |  |
| [[L2HGDH]] | -0.64 | -0.60 / -0.48 | both halves | 2e-05 |  |
| [[PRUNE1]] | -0.64 | -0.61 / -0.49 | both halves | 1e-05 |  |
| [[SLC9A6]] | -0.64 | -0.65 / -0.50 | both halves | 1e-05 |  |
| [[CCZ1B]] | -0.64 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[GMCL1]] | -0.64 | -0.67 / -0.47 | both halves | 2e-05 |  |
| [[SDHAP1]] | -0.63 | -0.70 / -0.43 | both halves | 3e-05 |  |
| [[MYPOP]] | -0.62 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[GTF2H2B]] | -0.62 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[SDHAP2]] | -0.62 | -0.69 / -0.44 | both halves | 3e-05 |  |
| [[NCK1]] | -0.62 | -0.62 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 6, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FSIP2-AS1]] | B | FSIP2-AS1 activity raises ITPR2-AS1's level | lines that do not express FSIP2-AS1 (6) vs lines expressing it (44) | 1.97× lower at baseline in the lines without FSIP2-AS1 | 0.010 | ⚠ within organs, on part of the lines; also absent: PMFBP1, SPATA17, ENSG00000287621; maybe low, not absent |
| [[LINC02516]] | B | LINC02516 activity raises ITPR2-AS1's level | lines that do not express LINC02516 (19) vs lines expressing it (31) | 1.45× lower at baseline in the lines without LINC02516 | 0.018 | ⚠ within organs, on part of the lines; also absent: ADAM23, TEK, SPOCK3 |
| [[SCUBE2]] | B | SCUBE2 activity raises ITPR2-AS1's level | lines that do not express SCUBE2 (7) vs lines expressing it (43) | 1.86× lower at baseline in the lines without SCUBE2 | 0.021 | ⚠ within organs, on part of the lines; also absent: NT5M, PRKACB, RASSF8-AS1; maybe low, not absent |
| [[CFAP299]] | B | CFAP299 activity raises ITPR2-AS1's level | lines that do not express CFAP299 (27) vs lines expressing it (23) | 1.46× lower at baseline in the lines without CFAP299 | 0.023 | ⚠ within organs, on part of the lines; also absent: FGF5, LINC00702, JAM2 |
| [[PMFBP1]] | B | PMFBP1 activity raises ITPR2-AS1's level | lines that do not express PMFBP1 (8) vs lines expressing it (42) | 1.79× lower at baseline in the lines without PMFBP1 | 0.027 | ⚠ within organs, on part of the lines; also absent: GALNT16, FSIP2-AS1, ENSG00000237356; maybe low, not absent |
| [[LINC00334]] | B | LINC00334 activity raises ITPR2-AS1's level | lines that do not express LINC00334 (10) vs lines expressing it (40) | 1.63× lower at baseline in the lines without LINC00334 | 0.064 | ⚠ within organs, on part of the lines; also absent: NEK10, SSC5D, KDM2B-DT; maybe low, not absent |
| [[ITPR2]] | C | ITPR2 activity raises ITPR2-AS1's level | lines that do not express ITPR2 (5) vs lines expressing it (45) | 2.49× lower at baseline in the lines without ITPR2 | 0.032 | ⚠ within organs, on part of the lines; also absent: ITPR2-AS1, ENSG00000286162, SPATA17; maybe low, not absent; co-absent with the target |
| [[NEK10]] | C | NEK10 activity raises ITPR2-AS1's level | lines that do not express NEK10 (6) vs lines expressing it (44) | 1.97× lower at baseline in the lines without NEK10 | 0.090 | ⚠ within organs, on part of the lines; also absent: ZNF474, ITPR2-AS1, LINC00334; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 0, C 16. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITPR2]] | C | ITPR2-AS1 activity raises ITPR2's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 5.53× lower at baseline in the lines without ITPR2-AS1 | 0.002 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17; co-absent with the target |
| [[ST7L]] | C | ITPR2-AS1 activity raises ST7L's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 2.15× lower at baseline in the lines without ITPR2-AS1 | 0.011 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17 |
| [[SDCBP2-AS1]] | C | ITPR2-AS1 activity raises SDCBP2-AS1's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 1.61× lower at baseline in the lines without ITPR2-AS1 | 0.018 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17 |
| [[ALDH8A1]] | C | ITPR2-AS1 activity raises ALDH8A1's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 2.43× lower at baseline in the lines without ITPR2-AS1 | 0.029 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17 |
| [[CAVIN4]] | C | ITPR2-AS1 activity raises CAVIN4's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 2.74× lower at baseline in the lines without ITPR2-AS1 | 0.039 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17 |
| [[WARS2-AS1]] | C | ITPR2-AS1 activity raises WARS2-AS1's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 2.30× lower at baseline in the lines without ITPR2-AS1 | 0.048 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17 |
| [[PSMD6-AS1]] | C | ITPR2-AS1 activity strengthens PSMD6-AS1's drug response | lines that do not express ITPR2-AS1 (4) vs lines expressing it (43) | the lines without ITPR2-AS1 respond 0.93× as strongly (z diff +0.29); strongest at Panobinostat 0.5 µM: 0.64x vs 0.35x (z diff +2.6) | 0.052 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17; target measured in part of the lines; both ways; artifact flags |
| [[LINC02803]] | C | ITPR2-AS1 activity raises LINC02803's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 1.74× lower at baseline in the lines without ITPR2-AS1 | 0.055 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17 |
| [[CCDC162P]] | C | ITPR2-AS1 activity raises CCDC162P's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 2.79× lower at baseline in the lines without ITPR2-AS1 | 0.064 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17; co-absent with the target |
| [[PMFBP1]] | C | ITPR2-AS1 activity raises PMFBP1's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 2.53× lower at baseline in the lines without ITPR2-AS1 | 0.067 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17 |
| [[STAC3]] | C | ITPR2-AS1 activity raises STAC3's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 1.73× lower at baseline in the lines without ITPR2-AS1 | 0.076 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17 |
| [[NEK10]] | C | ITPR2-AS1 activity raises NEK10's level | lines that do not express ITPR2-AS1 (4) vs lines expressing it (46) | 3.90× lower at baseline in the lines without ITPR2-AS1 | 0.084 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ITPR2, ENSG00000286162, SPATA17; co-absent with the target |

## Where it sits

- **Module**: [[Module 039]]; 115 genes; every member is in the + arm (projection on the module's main direction 0.675). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (35.5, -10.5); signed map (19.9, 8.1). **Vector** length 63.8, 11.5% of its response variance represented; |z| ≥ 3 in 894 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.0 | +15.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.6 | +7.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.8 | +7.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.9 | +2.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.9 | +4.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.0 | +1.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.0 | +5.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +1.6 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.3 | +1.6 |
| fall | [[Belinostat (drug)]] 0.5 µM |  | -2.8 | -3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -2.3 | -5.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -2.9 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | -2.1 | -3.0 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.1 | -0.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.5 | -2.8 |
|  | [[HI-TOPK-032 (drug)]] 0.05 µM |  | -1.4 | -1.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.4 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | SSPN antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12p12.1 — chr12:26,211,164-26,335,856 (-) |
| Ensembl biotype | lncRNA |
| Also known as | ; previously ITPR2-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56072](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56072) · Entrez [101928554](https://www.ncbi.nlm.nih.gov/gene/101928554) · Ensembl [ENSG00000256234](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000256234)

## Data

Gene col 14984: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14984); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14984, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14984]; `tensor/DDL_lfc|DDL_z.npy` [14984]; `embed/gene_vectors.npy` [14984]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14984 or target_col == 14984). Every well: [[ITPR2-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITPR2-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
