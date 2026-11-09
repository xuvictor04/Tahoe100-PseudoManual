---
symbol: "TMEM126B"
type: "gene"
col: 10071
ensembl_id: "ENSG00000171204"
name: "transmembrane protein 126B"
location: "11q14.1"
module: 122
arm: "+"
pooled_cpm: 17.96
n_lines_expressing: 50
n_dd_up: 17
n_dd_down: 0
n_dd_up_clean: 9
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/122"]
generated_by: "tahoemap"
---

# TMEM126B

*transmembrane protein 126B* — 11q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.98× (z +15.5, q 0e+00, up in 34 of 37 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 1.55× (z +6.2, q 4e-08, up in 29 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Simotinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.107×; ⚠ toxic); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.125×; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.348×; ⚠ cell-cycle shift, explains ~27% of this change); [[Sulfisoxazole (drug)]] 0.05 µM in 1 line (SNU-1 0.150×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPG21]] (+0.69, fdr 7e-06), [[GNPDA1]] (+0.67, fdr 7e-06), [[VPS13C]] (+0.65, fdr 9e-06); moves opposite to [[RABGEF1]] (-0.59, fdr 1e-05), [[MYO9B]] (-0.59, fdr 1e-05), [[ARID3B]] (-0.58, fdr 1e-05).
> It is in [[Module 122]], a single-armed module (Transferrin endocytosis and recycling).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZSCAN12]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10071.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.98×** | +15.5 | 0e+00 | 34/37 (PANC-1, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.81×** | +14.1 | 1e-42 | 27/31 (HEC-1-A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.99×** | +9.0 | 4e-17 | 24/33 (SW480, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **1.40×** | +6.7 | 2e-09 | 26/47 (A-172, J82, …) | all doses, stronger at high dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +6.5 | 8e-09 | 29/43 (NCI-H2030, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.55×** | +6.2 | 4e-08 | 29/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.50×** | +5.6 | 2e-06 | 25/46 (J82, NCI-H23, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.52×** | +5.4 | 5e-06 | 23/47 (A-427, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~40% of this change | **1.42×** | +4.9 | 5e-05 | 24/44 (PANC-1, NCI-H2347, …) | inconsistent across doses | low cells (technical?) |
| [[Belumosudil (drug)]] 5 µM |  | **1.43×** | +4.9 | 5e-05 | 19/47 (RPMI-7951, PANC-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~25% of this change | **1.43×** | +4.9 | 5e-05 | 22/43 (NCI-H23, NCI-H1573, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.37×** | +4.5 | 4e-04 | 20/47 (LOX-IMVI, A-427, …) | all doses, stronger at high dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.60×** | +4.2 | 0.001 | 17/44 (SK-MEL-2, NCI-H23, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.36×** | +4.0 | 0.002 | 17/46 (A-172, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **1.30×** | +3.7 | 0.008 | 16/47 (LOX-IMVI, HEC-1-A, …) | top dose only |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.52×** | +3.1 | 0.062 | 11/46 (RKO, C32, …) | top dose only | noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.26×** | +3.1 | 0.062 | 14/48 (HEC-1-A, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~8% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10071.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Simotinib (drug)]] 5 µM in 1 line (HepG2/C3A 0.107×; ⚠ toxic); [[Imiquimod (hydrochloride) (drug)]] 5 µM in 1 line (HepG2/C3A 0.125×; ⚠ toxic); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (RKO 0.348×; ⚠ cell-cycle shift, explains ~27% of this change); [[Sulfisoxazole (drug)]] 0.05 µM in 1 line (SNU-1 0.150×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.905× | -4.5 | 0.003 | 2/48 (Hs 766T, HS-578T) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.01 per unit of S-phase module lfc, +0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10071. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 14.7 | 0 | 2 (2 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.107× (z -10.2) ⚠ toxic |
| [[NCI-H1573 (line)]] | alt | 8.51 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.54× (z +9.2) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 12.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.85× (z +10.1) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 31.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +10.8) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 27.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.05 µM 2.50× (z +8.8) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 13.6 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +10.7) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[A498 (line)]] | wt | 11.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.44× (z +9.9) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 15.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 6.75× (z +12.2) ⚠ toxic; transcription drop | — |
| [[HOP62 (line)]] | alt | 7.60 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.82× (z +9.2) ⚠ toxic; transcription drop | — |
| [[J82 (line)]] | alt | 22.1 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.94× (z +10.3) ⚠ cell-cycle shift, explains ~62% of this change | — |
| [[NCI-H1792 (line)]] | alt | 12.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.05× (z +9.2) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 24.1 | 0 | 1 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -9.8) ⚠ cell-cycle shift, explains ~27% of this change |
| [[SNU-1 (line)]] | wt | 16.9 | 0 | 1 | — | [[Sulfisoxazole (drug)]] 0.05 µM 0.150× (z -8.7) |
| [[A-427 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.84 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.1 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 24.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 14.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.74 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 12.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10071), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*76 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPG21]] | +0.69 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[GNPDA1]] | +0.67 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[VPS13C]] | +0.65 | +0.67 / +0.57 | both halves | 9e-06 |  |
| [[HINT3]] | +0.61 | +0.45 / +0.63 | both halves | 3e-05 |  |
| [[ZNF260]] | +0.61 | +0.63 / +0.58 | both halves | 7e-06 |  |
| [[STX17]] | +0.61 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[COMMD8]] | +0.61 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[TAF9]] | +0.60 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[CHIC1]] | +0.60 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[ATP6V1C1]] | +0.59 | +0.57 / +0.55 | both halves | 1e-05 |  |
| [[PAIP1]] | +0.58 | +0.48 / +0.60 | both halves | 2e-05 |  |
| [[LDAH]] | +0.58 | +0.56 / +0.55 | both halves | 1e-05 |  |

## Genes that move opposite

*24 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RABGEF1]] | -0.59 | -0.60 / -0.57 | both halves | 1e-05 |  |
| [[MYO9B]] | -0.59 | -0.64 / -0.54 | both halves | 1e-05 |  |
| [[ARID3B]] | -0.58 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[TMEM184B]] | -0.57 | -0.58 / -0.57 | both halves | 1e-05 |  |
| [[SRGAP2D]] | -0.56 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[DRD4]] | -0.55 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[SH3GL1]] | -0.55 | -0.62 / -0.49 | both halves | 1e-05 |  |
| [[CSNK1E]] | -0.55 | -0.55 / -0.49 | both halves | 2e-05 |  |
| [[CHST7]] | -0.54 | -0.46 / -0.58 | both halves | 2e-05 |  |
| [[FLNB-AS1]] | -0.54 | -0.52 / -0.45 | both halves | 3e-05 |  |
| [[MAP2K1]] | -0.52 | -0.62 / -0.39 | both halves | 6e-05 |  |
| [[SENP5]] | -0.52 | -0.57 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZSCAN12]] | B | ZSCAN12 activity raises TMEM126B's level | lines that do not express ZSCAN12 (14) vs lines expressing it (36) | 1.23× lower at baseline in the lines without ZSCAN12 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with SETD1B; also absent: SLC35G2, ZNF469, PGF; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 122]] — Transferrin endocytosis and recycling; 40 genes; every member is in the + arm (projection on the module's main direction 0.568). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-17.8, 13.2); signed map (11.8, -26.2). **Vector** length 70.7, 13.6% of its response variance represented; |z| ≥ 3 in 692 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +15.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +3.7 | +5.4 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.5 | +6.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.5 | +14.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | +3.3 | +5.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.2 | +4.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +4.5 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.1 | +0.6 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +2.0 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.8 | +1.5 |
| fall | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -0.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.2 | -0.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.1 | +0.3 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -2.0 | -0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.5 | -1.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.5 | +0.0 |

## What is on record

|  |  |
|---|---|
| Name | transmembrane protein 126B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q14.1 — chr11:85,628,573-85,636,539 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HT007 |
| Gene groups (HGNC) | Mitochondrial complex I assembly complex |
| Reactome | 3 pathways, smallest: Complex I biogenesis; Respiratory electron transport; Aerobic respiration and respiratory electron transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IUX1](https://www.uniprot.org/uniprotkb/Q8IUX1) (Complex I assembly factor TMEM126B, mitochondrial):

> As part of the MCIA complex, involved in the assembly of the mitochondrial complex I. Participates in constructing the membrane arm of complex I.

**Summary**, from NCBI Gene [55863](https://www.ncbi.nlm.nih.gov/gene/55863):

> This gene encodes a mitochondrial transmembrane protein which is a component of the mitochondrial complex I assembly complex. The encoded protein serves as an assembly factor that is required for formation of the membrane arm of the complex. It interacts with NADH dehydrogenase [ubiquinone] 1 alpha subcomplex assembly factor 13. Naturally occurring mutations in this gene are associated with isolated complex I deficiency. A pseudogene of this gene has been defined on chromosome 9. [provided by …

**Accessions** — [HGNC:30883](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30883) · Entrez [55863](https://www.ncbi.nlm.nih.gov/gene/55863) · UniProt [Q8IUX1](https://www.uniprot.org/uniprotkb/Q8IUX1) · Ensembl [ENSG00000171204](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000171204)

## Data

Gene col 10071: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10071); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10071, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10071]; `tensor/DDL_lfc|DDL_z.npy` [10071]; `embed/gene_vectors.npy` [10071]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10071 or target_col == 10071). Every well: [[TMEM126B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TMEM126B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
