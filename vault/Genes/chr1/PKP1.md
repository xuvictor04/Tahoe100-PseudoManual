---
symbol: "PKP1"
type: "gene"
col: 1314
ensembl_id: "ENSG00000081277"
name: "plakophilin 1"
location: "1q32.1"
module: 73
arm: "+"
pooled_cpm: 5.0
n_lines_expressing: 17
n_dd_up: 23
n_dd_down: 1
n_dd_up_clean: 13
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 13
direction_downstream: 69
tags: ["gene", "module/073"]
generated_by: "tahoemap"
---

# PKP1

*plakophilin 1* — 1q32.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (10 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 4.34× (z +12.1, q 4e-31, up in 3 of 7 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.85× (z +7.1, q 1e-10, up in 10 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.569× (z -4.7, q 0.001, down in 7 of 14 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (Hs 766T 0.211×, NCI-H1792 0.398×); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H1792 0.205×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LoVo 0.0317×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H1792 0.227×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SERPINB5]] (+0.69, fdr 7e-06), [[DSG3]] (+0.63, fdr 1e-05), [[PRSS3]] (+0.63, fdr 1e-05).
> It is in [[Module 073]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 13 arrows point to it, the strongest [[IGSF9B]] → it (grade B ⚠); 69 go from it, the strongest it → [[UBE2H]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1314.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.34×** | +12.1 | 4e-31 | 3/7 (Hs 766T, J82, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.07×** | +11.2 | 2e-26 | 3/5 (Hs 766T, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.03×** | +10.6 | 3e-24 | 2/6 (Hs 766T, AsPC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.85×** | +7.1 | 1e-10 | 10/14 (J82, Hs 766T, …) | rises with dose |  |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **2.73×** | +5.9 | 4e-07 | 0/6 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +5.8 | 6e-07 | 0/9 | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.01×** | +5.8 | 7e-07 | 7/13 (J82, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.88×** | +5.0 | 5e-05 | 2/11 (SW1417, Hs 766T) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.46×** | +4.4 | 8e-04 | 1/14 (J82) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.43×** | +4.2 | 0.002 | 4/14 (COLO 205, BT-474, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **3.02×** | +4.1 | 0.002 | 0/5 | top dose only | noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.59×** | +3.8 | 0.007 | 0/10 | inconsistent across doses | low cells (technical?) |
| [[Thymol (drug)]] 0.5 µM |  | **1.58×** | +3.8 | 0.007 | 1/10 (BT-474) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.55×** | +3.6 | 0.015 | 1/6 (SW1417) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.80×** | +3.5 | 0.021 | 0/11 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.79×** | +3.4 | 0.022 | 0/8 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.50×** | +3.3 | 0.029 | 1/13 (NCI-H460) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.33×** | +3.2 | 0.038 | 0/13 | top dose only | cell-cycle shift (explains ~0% here) |
| [[Pyridoxine (drug)]] 0.5 µM |  | **1.48×** | +3.2 | 0.038 | 1/12 (COLO 205) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Omeprazole (drug)]] 0.5 µM |  | **1.46×** | +3.1 | 0.051 | 0/13 | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.45×** | +3.0 | 0.064 | 1/13 (CFPAC-1) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1314.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (Hs 766T 0.211×, NCI-H1792 0.398×); [[Panobinostat (drug)]] 5 µM in 1 line (NCI-H1792 0.205×); [[Ouabain (Octahydrate) (drug)]] 5 µM in 1 line (LoVo 0.0317×; ⚠ cell-cycle shift, explains ~0% of this change); [[Panobinostat (drug)]] 0.5 µM in 1 line (NCI-H1792 0.227×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.569×** | -4.7 | 0.001 | 7/14 (NCI-H1792, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | 0.656× | -3.6 | 0.11 | 10/14 (NCI-H1792, Hs 766T, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | 0.648× | -3.4 | 0.12 | 3/14 (SW48, AsPC-1, …) | inconsistent across doses |  |
| [[Rutin (trihydrate) (drug)]] 0.05 µM |  | 0.652× | -3.3 | 0.12 | 0/14 | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | 0.684× | -3.2 | 0.15 | 4/14 (LoVo, J82, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.00 per unit of S-phase module lfc, -0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1314. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 85.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.205× (z -10.5) |
| [[Hs 766T (line)]] | wt | 56.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.211× (z -13.8) |
| [[LoVo (line)]] | wt | 4.01 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0317× (z -10.3) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 0.687 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 0.238 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 0.334 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.364 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.538 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.00 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.348 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.466 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.09 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 0.469 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 0.836 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.339 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.367 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.438 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 0.417 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 0.959 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.460 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.397 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.408 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.291 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.603 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 0.292 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.12 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.269 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.35 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.55 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.428 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.06 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.333 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.410 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.456 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.437 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.352 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.660 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 2.08 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.426 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 6.60 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.92 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.01 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1314), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SERPINB5]] | +0.69 | +0.69 / +0.61 | both halves | 7e-06 | STRING 560 |
| [[DSG3]] | +0.63 | +0.63 / +0.51 | both halves | 1e-05 | pathway: Apoptosis; STRING 951 |
| [[PRSS3]] | +0.63 | +0.60 / +0.56 | both halves | 1e-05 |  |
| [[KLK10]] | +0.59 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[KLK11]] | +0.58 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[HS3ST1]] | +0.58 | +0.58 / +0.43 | both halves | 3e-05 | pathway: HALLMARK_HYPOXIA |
| [[ANO1]] | +0.58 | +0.55 / +0.49 | both halves | 1e-05 |  |
| [[IGSF9]] | +0.57 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[NGEF]] | +0.57 | +0.52 / +0.52 | both halves | 1e-05 |  |
| [[DENND2C]] | +0.56 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[IL2RG]] | +0.55 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[FA2H]] | +0.55 | +0.62 / +0.46 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 1, C 12. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IGSF9B]] | B | IGSF9B activity lowers PKP1's level | lines that do not express IGSF9B (17) vs lines expressing it (33) | 1.74× higher at baseline in the lines without IGSF9B | 0.072 | ⚠ within organs, on part of the lines; also absent: ADRA2C, PTPRN2, CBFA2T3 |
| [[HPGD]] | C | HPGD activity raises PKP1's level | lines that do not express HPGD (30) vs lines expressing it (20) | 2.89× lower at baseline in the lines without HPGD | 0.008 | ⚠ within organs, on part of the lines; also absent: ENSG00000251584, IL20RA, SDR16C5; co-absent with the target |
| [[EHF]] | C | EHF activity raises PKP1's level | lines that do not express EHF (27) vs lines expressing it (23) | 2.55× lower at baseline in the lines without EHF | 0.014 | ⚠ within organs, on part of the lines; also absent: TMPRSS4, IRF6, GJB3; co-absent with the target |
| [[ACSL5]] | C | ACSL5 activity raises PKP1's level | lines that do not express ACSL5 (24) vs lines expressing it (26) | 2.45× lower at baseline in the lines without ACSL5 | 0.031 | ⚠ within organs, on part of the lines; also absent: TNFRSF14-AS1, IL20RA, TINAGL1; co-absent with the target |
| [[FA2H]] | C | FA2H activity raises PKP1's level | lines that do not express FA2H (27) vs lines expressing it (23) | 2.72× lower at baseline in the lines without FA2H | 0.044 | ⚠ within organs, on part of the lines; also absent: IRF6, ST14, SGPP2; co-absent with the target |
| [[GALNT5]] | C | GALNT5 activity raises PKP1's level | lines that do not express GALNT5 (27) vs lines expressing it (23) | 2.29× lower at baseline in the lines without GALNT5 | 0.050 | ⚠ within organs, on part of the lines; also absent: IL20RA, HPGD, ICAM2; co-absent with the target |
| [[SKAP1]] | C | SKAP1 activity raises PKP1's level | lines that do not express SKAP1 (34) vs lines expressing it (16) | 2.52× lower at baseline in the lines without SKAP1 | 0.052 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: KCNE3, TMEM125, SLC5A1; co-absent with the target |
| [[AFAP1L2]] | C | AFAP1L2 activity raises PKP1's level | lines that do not express AFAP1L2 (27) vs lines expressing it (23) | 2.21× lower at baseline in the lines without AFAP1L2 | 0.064 | ⚠ within organs, on part of the lines; also absent: LY75, ENSG00000235726, SHH; co-absent with the target |
| [[SLC38A5]] | C | SLC38A5 activity raises PKP1's level | lines that do not express SLC38A5 (35) vs lines expressing it (15) | 2.20× lower at baseline in the lines without SLC38A5 | 0.065 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: XIST, HEPH, KRT5; co-absent with the target |
| [[C1orf116]] | C | C1orf116 activity raises PKP1's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 2.33× lower at baseline in the lines without C1orf116 | 0.074 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; co-absent with the target |
| [[DHRS9]] | C | DHRS9 activity raises PKP1's level | lines that do not express DHRS9 (40) vs lines expressing it (10) | 2.64× lower at baseline in the lines without DHRS9 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC17, PIGR, LINC01610; co-absent with the target |
| [[SLC22A3]] | C | SLC22A3 activity raises PKP1's level | lines that do not express SLC22A3 (30) vs lines expressing it (20) | 2.27× lower at baseline in the lines without SLC22A3 | 0.096 | ⚠ within organs, on part of the lines; also absent: TTC22, GCNT3, INAVA; co-absent with the target |

### Downstream of this gene

*69 arrows, 69 of them with an alert ⚠; grade A 0, B 32, C 37. Shown: the 12 strongest; 57 more arrows (57 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBE2H]] | B | PKP1 activity raises UBE2H's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 1.82× lower at baseline in the lines without PKP1 | 6e-04 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5 |
| [[LYPD3]] | B | PKP1 activity raises LYPD3's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 2.44× lower at baseline in the lines without PKP1 | 0.003 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5 |
| [[UBE2H]] | B | PKP1 activity weakens UBE2H's drug response | lines that do not express PKP1 (33) vs lines expressing it (16) | the lines without PKP1 respond 1.25× as strongly (z diff -0.90); strongest at Homoharringtonine 5 µM: 1.61x vs 1.15x (z diff -5.7) | 0.006 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5; target measured in part of the lines; both ways; artifact flags |
| [[OXSR1]] | B | PKP1 activity raises OXSR1's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 1.51× lower at baseline in the lines without PKP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5 |
| [[IL22RA1]] | B | PKP1 activity raises IL22RA1's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 2.08× lower at baseline in the lines without PKP1 | 0.011 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5 |
| [[JUP]] | B | PKP1 activity raises JUP's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 3.39× lower at baseline in the lines without PKP1 | 0.012 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5 |
| [[SLC9A2]] | B | PKP1 activity raises SLC9A2's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 2.69× lower at baseline in the lines without PKP1 | 0.014 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5 |
| [[GRHL3]] | B | PKP1 activity raises GRHL3's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 2.47× lower at baseline in the lines without PKP1 | 0.015 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5 |
| [[YOD1]] | B | PKP1 activity raises YOD1's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 1.88× lower at baseline in the lines without PKP1 | 0.020 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5 |
| [[NCF2]] | B | PKP1 activity raises NCF2's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 2.10× lower at baseline in the lines without PKP1 | 0.022 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5 |
| [[CDA]] | B | PKP1 activity raises CDA's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 2.72× lower at baseline in the lines without PKP1 | 0.028 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5 |
| [[IGSF9]] | B | PKP1 activity raises IGSF9's level | lines that do not express PKP1 (33) vs lines expressing it (17) | 1.93× lower at baseline in the lines without PKP1 | 0.031 | ⚠ within organs, on part of the lines; also absent: SERPINB5, TFF2, CLIC5 |

## Where it sits

- **Module**: [[Module 073]]; 66 genes; every member is in the + arm (projection on the module's main direction 0.607). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (13.0, 54.3); signed map (0.7, 39.4). **Vector** length 33.1, 7.89% of its response variance represented; |z| ≥ 3 in 340 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +7.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +11.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +2.5 | +5.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.5 | +12.1 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.4 | +10.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.3 | +2.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +1.1 | +3.3 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +0.9 | +0.6 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +0.8 | +2.6 |
| fall | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.1 | -2.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -0.9 | -1.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -0.9 | -1.6 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -0.9 | -1.9 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.8 | -1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -0.7 | -0.6 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -0.6 | -2.5 |
|  | [[Megestrol (drug)]] 5 µM |  | -0.5 | -0.7 |
|  | [[Sulfatinib (drug)]] 5 µM |  | -0.5 | -0.4 |

## What is on record

|  |  |
|---|---|
| Name | plakophilin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q32.1 — chr1:201,283,452-201,332,993 (+) |
| Ensembl biotype | protein_coding |
| Also known as | B6P |
| Gene groups (HGNC) | Armadillo repeat containing; Plakophilins |
| Hallmark sets | KRAS_SIGNALING_DN, HYPOXIA |
| Reactome | 9 pathways, smallest: Apoptotic cleavage of cell adhesion  proteins; Apoptotic cleavage of cellular proteins; Formation of the cornified envelope |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13835](https://www.uniprot.org/uniprotkb/Q13835) (Plakophilin-1):

> A component of desmosome cell-cell junctions which are required for positive regulation of cellular adhesion. Plays a role in desmosome protein expression regulation and localization to the desmosomal plaque, thereby maintaining cell sheet integrity and anchorage of desmosomes to intermediate filaments. Required for localization of DSG3 and YAP1 to the cell membrane in keratinocytes in response to mechanical strain, via the formation of an interaction complex composed of DSG3, YAP1, PKP1 and …

**Summary**, from NCBI Gene [5317](https://www.ncbi.nlm.nih.gov/gene/5317):

> This gene encodes a member of the arm-repeat (armadillo) and plakophilin gene families. Plakophilin proteins contain numerous armadillo repeats, localize to cell desmosomes and nuclei, and participate in linking cadherins to intermediate filaments in the cytoskeleton. This protein may be involved in molecular recruitment and stabilization during desmosome formation. Mutations in this gene have been associated with the ectodermal dysplasia/skin fragility syndrome. Two transcript variants …

**Accessions** — [HGNC:9023](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9023) · Entrez [5317](https://www.ncbi.nlm.nih.gov/gene/5317) · UniProt [Q13835](https://www.uniprot.org/uniprotkb/Q13835) · Ensembl [ENSG00000081277](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000081277)

## Data

Gene col 1314: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1314); `tables/drug_effects.parquet` (28 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1314, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1314]; `tensor/DDL_lfc|DDL_z.npy` [1314]; `embed/gene_vectors.npy` [1314]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1314 or target_col == 1314). Every well: [[PKP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PKP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
