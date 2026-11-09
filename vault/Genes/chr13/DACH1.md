---
symbol: "DACH1"
type: "gene"
col: 15879
ensembl_id: "ENSG00000276644"
name: "dachshund family transcription factor 1"
location: "13q21.33"
module: 27
arm: "+"
pooled_cpm: 19.7
n_lines_expressing: 20
n_dd_up: 37
n_dd_down: 6
n_dd_up_clean: 34
n_dd_down_clean: 4
in_vector_space: true
direction_upstream: 28
direction_downstream: 14
tags: ["gene", "module/027"]
generated_by: "tahoemap"
---

# DACH1

*dachshund family transcription factor 1* — 13q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 37 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.56× (z +22.5, q 0e+00, up in 9 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (2 with an alert ⚠); the strongest is [[Mebendazole (drug)]] 5 µM: 0.563× (z -5.8, q 4e-06, down in 12 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RUNX1T1]] (+0.73, fdr 7e-06), [[RMST]] (+0.71, fdr 7e-06), [[ARHGAP25]] (+0.70, fdr 7e-06).
> It is in [[Module 027]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[NRXN1]] → it (grade B ⚠); 14 go from it, the strongest it → [[LINC02466]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 37 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15879.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.56×** | +22.5 | 0e+00 | 9/18 (LOX-IMVI, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.44×** | +13.2 | 3e-37 | 10/18 (J82, SW 900, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.29×** | +12.3 | 3e-32 | 11/18 (HEC-1-A, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.62×** | +10.1 | 1e-21 | 9/18 (J82, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.28×** | +8.3 | 1e-14 | 1/11 (LOX-IMVI) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.12×** | +7.9 | 4e-13 | 11/18 (HEC-1-A, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.00×** | +7.3 | 3e-11 | 0/14 | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **1.88×** | +6.6 | 3e-09 | 7/18 (NCI-H23, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.73×** | +5.7 | 7e-07 | 4/18 (HEC-1-A, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.71×** | +5.6 | 1e-06 | 9/18 (J82, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **2.76×** | +5.6 | 1e-06 | 6/18 (J82, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.68×** | +5.2 | 9e-06 | 7/18 (NCI-H23, SW 900, …) | top dose only | cell-cycle shift (explains ~2% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +5.1 | 2e-05 | 2/17 (LOX-IMVI, SW480) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.63×** | +5.1 | 2e-05 | 6/18 (NCI-H23, A498, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.60×** | +4.9 | 3e-05 | 3/18 (NCI-H23, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.48×** | +4.9 | 4e-05 | 7/18 (SW480, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.33×** | +4.1 | 0.001 | 7/18 (SW480, SW48, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 2 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15879.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mebendazole (drug)]] 5 µM |  | **0.563×** | -5.8 | 4e-06 | 12/18 (HT-29, SW480, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.635×** | -4.8 | 5e-04 | 15/18 (SW480, J82, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.489×** | -3.9 | 0.016 | 10/18 (Hs 766T, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.695×** | -3.8 | 0.019 | 11/18 (SK-MEL-2, SHP-77, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.608×** | -3.7 | 0.022 | 8/18 (SW480, Hs 766T, …) | rises with dose | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.799×** | -3.3 | 0.078 | 12/18 (HT-29, CHP-212, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.811× | -3.1 | 0.13 | 5/18 (SHP-77, SW48, …) | top dose only |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | 0.743× | -3.1 | 0.13 | 2/18 (Hs 766T, SHP-77) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15879. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SK-MEL-2 (line)]] | alt | 65.5 | 0 | 12 (5 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0203× (z -20.6) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.145× (z -15.1) |
| [[SHP-77 (line)]] | alt | 195 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.141× (z -14.4) |
| [[A-427 (line)]] | wt | 72.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -10.1) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -9.8) |
| [[J82 (line)]] | alt | 44.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.16× (z +10.5) | — |
| [[HEC-1-A (line)]] | alt | 6.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.78× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 81.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.196× (z -9.4) ⚠ cell-cycle shift, explains ~11% of this change |
| [[LOX-IMVI (line)]] | wt | 11.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.10× (z +10.0) | — |
| [[SW480 (line)]] | alt | 75.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.195× (z -10.1) |
| [[A-172 (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 9.09 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.58 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.15 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 4.03 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 3.92 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.25 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.75 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 31.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.71 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.26 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 3.42 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.93 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.66 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 3.28 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.23 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 3.08 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 1.88 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.63 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.57 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.48 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.98 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.21 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 3.80 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 4.66 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.35 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 8.00 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 123 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 11.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15879), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RUNX1T1]] | +0.73 | +0.68 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[RMST]] | +0.71 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[ARHGAP25]] | +0.70 | +0.66 / +0.66 | both halves | 7e-06 |  |
| [[LINC02466]] | +0.70 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[KCNB2]] | +0.68 | +0.61 / +0.60 | both halves | 7e-06 |  |
| [[SYT4]] | +0.68 | +0.57 / +0.65 | both halves | 1e-05 |  |
| [[HS3ST5]] | +0.68 | +0.67 / +0.60 | both halves | 7e-06 | **novel candidate** |
| [[RIT2]] | +0.67 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[ST18]] | +0.66 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[ASCL1]] | +0.66 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[LINC02197]] | +0.66 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[AGMO]] | +0.65 | +0.65 / +0.57 | both halves | 9e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 8, C 20. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NRXN1]] | B | NRXN1 activity raises DACH1's level | lines that do not express NRXN1 (19) vs lines expressing it (31) | 2.53× lower at baseline in the lines without NRXN1 | 0.012 | ⚠ within organs, on part of the lines; also absent: CHRM3, MIR2052HG, ENSG00000265994; maybe low, not absent |
| [[FRG1FP]] | B | FRG1FP activity raises DACH1's level | lines that do not express FRG1FP (22) vs lines expressing it (28) | 2.47× lower at baseline in the lines without FRG1FP | 0.018 | ⚠ within organs, on part of the lines; also absent: FRG1GP, LINC01446, ENSG00000248973; maybe low, not absent |
| [[LINC02466]] | B | LINC02466 activity raises DACH1's level | lines that do not express LINC02466 (21) vs lines expressing it (29) | 2.73× lower at baseline in the lines without LINC02466 | 0.044 | ⚠ within organs, on part of the lines; also absent: MME, ENSG00000227088, GABRA3; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers DACH1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SERPINF1]] | B | SERPINF1 activity raises DACH1's level | lines that do not express SERPINF1 (29) vs lines expressing it (21) | 1.86× lower at baseline in the lines without SERPINF1 | 0.068 | ⚠ within organs, on part of the lines; also absent: JAKMIP2-AS1, AK4P3, TMEM132D; maybe low, not absent |
| [[DGKB]] | B | DGKB activity raises DACH1's level | lines that do not express DGKB (23) vs lines expressing it (27) | 1.94× lower at baseline in the lines without DGKB | 0.081 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ENSG00000287862, MIR2052HG, RMST; maybe low, not absent |
| [[JAK2]] | B | JAK2 activity lowers DACH1's level | compounds that target JAK2: 3 of 3 raise it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 6.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[MIR2052HG]] | B | MIR2052HG activity raises DACH1's level | lines that do not express MIR2052HG (27) vs lines expressing it (23) | 1.70× lower at baseline in the lines without MIR2052HG | 0.097 | ⚠ within organs, on part of the lines; also absent: PI15, ENSG00000251598, ENSG00000287352; maybe low, not absent |
| [[LINC02315]] | C | LINC02315 activity raises DACH1's level | lines that do not express LINC02315 (31) vs lines expressing it (19) | 4.42× lower at baseline in the lines without LINC02315 | 0.001 | ⚠ within organs, on part of the lines; also absent: GABRG2, COX7B2, SLC25A24P1; co-absent with the target |
| [[CSMD3]] | C | CSMD3 activity raises DACH1's level | lines that do not express CSMD3 (36) vs lines expressing it (14) | 5.13× lower at baseline in the lines without CSMD3 | 0.001 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, LINC01205, ENSG00000243486; co-absent with the target |
| [[AGMO]] | C | AGMO activity raises DACH1's level | lines that do not express AGMO (30) vs lines expressing it (20) | 3.56× lower at baseline in the lines without AGMO | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000275016, SCG3, ENSG00000258657; co-absent with the target |
| [[MEOX2]] | C | MEOX2 activity raises DACH1's level | lines that do not express MEOX2 (36) vs lines expressing it (14) | 3.29× lower at baseline in the lines without MEOX2 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02566, MMRN1, ENSG00000232252; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 5, C 9. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02466]] | B | DACH1 activity raises LINC02466's level | lines that do not express DACH1 (30) vs lines expressing it (20) | 1.57× lower at baseline in the lines without DACH1 | 0.040 | ⚠ within organs, on part of the lines; also absent: FGF20, CSMD3, XKR7 |
| [[MIR325HG]] | B | DACH1 activity raises MIR325HG's level | lines that do not express DACH1 (30) vs lines expressing it (20) | 1.63× lower at baseline in the lines without DACH1 | 0.044 | ⚠ within organs, on part of the lines; also absent: FGF20, CSMD3, XKR7 |
| [[ARHGAP25]] | B | DACH1 activity raises ARHGAP25's level | lines that do not express DACH1 (30) vs lines expressing it (20) | 1.58× lower at baseline in the lines without DACH1 | 0.049 | ⚠ within organs, on part of the lines; also absent: FGF20, CSMD3, XKR7 |
| [[LINC01695]] | B | DACH1 activity raises LINC01695's level | lines that do not express DACH1 (30) vs lines expressing it (20) | 2.03× lower at baseline in the lines without DACH1 | 0.059 | ⚠ within organs, on part of the lines; also absent: FGF20, CSMD3, XKR7 |
| [[ADGRL2]] | B | DACH1 activity raises ADGRL2's level | lines that do not express DACH1 (30) vs lines expressing it (20) | 2.37× lower at baseline in the lines without DACH1 | 0.070 | ⚠ within organs, on part of the lines; also absent: FGF20, CSMD3, XKR7 |
| [[NELL2]] | C | DACH1 activity raises NELL2's level | lines that do not express DACH1 (30) vs lines expressing it (20) | 2.52× lower at baseline in the lines without DACH1 | 0.039 | ⚠ within organs, on part of the lines; also absent: FGF20, CSMD3, XKR7; co-absent with the target |
| [[SIM1]] | C | DACH1 activity raises SIM1's level | lines that do not express DACH1 (30) vs lines expressing it (20) | 1.49× lower at baseline in the lines without DACH1 | 0.045 | ⚠ within organs, on part of the lines; also absent: FGF20, CSMD3, XKR7; co-absent with the target |
| [[GRIA2]] | C | DACH1 activity raises GRIA2's level | lines that do not express DACH1 (30) vs lines expressing it (20) | 1.99× lower at baseline in the lines without DACH1 | 0.061 | ⚠ within organs, on part of the lines; also absent: FGF20, CSMD3, XKR7; co-absent with the target |
| [[GUCY1A1]] | C | DACH1 activity raises GUCY1A1's level | lines that do not express DACH1 (30) vs lines expressing it (20) | 1.73× lower at baseline in the lines without DACH1 | 0.072 | ⚠ within organs, on part of the lines; also absent: FGF20, CSMD3, XKR7; co-absent with the target |
| [[CDH10]] | C | DACH1 activity raises CDH10's level | lines that do not express DACH1 (30) vs lines expressing it (20) | 3.39× lower at baseline in the lines without DACH1 | 0.073 | ⚠ within organs, on part of the lines; also absent: FGF20, CSMD3, XKR7; co-absent with the target |
| [[LINC02315]] | C | DACH1 activity raises LINC02315's level | lines that do not express DACH1 (30) vs lines expressing it (20) | 2.69× lower at baseline in the lines without DACH1 | 0.074 | ⚠ within organs, on part of the lines; also absent: FGF20, CSMD3, XKR7; co-absent with the target |
| [[CSMD3]] | C | DACH1 activity raises CSMD3's level | lines that do not express DACH1 (30) vs lines expressing it (20) | 3.31× lower at baseline in the lines without DACH1 | 0.086 | ⚠ within organs, on part of the lines; also absent: FGF20, CSMD3, XKR7; co-absent with the target |

## Where it sits

- **Module**: [[Module 027]]; 155 genes; every member is in the + arm (projection on the module's main direction 0.625). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (29.4, 41.5); signed map (46.8, 33.8). **Vector** length 66.4, 20.1% of its response variance represented; |z| ≥ 3 in 555 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +7.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +8.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.9 | +22.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +5.6 | +1.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.8 | +13.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +12.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +3.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.3 | +3.0 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +2.3 | +3.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.3 | +2.9 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -3.1 | -4.8 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -2.2 | -3.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.1 | -5.8 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.0 | -3.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -1.9 | +5.1 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.8 | -2.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.8 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | dachshund family transcription factor 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q21.33 — chr13:71,437,966-71,867,204 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously DACH |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UI36](https://www.uniprot.org/uniprotkb/Q9UI36) (Dachshund homolog 1):

> Transcription factor that is involved in regulation of organogenesis. Seems to be a regulator of SIX1, SIX6 and probably SIX5. Corepression of precursor cell proliferation in myoblasts by SIX1 is switched to coactivation through recruitment of EYA3 to the SIX1-DACH1 complex. Transcriptional activation also seems to involve association of CREBBP. Seems to act as a corepressor of SIX6 in regulating proliferation by directly repressing cyclin-dependent kinase inhibitors, including the p27Kip1 …

**Summary**, from NCBI Gene [1602](https://www.ncbi.nlm.nih.gov/gene/1602):

> This gene encodes a chromatin-associated protein that associates with other DNA-binding transcription factors to regulate gene expression and cell fate determination during development. The protein contains a Ski domain that is highly conserved from Drosophila to human. Expression of this gene is lost in some forms of metastatic cancer, and is correlated with poor prognosis. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2009]

**Accessions** — [HGNC:2663](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2663) · Entrez [1602](https://www.ncbi.nlm.nih.gov/gene/1602) · UniProt [Q9UI36](https://www.uniprot.org/uniprotkb/Q9UI36) · Ensembl [ENSG00000276644](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000276644)

## Data

Gene col 15879: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15879); `tables/drug_effects.parquet` (45 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15879, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15879]; `tensor/DDL_lfc|DDL_z.npy` [15879]; `embed/gene_vectors.npy` [15879]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15879 or target_col == 15879). Every well: [[DACH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DACH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
