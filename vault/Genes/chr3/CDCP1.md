---
symbol: "CDCP1"
type: "gene"
col: 8786
ensembl_id: "ENSG00000163814"
name: "CUB domain containing protein 1"
location: "3p21.31"
module: 34
arm: "+"
pooled_cpm: 256.09
n_lines_expressing: 34
n_dd_up: 5
n_dd_down: 73
n_dd_up_clean: 3
n_dd_down_clean: 60
in_vector_space: true
direction_upstream: 35
direction_downstream: 41
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# CDCP1

*CUB domain containing protein 1* — 3p21.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 5 µM: 1.33× (z +4.9, q 6e-04, up in 26 of 32 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Peretinoin (drug)]] 5 µM: 1.31× (z +4.5, q 0.002, up in 21 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 73 drug-doses (13 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.129× (z -49.2, q 0e+00, down in 32 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGA2]] (+0.85, fdr 7e-06), [[PLEK2]] (+0.77, fdr 7e-06), [[S100A16]] (+0.74, fdr 7e-06).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 35 arrows point to it, the strongest [[WNT7B]] → it (grade B ⚠); 41 go from it, the strongest it → [[SLCO4A1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8786.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.33×** | +4.9 | 6e-04 | 26/32 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.31×** | +4.5 | 0.002 | 21/32 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.29×** | +4.4 | 0.002 | 20/32 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.17× | +3.8 | 0.023 | 12/32 (HEC-1-A, KATO III, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.027 | 18/32 (SW48, LS 180, …) | two highest doses | low cells (technical?) |
| [[vincristine (drug)]] 0.5 µM |  | **1.34×** | +3.6 | 0.030 | 19/32 (MIA PaCa-2, HT-29, …) | all doses, flat | low cells (technical?); noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.15× | +3.5 | 0.040 | 13/33 (HT-29, MIA PaCa-2, …) | rises with dose |  |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 1.13× | +3.1 | 0.15 | 3/32 (NCI-H1792, A498, …) | inconsistent across doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | 1.19× | +3.0 | 0.15 | 16/32 (NCI-H460, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 83 in all, 15 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 73 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8786.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.129×** | -49.2 | 0e+00 | 32/32 (RPMI-7951, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.175×** | -29.5 | 0e+00 | 32/32 (NCI-H1792, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.295×** | -29.3 | 0e+00 | 33/33 (MIA PaCa-2, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.212×** | -26.3 | 0e+00 | 32/32 (HOP62, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.255×** | -22.3 | 0e+00 | 32/32 (RKO, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.300×** | -20.4 | 0e+00 | 32/32 (HOP62, A549, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.318×** | -19.4 | 0e+00 | 28/32 (RKO, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.410×** | -14.5 | 1e-45 | 32/32 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.416×** | -14.3 | 2e-44 | 31/32 (CFPAC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.542×** | -12.9 | 2e-36 | 28/32 (SW480, NCI-H460, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.560×** | -12.0 | 1e-31 | 29/32 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.494×** | -11.4 | 2e-28 | 31/34 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.613×** | -11.3 | 5e-28 | 29/33 (SW480, MIA PaCa-2, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.507×** | -11.0 | 1e-26 | 30/32 (SW480, NCI-H23, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | **0.527×** | -10.8 | 8e-26 | 28/33 (NCI-H1573, AsPC-1, …) | all doses, flat | composition shift |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.529×** | -10.8 | 2e-25 | 31/33 (SW480, NCI-H460, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.550×** | -10.6 | 7e-25 | 28/33 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.53 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8786. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 977 | 0 | 37 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0796× (z -43.5) |
| [[NCI-H23 (line)]] | alt | 220 | 0 | 31 (5 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.336× (z -30.5) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0714× (z -30.1) |
| [[MIA PaCa-2 (line)]] | alt | 204 | 0 | 27 (4 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.378× (z -34.3) ⚠ position not correctable · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.0970× (z -33.9) |
| [[NCI-H460 (line)]] | wt | 125 | 0 | 27 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -33.1) |
| [[SW480 (line)]] | alt | 229 | 0 | 25 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -32.2) |
| [[NCI-H1792 (line)]] | alt | 493 | 0 | 24 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0634× (z -40.5) |
| [[SW48 (line)]] | wt | 301 | 2 (1 ⚠) | 22 (3 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 3.18× (z +11.6) | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -27.2) |
| [[RKO (line)]] | wt | 207 | 0 | 21 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0764× (z -41.5) |
| [[PANC-1 (line)]] | alt | 288 | 0 | 20 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0802× (z -36.4) |
| [[NCI-H1573 (line)]] | alt | 475 | 0 | 18 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0681× (z -40.3) |
| [[HEC-1-A (line)]] | alt | 490 | 0 | 17 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -33.4) |
| [[J82 (line)]] | alt | 149 | 0 | 17 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0946× (z -35.7) |
| [[NCI-H2347 (line)]] | alt | 443 | 0 | 17 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -39.0) |
| [[SW 900 (line)]] | alt | 310 | 0 | 17 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -31.5) |
| [[A549 (line)]] | wt | 155 | 0 | 15 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0998× (z -29.5) |
| [[RPMI-7951 (line)]] | alt | 441 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0572× (z -45.0) |
| [[NCI-H2030 (line)]] | alt | 254 | 0 | 13 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0754× (z -36.8) |
| [[AsPC-1 (line)]] | alt | 556 | 0 | 11 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.180× (z -24.3) |
| [[CFPAC-1 (line)]] | alt | 495 | 0 | 11 (5 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.126× (z -29.0) |
| [[HCT15 (line)]] | alt | 245 | 0 | 11 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -23.7) |
| [[SNU-423 (line)]] | alt | 375 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -35.7) |
| [[HT-29 (line)]] | alt | 112 | 1 (1 ⚠) | 9 (2 ⚠) | [[Daptomycin (drug)]] 5 µM 2.38× (z +9.7) ⚠ unreliable plate only | [[Homoharringtonine (drug)]] 5 µM 0.253× (z -21.5) |
| [[LS 180 (line)]] | wt | 264 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -21.6) |
| [[Panc 03.27 (line)]] | alt | 435 | 0 | 10 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.277× (z -21.6) |
| [[A498 (line)]] | wt | 352 | 0 | 8 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -19.9) |
| [[LoVo (line)]] | wt | 160 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -34.2) |
| [[SW 1271 (line)]] | alt | 320 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0782× (z -22.6) |
| [[COLO 205 (line)]] | alt | 198 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -30.0) |
| [[KATO III (line)]] | alt | 175 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.161× (z -28.5) |
| [[SW1417 (line)]] | alt | 267 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -18.4) |
| [[Hs 766T (line)]] | wt | 207 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -23.1) |
| [[BT-474 (line)]] | alt | 91.3 | 0 | 3 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.296× (z -9.5) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.437× (z -9.5) |
| [[A-172 (line)]] | wt | 17.9 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 45.3 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 35.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 19.3 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 33.7 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 24.8 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 21.7 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 20.6 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 19.1 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.1 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 22.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 319 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 202 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 23.3 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 16.8 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 21.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 57.1 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 37.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8786), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGA2]] | +0.85 | +0.85 / +0.86 | both halves | 7e-06 | same gene group |
| [[PLEK2]] | +0.77 | +0.80 / +0.73 | both halves | 7e-06 |  |
| [[S100A16]] | +0.74 | +0.79 / +0.72 | both halves | 7e-06 |  |
| [[PLAUR]] | +0.71 | +0.74 / +0.68 | both halves | 7e-06 | same gene group |
| [[WNT7B]] | +0.71 | +0.70 / +0.68 | both halves | 7e-06 |  |
| [[ANTXR2]] | +0.71 | +0.75 / +0.76 | both halves | 7e-06 |  |
| [[SHB]] | +0.71 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[LAMC2]] | +0.70 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[CORO2B]] | +0.70 | +0.72 / +0.69 | both halves | 7e-06 |  |
| [[BMP6]] | +0.68 | +0.68 / +0.56 | both halves | 1e-05 |  |
| [[NTSR1]] | +0.68 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[NT5E]] | +0.67 | +0.75 / +0.67 | both halves | 7e-06 | same gene group; pathway: HALLMARK_IL2_STAT5_SIGNALING |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*35 arrows, 35 of them with an alert ⚠; grade A 0, B 27, C 8. Shown: the 12 strongest; 23 more arrows (23 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[WNT7B]] | B | WNT7B activity raises CDCP1's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 2.69× lower at baseline in the lines without WNT7B | 0.003 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[ADAM8]] | B | ADAM8 activity raises CDCP1's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 2.45× lower at baseline in the lines without ADAM8 | 0.006 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent |
| [[UPP1]] | B | UPP1 activity raises CDCP1's level | lines that do not express UPP1 (9) vs lines expressing it (41) | 2.94× lower at baseline in the lines without UPP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000230479, PPP1R18, EBI3; maybe low, not absent |
| [[SLCO4A1]] | B | SLCO4A1 activity raises CDCP1's level | lines that do not express SLCO4A1 (9) vs lines expressing it (41) | 4.85× lower at baseline in the lines without SLCO4A1 | 0.007 | ⚠ within organs, on part of the lines; also absent: OCIAD2, GPRC5A; maybe low, not absent |
| [[ARHGEF4]] | B | ARHGEF4 activity raises CDCP1's level | lines that do not express ARHGEF4 (15) vs lines expressing it (35) | 3.90× lower at baseline in the lines without ARHGEF4 | 0.009 | ⚠ within organs, on part of the lines; also absent: GALNT12, RBM47, NR2E3 |
| [[THBD]] | B | THBD activity raises CDCP1's level | lines that do not express THBD (28) vs lines expressing it (22) | 3.00× lower at baseline in the lines without THBD | 0.015 | ⚠ within organs, on part of the lines; also absent: EFEMP1, KRT7, LINC02742 |
| [[HRH1]] | B | HRH1 activity raises CDCP1's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 4.80× lower at baseline in the lines without HRH1 | 0.018 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[SMOX]] | B | SMOX activity raises CDCP1's level | lines that do not express SMOX (6) vs lines expressing it (44) | 3.65× lower at baseline in the lines without SMOX | 0.018 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |
| [[SLC35F3]] | B | SLC35F3 activity raises CDCP1's level | lines that do not express SLC35F3 (27) vs lines expressing it (23) | 3.46× lower at baseline in the lines without SLC35F3 | 0.021 | ⚠ within organs, on part of the lines; also absent: RHCG, THBD, NR2E3 |
| [[CELSR1]] | B | CELSR1 activity raises CDCP1's level | lines that do not express CELSR1 (7) vs lines expressing it (43) | 2.75× lower at baseline in the lines without CELSR1 | 0.021 | ⚠ within organs, on part of the lines; also absent: ST6GALNAC2, PORCN, WNT9A |
| [[TMEM154]] | B | TMEM154 activity raises CDCP1's level | lines that do not express TMEM154 (26) vs lines expressing it (24) | 2.23× lower at baseline in the lines without TMEM154 | 0.023 | ⚠ within organs, on part of the lines; also absent: ENSG00000287003, SYNPR-AS1, MMP13 |
| [[ALDH3B1]] | B | ALDH3B1 activity raises CDCP1's level | lines that do not express ALDH3B1 (9) vs lines expressing it (41) | 4.25× lower at baseline in the lines without ALDH3B1 | 0.024 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |

### Downstream of this gene

*41 arrows, 41 of them with an alert ⚠; grade A 0, B 36, C 5. Shown: the 12 strongest; 29 more arrows (29 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLCO4A1]] | B | CDCP1 activity raises SLCO4A1's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 3.16× lower at baseline in the lines without CDCP1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[SEMA4B]] | B | CDCP1 activity raises SEMA4B's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 2.39× lower at baseline in the lines without CDCP1 | 0.005 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[EHD1]] | B | CDCP1 activity raises EHD1's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 1.78× lower at baseline in the lines without CDCP1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[REV3L]] | B | CDCP1 activity lowers REV3L's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 1.99× higher at baseline in the lines without CDCP1 | 0.010 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[SLC35F3]] | B | CDCP1 activity raises SLC35F3's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 3.08× lower at baseline in the lines without CDCP1 | 0.013 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[S100A11]] | B | CDCP1 activity raises S100A11's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 1.97× lower at baseline in the lines without CDCP1 | 0.014 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[WNT7B]] | B | CDCP1 activity raises WNT7B's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 3.00× lower at baseline in the lines without CDCP1 | 0.016 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[THSD4]] | B | CDCP1 activity raises THSD4's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 2.82× lower at baseline in the lines without CDCP1 | 0.016 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[ALDH3B1]] | B | CDCP1 activity raises ALDH3B1's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 2.20× lower at baseline in the lines without CDCP1 | 0.016 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[BCAR3]] | B | CDCP1 activity raises BCAR3's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 1.89× lower at baseline in the lines without CDCP1 | 0.017 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[S100A16]] | B | CDCP1 activity raises S100A16's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 2.48× lower at baseline in the lines without CDCP1 | 0.017 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[SHB]] | B | CDCP1 activity raises SHB's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 1.97× lower at baseline in the lines without CDCP1 | 0.021 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.810). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.3, 2.7); signed map (2.2, 45.7). **Vector** length 138, 56.0% of its response variance represented; |z| ≥ 3 in 2,055 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +7.0 | -26.3 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.6 | -20.4 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.5 | -29.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | -1.1 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +4.7 | +4.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.4 | +4.5 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +3.6 | +3.5 |
|  | [[Belzutifan (drug)]] 5 µM |  | +3.4 | +2.0 |
|  | [[vincristine (drug)]] 0.5 µM |  | +3.4 | +3.6 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -9.8 | -12.9 |
|  | [[Trametinib (drug)]] 5 µM |  | -9.8 | -11.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | -8.8 | -10.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -8.6 | -10.8 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -8.2 | -12.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -8.1 | -11.0 |

## What is on record

|  |  |
|---|---|
| Name | CUB domain containing protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3p21.31 — chr3:45,082,277-45,146,422 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CD318, SIMA135 |
| Gene groups (HGNC) | CD molecules |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H5V8](https://www.uniprot.org/uniprotkb/Q9H5V8) (CUB domain-containing protein 1):

> May be involved in cell adhesion and cell matrix association. May play a role in the regulation of anchorage versus migration or proliferation versus differentiation via its phosphorylation. May be a novel marker for leukemia diagnosis and for immature hematopoietic stem cell subsets. Belongs to the tetraspanin web involved in tumor progression and metastasis.

**Summary**, from NCBI Gene [64866](https://www.ncbi.nlm.nih.gov/gene/64866):

> This gene encodes a transmembrane protein which contains three extracellular CUB domains and acts as a substrate for Src family kinases. The protein plays a role in the tyrosine phosphorylation-dependent regulation of cellular events that are involved in tumor invasion and metastasis. Alternative splicing results in multiple transcript variants of this gene. [provided by RefSeq, May 2013]

**Accessions** — [HGNC:24357](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24357) · Entrez [64866](https://www.ncbi.nlm.nih.gov/gene/64866) · UniProt [Q9H5V8](https://www.uniprot.org/uniprotkb/Q9H5V8) · Ensembl [ENSG00000163814](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000163814)

## Data

Gene col 8786: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8786); `tables/drug_effects.parquet` (92 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8786, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8786]; `tensor/DDL_lfc|DDL_z.npy` [8786]; `embed/gene_vectors.npy` [8786]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8786 or target_col == 8786). Every well: [[CDCP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CDCP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
