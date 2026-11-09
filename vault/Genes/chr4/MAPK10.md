---
symbol: "MAPK10"
type: "gene"
col: 3046
ensembl_id: "ENSG00000109339"
name: "mitogen-activated protein kinase 10"
location: "4q21.3"
module: 9
arm: "+"
pooled_cpm: 16.6
n_lines_expressing: 39
n_dd_up: 38
n_dd_down: 20
n_dd_up_clean: 33
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 12
direction_downstream: 5
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# MAPK10

*mitogen-activated protein kinase 10* — 4q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.66× (z +14.3, q 1e-43, up in 27 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (4 with an alert ⚠); the strongest is [[Vinblastine (sulfate) (drug)]] 5 µM: 0.656× (z -6.2, q 3e-07, down in 28 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDH8]] (+0.69, fdr 7e-06), [[RALYL]] (+0.67, fdr 7e-06), [[PCDH18]] (+0.66, fdr 1e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[AUTS2]] → it (grade B ⚠); 5 go from it, the strongest it → [[MEF2C-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3046.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.66×** | +14.3 | 1e-43 | 27/33 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.01×** | +10.2 | 7e-22 | 27/36 (A-172, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **2.19×** | +8.1 | 1e-13 | 30/37 (NCI-H23, A-172, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.18×** | +8.1 | 1e-13 | 26/35 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.95×** | +6.9 | 5e-10 | 27/35 (NCI-H23, HEC-1-A, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **1.93×** | +6.8 | 1e-09 | 23/37 (A498, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.89×** | +6.6 | 4e-09 | 22/36 (A498, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.57×** | +6.6 | 4e-09 | 23/37 (A-427, LOX-IMVI, …) | rises with dose | low cells (technical?) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.93×** | +6.5 | 4e-09 | 26/35 (HEC-1-A, NCI-H23, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.56×** | +6.5 | 5e-09 | 18/37 (A-172, HEC-1-A, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.83×** | +6.3 | 2e-08 | 9/30 (NCI-H1573, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.81×** | +6.1 | 5e-08 | 24/35 (NCI-H23, LoVo, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.75×** | +5.8 | 3e-07 | 17/36 (NCI-H2347, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.79×** | +5.8 | 3e-07 | 22/35 (HEC-1-A, A498, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.47×** | +5.6 | 7e-07 | 13/32 (C-33 A, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Brivudine (drug)]] 5 µM |  | **2.71×** | +5.4 | 2e-06 | 21/36 (LoVo, NCI-H23, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.67×** | +5.1 | 1e-05 | 13/35 (HEC-1-A, LoVo, …) | top dose only | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3046.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.656×** | -6.2 | 3e-07 | 28/36 (CHP-212, H4, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.582×** | -5.6 | 4e-06 | 20/35 (LoVo, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.583×** | -5.6 | 4e-06 | 21/36 (LoVo, Hs 766T, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.609×** | -5.2 | 4e-05 | 23/35 (LoVo, CHP-212, …) | rises with dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.637×** | -4.7 | 3e-04 | 22/35 (H4, Panc 03.27, …) | rises with dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.628×** | -4.6 | 3e-04 | 19/35 (LoVo, A-427, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.640×** | -4.6 | 3e-04 | 23/34 (LoVo, A549, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.646×** | -4.5 | 4e-04 | 18/35 (SHP-77, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.654×** | -4.4 | 6e-04 | 16/37 (LoVo, SHP-77, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.676×** | -4.1 | 0.003 | 14/35 (LOX-IMVI, H4, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.680×** | -4.0 | 0.003 | 14/37 (AN3 CA, PANC-1, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.683×** | -4.0 | 0.003 | 16/35 (SHP-77, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **0.792×** | -3.4 | 0.025 | 9/36 (LoVo, HEC-1-A, …) | top dose only | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.720×** | -3.4 | 0.025 | 14/35 (H4, LoVo, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.570×** | -3.1 | 0.085 | 12/35 (LoVo, SHP-77, …) | rises with dose | noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **0.576×** | -3.0 | 0.086 | 16/33 (Hs 766T, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.742×** | -3.0 | 0.086 | 14/36 (NCI-H460, H4, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.750×** | -3.0 | 0.086 | 10/35 (LOX-IMVI, CHP-212, …) | rises with dose | position effect removed |
| [[vincristine (drug)]] 0.05 µM |  | **0.739×** | -3.0 | 0.087 | 9/35 (A-427, SK-MEL-2, …) | all doses, flat |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.37 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3046. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LoVo (line)]] | wt | 51.1 | 0 | 10 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.197× (z -12.0) |
| [[CHP-212 (line)]] | wt | 292 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0534× (z -13.7) ⚠ toxic; transcription drop · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.209× (z -10.8) |
| [[SHP-77 (line)]] | alt | 144 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.208× (z -13.2) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.333× (z -13.1) |
| [[Hs 766T (line)]] | wt | 82.3 | 0 | 4 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.129× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 34.6 | 0 | 2 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0390× (z -12.7) ⚠ unreliable plate only · without an alert: [[Vinblastine (sulfate) (drug)]] 5 µM 0.180× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 21.2 | 1 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 2.23× (z +12.1) ⚠ position not correctable | [[Niclosamide (olamine) (drug)]] 5 µM 0.122× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~28% of this change |
| [[A-172 (line)]] | wt | 9.12 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 7.06× (z +8.5) | — |
| [[A-427 (line)]] | wt | 8.20 | 1 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 5.21× (z +9.0) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A498 (line)]] | wt | 30.0 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.59× (z +8.5) | — |
| [[HEC-1-A (line)]] | alt | 12.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.22× (z +11.8) | — |
| [[NCI-H460 (line)]] | wt | 4.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.11× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 7.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.32× (z +8.5) | — |
| [[A549 (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 59.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.27 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.59 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.55 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 7.41 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 5.93 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.42 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.24 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.09 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.54 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.72 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.44 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.00 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.72 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3046), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDH8]] | +0.69 | +0.59 / +0.69 | both halves | 7e-06 |  |
| [[RALYL]] | +0.67 | +0.72 / +0.58 | both halves | 7e-06 |  |
| [[PCDH18]] | +0.66 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[SCN2A]] | +0.65 | +0.57 / +0.59 | both halves | 1e-05 |  |
| [[GPM6A]] | +0.65 | +0.68 / +0.57 | both halves | 1e-05 |  |
| [[BRINP3]] | +0.65 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[PEX5L]] | +0.64 | +0.64 / +0.57 | both halves | 9e-06 |  |
| [[CDH12]] | +0.64 | +0.64 / +0.56 | both halves | 1e-05 |  |
| [[DMD]] | +0.64 | +0.65 / +0.62 | both halves | 7e-06 | same gene group |
| [[EPHA5-AS1]] | +0.64 | +0.67 / +0.55 | both halves | 1e-05 |  |
| [[SEMA3E]] | +0.63 | +0.61 / +0.57 | both halves | 8e-06 |  |
| [[CDH10]] | +0.63 | +0.59 / +0.63 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 11, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AUTS2]] | B | AUTS2 activity raises MAPK10's level | lines that do not express AUTS2 (18) vs lines expressing it (32) | 2.15× lower at baseline in the lines without AUTS2 | 0.043 | ⚠ within organs, on part of the lines; also absent: ZMAT4, KCNJ6, ENSG00000249111 |
| [[TOP2A]] | B | TOP2A activity lowers MAPK10's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ANGPT1]] | B | ANGPT1 activity raises MAPK10's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 2.60× lower at baseline in the lines without ANGPT1 | 0.045 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5 |
| [[GUCY1A1]] | B | GUCY1A1 activity raises MAPK10's level | lines that do not express GUCY1A1 (30) vs lines expressing it (20) | 2.54× lower at baseline in the lines without GUCY1A1 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FUT9, TLL1, LINC03046 |
| [[SLITRK6]] | B | SLITRK6 activity raises MAPK10's level | lines that do not express SLITRK6 (28) vs lines expressing it (22) | 2.40× lower at baseline in the lines without SLITRK6 | 0.070 | ⚠ within organs, on part of the lines; also absent: ENSG00000288098, ENSG00000259692, TENM4 |
| [[SYT4]] | B | SYT4 activity raises MAPK10's level | lines that do not express SYT4 (44) vs lines expressing it (6) | 4.44× lower at baseline in the lines without SYT4 | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CALCA, ENSG00000232252, CGA |
| [[NPAS3]] | B | NPAS3 activity raises MAPK10's level | lines that do not express NPAS3 (16) vs lines expressing it (34) | 2.40× lower at baseline in the lines without NPAS3 | 0.072 | ⚠ within organs, on part of the lines; also absent: SLC2A14, MARK1, CAMK4; maybe low, not absent |
| [[CDH12]] | B | CDH12 activity raises MAPK10's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 2.66× lower at baseline in the lines without CDH12 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent |
| [[PLXDC2]] | B | PLXDC2 activity raises MAPK10's level | lines that do not express PLXDC2 (24) vs lines expressing it (26) | 1.96× lower at baseline in the lines without PLXDC2 | 0.078 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ADAMTS2, ZNF667, ENSG00000248837; maybe low, not absent |
| [[BRINP3]] | B | BRINP3 activity raises MAPK10's level | lines that do not express BRINP3 (32) vs lines expressing it (18) | 2.41× lower at baseline in the lines without BRINP3 | 0.079 | ⚠ within organs, on part of the lines; also absent: CADM2, MMRN1, NETO1; maybe low, not absent |
| [[ANKRD30A]] | B | ANKRD30A activity raises MAPK10's level | lines that do not express ANKRD30A (37) vs lines expressing it (13) | 3.03× lower at baseline in the lines without ANKRD30A | 0.085 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC00993, ENSG00000232252, ASCL1 |
| [[PTPN13]] | C | PTPN13 activity raises MAPK10's level | lines that do not express PTPN13 (10) vs lines expressing it (40) | 4.07× lower at baseline in the lines without PTPN13 | 0.011 | ⚠ within organs, on part of the lines; also absent: MAPK10, AGPAT4, ENSG00000236230; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEF2C-AS1]] | B | MAPK10 activity raises MEF2C-AS1's level | lines that do not express MAPK10 (11) vs lines expressing it (39) | 3.97× lower at baseline in the lines without MAPK10 | 0.025 | ⚠ within organs, on part of the lines; also absent: PTPN13, HDGFL3, EML1; maybe low, not absent |
| [[KCNT2]] | B | MAPK10 activity raises KCNT2's level | lines that do not express MAPK10 (11) vs lines expressing it (39) | 3.51× lower at baseline in the lines without MAPK10 | 0.061 | ⚠ within organs, on part of the lines; also absent: PTPN13, HDGFL3, EML1; maybe low, not absent |
| [[ANGPT1]] | B | MAPK10 activity raises ANGPT1's level | lines that do not express MAPK10 (11) vs lines expressing it (39) | 3.71× lower at baseline in the lines without MAPK10 | 0.082 | ⚠ within organs, on part of the lines; also absent: PTPN13, HDGFL3, EML1; maybe low, not absent |
| [[SEMA3E]] | B | MAPK10 activity raises SEMA3E's level | lines that do not express MAPK10 (11) vs lines expressing it (39) | 3.23× lower at baseline in the lines without MAPK10 | 0.095 | ⚠ within organs, on part of the lines; also absent: PTPN13, HDGFL3, EML1; maybe low, not absent |
| [[PTPN13]] | C | MAPK10 activity raises PTPN13's level | lines that do not express MAPK10 (11) vs lines expressing it (39) | 5.63× lower at baseline in the lines without MAPK10 | 0.006 | ⚠ within organs, on part of the lines; also absent: PTPN13, HDGFL3, EML1; maybe low, not absent; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.751). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (36.6, 32.1); signed map (41.1, 33.0). **Vector** length 88.0, 22.5% of its response variance represented; |z| ≥ 3 in 1,024 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.4 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +9.4 | +6.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.8 | +14.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.6 | +4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +7.1 | +10.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.3 | +6.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.9 | +6.5 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.4 | +4.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.2 | +4.5 |
| fall | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -3.1 | -5.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.9 | -6.2 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -2.9 | -4.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.9 | -4.6 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.8 | -3.0 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.7 | -4.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.5 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q21.3 — chr4:85,990,007-86,594,625 (-) |
| Ensembl biotype | protein_coding |
| Also known as | JNK3, p493F12, p54bSAPK; previously PRKM10 |
| Gene groups (HGNC) | MicroRNA protein coding host genes; Mitogen-activated protein kinase 8-10 (JNK) family |
| Hallmark sets | PI3K_AKT_MTOR_SIGNALING |
| Reactome | 30 pathways, smallest: Activation of the AP-1 family of transcription factors; JNK (c-Jun kinases) phosphorylation and  activation mediated by activated human TAK1; FCERI mediated MAPK activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P53779](https://www.uniprot.org/uniprotkb/P53779) (Mitogen-activated protein kinase 10):

> Serine/threonine-protein kinase involved in various processes such as neuronal proliferation, differentiation, migration and programmed cell death. Extracellular stimuli such as pro-inflammatory cytokines or physical stress stimulate the stress-activated protein kinase/c-Jun N-terminal kinase (SAP/JNK) signaling pathway. In this cascade, two dual specificity kinases MAP2K4/MKK4 and MAP2K7/MKK7 phosphorylate and activate MAPK10/JNK3. In turn, MAPK10/JNK3 phosphorylates a number of transcription …

**Summary**, from NCBI Gene [5602](https://www.ncbi.nlm.nih.gov/gene/5602):

> The protein encoded by this gene is a member of the MAP kinase family. MAP kinases act as integration points for multiple biochemical signals, and thus are involved in a wide variety of cellular processes, such as proliferation, differentiation, transcription regulation and development. This kinase is specifically expressed in a subset of neurons in the nervous system, and is activated by threonine and tyrosine phosphorylation. Targeted deletion of this gene in mice suggests that it may have a …

**Accessions** — [HGNC:6872](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6872) · Entrez [5602](https://www.ncbi.nlm.nih.gov/gene/5602) · UniProt [P53779](https://www.uniprot.org/uniprotkb/P53779) · Ensembl [ENSG00000109339](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000109339)

## Data

Gene col 3046: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3046); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3046, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3046]; `tensor/DDL_lfc|DDL_z.npy` [3046]; `embed/gene_vectors.npy` [3046]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3046 or target_col == 3046). Every well: [[MAPK10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAPK10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
