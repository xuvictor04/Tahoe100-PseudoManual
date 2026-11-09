---
symbol: "ANG"
type: "gene"
col: 13191
ensembl_id: "ENSG00000214274"
name: "angiogenin"
location: "14q11.2"
module: 1
arm: "-"
pooled_cpm: 13.25
n_lines_expressing: 46
n_dd_up: 0
n_dd_down: 41
n_dd_up_clean: 0
n_dd_down_clean: 25
in_vector_space: true
direction_upstream: 2
direction_downstream: 18
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# ANG

*angiogenin* — 14q11.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (16 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.301× (z -19.6, q 0e+00, down in 41 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RNASE4]] (+0.88, fdr 7e-06, ⚠ same locus), [[ARL3]] (+0.73, fdr 7e-06), [[RAB40C]] (+0.73, fdr 7e-06), [[MOSPD3]] (+0.72, fdr 7e-06); moves opposite to [[UTP20]] (-0.75, fdr 7e-06), [[GNL3L]] (-0.75, fdr 7e-06), [[ANAPC7]] (-0.69, fdr 7e-06).
> It sits in the **-** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[FAM13A]] → it (grade B ⚠); 18 go from it, the strongest it → cells under [[AT7519 (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13191.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.55× | +3.1 | 0.63 | 6/41 (PANC-1, SW 900, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 41 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13191.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.301×** | -19.6 | 0e+00 | 41/44 (HS-578T, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.204×** | -18.3 | 0e+00 | 40/42 (HS-578T, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.200×** | -17.8 | 0e+00 | 42/44 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.297×** | -14.0 | 3e-42 | 39/44 (HS-578T, HOP62, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.303×** | -13.2 | 7e-38 | 33/39 (SW 900, SNU-423, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.341×** | -12.4 | 3e-33 | 40/44 (HS-578T, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.342×** | -12.3 | 5e-33 | 39/43 (MIA PaCa-2, PANC-1, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.354×** | -11.9 | 5e-31 | 37/44 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.389×** | -10.9 | 1e-25 | 34/41 (SNU-423, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.417×** | -10.0 | 6e-22 | 35/43 (SK-MEL-2, RPMI-7951, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.561×** | -9.4 | 3e-19 | 32/42 (CFPAC-1, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.454×** | -9.1 | 5e-18 | 34/44 (C32, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.458×** | -9.0 | 1e-17 | 33/43 (HOP62, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.466×** | -8.8 | 7e-17 | 33/43 (HepG2/C3A, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.584×** | -8.7 | 9e-17 | 29/44 (CFPAC-1, RPMI-7951, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.511×** | -7.3 | 9e-12 | 29/43 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~2% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.542×** | -7.0 | 6e-11 | 28/44 (C32, HepG2/C3A, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.548×** | -6.6 | 8e-10 | 29/42 (C32, NCI-H1792, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.588×** | -6.1 | 3e-08 | 27/44 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.372×** | -5.6 | 5e-07 | 23/41 (A549, MIA PaCa-2, …) | top dose only | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.436×** | -4.7 | 6e-05 | 20/38 (HepG2/C3A, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.91 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13191. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 23.3 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0615× (z -25.1) |
| [[C32 (line)]] | wt | 25.7 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0365× (z -19.3) |
| [[MIA PaCa-2 (line)]] | alt | 20.5 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.119× (z -12.0) |
| [[NCI-H460 (line)]] | wt | 15.7 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.122× (z -14.0) |
| [[A549 (line)]] | wt | 19.9 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0922× (z -21.1) |
| [[HOP62 (line)]] | alt | 16.1 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -15.0) |
| [[NCI-H1792 (line)]] | alt | 23.2 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.107× (z -13.9) |
| [[SNU-423 (line)]] | alt | 16.3 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0880× (z -18.0) |
| [[CFPAC-1 (line)]] | alt | 31.1 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -14.9) |
| [[LoVo (line)]] | wt | 14.7 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0993× (z -13.8) |
| [[A-172 (line)]] | wt | 14.7 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0161× (z -22.2) |
| [[HepG2_C3A (line)]] | wt | 35.8 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -16.2) |
| [[RPMI-7951 (line)]] | alt | 15.0 | 0 | 6 (3 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.153× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 16.0 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0717× (z -13.0) |
| [[NCI-H1573 (line)]] | alt | 18.9 | 0 | 5 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.203× (z -13.2) |
| [[SK-MEL-2 (line)]] | alt | 16.9 | 0 | 5 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0887× (z -12.3) |
| [[PANC-1 (line)]] | alt | 8.92 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.157× (z -11.6) |
| [[NCI-H2347 (line)]] | alt | 11.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -10.5) |
| [[Panc 03.27 (line)]] | alt | 13.5 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.113× (z -15.5) |
| [[H4 (line)]] | wt | 20.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.181× (z -9.8) |
| [[HCT15 (line)]] | alt | 18.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -13.4) |
| [[HT-29 (line)]] | alt | 10.3 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.114× (z -10.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.233× (z -9.9) |
| [[KATO III (line)]] | alt | 6.15 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -12.8) |
| [[LOX-IMVI (line)]] | wt | 8.70 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0489× (z -11.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.109× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 23.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.276× (z -9.3) |
| [[NCI-H23 (line)]] | alt | 12.4 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.0650× (z -13.2) |
| [[SW 900 (line)]] | alt | 13.8 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0483× (z -14.7) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.131× (z -10.3) |
| [[BT-474 (line)]] | alt | 5.26 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0590× (z -8.7) |
| [[COLO 205 (line)]] | alt | 11.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.122× (z -10.7) |
| [[Hs 766T (line)]] | wt | 11.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0922× (z -9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change |
| [[hTERT-HPNE (line)]] | wt | 12.8 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0812× (z -9.4) |
| [[J82 (line)]] | alt | 8.33 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.104× (z -9.7) ⚠ toxic |
| [[LS 180 (line)]] | wt | 6.41 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0490× (z -12.0) |
| [[A-427 (line)]] | wt | 10.9 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 8.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.17 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.63 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.26 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.52 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 7.10 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.98 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.50 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13191), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*70 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RNASE4]] | +0.88 | +0.91 / +0.84 | both halves | 7e-06 | STRING 988; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ARL3]] | +0.73 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[RAB40C]] | +0.73 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[MOSPD3]] | +0.72 | +0.69 / +0.75 | both halves | 7e-06 |  |
| [[MINDY2]] | +0.70 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[MXI1]] | +0.70 | +0.71 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[SNAPC3]] | +0.69 | +0.75 / +0.55 | both halves | 1e-05 |  |
| [[PJA2]] | +0.68 | +0.73 / +0.55 | both halves | 1e-05 |  |
| [[VKORC1]] | +0.68 | +0.67 / +0.63 | both halves | 7e-06 |  |
| [[APAF1]] | +0.68 | +0.71 / +0.62 | both halves | 7e-06 |  |
| [[SAP30-DT]] | +0.67 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[SUCO]] | +0.67 | +0.70 / +0.55 | both halves | 1e-05 |  |
| [[MGST3]] | +0.67 | +0.65 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*30 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UTP20]] | -0.75 | -0.73 / -0.69 | both halves | 7e-06 |  |
| [[GNL3L]] | -0.75 | -0.72 / -0.71 | both halves | 7e-06 |  |
| [[ANAPC7]] | -0.69 | -0.71 / -0.64 | both halves | 7e-06 |  |
| [[GPATCH4]] | -0.69 | -0.69 / -0.63 | both halves | 7e-06 |  |
| [[DNAJC11]] | -0.69 | -0.65 / -0.66 | both halves | 7e-06 |  |
| [[PRMT3]] | -0.67 | -0.68 / -0.59 | both halves | 7e-06 |  |
| [[SLC25A13]] | -0.67 | -0.66 / -0.62 | both halves | 7e-06 | pathway: HALLMARK_GLYCOLYSIS |
| [[ABCE1]] | -0.65 | -0.59 / -0.65 | both halves | 7e-06 |  |
| [[ME3]] | -0.64 | -0.58 / -0.55 | both halves | 1e-05 |  |
| [[CTPS1]] | -0.64 | -0.61 / -0.61 | both halves | 7e-06 |  |
| [[NIP7]] | -0.64 | -0.65 / -0.53 | both halves | 1e-05 |  |
| [[ENOX2]] | -0.64 | -0.68 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM13A]] | B | FAM13A activity raises ANG's level | lines that do not express FAM13A (6) vs lines expressing it (44) | 1.71× lower at baseline in the lines without FAM13A | 0.051 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |
| [[TOP2A]] | B | TOP2A activity raises ANG's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.3% of all compounds | 0.065 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

*18 arrows, 18 of them with an alert ⚠; grade A 0, B 0, C 18. Shown: the 12 strongest; 6 more arrows (6 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[AT7519 (drug)]] 5 µM | C | ANG, [[RNASE4]] activity raises the cells' numbers under AT7519 5 µM (protects the cells) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 0.44× the cells of the other lines | 0.004 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |
| cells under [[Idarubicin (hydrochloride) (drug)]] 0.05 µM | C | ANG, [[RNASE4]] activity raises the cells' numbers under Idarubicin (hydrochloride) 0.05 µM (protects the cells) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 0.68× the cells of the other lines | 0.005 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |
| cells under [[Infigratinib (drug)]] 5 µM | C | ANG, [[RNASE4]] activity raises the cells' numbers under Infigratinib 5 µM (protects the cells) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 0.60× the cells of the other lines | 0.012 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |
| cells under [[SBI-0640756 (drug)]] 5 µM | C | ANG, [[RNASE4]] activity lowers the cells' numbers under SBI-0640756 5 µM (makes them more sensitive) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 1.37× the cells of the other lines | 0.026 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |
| cells under [[Flumatinib (mesylate) (drug)]] 0.5 µM | C | ANG, [[RNASE4]] activity raises the cells' numbers under Flumatinib (mesylate) 0.5 µM (protects the cells) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 0.79× the cells of the other lines | 0.040 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |
| cells under [[Homoharringtonine (drug)]] 0.05 µM | C | ANG, [[RNASE4]] activity raises the cells' numbers under Homoharringtonine 0.05 µM (protects the cells) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 0.66× the cells of the other lines | 0.044 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |
| cells under [[PF-06260933 (drug)]] 5 µM | C | ANG, [[RNASE4]] activity lowers the cells' numbers under PF-06260933 5 µM (makes them more sensitive) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 1.46× the cells of the other lines | 0.045 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |
| cells under [[Bimiralisib (drug)]] 5 µM | C | ANG, [[RNASE4]] activity raises the cells' numbers under Bimiralisib 5 µM (protects the cells) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 0.53× the cells of the other lines | 0.053 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |
| [[NAA15]] | C | ANG activity lowers NAA15's level | lines that do not express ANG (4) vs lines expressing it (46) | 1.56× higher at baseline in the lines without ANG | 0.054 | ⚠ few lines (4 vs 46); across organs; co-absent genes; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent |
| cells under [[Naproxen (drug)]] 5 µM | C | ANG, [[RNASE4]] activity raises the cells' numbers under Naproxen 5 µM (protects the cells) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 0.79× the cells of the other lines | 0.055 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |
| cells under [[Tolcapone (drug)]] 5 µM | C | ANG, [[RNASE4]] activity raises the cells' numbers under Tolcapone 5 µM (protects the cells) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 0.81× the cells of the other lines | 0.058 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |
| cells under [[IQ 1 (drug)]] 5 µM | C | ANG, [[RNASE4]] activity raises the cells' numbers under IQ 1 5 µM (protects the cells) | lines that do not express ANG, RNASE4 (4) vs lines expressing them (44) | the lines without ANG, RNASE4: 0.76× the cells of the other lines | 0.068 | ⚠ few lines (4 vs 46); across organs; also absent: ALOXE3, LUCAT1, TBILA; maybe low, not absent; co-absent genes |

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **-** arm (projection on the module's main direction -0.606). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (4.1, -31.5); signed map (-33.0, 16.1). **Vector** length 88.4, 22.7% of its response variance represented; |z| ≥ 3 in 1,205 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Terfenadine (drug)]] 5 µM |  | +2.8 | +1.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | -1.4 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~63% of this change | +2.5 | -8.2 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | +2.3 | -2.9 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.2 | +2.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | +2.0 | +2.7 |
|  | [[Entrectinib (drug)]] 5 µM |  | +2.0 | +2.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.9 | +2.1 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -5.7 | -12.3 |
|  | [[Belumosudil (drug)]] 5 µM |  | -5.0 | -6.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.7 | -13.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.6 | -9.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -3.4 | -17.8 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.3 | -4.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -8.7 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.1 | -5.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.9 | -10.0 |

## What is on record

|  |  |
|---|---|
| Name | angiogenin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:20,684,177-20,698,971 (+) |
| Ensembl biotype | protein_coding |
| Also known as | RNASE5, RAA1, HEL168 |
| Gene groups (HGNC) | Ribonuclease A family |
| Hallmark sets | COAGULATION, COMPLEMENT, GLYCOLYSIS |
| Reactome | 6 pathways, smallest: tRNA-derived small RNA (tsRNA or tRNA-related fragment, tRF) biogenesis; Gene Silencing by RNA; Adherens junctions interactions |
| Matched by | ensembl_id |

**Function**, from UniProt [P03950](https://www.uniprot.org/uniprotkb/P03950) (Angiogenin):

> Secreted ribonuclease that can either promote or restrict cell proliferation of target cells, depending on the context. Endocytosed in target cells via its receptor PLXNB2 and translocates to the cytoplasm or nucleus. Under stress conditions, localizes to the cytoplasm and promotes the assembly of stress granules (SGs): specifically cleaves a subset of tRNAs within anticodon loops to produce tRNA-derived stress-induced fragments (tiRNAs), resulting in translation repression and inhibition of …

**Summary**, from NCBI Gene [283](https://www.ncbi.nlm.nih.gov/gene/283):

> The protein encoded by this gene is a member of the RNase A superfamily though it has relatively weak ribonucleolytic activity. This protein is a potent mediator of new blood vessel formation and thus, in addition to the name RNase5, is commonly called angiogenin. This protein induces angiogenesis after binding to actin on the surface of endothelial cells. This protein also accumulates at the nucleolus where it stimulates ribosomal transcription. Under stress conditions this protein …

**Accessions** — [HGNC:483](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:483) · Entrez [283](https://www.ncbi.nlm.nih.gov/gene/283) · UniProt [P03950](https://www.uniprot.org/uniprotkb/P03950) · Ensembl [ENSG00000214274](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000214274)

## Data

Gene col 13191: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13191); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13191, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13191]; `tensor/DDL_lfc|DDL_z.npy` [13191]; `embed/gene_vectors.npy` [13191]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13191 or target_col == 13191). Every well: [[ANG — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANG.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
