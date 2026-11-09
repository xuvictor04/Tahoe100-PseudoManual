---
symbol: "CNP"
type: "gene"
col: 10426
ensembl_id: "ENSG00000173786"
name: "2',3'-cyclic nucleotide 3' phosphodiesterase"
location: "17q21.2"
module: 32
arm: "+"
pooled_cpm: 29.59
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 17
n_dd_up_clean: 16
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# CNP

*2',3'-cyclic nucleotide 3' phosphodiesterase* — 17q21.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (8 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.58× (z +5.8, q 5e-06, up in 23 of 37 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.26× (z +4.3, q 0.002, up in 23 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (2 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 0.05 µM: 0.647× (z -5.4, q 3e-05, down in 29 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ADAR]] (+0.77, fdr 7e-06), [[OAS3]] (+0.76, fdr 7e-06), [[OAS2]] (+0.76, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[IFI30]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10426.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | **1.58×** | +5.8 | 5e-06 | 23/37 (J82, HEC-1-A, …) | rises with dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | **1.52×** | +5.5 | 1e-05 | 23/44 (J82, HEC-1-A, …) | rises with dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +4.9 | 2e-04 | 25/46 (KATO III, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.43×** | +4.7 | 5e-04 | 27/48 (HEC-1-A, SW480, …) | two highest doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.43×** | +4.5 | 6e-04 | 27/46 (HT-29, SW480, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.26×** | +4.3 | 0.002 | 23/48 (Panc 03.27, CFPAC-1, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.56×** | +4.2 | 0.003 | 27/45 (A498, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.36×** | +4.1 | 0.003 | 21/47 (CFPAC-1, SW480, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.24×** | +4.0 | 0.005 | 20/48 (KATO III, HEC-1-A, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.33×** | +3.7 | 0.012 | 17/48 (SK-MEL-2, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.32×** | +3.7 | 0.013 | 17/48 (A498, CFPAC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.22×** | +3.6 | 0.013 | 16/48 (HEC-1-A, CFPAC-1, …) | top dose only |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.47×** | +3.6 | 0.014 | 19/47 (A498, PANC-1, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.29×** | +3.3 | 0.031 | 18/47 (SK-MEL-2, NCI-H1792, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.31×** | +3.3 | 0.031 | 18/48 (SK-MEL-2, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.044 | 16/48 (MIA PaCa-2, Panc 03.27, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +3.2 | 0.044 | 22/48 (NCI-H2347, HS-578T, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[DT-061 (drug)]] 5 µM |  | **1.59×** | +3.2 | 0.044 | 11/45 (MIA PaCa-2, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.049 | 21/47 (AsPC-1, SK-MEL-2, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.28×** | +3.1 | 0.059 | 17/47 (NCI-H23, SK-MEL-2, …) | rises with dose |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.22×** | +3.1 | 0.060 | 14/48 (SK-MEL-2, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[AZD-7648 (drug)]] 5 µM |  | **1.54×** | +3.0 | 0.077 | 11/45 (A549, C32, …) | rises with dose | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 2 with an alert ⚠. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10426.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 0.05 µM |  | **0.647×** | -5.4 | 3e-05 | 29/48 (A498, A-172, …) | all doses, flat | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.685×** | -5.0 | 2e-04 | 27/47 (A498, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | **0.780×** | -4.7 | 6e-04 | 25/48 (A-172, A549, …) | rises with dose | position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **0.723×** | -4.3 | 0.003 | 25/47 (NCI-H23, A498, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.564×** | -3.9 | 0.009 | 21/45 (RKO, SNU-423, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.813×** | -3.9 | 0.011 | 20/48 (SK-MEL-2, A-172, …) | rises with dose | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.817×** | -3.8 | 0.013 | 24/48 (COLO 205, A549, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.824×** | -3.6 | 0.020 | 19/48 (SK-MEL-2, LoVo, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.765×** | -3.5 | 0.026 | 20/46 (A549, NCI-H1573, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.772×** | -3.4 | 0.036 | 12/47 (SNU-423, SW1417, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.617×** | -3.3 | 0.044 | 18/48 (A498, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.779×** | -3.3 | 0.044 | 18/47 (A549, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.772×** | -3.3 | 0.044 | 20/47 (HepG2/C3A, SW 900, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.781×** | -3.3 | 0.044 | 20/47 (NCI-H23, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.782×** | -3.2 | 0.044 | 18/47 (NCI-H2030, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.794×** | -3.0 | 0.083 | 16/48 (KATO III, HepG2/C3A, …) | rises with dose | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.796×** | -3.0 | 0.084 | 19/48 (A549, NCI-H1792, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10426. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[J82 (line)]] | alt | 28.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~57% of this change | — |
| [[KATO III (line)]] | alt | 43.3 | 1 (1 ⚠) | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.10× (z +8.7) ⚠ cell-cycle shift, explains ~37% of this change | [[Dinaciclib (drug)]] 0.05 µM 0.242× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[A-427 (line)]] | wt | 28.1 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.263× (z -14.0) ⚠ cell-cycle shift, explains ~93% of this change |
| [[A549 (line)]] | wt | 43.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.250× (z -10.0) ⚠ toxic; transcription drop |
| [[H4 (line)]] | wt | 16.4 | 0 | 1 | — | [[Temsirolimus (drug)]] 0.5 µM 0.106× (z -9.6) |
| [[HEC-1-A (line)]] | alt | 29.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.99× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change | — |
| [[LoVo (line)]] | wt | 19.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.289× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~48% of this change |
| [[NCI-H23 (line)]] | alt | 34.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.200× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[SNU-423 (line)]] | alt | 28.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.360× (z -9.8) ⚠ cell-cycle shift, explains ~93% of this change |
| [[A-172 (line)]] | wt | 66.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 77.9 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 49.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 30.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 40.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 30.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 24.7 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 16.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 25.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 24.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 18.5 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 39.3 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 48.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 34.5 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 30.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 50.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 34.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 21.2 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 21.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10426), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ADAR]] | +0.77 | +0.71 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[OAS3]] | +0.76 | +0.74 / +0.75 | both halves | 7e-06 |  |
| [[OAS2]] | +0.76 | +0.71 / +0.75 | both halves | 7e-06 |  |
| [[IFI35]] | +0.75 | +0.71 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFIT1]] | +0.75 | +0.70 / +0.75 | both halves | 7e-06 |  |
| [[PARP9]] | +0.73 | +0.69 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[MX1]] | +0.73 | +0.69 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[OAS1]] | +0.73 | +0.69 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[TAP1]] | +0.72 | +0.69 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[CMPK2]] | +0.72 | +0.66 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[XAF1]] | +0.72 | +0.67 / +0.73 | both halves | 7e-06 |  |
| [[STAT1]] | +0.71 | +0.73 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFI30]] | B | IFI30 activity raises CNP's level | lines that do not express IFI30 (5) vs lines expressing it (45) | 1.20× lower at baseline in the lines without IFI30 | 0.089 | ⚠ within organs, on part of the lines; also absent: RAP1GAP2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.752). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.5, 54.6); signed map (64.8, 32.6). **Vector** length 104, 26.6% of its response variance represented; |z| ≥ 3 in 871 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.64 to 60); *interferon* (control, mean cos +0.70 to 23); *Interferon Signaling* (reactome, mean cos +0.65 to 45).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +3.7 | +3.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~31% of this change | +3.7 | +4.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | +3.7 | +2.3 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +3.2 | +4.9 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | +2.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.7 | +3.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.6 | +3.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +2.6 | +4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.5 | +3.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.5 | +2.3 |
| fall | [[Auranofin (drug)]] 5 µM |  | -5.5 | -4.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -5.2 | -3.6 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -4.7 | -4.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | -4.5 | -3.4 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.3 | -3.8 |
|  | [[Verteporfin (drug)]] 5 µM |  | -4.1 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | 2',3'-cyclic nucleotide 3' phosphodiesterase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.2 — chr17:41,966,763-41,977,740 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CN37 |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, UV_RESPONSE_UP |
| Matched by | ensembl_id |

**Function**, from UniProt [P09543](https://www.uniprot.org/uniprotkb/P09543) (Myelin protein CNP):

> [Myelin protein CNP]: Non-compacted myelin sheath-associated protein that is involved in oligodendrocytes differentiation and myelin maintenance. Myelin is formed by oligodendrocytes that spirally wrap their plasma membrane around axons providing insulation but also metabolic support from the oligodendrocyte to the underlying neuron. Displays molecular condensate scaffold activity and promotes microtubule assembly. Binds tubulin heterodimers and co-polymerizes with tubulin, thereby supporting …

**Summary**, from NCBI Gene [1267](https://www.ncbi.nlm.nih.gov/gene/1267):

> Predicted to enable 2',3'-cyclic-nucleotide 3'-phosphodiesterase activity. Involved in substantia nigra development. Located in cytoplasm; microtubule; and obsolete extracellular space. Implicated in hypomyelinating leukodystrophy 20; multiple sclerosis; and schizophrenia. Biomarker of alcoholic liver cirrhosis; multiple sclerosis; and restless legs syndrome. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:2158](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2158) · Entrez [1267](https://www.ncbi.nlm.nih.gov/gene/1267) · UniProt [P09543](https://www.uniprot.org/uniprotkb/P09543) · Ensembl [ENSG00000173786](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000173786)

## Data

Gene col 10426: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10426); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10426, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10426]; `tensor/DDL_lfc|DDL_z.npy` [10426]; `embed/gene_vectors.npy` [10426]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10426 or target_col == 10426). Every well: [[CNP — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CNP.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
