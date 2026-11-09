---
symbol: "ARL14"
type: "gene"
col: 11051
ensembl_id: "ENSG00000179674"
name: "ARF like GTPase 14"
location: "3q25.33"
module: 158
arm: "+"
pooled_cpm: 2.37
n_lines_expressing: 27
n_dd_up: 31
n_dd_down: 1
n_dd_up_clean: 17
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 6
direction_downstream: 14
tags: ["gene", "module/158"]
generated_by: "tahoemap"
---

# ARL14

*ARF like GTPase 14* — 3q25.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 31 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 18.2× (z +25.4, q 0e+00, up in 18 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.530× (z -4.0, q 0.041, down in 11 of 23 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 5 µM in 1 line (NCI-H23 0.0298×); [[Betamethasone dipropionate (drug)]] 0.05 µM in 1 line (HOP62 0.0396×); [[Budesonide (drug)]] 5 µM in 1 line (NCI-H1573 0.0795×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRKG2-AS1]] (+0.65, fdr 7e-06), [[ZNF702P]] (+0.63, fdr 7e-06), [[CDKN2B]] (+0.63, fdr 1e-05); moves opposite to [[NUDT21]] (-0.56, fdr 1e-05), [[RPA1]] (-0.56, fdr 1e-05), [[WDR5]] (-0.54, fdr 4e-05).
> It is in [[Module 158]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 14 go from it, the strongest it → [[SMAD3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 14 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 31 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11051.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **18.2×** | +25.4 | 0e+00 | 18/18 (LoVo, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **17.0×** | +17.5 | 0e+00 | 19/19 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **15.5×** | +16.3 | 0e+00 | 21/21 (HOP62, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **5.89×** | +11.0 | 9e-26 | 21/22 (KATO III, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.88×** | +9.4 | 6e-19 | 0/2 | all doses, flat | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **5.05×** | +9.2 | 2e-18 | 3/5 (CFPAC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **3.80×** | +8.2 | 1e-14 | 6/8 (PANC-1, SW1417, …) | all doses, flat | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.35×** | +7.4 | 8e-12 | 8/16 (NCI-H1573, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.25×** | +7.0 | 1e-10 | 15/21 (KATO III, SW1417, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~35% of this change | **2.52×** | +5.7 | 7e-07 | 0/8 | inconsistent across doses | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.88×** | +5.5 | 2e-06 | 9/22 (Panc 03.27, HOP62, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.28×** | +4.9 | 5e-05 | 3/12 (PANC-1, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **2.20×** | +4.8 | 6e-05 | 11/21 (KATO III, A-427, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | **2.12×** | +4.6 | 1e-04 | 6/15 (NCI-H1573, HOP62, …) | top dose only | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.95×** | +4.1 | 0.001 | 10/20 (KATO III, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.97×** | +4.0 | 0.002 | 5/16 (CFPAC-1, SW1417, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.88×** | +3.9 | 0.004 | 8/20 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.55×** | +3.8 | 0.005 | 6/21 (HOP62, HEC-1-A, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Pimozide (drug)]] 0.05 µM |  | **1.82×** | +3.7 | 0.007 | 2/14 (LS 180, NCI-H23) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.74×** | +3.3 | 0.030 | 0/17 | top dose only | cell-cycle shift (explains ~18% here) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.67×** | +3.2 | 0.040 | 0/14 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 11051.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, none with an alert; `tables/drug_line_top.parquet`), these lower it: [[Cobimetinib (drug)]] 5 µM in 1 line (NCI-H23 0.0298×); [[Betamethasone dipropionate (drug)]] 0.05 µM in 1 line (HOP62 0.0396×); [[Budesonide (drug)]] 5 µM in 1 line (NCI-H1573 0.0795×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.530×** | -4.0 | 0.041 | 11/23 (NCI-H1573, HOP62, …) | inconsistent across doses |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 0.587× | -3.3 | 0.24 | 9/23 (HOP62, SW 900, …) | rises with dose |  |
| [[Citalopram (hydrobromide) (drug)]] 0.05 µM |  | 0.602× | -3.2 | 0.26 | 7/23 (HOP62, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 0.705× | -3.1 | 0.26 | 8/23 (BT-474, Panc 03.27, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.18 per unit of S-phase module lfc, +0.63 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11051. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 5.99 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 48.6× (z +16.4) | [[Betamethasone dipropionate (drug)]] 0.05 µM 0.0396× (z -9.0) |
| [[KATO III (line)]] | alt | 8.00 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.0× (z +13.1) | — |
| [[NCI-H1573 (line)]] | alt | 5.83 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +13.0) | [[Budesonide (drug)]] 5 µM 0.0795× (z -8.8) |
| [[COLO 205 (line)]] | alt | 7.76 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 50.4× (z +14.0) | — |
| [[LoVo (line)]] | wt | 3.12 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 52.8× (z +17.6) | — |
| [[AsPC-1 (line)]] | alt | 3.21 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 75.1× (z +14.8) | — |
| [[CFPAC-1 (line)]] | alt | 4.43 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 28.7× (z +14.3) | — |
| [[SW1417 (line)]] | alt | 3.04 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.1× (z +11.2) | — |
| [[A549 (line)]] | wt | 0.685 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 40.7× (z +8.8) | — |
| [[BT-474 (line)]] | alt | 2.05 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 44.2× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 5.35 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 24.7× (z +13.6) | — |
| [[NCI-H23 (line)]] | alt | 30.4 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.0298× (z -14.3) |
| [[Panc 03.27 (line)]] | alt | 5.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +12.3) | — |
| [[PANC-1 (line)]] | alt | 1.53 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 18.6× (z +10.5) | — |
| [[A-172 (line)]] | wt | 0.586 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.321 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.477 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.327 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.356 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 0.348 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.431 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.653 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 0.380 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.499 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.403 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.436 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.11 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.289 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.458 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 3.03 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.613 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.389 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.307 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.358 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 0.485 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.292 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.504 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.363 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.781 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 0.858 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.779 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.05 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 0.508 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.522 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11051), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKG2-AS1]] | +0.65 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[ZNF702P]] | +0.63 | +0.67 / +0.60 | both halves | 7e-06 |  |
| [[CDKN2B]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[DIAPH2-AS1]] | +0.62 | +0.64 / +0.55 | both halves | 1e-05 |  |
| [[MSX2]] | +0.61 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[IL23A]] | +0.61 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[SFR1]] | +0.59 | +0.52 / +0.68 | both halves | 1e-05 |  |
| [[TRPV3]] | +0.59 | +0.60 / +0.48 | both halves | 2e-05 |  |
| [[ISG20]] | +0.59 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[IER3]] | +0.59 | +0.51 / +0.66 | both halves | 1e-05 |  |
| [[HDAC9]] | +0.58 | +0.47 / +0.59 | both halves | 2e-05 |  |
| [[KIAA1217]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NUDT21]] | -0.56 | -0.53 / -0.50 | both halves | 1e-05 |  |
| [[RPA1]] | -0.56 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[WDR5]] | -0.54 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[SRD5A1]] | -0.52 | -0.54 / -0.47 | both halves | 2e-05 |  |
| [[INPP5B]] | -0.52 | -0.39 / -0.59 | both halves | 5e-05 |  |
| [[GLB1]] | -0.51 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[CPD]] | -0.51 | -0.50 / -0.45 | both halves | 3e-05 |  |
| [[PMS2P3]] | -0.50 | -0.37 / -0.50 | both halves | 7e-05 |  |
| [[SDHAP1]] | -0.50 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[SMG1P5]] | -0.50 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[SDHAP4]] | -0.50 | -0.51 / -0.43 | both halves | 3e-05 |  |
| [[NTAQ1]] | -0.49 | -0.50 / -0.49 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 3, C 3.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ARL14's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.4% of all compounds | 0.053 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[KMO]] | B | KMO activity raises ARL14's level | lines that do not express KMO (18) vs lines expressing it (32) | 1.38× lower at baseline in the lines without KMO | 0.055 | ⚠ within organs, on part of the lines; co-occurs with ARID1A; also absent: SRPX2, IL1R1, TRIM6; maybe low, not absent |
| [[ZNF165]] | B | ZNF165 activity raises ARL14's level | lines that do not express ZNF165 (19) vs lines expressing it (31) | 1.90× lower at baseline in the lines without ZNF165 | 0.094 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: ENSG00000224621, ESRP2, CNKSR1 |
| [[GOLT1A]] | C | GOLT1A activity raises ARL14's level | lines that do not express GOLT1A (24) vs lines expressing it (26) | 1.99× lower at baseline in the lines without GOLT1A | 0.030 | ⚠ within organs, on part of the lines; also absent: GRB7, RHOV, ELF3; maybe low, not absent; co-absent with the target |
| [[SHH]] | C | SHH activity raises ARL14's level | lines that do not express SHH (29) vs lines expressing it (21) | 1.95× lower at baseline in the lines without SHH | 0.050 | ⚠ within organs, on part of the lines; also absent: KLK6, HSD17B2, EPS8L3; co-absent with the target |
| [[OVOL1]] | C | OVOL1 activity raises ARL14's level | lines that do not express OVOL1 (33) vs lines expressing it (17) | 2.11× lower at baseline in the lines without OVOL1 | 0.052 | ⚠ within organs, on part of the lines; co-absent genes; also absent: GRHL2, ST14, TMEM30B; co-absent with the target |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 11, C 3. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMAD3]] | B | ARL14 activity raises SMAD3's level | lines that do not express ARL14 (23) vs lines expressing it (27) | 1.99× lower at baseline in the lines without ARL14 | 0.005 | ⚠ within organs, on part of the lines; also absent: TMEM92, LIPH, AFAP1L2; maybe low, not absent |
| [[GAP43]] | B | ARL14 activity lowers GAP43's level | lines that do not express ARL14 (23) vs lines expressing it (27) | 2.01× higher at baseline in the lines without ARL14 | 0.009 | ⚠ within organs, on part of the lines; also absent: TMEM92, LIPH, AFAP1L2; maybe low, not absent |
| [[NUDT21]] | B | ARL14 activity lowers NUDT21's level | lines that do not express ARL14 (23) vs lines expressing it (27) | 1.27× higher at baseline in the lines without ARL14 | 0.011 | ⚠ within organs, on part of the lines; also absent: TMEM92, LIPH, AFAP1L2; maybe low, not absent |
| [[DIAPH2-AS1]] | B | ARL14 activity raises DIAPH2-AS1's level | lines that do not express ARL14 (23) vs lines expressing it (27) | 1.52× lower at baseline in the lines without ARL14 | 0.041 | ⚠ within organs, on part of the lines; also absent: TMEM92, LIPH, AFAP1L2; maybe low, not absent |
| [[ARRDC4]] | B | ARL14 activity raises ARRDC4's level | lines that do not express ARL14 (23) vs lines expressing it (27) | 1.56× lower at baseline in the lines without ARL14 | 0.058 | ⚠ within organs, on part of the lines; also absent: TMEM92, LIPH, AFAP1L2; maybe low, not absent |
| [[RPA1]] | B | ARL14 activity lowers RPA1's level | lines that do not express ARL14 (23) vs lines expressing it (27) | 1.21× higher at baseline in the lines without ARL14 | 0.075 | ⚠ within organs, on part of the lines; also absent: TMEM92, LIPH, AFAP1L2; maybe low, not absent |
| [[PIK3IP1-DT]] | B | ARL14 activity raises PIK3IP1-DT's level | lines that do not express ARL14 (23) vs lines expressing it (27) | 1.33× lower at baseline in the lines without ARL14 | 0.079 | ⚠ within organs, on part of the lines; also absent: TMEM92, LIPH, AFAP1L2; maybe low, not absent |
| [[MSX2]] | B | ARL14 activity raises MSX2's level | lines that do not express ARL14 (23) vs lines expressing it (27) | 1.69× lower at baseline in the lines without ARL14 | 0.085 | ⚠ within organs, on part of the lines; also absent: TMEM92, LIPH, AFAP1L2; maybe low, not absent |
| [[SMG1P5]] | B | ARL14 activity lowers SMG1P5's level | lines that do not express ARL14 (23) vs lines expressing it (27) | 1.17× higher at baseline in the lines without ARL14 | 0.087 | ⚠ within organs, on part of the lines; also absent: TMEM92, LIPH, AFAP1L2; maybe low, not absent |
| [[TUBB2A]] | B | ARL14 activity lowers TUBB2A's level | lines that do not express ARL14 (23) vs lines expressing it (27) | 1.29× higher at baseline in the lines without ARL14 | 0.087 | ⚠ within organs, on part of the lines; also absent: TMEM92, LIPH, AFAP1L2; maybe low, not absent |
| [[KIAA1217]] | B | ARL14 activity raises KIAA1217's level | lines that do not express ARL14 (23) vs lines expressing it (27) | 1.74× lower at baseline in the lines without ARL14 | 0.092 | ⚠ within organs, on part of the lines; also absent: TMEM92, LIPH, AFAP1L2; maybe low, not absent |
| [[C6orf141]] | C | ARL14 activity raises C6orf141's level | lines that do not express ARL14 (23) vs lines expressing it (27) | 2.80× lower at baseline in the lines without ARL14 | 0.016 | ⚠ within organs, on part of the lines; also absent: TMEM92, LIPH, AFAP1L2; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 158]]; 27 genes; every member is in the + arm (projection on the module's main direction 0.678). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.41; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.9, 3.8); signed map (6.6, 21.9). **Vector** length 60.4, 16.1% of its response variance represented; |z| ≥ 3 in 592 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM |  | +4.7 | +16.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +17.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +4.0 | +11.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.9 | +7.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.6 | +25.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.8 | +5.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.3 | +4.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.4 | +2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.3 | +1.0 |
| fall | [[Clobetasol propionate (drug)]] 5 µM |  | -1.7 | -3.3 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -1.7 | -4.0 |
|  | [[Budesonide (drug)]] 5 µM |  | -1.6 | -1.6 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -1.5 | -1.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -1.4 | +0.7 |

## What is on record

|  |  |
|---|---|
| Name | ARF like GTPase 14 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.33 — chr3:160,677,160-160,678,448 (+) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ22595; previously ARF7 |
| Gene groups (HGNC) | ARF GTPase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N4G2](https://www.uniprot.org/uniprotkb/Q8N4G2) (ADP-ribosylation factor-like protein 14):

> GTPase that recruits MYO1E to MHC class II-containing vesicles via the effector protein ARL14EP and hence controls the movement of these vesicles along the actin cytoskeleton in dendritic cells.

**Summary**, from NCBI Gene [80117](https://www.ncbi.nlm.nih.gov/gene/80117):

> Predicted to enable GTP binding activity. Predicted to be involved in intracellular protein transport and vesicle-mediated transport. Predicted to be located in cytoplasmic vesicle. Predicted to be active in cytoplasm and plasma membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:22974](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:22974) · Entrez [80117](https://www.ncbi.nlm.nih.gov/gene/80117) · UniProt [Q8N4G2](https://www.uniprot.org/uniprotkb/Q8N4G2) · Ensembl [ENSG00000179674](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179674)

## Data

Gene col 11051: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11051); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11051, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11051]; `tensor/DDL_lfc|DDL_z.npy` [11051]; `embed/gene_vectors.npy` [11051]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11051 or target_col == 11051). Every well: [[ARL14 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARL14.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
