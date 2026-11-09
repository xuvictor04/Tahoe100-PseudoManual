---
symbol: "DMGDH"
type: "gene"
col: 5381
ensembl_id: "ENSG00000132837"
name: "dimethylglycine dehydrogenase"
location: "5q14.1"
module: 133
arm: "+"
pooled_cpm: 19.22
n_lines_expressing: 42
n_dd_up: 52
n_dd_down: 16
n_dd_up_clean: 48
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 2
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# DMGDH

*dimethylglycine dehydrogenase* — 5q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 52 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.87× (z +16.4, q 0e+00, up in 36 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 16 drug-doses (9 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.369× (z -8.6, q 5e-15, down in 34 of 40 measured lines) ⚠ cell-cycle shift, explains ~41% of this change. The strongest without an alert is [[PH-797804 (drug)]] 5 µM: 0.346× (z -4.8, q 2e-04, down in 23 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NBR2]] (+0.78, fdr 7e-06), [[PCK2]] (+0.77, fdr 7e-06), [[EIF2S2]] (+0.74, fdr 7e-06).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 2 go from it, the strongest it → [[SESN2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 52 in all, 4 with an alert ⚠; shown: the 15 strongest. 52 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5381.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.87×** | +16.4 | 0e+00 | 36/37 (HOP62, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **3.47×** | +10.7 | 3e-24 | 35/40 (LS 180, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **3.32×** | +10.3 | 1e-22 | 34/39 (A-172, SHP-77, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM |  | **2.23×** | +9.7 | 3e-20 | 34/40 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.70×** | +8.2 | 2e-14 | 28/37 (HOP62, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **2.43×** | +7.6 | 2e-12 | 33/39 (HEC-1-A, NCI-H460, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **2.32×** | +7.2 | 5e-11 | 27/37 (BT-474, H4, …) | two highest doses | cell-cycle shift (explains ~20% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.36×** | +7.1 | 1e-10 | 25/38 (CFPAC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.65×** | +6.1 | 7e-08 | 27/40 (BT-474, SW480, …) | two highest doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.02×** | +6.0 | 1e-07 | 23/39 (NCI-H2347, J82, …) | rises with dose | cell-cycle shift (explains ~23% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **2.00×** | +6.0 | 1e-07 | 28/40 (HEC-1-A, SW480, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.97×** | +5.8 | 3e-07 | 24/39 (HEC-1-A, RKO, …) | all doses, stronger at high dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.58×** | +5.6 | 1e-06 | 24/40 (MIA PaCa-2, A-172, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.82×** | +5.1 | 1e-05 | 25/39 (BT-474, C-33 A, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.84×** | +5.0 | 2e-05 | 21/37 (SW480, A498, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 9 with an alert ⚠. 16 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5381.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.369×** | -8.6 | 5e-15 | 34/40 (SW480, LoVo, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.369×** | -8.1 | 1e-13 | 27/39 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.427×** | -7.3 | 4e-11 | 27/36 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.346×** | -4.8 | 2e-04 | 23/34 (HCT15, A-427, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.578×** | -4.7 | 2e-04 | 22/38 (PANC-1, SW480, …) | all doses, flat |  |
| [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **0.364×** | -4.6 | 4e-04 | 22/38 (HT-29, PANC-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.578×** | -4.5 | 4e-04 | 23/38 (PANC-1, SW480, …) | all doses, flat | composition shift |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.707×** | -4.2 | 0.002 | 14/40 (HEC-1-A, A-427, …) | all doses, flat | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.599×** | -4.2 | 0.002 | 21/39 (SW480, PANC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.650×** | -3.7 | 0.011 | 16/38 (PANC-1, HepG2/C3A, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.635×** | -3.6 | 0.015 | 18/35 (H4, LoVo, …) | all doses, flat | low cells (technical?) |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.671×** | -3.5 | 0.026 | 14/40 (A-427, HT-29, …) | all doses, flat | position effect removed |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | **0.678×** | -3.4 | 0.031 | 9/40 (PANC-1, SHP-77, …) | all doses, flat | position effect removed |
| [[EX229 (drug)]] 5 µM |  | **0.475×** | -3.4 | 0.031 | 15/34 (BT-474, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.694×** | -3.2 | 0.058 | 17/40 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **0.507×** | -3.1 | 0.078 | 14/35 (HCT15, HT-29, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.74 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5381. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 28.2 | 0 | 13 (12 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.100× (z -19.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.180× (z -10.3) |
| [[LoVo (line)]] | wt | 83.7 | 0 | 10 (8 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0553× (z -16.6) ⚠ toxic; transcription drop · without an alert: [[Belinostat (drug)]] 5 µM 0.224× (z -9.0) |
| [[HT-29 (line)]] | alt | 68.2 | 0 | 9 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0767× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SW480 (line)]] | alt | 46.6 | 1 | 8 (8 ⚠) | [[Artesunate (drug)]] 5 µM 3.83× (z +11.4) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0633× (z -15.9) ⚠ cell-cycle shift, explains ~53% of this change |
| [[A-427 (line)]] | wt | 16.2 | 0 | 3 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0863× (z -11.5) ⚠ toxic; cell-cycle shift, would explain all of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.103× (z -10.7) |
| [[HOP62 (line)]] | alt | 4.88 | 2 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +12.5) | [[Bosentan (hydrate) (drug)]] 5 µM 0.0822× (z -8.5) |
| [[A-172 (line)]] | wt | 9.26 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.84× (z +11.2) | — |
| [[HCT15 (line)]] | alt | 38.2 | 1 | 1 (1 ⚠) | [[Artesunate (drug)]] 5 µM 5.54× (z +9.4) | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -8.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 24.4 | 2 | 0 | [[Artesunate (drug)]] 5 µM 5.48× (z +10.7) | — |
| [[LS 180 (line)]] | wt | 28.1 | 1 | 1 (1 ⚠) | [[Artesunate (drug)]] 5 µM 4.45× (z +9.3) | [[Digitoxin (drug)]] 5 µM 0.139× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change |
| [[SW48 (line)]] | wt | 31.7 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0319× (z -11.8) ⚠ cell-cycle shift, explains ~28% of this change |
| [[A498 (line)]] | wt | 31.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -12.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 33.9 | 1 | 0 | [[Afatinib (drug)]] 5 µM 5.88× (z +9.2) | — |
| [[CFPAC-1 (line)]] | alt | 7.75 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.7× (z +12.1) | — |
| [[COLO 205 (line)]] | alt | 31.0 | 1 | 0 | [[Artesunate (drug)]] 5 µM 8.63× (z +10.9) | — |
| [[H4 (line)]] | wt | 21.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0317× (z -10.6) ⚠ cell-cycle shift, explains ~28% of this change |
| [[HS-578T (line)]] | alt | 10.5 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.04× (z +9.3) | — |
| [[J82 (line)]] | alt | 9.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.10× (z +9.6) | — |
| [[MIA PaCa-2 (line)]] | alt | 13.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.69× (z +10.2) | — |
| [[NCI-H23 (line)]] | alt | 16.3 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[NCI-H460 (line)]] | wt | 5.02 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.57× (z +9.9) | — |
| [[SHP-77 (line)]] | alt | 19.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 4.80× (z +8.5) | — |
| [[SNU-423 (line)]] | alt | 9.24 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.59× (z +11.3) | — |
| [[A549 (line)]] | wt | 3.63 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.49 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 4.70 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 5.58 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.05 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.06 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 4.16 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 6.25 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.40 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.98 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.54 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 5.46 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.76 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5381), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBR2]] | +0.78 | +0.77 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[PCK2]] | +0.77 | +0.74 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[EIF2S2]] | +0.74 | +0.69 / +0.78 | both halves | 7e-06 | **novel candidate** |
| [[SLC6A9]] | +0.73 | +0.61 / +0.72 | both halves | 7e-06 |  |
| [[YARS1]] | +0.73 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[VLDLR-AS1]] | +0.72 | +0.61 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[CEBPG]] | +0.72 | +0.61 / +0.75 | both halves | 7e-06 |  |
| [[AARS1]] | +0.69 | +0.61 / +0.81 | both halves | 7e-06 |  |
| [[NIBAN1]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[MIA2]] | +0.68 | +0.54 / +0.70 | both halves | 1e-05 | **novel candidate** |
| [[MOCOS]] | +0.68 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[GARS1]] | +0.68 | +0.53 / +0.85 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DMGDH's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 8.7% of all compounds | 0.015 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[NUPR1]] | B | NUPR1 activity raises DMGDH's level | lines that do not express NUPR1 (24) vs lines expressing it (26) | 1.19× lower at baseline in the lines without NUPR1 | 0.087 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: TTTY14, SPARC, PCDH18 |
| [[ASNSP1]] | B | ASNSP1 activity raises DMGDH's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.36× lower at baseline in the lines without ASNSP1 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SESN2]] | B | DMGDH activity raises SESN2's level | lines that do not express DMGDH (8) vs lines expressing it (42) | 1.68× lower at baseline in the lines without DMGDH | 0.073 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[SLC6A9]] | B | DMGDH activity raises SLC6A9's level | lines that do not express DMGDH (8) vs lines expressing it (42) | 1.61× lower at baseline in the lines without DMGDH | 0.081 | ⚠ within organs, on part of the lines; maybe low, not absent |

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.860). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-16.0, 47.4); signed map (-12.8, 23.0). **Vector** length 117, 34.2% of its response variance represented; |z| ≥ 3 in 1,301 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.5 | +10.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.7 | +10.7 |
|  | [[Artesunate (drug)]] 5 µM |  | +6.4 | +9.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +6.3 | +7.6 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +6.2 | +6.1 |
|  | [[Neratinib (drug)]] 5 µM |  | +4.7 | +5.1 |
| fall | [[Belinostat (drug)]] 5 µM |  | -4.1 | +3.1 |
|  | [[Panobinostat (drug)]] 5 µM |  | -3.9 | +3.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -3.9 | +2.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | -3.0 | -4.5 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.7 | +0.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.3 | -4.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.2 | -3.6 |
|  | [[Methotrexate (drug)]] 5 µM |  | -2.1 | -2.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.0 | -3.5 |
|  | [[Flutamide (drug)]] 5 µM |  | -1.7 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | dimethylglycine dehydrogenase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q14.1 — chr5:78,997,564-79,236,038 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ME2GLYDH |
| Gene groups (HGNC) | Flavoproteins; Oxidoreductases |
| Reactome | 2 pathways, smallest: Choline catabolism; Metabolism of amino acids and derivatives |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UI17](https://www.uniprot.org/uniprotkb/Q9UI17) (Dimethylglycine dehydrogenase, mitochondrial):

> Catalyzes the demethylation of N,N-dimethylglycine to sarcosine. Also has activity with sarcosine in vitro.

**Summary**, from NCBI Gene [29958](https://www.ncbi.nlm.nih.gov/gene/29958):

> This gene encodes an enzyme involved in the catabolism of choline, catalyzing the oxidative demethylation of dimethylglycine to form sarcosine. The enzyme is found as a monomer in the mitochondrial matrix, and uses flavin adenine dinucleotide and folate as cofactors. Mutation in this gene causes dimethylglycine dehydrogenase deficiency, characterized by a fishlike body odor, chronic muscle fatigue, and elevated levels of the muscle form of creatine kinase in serum. Alternative splicing results …

**Accessions** — [HGNC:24475](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24475) · Entrez [29958](https://www.ncbi.nlm.nih.gov/gene/29958) · UniProt [Q9UI17](https://www.uniprot.org/uniprotkb/Q9UI17) · Ensembl [ENSG00000132837](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000132837)

## Data

Gene col 5381: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5381); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5381, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5381]; `tensor/DDL_lfc|DDL_z.npy` [5381]; `embed/gene_vectors.npy` [5381]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5381 or target_col == 5381). Every well: [[DMGDH — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DMGDH.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
