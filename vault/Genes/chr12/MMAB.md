---
symbol: "MMAB"
type: "gene"
col: 6304
ensembl_id: "ENSG00000139428"
name: "metabolism of cobalamin associated B"
location: "12q24.11"
module: 86
arm: "+"
pooled_cpm: 11.19
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 26
n_dd_up_clean: 14
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/086"]
generated_by: "tahoemap"
---

# MMAB

*metabolism of cobalamin associated B* — 12q24.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.38× (z +11.7, q 1e-28, up in 28 of 34 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Cepharanthine (drug)]] 5 µM: 1.76× (z +10.8, q 9e-25, up in 37 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.462× (z -10.3, q 3e-22, down in 40 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MVK]] (+0.77, fdr 7e-06, ⚠ same locus), [[DHCR7]] (+0.70, fdr 7e-06), [[ACAT2]] (+0.68, fdr 7e-06), [[IDI1]] (+0.66, fdr 1e-05); moves opposite to [[MAMLD1]] (-0.38, fdr 2e-04), [[CAP1]] (-0.35, fdr 9e-05), [[PRKG1-AS1]] (-0.33, fdr 4e-04).
> It is in [[Module 086]], a single-armed module (cholesterol synthesis).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[EPB41]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6304.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.38×** | +11.7 | 1e-28 | 28/34 (J82, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Cepharanthine (drug)]] 5 µM |  | **1.76×** | +10.8 | 9e-25 | 37/48 (LoVo, A549, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.26×** | +10.6 | 8e-24 | 17/21 (NCI-H460, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Berbamine (drug)]] 5 µM |  | **1.73×** | +10.5 | 2e-23 | 37/48 (LoVo, HT-29, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.85×** | +7.6 | 2e-12 | 19/25 (NCI-H2347, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Entrectinib (drug)]] 5 µM |  | **1.59×** | +6.2 | 4e-08 | 26/46 (SNU-423, A498, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.46×** | +5.1 | 3e-05 | 17/46 (HOP62, SNU-423, …) | rises with dose |  |
| [[Adagrasib (drug)]] 5 µM |  | **1.46×** | +4.9 | 8e-05 | 15/47 (NCI-H1792, NCI-H460, …) | top dose only |  |
| [[Posaconazole (drug)]] 5 µM |  | **1.41×** | +4.4 | 6e-04 | 15/47 (HEC-1-A, NCI-H1573, …) | rises with dose | plate-row cell shift |
| [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.4 | 7e-04 | 13/47 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.37×** | +4.2 | 0.001 | 11/47 (HT-29, SW480, …) | top dose only |  |
| [[Almonertinib (mesylate) (drug)]] 5 µM |  | **1.36×** | +4.0 | 0.003 | 15/47 (SNU-423, NCI-H460, …) | top dose only | plate-row cell shift |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.004 | 9/47 (SNU-423, LS 180, …) | top dose only |  |
| [[Ritonavir (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.006 | 8/48 (PANC-1, LS 180, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +3.5 | 0.017 | 10/45 (NCI-H2030, A549, …) | top dose only |  |
| [[(S)-Crizotinib (drug)]] 5 µM |  | **1.30×** | +3.4 | 0.023 | 9/47 (HOP62, HS-578T, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.28×** | +3.4 | 0.026 | 7/47 (SNU-423, HOP62, …) | rises with dose |  |
| [[Almonertinib (hydrochloride) (drug)]] 5 µM |  | 1.18× | +3.1 | 0.050 | 11/47 (PANC-1, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6304.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.462×** | -10.3 | 3e-22 | 40/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.503×** | -9.2 | 1e-17 | 35/45 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.521×** | -8.7 | 5e-16 | 36/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.542×** | -8.2 | 4e-14 | 33/47 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.558×** | -7.8 | 8e-13 | 28/46 (NCI-H23, SW480, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.434×** | -5.8 | 5e-07 | 23/43 (MIA PaCa-2, SK-MEL-2, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.446×** | -5.7 | 1e-06 | 25/47 (HCT15, SW480, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.656×** | -5.6 | 1e-06 | 24/47 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.686×** | -4.8 | 1e-04 | 19/47 (NCI-H2347, RKO, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.701×** | -4.7 | 1e-04 | 15/47 (HS-578T, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **0.778×** | -4.7 | 1e-04 | 17/44 (SW480, COLO 205, …) | top dose only |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.702×** | -4.7 | 1e-04 | 19/47 (SK-MEL-2, LOX-IMVI, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.779×** | -4.7 | 1e-04 | 21/48 (C32, HEC-1-A, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.708×** | -4.4 | 4e-04 | 18/43 (SW480, NCI-H23, …) | top dose only | cell-cycle shift (explains ~20% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.801×** | -4.2 | 0.001 | 23/46 (RPMI-7951, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **0.738×** | -4.0 | 0.002 | 12/44 (HOP62, SW48, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Asciminib (drug)]] 5 µM |  | **0.742×** | -4.0 | 0.002 | 11/47 (BT-474, KATO III, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.773×** | -3.4 | 0.018 | 14/46 (PANC-1, SNU-1, …) | two highest doses | cell-cycle shift (explains ~8% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6304. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 12.5 | 0 | 6 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.150× (z -15.2) |
| [[LoVo (line)]] | wt | 13.6 | 3 (1 ⚠) | 0 | [[Berbamine (drug)]] 5 µM 2.51× (z +8.8) | — |
| [[PANC-1 (line)]] | alt | 17.4 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.196× (z -13.3) |
| [[NCI-H1792 (line)]] | alt | 12.8 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.101× (z -11.1) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 12.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.21× (z +9.7) ⚠ toxic; transcription drop | — |
| [[COLO 205 (line)]] | alt | 14.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.238× (z -8.7) ⚠ cell-cycle shift, explains ~17% of this change |
| [[HCT15 (line)]] | alt | 14.6 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.108× (z -9.5) ⚠ transcription drop |
| [[HOP62 (line)]] | alt | 9.98 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.180× (z -10.1) |
| [[J82 (line)]] | alt | 13.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.69× (z +9.0) ⚠ toxic; transcription drop | — |
| [[NCI-H23 (line)]] | alt | 10.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0635× (z -13.0) |
| [[RKO (line)]] | wt | 9.72 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0374× (z -13.2) |
| [[RPMI-7951 (line)]] | alt | 11.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -11.2) ⚠ cell-cycle shift, explains ~11% of this change |
| [[A-172 (line)]] | wt | 6.89 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.32 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.36 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 9.68 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.70 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.39 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 9.78 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.65 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 7.33 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.36 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.66 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.34 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.48 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 7.00 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6304), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*96 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MVK]] | +0.77 | +0.81 / +0.77 | both halves | 7e-06 | STRING 778; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[DHCR7]] | +0.70 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[ACAT2]] | +0.68 | +0.73 / +0.60 | both halves | 7e-06 |  |
| [[IDI1]] | +0.66 | +0.74 / +0.54 | both halves | 1e-05 |  |
| [[CYP51A1]] | +0.66 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[FDPS]] | +0.66 | +0.66 / +0.58 | both halves | 7e-06 |  |
| [[HMGCS1]] | +0.65 | +0.75 / +0.49 | both halves | 1e-05 |  |
| [[SC5D]] | +0.64 | +0.71 / +0.52 | both halves | 1e-05 |  |
| [[SREBF2]] | +0.63 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[HMGCR]] | +0.63 | +0.70 / +0.52 | both halves | 1e-05 |  |
| [[MVD]] | +0.62 | +0.62 / +0.58 | both halves | 7e-06 |  |
| [[ERG28]] | +0.62 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[ACSS2]] | +0.61 | +0.62 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*4 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAMLD1]] | -0.38 | -0.32 / -0.38 | both halves | 2e-04 |  |
| [[CAP1]] | -0.35 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[PRKG1-AS1]] | -0.33 | -0.30 / -0.26 | both halves | 4e-04 |  |
| [[BMP6]] | -0.33 | -0.36 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EPB41]] | C | EPB41 activity raises MMAB's level | lines that do not express EPB41 (3) vs lines expressing it (47) | 1.55× lower at baseline in the lines without EPB41 | 0.044 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: BRME1, NRTN, CSRP1-AS1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 086]] — cholesterol synthesis; 51 genes; every member is in the + arm (projection on the module's main direction 0.738). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (22.1, -49.2); signed map (-52.9, 32.0). **Vector** length 85.1, 17.7% of its response variance represented; |z| ≥ 3 in 1,023 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *cholesterol synthesis* (control, mean cos +0.59 to 22); *Cholesterol biosynthesis* (reactome, mean cos +0.60 to 20); *cholesterol homeostasis* (hallmark, mean cos +0.60 to 24).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.8 | +10.6 |
|  | [[Cepharanthine (drug)]] 5 µM |  | +5.7 | +10.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.6 | +11.7 |
|  | [[Berbamine (drug)]] 5 µM |  | +5.2 | +10.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.3 | +7.6 |
|  | [[Entrectinib (drug)]] 5 µM |  | +3.2 | +6.2 |
|  | [[Almonertinib (mesylate) (drug)]] 5 µM |  | +2.9 | +4.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.9 | +3.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.6 | -7.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -3.6 | -8.2 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -3.4 | -10.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.3 | -3.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -2.7 | -9.2 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.6 | -4.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.3 | -4.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | metabolism of cobalamin associated B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.11 — chr12:109,553,715-109,573,580 (-) |
| Ensembl biotype | protein_coding |
| Also known as | cblB, CFAP23 |
| Gene groups (HGNC) | Cilia and flagella associated |
| Reactome | 7 pathways, smallest: Cobalamin (Cbl) metabolism; Defects in cobalamin (B12) metabolism; Cobalamin (Cbl, vitamin B12) transport and metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96EY8](https://www.uniprot.org/uniprotkb/Q96EY8) (Corrinoid adenosyltransferase MMAB):

> Converts cob(I)alamin to adenosylcobalamin (adenosylcob(III)alamin), a coenzyme for methylmalonyl-CoA mutase, therefore participates in the final step of the vitamin B12 conversion. Generates adenosylcobalamin (AdoCbl) and directly delivers the cofactor to MUT in a transfer that is stimulated by ATP-binding to MMAB and gated by MMAA (Probable).

**Summary**, from NCBI Gene [326625](https://www.ncbi.nlm.nih.gov/gene/326625):

> This gene encodes a protein that catalyzes the final step in the conversion of vitamin B(12) into adenosylcobalamin (AdoCbl), a vitamin B12-containing coenzyme for methylmalonyl-CoA mutase. Mutations in the gene are the cause of vitamin B12-dependent methylmalonic aciduria linked to the cblB complementation group. Alternatively spliced transcript variants have been found. [provided by RefSeq, Apr 2011]

**Accessions** — [HGNC:19331](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19331) · Entrez [326625](https://www.ncbi.nlm.nih.gov/gene/326625) · UniProt [Q96EY8](https://www.uniprot.org/uniprotkb/Q96EY8) · Ensembl [ENSG00000139428](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139428)

## Data

Gene col 6304: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6304); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6304, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6304]; `tensor/DDL_lfc|DDL_z.npy` [6304]; `embed/gene_vectors.npy` [6304]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6304 or target_col == 6304). Every well: [[MMAB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MMAB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
