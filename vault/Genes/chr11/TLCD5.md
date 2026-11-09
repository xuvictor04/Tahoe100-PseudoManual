---
symbol: "TLCD5"
type: "gene"
col: 11176
ensembl_id: "ENSG00000181264"
name: "TLC domain containing 5"
location: "11q23.3"
module: 14
arm: "+"
pooled_cpm: 7.75
n_lines_expressing: 45
n_dd_up: 15
n_dd_down: 13
n_dd_up_clean: 10
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 0
direction_downstream: 2
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# TLCD5

*TLC domain containing 5* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 15 drug-doses (5 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.65× (z +5.6, q 1e-05, up in 16 of 27 measured lines) ⚠ toxic. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.39× (z +5.4, q 2e-05, up in 10 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.486× (z -8.3, q 6e-14, down in 27 of 42 measured lines) ⚠ cell-cycle shift, explains ~47% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.335× (z -6.0, q 4e-07, down in 25 of 41 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC49A4]] (+0.62, fdr 1e-05), [[BEND7]] (+0.60, fdr 1e-05), [[STAT5B]] (+0.60, fdr 3e-05); moves opposite to [[MYH10]] (-0.51, fdr 4e-05), [[TRIB2]] (-0.49, fdr 3e-05), [[SLC25A10]] (-0.49, fdr 4e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 2 go from it, the strongest it → [[ITSN2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 5 with an alert ⚠. 15 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11176.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +5.6 | 1e-05 | 16/27 (SW480, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **1.39×** | +5.4 | 2e-05 | 10/42 (SW480, HOP62, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~17% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.34×** | +4.8 | 3e-04 | 16/41 (KATO III, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.49×** | +4.5 | 0.001 | 2/12 (NCI-H2347, PANC-1) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.62×** | +4.0 | 0.006 | 8/39 (A498, SHP-77, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +4.0 | 0.006 | 12/42 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 0.5 µM |  | **1.36×** | +3.6 | 0.029 | 5/36 (hTERT-HPNE, C-33 A, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.35×** | +3.5 | 0.033 | 7/28 (PANC-1, SNU-423, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.059 | 8/41 (SW480, A498, …) | all doses, flat | noisy plate (z scaled) |
| [[Pimozide (drug)]] 0.5 µM | ⚠ transcription drop | **1.33×** | +3.3 | 0.059 | 4/39 (SW1417, NCI-H2347, …) | inconsistent across doses |  |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.32×** | +3.2 | 0.067 | 7/37 (HCT15, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[18β-Glycyrrhetinic acid (drug)]] 5 µM |  | **1.21×** | +3.2 | 0.068 | 5/42 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.080 | 7/42 (NCI-H1573, HS-578T, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.30×** | +3.1 | 0.084 | 12/41 (HT-29, KATO III, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.1 | 0.084 | 3/41 (MIA PaCa-2, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11176.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.486×** | -8.3 | 6e-14 | 27/42 (RKO, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.574×** | -6.4 | 5e-08 | 23/42 (RKO, A-427, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.335×** | -6.0 | 4e-07 | 25/41 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.873× | -5.4 | 1e-05 | 14/43 (SHP-77, KATO III, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.650×** | -4.9 | 9e-05 | 17/42 (NCI-H1573, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.412×** | -4.9 | 1e-04 | 18/36 (RKO, SW480, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.753×** | -4.6 | 4e-04 | 17/35 (NCI-H1573, NCI-H23, …) | top dose only |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.661×** | -4.5 | 5e-04 | 14/40 (NCI-H1573, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.783×** | -4.0 | 0.005 | 13/43 (A498, PANC-1, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~88% of this change | **0.709×** | -3.9 | 0.005 | 17/42 (NCI-H23, RKO, …) | top dose only | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.726×** | -3.7 | 0.012 | 13/42 (SNU-1, NCI-H1573, …) | top dose only | composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.818×** | -3.2 | 0.057 | 17/38 (NCI-H1573, NCI-H460, …) | top dose only | cell-cycle shift (explains ~4% here); composition shift |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.687×** | -3.1 | 0.086 | 5/42 (NCI-H661, RKO, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.765×** | -3.1 | 0.086 | 11/41 (SW 1271, NCI-H1573, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | 0.761× | -3.0 | 0.10 | 12/38 (C-33 A, SW480, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.54 per unit of S-phase module lfc, +0.09 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11176. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1573 (line)]] | alt | 28.1 | 0 | 4 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.119× (z -20.0) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.225× (z -14.0) |
| [[A-427 (line)]] | wt | 9.48 | 0 | 3 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.130× (z -10.1) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[RKO (line)]] | wt | 20.6 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.160× (z -10.8) ⚠ cell-cycle shift, explains ~52% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0406× (z -9.0) |
| [[C-33 A (line)]] | alt | 20.4 | 0 | 2 (2 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0835× (z -12.5) ⚠ cell-cycle shift, would explain all of this change |
| [[NCI-H23 (line)]] | alt | 11.8 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.199× (z -8.6) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.324× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 5.03 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -10.7) |
| [[A549 (line)]] | wt | 9.31 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.274× (z -9.2) |
| [[HepG2_C3A (line)]] | wt | 8.39 | 0 | 1 | — | [[Valdecoxib (drug)]] 0.05 µM 0.0764× (z -9.1) |
| [[SHP-77 (line)]] | alt | 10.8 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.128× (z -9.5) |
| [[A-172 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.88 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.71 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.91 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.06 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.36 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 6.24 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.20 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 4.19 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.46 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 7.23 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.60 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 9.57 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.784 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 10.3 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.98 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.03 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.52 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.31 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.55 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.46 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.70 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.66 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.82 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 10.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11176), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC49A4]] | +0.62 | +0.68 / +0.55 | both halves | 1e-05 |  |
| [[BEND7]] | +0.60 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[STAT5B]] | +0.60 | +0.55 / +0.46 | both halves | 3e-05 |  |
| [[BTG3]] | +0.59 | +0.45 / +0.58 | both halves | 3e-05 |  |
| [[ZDHHC1]] | +0.55 | +0.49 / +0.50 | both halves | 1e-05 |  |
| [[RAB9A]] | +0.55 | +0.48 / +0.54 | both halves | 2e-05 |  |
| [[ZSWIM7]] | +0.55 | +0.59 / +0.59 | both halves | 7e-06 |  |
| [[ZNF302]] | +0.55 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[RAB32]] | +0.54 | +0.37 / +0.60 | both halves | 8e-05 |  |
| [[ZNRF2P2]] | +0.53 | +0.57 / +0.40 | both halves | 5e-05 |  |
| [[RWDD3]] | +0.53 | +0.42 / +0.50 | both halves | 4e-05 |  |
| [[C5orf24]] | +0.52 | +0.47 / +0.50 | both halves | 2e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MYH10]] | -0.51 | -0.41 / -0.52 | both halves | 4e-05 |  |
| [[TRIB2]] | -0.49 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[SLC25A10]] | -0.49 | -0.41 / -0.42 | both halves | 4e-05 |  |
| [[TNIK]] | -0.48 | -0.51 / -0.31 | both halves | 2e-04 | STRING 422 |
| [[TPM3]] | -0.48 | -0.41 / -0.45 | both halves | 4e-05 |  |
| [[TXN2]] | -0.48 | -0.45 / -0.37 | both halves | 7e-05 |  |
| [[KNTC1]] | -0.47 | -0.35 / -0.59 | both halves | 1e-04 |  |
| [[GDI2]] | -0.46 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[SYS1-DBNDD2]] | -0.45 | -0.41 / -0.43 | both halves | 4e-05 |  |
| [[MYCBP]] | -0.44 | -0.30 / -0.41 | both halves | 2e-04 |  |
| [[ADSS1]] | -0.44 | -0.41 / -0.36 | both halves | 1e-04 |  |
| [[EIF2AK1]] | -0.44 | -0.32 / -0.44 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITSN2]] | B | TLCD5 activity raises ITSN2's level | lines that do not express TLCD5 (5) vs lines expressing it (45) | 1.50× lower at baseline in the lines without TLCD5 | 0.022 | ⚠ within organs, on part of the lines; also absent: DNAJB5, SYDE2, CEP170; maybe low, not absent |
| [[GDI2]] | B | TLCD5 activity raises GDI2's level | lines that do not express TLCD5 (5) vs lines expressing it (45) | 1.23× lower at baseline in the lines without TLCD5 | 0.089 | ⚠ within organs, on part of the lines; also absent: DNAJB5, SYDE2, CEP170; maybe low, not absent |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.308). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-13.4, 12.0); signed map (7.2, -6.8). **Vector** length 60.0, 9.36% of its response variance represented; |z| ≥ 3 in 770 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +3.5 | +5.4 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.4 | +5.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.4 | +1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +2.3 | +3.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +4.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +3.1 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.9 | +1.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.9 | +2.8 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.8 | +3.3 |
| fall | [[TAK-901 (drug)]] 5 µM |  | -2.5 | -6.0 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -4.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -4.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -1.9 | -3.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~47% of this change | -1.8 | -8.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.3 | -3.1 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.1 | -1.8 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | -1.1 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | TLC domain containing 5 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:120,325,296-120,333,686 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC17839; previously TMEM136 |
| Gene groups (HGNC) | TLC domain containing |
| Matched by | ensembl_id |

UniProt [Q6ZRR5](https://www.uniprot.org/uniprotkb/Q6ZRR5) carries no function annotation.

**Summary**, from NCBI Gene [219902](https://www.ncbi.nlm.nih.gov/gene/219902):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28280](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28280) · Entrez [219902](https://www.ncbi.nlm.nih.gov/gene/219902) · UniProt [Q6ZRR5](https://www.uniprot.org/uniprotkb/Q6ZRR5) · Ensembl [ENSG00000181264](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000181264)

## Data

Gene col 11176: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11176); `tables/drug_effects.parquet` (30 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11176, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11176]; `tensor/DDL_lfc|DDL_z.npy` [11176]; `embed/gene_vectors.npy` [11176]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11176 or target_col == 11176). Every well: [[TLCD5 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TLCD5.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
