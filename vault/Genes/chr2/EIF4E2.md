---
symbol: "EIF4E2"
type: "gene"
col: 5782
ensembl_id: "ENSG00000135930"
name: "eukaryotic translation initiation factor 4E family member 2"
location: "2q37.1"
module: 119
arm: "+"
pooled_cpm: 63.98
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 14
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/119"]
generated_by: "tahoemap"
---

# EIF4E2

*eukaryotic translation initiation factor 4E family member 2* — 2q37.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 2.02× (z +9.6, q 3e-19, up in 32 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 1 line (PANC-1 3.04×).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.591× (z -13.2, q 4e-37, down in 35 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 0.790× (z -8.7, q 6e-16, down in 27 of 48 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 7 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[POP7]] (+0.74, fdr 1e-05), [[SCNM1]] (+0.69, fdr 1e-05), [[MRPL55]] (+0.69, fdr 7e-06); moves opposite to [[SEPTIN11]] (-0.54, fdr 5e-05).
> It is in [[Module 119]], a single-armed module (Mitochondrial ribosome-associated quality control).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5782.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 1 line (PANC-1 3.04×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.02×** | +9.6 | 3e-19 | 32/49 (PANC-1, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~6% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.032 | 20/48 (SW1417, PANC-1, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | 1.14× | +3.4 | 0.11 | 16/48 (HOP62, hTERT-HPNE, …) | inconsistent across doses | low cells (technical?) |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | 1.19× | +3.3 | 0.13 | 15/48 (SHP-77, RPMI-7951, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Infigratinib (drug)]] 0.05 µM |  | 1.13× | +3.2 | 0.18 | 8/48 (MIA PaCa-2, A-427, …) | inconsistent across doses |  |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.12× | +3.1 | 0.20 | 13/48 (C-33 A, KATO III, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 10 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5782.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.591×** | -13.2 | 4e-37 | 35/44 (NCI-H23, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.656×** | -11.0 | 1e-25 | 34/49 (NCI-H2347, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.645×** | -10.6 | 7e-24 | 32/45 (NCI-H2347, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.790×** | -8.7 | 6e-16 | 27/48 (SNU-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.727×** | -8.3 | 1e-14 | 33/48 (NCI-H1573, HOP62, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.733×** | -8.1 | 6e-14 | 31/48 (A-172, A498, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~10% of this change | **0.810×** | -7.7 | 9e-13 | 25/49 (A-172, AsPC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.795×** | -5.7 | 7e-07 | 25/48 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.802×** | -5.5 | 2e-06 | 27/50 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~7% here) |
| [[Tucidinostat (drug)]] 5 µM |  | 0.862× | -5.4 | 3e-06 | 22/48 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.817×** | -5.2 | 8e-06 | 23/48 (BT-474, J82, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.823×** | -5.0 | 2e-05 | 22/48 (NCI-H2347, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.829×** | -4.9 | 5e-05 | 24/48 (NCI-H2347, H4, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | **0.829×** | -4.9 | 5e-05 | 20/48 (A-172, A498, …) | all doses, flat |  |
| [[Brivudine (drug)]] 5 µM |  | **0.711×** | -4.7 | 1e-04 | 23/49 (A498, NCI-H23, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | 0.847× | -4.3 | 6e-04 | 14/48 (NCI-H2347, hTERT-HPNE, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | 0.862× | -3.6 | 0.011 | 17/47 (H4, NCI-H1573, …) | all doses, flat | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | 0.874× | -3.5 | 0.014 | 21/48 (HOP62, SK-MEL-2, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | 0.879× | -3.3 | 0.023 | 14/48 (SW 1088, AsPC-1, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | 0.883× | -3.2 | 0.034 | 9/48 (NCI-H23, H4, …) | rises with dose |  |
| [[Bergenin (drug)]] 0.5 µM |  | 0.891× | -3.0 | 0.066 | 13/48 (CHP-212, hTERT-HPNE, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5782. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 64.9 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -19.7) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.531× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 86.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.153× (z -26.4) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.533× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 67.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.289× (z -15.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.520× (z -12.4) |
| [[AsPC-1 (line)]] | alt | 85.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.506× (z -11.7) |
| [[NCI-H2030 (line)]] | alt | 77.9 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.139× (z -22.0) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 78.5 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.530× (z -11.5) ⚠ cell-cycle shift, explains ~10% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.518× (z -8.5) |
| [[HEC-1-A (line)]] | alt | 50.8 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.372× (z -11.4) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 63.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.488× (z -9.1) |
| [[SNU-1 (line)]] | wt | 78.7 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -19.3) |
| [[C-33 A (line)]] | alt | 59.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.227× (z -12.6) ⚠ toxic; transcription drop |
| [[CFPAC-1 (line)]] | alt | 66.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.371× (z -11.4) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 48.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -14.6) ⚠ toxic; transcription drop |
| [[HS-578T (line)]] | alt | 76.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.392× (z -9.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 61.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.425× (z -9.4) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 59.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.362× (z -11.9) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 60.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.529× (z -8.8) |
| [[PANC-1 (line)]] | alt | 62.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 3.04× (z +9.2) | — |
| [[RPMI-7951 (line)]] | alt | 81.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.308× (z -11.6) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 67.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.369× (z -9.9) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 58.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.243× (z -14.2) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 69.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.378× (z -10.1) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 73.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.367× (z -11.4) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 51.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.471× (z -10.4) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 48.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 80.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 73.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 58.5 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 80.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 75.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 52.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 57.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 45.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 51.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 59.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 70.9 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 61.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 69.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 59.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 71.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 55.8 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 48.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 79.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 67.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 55.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5782), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 7 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[POP7]] | +0.74 | +0.56 / +0.67 | both halves | 1e-05 |  |
| [[SCNM1]] | +0.69 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[MRPL55]] | +0.69 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[C16orf91]] | +0.66 | +0.32 / +0.64 | both halves | 2e-04 |  |
| [[CCDC12]] | +0.66 | +0.69 / +0.65 | both halves | 7e-06 |  |
| [[KLHDC10]] | +0.65 | +0.54 / +0.65 | both halves | 1e-05 |  |
| [[TFIP11]] | +0.64 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[EYA3]] | +0.64 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[NUP54]] | +0.63 | +0.55 / +0.56 | both halves | 1e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[MRPS12]] | +0.63 | +0.25 / +0.65 | both halves | 4e-04 |  |
| [[NCBP2AS2]] | +0.63 | +0.27 / +0.61 | both halves | 3e-04 |  |
| [[SF3B5]] ⚠ | +0.62 | +0.24 / +0.61 | both halves | 4e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ESS2]] | +0.62 | +0.64 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN11]] | -0.54 | -0.40 / -0.50 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises EIF4E2's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 119]] — Mitochondrial ribosome-associated quality control; 41 genes; every member is in the + arm (projection on the module's main direction 0.693). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.32; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-41.6, -8.8); signed map (-12.1, -9.8). **Vector** length 90.1, 19.5% of its response variance represented; |z| ≥ 3 in 819 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +2.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +4.7 | +0.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~11% of this change | +4.2 | -4.3 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~11% of this change | +3.9 | -4.9 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~49% of this change | +3.3 | +3.4 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.6 | +3.9 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.0 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.9 | +0.9 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.8 | +2.0 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | +1.4 | +3.3 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.2 | -11.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.0 | -13.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.4 | -4.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.0 | -10.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -2.9 | -2.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -3.5 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -2.1 | -2.6 |
|  | [[Berberine (chloride hydrate) (drug)]] 5 µM |  | -1.7 | -0.6 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -1.6 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.6 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 4E family member 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q37.1 — chr2:232,550,659-232,583,644 (+) |
| Ensembl biotype | protein_coding |
| Also known as | IF4e, 4EHP; previously EIF4EL3 |
| Reactome | 4 pathways, smallest: ISG15 antiviral mechanism; Antimicrobial mechanism of IFN-stimulated genes; Interferon Signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [O60573](https://www.uniprot.org/uniprotkb/O60573) (Eukaryotic translation initiation factor 4E type 2):

> Recognizes and binds the 7-methylguanosine-containing mRNA cap during an early step in the initiation. Acts as a repressor of translation initiation. In contrast to EIF4E, it is unable to bind eIF4G (EIF4G1, EIF4G2 or EIF4G3), suggesting that it acts by competing with EIF4E and block assembly of eIF4F at the cap (By similarity). In P-bodies, component of a complex that promotes miRNA-mediated translational repression. Involved in virus-induced host response by mediating miRNA MIR34A-induced …

**Summary**, from NCBI Gene [9470](https://www.ncbi.nlm.nih.gov/gene/9470):

> Enables RNA 7-methylguanosine cap binding activity; mRNA cap binding activity; and ubiquitin protein ligase binding activity. Involved in negative regulation of translational initiation; negative regulation of type I interferon-mediated signaling pathway; and rescue of stalled cytosolic ribosome. Acts upstream of with a positive effect on miRNA-mediated gene silencing by inhibition of translation. Acts upstream of or within negative regulation of translation. Located in P-body and cytosol. …

**Accessions** — [HGNC:3293](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3293) · Entrez [9470](https://www.ncbi.nlm.nih.gov/gene/9470) · UniProt [O60573](https://www.uniprot.org/uniprotkb/O60573) · Ensembl [ENSG00000135930](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135930)

## Data

Gene col 5782: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5782); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5782, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5782]; `tensor/DDL_lfc|DDL_z.npy` [5782]; `embed/gene_vectors.npy` [5782]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5782 or target_col == 5782). Every well: [[EIF4E2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF4E2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
