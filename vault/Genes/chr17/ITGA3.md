---
symbol: "ITGA3"
type: "gene"
col: 91
ensembl_id: "ENSG00000005884"
name: "integrin subunit alpha 3"
location: "17q21.33"
module: 78
arm: "+"
pooled_cpm: 253.23
n_lines_expressing: 40
n_dd_up: 2
n_dd_down: 54
n_dd_up_clean: 0
n_dd_down_clean: 49
in_vector_space: true
direction_upstream: 22
direction_downstream: 40
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# ITGA3

*integrin subunit alpha 3* — 17q21.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.42× (z +5.5, q 2e-05, up in 24 of 39 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 3.50×, NCI-H1792 2.88×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 3.04×, NCI-H1792 2.75×; ⚠ toxic; transcription drop).
> Pooled over the cell lines (median), lowered significantly by 54 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.326× (z -17.5, q 0e+00, down in 37 of 38 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[STMN3]] (+0.73, fdr 7e-06), [[COL13A1]] (+0.72, fdr 7e-06), [[LTBP3]] (+0.69, fdr 7e-06).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 22 arrows point to it, the strongest [[TGM2]] → it (grade B ⚠); 40 go from it, the strongest it → [[SHB]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 91.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 5 µM in 2 lines (NCI-H1573 3.50×, NCI-H1792 2.88×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.5 µM in 2 lines (NCI-H1573 3.04×, NCI-H1792 2.75×; ⚠ toxic; transcription drop).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.42×** | +5.5 | 2e-05 | 24/39 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.30×** | +4.0 | 0.017 | 24/35 (NCI-H1573, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 1.22× | +3.2 | 0.29 | 19/38 (LOX-IMVI, SNU-423, …) | inconsistent across doses |  |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.21× | +3.0 | 0.33 | 16/38 (Panc 03.27, PANC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 60 in all, 6 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 54 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 91.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.326×** | -17.5 | 0e+00 | 37/38 (Hs 766T, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.363×** | -15.8 | 0e+00 | 37/38 (SK-MEL-2, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.491×** | -15.7 | 0e+00 | 35/38 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.549×** | -13.2 | 1e-37 | 32/39 (HEC-1-A, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.427×** | -12.7 | 4e-35 | 33/38 (NCI-H2347, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.445×** | -12.6 | 1e-34 | 35/38 (SK-MEL-2, Hs 766T, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.464×** | -12.0 | 4e-31 | 36/38 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.447×** | -11.9 | 1e-30 | 37/38 (HOP62, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~4% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.459×** | -11.7 | 1e-29 | 33/37 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.515×** | -9.8 | 5e-21 | 36/40 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM |  | **0.652×** | -9.4 | 2e-19 | 29/38 (HEC-1-A, SK-MEL-2, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~8% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.609×** | -9.3 | 8e-19 | 34/38 (HEC-1-A, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.554×** | -9.2 | 2e-18 | 35/39 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.593×** | -8.1 | 2e-14 | 32/38 (HOP62, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Binimetinib (drug)]] 5 µM |  | **0.595×** | -8.1 | 2e-14 | 34/39 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.588×** | -8.0 | 6e-14 | 28/37 (SK-MEL-2, HEC-1-A, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, +0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 91. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 591 | 0 | 35 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0834× (z -19.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.136× (z -17.0) |
| [[SK-MEL-2 (line)]] | alt | 222 | 0 | 26 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -26.1) |
| [[HEC-1-A (line)]] | alt | 608 | 0 | 22 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.269× (z -20.8) |
| [[C32 (line)]] | wt | 323 | 0 | 21 | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -23.0) |
| [[HOP62 (line)]] | alt | 908 | 0 | 20 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -27.2) |
| [[PANC-1 (line)]] | alt | 317 | 0 | 14 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -17.9) |
| [[A549 (line)]] | wt | 265 | 0 | 11 | — | [[Panobinostat (drug)]] 5 µM 0.222× (z -16.6) |
| [[J82 (line)]] | alt | 378 | 0 | 9 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -19.7) |
| [[Panc 03.27 (line)]] | alt | 517 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.254× (z -15.6) |
| [[RPMI-7951 (line)]] | alt | 229 | 0 | 9 | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -16.8) |
| [[HCT15 (line)]] | alt | 254 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -19.1) |
| [[NCI-H2347 (line)]] | alt | 366 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -28.4) |
| [[SW 900 (line)]] | alt | 297 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -16.8) |
| [[HS-578T (line)]] | alt | 209 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -21.8) |
| [[MIA PaCa-2 (line)]] | alt | 143 | 0 | 7 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.524× (z -19.2) ⚠ position not correctable · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.259× (z -11.5) |
| [[Hs 766T (line)]] | wt | 485 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.255× (z -19.7) |
| [[KATO III (line)]] | alt | 212 | 0 | 6 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.371× (z -12.3) |
| [[NCI-H23 (line)]] | alt | 93.1 | 0 | 6 | — | [[Ixazomib citrate (drug)]] 5 µM 0.364× (z -10.4) |
| [[SNU-423 (line)]] | alt | 445 | 0 | 6 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.325× (z -13.1) |
| [[SW1417 (line)]] | alt | 185 | 0 | 6 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.316× (z -15.2) |
| [[A-172 (line)]] | wt | 486 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.257× (z -20.7) |
| [[CFPAC-1 (line)]] | alt | 378 | 0 | 5 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -14.2) |
| [[H4 (line)]] | wt | 337 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -13.9) |
| [[HT-29 (line)]] | alt | 194 | 0 | 5 | — | [[Panobinostat (drug)]] 5 µM 0.219× (z -11.5) |
| [[LOX-IMVI (line)]] | wt | 207 | 0 | 5 | — | [[Ixazomib citrate (drug)]] 5 µM 0.237× (z -13.1) |
| [[NCI-H1573 (line)]] | alt | 107 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +12.1) ⚠ toxic; transcription drop | [[Ixazomib citrate (drug)]] 5 µM 0.423× (z -8.5) |
| [[SW 1088 (line)]] | alt | 556 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -14.5) |
| [[AsPC-1 (line)]] | alt | 160 | 0 | 3 | — | [[Panobinostat (drug)]] 0.5 µM 0.218× (z -15.2) |
| [[hTERT-HPNE (line)]] | wt | 240 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.164× (z -11.7) |
| [[NCI-H1792 (line)]] | alt | 77.4 | 2 (2 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.88× (z +8.8) ⚠ toxic; transcription drop | [[Adagrasib (drug)]] 0.05 µM 0.627× (z -13.4) ⚠ position not correctable |
| [[COLO 205 (line)]] | alt | 167 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.240× (z -12.0) |
| [[SW480 (line)]] | alt | 102 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.322× (z -10.3) |
| [[LoVo (line)]] | wt | 72.5 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.415× (z -8.5) |
| [[LS 180 (line)]] | wt | 96.4 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.316× (z -11.2) |
| [[NCI-H2030 (line)]] | alt | 90.5 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.415× (z -9.4) |
| [[A-427 (line)]] | wt | 42.7 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 338 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.7 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 32.2 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 92.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 30.7 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 220 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 35.3 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 183 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 33.6 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 60.5 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 52.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 25.4 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 210 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 51.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 91), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STMN3]] | +0.73 | +0.69 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[COL13A1]] | +0.72 | +0.75 / +0.68 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[LTBP3]] | +0.69 | +0.65 / +0.68 | both halves | 7e-06 | pathway: Extracellular matrix organization |
| [[ACTN1]] | +0.69 | +0.73 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION; STRING 744 |
| [[ARPC2]] | +0.66 | +0.70 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION |
| [[ITGB5]] | +0.66 | +0.71 / +0.61 | both halves | 7e-06 | pathway: Extracellular matrix organization; STRING 986 |
| [[SHB]] | +0.66 | +0.65 / +0.68 | both halves | 7e-06 |  |
| [[SPRY4]] | +0.65 | +0.70 / +0.62 | both halves | 7e-06 |  |
| [[DCBLD2]] | +0.65 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[NT5E]] | +0.65 | +0.67 / +0.66 | both halves | 7e-06 | same gene group |
| [[CD59]] | +0.64 | +0.65 / +0.65 | both halves | 7e-06 | same gene group |
| [[NIBAN2]] | +0.64 | +0.66 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*22 arrows, 22 of them with an alert ⚠; grade A 0, B 15, C 7. Shown: the 12 strongest; 10 more arrows (10 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TGM2]] | B | TGM2 activity raises ITGA3's level | lines that do not express TGM2 (16) vs lines expressing it (34) | 2.63× lower at baseline in the lines without TGM2 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: CCL20, SAA2, ALDH1A3 |
| [[TINAGL1]] | B | TINAGL1 activity raises ITGA3's level | lines that do not express TINAGL1 (26) vs lines expressing it (24) | 1.64× lower at baseline in the lines without TINAGL1 | 0.012 | ⚠ within organs, on part of the lines; also absent: IL20RA, MSLN, KRT19 |
| [[ITGB3]] | B | ITGB3 activity raises ITGA3's level | lines that do not express ITGB3 (25) vs lines expressing it (25) | 3.07× lower at baseline in the lines without ITGB3 | 0.019 | ⚠ within organs, on part of the lines; also absent: ENSG00000259753, BICC1, ENSG00000291130 |
| [[MICAL2]] | B | MICAL2 activity raises ITGA3's level | lines that do not express MICAL2 (11) vs lines expressing it (39) | 2.93× lower at baseline in the lines without MICAL2 | 0.023 | ⚠ within organs, on part of the lines; also absent: UBA7, ENSG00000285906, SERPINB1 |
| [[MLPH]] | B | MLPH activity raises ITGA3's level | lines that do not express MLPH (13) vs lines expressing it (37) | 3.20× lower at baseline in the lines without MLPH | 0.033 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |
| [[MAP2K1]] | B | MAP2K1 activity raises ITGA3's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 8.4% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PRAG1]] | B | PRAG1 activity raises ITGA3's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 2.04× lower at baseline in the lines without PRAG1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[PTPRE]] | B | PTPRE activity raises ITGA3's level | lines that do not express PTPRE (13) vs lines expressing it (37) | 2.36× lower at baseline in the lines without PTPRE | 0.054 | ⚠ within organs, on part of the lines; also absent: PTPN22, FUT2, JPH1 |
| [[ELFN2]] | B | ELFN2 activity raises ITGA3's level | lines that do not express ELFN2 (19) vs lines expressing it (31) | 2.49× lower at baseline in the lines without ELFN2 | 0.065 | ⚠ within organs, on part of the lines; also absent: IL31RA, LHX1, TMEM92 |
| [[ALDH1A3]] | B | ALDH1A3 activity raises ITGA3's level | lines that do not express ALDH1A3 (20) vs lines expressing it (30) | 2.67× lower at baseline in the lines without ALDH1A3 | 0.067 | ⚠ within organs, on part of the lines; also absent: SHROOM4, ENSG00000232386, ADAMTS16 |
| [[MIR4280HG]] | B | MIR4280HG activity raises ITGA3's level | lines that do not express MIR4280HG (21) vs lines expressing it (29) | 1.94× lower at baseline in the lines without MIR4280HG | 0.067 | ⚠ within organs, on part of the lines; also absent: EVA1A, MILR1, LNX1; maybe low, not absent |
| [[KRT15]] | B | KRT15 activity raises ITGA3's level | lines that do not express KRT15 (15) vs lines expressing it (35) | 2.33× lower at baseline in the lines without KRT15 | 0.067 | ⚠ within organs, on part of the lines; also absent: MISP, PSORS1C1, ENSG00000266088 |

### Downstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 35, C 5. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SHB]] | B | ITGA3 activity raises SHB's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 2.65× lower at baseline in the lines without ITGA3 | 0.002 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[EHD1]] | B | ITGA3 activity raises EHD1's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 2.06× lower at baseline in the lines without ITGA3 | 0.002 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[ELFN2]] | B | ITGA3 activity raises ELFN2's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 2.95× lower at baseline in the lines without ITGA3 | 0.009 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[SLC25A51]] | B | ITGA3 activity raises SLC25A51's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 1.64× lower at baseline in the lines without ITGA3 | 0.010 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[PLEC]] | B | ITGA3 activity raises PLEC's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 2.67× lower at baseline in the lines without ITGA3 | 0.010 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[PICART1]] | B | ITGA3 activity raises PICART1's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 2.11× lower at baseline in the lines without ITGA3 | 0.011 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[PTPRE]] | B | ITGA3 activity raises PTPRE's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 3.52× lower at baseline in the lines without ITGA3 | 0.012 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[ALDH1A3]] | B | ITGA3 activity raises ALDH1A3's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 4.57× lower at baseline in the lines without ITGA3 | 0.015 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[PMEPA1]] | B | ITGA3 activity raises PMEPA1's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 3.15× lower at baseline in the lines without ITGA3 | 0.016 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[KRT15]] | B | ITGA3 activity raises KRT15's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 3.26× lower at baseline in the lines without ITGA3 | 0.020 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[TRIOBP]] | B | ITGA3 activity raises TRIOBP's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 1.70× lower at baseline in the lines without ITGA3 | 0.024 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[MYEOV]] | B | ITGA3 activity raises MYEOV's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 3.00× lower at baseline in the lines without ITGA3 | 0.032 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.815). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.9, 5.8); signed map (6.2, 50.6). **Vector** length 139, 53.4% of its response variance represented; |z| ≥ 3 in 1,782 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +5.6 | -1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.9 | +0.8 |
|  | [[Belinostat (drug)]] 5 µM |  | +4.5 | -12.6 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +4.1 | -15.8 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | -0.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.9 | -2.3 |
|  | [[Bentamapimod (drug)]] 5 µM |  | +2.9 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.8 | +1.8 |
|  | [[Diphenhydramine (drug)]] 0.5 µM |  | +2.8 | +3.2 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -9.6 | -9.3 |
|  | [[Trametinib (drug)]] 5 µM |  | -8.9 | -9.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -8.4 | -7.9 |
|  | [[Binimetinib (drug)]] 5 µM |  | -8.0 | -8.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -8.0 | -9.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -7.8 | -8.0 |

## What is on record

|  |  |
|---|---|
| Name | integrin subunit alpha 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.33 — chr17:50,055,968-50,090,481 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CD49c, VLA3a, VCA-2, GAP-B3; previously MSK18 |
| Gene groups (HGNC) | CD molecules; Integrin alpha subunits |
| Hallmark sets | APICAL_JUNCTION |
| Reactome | 10 pathways, smallest: Basigin interactions; MET activates PTK2 signaling; Laminin interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [P26006](https://www.uniprot.org/uniprotkb/P26006) (Integrin alpha-3):

> Integrin alpha-3/beta-1 is a receptor for fibronectin, laminin, collagen, epiligrin, thrombospondin and CSPG4. Integrin alpha-3/beta-1 provides a docking site for FAP (seprase) at invadopodia plasma membranes in a collagen-dependent manner and hence may participate in the adhesion, formation of invadopodia and matrix degradation processes, promoting cell invasion. Alpha-3/beta-1 may mediate with LGALS3 the stimulation by CSPG4 of endothelial cells migration.; (Microbial infection) Integrin …

**Summary**, from NCBI Gene [3675](https://www.ncbi.nlm.nih.gov/gene/3675):

> The gene encodes a member of the integrin alpha chain family of proteins. Integrins are heterodimeric integral membrane proteins composed of an alpha chain and a beta chain that function as cell surface adhesion molecules. The encoded preproprotein is proteolytically processed to generate light and heavy chains that comprise the alpha 3 subunit. This subunit joins with a beta 1 subunit to form an integrin that interacts with extracellular matrix proteins including members of the laminin family. …

**Accessions** — [HGNC:6139](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6139) · Entrez [3675](https://www.ncbi.nlm.nih.gov/gene/3675) · UniProt [P26006](https://www.uniprot.org/uniprotkb/P26006) · Ensembl [ENSG00000005884](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000005884)

## Data

Gene col 91: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 91); `tables/drug_effects.parquet` (64 rows, flagged included); `relations/gene_relations.parquet` (col_a == 91, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 91]; `tensor/DDL_lfc|DDL_z.npy` [91]; `embed/gene_vectors.npy` [91]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 91 or target_col == 91). Every well: [[ITGA3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGA3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
