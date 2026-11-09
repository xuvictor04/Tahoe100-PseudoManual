---
symbol: "DPYSL4"
type: "gene"
col: 7544
ensembl_id: "ENSG00000151640"
name: "dihydropyrimidinase like 4"
location: "10q26.3"
module: 103
arm: "+"
pooled_cpm: 3.6
n_lines_expressing: 26
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 7
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/103"]
generated_by: "tahoemap"
---

# DPYSL4

*dihydropyrimidinase like 4* — 10q26.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 1.99× (z +6.4, q 1e-07, up in 13 of 22 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.504× (z -6.4, q 1e-07, down in 11 of 20 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DDX41]] (+0.64, fdr 7e-06), [[PPFIA4]] (+0.64, fdr 1e-05), [[EPHA3]] (+0.62, fdr 9e-06).
> It is in [[Module 103]], a single-armed module (glycolysis).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[HOXA13]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SCAND2P]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7544.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **1.99×** | +6.4 | 1e-07 | 13/22 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.92×** | +5.6 | 7e-06 | 1/10 (H4) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.82×** | +5.3 | 2e-05 | 2/9 (HS-578T, H4) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +5.2 | 3e-05 | 9/22 (CFPAC-1, NCI-H1573, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.62×** | +4.5 | 8e-04 | 12/22 (PANC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.62×** | +4.3 | 0.002 | 6/17 (C32, A-172, …) | top dose only | position effect removed |
| [[Folic acid (drug)]] 5 µM |  | **1.37×** | +4.1 | 0.004 | 8/24 (PANC-1, SNU-423, …) | inconsistent across doses | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +4.0 | 0.005 | 0/12 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Roxadustat (drug)]] 5 µM |  | **1.52×** | +3.7 | 0.013 | 7/20 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[Glasdegib (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +3.2 | 0.084 | 2/22 (NCI-H1792, CFPAC-1) | inconsistent across doses | position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **1.61×** | +3.1 | 0.088 | 1/11 (AN3 CA) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.89×** | +3.1 | 0.095 | 4/16 (SNU-423, PANC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.39×** | +3.1 | 0.097 | 0/13 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7544.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.504×** | -6.4 | 1e-07 | 11/20 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.586×** | -4.8 | 5e-04 | 12/20 (A-172, C-33 A, …) | top dose only | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.602×** | -4.7 | 5e-04 | 14/17 (C-33 A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.611×** | -4.4 | 0.001 | 9/18 (NCI-H460, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.690×** | -3.4 | 0.056 | 8/19 (C-33 A, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | **0.771×** | -3.4 | 0.056 | 5/21 (NCI-H1792, C32, …) | top dose only | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.694×** | -3.4 | 0.056 | 12/17 (NCI-H1792, NCI-H460, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~77% of this change | **0.779×** | -3.3 | 0.064 | 12/19 (SNU-423, C32, …) | rises with dose | composition shift |
| [[Sodium Salicylate (drug)]] 0.5 µM |  | **0.703×** | -3.3 | 0.064 | 4/20 (CHP-212, NCI-H23, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.786×** | -3.2 | 0.087 | 10/19 (NCI-H1792, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.721× | -3.0 | 0.12 | 2/22 (NCI-H23, SNU-1) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7544. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 15.1 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0402× (z -16.1) ⚠ cell-cycle shift, explains ~27% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.212× (z -11.1) |
| [[C32 (line)]] | wt | 34.9 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -12.1) ⚠ cell-cycle shift, explains ~77% of this change |
| [[A-172 (line)]] | wt | 11.5 | 0 | 3 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0908× (z -11.4) |
| [[C-33 A (line)]] | alt | 17.2 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0607× (z -12.5) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 6.60 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0470× (z -12.6) ⚠ cell-cycle shift, explains ~50% of this change |
| [[AN3 CA (line)]] | alt | 39.4 | 0 | 2 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0809× (z -9.5) ⚠ cell-cycle shift, explains ~50% of this change |
| [[NCI-H460 (line)]] | wt | 4.56 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.113× (z -10.0) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 13.4 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0950× (z -15.3) ⚠ cell-cycle shift, explains ~77% of this change |
| [[A549 (line)]] | wt | 7.71 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.40× (z +9.0) | — |
| [[H4 (line)]] | wt | 16.5 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.112× (z -9.0) |
| [[NCI-H23 (line)]] | alt | 3.73 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0634× (z -8.9) |
| [[PANC-1 (line)]] | alt | 3.88 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 5.93× (z +8.6) | — |
| [[A498 (line)]] | wt | 0.331 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.297 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.236 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.367 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.289 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.302 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 0.334 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.364 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.376 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 0.263 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.317 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.263 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.347 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.376 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.558 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.22 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.20 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.173 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 3.99 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.04 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.196 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.272 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.470 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.342 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.13 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.230 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.390 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.806 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7544), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DDX41]] | +0.64 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[PPFIA4]] | +0.64 | +0.55 / +0.63 | both halves | 1e-05 | pathway: HALLMARK_GLYCOLYSIS |
| [[EPHA3]] | +0.62 | +0.57 / +0.59 | both halves | 9e-06 | **novel candidate** |
| [[AK2]] | +0.61 | +0.54 / +0.63 | both halves | 1e-05 |  |
| [[ISM2]] | +0.61 | +0.49 / +0.65 | both halves | 1e-05 | **novel candidate** |
| [[LRAT]] | +0.61 | +0.53 / +0.61 | both halves | 1e-05 | **novel candidate** |
| [[TBC1D9B]] | +0.58 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[KCNC3]] | +0.57 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[NRN1]] | +0.57 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[EFR3B]] | +0.56 | +0.61 / +0.43 | both halves | 4e-05 |  |
| [[CPNE5]] | +0.56 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[HOXA13]] | +0.54 | +0.50 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HOXA13]] | B | HOXA13 activity raises DPYSL4's level | lines that do not express HOXA13 (14) vs lines expressing it (36) | 1.91× lower at baseline in the lines without HOXA13 | 0.069 | ⚠ within organs, on part of the lines; also absent: PRR5L |
| [[TRIM9]] | B | TRIM9 activity raises DPYSL4's level | lines that do not express TRIM9 (16) vs lines expressing it (34) | 2.66× lower at baseline in the lines without TRIM9 | 0.091 | ⚠ within organs, on part of the lines; also absent: NRG1, DPYSL3, WIPF1 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SCAND2P]] | B | DPYSL4 activity raises SCAND2P's level | lines that do not express DPYSL4 (24) vs lines expressing it (26) | 1.36× lower at baseline in the lines without DPYSL4 | 0.047 | ⚠ within organs, on part of the lines; also absent: TWIST2, ZIC1, MICU3 |

## Where it sits

- **Module**: [[Module 103]] — glycolysis; 45 genes; every member is in the + arm (projection on the module's main direction 0.733). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (6.0, 44.7); signed map (-30.0, 34.7). **Vector** length 49.1, 10.4% of its response variance represented; |z| ≥ 3 in 597 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.9 | +5.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +5.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.6 | +4.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.3 | +5.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.2 | +6.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | -1.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.5 | +3.1 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.0 | +1.3 |
|  | [[Infigratinib (drug)]] 0.05 µM |  | +0.9 | +1.6 |
| fall | [[Digitoxin (drug)]] 0.05 µM |  | -1.6 | -3.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -1.4 | -1.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -1.3 | -3.4 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.3 | -1.0 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.3 | -1.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.1 | -0.1 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.0 | -1.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.0 | -1.4 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.0 | +0.4 |
|  | [[(S)-Crizotinib (drug)]] 0.05 µM |  | -0.9 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | dihydropyrimidinase like 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.3 — chr10:132,186,948-132,205,759 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ULIP4, DRP-4, CRMP3 |
| Gene groups (HGNC) | M38 metallopeptidases |
| Hallmark sets | GLYCOLYSIS, HYPOXIA |
| Reactome | 4 pathways, smallest: CRMPs in Sema3A signaling; Semaphorin interactions; Axon guidance |
| Matched by | ensembl_id |

**Function**, from UniProt [O14531](https://www.uniprot.org/uniprotkb/O14531) (Dihydropyrimidinase-related protein 4):

> Necessary for signaling by class 3 semaphorins and subsequent remodeling of the cytoskeleton. Plays a role in axon guidance, neuronal growth cone collapse and cell migration (By similarity).

**Summary**, from NCBI Gene [10570](https://www.ncbi.nlm.nih.gov/gene/10570):

> Enables filamin binding activity. Predicted to be involved in nervous system development. Predicted to be located in cytoplasm. Predicted to be active in cytosol. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:3016](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3016) · Entrez [10570](https://www.ncbi.nlm.nih.gov/gene/10570) · UniProt [O14531](https://www.uniprot.org/uniprotkb/O14531) · Ensembl [ENSG00000151640](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151640)

## Data

Gene col 7544: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7544); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7544, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7544]; `tensor/DDL_lfc|DDL_z.npy` [7544]; `embed/gene_vectors.npy` [7544]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7544 or target_col == 7544). Every well: [[DPYSL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DPYSL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
