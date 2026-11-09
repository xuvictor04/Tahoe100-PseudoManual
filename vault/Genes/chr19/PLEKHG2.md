---
symbol: "PLEKHG2"
type: "gene"
col: 1643
ensembl_id: "ENSG00000090924"
name: "pleckstrin homology and RhoGEF domain containing G2"
location: "19q13.2"
module: 109
arm: "+"
pooled_cpm: 42.55
n_lines_expressing: 40
n_dd_up: 8
n_dd_down: 24
n_dd_up_clean: 5
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 0
direction_downstream: 4
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# PLEKHG2

*pleckstrin homology and RhoGEF domain containing G2* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.01× (z +12.5, q 8e-33, up in 25 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 24 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 0.5 µM: 0.543× (z -7.7, q 5e-12, down in 28 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[JUNB]] (+0.64, fdr 7e-06), [[EGR1]] (+0.64, fdr 7e-06), [[EGR2]] (+0.64, fdr 7e-06); moves opposite to [[CNIH4]] (-0.55, fdr 1e-05), [[VDAC3]] (-0.55, fdr 3e-05), [[MTM1]] (-0.55, fdr 1e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): none points to it; 4 go from it, the strongest it → [[KLF10]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1643.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.01×** | +12.5 | 8e-33 | 25/37 (C32, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.46×** | +8.2 | 6e-14 | 29/38 (NCI-H460, A-172, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **1.78×** | +7.0 | 5e-10 | 23/37 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.38×** | +5.7 | 1e-06 | 17/38 (RKO, C32, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +5.5 | 5e-06 | 15/33 (C32, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **1.95×** | +4.4 | 9e-04 | 18/35 (A-172, NCI-H2347, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.40×** | +4.1 | 0.004 | 9/25 (C32, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.35×** | +3.5 | 0.030 | 12/29 (CFPAC-1, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 24 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1643.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.543×** | -7.7 | 5e-12 | 28/37 (NCI-H23, HepG2/C3A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.545×** | -7.7 | 5e-12 | 29/37 (LOX-IMVI, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.557×** | -7.0 | 6e-10 | 26/37 (AN3 CA, NCI-H460, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.608×** | -6.3 | 4e-08 | 26/37 (NCI-H460, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.730×** | -5.6 | 2e-06 | 18/38 (A-427, Hs 766T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.640×** | -5.6 | 2e-06 | 21/36 (SW 900, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.667×** | -5.1 | 2e-05 | 18/38 (NCI-H2347, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~13% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.751×** | -5.1 | 2e-05 | 19/38 (NCI-H460, SHP-77, …) | all doses, stronger at high dose |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.671×** | -5.0 | 3e-05 | 18/37 (NCI-H23, LOX-IMVI, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.665×** | -5.0 | 4e-05 | 18/37 (NCI-H460, SHP-77, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.679×** | -4.5 | 3e-04 | 18/37 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.689×** | -4.5 | 3e-04 | 17/36 (A549, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.704×** | -4.4 | 4e-04 | 18/38 (AsPC-1, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~16% here) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.709×** | -4.4 | 5e-04 | 18/38 (NCI-H460, NCI-H1573, …) | all doses, flat |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.714×** | -4.1 | 0.002 | 20/37 (HT-29, A-427, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.778×** | -3.7 | 0.009 | 19/38 (NCI-H460, SHP-77, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, +0.04 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1643. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 37.8 | 3 (1 ⚠) | 7 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.77× (z +11.8) | [[Trametinib (drug)]] 5 µM 0.280× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.258× (z -10.2) |
| [[C32 (line)]] | wt | 13.6 | 2 (1 ⚠) | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 17.0× (z +13.5) | [[Pimozide (drug)]] 0.5 µM 0.0594× (z -9.6) ⚠ transcription drop |
| [[A549 (line)]] | wt | 60.8 | 2 | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 4.49× (z +9.0) | [[Dinaciclib (drug)]] 0.05 µM 0.136× (z -11.4) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 25.9 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +9.9) | — |
| [[LOX-IMVI (line)]] | wt | 25.3 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +8.9) | [[Ixazomib citrate (drug)]] 5 µM 0.293× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 25.5 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0744× (z -15.5) |
| [[COLO 205 (line)]] | alt | 15.7 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0923× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[H4 (line)]] | wt | 13.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.23× (z +9.0) | — |
| [[HCT15 (line)]] | alt | 20.4 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.103× (z -9.1) |
| [[Hs 766T (line)]] | wt | 24.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.33× (z +9.6) | — |
| [[hTERT-HPNE (line)]] | wt | 22.9 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.01× (z +10.8) | — |
| [[RPMI-7951 (line)]] | alt | 29.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.51× (z +12.9) | — |
| [[A-427 (line)]] | wt | 31.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 9.39 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 25.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.10 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 7.98 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 28.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.4 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.34 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.52 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 3.80 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 25.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.02 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.5 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 87.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 412 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 26.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 53.4 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.23 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.77 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 41.6 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1643), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[JUNB]] | +0.64 | +0.65 / +0.67 | both halves | 7e-06 |  |
| [[EGR1]] | +0.64 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[EGR2]] | +0.64 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[EGR3]] | +0.64 | +0.66 / +0.63 | both halves | 7e-06 |  |
| [[RGL2]] | +0.63 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[MCL1]] | +0.63 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[KBTBD2]] | +0.63 | +0.63 / +0.57 | both halves | 9e-06 |  |
| [[NR4A1]] | +0.62 | +0.70 / +0.64 | both halves | 7e-06 |  |
| [[HIVEP2-DT]] | +0.61 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[ADAMTSL4-AS2]] | +0.59 | +0.56 / +0.59 | both halves | 1e-05 |  |
| [[GNL1]] | +0.59 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[EXTL2]] | +0.58 | +0.51 / +0.53 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CNIH4]] | -0.55 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[VDAC3]] | -0.55 | -0.44 / -0.57 | both halves | 3e-05 |  |
| [[MTM1]] | -0.55 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[RAB18]] | -0.54 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[FBXO42]] | -0.53 | -0.44 / -0.52 | both halves | 3e-05 |  |
| [[ANKIB1]] | -0.53 | -0.47 / -0.44 | both halves | 3e-05 |  |
| [[ECI2]] | -0.52 | -0.47 / -0.51 | both halves | 2e-05 |  |
| [[ANO10]] | -0.52 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[ABCD4]] | -0.52 | -0.47 / -0.46 | both halves | 3e-05 |  |
| [[RAB6A]] | -0.51 | -0.42 / -0.47 | both halves | 4e-05 |  |
| [[SVIL-AS1-1]] | -0.51 | -0.60 / -0.41 | both halves | 4e-05 |  |
| [[SCAI]] | -0.51 | -0.44 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

None: no arrow points to this gene.

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KLF10]] | B | PLEKHG2 activity raises KLF10's level | lines that do not express PLEKHG2 (10) vs lines expressing it (40) | 1.29× lower at baseline in the lines without PLEKHG2 | 0.030 | ⚠ within organs, on part of the lines; also absent: ENSG00000225689; maybe low, not absent |
| cells under [[RMC-6236 (drug)]] 5 µM | B | PLEKHG2 activity raises the cells' numbers under RMC-6236 5 µM (protects the cells) | lines that do not express PLEKHG2 (10) vs lines expressing it (38) | the lines without PLEKHG2: 0.87× the cells of the other lines | 0.077 | ⚠ within organs, on part of the lines; also absent: ENSG00000225689; maybe low, not absent |
| [[MIEF2]] | B | PLEKHG2 activity raises MIEF2's level | lines that do not express PLEKHG2 (10) vs lines expressing it (40) | 1.05× lower at baseline in the lines without PLEKHG2 | 0.089 | ⚠ within organs, on part of the lines; also absent: ENSG00000225689; maybe low, not absent |
| [[EGR1]] | B | PLEKHG2 activity raises EGR1's level | lines that do not express PLEKHG2 (10) vs lines expressing it (40) | 1.85× lower at baseline in the lines without PLEKHG2 | 0.098 | ⚠ within organs, on part of the lines; also absent: ENSG00000225689; maybe low, not absent |

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.743). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (36.2, 0.4); signed map (5.4, 28.9). **Vector** length 100, 25.1% of its response variance represented; |z| ≥ 3 in 875 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *immediate early* (control, mean cos +0.58 to 9); *NGF-stimulated transcription* (reactome, mean cos +0.53 to 9); *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.56 to 13).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +8.2 | +12.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.8 | +3.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +6.4 | +8.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +6.0 | +7.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.8 | +5.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.2 | +4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.0 | +2.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +1.7 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | +2.1 | +2.9 |
| fall | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.7 | -5.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.5 | -7.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -4.1 | -7.0 |
|  | [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -3.7 | -2.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -3.7 | -5.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.4 | -7.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -3.4 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -3.4 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | pleckstrin homology and RhoGEF domain containing G2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:39,412,669-39,428,415 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CLG, FLJ00018, ARHGEF42 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 12 pathways, smallest: NRAGE signals death through JNK; G alpha (12/13) signalling events; Cell death signalling via NRAGE, NRIF and NADE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H7P9](https://www.uniprot.org/uniprotkb/Q9H7P9) (Pleckstrin homology domain-containing family G member 2):

> May be a transforming oncogene with exchange activity for CDC42 (By similarity). May be a guanine-nucleotide exchange factor (GEF) for RAC1 and CDC42. Activated by the binding to subunits beta and gamma of the heterotrimeric guanine nucleotide-binding protein (G protein). Involved in the regulation of actin polymerization.

**Summary**, from NCBI Gene [64857](https://www.ncbi.nlm.nih.gov/gene/64857):

> The protein encoded by this gene is a RhoGTPase that can activate CDC42 by promoting exchange of GDP for GTP on CDC42. The encoded protein is activated by binding to the beta and gamma subunits of heterotrimeric guanine nucleotide-binding protein. Defects in this gene have been associated with leukodystrophy and acquired microcephaly with or without dystonia. [provided by RefSeq, May 2017]

**Accessions** — [HGNC:29515](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:29515) · Entrez [64857](https://www.ncbi.nlm.nih.gov/gene/64857) · UniProt [Q9H7P9](https://www.uniprot.org/uniprotkb/Q9H7P9) · Ensembl [ENSG00000090924](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090924)

## Data

Gene col 1643: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1643); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1643, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1643]; `tensor/DDL_lfc|DDL_z.npy` [1643]; `embed/gene_vectors.npy` [1643]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1643 or target_col == 1643). Every well: [[PLEKHG2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEKHG2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
