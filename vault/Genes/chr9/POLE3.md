---
symbol: "POLE3"
type: "gene"
col: 7255
ensembl_id: "ENSG00000148229"
name: "DNA polymerase epsilon 3, accessory subunit"
location: "9q32"
module: 71
arm: "+"
pooled_cpm: 43.45
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 2
n_dd_up_clean: 3
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 1
tags: ["gene", "module/071"]
generated_by: "tahoemap"
---

# POLE3

*DNA polymerase epsilon 3, accessory subunit* — 9q32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (11 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.27× (z +12.5, q 3e-33, up in 47 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (1 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.752× (z -4.4, q 0.004, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TOP3A]] (+0.75, fdr 7e-06), [[TOPBP1]] (+0.69, fdr 8e-06), [[ACAD9]] (+0.63, fdr 1e-05); moves opposite to [[ATP6V0A1]] (-0.57, fdr 1e-05), [[HDHD3]] (-0.53, fdr 2e-05, ⚠ same locus), [[UBE2E2]] (-0.51, fdr 1e-04), [[ZMIZ2]] (-0.50, fdr 3e-05).
> It is in [[Module 071]], a single-armed module (Metabolism of non-coding RNA).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 1 goes from it, the strongest it → [[ERCC5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 11 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7255.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.27×** | +12.5 | 3e-33 | 47/48 (A549, KATO III, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | **2.98×** | +11.8 | 7e-30 | 46/47 (KATO III, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | **2.59×** | +9.9 | 7e-21 | 35/38 (MIA PaCa-2, Panc 03.27, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~37% of this change | **2.58×** | +9.5 | 3e-19 | 40/43 (KATO III, A-172, …) | all doses, flat | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.40×** | +9.1 | 8e-18 | 45/47 (MIA PaCa-2, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.69×** | +5.7 | 1e-06 | 36/48 (SW480, LOX-IMVI, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~49% of this change | **1.64×** | +5.2 | 2e-05 | 31/47 (C32, LoVo, …) | top dose only |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~46% of this change | **1.60×** | +5.1 | 2e-05 | 37/46 (BT-474, HCT15, …) | inconsistent across doses | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **1.63×** | +5.1 | 2e-05 | 32/48 (MIA PaCa-2, C32, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.34×** | +4.5 | 4e-04 | 32/48 (NCI-H2347, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~84% of this change | **1.50×** | +4.4 | 6e-04 | 28/48 (LOX-IMVI, A-172, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | **1.41×** | +3.7 | 0.009 | 25/48 (A-172, SK-MEL-2, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.42×** | +3.7 | 0.010 | 26/47 (SNU-423, MIA PaCa-2, …) | top dose only |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.25×** | +3.5 | 0.021 | 20/48 (HT-29, NCI-H23, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7255.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.752×** | -4.4 | 0.004 | 29/48 (A498, KATO III, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.671×** | -4.3 | 0.004 | 29/48 (KATO III, C32, …) | rises with dose |  |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.740× | -3.3 | 0.21 | 22/47 (hTERT-HPNE, LS 180, …) | two highest doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, +0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7255. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 53.9 | 4 (3 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +12.1) | — |
| [[MIA PaCa-2 (line)]] | alt | 44.7 | 4 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.52× (z +9.0) | — |
| [[A-172 (line)]] | wt | 32.9 | 3 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +10.4) | — |
| [[HEC-1-A (line)]] | alt | 62.0 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.98× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.12× (z +8.6) | — |
| [[SNU-423 (line)]] | alt | 45.3 | 3 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.82× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +9.9) | — |
| [[HOP62 (line)]] | alt | 36.9 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.58× (z +9.5) | — |
| [[HT-29 (line)]] | alt | 35.6 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.25× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.54× (z +8.8) | — |
| [[Panc 03.27 (line)]] | alt | 45.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.23× (z +10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[PANC-1 (line)]] | alt | 36.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.75× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[A549 (line)]] | wt | 34.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.66× (z +14.7) | — |
| [[C32 (line)]] | wt | 35.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.98× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 23.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.73× (z +9.4) | — |
| [[Hs 766T (line)]] | wt | 57.1 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.53× (z +8.9) | — |
| [[NCI-H1792 (line)]] | alt | 26.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.55× (z +12.0) | — |
| [[NCI-H2030 (line)]] | alt | 29.3 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.90× (z +10.0) | — |
| [[NCI-H2347 (line)]] | alt | 34.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.86× (z +11.4) | — |
| [[RKO (line)]] | wt | 58.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.41× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[RPMI-7951 (line)]] | alt | 38.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.85× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[SW1417 (line)]] | alt | 44.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.19× (z +9.1) | — |
| [[SW480 (line)]] | alt | 50.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.66× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | — |
| [[A-427 (line)]] | wt | 25.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 113 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 43.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 39.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 47.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 51.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 21.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 35.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 28.6 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 125 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 25.1 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 30.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 36.9 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 39.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 32.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 52.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 42.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 39.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 57.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 39.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7255), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOP3A]] | +0.75 | +0.58 / +0.77 | both halves | 7e-06 | pathway: DNA Double-Strand Break Repair; STRING 401 |
| [[TOPBP1]] | +0.69 | +0.58 / +0.68 | both halves | 8e-06 | pathway: DNA Double-Strand Break Repair; STRING 580 |
| [[ACAD9]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[CENPJ]] | +0.63 | +0.50 / +0.77 | both halves | 1e-05 |  |
| [[HSPA14]] | +0.61 | +0.47 / +0.61 | both halves | 2e-05 |  |
| [[FOXRED1]] | +0.61 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[DSN1]] | +0.61 | +0.51 / +0.73 | both halves | 1e-05 |  |
| [[RECQL5]] | +0.58 | +0.47 / +0.58 | both halves | 2e-05 |  |
| [[TSN]] | +0.58 | +0.57 / +0.44 | both halves | 3e-05 |  |
| [[DYRK4]] | +0.58 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[GLE1]] | +0.57 | +0.41 / +0.59 | both halves | 4e-05 |  |
| [[MTBP]] | +0.57 | +0.42 / +0.66 | both halves | 4e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP6V0A1]] | -0.57 | -0.57 / -0.52 | both halves | 1e-05 |  |
| [[HDHD3]] | -0.53 | -0.47 / -0.51 | both halves | 2e-05 | ⚠ same locus (30.2 kb, same strand: neighbours can correlate without regulation) |
| [[UBE2E2]] | -0.51 | -0.35 / -0.50 | both halves | 1e-04 |  |
| [[ZMIZ2]] | -0.50 | -0.46 / -0.45 | both halves | 3e-05 |  |
| [[NDRG4]] | -0.50 | -0.35 / -0.48 | both halves | 1e-04 |  |
| [[SYP]] | -0.49 | -0.29 / -0.48 | both halves | 2e-04 |  |
| [[SUSD4]] | -0.48 | -0.40 / -0.43 | both halves | 5e-05 |  |
| [[PPP2R2A]] | -0.48 | -0.33 / -0.52 | both halves | 1e-04 | pathway: Mitotic G1 phase and G1/S transition |
| [[TMEM135]] | -0.47 | -0.27 / -0.51 | both halves | 3e-04 |  |
| [[TPPP]] | -0.47 | -0.26 / -0.49 | both halves | 4e-04 |  |
| [[CEBPZOS]] | -0.47 | -0.40 / -0.51 | both halves | 5e-05 |  |
| [[PICALM]] | -0.46 | -0.39 / -0.46 | both halves | 6e-05 |  |
| [[USP9X]] | -0.46 | -0.27 / -0.51 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers POLE3's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.1% of all compounds | 0.013 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[AP1M2]] | B | AP1M2 activity lowers POLE3's level | lines that do not express AP1M2 (24) vs lines expressing it (26) | 1.17× higher at baseline in the lines without AP1M2 | 0.027 | ⚠ within organs, on part of the lines; also absent: CRB3, SPINT1-AS1, GRB7 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ERCC5]] | C | POLE3's natural level strengthens ERCC5's drug response | POLE3's natural level across 50 lines (lineage-adjusted; a glimpse) | r +0.63, reverse +0.01; direction clear | 0.050 | ⚠ tissue can mimic it; precision caveat |

## Where it sits

- **Module**: [[Module 071]] — Metabolism of non-coding RNA; 70 genes; every member is in the + arm (projection on the module's main direction 0.611). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-39.3, -40.8); signed map (-40.6, -39.8). **Vector** length 68.5, 18.0% of its response variance represented; |z| ≥ 3 in 736 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +3.6 | +12.5 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | +2.4 | +3.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | +2.2 | +5.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | +1.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.6 | +4.5 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.5 | -1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | -0.0 |
|  | [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | +1.2 | -0.1 |
|  | [[Methotrexate (drug)]] 5 µM |  | +1.1 | +0.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.5 | -4.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | -5.2 | -4.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~50% of this change | -3.1 | +9.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~49% of this change | -2.9 | +11.8 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -2.6 | -0.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | +1.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -1.6 | +1.4 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.5 | -3.3 |
|  | [[Rapamycin (drug)]] 5 µM |  | -1.5 | -1.9 |

## What is on record

|  |  |
|---|---|
| Name | DNA polymerase epsilon 3, accessory subunit |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q32 — chr9:113,407,235-113,410,675 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CHRAC17, Ybl1, p17, CHARAC17, CHRAC2 |
| Gene groups (HGNC) | DNA polymerases; ATAC complex; Chromatin accessibility complex |
| Hallmark sets | UV_RESPONSE_UP, MYC_TARGETS_V1 |
| Reactome | 30 pathways, smallest: DNA replication initiation; PCNA-Dependent Long Patch Base Excision Repair; Gap-filling DNA repair synthesis and ligation in GG-NER |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NRF9](https://www.uniprot.org/uniprotkb/Q9NRF9) (DNA polymerase epsilon subunit 3):

> Accessory component of the DNA polymerase epsilon complex. Participates in DNA repair and in chromosomal DNA replication (By similarity). Forms a complex with CHRAC1 and binds naked DNA, which is then incorporated into chromatin, aided by the nucleosome-remodeling activity of ISWI/SNF2H and ACF1. Does not enhance nucleosome sliding activity of the ACF-5 ISWI chromatin remodeling complex.

**Summary**, from NCBI Gene [54107](https://www.ncbi.nlm.nih.gov/gene/54107):

> POLE3 is a histone-fold protein that interacts with other histone-fold proteins to bind DNA in a sequence-independent manner. These histone-fold protein dimers combine within larger enzymatic complexes for DNA transcription, replication, and packaging.[supplied by OMIM, Apr 2004]

**Accessions** — [HGNC:13546](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:13546) · Entrez [54107](https://www.ncbi.nlm.nih.gov/gene/54107) · UniProt [Q9NRF9](https://www.uniprot.org/uniprotkb/Q9NRF9) · Ensembl [ENSG00000148229](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148229)

## Data

Gene col 7255: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7255); `tables/drug_effects.parquet` (17 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7255, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7255]; `tensor/DDL_lfc|DDL_z.npy` [7255]; `embed/gene_vectors.npy` [7255]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7255 or target_col == 7255). Every well: [[POLE3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/POLE3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
