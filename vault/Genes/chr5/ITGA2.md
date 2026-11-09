---
symbol: "ITGA2"
type: "gene"
col: 8891
ensembl_id: "ENSG00000164171"
name: "integrin subunit alpha 2"
location: "5q11.2"
module: 81
arm: "+"
pooled_cpm: 529.93
n_lines_expressing: 39
n_dd_up: 8
n_dd_down: 87
n_dd_up_clean: 5
n_dd_down_clean: 71
in_vector_space: true
direction_upstream: 49
direction_downstream: 46
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# ITGA2

*integrin subunit alpha 2* — 5q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 5 µM: 1.43× (z +4.8, q 8e-04, up in 22 of 37 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Pitavastatin (Calcium) (drug)]] 0.5 µM: 1.40× (z +4.6, q 0.001, up in 22 of 36 measured lines).
> Pooled over the cell lines (median), lowered significantly by 87 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.104× (z -43.0, q 0e+00, down in 37 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CDCP1]] (+0.85, fdr 7e-06), [[ANTXR2]] (+0.84, fdr 7e-06), [[S100A16]] (+0.82, fdr 7e-06).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 49 arrows point to it, the strongest [[F3]] → it (grade B ⚠); 46 go from it, the strongest it → [[ITGA2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8891.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.43×** | +4.8 | 8e-04 | 22/37 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.40×** | +4.6 | 0.001 | 22/36 (SW48, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.45×** | +4.3 | 0.003 | 23/36 (SW480, COLO 205, …) | rises with dose |  |
| [[Rapamycin (drug)]] 5 µM |  | **1.24×** | +4.1 | 0.005 | 24/37 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[BAY1125976 (drug)]] 5 µM |  | **2.17×** | +4.0 | 0.008 | 25/37 (LS 180, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **1.34×** | +3.8 | 0.014 | 20/36 (COLO 205, SW480, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.047 | 23/38 (Panc 03.27, NCI-H2347, …) | inconsistent across doses |  |
| [[Larotrectinib sulfate (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.34×** | +3.4 | 0.048 | 18/37 (LOX-IMVI, NCI-H460, …) | two highest doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 1.26× | +3.1 | 0.11 | 22/37 (NCI-H2347, NCI-H23, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | 1.30× | +3.1 | 0.12 | 19/37 (LoVo, A-427, …) | inconsistent across doses |  |
| [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | 1.37× | +3.0 | 0.13 | 17/37 (A-427, LoVo, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 88 in all, 17 with an alert ⚠; shown: the 15 strongest. 87 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8891.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.104×** | -43.0 | 0e+00 | 37/37 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.242×** | -26.9 | 0e+00 | 37/38 (Panc 03.27, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.174×** | -22.6 | 0e+00 | 37/37 (AsPC-1, A549, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.270×** | -17.6 | 0e+00 | 36/37 (HOP62, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.385×** | -16.0 | 0e+00 | 36/37 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.313×** | -15.6 | 0e+00 | 32/37 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.320×** | -15.3 | 0e+00 | 36/38 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.315×** | -14.9 | 0e+00 | 36/37 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.342×** | -14.7 | 0e+00 | 38/39 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 5 µM |  | **0.341×** | -14.4 | 3e-45 | 37/38 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.406×** | -14.4 | 3e-45 | 34/37 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.345×** | -14.3 | 2e-44 | 34/37 (HOP62, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **0.332×** | -14.2 | 4e-44 | 34/36 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.385×** | -11.8 | 1e-30 | 36/37 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.438×** | -11.0 | 9e-27 | 33/36 (HepG2/C3A, AsPC-1, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.47 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8891. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 331 | 0 | 48 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0837× (z -22.4) |
| [[HOP62 (line)]] | alt | 697 | 0 | 46 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0633× (z -45.6) |
| [[H4 (line)]] | wt | 709 | 0 | 43 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0514× (z -35.2) |
| [[SW480 (line)]] | alt | 233 | 5 (1 ⚠) | 23 (4 ⚠) | [[Vinblastine (sulfate) (drug)]] 5 µM 2.35× (z +12.4) | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -25.8) |
| [[HepG2_C3A (line)]] | wt | 1,541 | 0 | 27 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0617× (z -41.9) |
| [[KATO III (line)]] | alt | 462 | 0 | 27 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.168× (z -21.4) |
| [[NCI-H460 (line)]] | wt | 237 | 1 | 24 (5 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.33× (z +9.2) | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -32.2) |
| [[hTERT-HPNE (line)]] | wt | 961 | 0 | 23 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -27.3) |
| [[LoVo (line)]] | wt | 935 | 0 | 23 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -30.5) |
| [[A-172 (line)]] | wt | 445 | 0 | 22 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0640× (z -33.6) |
| [[AsPC-1 (line)]] | alt | 1,492 | 0 | 22 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0362× (z -40.8) |
| [[CFPAC-1 (line)]] | alt | 1,003 | 0 | 21 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0405× (z -42.7) |
| [[SW 900 (line)]] | alt | 1,106 | 0 | 21 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0788× (z -27.7) |
| [[SW48 (line)]] | wt | 822 | 2 (1 ⚠) | 19 (1 ⚠) | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 3.92× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.0996× (z -25.5) |
| [[HS-578T (line)]] | alt | 752 | 0 | 20 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0799× (z -25.1) |
| [[NCI-H23 (line)]] | alt | 379 | 0 | 20 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0906× (z -27.4) |
| [[Hs 766T (line)]] | wt | 701 | 0 | 19 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0615× (z -38.0) |
| [[PANC-1 (line)]] | alt | 791 | 0 | 19 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0613× (z -35.3) |
| [[J82 (line)]] | alt | 192 | 0 | 18 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.164× (z -16.4) |
| [[NCI-H1573 (line)]] | alt | 384 | 3 | 14 | [[Harringtonine (drug)]] 0.5 µM 3.69× (z +10.7) | [[Homoharringtonine (drug)]] 5 µM 0.0794× (z -29.3) |
| [[Panc 03.27 (line)]] | alt | 1,297 | 0 | 17 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -32.8) |
| [[A549 (line)]] | wt | 860 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0314× (z -37.1) |
| [[NCI-H1792 (line)]] | alt | 865 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0539× (z -32.0) |
| [[NCI-H2347 (line)]] | alt | 2,021 | 0 | 12 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0489× (z -37.2) |
| [[HCT15 (line)]] | alt | 337 | 0 | 11 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -21.8) |
| [[LOX-IMVI (line)]] | wt | 183 | 3 (2 ⚠) | 7 | [[Dinaciclib (drug)]] 5 µM 2.49× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Pitavastatin (Calcium) (drug)]] 0.5 µM 2.40× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -21.9) |
| [[HEC-1-A (line)]] | alt | 215 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -20.6) |
| [[LS 180 (line)]] | wt | 428 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -19.1) |
| [[NCI-H2030 (line)]] | alt | 454 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -24.8) |
| [[A-427 (line)]] | wt | 240 | 0 | 8 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.262× (z -10.6) |
| [[COLO 205 (line)]] | alt | 282 | 4 (1 ⚠) | 4 | [[Harringtonine (drug)]] 0.5 µM 4.17× (z +11.3) | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -23.8) |
| [[SK-MEL-2 (line)]] | alt | 133 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.305× (z -13.4) |
| [[SNU-423 (line)]] | alt | 420 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0700× (z -27.5) |
| [[SW 1271 (line)]] | alt | 644 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -15.6) |
| [[A498 (line)]] | wt | 133 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.217× (z -19.3) |
| [[SW 1088 (line)]] | alt | 721 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.123× (z -15.2) |
| [[CHP-212 (line)]] | wt | 207 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -15.5) |
| [[AN3 CA (line)]] | alt | 70.0 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 54.0 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 72.8 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 125 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.4 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1,027 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 383 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 46.3 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 109 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 126 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 30.1 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 37.3 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 80.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8891), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDCP1]] | +0.85 | +0.85 / +0.86 | both halves | 7e-06 | same gene group |
| [[ANTXR2]] | +0.84 | +0.86 / +0.85 | both halves | 7e-06 | **novel candidate** |
| [[S100A16]] | +0.82 | +0.85 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[NT5E]] | +0.78 | +0.79 / +0.78 | both halves | 7e-06 | same gene group; pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 482 |
| [[PLEK2]] | +0.76 | +0.77 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[DCBLD2]] | +0.76 | +0.78 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_KRAS_SIGNALING_UP |
| [[ITGB5]] | +0.75 | +0.79 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_EPITHELIAL_MESENCHYMAL_TRANSITION; STRING 980 |
| [[SLC25A51]] | +0.74 | +0.76 / +0.68 | both halves | 7e-06 |  |
| [[MMP1]] | +0.74 | +0.73 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_COAGULATION; STRING 813 |
| [[LAMC2]] | +0.72 | +0.69 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION; STRING 883 |
| [[CORO2B]] | +0.72 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[SEPTIN10]] | +0.70 | +0.74 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*49 arrows, 49 of them with an alert ⚠; grade A 0, B 44, C 5. Shown: the 12 strongest; 37 more arrows (37 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F3]] | B | F3 activity raises ITGA2's level | lines that do not express F3 (24) vs lines expressing it (26) | 3.94× lower at baseline in the lines without F3 | 0.001 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[C11orf91]] | B | C11orf91 activity raises ITGA2's level | lines that do not express C11orf91 (8) vs lines expressing it (42) | 4.20× lower at baseline in the lines without C11orf91 | 0.003 | ⚠ within organs, on part of the lines; also absent: CD59, ENSG00000284969, ENSG00000255202 |
| [[CD59]] | B | CD59 activity raises ITGA2's level | lines that do not express CD59 (7) vs lines expressing it (43) | 4.71× lower at baseline in the lines without CD59 | 0.006 | ⚠ within organs, on part of the lines; also absent: C11orf91, ENSG00000284969, MET; maybe low, not absent |
| [[ADAM19]] | B | ADAM19 activity raises ITGA2's level | lines that do not express ADAM19 (13) vs lines expressing it (37) | 3.04× lower at baseline in the lines without ADAM19 | 0.006 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: ITGA1, ABLIM3, LBH |
| [[IL1RAP]] | B | IL1RAP activity raises ITGA2's level | lines that do not express IL1RAP (8) vs lines expressing it (42) | 5.53× lower at baseline in the lines without IL1RAP | 0.006 | ⚠ within organs, on part of the lines; also absent: LACC1, GSDMD, TGFBR2 |
| [[RAI14]] | B | RAI14 activity raises ITGA2's level | lines that do not express RAI14 (11) vs lines expressing it (39) | 2.88× lower at baseline in the lines without RAI14 | 0.008 | ⚠ within organs, on part of the lines; also absent: CCDC71L, LINC01828, ENSG00000285744; maybe low, not absent |
| [[ITGA6]] | B | ITGA6 activity raises ITGA2's level | lines that do not express ITGA6 (9) vs lines expressing it (41) | 2.93× lower at baseline in the lines without ITGA6 | 0.008 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[ALDH3B1]] | B | ALDH3B1 activity raises ITGA2's level | lines that do not express ALDH3B1 (9) vs lines expressing it (41) | 4.41× lower at baseline in the lines without ALDH3B1 | 0.010 | ⚠ within organs, on part of the lines; also absent: NIBAN2, IER3, FOSL1; maybe low, not absent |
| [[FAM107B]] | B | FAM107B activity raises ITGA2's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 4.31× lower at baseline in the lines without FAM107B | 0.011 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[WNT7B]] | B | WNT7B activity raises ITGA2's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 3.52× lower at baseline in the lines without WNT7B | 0.013 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG |
| [[S100A16]] | B | S100A16 activity raises ITGA2's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 5.19× lower at baseline in the lines without S100A16 | 0.015 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[HRH1]] | B | HRH1 activity raises ITGA2's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 3.39× lower at baseline in the lines without HRH1 | 0.018 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |

### Downstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 46, C 0. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA2-AS1]] | B | ITGA2 activity raises ITGA2-AS1's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 2.29× lower at baseline in the lines without ITGA2 | 6e-04 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[ITGA6]] | B | ITGA2 activity raises ITGA6's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 2.09× lower at baseline in the lines without ITGA2 | 0.004 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[S100A11]] | B | ITGA2 activity raises S100A11's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 1.97× lower at baseline in the lines without ITGA2 | 0.009 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[ASPH]] | B | ITGA2 activity raises ASPH's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 2.19× lower at baseline in the lines without ITGA2 | 0.013 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[PLEK2]] | B | ITGA2 activity raises PLEK2's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 2.80× lower at baseline in the lines without ITGA2 | 0.016 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[SHB]] | B | ITGA2 activity raises SHB's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 2.50× lower at baseline in the lines without ITGA2 | 0.017 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[MOCS2-DT]] | B | ITGA2 activity raises MOCS2-DT's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 1.98× lower at baseline in the lines without ITGA2 | 0.019 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[LAMC2]] | B | ITGA2 activity raises LAMC2's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 3.39× lower at baseline in the lines without ITGA2 | 0.024 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[MAMLD1]] | B | ITGA2 activity raises MAMLD1's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 2.05× lower at baseline in the lines without ITGA2 | 0.026 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[TNFAIP8]] | B | ITGA2 activity raises TNFAIP8's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 1.99× lower at baseline in the lines without ITGA2 | 0.030 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[ITPRID2]] | B | ITGA2 activity raises ITPRID2's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 1.83× lower at baseline in the lines without ITGA2 | 0.034 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[NT5E]] | B | ITGA2 activity raises NT5E's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 3.13× lower at baseline in the lines without ITGA2 | 0.038 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.837). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.0, 4.1); signed map (5.1, 45.9). **Vector** length 149, 61.0% of its response variance represented; |z| ≥ 3 in 2,435 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +1.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +6.6 | -10.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.4 | -14.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.1 | -2.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.7 | -17.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.3 | +3.8 |
|  | [[BAY1125976 (drug)]] 5 µM |  | +4.0 | +4.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.9 | -2.1 |
|  | [[Rapamycin (drug)]] 5 µM |  | +3.7 | +4.1 |
| fall | [[Trametinib (drug)]] 5 µM |  | -13.6 | -14.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -12.9 | -16.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | -11.8 | -14.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -11.5 | -15.3 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -11.4 | -14.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -11.3 | -14.9 |

## What is on record

|  |  |
|---|---|
| Name | integrin subunit alpha 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q11.2 — chr5:52,989,340-53,094,779 (+) |
| Ensembl biotype | protein_coding |
| Also known as | GPIa, VLAA2, HPA-5; previously CD49B |
| Gene groups (HGNC) | CD molecules; Integrin alpha subunits; Human platelet antigens |
| Hallmark sets | COAGULATION, KRAS_SIGNALING_UP, APICAL_JUNCTION, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 19 pathways, smallest: CHL1 interactions; Platelet Adhesion to exposed collagen; Regulation of MITF-M-dependent genes involved in extracellular matrix, focal adhesion and epithelial-to-mesenchymal transition |
| Matched by | ensembl_id |

**Function**, from UniProt [P17301](https://www.uniprot.org/uniprotkb/P17301) (Integrin alpha-2):

> Integrin alpha-2/beta-1 is a receptor for laminin, collagen, collagen C-propeptides, fibronectin and E-cadherin. It recognizes the proline-hydroxylated sequence G-F-P-G-E-R in collagen. It is responsible for adhesion of platelets and other cells to collagens, modulation of collagen and collagenase gene expression, force generation and organization of newly synthesized extracellular matrix.; (Microbial infection) Integrin ITGA2:ITGB1 acts as a receptor for Human rotavirus A.; (Microbial …

**Summary**, from NCBI Gene [3673](https://www.ncbi.nlm.nih.gov/gene/3673):

> This gene encodes the alpha subunit of a transmembrane receptor for collagens and related proteins. The encoded protein forms a heterodimer with a beta subunit and mediates the adhesion of platelets and other cell types to the extracellular matrix. Loss of the encoded protein is associated with bleeding disorder platelet-type 9. Antibodies against this protein are found in several immune disorders, including neonatal alloimmune thrombocytopenia. This gene is located adjacent to a related alpha …

**Accessions** — [HGNC:6137](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6137) · Entrez [3673](https://www.ncbi.nlm.nih.gov/gene/3673) · UniProt [P17301](https://www.uniprot.org/uniprotkb/P17301) · Ensembl [ENSG00000164171](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164171)

## Data

Gene col 8891: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8891); `tables/drug_effects.parquet` (99 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8891, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8891]; `tensor/DDL_lfc|DDL_z.npy` [8891]; `embed/gene_vectors.npy` [8891]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8891 or target_col == 8891). Every well: [[ITGA2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ITGA2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
