---
symbol: "AFG1L"
type: "gene"
col: 5721
ensembl_id: "ENSG00000135537"
name: "AFG1 like ATPase"
location: "6q21"
module: 1
arm: "+"
pooled_cpm: 34.39
n_lines_expressing: 49
n_dd_up: 2
n_dd_down: 30
n_dd_up_clean: 2
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 5
direction_downstream: 0
tags: ["gene", "module/001"]
generated_by: "tahoemap"
---

# AFG1L

*AFG1 like ATPase* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.35× (z +3.9, q 0.045, up in 25 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 30 drug-doses (11 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.402× (z -12.2, q 3e-31, down in 43 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GATB]] (+0.75, fdr 7e-06), [[MRPS7]] (+0.72, fdr 7e-06), [[UTP20]] (+0.72, fdr 7e-06); moves opposite to [[TMEM184B]] (-0.66, fdr 1e-05), [[F11R]] (-0.62, fdr 1e-05), [[WIPI1]] (-0.61, fdr 4e-05).
> It sits in the **+** arm of [[Module 001]] (rRNA processing).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[RALGPS2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5721.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +3.9 | 0.045 | 25/46 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.045 | 18/47 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.17× | +3.0 | 0.41 | 9/47 (PANC-1, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 31 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 30 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5721.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.402×** | -12.2 | 3e-31 | 43/47 (SW480, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.411×** | -11.9 | 5e-30 | 44/47 (SW480, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.413×** | -11.8 | 8e-30 | 43/47 (C-33 A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.468×** | -10.1 | 6e-22 | 39/47 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.497×** | -9.3 | 1e-18 | 37/46 (KATO III, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.546×** | -8.1 | 7e-14 | 40/47 (PANC-1, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.540×** | -7.6 | 3e-12 | 27/42 (A-427, KATO III, …) | all doses, flat | cell-cycle shift (explains ~21% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.554×** | -7.6 | 3e-12 | 33/46 (HCT15, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.595×** | -6.7 | 2e-09 | 32/44 (MIA PaCa-2, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.717×** | -6.3 | 2e-08 | 33/47 (H4, SW480, …) | rises with dose |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.410×** | -6.2 | 2e-08 | 37/46 (RKO, SNU-423, …) | rises with dose | noisy plate (z scaled); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.629×** | -6.2 | 3e-08 | 31/47 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.724×** | -6.1 | 6e-08 | 29/47 (SNU-423, H4, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **0.685×** | -5.0 | 2e-05 | 23/43 (SHP-77, SNU-423, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.491×** | -5.0 | 3e-05 | 29/47 (PANC-1, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~18% here); composition shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.689×** | -4.9 | 3e-05 | 32/47 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.712×** | -4.3 | 4e-04 | 24/47 (NCI-H23, SNU-423, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.539×** | -4.3 | 5e-04 | 24/47 (NCI-H23, SW480, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.798×** | -4.2 | 7e-04 | 22/47 (CFPAC-1, MIA PaCa-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.731×** | -4.2 | 8e-04 | 22/47 (SW480, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.703×** | -4.2 | 8e-04 | 26/47 (SW480, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.753×** | -3.8 | 0.004 | 20/46 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~13% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5721. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C-33 A (line)]] | alt | 115 | 0 | 8 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.136× (z -14.7) |
| [[KATO III (line)]] | alt | 46.2 | 0 | 8 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0951× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.352× (z -8.7) |
| [[MIA PaCa-2 (line)]] | alt | 71.4 | 0 | 8 (4 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.165× (z -14.2) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.254× (z -11.2) |
| [[SNU-1 (line)]] | wt | 72.9 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.281× (z -12.8) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.219× (z -10.9) |
| [[SW480 (line)]] | alt | 41.2 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.229× (z -14.5) |
| [[PANC-1 (line)]] | alt | 64.8 | 0 | 7 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.178× (z -17.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.287× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 26.0 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.214× (z -12.4) |
| [[SNU-423 (line)]] | alt | 47.3 | 0 | 6 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.132× (z -13.7) ⚠ toxic · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.342× (z -10.7) |
| [[LS 180 (line)]] | wt | 37.9 | 0 | 5 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.205× (z -12.8) ⚠ cell-cycle shift, explains ~29% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.281× (z -10.2) |
| [[NCI-H23 (line)]] | alt | 56.3 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.251× (z -12.9) |
| [[HCT15 (line)]] | alt | 66.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.111× (z -15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[A-427 (line)]] | wt | 54.5 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.186× (z -14.8) ⚠ toxic; transcription drop · without an alert: [[Panobinostat (drug)]] 5 µM 0.389× (z -9.0) |
| [[H4 (line)]] | wt | 39.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.117× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change · without an alert: [[Tucidinostat (drug)]] 5 µM 0.327× (z -9.2) |
| [[HOP62 (line)]] | alt | 31.8 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.271× (z -10.0) |
| [[RKO (line)]] | wt | 27.1 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0814× (z -14.1) ⚠ cell-cycle shift, explains ~15% of this change |
| [[BT-474 (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.224× (z -9.0) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 28.8 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -8.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HEC-1-A (line)]] | alt | 30.7 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.323× (z -9.4) |
| [[HT-29 (line)]] | alt | 21.4 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.304× (z -8.5) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 30.3 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.315× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 30.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.218× (z -10.4) |
| [[NCI-H2347 (line)]] | alt | 15.2 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.203× (z -10.4) ⚠ transcription drop; cell-cycle shift, explains ~94% of this change |
| [[NCI-H661 (line)]] | alt | 75.5 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0740× (z -10.4) |
| [[Panc 03.27 (line)]] | alt | 21.9 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.239× (z -8.6) |
| [[RPMI-7951 (line)]] | alt | 43.2 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.138× (z -12.3) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 54.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.261× (z -11.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change |
| [[SK-MEL-2 (line)]] | alt | 41.7 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -9.3) ⚠ cell-cycle shift, explains ~15% of this change |
| [[SW48 (line)]] | wt | 28.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.108× (z -10.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 24.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 28.9 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 26.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 23.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 19.1 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 30.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.1 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 7.84 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5721), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GATB]] | +0.75 | +0.73 / +0.72 | both halves | 7e-06 |  |
| [[MRPS7]] | +0.72 | +0.72 / +0.63 | both halves | 7e-06 |  |
| [[UTP20]] | +0.72 | +0.66 / +0.65 | both halves | 7e-06 |  |
| [[PRORP]] | +0.71 | +0.63 / +0.71 | both halves | 7e-06 |  |
| [[DNAJC11]] | +0.69 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[USP40]] | +0.69 | +0.69 / +0.59 | both halves | 7e-06 |  |
| [[SLX4IP]] | +0.68 | +0.68 / +0.70 | both halves | 7e-06 |  |
| [[TTC27]] | +0.67 | +0.62 / +0.64 | both halves | 7e-06 |  |
| [[FASTKD2]] | +0.67 | +0.59 / +0.63 | both halves | 7e-06 |  |
| [[RIF1]] | +0.65 | +0.61 / +0.58 | both halves | 7e-06 |  |
| [[ZNF507]] | +0.65 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[TASOR]] | +0.65 | +0.62 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM184B]] | -0.66 | -0.61 / -0.57 | both halves | 1e-05 |  |
| [[F11R]] | -0.62 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[WIPI1]] | -0.61 | -0.66 / -0.41 | both halves | 4e-05 |  |
| [[KMT5C]] | -0.61 | -0.59 / -0.50 | both halves | 1e-05 |  |
| [[ADIPOR1]] | -0.61 | -0.57 / -0.45 | both halves | 3e-05 |  |
| [[LINC01881]] | -0.60 | -0.51 / -0.55 | both halves | 1e-05 |  |
| [[TIMP2]] | -0.60 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[RAP1A]] | -0.60 | -0.53 / -0.53 | both halves | 1e-05 |  |
| [[PCMT1]] | -0.58 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[EIF4E3]] | -0.57 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[KLHL7]] | -0.57 | -0.53 / -0.46 | both halves | 2e-05 |  |
| [[C1QL1]] | -0.57 | -0.42 / -0.45 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RALGPS2]] | B | RALGPS2 activity lowers AFG1L's level | lines that do not express RALGPS2 (7) vs lines expressing it (43) | 2.15× higher at baseline in the lines without RALGPS2 | 0.006 | ⚠ within organs, on part of the lines; also absent: NABP1, ITGA2-AS1, GSDMD; maybe low, not absent |
| [[C1QL1]] | B | C1QL1 activity raises AFG1L's level | lines that do not express C1QL1 (22) vs lines expressing it (28) | 1.42× lower at baseline in the lines without C1QL1 | 0.033 | ⚠ within organs, on part of the lines; also absent: CPEB1, PDZD4, BARX1 |
| [[WWOX]] | B | WWOX activity strengthens AFG1L's drug response | lines that do not express WWOX (5) vs lines expressing it (42) | the lines without WWOX respond 0.55× as strongly (z diff +2.32); strongest at Dinaciclib 0.05 µM: 0.98x vs 0.53x (z diff +4.0) | 0.068 | ⚠ within organs, on part of the lines; also absent: ZFHX2, WARS2-AS1, TMCC1-DT; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[CNGA1]] | B | CNGA1 activity lowers AFG1L's level | lines that do not express CNGA1 (5) vs lines expressing it (45) | 1.82× higher at baseline in the lines without CNGA1 | 0.072 | ⚠ within organs, on part of the lines; co-absent genes; also absent: FHIP1A, NIPAL1, RALGPS2 |
| [[LINC00630]] | C | LINC00630's natural level strengthens AFG1L's drug response | LINC00630's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.66, reverse +0.24; direction not clear | 0.058 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 001]] — rRNA processing; 298 genes; this gene is in the **+** arm (projection on the module's main direction 0.626). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (-20.7, 10.9); signed map (5.2, -37.9). **Vector** length 91.3, 24.2% of its response variance represented; |z| ≥ 3 in 1,090 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +5.6 | -2.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.3 | -0.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.0 | -3.4 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.7 | -1.1 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.7 | +1.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.4 | -0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +0.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | +3.2 | +2.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +1.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | -1.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.0 | -6.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -5.0 | -4.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -4.7 | -11.8 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.3 | -11.9 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.0 | -12.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -3.1 | -4.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -2.6 | -6.2 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.5 | -4.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.2 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | AFG1 like ATPase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:108,294,991-108,526,796 (+) |
| Ensembl biotype | protein_coding |
| Also known as | AFG1; previously LACE1 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8WV93](https://www.uniprot.org/uniprotkb/Q8WV93) (AFG1-like ATPase):

> Putative mitochondrial ATPase. Plays a role in mitochondrial morphology and mitochondrial protein metabolism. Promotes degradation of excess nuclear-encoded complex IV subunits (COX4I1, COX5A and COX6A1) and normal activity of complexes III and IV of the respiratory chain. Mediates mitochondrial translocation of TP53 and its transcription-independent apoptosis in response to genotoxic stress.

**Summary**, from NCBI Gene [246269](https://www.ncbi.nlm.nih.gov/gene/246269):

> This gene encodes a mitochondrial integral membrane protein that plays a role in mitochondrial protein homeostasis. The protein contains a P-loop motif and a five-domain structure that is conserved in fly, yeast, and bacteria. It functions to mediate the degradation of nuclear-encoded complex IV subunits. Two conserved estrogen receptor binding sites are located within 2.5 kb of this gene. Polymorphisms in this gene have been associated with bipolar disorder. Alternative splicing results in …

**Accessions** — [HGNC:16411](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16411) · Entrez [246269](https://www.ncbi.nlm.nih.gov/gene/246269) · UniProt [Q8WV93](https://www.uniprot.org/uniprotkb/Q8WV93) · Ensembl [ENSG00000135537](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135537)

## Data

Gene col 5721: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5721); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5721, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5721]; `tensor/DDL_lfc|DDL_z.npy` [5721]; `embed/gene_vectors.npy` [5721]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5721 or target_col == 5721). Every well: [[AFG1L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AFG1L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
