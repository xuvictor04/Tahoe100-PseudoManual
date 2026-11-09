---
symbol: "DUSP4"
type: "gene"
col: 4230
ensembl_id: "ENSG00000120875"
name: "dual specificity phosphatase 4"
location: "8p12"
module: 92
arm: "+"
pooled_cpm: 81.86
n_lines_expressing: 35
n_dd_up: 5
n_dd_down: 48
n_dd_up_clean: 5
n_dd_down_clean: 38
in_vector_space: true
direction_upstream: 24
direction_downstream: 39
tags: ["gene", "module/092"]
generated_by: "tahoemap"
---

# DUSP4

*dual specificity phosphatase 4* — 8p12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 1.72× (z +4.1, q 0.022, up in 18 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 48 drug-doses (10 with an alert ⚠); the strongest is [[Trametinib (drug)]] 5 µM: 0.301× (z -18.1, q 0e+00, down in 33 of 35 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ITGB5]] (+0.74, fdr 7e-06), [[DUSP6]] (+0.72, fdr 7e-06), [[CEMIP]] (+0.68, fdr 7e-06); moves opposite to [[ALDH2]] (-0.55, fdr 1e-05), [[BLTP3B]] (-0.51, fdr 1e-05).
> It is in [[Module 092]], a single-armed module (MAPK output).
> Probable direction (from the cell lines, not proof of direct regulation): 24 arrows point to it, the strongest [[ABHD17C]] → it (grade B ⚠); 39 go from it, the strongest it → [[ABHD17C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, none with an alert. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4230.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **1.72×** | +4.1 | 0.022 | 18/34 (SNU-1, NCI-H1573, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.31×** | +3.9 | 0.022 | 14/33 (LoVo, SNU-1, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.33×** | +3.8 | 0.022 | 14/32 (SNU-1, LoVo, …) | inconsistent across doses | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **1.30×** | +3.8 | 0.022 | 20/33 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.027 | 15/33 (A-172, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Belumosudil (drug)]] 5 µM |  | 1.25× | +3.2 | 0.14 | 12/33 (A-172, SK-MEL-2, …) | top dose only |  |
| [[4EGI-1 (drug)]] 5 µM |  | 1.51× | +3.1 | 0.14 | 11/33 (A-172, SW480, …) | rises with dose | noisy plate (z scaled) |
| [[Tirabrutinib (drug)]] 0.5 µM |  | 1.23× | +3.0 | 0.17 | 8/33 (NCI-H2347, KATO III, …) | inconsistent across doses |  |
| [[Diphenhydramine (drug)]] 0.5 µM |  | 1.23× | +3.0 | 0.17 | 11/33 (COLO 205, NCI-H1573, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 49 in all, 11 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 48 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4230.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (drug)]] 5 µM |  | **0.301×** | -18.1 | 0e+00 | 33/35 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.417×** | -14.4 | 1e-44 | 32/33 (NCI-H460, SW480, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.375×** | -14.1 | 1e-42 | 33/34 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.380×** | -13.4 | 1e-38 | 31/32 (NCI-H460, Hs 766T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.405×** | -13.0 | 2e-36 | 31/33 (NCI-H1573, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.400×** | -12.6 | 1e-34 | 31/33 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.454×** | -12.2 | 2e-32 | 32/34 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.463×** | -11.0 | 2e-26 | 28/33 (BT-474, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.594×** | -10.5 | 6e-24 | 26/34 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.598×** | -10.3 | 3e-23 | 22/33 (NCI-H460, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.486×** | -10.3 | 3e-23 | 27/33 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.489×** | -10.2 | 6e-23 | 27/33 (LS 180, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.463×** | -10.2 | 8e-23 | 32/33 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.619×** | -9.6 | 2e-20 | 31/33 (NCI-H460, SW480, …) | all doses, stronger at high dose |  |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **0.307×** | -8.9 | 3e-17 | 30/31 (NCI-H460, SK-MEL-2, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.541×** | -8.8 | 5e-17 | 27/32 (NCI-H460, SK-MEL-2, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4230. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 259 | 0 | 31 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -30.8) |
| [[NCI-H1573 (line)]] | alt | 128 | 1 | 29 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.88× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -23.8) |
| [[BT-474 (line)]] | alt | 261 | 0 | 17 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.220× (z -20.0) |
| [[SW48 (line)]] | wt | 336 | 0 | 15 (5 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.113× (z -15.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.226× (z -15.5) |
| [[Hs 766T (line)]] | wt | 238 | 0 | 14 | — | [[Binimetinib (drug)]] 5 µM 0.146× (z -15.5) |
| [[SNU-1 (line)]] | wt | 565 | 2 | 12 (6 ⚠) | [[TAK-901 (drug)]] 5 µM 6.45× (z +11.7) | [[Homoharringtonine (drug)]] 5 µM 0.225× (z -24.9) |
| [[HOP62 (line)]] | alt | 48.0 | 0 | 13 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.536× (z -17.2) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.180× (z -15.0) |
| [[CFPAC-1 (line)]] | alt | 99.0 | 0 | 12 | — | [[Trametinib (drug)]] 5 µM 0.257× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 106 | 0 | 12 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.133× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Trametinib (drug)]] 5 µM 0.230× (z -13.6) |
| [[COLO 205 (line)]] | alt | 124 | 0 | 11 (1 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.191× (z -12.8) |
| [[SW480 (line)]] | alt | 46.8 | 0 | 11 | — | [[Trametinib (drug)]] 5 µM 0.238× (z -15.5) |
| [[LS 180 (line)]] | wt | 173 | 0 | 10 (3 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.135× (z -18.0) |
| [[KATO III (line)]] | alt | 149 | 0 | 9 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.226× (z -13.0) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.289× (z -11.7) |
| [[AsPC-1 (line)]] | alt | 171 | 0 | 8 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0992× (z -18.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.259× (z -16.1) |
| [[NCI-H2030 (line)]] | alt | 60.6 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -13.8) |
| [[RPMI-7951 (line)]] | alt | 114 | 0 | 7 (2 ⚠) | — | [[Trametinib (drug)]] 5 µM 0.188× (z -14.4) |
| [[A-172 (line)]] | wt | 44.4 | 1 | 5 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.28× (z +13.1) | [[Cobimetinib (drug)]] 5 µM 0.165× (z -13.6) |
| [[LoVo (line)]] | wt | 182 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.190× (z -13.6) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.259× (z -11.5) |
| [[NCI-H1792 (line)]] | alt | 30.2 | 0 | 5 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.571× (z -12.7) ⚠ position not correctable · without an alert: [[Trametinib (drug)]] 5 µM 0.209× (z -10.1) |
| [[SHP-77 (line)]] | alt | 130 | 0 | 5 | — | [[Trametinib (drug)]] 5 µM 0.289× (z -11.1) |
| [[C32 (line)]] | wt | 50.6 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0671× (z -16.0) ⚠ toxic; transcription drop · without an alert: [[Binimetinib (drug)]] 5 µM 0.139× (z -12.4) |
| [[H4 (line)]] | wt | 53.4 | 0 | 4 | — | [[Trametinib (drug)]] 5 µM 0.195× (z -10.3) |
| [[Panc 03.27 (line)]] | alt | 92.2 | 0 | 4 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.276× (z -14.4) |
| [[A549 (line)]] | wt | 83.5 | 0 | 3 | — | [[Trametinib (drug)]] 5 µM 0.228× (z -9.6) |
| [[SW 900 (line)]] | alt | 52.1 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -9.0) ⚠ toxic; transcription drop · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.293× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 34.4 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.198× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.572× (z -9.8) ⚠ position not correctable |
| [[A-427 (line)]] | wt | 7.76 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.98 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 19.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 8.35 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 26.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.3 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 10.8 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.85 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 8.36 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 18.4 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 8.80 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.50 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 158 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 62.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 90.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.70 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 5.20 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.36 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 46.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4230), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ITGB5]] | +0.74 | +0.69 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[DUSP6]] | +0.72 | +0.68 / +0.74 | both halves | 7e-06 | same gene group; pathway: ERK/MAPK targets; STRING 574 |
| [[CEMIP]] | +0.68 | +0.71 / +0.67 | both halves | 7e-06 | **novel candidate** |
| [[ETV4]] | +0.67 | +0.64 / +0.68 | both halves | 7e-06 | pathway: MAPK family signaling cascades; STRING 464 |
| [[SPRY2]] | +0.67 | +0.67 / +0.67 | both halves | 7e-06 | STRING 567 |
| [[SPRED1]] | +0.66 | +0.61 / +0.68 | both halves | 7e-06 | pathway: MAPK family signaling cascades |
| [[ABHD17C]] | +0.65 | +0.70 / +0.61 | both halves | 7e-06 | pathway: MAPK family signaling cascades |
| [[SHC4]] | +0.65 | +0.63 / +0.64 | both halves | 7e-06 | **novel candidate** |
| [[ITGA2]] | +0.64 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[PHLDA1]] | +0.64 | +0.63 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 536 |
| [[ZG16B]] | +0.64 | +0.55 / +0.56 | both halves | 1e-05 |  |
| [[ANTXR2]] | +0.64 | +0.65 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ALDH2]] | -0.55 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[BLTP3B]] | -0.51 | -0.51 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*24 arrows, 24 of them with an alert ⚠; grade A 0, B 18, C 6. Shown: the 12 strongest; 12 more arrows (12 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABHD17C]] | B | ABHD17C activity raises DUSP4's level | lines that do not express ABHD17C (8) vs lines expressing it (42) | 5.75× lower at baseline in the lines without ABHD17C | 4e-04 | ⚠ within organs, on part of the lines; also absent: SESTD1; maybe low, not absent |
| [[NR4A2]] | B | NR4A2 activity raises DUSP4's level | lines that do not express NR4A2 (7) vs lines expressing it (43) | 5.63× lower at baseline in the lines without NR4A2 | 0.010 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[EPHA4]] | B | EPHA4 activity raises DUSP4's level | lines that do not express EPHA4 (19) vs lines expressing it (31) | 2.36× lower at baseline in the lines without EPHA4 | 0.013 | ⚠ within organs, on part of the lines; also absent: SNAI2, GNG2, TNFSF10 |
| [[SDR16C5]] | B | SDR16C5 activity raises DUSP4's level | lines that do not express SDR16C5 (28) vs lines expressing it (22) | 3.36× lower at baseline in the lines without SDR16C5 | 0.032 | ⚠ within organs, on part of the lines; also absent: CATSPERB, FA2H, LIPH |
| [[AMIGO2]] | B | AMIGO2 activity raises DUSP4's level | lines that do not express AMIGO2 (12) vs lines expressing it (38) | 1.98× lower at baseline in the lines without AMIGO2 | 0.034 | ⚠ within organs, on part of the lines; also absent: PCED1B, CXCL3, PRDM1 |
| [[PLEK2]] | B | PLEK2 activity raises DUSP4's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 2.98× lower at baseline in the lines without PLEK2 | 0.036 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[KIAA0040]] | B | KIAA0040 activity raises DUSP4's level | lines that do not express KIAA0040 (24) vs lines expressing it (26) | 3.19× lower at baseline in the lines without KIAA0040 | 0.039 | ⚠ within organs, on part of the lines; also absent: ENSG00000226281, CLDN3, ESRP1 |
| [[MAP2K1]] | B | MAP2K1 activity raises DUSP4's level | compounds that target MAP2K1: 4 of 4 lower it (Binimetinib, Cobimetinib, TAK-733, Trametinib) | 100% of the class's compounds vs 8.1% of all compounds | 0.042 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ABCC3]] | B | ABCC3 activity raises DUSP4's level | lines that do not express ABCC3 (16) vs lines expressing it (34) | 2.49× lower at baseline in the lines without ABCC3 | 0.055 | ⚠ within organs, on part of the lines; also absent: AQP3, CDC42BPG, NUP62CL |
| [[LRATD2]] | B | LRATD2 activity raises DUSP4's level | lines that do not express LRATD2 (16) vs lines expressing it (34) | 2.15× lower at baseline in the lines without LRATD2 | 0.057 | ⚠ within organs, on part of the lines; also absent: POU5F1B, PCAT1, ITGB8; maybe low, not absent |
| [[ALDH2]] | B | ALDH2 activity raises DUSP4's level | lines that do not express ALDH2 (9) vs lines expressing it (41) | 2.36× lower at baseline in the lines without ALDH2 | 0.066 | ⚠ within organs, on part of the lines; also absent: MTARC2, SLC12A7; maybe low, not absent |
| [[PCED1B]] | B | PCED1B activity raises DUSP4's level | lines that do not express PCED1B (11) vs lines expressing it (39) | 2.37× lower at baseline in the lines without PCED1B | 0.075 | ⚠ within organs, on part of the lines; also absent: AMIGO2, CXCL3, PRDM1 |

### Downstream of this gene

*39 arrows, 39 of them with an alert ⚠; grade A 0, B 34, C 5. Shown: the 12 strongest; 27 more arrows (27 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ABHD17C]] | B | DUSP4 activity raises ABHD17C's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 3.71× lower at baseline in the lines without DUSP4 | 6e-04 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[MAML3]] | B | DUSP4 activity raises MAML3's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 2.49× lower at baseline in the lines without DUSP4 | 0.004 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[ATP2B1]] | B | DUSP4 activity raises ATP2B1's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 1.77× lower at baseline in the lines without DUSP4 | 0.014 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[ST3GAL1]] | B | DUSP4 activity raises ST3GAL1's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 2.06× lower at baseline in the lines without DUSP4 | 0.015 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[KIAA0040]] | B | DUSP4 activity raises KIAA0040's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 3.28× lower at baseline in the lines without DUSP4 | 0.016 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[SLC38A2]] | B | DUSP4 activity lowers SLC38A2's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 1.24× higher at baseline in the lines without DUSP4 | 0.018 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[NR4A2]] | B | DUSP4 activity raises NR4A2's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 2.44× lower at baseline in the lines without DUSP4 | 0.021 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[LAMA3]] | B | DUSP4 activity raises LAMA3's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 2.62× lower at baseline in the lines without DUSP4 | 0.022 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[ABCC3]] | B | DUSP4 activity raises ABCC3's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 2.44× lower at baseline in the lines without DUSP4 | 0.025 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[TNFRSF21]] | B | DUSP4 activity raises TNFRSF21's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 2.63× lower at baseline in the lines without DUSP4 | 0.027 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[PCED1B]] | B | DUSP4 activity raises PCED1B's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 2.14× lower at baseline in the lines without DUSP4 | 0.033 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |
| [[PTPRE]] | B | DUSP4 activity raises PTPRE's level | lines that do not express DUSP4 (15) vs lines expressing it (35) | 2.50× lower at baseline in the lines without DUSP4 | 0.040 | ⚠ within organs, on part of the lines; also absent: IGSF9, CEMIP, SYTL5 |

## Where it sits

- **Module**: [[Module 092]] — MAPK output; 49 genes; every member is in the + arm (projection on the module's main direction 0.748). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.7, 5.7); signed map (8.7, 49.0). **Vector** length 132, 41.9% of its response variance represented; |z| ≥ 3 in 1,384 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *KRAS signaling up* (hallmark, mean cos +0.55 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.4 | +0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +4.7 | -10.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.3 | -0.3 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~11% of this change | +4.2 | -3.1 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +0.1 |
|  | [[Filgotinib (drug)]] 5 µM |  | +4.1 | +3.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.5 | +2.2 |
|  | [[4EGI-1 (drug)]] 5 µM |  | +3.4 | +3.1 |
| fall | [[Trametinib (drug)]] 5 µM |  | -10.6 | -18.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -8.7 | -14.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -8.6 | -14.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -8.2 | -10.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -8.2 | -12.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -8.0 | -13.4 |

## What is on record

|  |  |
|---|---|
| Name | dual specificity phosphatase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8p12 — chr8:29,333,064-29,350,684 (-) |
| Ensembl biotype | protein_coding |
| Also known as | HVH2, MKP-2, TYP |
| Gene groups (HGNC) | MAP kinase phosphatases |
| Hallmark sets | TNFA_SIGNALING_VIA_NFKB |
| Reactome | 33 pathways, smallest: ERKs are inactivated; ERK/MAPK targets; RAF-independent MAPK1/3 activation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13115](https://www.uniprot.org/uniprotkb/Q13115) (Dual specificity protein phosphatase 4):

> Regulates mitogenic signal transduction by dephosphorylating both Thr and Tyr residues on MAP kinases ERK1 and ERK2.

**Summary**, from NCBI Gene [1846](https://www.ncbi.nlm.nih.gov/gene/1846):

> The protein encoded by this gene is a member of the dual specificity protein phosphatase subfamily. These phosphatases inactivate their target kinases by dephosphorylating both the phosphoserine/threonine and phosphotyrosine residues. They negatively regulate members of the mitogen-activated protein (MAP) kinase superfamily (MAPK/ERK, SAPK/JNK, p38), which are associated with cellular proliferation and differentiation. Different members of the family of dual specificity phosphatases show …

**Accessions** — [HGNC:3070](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3070) · Entrez [1846](https://www.ncbi.nlm.nih.gov/gene/1846) · UniProt [Q13115](https://www.uniprot.org/uniprotkb/Q13115) · Ensembl [ENSG00000120875](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120875)

## Data

Gene col 4230: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4230); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4230, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4230]; `tensor/DDL_lfc|DDL_z.npy` [4230]; `embed/gene_vectors.npy` [4230]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4230 or target_col == 4230). Every well: [[DUSP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DUSP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
