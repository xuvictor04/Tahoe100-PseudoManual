---
symbol: "LTBP4"
type: "gene"
col: 1606
ensembl_id: "ENSG00000090006"
name: "latent transforming growth factor beta binding protein 4"
location: "19q13.2"
module: 208
arm: "+"
pooled_cpm: 40.47
n_lines_expressing: 44
n_dd_up: 5
n_dd_down: 30
n_dd_up_clean: 4
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/208"]
generated_by: "tahoemap"
---

# LTBP4

*latent transforming growth factor beta binding protein 4* — 19q13.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (1 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.14× (z +7.1, q 5e-10, up in 4 of 42 measured lines) ⚠ position not correctable. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.23× (z +4.9, q 2e-04, up in 16 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.378× (z -22.6, q 0e+00, down in 37 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EHBP1L1]] (+0.69, fdr 1e-05), [[ARID3B]] (+0.66, fdr 1e-05), [[TNFRSF25]] (+0.66, fdr 7e-06); moves opposite to [[ZFX]] (-0.61, fdr 1e-05), [[SETD2]] (-0.60, fdr 2e-05), [[THOC7]] (-0.60, fdr 2e-05).
> It is in [[Module 208]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[PMP22]] → it (grade B ⚠); 1 goes from it, the strongest it → [[NIPBL]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 2 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1606.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +7.1 | 5e-10 | 4/42 (NCI-H23, AN3 CA, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.23×** | +4.9 | 2e-04 | 16/42 (HEC-1-A, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.34×** | +4.8 | 2e-04 | 25/42 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.28×** | +4.0 | 0.008 | 19/41 (NCI-H2030, LOX-IMVI, …) | two highest doses | low cells (technical?) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.24×** | +3.4 | 0.085 | 15/41 (LOX-IMVI, NCI-H2030, …) | two highest doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.089 | 12/40 (COLO 205, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 37 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1606.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.378×** | -22.6 | 0e+00 | 37/42 (A549, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.343×** | -16.9 | 0e+00 | 37/42 (A549, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.363×** | -16.7 | 0e+00 | 35/41 (A549, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.522×** | -10.7 | 2e-24 | 34/42 (A549, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.561×** | -9.5 | 2e-19 | 28/42 (HS-578T, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.713×** | -7.9 | 4e-13 | 22/42 (A549, LoVo, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.635×** | -7.5 | 6e-12 | 27/41 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.646×** | -7.2 | 5e-11 | 23/41 (HS-578T, SW480, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.652×** | -7.0 | 1e-10 | 25/42 (LOX-IMVI, HOP62, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.658×** | -6.6 | 2e-09 | 28/41 (SNU-423, A549, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.658×** | -6.6 | 2e-09 | 22/39 (HOP62, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.682×** | -6.3 | 2e-08 | 27/42 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.774×** | -6.0 | 1e-07 | 23/42 (A549, NCI-H1573, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.696×** | -5.7 | 4e-07 | 20/42 (CFPAC-1, A549, …) | top dose only | cell-cycle shift (explains ~15% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.793×** | -5.4 | 3e-06 | 20/42 (A549, CFPAC-1, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.743×** | -4.7 | 1e-04 | 18/42 (A549, NCI-H1792, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.605×** | -4.3 | 5e-04 | 12/42 (PANC-1, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.765×** | -4.2 | 9e-04 | 19/41 (A-172, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.798×** | -3.7 | 0.005 | 11/41 (CFPAC-1, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.817×** | -3.3 | 0.022 | 14/42 (LoVo, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.25 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1606. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A549 (line)]] | wt | 216 | 0 | 21 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0906× (z -28.0) |
| [[HOP62 (line)]] | alt | 89.2 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -19.1) |
| [[LOX-IMVI (line)]] | wt | 81.4 | 0 | 7 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -16.0) |
| [[SW480 (line)]] | alt | 35.9 | 0 | 6 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.236× (z -14.8) |
| [[HS-578T (line)]] | alt | 35.3 | 0 | 5 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.204× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.337× (z -11.8) |
| [[LoVo (line)]] | wt | 31.8 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -20.0) |
| [[NCI-H460 (line)]] | wt | 25.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.211× (z -13.5) |
| [[A-172 (line)]] | wt | 41.1 | 0 | 3 | — | [[Harringtonine (drug)]] 0.5 µM 0.247× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 32.3 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.283× (z -12.0) |
| [[LS 180 (line)]] | wt | 26.8 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -17.5) |
| [[NCI-H1792 (line)]] | alt | 57.9 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -13.4) |
| [[PANC-1 (line)]] | alt | 42.7 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.337× (z -16.2) |
| [[A498 (line)]] | wt | 90.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -10.6) |
| [[MIA PaCa-2 (line)]] | alt | 17.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.137× (z -12.2) |
| [[NCI-H2347 (line)]] | alt | 18.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -11.0) |
| [[RPMI-7951 (line)]] | alt | 41.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -11.3) |
| [[SW 900 (line)]] | alt | 51.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.351× (z -12.7) |
| [[AN3 CA (line)]] | alt | 43.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.123× (z -9.0) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[AsPC-1 (line)]] | alt | 29.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.384× (z -8.9) |
| [[COLO 205 (line)]] | alt | 11.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.105× (z -8.6) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[H4 (line)]] | wt | 29.1 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.147× (z -8.9) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[HEC-1-A (line)]] | alt | 10.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.61× (z +10.1) | — |
| [[Hs 766T (line)]] | wt | 61.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.310× (z -12.7) |
| [[HT-29 (line)]] | alt | 25.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.130× (z -12.2) |
| [[NCI-H1573 (line)]] | alt | 20.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.275× (z -13.3) |
| [[NCI-H2030 (line)]] | alt | 50.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.359× (z -13.9) |
| [[NCI-H23 (line)]] | alt | 60.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.433× (z -10.8) |
| [[SK-MEL-2 (line)]] | alt | 34.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.370× (z -9.4) |
| [[SNU-423 (line)]] | alt | 13.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0966× (z -12.1) ⚠ toxic; cell-cycle shift, explains ~26% of this change |
| [[SW48 (line)]] | wt | 19.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.146× (z -8.7) |
| [[A-427 (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.42 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 109 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.44 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 15.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.15 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 33.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.06 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 34.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 80.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 8.60 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 14.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 31.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.25 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1606), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EHBP1L1]] | +0.69 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[ARID3B]] | +0.66 | +0.66 / +0.56 | both halves | 1e-05 |  |
| [[TNFRSF25]] | +0.66 | +0.60 / +0.59 | both halves | 7e-06 |  |
| [[PLEKHG5]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[FCHSD1]] | +0.65 | +0.64 / +0.52 | both halves | 1e-05 |  |
| [[F11R]] | +0.64 | +0.66 / +0.52 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[GDI1]] | +0.62 | +0.62 / +0.51 | both halves | 1e-05 |  |
| [[PLCB3]] | +0.62 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[TNNT1]] | +0.62 | +0.64 / +0.47 | both halves | 2e-05 |  |
| [[ATG16L2]] | +0.62 | +0.63 / +0.41 | both halves | 4e-05 |  |
| [[GIPR]] | +0.61 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[PITPNM1]] | +0.60 | +0.60 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFX]] | -0.61 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[SETD2]] | -0.60 | -0.47 / -0.59 | both halves | 2e-05 |  |
| [[THOC7]] | -0.60 | -0.64 / -0.47 | both halves | 2e-05 |  |
| [[NIPBL]] | -0.59 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[NSD1]] | -0.59 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[NFYC]] | -0.56 | -0.46 / -0.46 | both halves | 3e-05 |  |
| [[RNF115]] | -0.55 | -0.56 / -0.41 | both halves | 4e-05 |  |
| [[ZNF644]] | -0.55 | -0.53 / -0.48 | both halves | 2e-05 |  |
| [[CREBBP]] | -0.55 | -0.47 / -0.33 | both halves | 1e-04 |  |
| [[INO80D]] | -0.55 | -0.48 / -0.30 | both halves | 2e-04 |  |
| [[PPCS]] | -0.55 | -0.58 / -0.42 | both halves | 4e-05 |  |
| [[GTF3C6]] | -0.54 | -0.47 / -0.39 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PMP22]] | B | PMP22 activity raises LTBP4's level | lines that do not express PMP22 (10) vs lines expressing it (40) | 2.40× lower at baseline in the lines without PMP22 | 0.014 | ⚠ within organs, on part of the lines; also absent: FKBP7, FAM216A, ARHGEF6; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity raises LTBP4's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.9% of all compounds | 0.044 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[ACTR3C]] | B | ACTR3C activity lowers LTBP4's level | lines that do not express ACTR3C (15) vs lines expressing it (35) | 1.86× higher at baseline in the lines without ACTR3C | 0.080 | ⚠ within organs, on part of the lines; also absent: LRRC61, ENPP4, ENSG00000263325 |
| [[MEG3]] | B | MEG3 activity raises LTBP4's level | lines that do not express MEG3 (35) vs lines expressing it (15) | 1.43× lower at baseline in the lines without MEG3 | 0.095 | ⚠ within organs, on part of the lines; also absent: MIR493HG, MEG8, MXRA8 |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NIPBL]] | B | LTBP4 activity lowers NIPBL's level | lines that do not express LTBP4 (6) vs lines expressing it (44) | 1.15× higher at baseline in the lines without LTBP4 | 0.072 | ⚠ within organs, on part of the lines; also absent: TMEM132B, STK31, DDX59-AS1 |

## Where it sits

- **Module**: [[Module 208]]; 14 genes; every member is in the + arm (projection on the module's main direction 0.775). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (14.4, -2.6); signed map (-6.5, 46.2). **Vector** length 108, 28.6% of its response variance represented; |z| ≥ 3 in 1,140 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.8 | +4.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.6 | +1.7 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +2.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.1 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.6 | +3.3 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +3.0 | +4.0 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.0 | +1.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +2.4 | +2.7 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -6.0 | -10.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.6 | -16.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.3 | -16.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.5 | -22.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -4.0 | -6.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.6 | -6.3 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -3.5 | -1.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.2 | -5.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.9 | -4.2 |
|  | [[Budesonide (drug)]] 0.05 µM |  | -2.6 | -3.0 |

## What is on record

|  |  |
|---|---|
| Name | latent transforming growth factor beta binding protein 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19q13.2 — chr19:40,592,883-40,629,818 (+) |
| Ensembl biotype | protein_coding |
| Also known as | LTBP-4, LTBP-4L, FLJ46318, FLJ90018 |
| Gene groups (HGNC) | Latent transforming growth factor beta binding proteins |
| Reactome | 6 pathways, smallest: Molecules associated with elastic fibres; Elastic fibre formation; TGF-beta receptor signaling activates SMADs |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N2S1](https://www.uniprot.org/uniprotkb/Q8N2S1) (Latent-transforming growth factor beta-binding protein 4):

> Key regulator of transforming growth factor beta (TGFB1, TGFB2 and TGFB3) that controls TGF-beta activation by maintaining it in a latent state during storage in extracellular space. Associates specifically via disulfide bonds with the Latency-associated peptide (LAP), which is the regulatory chain of TGF-beta, and regulates integrin-dependent activation of TGF-beta.

**Summary**, from NCBI Gene [8425](https://www.ncbi.nlm.nih.gov/gene/8425):

> The protein encoded by this gene binds transforming growth factor beta (TGFB) as it is secreted and targeted to the extracellular matrix. TGFB is biologically latent after secretion and insertion into the extracellular matrix, and sheds TGFB and other proteins upon activation. Defects in this gene may be a cause of cutis laxa and severe pulmonary, gastrointestinal, and urinary abnormalities. Three transcript variants encoding different isoforms have been found for this gene.[provided by RefSeq, …

**Accessions** — [HGNC:6717](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6717) · Entrez [8425](https://www.ncbi.nlm.nih.gov/gene/8425) · UniProt [Q8N2S1](https://www.uniprot.org/uniprotkb/Q8N2S1) · Ensembl [ENSG00000090006](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000090006)

## Data

Gene col 1606: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1606); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1606, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1606]; `tensor/DDL_lfc|DDL_z.npy` [1606]; `embed/gene_vectors.npy` [1606]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1606 or target_col == 1606). Every well: [[LTBP4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LTBP4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
