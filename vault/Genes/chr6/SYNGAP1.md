---
symbol: "SYNGAP1"
type: "gene"
col: 12374
ensembl_id: "ENSG00000197283"
name: "synaptic Ras GTPase activating protein 1"
location: "6p21.32"
module: 14
arm: "+"
pooled_cpm: 19.15
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 15
n_dd_up_clean: 5
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/014"]
generated_by: "tahoemap"
---

# SYNGAP1

*synaptic Ras GTPase activating protein 1* — 6p21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.72× (z +19.1, q 0e+00, up in 42 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 15 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.643× (z -6.0, q 1e-06, down in 28 of 48 measured lines) ⚠ cell-cycle shift, explains ~42% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 0.5 µM: 0.647× (z -5.9, q 1e-06, down in 31 of 48 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GNL1]] (+0.68, fdr 7e-06), [[TEF]] (+0.67, fdr 8e-06), [[SYNPO]] (+0.66, fdr 2e-05); moves opposite to [[TYW1]] (-0.60, fdr 2e-05), [[GIT2]] (-0.54, fdr 4e-05), [[SEC24B]] (-0.53, fdr 3e-05).
> It is in [[Module 014]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[BRSK1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 2 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12374.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.72×** | +19.1 | 0e+00 | 42/48 (SNU-423, A-172, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.16× | +6.9 | 2e-09 | 11/48 (HOP62, NCI-H23, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.59×** | +5.7 | 2e-06 | 24/48 (PANC-1, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.32×** | +3.8 | 0.024 | 21/48 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |
| [[Folic acid (drug)]] 5 µM |  | **1.21×** | +3.6 | 0.035 | 9/48 (CFPAC-1, HOP62, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.055 | 9/48 (NCI-H2347, HEC-1-A, …) | inconsistent across doses |  |
| [[GSK1059615 (drug)]] 5 µM |  | **1.59×** | +3.3 | 0.084 | 9/48 (PANC-1, A498, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 7 with an alert ⚠. 15 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12374.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.643×** | -6.0 | 1e-06 | 28/48 (SNU-423, hTERT-HPNE, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.647×** | -5.9 | 1e-06 | 31/48 (SK-MEL-2, Hs 766T, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.666×** | -5.5 | 7e-06 | 26/48 (HS-578T, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.672×** | -5.4 | 1e-05 | 26/47 (Panc 03.27, Hs 766T, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.689×** | -5.0 | 5e-05 | 21/48 (NCI-H1573, KATO III, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change | **0.693×** | -5.0 | 6e-05 | 23/46 (NCI-H2030, KATO III, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.701×** | -4.8 | 1e-04 | 19/48 (NCI-H1792, J82, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.807×** | -4.1 | 0.003 | 20/48 (CFPAC-1, J82, …) | all doses, stronger at high dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.720×** | -4.0 | 0.003 | 15/48 (CFPAC-1, NCI-H23, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | **0.742×** | -4.0 | 0.003 | 20/48 (HS-578T, hTERT-HPNE, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.761×** | -3.7 | 0.011 | 22/47 (CFPAC-1, H4, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.753×** | -3.6 | 0.014 | 16/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Doxycycline (monohydrate) (drug)]] 0.5 µM |  | **0.776×** | -3.4 | 0.026 | 15/47 (HS-578T, NCI-H1573, …) | inconsistent across doses |  |
| [[Peretinoin (drug)]] 5 µM |  | **0.767×** | -3.3 | 0.047 | 14/47 (hTERT-HPNE, NCI-H1792, …) | rises with dose | position effect removed |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.794×** | -3.1 | 0.068 | 14/47 (LoVo, A-427, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.30 per unit of S-phase module lfc, -0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12374. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 25.9 | 2 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.85× (z +21.2) | [[Belinostat (drug)]] 5 µM 0.205× (z -11.6) ⚠ cell-cycle shift, explains ~71% of this change |
| [[MIA PaCa-2 (line)]] | alt | 64.8 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 17.1× (z +27.2) | [[Panobinostat (drug)]] 5 µM 0.278× (z -8.7) ⚠ cell-cycle shift, explains ~53% of this change |
| [[NCI-H460 (line)]] | wt | 9.28 | 4 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 24.0× (z +27.5) | — |
| [[A-172 (line)]] | wt | 35.8 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.3× (z +28.3) | — |
| [[HOP62 (line)]] | alt | 20.2 | 3 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.5× (z +22.8) | — |
| [[hTERT-HPNE (line)]] | wt | 46.5 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 9.18× (z +19.3) | [[Panobinostat (drug)]] 0.5 µM 0.208× (z -9.8) ⚠ cell-cycle shift, explains ~42% of this change |
| [[NCI-H23 (line)]] | alt | 21.3 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.71× (z +9.1) | [[Auranofin (drug)]] 5 µM 0.202× (z -10.4) |
| [[PANC-1 (line)]] | alt | 29.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.09× (z +27.7) | — |
| [[SNU-423 (line)]] | alt | 38.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 22.9× (z +30.5) | [[Panobinostat (drug)]] 0.5 µM 0.189× (z -11.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[CFPAC-1 (line)]] | alt | 26.9 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.17× (z +11.6) | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.243× (z -10.1) |
| [[HepG2_C3A (line)]] | wt | 16.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.1× (z +19.0) | — |
| [[NCI-H2030 (line)]] | alt | 20.5 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.36× (z +11.5) | [[Digitoxin (drug)]] 5 µM 0.206× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[A-427 (line)]] | wt | 20.8 | 1 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 4.48× (z +10.1) | — |
| [[A498 (line)]] | wt | 8.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.07× (z +11.2) | — |
| [[AsPC-1 (line)]] | alt | 10.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.11× (z +14.2) | — |
| [[H4 (line)]] | wt | 21.0 | 0 | 1 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0927× (z -10.0) |
| [[HEC-1-A (line)]] | alt | 12.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HT-29 (line)]] | alt | 10.1 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0800× (z -11.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[J82 (line)]] | alt | 11.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.28× (z +14.3) | — |
| [[KATO III (line)]] | alt | 11.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.145× (z -10.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[LoVo (line)]] | wt | 15.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.261× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[LOX-IMVI (line)]] | wt | 18.8 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.74× (z +10.5) | — |
| [[NCI-H2347 (line)]] | alt | 8.46 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.27× (z +9.2) | — |
| [[RKO (line)]] | wt | 22.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.220× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[RPMI-7951 (line)]] | alt | 46.7 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.84× (z +9.6) | — |
| [[SHP-77 (line)]] | alt | 25.7 | 0 | 1 | — | [[Lenalidomide (hemihydrate) (drug)]] 0.5 µM 0.113× (z -13.0) |
| [[SK-MEL-2 (line)]] | alt | 11.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.9× (z +15.3) | — |
| [[SNU-1 (line)]] | wt | 14.2 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0927× (z -8.5) ⚠ cell-cycle shift, explains ~93% of this change |
| [[SW48 (line)]] | wt | 13.9 | 0 | 1 | — | [[Finasteride (drug)]] 0.05 µM 0.0712× (z -9.8) |
| [[A549 (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.60 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 22.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12374), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GNL1]] | +0.68 | +0.68 / +0.67 | both halves | 7e-06 |  |
| [[TEF]] | +0.67 | +0.71 / +0.58 | both halves | 8e-06 |  |
| [[SYNPO]] | +0.66 | +0.72 / +0.47 | both halves | 2e-05 |  |
| [[NOTCH2NLC]] | +0.65 | +0.63 / +0.49 | both halves | 1e-05 |  |
| [[PBX2]] | +0.65 | +0.72 / +0.48 | both halves | 2e-05 |  |
| [[PRR14]] | +0.63 | +0.75 / +0.48 | both halves | 2e-05 |  |
| [[MMRN2]] | +0.63 | +0.60 / +0.51 | both halves | 1e-05 |  |
| [[DXO]] | +0.62 | +0.64 / +0.43 | both halves | 3e-05 |  |
| [[RGL2]] | +0.62 | +0.69 / +0.37 | both halves | 7e-05 | pathway: MAPK family signaling cascades |
| [[CELSR3]] | +0.62 | +0.59 / +0.60 | both halves | 7e-06 | same gene group |
| [[ENO3]] | +0.61 | +0.63 / +0.45 | both halves | 3e-05 |  |
| [[NANOS3]] | +0.61 | +0.53 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TYW1]] | -0.60 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[GIT2]] | -0.54 | -0.54 / -0.42 | both halves | 4e-05 |  |
| [[SEC24B]] | -0.53 | -0.55 / -0.45 | both halves | 3e-05 | same gene group |
| [[RNF216]] | -0.52 | -0.55 / -0.35 | both halves | 1e-04 | same gene group |
| [[ATG5]] | -0.51 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[MRPL52]] | -0.51 | -0.58 / -0.32 | both halves | 2e-04 |  |
| [[INPP4A]] | -0.51 | -0.51 / -0.29 | both halves | 2e-04 |  |
| [[GPR89A]] | -0.51 | -0.53 / -0.40 | both halves | 5e-05 |  |
| [[SRPK2]] | -0.50 | -0.53 / -0.33 | both halves | 1e-04 |  |
| [[LYPLA1]] | -0.50 | -0.58 / -0.36 | both halves | 1e-04 | pathway: MAPK family signaling cascades |
| [[WRN]] | -0.50 | -0.52 / -0.32 | both halves | 2e-04 |  |
| [[NFATC3]] | -0.50 | -0.50 / -0.37 | both halves | 9e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[BRSK1]] | B | BRSK1 activity raises SYNGAP1's level | lines that do not express BRSK1 (13) vs lines expressing it (37) | 1.57× lower at baseline in the lines without BRSK1 | 0.044 | ⚠ within organs, on part of the lines; also absent: B4GALNT1, GIHCG, FSD1; maybe low, not absent |
| [[DLX2]] | B | DLX2 activity raises SYNGAP1's level | lines that do not express DLX2 (8) vs lines expressing it (42) | 1.58× lower at baseline in the lines without DLX2 | 0.046 | ⚠ within organs, on part of the lines; also absent: LINC01145-1, SCHIP1, NPHS1; maybe low, not absent |
| [[FMNL3]] | B | FMNL3 activity raises SYNGAP1's level | lines that do not express FMNL3 (8) vs lines expressing it (42) | 1.55× lower at baseline in the lines without FMNL3 | 0.058 | ⚠ within organs, on part of the lines; also absent: STARD9, CERCAM, ASAP3 |
| [[CCDC102A]] | B | CCDC102A activity raises SYNGAP1's level | lines that do not express CCDC102A (5) vs lines expressing it (45) | 1.64× lower at baseline in the lines without CCDC102A | 0.075 | ⚠ within organs, on part of the lines; also absent: CYP46A1, TMOD2, DPF1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 014]] — TNF-alpha signaling via NF-kB; 212 genes; every member is in the + arm (projection on the module's main direction 0.565). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.9, 5.2); signed map (28.5, 7.5). **Vector** length 93.8, 20.0% of its response variance represented; |z| ≥ 3 in 938 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +10.4 | +19.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | +7.1 | +5.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.6 | +2.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +4.3 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.0 | -0.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.1 | +3.4 |
|  | [[Entrectinib (drug)]] 5 µM |  | +1.7 | +1.7 |
|  | [[Posaconazole (drug)]] 5 µM |  | +1.4 | +1.9 |
|  | [[venetoclax (drug)]] 5 µM |  | +1.4 | +0.4 |
| fall | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -4.0 | -6.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -4.0 | -5.5 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~71% of this change | -3.7 | -4.0 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -2.7 | -5.4 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.7 | -3.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -5.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.3 | -4.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.2 | -4.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -3.3 |
|  | [[Bosentan (hydrate) (drug)]] 0.5 µM |  | -1.8 | -2.3 |

## What is on record

|  |  |
|---|---|
| Name | synaptic Ras GTPase activating protein 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.32 — chr6:33,419,661-33,453,689 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SYNGAP, RASA5, KIAA1938 |
| Gene groups (HGNC) | C2 and RasGAP domain containing; MicroRNA protein coding host genes |
| Reactome | 4 pathways, smallest: Regulation of RAS by GAPs; RAF/MAP kinase cascade; MAPK1/MAPK3 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96PV0](https://www.uniprot.org/uniprotkb/Q96PV0) (Ras/Rap GTPase-activating protein SynGAP):

> Major constituent of the PSD essential for postsynaptic signaling. Inhibitory regulator of the Ras-cAMP pathway. Member of the NMDAR signaling complex in excitatory synapses, it may play a role in NMDAR-dependent control of AMPAR potentiation, AMPAR membrane trafficking and synaptic plasticity. Regulates AMPAR-mediated miniature excitatory postsynaptic currents. Exhibits dual GTPase-activating specificity for Ras and Rap. May be involved in certain forms of brain injury, leading to long-term …

**Summary**, from NCBI Gene [8831](https://www.ncbi.nlm.nih.gov/gene/8831):

> This gene encodes a Ras GTPase activating protein that is a member of the N-methyl-D-aspartate receptor complex. The N-terminal domain of the protein contains a Ras-GAP domain, a pleckstrin homology domain, and a C2 domain that may be involved in binding of calcium and phospholipids. The C-terminal domain consists of a ten histidine repeat region, serine and tyrosine phosphorylation sites, and a T/SXV motif required for postsynaptic scaffold protein interaction. The encoded protein negatively …

**Accessions** — [HGNC:11497](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11497) · Entrez [8831](https://www.ncbi.nlm.nih.gov/gene/8831) · UniProt [Q96PV0](https://www.uniprot.org/uniprotkb/Q96PV0) · Ensembl [ENSG00000197283](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197283)

## Data

Gene col 12374: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12374); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12374, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12374]; `tensor/DDL_lfc|DDL_z.npy` [12374]; `embed/gene_vectors.npy` [12374]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12374 or target_col == 12374). Every well: [[SYNGAP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SYNGAP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
