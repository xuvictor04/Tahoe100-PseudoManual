---
symbol: "ALKBH6"
type: "gene"
col: 14191
ensembl_id: "ENSG00000239382"
name: "alkB homolog 6, nucleotide demethylase"
location: "19q13.12"
module: 72
arm: "+"
pooled_cpm: 4.83
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 13
n_dd_up_clean: 12
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/072"]
generated_by: "tahoemap"
---

# ALKBH6

*alkB homolog 6, nucleotide demethylase* — 19q13.12

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.88× (z +9.9, q 2e-20, up in 30 of 38 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.572× (z -8.7, q 2e-15, down in 29 of 40 measured lines) ⚠ cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Digitoxin (drug)]] 0.5 µM: 0.505× (z -7.5, q 1e-11, down in 25 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AHSA2P]] (+0.70, fdr 7e-06), [[OGFOD2]] (+0.67, fdr 7e-06), [[BABAM1]] (+0.67, fdr 7e-06); moves opposite to [[SPTSSA]] (-0.52, fdr 4e-05), [[SERBP1]] (-0.48, fdr 2e-04), [[H2AZ2]] (-0.48, fdr 7e-05).
> It is in [[Module 072]], a single-armed module (Degradation of DVL).
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14191.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.88×** | +9.9 | 2e-20 | 30/38 (NCI-H2030, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.18×** | +8.6 | 2e-15 | 33/43 (HEC-1-A, KATO III, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +8.2 | 6e-14 | 7/8 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.12×** | +7.8 | 7e-13 | 29/43 (NCI-H23, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~20% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.94×** | +7.3 | 3e-11 | 28/46 (HEC-1-A, C32, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.57×** | +7.1 | 1e-10 | 16/46 (RKO, A-172, …) | rises with dose | low cells (technical?); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.72×** | +6.0 | 2e-07 | 10/26 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +5.6 | 2e-06 | 10/48 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.71×** | +5.5 | 2e-06 | 7/13 (HEC-1-A, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.60×** | +5.0 | 4e-05 | 17/36 (HEC-1-A, HS-578T, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +4.1 | 0.003 | 7/37 (HS-578T, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.39×** | +3.7 | 0.012 | 13/43 (HOP62, C32, …) | top dose only | position effect removed |
| [[Bestatin (hydrochloride) (drug)]] 0.05 µM |  | **1.37×** | +3.5 | 0.021 | 4/44 (SW 900, RPMI-7951, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.25×** | +3.4 | 0.023 | 11/47 (NCI-H2347, HEC-1-A, …) | top dose only |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.52×** | +3.3 | 0.036 | 7/32 (LS 180, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Penfluridol (drug)]] 0.5 µM |  | **1.32×** | +3.1 | 0.066 | 3/46 (NCI-H2030, AN3 CA, …) | inconsistent across doses | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.46×** | +3.0 | 0.079 | 4/41 (Hs 766T, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 6 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14191.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.572×** | -8.7 | 2e-15 | 29/40 (NCI-H460, SW 900, …) | rises with dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.505×** | -7.5 | 1e-11 | 25/45 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.596×** | -5.7 | 2e-06 | 21/47 (SW 900, HT-29, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.603×** | -5.6 | 3e-06 | 21/38 (SW480, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.644×** | -4.8 | 1e-04 | 16/43 (A-427, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.739×** | -4.7 | 2e-04 | 19/44 (NCI-H460, SW1417, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.686×** | -4.2 | 0.002 | 9/46 (NCI-H460, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.686×** | -4.1 | 0.002 | 13/45 (SW480, BT-474, …) | all doses, stronger at high dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.687×** | -4.1 | 0.002 | 15/39 (NCI-H23, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.496×** | -4.0 | 0.003 | 6/44 (NCI-H1792, H4, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.739×** | -3.3 | 0.046 | 9/46 (SW480, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.743×** | -3.3 | 0.051 | 11/45 (NCI-H1792, HT-29, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.755×** | -3.1 | 0.088 | 11/44 (BT-474, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14191. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 5.45 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0431× (z -11.1) ⚠ cell-cycle shift, explains ~32% of this change |
| [[SW480 (line)]] | alt | 6.45 | 0 | 2 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0796× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Bimatoprost (drug)]] 0.5 µM 0.219× (z -9.0) |
| [[A498 (line)]] | wt | 3.42 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.123× (z -8.6) ⚠ toxic |
| [[HEC-1-A (line)]] | alt | 6.08 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 0.5 µM 0.164× (z -9.2) |
| [[HT-29 (line)]] | alt | 7.05 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0495× (z -14.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[LOX-IMVI (line)]] | wt | 3.53 | 0 | 1 | — | [[Naproxen (drug)]] 5 µM 0.0635× (z -8.9) |
| [[LS 180 (line)]] | wt | 5.04 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0718× (z -10.3) |
| [[MIA PaCa-2 (line)]] | alt | 6.00 | 0 | 1 | — | [[Ixazomib (drug)]] 0.05 µM 0.0923× (z -9.0) |
| [[NCI-H1792 (line)]] | alt | 4.77 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0385× (z -11.6) |
| [[NCI-H460 (line)]] | wt | 4.00 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.241× (z -9.6) ⚠ cell-cycle shift, explains ~48% of this change |
| [[PANC-1 (line)]] | alt | 6.78 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.215× (z -8.6) |
| [[SW1417 (line)]] | alt | 3.97 | 0 | 1 | — | [[Menadione (drug)]] 5 µM 0.0887× (z -8.7) |
| [[A-172 (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 5.63 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.44 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.09 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.67 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.27 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.25 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.59 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 4.84 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.38 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.53 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 2.37 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 3.01 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 4.87 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.04 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 4.79 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.66 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.75 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.94 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 6.61 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.83 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.61 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 2.93 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14191), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*97 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AHSA2P]] | +0.70 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[OGFOD2]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[BABAM1]] | +0.67 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[MRPL18]] | +0.65 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[SERPINH1]] | +0.63 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[EXOC7]] | +0.62 | +0.58 / +0.60 | both halves | 8e-06 |  |
| [[VIPAS39]] | +0.61 | +0.59 / +0.57 | both halves | 1e-05 |  |
| [[SUPT7L]] | +0.60 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[IGHMBP2]] | +0.59 | +0.54 / +0.55 | both halves | 1e-05 |  |
| [[PSMB4]] | +0.58 | +0.64 / +0.46 | both halves | 2e-05 |  |
| [[VPS39]] | +0.58 | +0.47 / +0.57 | both halves | 2e-05 |  |
| [[MRPS15]] | +0.57 | +0.47 / +0.52 | both halves | 2e-05 |  |

## Genes that move opposite

*3 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPTSSA]] | -0.52 | -0.41 / -0.48 | both halves | 4e-05 |  |
| [[SERBP1]] | -0.48 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[H2AZ2]] | -0.48 | -0.44 / -0.38 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers ALKBH6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises ALKBH6's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity raises ALKBH6's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 072]] — Degradation of DVL; 69 genes; every member is in the + arm (projection on the module's main direction 0.641). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-16.9, -10.1); signed map (-25.0, -26.3). **Vector** length 64.1, 9.66% of its response variance represented; |z| ≥ 3 in 966 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DNA Double Strand Break Response* (reactome, mean cos +0.50 to 12).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.3 | +8.6 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.2 | +7.3 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.1 | +7.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.6 | +9.9 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | +4.2 | +7.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +3.7 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.3 | +3.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.3 | +2.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.9 | -4.7 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.8 | -7.5 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -2.3 | -5.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -2.3 | -3.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.2 | -4.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | -1.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.1 | -0.8 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.1 | -1.9 |
|  | [[Entecavir (monohydrate) (drug)]] 0.5 µM |  | -1.0 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | alkB homolog 6, nucleotide demethylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.12 — chr19:36,009,120-36,014,239 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC15677 |
| Gene groups (HGNC) | Alkylation repair homologs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q3KRA9](https://www.uniprot.org/uniprotkb/Q3KRA9) (Demethylase ALKBH6):

> Fe(2+)/2-oxoglutarate-dependent dioxygenase that catalyzes the oxidative demethylation of N-methylated nucleotide monophosphates, such as N(7)-methyl-GMP, N(7)-methyl-dGMP, N(1)-methyl-AMP, N(1)-methyl-dAMP and N(3)-methyl-dCMP, with N(7)-methyl-GMP and N(1)-methyl-AMP as the preferred endogenous substrates. Does not act on the corresponding methylated nucleobases or nucleosides lacking a phosphate group. May contribute to the sanitization of alkylation-damaged nucleotide pools, thereby …

**Summary**, from NCBI Gene [84964](https://www.ncbi.nlm.nih.gov/gene/84964):

> Enables 2-oxoglutarate-dependent dioxygenase activity. Located in cytoplasm and nucleus. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:28243](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28243) · Entrez [84964](https://www.ncbi.nlm.nih.gov/gene/84964) · UniProt [Q3KRA9](https://www.uniprot.org/uniprotkb/Q3KRA9) · Ensembl [ENSG00000239382](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000239382)

## Data

Gene col 14191: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14191); `tables/drug_effects.parquet` (32 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14191, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14191]; `tensor/DDL_lfc|DDL_z.npy` [14191]; `embed/gene_vectors.npy` [14191]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14191 or target_col == 14191). Every well: [[ALKBH6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ALKBH6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
