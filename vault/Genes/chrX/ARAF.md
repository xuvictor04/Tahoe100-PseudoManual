---
symbol: "ARAF"
type: "gene"
col: 1205
ensembl_id: "ENSG00000078061"
name: "A-Raf proto-oncogene, serine/threonine kinase"
location: "Xp11.3"
module: 153
arm: "+"
pooled_cpm: 13.81
n_lines_expressing: 50
n_dd_up: 5
n_dd_down: 13
n_dd_up_clean: 2
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/153"]
generated_by: "tahoemap"
---

# ARAF

*A-Raf proto-oncogene, serine/threonine kinase* — Xp11.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (3 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.19× (z +10.3, q 6e-22, up in 23 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.27× (z +4.0, q 0.008, up in 11 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.373× (z -24.2, q 0e+00, down in 46 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PIGO]] (+0.81, fdr 7e-06), [[BCL7B]] (+0.68, fdr 1e-05), [[RAB1B]] (+0.68, fdr 1e-05); moves opposite to [[TPTEP2-CSNK1E]] (-0.59, fdr 4e-05), [[ANKRD16]] (-0.57, fdr 2e-05), [[DGKE]] (-0.56, fdr 4e-05).
> It is in [[Module 153]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1205.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.19× | +10.3 | 6e-22 | 23/48 (MIA PaCa-2, PANC-1, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.65×** | +8.3 | 2e-14 | 19/28 (SW 900, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.53×** | +7.3 | 5e-11 | 26/36 (NCI-H1792, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.43×** | +5.7 | 1e-06 | 15/31 (A498, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +4.0 | 0.008 | 11/45 (HOP62, NCI-H1792, …) | top dose only |  |
| [[GSK1059615 (drug)]] 0.5 µM |  | **1.31×** | +3.4 | 0.075 | 6/44 (MIA PaCa-2, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | 1.30× | +3.2 | 0.10 | 10/38 (KATO III, HS-578T, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1205.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.373×** | -24.2 | 0e+00 | 46/47 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.505×** | -11.9 | 3e-30 | 37/48 (A-172, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.522×** | -11.3 | 2e-27 | 38/47 (SW1417, SK-MEL-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.557×** | -9.8 | 2e-20 | 32/44 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.611×** | -8.6 | 9e-16 | 29/45 (SNU-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.614×** | -8.5 | 2e-15 | 35/48 (SW480, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.634×** | -8.0 | 1e-13 | 31/48 (SW1417, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.705×** | -6.1 | 7e-08 | 24/47 (SW1417, SW480, …) | rises with dose | cell-cycle shift (explains ~15% here); position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **0.725×** | -5.4 | 4e-06 | 21/46 (SW480, COLO 205, …) | rises with dose | position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **0.558×** | -5.3 | 6e-06 | 19/48 (RPMI-7951, A498, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.741×** | -5.2 | 8e-06 | 18/46 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.836× | -4.5 | 4e-04 | 19/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~12% of this change | **0.803×** | -3.9 | 0.005 | 16/45 (KATO III, H4, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.807×** | -3.8 | 0.007 | 7/47 (PANC-1, A498, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 0.5 µM |  | 0.834× | -3.2 | 0.054 | 5/47 (BT-474, SW480, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1205. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 24.7 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -15.1) |
| [[HOP62 (line)]] | alt | 9.02 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.164× (z -10.8) |
| [[NCI-H460 (line)]] | wt | 17.9 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.274× (z -15.9) |
| [[AsPC-1 (line)]] | alt | 9.19 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.184× (z -12.0) |
| [[BT-474 (line)]] | alt | 16.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.307× (z -9.4) |
| [[C-33 A (line)]] | alt | 19.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.176× (z -9.3) |
| [[C32 (line)]] | wt | 9.61 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.202× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 16.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.298× (z -12.4) |
| [[COLO 205 (line)]] | alt | 19.0 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.283× (z -9.5) |
| [[HCT15 (line)]] | alt | 14.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -10.2) |
| [[HEC-1-A (line)]] | alt | 11.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 11.8 | 0 | 1 | — | [[Verteporfin (drug)]] 5 µM 0.114× (z -8.9) |
| [[HS-578T (line)]] | alt | 9.75 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.172× (z -9.3) |
| [[HT-29 (line)]] | alt | 15.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.340× (z -9.6) |
| [[J82 (line)]] | alt | 15.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -9.0) |
| [[KATO III (line)]] | alt | 20.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.317× (z -12.6) |
| [[LS 180 (line)]] | wt | 13.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.220× (z -13.5) |
| [[NCI-H1573 (line)]] | alt | 10.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -9.1) |
| [[NCI-H1792 (line)]] | alt | 13.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.345× (z -9.2) |
| [[NCI-H2347 (line)]] | alt | 17.1 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.464× (z -8.8) |
| [[Panc 03.27 (line)]] | alt | 21.3 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.313× (z -10.7) |
| [[PANC-1 (line)]] | alt | 13.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.331× (z -12.9) |
| [[RKO (line)]] | wt | 11.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.214× (z -10.8) |
| [[RPMI-7951 (line)]] | alt | 17.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -9.7) |
| [[SW 900 (line)]] | alt | 12.9 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.158× (z -14.2) |
| [[SW1417 (line)]] | alt | 16.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.290× (z -9.1) |
| [[A-172 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 14.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.85 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.24 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.64 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.99 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1205), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*79 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PIGO]] | +0.81 | +0.63 / +0.83 | both halves | 7e-06 |  |
| [[BCL7B]] | +0.68 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[RAB1B]] | +0.68 | +0.54 / +0.75 | both halves | 1e-05 |  |
| [[SF3A1]] | +0.65 | +0.55 / +0.63 | both halves | 1e-05 |  |
| [[RAB11B]] | +0.64 | +0.56 / +0.62 | both halves | 1e-05 |  |
| [[DMAP1]] | +0.64 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[USP19]] | +0.63 | +0.47 / +0.67 | both halves | 2e-05 |  |
| [[PABIR1]] | +0.63 | +0.44 / +0.63 | both halves | 3e-05 |  |
| [[SMARCD1]] | +0.63 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[OCRL]] | +0.62 | +0.39 / +0.64 | both halves | 5e-05 |  |
| [[SMARCB1]] | +0.61 | +0.46 / +0.69 | both halves | 3e-05 |  |
| [[DLD]] | +0.60 | +0.48 / +0.62 | both halves | 2e-05 | pathway: HALLMARK_ADIPOGENESIS |

## Genes that move opposite

*21 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TPTEP2-CSNK1E]] | -0.59 | -0.41 / -0.59 | both halves | 4e-05 |  |
| [[ANKRD16]] | -0.57 | -0.48 / -0.57 | both halves | 2e-05 |  |
| [[DGKE]] | -0.56 | -0.42 / -0.58 | both halves | 4e-05 |  |
| [[CDC20-DT]] | -0.55 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[TMEM38A]] | -0.54 | -0.43 / -0.62 | both halves | 3e-05 |  |
| [[SEPTIN1]] | -0.54 | -0.32 / -0.60 | both halves | 2e-04 |  |
| [[GNRH1]] | -0.54 | -0.34 / -0.62 | both halves | 1e-04 |  |
| [[ING2-DT]] | -0.54 | -0.39 / -0.61 | both halves | 5e-05 |  |
| [[SNX14]] | -0.54 | -0.30 / -0.56 | both halves | 2e-04 |  |
| [[BCL7A]] | -0.54 | -0.38 / -0.54 | both halves | 7e-05 |  |
| [[FAM89A]] | -0.54 | -0.36 / -0.60 | both halves | 9e-05 |  |
| [[DDN-AS1]] | -0.54 | -0.25 / -0.59 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises ARAF's level | compounds that target TOP2A: 3 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.5% of all compounds | 0.065 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[GRIPAP1]] | C | GRIPAP1's natural level strengthens ARAF's drug response | GRIPAP1's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.11; direction not clear | 0.077 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 153]]; 29 genes; every member is in the + arm (projection on the module's main direction 0.652). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-20.3, -23.7); signed map (-14.5, -34.5). **Vector** length 65.7, 10.1% of its response variance represented; |z| ≥ 3 in 955 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +7.3 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.8 | -1.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.4 | +5.7 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | -0.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.8 | +4.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +1.5 | +0.5 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.5 | +3.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.4 | +2.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.0 | -24.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.9 | -9.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~24% of this change | -2.9 | -5.4 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.8 | -8.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.1 | -5.2 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.0 | -2.6 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -2.4 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.5 | -2.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -1.4 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | A-Raf proto-oncogene, serine/threonine kinase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | Xp11.3 — chrX:47,561,205-47,571,908 (+) |
| Ensembl biotype | protein_coding |
| Also known as | A-Raf; previously ARAF1 |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinase kinases; RAF family |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 18 pathways, smallest: Gain-of-function MRAS complexes activate RAF signaling; SHOC2 M1731 mutant abolishes MRAS complex function; Signaling by MRAS-complex mutants |
| Matched by | ensembl_id |

**Function**, from UniProt [P10398](https://www.uniprot.org/uniprotkb/P10398) (Serine/threonine-protein kinase A-Raf):

> Involved in the transduction of mitogenic signals from the cell membrane to the nucleus. May also regulate the TOR signaling cascade. Phosphorylates PFKFB2.; [Isoform 2]: Serves as a positive regulator of myogenic differentiation by inducing cell cycle arrest, the expression of myogenin and other muscle-specific proteins, and myotube formation.

**Summary**, from NCBI Gene [369](https://www.ncbi.nlm.nih.gov/gene/369):

> Enables protein serine/threonine kinase activity. Involved in negative regulation of apoptotic process; regulation of TOR signaling; and regulation of protein metabolic process. Located in plasma membrane. Biomarker of high grade glioma. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:646](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:646) · Entrez [369](https://www.ncbi.nlm.nih.gov/gene/369) · UniProt [P10398](https://www.uniprot.org/uniprotkb/P10398) · Ensembl [ENSG00000078061](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000078061)

## Data

Gene col 1205: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1205); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1205, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1205]; `tensor/DDL_lfc|DDL_z.npy` [1205]; `embed/gene_vectors.npy` [1205]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1205 or target_col == 1205). Every well: [[ARAF — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARAF.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
