---
symbol: "SLC6A9"
type: "gene"
col: 12228
ensembl_id: "ENSG00000196517"
name: "solute carrier family 6 member 9"
location: "1p34.1"
module: 133
arm: "+"
pooled_cpm: 4.32
n_lines_expressing: 49
n_dd_up: 28
n_dd_down: 19
n_dd_up_clean: 23
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# SLC6A9

*solute carrier family 6 member 9* — 1p34.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 28 drug-doses (5 with an alert ⚠); the strongest is [[Ponatinib (drug)]] 5 µM: 2.76× (z +9.2, q 2e-17, up in 30 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (8 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.386× (z -12.3, q 4e-32, down in 29 of 36 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.351× (z -9.6, q 2e-19, down in 31 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PCK2]] (+0.81, fdr 7e-06), [[MOCOS]] (+0.80, fdr 7e-06), [[MARS1]] (+0.79, fdr 7e-06).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[ULBP1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 28 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12228.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ponatinib (drug)]] 5 µM |  | **2.76×** | +9.2 | 2e-17 | 30/43 (Panc 03.27, HCT15, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **2.29×** | +7.5 | 1e-11 | 28/38 (HEC-1-A, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.77×** | +7.4 | 3e-11 | 27/44 (LS 180, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.73×** | +7.0 | 3e-10 | 27/44 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.70×** | +6.8 | 1e-09 | 16/33 (SW480, LS 180, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.03×** | +6.0 | 2e-07 | 2/9 (LS 180, CFPAC-1) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.92×** | +5.7 | 1e-06 | 0/6 | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.84×** | +5.6 | 2e-06 | 23/44 (SW1417, SW 900, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.82×** | +5.4 | 4e-06 | 3/20 (HEC-1-A, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.73×** | +5.0 | 4e-05 | 12/44 (C-33 A, SW480, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.71×** | +4.9 | 5e-05 | 19/43 (C-33 A, HEC-1-A, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.69×** | +4.8 | 8e-05 | 13/42 (SHP-77, HEC-1-A, …) | two highest doses |  |
| [[Auranofin (drug)]] 5 µM |  | **1.63×** | +4.4 | 4e-04 | 12/41 (LoVo, NCI-H460, …) | top dose only |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.39×** | +4.2 | 9e-04 | 14/43 (Hs 766T, SNU-1, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.58×** | +4.2 | 0.001 | 16/42 (NCI-H1573, NCI-H2030, …) | rises with dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.52×** | +3.8 | 0.004 | 9/44 (HEC-1-A, LS 180, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.52×** | +3.8 | 0.004 | 16/43 (HEC-1-A, SHP-77, …) | two highest doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.30×** | +3.3 | 0.025 | 6/44 (A498, SW 900, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.45×** | +3.3 | 0.030 | 8/37 (NCI-H1573, A549, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 8 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12228.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.386×** | -12.3 | 4e-32 | 29/36 (LoVo, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.301×** | -10.6 | 1e-23 | 31/42 (KATO III, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.351×** | -9.6 | 2e-19 | 31/43 (LoVo, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.362×** | -9.3 | 2e-18 | 26/42 (SW48, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.373×** | -9.0 | 2e-17 | 27/45 (LoVo, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.387×** | -8.7 | 3e-16 | 25/35 (LoVo, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.418×** | -8.0 | 1e-13 | 28/42 (KATO III, LoVo, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.429×** | -7.7 | 7e-13 | 27/43 (LoVo, SW48, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.485×** | -6.6 | 2e-09 | 23/44 (KATO III, PANC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **0.508×** | -6.2 | 3e-08 | 18/31 (PANC-1, A-172, …) | all doses, stronger at high dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.560×** | -5.3 | 6e-06 | 19/42 (SW1417, HT-29, …) | all doses, stronger at high dose | position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.549×** | -5.1 | 2e-05 | 16/32 (SNU-1, HEC-1-A, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.592×** | -4.8 | 7e-05 | 20/43 (PANC-1, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.606×** | -4.6 | 2e-04 | 16/44 (HS-578T, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.748×** | -3.8 | 0.006 | 14/43 (KATO III, HT-29, …) | rises with dose |  |
| [[Diammonium Glycyrrhizinate (drug)]] 5 µM |  | **0.778×** | -3.3 | 0.035 | 10/45 (HOP62, SW480, …) | top dose only |  |
| [[Glycyrrhizic acid (drug)]] 5 µM |  | **0.699×** | -3.2 | 0.047 | 8/42 (C-33 A, HepG2/C3A, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.57 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12228. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 8.87 | 0 | 6 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0501× (z -12.1) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.0751× (z -10.5) |
| [[LoVo (line)]] | wt | 8.27 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0726× (z -17.1) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0490× (z -13.9) |
| [[HT-29 (line)]] | alt | 6.57 | 0 | 5 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0576× (z -15.7) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0980× (z -9.1) |
| [[PANC-1 (line)]] | alt | 5.16 | 0 | 5 (3 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0701× (z -13.7) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0784× (z -13.1) |
| [[A-172 (line)]] | wt | 7.83 | 0 | 3 (2 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.0294× (z -12.0) |
| [[HS-578T (line)]] | alt | 14.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0851× (z -11.5) |
| [[SW1417 (line)]] | alt | 4.14 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0686× (z -12.1) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SW48 (line)]] | wt | 9.73 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0396× (z -9.8) |
| [[LS 180 (line)]] | wt | 7.81 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -11.2) ⚠ cell-cycle shift, explains ~44% of this change |
| [[SW480 (line)]] | alt | 4.24 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.154× (z -11.7) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A498 (line)]] | wt | 5.95 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -9.5) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A549 (line)]] | wt | 2.38 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.104× (z -8.9) ⚠ cell-cycle shift, explains ~44% of this change |
| [[H4 (line)]] | wt | 9.27 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.0485× (z -9.3) |
| [[NCI-H1573 (line)]] | alt | 4.54 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0526× (z -9.7) |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0797× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[A-427 (line)]] | wt | 3.24 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.34 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.67 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.69 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.66 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.58 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 2.23 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.14 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.15 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.71 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.37 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.17 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.59 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.63 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.51 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.37 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.608 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.30 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.17 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12228), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PCK2]] | +0.81 | +0.74 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[MOCOS]] | +0.80 | +0.75 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_HEME_METABOLISM |
| [[MARS1]] | +0.79 | +0.82 / +0.83 | both halves | 7e-06 |  |
| [[YARS1]] | +0.79 | +0.78 / +0.77 | both halves | 7e-06 |  |
| [[NBR2]] | +0.78 | +0.70 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[AARS1]] | +0.77 | +0.78 / +0.80 | both halves | 7e-06 |  |
| [[CEBPG]] | +0.77 | +0.71 / +0.79 | both halves | 7e-06 | **novel candidate** |
| [[PSAT1]] | +0.77 | +0.79 / +0.78 | both halves | 7e-06 | STRING 431 |
| [[IARS1]] | +0.76 | +0.76 / +0.76 | both halves | 7e-06 |  |
| [[SLC1A4]] | +0.76 | +0.72 / +0.75 | both halves | 7e-06 | pathway: SLC-mediated transmembrane transport; STRING 590 |
| [[PHGDH]] | +0.75 | +0.81 / +0.77 | both halves | 7e-06 |  |
| [[CARS1]] | +0.74 | +0.72 / +0.82 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 3, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ULBP1]] | B | ULBP1 activity raises SLC6A9's level | lines that do not express ULBP1 (15) vs lines expressing it (35) | 1.46× lower at baseline in the lines without ULBP1 | 0.069 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[DMGDH]] | B | DMGDH activity raises SLC6A9's level | lines that do not express DMGDH (8) vs lines expressing it (42) | 1.61× lower at baseline in the lines without DMGDH | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[NIBAN1]] | B | NIBAN1 activity raises SLC6A9's level | lines that do not express NIBAN1 (11) vs lines expressing it (39) | 1.16× lower at baseline in the lines without NIBAN1 | 0.097 | ⚠ within organs, on part of the lines; also absent: CAV1, FGF2, PCOLCE2 |
| [[LINC00662]] | C | LINC00662 activity weakens SLC6A9's drug response | lines that do not express LINC00662 (3) vs lines expressing it (42) | the lines without LINC00662 respond 2.21× as strongly (z diff -3.66); strongest at Belinostat 5 µM: 0.08x vs 0.40x (z diff -6.3) | 0.002 | ⚠ few lines (3 vs 47); across organs; co-absent genes; also absent: NME4, ZFP14, ZNF221; target measured in part of the lines; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.868). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.5, 47.2); signed map (-13.4, 23.2). **Vector** length 94.5, 20.5% of its response variance represented; |z| ≥ 3 in 1,132 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +5.2 | +4.1 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.0 | +6.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.7 | +9.2 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +4.5 | +7.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +4.1 | +7.0 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +3.9 | +5.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.9 | +4.4 |
|  | [[Neratinib (drug)]] 5 µM |  | +3.4 | +4.9 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -5.2 | -9.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.4 | -8.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.2 | -5.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | -3.7 | -10.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -1.9 | -8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.8 | -3.8 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.6 | -1.4 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.5 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 6 member 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.1 — chr1:43,991,500-44,031,467 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GLYT1, GlyT-1 |
| Gene groups (HGNC) | Solute carrier family 6 |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 3 pathways, smallest: SLC-mediated transport of neurotransmitters; SLC-mediated transmembrane transport; Transport of small molecules |
| Matched by | ensembl_id |

**Function**, from UniProt [P48067](https://www.uniprot.org/uniprotkb/P48067) (Sodium- and chloride-dependent glycine transporter 1):

> Sodium- and chloride-dependent glycine transporter. Essential for regulating glycine concentrations at inhibitory glycinergic synapses.; [Isoform GlyT-1B]: Sodium- and chloride-dependent glycine transporter.; [Isoform GlyT-1C]: Sodium- and chloride-dependent glycine transporter.

**Summary**, from NCBI Gene [6536](https://www.ncbi.nlm.nih.gov/gene/6536):

> The amino acid glycine acts as an inhibitory neurotransmitter in the central nervous system. The protein encoded by this gene is one of two transporters that stop glycine signaling by removing it from the synaptic cleft. [provided by RefSeq, Jun 2016]

**Accessions** — [HGNC:11056](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11056) · Entrez [6536](https://www.ncbi.nlm.nih.gov/gene/6536) · UniProt [P48067](https://www.uniprot.org/uniprotkb/P48067) · Ensembl [ENSG00000196517](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196517)

## Data

Gene col 12228: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12228); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12228, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12228]; `tensor/DDL_lfc|DDL_z.npy` [12228]; `embed/gene_vectors.npy` [12228]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12228 or target_col == 12228). Every well: [[SLC6A9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC6A9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
