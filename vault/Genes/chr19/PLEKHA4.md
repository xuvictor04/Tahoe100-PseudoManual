---
symbol: "PLEKHA4"
type: "gene"
col: 2620
ensembl_id: "ENSG00000105559"
name: "pleckstrin homology domain containing A4"
location: "19q13.33"
module: 32
arm: "+"
pooled_cpm: 61.76
n_lines_expressing: 43
n_dd_up: 8
n_dd_down: 28
n_dd_up_clean: 6
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 9
direction_downstream: 1
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# PLEKHA4

*pleckstrin homology domain containing A4* — 19q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.55× (z +14.0, q 6e-42, up in 37 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.354× (z -11.0, q 3e-25, down in 39 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFIH1]] (+0.83, fdr 7e-06), [[RIGI]] (+0.80, fdr 7e-06), [[HLA-F]] (+0.80, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[UBA7]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ELF1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2620.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.55×** | +14.0 | 6e-42 | 37/41 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **3.21×** | +11.9 | 5e-30 | 36/41 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +6.9 | 8e-10 | 25/41 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.86×** | +6.6 | 7e-09 | 27/41 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.19× | +6.0 | 2e-07 | 18/42 (MIA PaCa-2, HEC-1-A, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.57×** | +4.8 | 1e-04 | 24/41 (NCI-H460, PANC-1, …) | top dose only | cell-cycle shift (explains ~20% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.36×** | +4.6 | 4e-04 | 22/42 (AsPC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~24% of this change | **1.37×** | +3.3 | 0.060 | 18/41 (HS-578T, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.36×** | +3.3 | 0.062 | 20/41 (NCI-H460, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2620.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.354×** | -11.0 | 3e-25 | 39/41 (CFPAC-1, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.509×** | -10.1 | 1e-21 | 32/42 (RPMI-7951, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.398×** | -9.8 | 3e-20 | 40/41 (COLO 205, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.418×** | -9.2 | 4e-18 | 39/41 (CFPAC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.462×** | -8.2 | 4e-14 | 33/42 (NCI-H1792, SNU-423, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.520×** | -6.9 | 4e-10 | 35/41 (HS-578T, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.654×** | -6.4 | 2e-08 | 29/42 (MIA PaCa-2, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.556×** | -6.2 | 4e-08 | 30/42 (HS-578T, RPMI-7951, …) | top dose only | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.549×** | -6.0 | 1e-07 | 32/41 (MIA PaCa-2, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.583×** | -5.7 | 7e-07 | 27/41 (NCI-H1792, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.687×** | -5.6 | 1e-06 | 35/42 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.604×** | -5.3 | 5e-06 | 29/41 (BT-474, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.420×** | -4.8 | 7e-05 | 30/42 (NCI-H1792, HS-578T, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.726×** | -4.8 | 7e-05 | 26/41 (BT-474, NCI-H1792, …) | rises with dose | low cells (technical?) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.660×** | -4.4 | 4e-04 | 25/41 (MIA PaCa-2, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.662×** | -4.4 | 5e-04 | 32/41 (NCI-H23, CFPAC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.10 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2620. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 169 | 4 | 7 | [[Homoharringtonine (drug)]] 5 µM 2.79× (z +12.0) | [[Belinostat (drug)]] 5 µM 0.196× (z -13.4) |
| [[NCI-H460 (line)]] | wt | 21.5 | 10 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 21.0× (z +28.1) | — |
| [[A-172 (line)]] | wt | 85.9 | 4 | 5 | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +11.1) | [[Panobinostat (drug)]] 5 µM 0.246× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 296 | 0 | 9 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.259× (z -13.6) |
| [[RPMI-7951 (line)]] | alt | 247 | 0 | 9 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.282× (z -13.8) |
| [[SNU-423 (line)]] | alt | 81.3 | 1 | 8 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +12.5) | [[Panobinostat (drug)]] 5 µM 0.150× (z -13.4) |
| [[NCI-H1792 (line)]] | alt | 45.8 | 0 | 7 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.233× (z -11.3) |
| [[CFPAC-1 (line)]] | alt | 104 | 1 | 5 | [[Homoharringtonine (drug)]] 5 µM 4.11× (z +15.9) | [[Panobinostat (drug)]] 5 µM 0.141× (z -15.5) |
| [[HEC-1-A (line)]] | alt | 112 | 5 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.94× (z +24.2) | — |
| [[AsPC-1 (line)]] | alt | 67.7 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 4.93× (z +16.4) | [[Tofacitinib (drug)]] 5 µM 0.380× (z -9.8) |
| [[COLO 205 (line)]] | alt | 69.3 | 1 | 3 | [[Harringtonine (drug)]] 5 µM 5.53× (z +9.4) | [[Belinostat (drug)]] 5 µM 0.0919× (z -13.6) |
| [[LS 180 (line)]] | wt | 38.7 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 7.66× (z +19.1) | — |
| [[NCI-H2347 (line)]] | alt | 60.9 | 0 | 4 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.357× (z -9.8) |
| [[SK-MEL-2 (line)]] | alt | 95.2 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 7.32× (z +21.3) | [[Tofacitinib (drug)]] 5 µM 0.405× (z -9.6) |
| [[BT-474 (line)]] | alt | 39.9 | 0 | 3 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.131× (z -12.4) ⚠ cell-cycle shift, explains ~22% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.0956× (z -10.1) |
| [[Hs 766T (line)]] | wt | 77.2 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.87× (z +17.1) | — |
| [[hTERT-HPNE (line)]] | wt | 40.7 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +19.7) | — |
| [[NCI-H1573 (line)]] | alt | 21.6 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.37× (z +9.5) | [[Belinostat (drug)]] 5 µM 0.178× (z -9.6) |
| [[PANC-1 (line)]] | alt | 18.0 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.98× (z +21.7) | — |
| [[HOP62 (line)]] | alt | 17.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +20.1) | — |
| [[Panc 03.27 (line)]] | alt | 41.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +16.4) | — |
| [[SW 900 (line)]] | alt | 27.3 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.48× (z +13.5) | — |
| [[C32 (line)]] | wt | 88.8 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.387× (z -8.8) |
| [[H4 (line)]] | wt | 64.4 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.00× (z +15.1) | — |
| [[HCT15 (line)]] | alt | 119 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.47× (z +9.8) | — |
| [[HT-29 (line)]] | alt | 40.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +11.1) | — |
| [[NCI-H23 (line)]] | alt | 24.4 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.155× (z -9.4) |
| [[SW480 (line)]] | alt | 73.5 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.400× (z -8.7) |
| [[A-427 (line)]] | wt | 11.7 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 35.4 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 36.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 117 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 122 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 60.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.9 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 8.35 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 10.3 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.32 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 58.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 26.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 85.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 46.0 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 201 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 73.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.7 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 88.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.80 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2620), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFIH1]] | +0.83 | +0.77 / +0.84 | both halves | 7e-06 |  |
| [[RIGI]] | +0.80 | +0.75 / +0.83 | both halves | 7e-06 |  |
| [[HLA-F]] | +0.80 | +0.73 / +0.79 | both halves | 7e-06 |  |
| [[USP18]] | +0.80 | +0.69 / +0.85 | both halves | 7e-06 |  |
| [[PARP14]] | +0.79 | +0.71 / +0.80 | both halves | 7e-06 |  |
| [[PARP10]] | +0.79 | +0.70 / +0.80 | both halves | 7e-06 |  |
| [[PARP9]] | +0.78 | +0.68 / +0.83 | both halves | 7e-06 |  |
| [[DDX60L]] | +0.78 | +0.68 / +0.78 | both halves | 7e-06 |  |
| [[BATF2]] | +0.78 | +0.69 / +0.84 | both halves | 7e-06 |  |
| [[IRF9]] | +0.78 | +0.67 / +0.83 | both halves | 7e-06 |  |
| [[TRIM5]] | +0.78 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[SLC15A3]] | +0.78 | +0.62 / +0.81 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[UBA7]] | B | UBA7 activity raises PLEKHA4's level | lines that do not express UBA7 (9) vs lines expressing it (41) | 2.97× lower at baseline in the lines without UBA7 | 0.027 | ⚠ within organs, on part of the lines; also absent: XAF1, SH3TC1, SLC15A3; maybe low, not absent |
| [[RASGRP3]] | B | RASGRP3 activity raises PLEKHA4's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 2.22× lower at baseline in the lines without RASGRP3 | 0.036 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[IFITM1]] | B | IFITM1 activity raises PLEKHA4's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 2.20× lower at baseline in the lines without IFITM1 | 0.041 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[TRIM22]] | B | TRIM22 activity raises PLEKHA4's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.02× lower at baseline in the lines without TRIM22 | 0.045 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[IFI6]] | B | IFI6 activity raises PLEKHA4's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 1.96× lower at baseline in the lines without IFI6 | 0.049 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[JAK2]] | B | JAK2 activity raises PLEKHA4's level | compounds that target JAK2: 3 of 3 lower it (Fedratinib, Filgotinib, Tofacitinib) | 100% of the class's compounds vs 4.8% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds |
| [[OAS1]] | B | OAS1 activity raises PLEKHA4's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.72× lower at baseline in the lines without OAS1 | 0.078 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[IFITM2]] | B | IFITM2 activity raises PLEKHA4's level | lines that do not express IFITM2 (14) vs lines expressing it (36) | 1.69× lower at baseline in the lines without IFITM2 | 0.087 | ⚠ within organs, on part of the lines; co-absent genes; co-occurs with SMARCA4; also absent: CASP10, MX2, MAFB |
| [[SAMD9L]] | B | SAMD9L activity raises PLEKHA4's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 1.84× lower at baseline in the lines without SAMD9L | 0.088 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ELF1]] | B | PLEKHA4 activity strengthens ELF1's drug response | lines that do not express PLEKHA4 (7) vs lines expressing it (43) | the lines without PLEKHA4 respond 0.62× as strongly (z diff +2.46); strongest at Panobinostat 5 µM: 0.89x vs 0.48x (z diff +6.7) | 0.087 | ⚠ within organs, on part of the lines; maybe low, not absent; artifact flags |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.811). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.2, 51.7); signed map (64.2, 29.5). **Vector** length 151, 50.5% of its response variance represented; |z| ≥ 3 in 1,270 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.66 to 56); *interferon gamma response* (hallmark, mean cos +0.67 to 60); *interferon* (control, mean cos +0.74 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.0 | +14.0 |
|  | [[Harringtonine (drug)]] 5 µM |  | +8.7 | +11.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.9 | +6.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.4 | +4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.4 | +1.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.5 | +2.5 |
|  | [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | +3.1 | +2.2 |
|  | [[Docetaxel (drug)]] 5 µM |  | +2.9 | +3.0 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +2.8 | +1.7 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -7.8 | -10.1 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -7.4 | -8.2 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -6.2 | -6.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -6.0 | -6.4 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -5.9 | -5.7 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology domain containing A4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.33 — chr19:48,837,092-48,868,617 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PEPP1 |
| Gene groups (HGNC) | Pleckstrin homology domain containing |
| Reactome | 4 pathways, smallest: Synthesis of PIPs at the plasma membrane; PI Metabolism; Phospholipid metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4M7](https://www.uniprot.org/uniprotkb/Q9H4M7) (Pleckstrin homology domain-containing family A member 4):

> Binds specifically to phosphatidylinositol 3-phosphate (PtdIns3P), but not to other phosphoinositides.

**Summary**, from NCBI Gene [57664](https://www.ncbi.nlm.nih.gov/gene/57664):

> This gene encodes a pleckstrin homology (PH) domain-containing protein. The PH domain is found near the N-terminus and contains a putative phosphatidylinositol 3, 4, 5-triphosphate-binding motif (PPBM). Elevated expression of this gene has been observed in some melanomas. Alternate splicing results in multiple transcript variants encoding different isoforms. [provided by RefSeq, May 2017]

**Accessions** — [HGNC:14339](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14339) · Entrez [57664](https://www.ncbi.nlm.nih.gov/gene/57664) · UniProt [Q9H4M7](https://www.uniprot.org/uniprotkb/Q9H4M7) · Ensembl [ENSG00000105559](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000105559)

## Data

Gene col 2620: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2620); `tables/drug_effects.parquet` (37 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2620, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2620]; `tensor/DDL_lfc|DDL_z.npy` [2620]; `embed/gene_vectors.npy` [2620]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2620 or target_col == 2620). Every well: [[PLEKHA4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHA4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
