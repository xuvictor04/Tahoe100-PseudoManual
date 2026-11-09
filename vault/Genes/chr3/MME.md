---
symbol: "MME"
type: "gene"
col: 12234
ensembl_id: "ENSG00000196549"
name: "membrane metalloendopeptidase"
location: "3q25.2"
module: 13
arm: "+"
pooled_cpm: 131.92
n_lines_expressing: 20
n_dd_up: 8
n_dd_down: 26
n_dd_up_clean: 4
n_dd_down_clean: 16
in_vector_space: true
direction_upstream: 25
direction_downstream: 45
tags: ["gene", "module/013"]
generated_by: "tahoemap"
---

# MME

*membrane metalloendopeptidase* — 3q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.52× (z +12.8, q 9e-35, up in 2 of 19 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Verteporfin (drug)]] 0.5 µM: 1.39× (z +4.6, q 7e-04, up in 0 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (10 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.533× (z -12.2, q 1e-31, down in 17 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MME-AS1]] (+0.65, fdr 7e-06, ⚠ same locus), [[WNT5A]] (+0.59, fdr 1e-05), [[APBB1IP]] (+0.55, fdr 1e-05), [[ADAMTS18]] (+0.54, fdr 2e-05); moves opposite to [[DLG3]] (-0.44, fdr 2e-04), [[PKP3]] (-0.43, fdr 4e-04), [[FAM83B]] (-0.41, fdr 5e-04).
> It is in [[Module 013]], a single-armed module (epithelial mesenchymal transition).
> Probable direction (from the cell lines, not proof of direct regulation): 25 arrows point to it, the strongest [[CRMP1]] → it (grade B ⚠); 45 go from it, the strongest it → [[MME-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12234.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.52×** | +12.8 | 9e-35 | 2/19 (CHP-212, LS 180) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.16×** | +10.3 | 2e-22 | 3/16 (CHP-212, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.60×** | +6.0 | 4e-07 | 0/16 | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Verteporfin (drug)]] 0.5 µM |  | **1.39×** | +4.6 | 7e-04 | 0/19 | all doses, flat | position effect removed |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.37×** | +4.3 | 0.002 | 0/18 | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.29×** | +3.5 | 0.041 | 1/18 (CHP-212) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.051 | 0/18 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | **1.26×** | +3.2 | 0.093 | 7/18 (RPMI-7951, J82, …) | top dose only | position effect removed |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +3.1 | 0.12 | 3/19 (SK-MEL-2, RPMI-7951, …) | top dose only |  |
| [[Selinexor (drug)]] 0.05 µM |  | 1.25× | +3.1 | 0.12 | 8/19 (HS-578T, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~9% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 11 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12234.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.533×** | -12.2 | 1e-31 | 17/18 (H4, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.447×** | -11.1 | 4e-26 | 16/18 (hTERT-HPNE, LOX-IMVI, …) | rises with dose | position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.555×** | -8.1 | 9e-14 | 14/18 (H4, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~48% of this change | **0.573×** | -7.7 | 3e-12 | 17/18 (LOX-IMVI, J82, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.565×** | -7.6 | 4e-12 | 17/18 (hTERT-HPNE, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.579×** | -7.5 | 5e-12 | 17/18 (LOX-IMVI, A-427, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.627×** | -6.4 | 1e-08 | 15/18 (hTERT-HPNE, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~43% of this change | **0.664×** | -5.4 | 5e-06 | 14/17 (LOX-IMVI, hTERT-HPNE, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **0.677×** | -5.4 | 5e-06 | 14/18 (LOX-IMVI, hTERT-HPNE, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.719×** | -4.5 | 3e-04 | 16/18 (hTERT-HPNE, LOX-IMVI, …) | top dose only |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.720×** | -4.5 | 3e-04 | 14/18 (J82, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~21% here); position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.710×** | -4.3 | 6e-04 | 4/18 (NCI-H23, SK-MEL-2, …) | inconsistent across doses |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.742×** | -4.1 | 0.002 | 14/19 (H4, LOX-IMVI, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **0.567×** | -4.1 | 0.002 | 9/19 (hTERT-HPNE, J82, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **0.821×** | -3.8 | 0.006 | 2/18 (NCI-H23, SK-MEL-2) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.598×** | -3.7 | 0.008 | 9/18 (SK-MEL-2, HS-578T, …) | top dose only | noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **0.767×** | -3.6 | 0.009 | 15/18 (SNU-423, SK-MEL-2, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.836× | -3.5 | 0.016 | 15/18 (J82, SNU-423, …) | rises with dose | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.782×** | -3.4 | 0.021 | 5/18 (SW480, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | **0.781×** | -3.2 | 0.031 | 4/17 (HS-578T, J82, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.638×** | -3.2 | 0.031 | 4/19 (NCI-H23, HOP62, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.47 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12234. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[hTERT-HPNE (line)]] | wt | 552 | 0 | 16 (11 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.132× (z -19.2) |
| [[LOX-IMVI (line)]] | wt | 1,132 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -19.7) |
| [[J82 (line)]] | alt | 263 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -17.2) |
| [[NCI-H23 (line)]] | alt | 292 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.260× (z -13.3) |
| [[RPMI-7951 (line)]] | alt | 435 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -18.7) |
| [[SNU-423 (line)]] | alt | 372 | 0 | 6 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.129× (z -15.4) ⚠ cell-cycle shift, explains ~48% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.335× (z -11.6) |
| [[H4 (line)]] | wt | 264 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0362× (z -25.4) |
| [[LS 180 (line)]] | wt | 118 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -15.4) |
| [[HOP62 (line)]] | alt | 225 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.158× (z -13.1) |
| [[SK-MEL-2 (line)]] | alt | 340 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -19.7) |
| [[A-427 (line)]] | wt | 1,635 | 0 | 3 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.202× (z -14.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[HS-578T (line)]] | alt | 39.2 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -12.2) |
| [[SW 1088 (line)]] | alt | 268 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0953× (z -13.8) |
| [[SW480 (line)]] | alt | 57.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.248× (z -11.7) |
| [[NCI-H1792 (line)]] | alt | 40.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.208× (z -13.3) |
| [[A-172 (line)]] | wt | 276 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.8 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 7.90 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 20.2 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 9.43 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 8.25 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 10.9 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 9.16 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 14.5 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 67.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.98 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 10.2 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 8.45 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 9.45 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 8.13 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 11.0 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 8.52 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 8.02 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.47 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 7.88 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.63 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 93.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.8 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 8.55 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 141 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.0 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 7.57 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 9.24 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 8.20 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 10.6 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 85.5 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 12.7 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 8.11 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 12.1 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12234), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MME-AS1]] | +0.65 | +0.65 / +0.60 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[WNT5A]] | +0.59 | +0.55 / +0.54 | both halves | 1e-05 | **novel candidate** |
| [[APBB1IP]] | +0.55 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[ADAMTS18]] | +0.54 | +0.54 / +0.48 | both halves | 2e-05 |  |
| [[THBS2]] | +0.53 | +0.53 / +0.48 | both halves | 2e-05 |  |
| [[DENND2A]] | +0.53 | +0.45 / +0.53 | both halves | 3e-05 |  |
| [[BCL11B]] | +0.52 | +0.58 / +0.46 | both halves | 3e-05 |  |
| [[TSHZ3]] | +0.52 | +0.52 / +0.46 | both halves | 3e-05 |  |
| [[ZNF521]] | +0.52 | +0.54 / +0.50 | both halves | 1e-05 |  |
| [[EVC2]] | +0.51 | +0.49 / +0.49 | both halves | 1e-05 |  |
| [[CNRIP1]] | +0.51 | +0.55 / +0.44 | both halves | 3e-05 |  |
| [[SLC43A3]] | +0.51 | +0.44 / +0.45 | both halves | 3e-05 |  |
| [[TNS1]] | +0.50 | +0.45 / +0.47 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DLG3]] | -0.44 | -0.31 / -0.44 | both halves | 2e-04 |  |
| [[PKP3]] | -0.43 | -0.48 / -0.25 | both halves | 4e-04 |  |
| [[FAM83B]] | -0.41 | -0.29 / -0.23 | both halves | 5e-04 |  |
| [[SEMA3B]] | -0.41 | -0.27 / -0.39 | both halves | 3e-04 |  |
| [[PATJ]] | -0.41 | -0.40 / -0.29 | both halves | 2e-04 |  |
| [[KRT14]] | -0.38 | -0.32 / -0.29 | both halves | 3e-04 | STRING 466 |
| [[TMC7]] | -0.38 | -0.24 / -0.35 | both halves | 5e-04 |  |
| [[DENND1B]] | -0.38 | -0.33 / -0.24 | both halves | 4e-04 |  |
| [[SLMAP]] | -0.37 | -0.36 / -0.36 | both halves | 1e-04 |  |
| [[GCLM]] | -0.37 | -0.41 / -0.29 | both halves | 3e-04 |  |
| [[TTC9]] | -0.37 | -0.29 / -0.36 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 1, C 24. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CRMP1]] | B | CRMP1 activity raises MME's level | lines that do not express CRMP1 (19) vs lines expressing it (31) | 3.68× lower at baseline in the lines without CRMP1 | 0.062 | ⚠ within organs, on part of the lines; also absent: JAM3, NHSL2, ENSG00000286033; maybe low, not absent |
| [[EVC2]] | C | EVC2 activity raises MME's level | lines that do not express EVC2 (34) vs lines expressing it (16) | 7.22× lower at baseline in the lines without EVC2 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000226043, LINC01242, ADGRG7; co-absent with the target |
| [[HS3ST3A1]] | C | HS3ST3A1 activity raises MME's level | lines that do not express HS3ST3A1 (33) vs lines expressing it (17) | 8.95× lower at baseline in the lines without HS3ST3A1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: ENSG00000224865, CDH13, COL19A1; co-absent with the target |
| [[NLRP3]] | C | NLRP3 activity raises MME's level | lines that do not express NLRP3 (28) vs lines expressing it (22) | 7.47× lower at baseline in the lines without NLRP3 | 0.009 | ⚠ within organs, on part of the lines; also absent: FLI1, APCDD1L, MME; co-absent with the target |
| [[LINC01615]] | C | LINC01615 activity raises MME's level | lines that do not express LINC01615 (36) vs lines expressing it (14) | 10.62× lower at baseline in the lines without LINC01615 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ENSG00000235749, ENSG00000222032, GYPC; co-absent with the target |
| [[FAM167A]] | C | FAM167A activity raises MME's level | lines that do not express FAM167A (17) vs lines expressing it (33) | 5.50× lower at baseline in the lines without FAM167A | 0.020 | ⚠ within organs, on part of the lines; also absent: ENSG00000255330, PREX1, SOGA3; maybe low, not absent; co-absent with the target |
| [[CDH13]] | C | CDH13 activity raises MME's level | lines that do not express CDH13 (35) vs lines expressing it (15) | 7.80× lower at baseline in the lines without CDH13 | 0.021 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MMP2, APCDD1L, ENSG00000222032; co-absent with the target |
| [[APCDD1L]] | C | APCDD1L activity raises MME's level | lines that do not express APCDD1L (34) vs lines expressing it (16) | 9.94× lower at baseline in the lines without APCDD1L | 0.026 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: MMP2, ENSG00000222032, PHACTR1; co-absent with the target |
| [[ADAMTS2]] | C | ADAMTS2 activity raises MME's level | lines that do not express ADAMTS2 (29) vs lines expressing it (21) | 6.12× lower at baseline in the lines without ADAMTS2 | 0.032 | ⚠ within organs, on part of the lines; co-occurs with KRAS; also absent: ZNF667, ZNF667-AS1, COL3A1; co-absent with the target |
| [[PRR16]] | C | PRR16 activity raises MME's level | lines that do not express PRR16 (24) vs lines expressing it (26) | 7.22× lower at baseline in the lines without PRR16 | 0.034 | ⚠ within organs, on part of the lines; also absent: PCDH10, LINC00839, ZEB2; co-absent with the target |
| [[MIR137HG]] | C | MIR137HG activity raises MME's level | lines that do not express MIR137HG (28) vs lines expressing it (22) | 5.45× lower at baseline in the lines without MIR137HG | 0.034 | ⚠ within organs, on part of the lines; also absent: EDNRA, CCBE1, ARMCX2; co-absent with the target |
| [[TRPC4]] | C | TRPC4 activity raises MME's level | lines that do not express TRPC4 (32) vs lines expressing it (18) | 5.86× lower at baseline in the lines without TRPC4 | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FMN2, LINC02211, FAM133A; co-absent with the target |

### Downstream of this gene

*45 arrows, 45 of them with an alert ⚠; grade A 0, B 10, C 35. Shown: the 12 strongest; 33 more arrows (33 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MME-AS1]] | B | MME activity raises MME-AS1's level | lines that do not express MME (30) vs lines expressing it (20) | 1.90× lower at baseline in the lines without MME | 3e-04 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC |
| [[ICAM5]] | B | MME activity raises ICAM5's level | lines that do not express MME (30) vs lines expressing it (20) | 2.32× lower at baseline in the lines without MME | 0.004 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC |
| [[PDE4DIPP2]] | B | MME activity raises PDE4DIPP2's level | lines that do not express MME (30) vs lines expressing it (20) | 2.91× lower at baseline in the lines without MME | 0.008 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC |
| [[ATP13A3]] | B | MME activity raises ATP13A3's level | lines that do not express MME (30) vs lines expressing it (20) | 1.79× lower at baseline in the lines without MME | 0.008 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC |
| [[CRMP1]] | B | MME activity raises CRMP1's level | lines that do not express MME (30) vs lines expressing it (20) | 2.43× lower at baseline in the lines without MME | 0.029 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC |
| [[BCL11B]] | B | MME activity strengthens BCL11B's drug response | lines that do not express MME (17) vs lines expressing it (13) | the lines without MME respond 0.74× as strongly (z diff +1.12); strongest at Ixazomib citrate 5 µM: 0.56x vs 0.27x (z diff +3.7) | 0.075 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC; target measured in part of the lines; artifact flags |
| [[AKT3]] | B | MME activity raises AKT3's level | lines that do not express MME (30) vs lines expressing it (20) | 4.34× lower at baseline in the lines without MME | 0.079 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC |
| [[C14orf132]] | B | MME activity raises C14orf132's level | lines that do not express MME (30) vs lines expressing it (20) | 3.44× lower at baseline in the lines without MME | 0.079 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC |
| [[SH3BP5]] | B | MME activity raises SH3BP5's level | lines that do not express MME (30) vs lines expressing it (20) | 2.40× lower at baseline in the lines without MME | 0.080 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC |
| [[ARL10]] | B | MME activity raises ARL10's level | lines that do not express MME (30) vs lines expressing it (20) | 1.75× lower at baseline in the lines without MME | 0.087 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC |
| [[CAMK4]] | C | MME activity raises CAMK4's level | lines that do not express MME (30) vs lines expressing it (20) | 6.67× lower at baseline in the lines without MME | 0.001 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC; co-absent with the target |
| [[CDH13]] | C | MME activity raises CDH13's level | lines that do not express MME (30) vs lines expressing it (20) | 7.56× lower at baseline in the lines without MME | 0.002 | ⚠ within organs, on part of the lines; also absent: APCDD1L, PHACTR1, GYPC; co-absent with the target |

## Where it sits

- **Module**: [[Module 013]] — epithelial mesenchymal transition; 213 genes; every member is in the + arm (projection on the module's main direction 0.474). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (51.3, 19.9); signed map (27.0, 47.6). **Vector** length 90.9, 34.2% of its response variance represented; |z| ≥ 3 in 697 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.5 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.1 | +12.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.7 | +6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.9 | +0.1 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | +3.4 | -1.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.2 | -3.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.0 | +0.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +2.4 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +3.4 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.2 | +4.3 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -2.1 | -4.5 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | -0.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.8 | -1.1 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~6% of this change | -1.8 | -2.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.7 | -4.3 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.6 | -3.2 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -1.6 | -1.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | membrane metalloendopeptidase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.2 — chr3:155,024,124-155,183,704 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CALLA, CD10, NEP |
| Gene groups (HGNC) | CD molecules; M13 metallopeptidases; Elastases |
| Reactome | 7 pathways, smallest: Metabolism of Angiotensinogen to Angiotensins; Physiological factors; Peptide hormone metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [P08473](https://www.uniprot.org/uniprotkb/P08473) (Neprilysin):

> Thermolysin-like specificity, but is almost confined on acting on polypeptides of up to 30 amino acids. Biologically important in the destruction of opioid peptides such as Met- and Leu-enkephalins by cleavage of a Gly-Phe bond. Catalyzes cleavage of bradykinin, substance P and neurotensin peptides. Able to cleave angiotensin-1, angiotensin-2 and angiotensin 1-9. Involved in the degradation of atrial natriuretic factor (ANF) and brain natriuretic factor (BNP(1-32)). Displays UV-inducible …

**Summary**, from NCBI Gene [4311](https://www.ncbi.nlm.nih.gov/gene/4311):

> The protein encoded by this gene is a type II transmembrane glycoprotein and a common acute lymphocytic leukemia antigen that is an important cell surface marker in the diagnosis of human acute lymphocytic leukemia (ALL). The encoded protein is present on leukemic cells of pre-B phenotype, which represent 85% of cases of ALL. This protein is not restricted to leukemic cells, however, and is found on a variety of normal tissues. The protein is a neutral endopeptidase that cleaves peptides at the …

**Accessions** — [HGNC:7154](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7154) · Entrez [4311](https://www.ncbi.nlm.nih.gov/gene/4311) · UniProt [P08473](https://www.uniprot.org/uniprotkb/P08473) · Ensembl [ENSG00000196549](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196549)

## Data

Gene col 12234: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12234); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12234, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12234]; `tensor/DDL_lfc|DDL_z.npy` [12234]; `embed/gene_vectors.npy` [12234]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12234 or target_col == 12234). Every well: [[MME — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MME.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
