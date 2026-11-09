---
symbol: "PDGFB"
type: "gene"
col: 1922
ensembl_id: "ENSG00000100311"
name: "platelet derived growth factor subunit B"
location: "22q13.1"
module: 206
arm: "+"
pooled_cpm: 41.02
n_lines_expressing: 34
n_dd_up: 3
n_dd_down: 63
n_dd_up_clean: 3
n_dd_down_clean: 47
in_vector_space: true
direction_upstream: 10
direction_downstream: 28
tags: ["gene", "module/206"]
generated_by: "tahoemap"
---

# PDGFB

*platelet derived growth factor subunit B* — 22q13.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 3 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 1.66× (z +4.6, q 0.003, up in 13 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 63 drug-doses (16 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.213× (z -16.1, q 0e+00, down in 30 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[N4BP3]] (+0.65, fdr 1e-05), [[EHD1]] (+0.65, fdr 1e-05), [[BIK]] (+0.63, fdr 1e-05); moves opposite to [[PDS5A]] (-0.56, fdr 3e-05), [[MGST1]] (-0.54, fdr 4e-05), [[SUCLG2]] (-0.53, fdr 1e-05).
> It is in [[Module 206]], a single-armed module (Constitutive Signaling by Aberrant PI3K in Cancer).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[SERPINB1]] → it (grade B ⚠); 28 go from it, the strongest it → [[CELSR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 3 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1922.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.66×** | +4.6 | 0.003 | 13/32 (A-172, J82, …) | two highest doses | cell-cycle shift (explains ~17% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.31×** | +4.0 | 0.019 | 15/32 (J82, A498, …) | two highest doses | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | **2.06×** | +3.9 | 0.019 | 14/32 (HOP62, HT-29, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | 1.40× | +3.4 | 0.11 | 15/31 (RPMI-7951, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Vilanterol (drug)]] 5 µM |  | 1.23× | +3.1 | 0.24 | 10/32 (A-172, HepG2/C3A, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 64 in all, 16 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 63 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 16 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1922.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.213×** | -16.1 | 0e+00 | 30/32 (Hs 766T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.264×** | -13.8 | 4e-41 | 30/32 (A-172, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.269×** | -13.6 | 4e-40 | 27/32 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.355×** | -10.8 | 8e-25 | 27/32 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.482×** | -10.7 | 9e-25 | 26/32 (PANC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.380×** | -10.1 | 8e-22 | 23/31 (HOP62, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.373×** | -9.8 | 6e-21 | 25/31 (HOP62, Hs 766T, …) | top dose only | cell-cycle shift (explains ~3% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.388×** | -9.8 | 6e-21 | 26/32 (HOP62, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.515×** | -9.7 | 1e-20 | 26/32 (SNU-423, A-172, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~21% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.396×** | -9.6 | 4e-20 | 24/32 (HepG2/C3A, HOP62, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.404×** | -9.4 | 3e-19 | 29/32 (HOP62, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~32% of this change | **0.403×** | -9.1 | 6e-18 | 24/31 (Hs 766T, HOP62, …) | rises with dose | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.433×** | -8.7 | 2e-16 | 22/29 (Hs 766T, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.448×** | -8.3 | 3e-15 | 24/31 (NCI-H1792, Hs 766T, …) | all doses, flat | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.457×** | -8.1 | 2e-14 | 26/32 (HOP62, A-172, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.538×** | -6.4 | 4e-09 | 20/32 (SW 900, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.533×** | -6.2 | 2e-08 | 22/32 (HOP62, A-172, …) | all doses, flat | cell-cycle shift (explains ~19% here); position effect removed |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.557×** | -6.1 | 3e-08 | 24/32 (H4, NCI-H1792, …) | all doses, flat | position effect removed |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.570×** | -5.8 | 1e-07 | 17/31 (H4, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.678×** | -5.7 | 3e-07 | 19/32 (HOP62, Hs 766T, …) | top dose only | position effect removed |
| [[Budesonide (drug)]] 5 µM |  | **0.580×** | -5.6 | 4e-07 | 24/32 (Hs 766T, Panc 03.27, …) | all doses, stronger at high dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.67 per unit of S-phase module lfc, +0.59 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1922. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 111 | 0 | 26 (12 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.107× (z -23.1) |
| [[Hs 766T (line)]] | wt | 224 | 0 | 26 (12 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0550× (z -26.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.0664× (z -25.1) |
| [[A-172 (line)]] | wt | 111 | 0 | 24 (10 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.137× (z -23.2) |
| [[PANC-1 (line)]] | alt | 139 | 1 (1 ⚠) | 19 (10 ⚠) | [[Harringtonine (drug)]] 5 µM 3.77× (z +11.6) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -26.5) |
| [[SW480 (line)]] | alt | 39.2 | 0 | 20 (12 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.139× (z -16.8) |
| [[NCI-H1792 (line)]] | alt | 50.3 | 0 | 19 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0506× (z -16.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.127× (z -16.3) |
| [[HepG2_C3A (line)]] | wt | 298 | 0 | 12 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0734× (z -19.8) |
| [[H4 (line)]] | wt | 31.1 | 0 | 11 (2 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0247× (z -13.6) |
| [[MIA PaCa-2 (line)]] | alt | 42.3 | 0 | 10 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0594× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Selinexor (drug)]] 5 µM 0.173× (z -13.4) |
| [[CFPAC-1 (line)]] | alt | 107 | 1 (1 ⚠) | 7 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.76× (z +9.5) ⚠ cell-cycle shift, would explain all of this change | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.213× (z -14.5) |
| [[RPMI-7951 (line)]] | alt | 26.4 | 0 | 7 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0290× (z -15.1) |
| [[SNU-423 (line)]] | alt | 29.0 | 1 (1 ⚠) | 6 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.37× (z +14.6) ⚠ cell-cycle shift, would explain all of this change | [[Selinexor (drug)]] 5 µM 0.140× (z -15.5) |
| [[HEC-1-A (line)]] | alt | 46.9 | 2 (2 ⚠) | 4 (2 ⚠) | [[Harringtonine (drug)]] 5 µM 4.45× (z +11.0) ⚠ cell-cycle shift, would explain all of this change | [[Dinaciclib (drug)]] 5 µM 0.0717× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.143× (z -14.8) |
| [[A498 (line)]] | wt | 30.8 | 3 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.14× (z +18.2) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 5.49× (z +8.7) | — |
| [[Panc 03.27 (line)]] | alt | 29.7 | 2 (2 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 8.78× (z +19.3) ⚠ cell-cycle shift, would explain all of this change | [[Budesonide (drug)]] 5 µM 0.230× (z -9.1) |
| [[COLO 205 (line)]] | alt | 17.8 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0613× (z -11.4) ⚠ toxic · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0712× (z -11.2) |
| [[J82 (line)]] | alt | 17.8 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.59× (z +18.7) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SW 900 (line)]] | alt | 18.0 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.0641× (z -10.3) |
| [[A549 (line)]] | wt | 20.2 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.149× (z -9.3) |
| [[KATO III (line)]] | alt | 14.7 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.00× (z +12.3) ⚠ cell-cycle shift, would explain all of this change | — |
| [[SK-MEL-2 (line)]] | alt | 20.2 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0788× (z -9.6) |
| [[SW1417 (line)]] | alt | 50.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -11.5) |
| [[A-427 (line)]] | wt | 3.74 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 5.62 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.87 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.53 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.05 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 30.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.24 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.86 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.84 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 6.73 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.01 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 26.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.96 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.66 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 30.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.35 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 4.32 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.78 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 17.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1922), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[N4BP3]] | +0.65 | +0.56 / +0.63 | both halves | 1e-05 |  |
| [[EHD1]] | +0.65 | +0.56 / +0.65 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT |
| [[BIK]] | +0.63 | +0.53 / +0.54 | both halves | 1e-05 |  |
| [[RARA]] | +0.62 | +0.60 / +0.61 | both halves | 7e-06 |  |
| [[PDGFA]] | +0.61 | +0.58 / +0.60 | both halves | 8e-06 | same gene group; pathway: Constitutive Signaling by Aberrant PI3K in Cancer; STRING 998 |
| [[ADAM8]] | +0.60 | +0.63 / +0.53 | both halves | 1e-05 | pathway: Extracellular matrix organization |
| [[FSCN1]] | +0.60 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[LGALS1]] | +0.60 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[NFKBIE]] | +0.60 | +0.48 / +0.56 | both halves | 2e-05 |  |
| [[SOX9]] | +0.59 | +0.52 / +0.66 | both halves | 1e-05 |  |
| [[SPNS2]] | +0.58 | +0.55 / +0.51 | both halves | 1e-05 |  |
| [[SLC9A7]] | +0.58 | +0.59 / +0.44 | both halves | 3e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PDS5A]] | -0.56 | -0.44 / -0.55 | both halves | 3e-05 |  |
| [[MGST1]] | -0.54 | -0.59 / -0.41 | both halves | 4e-05 |  |
| [[SUCLG2]] | -0.53 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[ADPGK]] | -0.53 | -0.44 / -0.47 | both halves | 3e-05 |  |
| [[NCKAP1]] | -0.53 | -0.42 / -0.46 | both halves | 4e-05 |  |
| [[LARP1]] | -0.52 | -0.47 / -0.52 | both halves | 2e-05 |  |
| [[CERS2]] | -0.52 | -0.42 / -0.35 | both halves | 1e-04 |  |
| [[SEPHS1]] | -0.50 | -0.38 / -0.45 | both halves | 6e-05 |  |
| [[MRPS25]] | -0.50 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[SETD7]] | -0.50 | -0.50 / -0.40 | both halves | 5e-05 |  |
| [[TOR1A]] | -0.50 | -0.50 / -0.28 | both halves | 3e-04 |  |
| [[TRRAP]] | -0.50 | -0.31 / -0.48 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 6, C 4.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SERPINB1]] | B | SERPINB1 activity raises PDGFB's level | lines that do not express SERPINB1 (12) vs lines expressing it (38) | 2.97× lower at baseline in the lines without SERPINB1 | 0.042 | ⚠ within organs, on part of the lines; also absent: ENSG00000285906, SERPINB9P1, LASTR |
| [[N4BP3]] | B | N4BP3 activity raises PDGFB's level | lines that do not express N4BP3 (6) vs lines expressing it (44) | 2.31× lower at baseline in the lines without N4BP3 | 0.060 | ⚠ within organs, on part of the lines; also absent: KIAA1522, ENSG00000257489, CCDC88C; its own permutation p |
| [[RHBDF2]] | B | RHBDF2 activity raises PDGFB's level | lines that do not express RHBDF2 (5) vs lines expressing it (45) | 3.13× lower at baseline in the lines without RHBDF2 | 0.070 | ⚠ within organs, on part of the lines; also absent: DBNDD1, PHF11, ARFGEF3; maybe low, not absent |
| [[BAIAP3]] | B | BAIAP3 activity raises PDGFB's level | lines that do not express BAIAP3 (8) vs lines expressing it (42) | 2.76× lower at baseline in the lines without BAIAP3 | 0.089 | ⚠ within organs, on part of the lines; also absent: PPFIA4; maybe low, not absent; its own permutation p |
| [[CCDC33]] | B | CCDC33 activity raises PDGFB's level | lines that do not express CCDC33 (24) vs lines expressing it (26) | 2.05× lower at baseline in the lines without CCDC33 | 0.089 | ⚠ within organs, on part of the lines; also absent: STRA6, ENSG00000261543, KLF8 |
| [[BIK]] | B | BIK activity raises PDGFB's level | lines that do not express BIK (15) vs lines expressing it (35) | 2.04× lower at baseline in the lines without BIK | 0.096 | ⚠ within organs, on part of the lines; also absent: PRRG4, DMTN, LAMA3 |
| [[KRT19]] | C | KRT19 activity raises PDGFB's level | lines that do not express KRT19 (22) vs lines expressing it (28) | 2.97× lower at baseline in the lines without KRT19 | 0.004 | ⚠ within organs, on part of the lines; also absent: RNF223, TINAGL1, CLDN4; co-absent with the target |
| [[WNT7B]] | C | WNT7B activity raises PDGFB's level | lines that do not express WNT7B (20) vs lines expressing it (30) | 3.43× lower at baseline in the lines without WNT7B | 0.005 | ⚠ within organs, on part of the lines; also absent: ABCC3, NHS, PPARG; co-absent with the target |
| [[ZMIZ1]] | C | ZMIZ1 activity raises PDGFB's level | lines that do not express ZMIZ1 (4) vs lines expressing it (46) | 5.09× lower at baseline in the lines without ZMIZ1 | 0.046 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: WWC3, PYROXD2, NINJ1; maybe low, not absent |
| [[ADAM8]] | C | ADAM8 activity raises PDGFB's level | lines that do not express ADAM8 (28) vs lines expressing it (22) | 3.02× lower at baseline in the lines without ADAM8 | 0.052 | ⚠ within organs, on part of the lines; also absent: PLAU, ENSG00000233539, CST6; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 25, C 3. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CELSR1]] | B | PDGFB activity raises CELSR1's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 2.46× lower at baseline in the lines without PDGFB | 0.004 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[GIPR]] | B | PDGFB activity raises GIPR's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 2.15× lower at baseline in the lines without PDGFB | 0.007 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[KRT15]] | B | PDGFB activity raises KRT15's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 2.87× lower at baseline in the lines without PDGFB | 0.009 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[EHD1]] | B | PDGFB activity raises EHD1's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 1.69× lower at baseline in the lines without PDGFB | 0.012 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[AHDC1]] | B | PDGFB activity raises AHDC1's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 1.47× lower at baseline in the lines without PDGFB | 0.012 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[PTAFR]] | B | PDGFB activity raises PTAFR's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 2.44× lower at baseline in the lines without PDGFB | 0.013 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[CCDC33]] | B | PDGFB activity raises CCDC33's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 2.30× lower at baseline in the lines without PDGFB | 0.015 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[SPNS2]] | B | PDGFB activity raises SPNS2's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 2.51× lower at baseline in the lines without PDGFB | 0.022 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[SLC9A7]] | B | PDGFB activity strengthens SLC9A7's drug response | lines that do not express PDGFB (16) vs lines expressing it (33) | the lines without PDGFB respond 0.71× as strongly (z diff +1.38); strongest at Topotecan (hydrochloride) 5 µM: 0.72x vs 0.54x (z diff +2.5) | 0.028 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8; target measured in part of the lines; artifact flags |
| [[CXorf38]] | B | PDGFB activity raises CXorf38's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 1.34× lower at baseline in the lines without PDGFB | 0.038 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[UBE2I]] | B | PDGFB activity raises UBE2I's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 1.21× lower at baseline in the lines without PDGFB | 0.038 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |
| [[CRABP2]] | B | PDGFB activity raises CRABP2's level | lines that do not express PDGFB (16) vs lines expressing it (34) | 2.71× lower at baseline in the lines without PDGFB | 0.039 | ⚠ within organs, on part of the lines; also absent: PRAG1, LGALS3, ADAM8 |

## Where it sits

- **Module**: [[Module 206]] — Constitutive Signaling by Aberrant PI3K in Cancer; 15 genes; every member is in the + arm (projection on the module's main direction 0.782). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (40.7, -1.9); signed map (-0.7, 43.2). **Vector** length 121, 36.6% of its response variance represented; |z| ≥ 3 in 1,349 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +8.2 | +2.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +6.0 | +1.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +4.0 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.0 | +4.6 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~25% of this change | +3.8 | -3.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +2.2 | +3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +3.9 |
|  | [[Vilanterol (drug)]] 5 µM |  | +1.9 | +3.1 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +1.4 |
| fall | [[Selinexor (drug)]] 5 µM |  | -5.1 | -9.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -5.1 | -8.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | -4.8 | -6.9 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -4.8 | -10.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -4.8 | -9.8 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -4.4 | -8.3 |
|  | [[Budesonide (drug)]] 5 µM |  | -4.3 | -5.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -4.2 | -6.1 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | -3.8 | -4.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -3.7 | -8.1 |

## What is on record

|  |  |
|---|---|
| Name | platelet derived growth factor subunit B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.1 — chr22:39,223,359-39,244,982 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SSV; previously SIS |
| Gene groups (HGNC) | PDGF family ligands |
| Hallmark sets | COAGULATION, COMPLEMENT, HYPOXIA |
| Reactome | 19 pathways, smallest: Downstream signal transduction; Signaling by PDGF; Constitutive Signaling by Aberrant PI3K in Cancer |
| Matched by | ensembl_id |

**Function**, from UniProt [P01127](https://www.uniprot.org/uniprotkb/P01127) (Platelet-derived growth factor subunit B):

> Growth factor that plays an essential role in the regulation of embryonic development, cell proliferation, cell migration, survival and chemotaxis. Potent mitogen for cells of mesenchymal origin. Required for normal proliferation and recruitment of pericytes and vascular smooth muscle cells in the central nervous system, skin, lung, heart and placenta. Required for normal blood vessel development, and for normal development of kidney glomeruli. Plays an important role in wound healing. …

**Summary**, from NCBI Gene [5155](https://www.ncbi.nlm.nih.gov/gene/5155):

> This gene encodes a member of the protein family comprised of both platelet-derived growth factors (PDGF) and vascular endothelial growth factors (VEGF). The encoded preproprotein is proteolytically processed to generate platelet-derived growth factor subunit B, which can homodimerize, or alternatively, heterodimerize with the related platelet-derived growth factor subunit A. These proteins bind and activate PDGF receptor tyrosine kinases, which play a role in a wide range of developmental …

**Accessions** — [HGNC:8800](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8800) · Entrez [5155](https://www.ncbi.nlm.nih.gov/gene/5155) · UniProt [P01127](https://www.uniprot.org/uniprotkb/P01127) · Ensembl [ENSG00000100311](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000100311)

## Data

Gene col 1922: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1922); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1922, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1922]; `tensor/DDL_lfc|DDL_z.npy` [1922]; `embed/gene_vectors.npy` [1922]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1922 or target_col == 1922). Every well: [[PDGFB — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PDGFB.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
