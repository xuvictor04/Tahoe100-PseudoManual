---
symbol: "AGAP6"
type: "gene"
col: 12820
ensembl_id: "ENSG00000204149"
name: "ArfGAP with GTPase domain, ankyrin repeat and PH domain 6"
location: "10q11.23"
module: 5
arm: "+"
pooled_cpm: 11.74
n_lines_expressing: 50
n_dd_up: 42
n_dd_down: 0
n_dd_up_clean: 25
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/005"]
generated_by: "tahoemap"
---

# AGAP6

*ArfGAP with GTPase domain, ankyrin repeat and PH domain 6* — 10q11.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 42 drug-doses (17 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.26× (z +19.5, q 0e+00, up in 41 of 47 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 2 lines (NCI-H1792 0.104×, PANC-1 0.273×; ⚠ transcription drop; cell-cycle shift, explains ~66% of this change); [[Radotinib (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0637×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (NCI-H2030 0.169×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (SNU-1 0.0907×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TIMM23B-AGAP6]] (+0.84, fdr 7e-06, ⚠ same locus), [[GTPBP4]] (+0.67, fdr 7e-06), [[AGAP5]] (+0.64, fdr 1e-05), [[MYH3]] (+0.64, fdr 2e-05); moves opposite to [[RYBP]] (-0.65, fdr 1e-05), [[SNX30]] (-0.64, fdr 1e-05), [[LTA4H]] (-0.63, fdr 1e-05).
> It sits in the **+** arm of [[Module 005]] (MYC targets v2).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 18 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 42 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 17 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12820.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.26×** | +19.5 | 0e+00 | 41/47 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **6.62×** | +16.7 | 0e+00 | 42/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.32×** | +14.2 | 1e-43 | 36/44 (NCI-H1573, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.68×** | +12.4 | 3e-33 | 31/45 (CFPAC-1, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Harringtonine (drug)]] 5 µM |  | **2.14×** | +12.4 | 3e-33 | 37/46 (SW480, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.05×** | +12.1 | 9e-32 | 38/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.03×** | +11.9 | 6e-31 | 36/47 (LS 180, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **3.82×** | +11.9 | 1e-30 | 35/44 (SW480, PANC-1, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.86×** | +10.5 | 5e-24 | 39/47 (SW480, SNU-423, …) | all doses, stronger at high dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.80×** | +10.0 | 1e-21 | 28/47 (NCI-H460, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.83×** | +9.8 | 6e-21 | 32/46 (SW480, HOP62, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.78×** | +9.7 | 9e-21 | 28/46 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.81×** | +9.6 | 3e-20 | 31/46 (SW480, C32, …) | top dose only |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **1.76×** | +9.5 | 7e-20 | 29/47 (A-172, SW480, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.70×** | +8.9 | 2e-17 | 32/47 (SW480, A-172, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.68×** | +8.7 | 8e-17 | 29/47 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.66×** | +8.6 | 3e-16 | 28/47 (SW480, SK-MEL-2, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.62×** | +8.1 | 1e-14 | 31/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.66×** | +8.1 | 2e-14 | 29/45 (PANC-1, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.44×** | +6.1 | 3e-08 | 21/46 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **1.40×** | +5.3 | 2e-06 | 16/47 (LOX-IMVI, SW1417, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12820.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Docetaxel (drug)]] 0.05 µM in 2 lines (NCI-H1792 0.104×, PANC-1 0.273×; ⚠ transcription drop; cell-cycle shift, explains ~66% of this change); [[Radotinib (drug)]] 0.5 µM in 1 line (RPMI-7951 0.0637×); [[Canagliflozin (drug)]] 0.05 µM in 1 line (NCI-H2030 0.169×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (SNU-1 0.0907×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | 0.867× | -3.5 | 0.22 | 12/48 (LS 180, SW 1088, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | 0.823× | -3.4 | 0.22 | 11/47 (SNU-1, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.852× | -3.1 | 0.29 | 6/48 (A-427, SK-MEL-2, …) | two highest doses | noisy plate (z scaled) |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~32% of this change | 0.836× | -3.1 | 0.29 | 4/48 (RKO, RPMI-7951, …) | inconsistent across doses |  |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | 0.834× | -3.0 | 0.30 | 9/46 (SHP-77, AsPC-1, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.53 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12820. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 16.4 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.57× (z +11.4) | [[Docetaxel (drug)]] 0.05 µM 0.273× (z -11.1) ⚠ transcription drop; cell-cycle shift, explains ~66% of this change |
| [[LoVo (line)]] | wt | 14.8 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.70× (z +10.3) | — |
| [[NCI-H1573 (line)]] | alt | 9.67 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.64× (z +11.4) | — |
| [[NCI-H460 (line)]] | wt | 15.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.38× (z +9.5) | — |
| [[SW480 (line)]] | alt | 18.2 | 2 (1 ⚠) | 0 | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 3.00× (z +9.5) ⚠ cell-cycle shift, explains ~34% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 6.87× (z +9.1) | — |
| [[LS 180 (line)]] | wt | 12.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.32× (z +9.5) | — |
| [[NCI-H1792 (line)]] | alt | 9.02 | 0 | 1 (1 ⚠) | — | [[Docetaxel (drug)]] 0.05 µM 0.104× (z -11.5) ⚠ transcription drop; cell-cycle shift, explains ~66% of this change |
| [[NCI-H2030 (line)]] | alt | 13.7 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.169× (z -10.9) |
| [[NCI-H2347 (line)]] | alt | 5.31 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +8.8) | — |
| [[RPMI-7951 (line)]] | alt | 10.3 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0637× (z -11.2) |
| [[SNU-1 (line)]] | wt | 15.9 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.0907× (z -9.7) |
| [[A-172 (line)]] | wt | 9.22 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 9.46 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 8.87 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.23 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.16 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.58 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.10 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 9.53 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.61 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.02 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.42 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 22.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.60 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 16.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12820), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*66 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TIMM23B-AGAP6]] | +0.84 | +0.83 / +0.81 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[GTPBP4]] | +0.67 | +0.64 / +0.66 | both halves | 7e-06 |  |
| [[AGAP5]] | +0.64 | +0.64 / +0.57 | both halves | 1e-05 | same gene group; STRING 531 |
| [[MYH3]] | +0.64 | +0.69 / +0.48 | both halves | 2e-05 |  |
| [[SDAD1]] | +0.62 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[RPTOR]] | +0.62 | +0.62 / +0.47 | both halves | 2e-05 |  |
| [[DNAJC11]] | +0.61 | +0.65 / +0.53 | both halves | 1e-05 |  |
| [[KCNJ14]] | +0.61 | +0.62 / +0.56 | both halves | 1e-05 |  |
| [[TRAPPC12]] | +0.60 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[AGAP4]] | +0.59 | +0.65 / +0.53 | both halves | 1e-05 | same gene group; STRING 925 |
| [[MCM3AP]] | +0.59 | +0.59 / +0.47 | both halves | 2e-05 |  |
| [[CDR2]] | +0.59 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[DPH5-DT]] | +0.59 | +0.64 / +0.47 | both halves | 2e-05 |  |

## Genes that move opposite

*34 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RYBP]] | -0.65 | -0.56 / -0.65 | both halves | 1e-05 |  |
| [[SNX30]] | -0.64 | -0.64 / -0.53 | both halves | 1e-05 |  |
| [[LTA4H]] | -0.63 | -0.57 / -0.56 | both halves | 1e-05 |  |
| [[TEC]] | -0.63 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[FHIP1A]] | -0.62 | -0.62 / -0.59 | both halves | 7e-06 |  |
| [[RAB8B]] | -0.62 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[GPR160]] | -0.61 | -0.62 / -0.52 | both halves | 1e-05 |  |
| [[SLC25A30]] | -0.60 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[PPP1R2]] | -0.59 | -0.64 / -0.49 | both halves | 1e-05 |  |
| [[SPOPL]] | -0.59 | -0.54 / -0.57 | both halves | 1e-05 |  |
| [[FAM102B]] | -0.58 | -0.59 / -0.44 | both halves | 3e-05 |  |
| [[FNBP1L]] | -0.58 | -0.59 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AGAP6's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.0% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[NR3C2]] | B | NR3C2 activity lowers AGAP6's level | lines that do not express NR3C2 (15) vs lines expressing it (35) | 1.25× higher at baseline in the lines without NR3C2 | 0.065 | ⚠ within organs, on part of the lines; also absent: ENSG00000249631, ENSG00000287292, SATB1; maybe low, not absent |
| [[LRCH2]] | B | LRCH2 activity lowers AGAP6's level | lines that do not express LRCH2 (27) vs lines expressing it (23) | 1.29× higher at baseline in the lines without LRCH2 | 0.080 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: PDGFRA, ENSG00000263655, PCDH17 |
| [[MTHFD1L]] | C | MTHFD1L activity raises AGAP6's level | lines that do not express MTHFD1L (3) vs lines expressing it (47) | 1.88× lower at baseline in the lines without MTHFD1L | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: MIR3659HG, SLC4A7, HCN2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 005]] — MYC targets v2; 244 genes; this gene is in the **+** arm (projection on the module's main direction 0.660). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (9.7, -11.0); signed map (2.7, -47.4). **Vector** length 66.1, 11.2% of its response variance represented; |z| ≥ 3 in 1,185 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *tRNA modification in the nucleus and cytosol* (reactome, mean cos +0.52 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +3.7 | +16.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.4 | +11.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +2.8 | +8.1 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | +2.4 | +9.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~71% of this change | +2.3 | +7.0 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.2 | +5.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.0 | +4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +8.6 |
|  | [[Lactate (calcium) (drug)]] 0.5 µM |  | +1.4 | -1.3 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -3.5 | -3.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -3.1 | -1.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | -2.8 | -3.4 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -0.4 |
|  | [[Dimethyl fumarate (drug)]] 5 µM |  | -2.1 | -1.4 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -2.8 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.7 | +0.9 |
|  | [[Fumaric acid (drug)]] 5 µM |  | -1.4 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | ArfGAP with GTPase domain, ankyrin repeat and PH domain 6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q11.23 — chr10:49,982,190-50,011,654 (+) |
| Ensembl biotype | protein_coding |
| Also known as | bA324H6.1; previously CTGLF3 |
| Gene groups (HGNC) | ArfGAPs; Ankyrin repeat domain containing; BAR-PH domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5VW22](https://www.uniprot.org/uniprotkb/Q5VW22) (Arf-GAP with GTPase, ANK repeat and PH domain-containing protein 6):

> Putative GTPase-activating protein.

**Summary**, from NCBI Gene [414189](https://www.ncbi.nlm.nih.gov/gene/414189):

> Predicted to enable GTPase activator activity and GTPase activity. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23466](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23466) · Entrez [414189](https://www.ncbi.nlm.nih.gov/gene/414189) · UniProt [Q5VW22](https://www.uniprot.org/uniprotkb/Q5VW22) · Ensembl [ENSG00000204149](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204149)

## Data

Gene col 12820: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12820); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12820, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12820]; `tensor/DDL_lfc|DDL_z.npy` [12820]; `embed/gene_vectors.npy` [12820]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12820 or target_col == 12820). Every well: [[AGAP6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AGAP6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
