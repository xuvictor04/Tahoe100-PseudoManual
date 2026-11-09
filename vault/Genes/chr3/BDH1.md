---
symbol: "BDH1"
type: "gene"
col: 8426
ensembl_id: "ENSG00000161267"
name: "3-hydroxybutyrate dehydrogenase 1"
location: "3q29"
module: 14
arm: "+"
pooled_cpm: 20.0
n_lines_expressing: 39
n_dd_up: 6
n_dd_down: 34
n_dd_up_clean: 5
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 5
direction_downstream: 3
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# BDH1

*3-hydroxybutyrate dehydrogenase 1* — 3q29

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.57× (z +6.9, q 3e-09, up in 10 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.28× (z +5.6, q 8e-06, up in 17 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.297× (z -27.4, q 0e+00, down in 28 of 35 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CRACR2A]] (+0.58, fdr 2e-05), [[SLC43A1]] (+0.52, fdr 2e-05), [[TMEM181]] (+0.50, fdr 1e-04); moves opposite to [[CDKN2B]] (-0.58, fdr 1e-05), [[C2orf74-DT]] (-0.58, fdr 1e-05), [[COL5A2]] (-0.54, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[RORC]] → it (grade B ⚠); 3 go from it, the strongest it → [[DCLK2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8426.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +6.9 | 3e-09 | 10/21 (LoVo, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.28×** | +5.6 | 8e-06 | 17/33 (HEC-1-A, AN3 CA, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.28×** | +3.9 | 0.019 | 9/37 (NCI-H2347, SW1417, …) | top dose only |  |
| [[Tofacitinib (drug)]] 5 µM |  | 1.16× | +3.4 | 0.073 | 11/35 (COLO 205, NCI-H2347, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.24×** | +3.4 | 0.073 | 7/34 (Hs 766T, NCI-H1792, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **1.50×** | +3.4 | 0.073 | 10/32 (SW1417, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Vortioxetine (drug)]] 0.5 µM |  | **1.23×** | +3.3 | 0.088 | 5/36 (KATO III, SK-MEL-2, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | 1.23× | +3.1 | 0.12 | 4/36 (SW1417, SW480, …) | top dose only | plate-row cell shift; position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | 1.22× | +3.1 | 0.12 | 8/34 (LS 180, SW480, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | 1.21× | +3.0 | 0.14 | 8/33 (Hs 766T, SW48, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.21× | +3.0 | 0.14 | 11/36 (KATO III, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 11 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8426.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.297×** | -27.4 | 0e+00 | 28/35 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.239×** | -22.8 | 0e+00 | 31/33 (RKO, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.265×** | -20.3 | 0e+00 | 31/34 (J82, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.343×** | -17.0 | 0e+00 | 30/36 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.349×** | -16.7 | 0e+00 | 30/36 (SW480, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.352×** | -16.6 | 0e+00 | 31/36 (MIA PaCa-2, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.406×** | -14.3 | 1e-44 | 28/33 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.430×** | -13.4 | 2e-39 | 27/36 (MIA PaCa-2, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.445×** | -12.9 | 3e-36 | 26/36 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.456×** | -12.5 | 5e-34 | 28/35 (SW480, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.597×** | -11.6 | 2e-29 | 26/36 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.491×** | -11.3 | 5e-28 | 23/35 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.386×** | -7.9 | 1e-13 | 22/34 (SW480, J82, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~15% here); composition shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.611×** | -7.5 | 2e-12 | 20/31 (NCI-H2347, KATO III, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.643×** | -6.8 | 5e-10 | 19/31 (J82, LoVo, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.657×** | -6.7 | 8e-10 | 22/33 (KATO III, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.684×** | -6.0 | 5e-08 | 19/34 (NCI-H2347, AN3 CA, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.776×** | -5.7 | 4e-07 | 19/36 (NCI-H2347, NCI-H1792, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.20 per unit of S-phase module lfc, -0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8426. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 58.6 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -21.7) |
| [[SW480 (line)]] | alt | 38.0 | 0 | 12 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.105× (z -23.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.158× (z -19.3) |
| [[COLO 205 (line)]] | alt | 64.8 | 0 | 10 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.141× (z -13.3) |
| [[KATO III (line)]] | alt | 39.7 | 0 | 10 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -18.2) |
| [[NCI-H2347 (line)]] | alt | 25.0 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -20.1) |
| [[LS 180 (line)]] | wt | 43.3 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.297× (z -14.1) |
| [[MIA PaCa-2 (line)]] | alt | 81.8 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -21.8) |
| [[RKO (line)]] | wt | 33.6 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0317× (z -21.1) |
| [[J82 (line)]] | alt | 40.6 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -19.7) |
| [[SW 900 (line)]] | alt | 18.1 | 0 | 6 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0747× (z -14.4) |
| [[SW1417 (line)]] | alt | 46.9 | 0 | 6 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.171× (z -15.7) |
| [[HEC-1-A (line)]] | alt | 17.0 | 1 | 4 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.78× (z +10.6) | [[Dinaciclib (drug)]] 5 µM 0.181× (z -12.1) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.313× (z -12.1) |
| [[LoVo (line)]] | wt | 14.6 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.147× (z -12.2) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.238× (z -9.1) |
| [[SK-MEL-2 (line)]] | alt | 32.6 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -18.5) |
| [[AsPC-1 (line)]] | alt | 17.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -14.0) |
| [[HOP62 (line)]] | alt | 27.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -17.0) |
| [[Panc 03.27 (line)]] | alt | 21.0 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -14.4) |
| [[RPMI-7951 (line)]] | alt | 22.6 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.187× (z -12.4) |
| [[BT-474 (line)]] | alt | 35.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -14.9) |
| [[SHP-77 (line)]] | alt | 15.5 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.210× (z -8.8) |
| [[HCT15 (line)]] | alt | 33.7 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.204× (z -9.1) |
| [[Hs 766T (line)]] | wt | 11.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.240× (z -9.5) |
| [[NCI-H1792 (line)]] | alt | 10.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0739× (z -12.1) |
| [[SNU-1 (line)]] | wt | 21.0 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0778× (z -10.9) |
| [[SW48 (line)]] | wt | 15.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.215× (z -8.5) |
| [[A-172 (line)]] | wt | 2.86 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.34 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 4.58 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 19.0 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.60 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.64 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 19.5 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 6.14 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.55 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.97 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.12 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 3.87 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.67 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.07 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8426), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*49 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CRACR2A]] | +0.58 | +0.63 / +0.48 | both halves | 2e-05 |  |
| [[SLC43A1]] | +0.52 | +0.47 / +0.50 | both halves | 2e-05 |  |
| [[TMEM181]] | +0.50 | +0.35 / +0.52 | both halves | 1e-04 |  |
| [[SFXN2]] | +0.50 | +0.39 / +0.50 | both halves | 5e-05 |  |
| [[GOLGA2P5-1]] | +0.50 | +0.31 / +0.55 | both halves | 2e-04 |  |
| [[GOLGA2P5]] | +0.50 | +0.34 / +0.47 | both halves | 1e-04 |  |
| [[ITGA9-AS1]] | +0.50 | +0.43 / +0.58 | both halves | 3e-05 |  |
| [[IL20RA]] | +0.49 | +0.52 / +0.40 | both halves | 4e-05 |  |
| [[MAPK13]] | +0.49 | +0.54 / +0.34 | both halves | 1e-04 |  |
| [[ABO]] | +0.47 | +0.55 / +0.33 | both halves | 1e-04 |  |
| [[CFAP92]] | +0.46 | +0.34 / +0.38 | both halves | 1e-04 |  |
| [[KCNE3]] | +0.46 | +0.51 / +0.32 | both halves | 2e-04 |  |

## Genes that move opposite

*51 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDKN2B]] | -0.58 | -0.49 / -0.67 | both halves | 1e-05 |  |
| [[C2orf74-DT]] | -0.58 | -0.56 / -0.53 | both halves | 1e-05 |  |
| [[COL5A2]] | -0.54 | -0.51 / -0.45 | both halves | 3e-05 |  |
| [[IGSF1]] | -0.53 | -0.47 / -0.54 | both halves | 2e-05 |  |
| [[MARCKS]] | -0.50 | -0.45 / -0.45 | both halves | 3e-05 |  |
| [[MIR3171HG]] | -0.50 | -0.43 / -0.41 | both halves | 4e-05 |  |
| [[MSC-AS1]] | -0.48 | -0.54 / -0.32 | both halves | 2e-04 |  |
| [[MSX2]] | -0.47 | -0.40 / -0.47 | both halves | 5e-05 |  |
| [[TRIM5]] | -0.46 | -0.44 / -0.44 | both halves | 3e-05 |  |
| [[B2M]] | -0.45 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[C1R]] | -0.45 | -0.40 / -0.36 | both halves | 9e-05 |  |
| [[LINC00648]] | -0.45 | -0.35 / -0.33 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RORC]] | B | RORC activity raises BDH1's level | lines that do not express RORC (30) vs lines expressing it (20) | 2.84× lower at baseline in the lines without RORC | 0.001 | ⚠ within organs, on part of the lines; also absent: LRG1, LINC03040, ATP2C2 |
| [[CRACR2A]] | B | CRACR2A activity raises BDH1's level | lines that do not express CRACR2A (20) vs lines expressing it (30) | 3.11× lower at baseline in the lines without CRACR2A | 0.009 | ⚠ within organs, on part of the lines; also absent: ICA1, ABO, ENSG00000235726 |
| [[P3H2]] | B | P3H2 activity lowers BDH1's level | lines that do not express P3H2 (28) vs lines expressing it (22) | 2.17× higher at baseline in the lines without P3H2 | 0.045 | ⚠ within organs, on part of the lines; also absent: P3H2-AS1, SRGN, SPOCK1 |
| [[MLPH]] | B | MLPH activity raises BDH1's level | lines that do not express MLPH (13) vs lines expressing it (37) | 1.88× lower at baseline in the lines without MLPH | 0.077 | ⚠ within organs, on part of the lines; also absent: GBP3, LGALS3, FBXO32 |
| [[SYK]] | B | SYK activity raises BDH1's level | lines that do not express SYK (30) vs lines expressing it (20) | 2.57× lower at baseline in the lines without SYK | 0.095 | ⚠ within organs, on part of the lines; also absent: TNFSF15, ITGB6, ST14 |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[DCLK2]] | B | BDH1 activity lowers DCLK2's level | lines that do not express BDH1 (11) vs lines expressing it (39) | 4.10× higher at baseline in the lines without BDH1 | 0.042 | ⚠ within organs, on part of the lines; also absent: ZNF785, STAP2 |
| [[P3H2]] | B | BDH1 activity lowers P3H2's level | lines that do not express BDH1 (11) vs lines expressing it (39) | 4.24× higher at baseline in the lines without BDH1 | 0.047 | ⚠ within organs, on part of the lines; also absent: ZNF785, STAP2 |
| [[CRACR2A]] | B | BDH1 activity raises CRACR2A's level | lines that do not express BDH1 (11) vs lines expressing it (39) | 3.92× lower at baseline in the lines without BDH1 | 0.052 | ⚠ within organs, on part of the lines; also absent: ZNF785, STAP2 |

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction -0.253). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-8.6, 40.7); signed map (38.1, -15.8). **Vector** length 91.2, 21.1% of its response variance represented; |z| ≥ 3 in 1,095 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +5.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.8 | +2.2 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +2.7 | +2.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.6 | +6.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +2.5 | +0.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | +1.6 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +0.3 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.5 | +2.8 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +1.4 | +2.7 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.3 | +1.7 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -5.8 | -11.6 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.5 | -6.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -3.7 | -16.6 |
|  | [[Binimetinib (drug)]] 5 µM |  | -3.0 | -2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -2.7 | -1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.7 | -3.4 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.7 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | 3-hydroxybutyrate dehydrogenase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q29 — chr3:197,509,783-197,573,323 (-) |
| Ensembl biotype | protein_coding |
| Also known as | SDR9C1; previously BDH |
| Gene groups (HGNC) | Short chain dehydrogenase/reductase superfamily |
| Reactome | 5 pathways, smallest: Utilization of Ketone Bodies; Synthesis of Ketone Bodies; Ketone body metabolism |
| Matched by | ensembl_id |

UniProt [Q02338](https://www.uniprot.org/uniprotkb/Q02338) carries no function annotation.

**Summary**, from NCBI Gene [622](https://www.ncbi.nlm.nih.gov/gene/622):

> This gene encodes a member of the short-chain dehydrogenase/reductase gene family. The encoded protein forms a homotetrameric lipid-requiring enzyme of the mitochondrial membrane and has a specific requirement for phosphatidylcholine for optimal enzymatic activity. The encoded protein catalyzes the interconversion of acetoacetate and (R)-3-hydroxybutyrate, the two major ketone bodies produced during fatty acid catabolism. Alternatively spliced transcript variants encoding the same protein have …

**Accessions** — [HGNC:1027](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1027) · Entrez [622](https://www.ncbi.nlm.nih.gov/gene/622) · UniProt [Q02338](https://www.uniprot.org/uniprotkb/Q02338) · Ensembl [ENSG00000161267](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000161267)

## Data

Gene col 8426: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8426); `tables/drug_effects.parquet` (49 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8426, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8426]; `tensor/DDL_lfc|DDL_z.npy` [8426]; `embed/gene_vectors.npy` [8426]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8426 or target_col == 8426). Every well: [[BDH1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BDH1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
