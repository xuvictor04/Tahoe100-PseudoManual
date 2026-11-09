---
symbol: "WDR45B"
type: "gene"
col: 6554
ensembl_id: "ENSG00000141580"
name: "WD repeat domain 45B"
location: "17q25.3"
module: 164
arm: "+"
pooled_cpm: 230.0
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 23
n_dd_up_clean: 4
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/164"]
generated_by: "tahoemap"
---

# WDR45B

*WD repeat domain 45B* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (4 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 3.36× (z +7.3, q 2e-10, up in 46 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (8 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.587× (z -6.1, q 4e-07, down in 41 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[INSIG2]] (+0.85, fdr 7e-06), [[ANKRD37]] (+0.79, fdr 7e-06), [[FAM162A]] (+0.79, fdr 7e-06); moves opposite to [[CPLANE1]] (-0.65, fdr 7e-06), [[AVEN]] (-0.61, fdr 3e-05), [[PARVA]] (-0.61, fdr 3e-05).
> It is in [[Module 164]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[GPR160]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6554.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **3.36×** | +7.3 | 2e-10 | 46/49 (COLO 205, LoVo, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.78×** | +6.1 | 2e-07 | 41/48 (HEC-1-A, LoVo, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.59×** | +5.3 | 2e-05 | 35/48 (LoVo, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.50×** | +4.6 | 6e-04 | 36/48 (LoVo, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Fumaric acid (drug)]] 5 µM |  | **1.41×** | +3.8 | 0.017 | 42/49 (SHP-77, AsPC-1, …) | top dose only | plate-row cell shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **1.36×** | +3.6 | 0.036 | 31/48 (LoVo, PANC-1, …) | rises with dose |  |
| [[Pravastatin (sodium) (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.056 | 38/48 (KATO III, HepG2/C3A, …) | top dose only | plate-row cell shift |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.34×** | +3.4 | 0.056 | 30/48 (SW480, NCI-H460, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.68× | +3.1 | 0.12 | 30/48 (SHP-77, CHP-212, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | 1.66× | +3.0 | 0.13 | 34/48 (MIA PaCa-2, H4, …) | rises with dose | noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 1.30× | +3.0 | 0.13 | 27/48 (LoVo, PANC-1, …) | all doses, stronger at high dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 8 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6554.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.587×** | -6.1 | 4e-07 | 41/48 (CFPAC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.690×** | -6.0 | 4e-07 | 29/48 (COLO 205, C32, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.589×** | -5.9 | 8e-07 | 39/48 (NCI-H1573, COLO 205, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.600×** | -5.7 | 2e-06 | 30/44 (NCI-H1573, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.737×** | -5.0 | 7e-05 | 40/48 (CFPAC-1, AN3 CA, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **0.738×** | -5.0 | 7e-05 | 38/48 (NCI-H2347, C32, …) | rises with dose | low cells (technical?) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.657×** | -4.8 | 1e-04 | 35/49 (CFPAC-1, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **0.651×** | -4.8 | 1e-04 | 35/47 (CFPAC-1, KATO III, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.666×** | -4.7 | 2e-04 | 36/48 (CFPAC-1, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.660×** | -4.4 | 5e-04 | 35/45 (A-427, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.688×** | -4.3 | 8e-04 | 39/48 (CFPAC-1, LS 180, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.699×** | -4.1 | 0.002 | 39/48 (HOP62, SW 1271, …) | all doses, flat |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.695×** | -4.0 | 0.002 | 34/47 (C-33 A, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.721×** | -3.8 | 0.006 | 31/48 (CFPAC-1, KATO III, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.746×** | -3.4 | 0.026 | 30/47 (NCI-H23, NCI-H2347, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.749×** | -3.3 | 0.030 | 33/49 (NCI-H661, NCI-H1573, …) | inconsistent across doses |  |
| [[Rapamycin (drug)]] 5 µM |  | **0.826×** | -3.1 | 0.057 | 21/48 (HepG2/C3A, J82, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.759×** | -3.1 | 0.069 | 26/48 (SNU-1, NCI-H1573, …) | top dose only |  |
| [[Brimonidine (drug)]] 5 µM |  | **0.776×** | -2.9 | 0.093 | 28/48 (NCI-H1573, RKO, …) | top dose only |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.617×** | -2.9 | 0.096 | 25/50 (HEC-1-A, NCI-H23, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Benztropine (mesylate) (drug)]] 0.05 µM |  | **0.779×** | -2.9 | 0.097 | 30/48 (HT-29, BT-474, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.779×** | -2.9 | 0.097 | 25/48 (LOX-IMVI, SW48, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, +0.38 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6554. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CFPAC-1 (line)]] | alt | 364 | 0 | 8 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.311× (z -12.5) |
| [[KATO III (line)]] | alt | 423 | 0 | 7 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.492× (z -11.9) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.387× (z -11.2) |
| [[LoVo (line)]] | wt | 110 | 4 (3 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.75× (z +15.3) ⚠ toxic; transcription drop · without an alert: [[TAK-901 (drug)]] 5 µM 5.08× (z +9.8) | — |
| [[NCI-H1573 (line)]] | alt | 304 | 0 | 4 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.174× (z -12.9) |
| [[AsPC-1 (line)]] | alt | 156 | 0 | 3 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.417× (z -9.8) |
| [[C-33 A (line)]] | alt | 286 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.210× (z -11.4) ⚠ toxic · without an alert: [[Harringtonine (drug)]] 5 µM 0.246× (z -10.2) |
| [[C32 (line)]] | wt | 391 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.355× (z -11.5) |
| [[CHP-212 (line)]] | wt | 521 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -11.2) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 296 | 1 | 2 | [[TAK-901 (drug)]] 5 µM 7.38× (z +10.8) | [[Homoharringtonine (drug)]] 5 µM 0.368× (z -14.7) |
| [[HT-29 (line)]] | alt | 264 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.516× (z -10.9) |
| [[LS 180 (line)]] | wt | 321 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.467× (z -9.8) |
| [[NCI-H1792 (line)]] | alt | 265 | 2 (2 ⚠) | 1 (1 ⚠) | [[Digitoxin (drug)]] 5 µM 3.57× (z +10.3) ⚠ toxic; transcription drop | [[Dinaciclib (drug)]] 5 µM 0.332× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 165 | 0 | 2 | — | [[Harringtonine (drug)]] 5 µM 0.318× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 360 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -10.1) |
| [[PANC-1 (line)]] | alt | 235 | 2 (2 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.22× (z +10.0) ⚠ cell-cycle shift, explains ~30% of this change | — |
| [[A-427 (line)]] | wt | 203 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.334× (z -11.6) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 218 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -8.5) |
| [[BT-474 (line)]] | alt | 195 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.382× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H23 (line)]] | alt | 203 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 5.70× (z +9.0) | — |
| [[SK-MEL-2 (line)]] | alt | 274 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.478× (z -10.3) |
| [[SNU-1 (line)]] | wt | 223 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.22× (z +8.6) | — |
| [[SW480 (line)]] | alt | 159 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.05 µM 2.23× (z +8.6) ⚠ cell-cycle shift, explains ~28% of this change | — |
| [[A498 (line)]] | wt | 139 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 256 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 276 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 274 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 258 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 290 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 315 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 130 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 194 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 248 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 283 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 99.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 282 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 127 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 229 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 288 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 122 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 188 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 279 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 245 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 251 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 303 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 180 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6554), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[INSIG2]] | +0.85 | +0.88 / +0.80 | both halves | 7e-06 |  |
| [[ANKRD37]] | +0.79 | +0.85 / +0.66 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.79 | +0.80 / +0.72 | both halves | 7e-06 |  |
| [[CNOT8]] | +0.78 | +0.84 / +0.70 | both halves | 7e-06 |  |
| [[PDK3]] | +0.77 | +0.81 / +0.68 | both halves | 7e-06 |  |
| [[USP37]] | +0.77 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[KDM3A]] | +0.76 | +0.78 / +0.69 | both halves | 7e-06 |  |
| [[P4HA1]] | +0.76 | +0.72 / +0.70 | both halves | 7e-06 |  |
| [[YEATS2]] | +0.75 | +0.84 / +0.64 | both halves | 7e-06 |  |
| [[PFKFB4]] | +0.75 | +0.73 / +0.74 | both halves | 7e-06 |  |
| [[KDM4B]] | +0.74 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[ERO1A]] | +0.74 | +0.81 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CPLANE1]] | -0.65 | -0.68 / -0.59 | both halves | 7e-06 |  |
| [[AVEN]] | -0.61 | -0.65 / -0.45 | both halves | 3e-05 |  |
| [[PARVA]] | -0.61 | -0.51 / -0.44 | both halves | 3e-05 |  |
| [[RBM12]] | -0.60 | -0.49 / -0.56 | both halves | 1e-05 |  |
| [[SLC25A24]] | -0.59 | -0.44 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GPR160]] | B | GPR160 activity raises WDR45B's level | lines that do not express GPR160 (8) vs lines expressing it (42) | 1.38× lower at baseline in the lines without GPR160 | 0.016 | ⚠ within organs, on part of the lines; also absent: PNPLA4, PRKCZ; maybe low, not absent |
| [[TFPI]] | B | TFPI activity raises WDR45B's level | lines that do not express TFPI (14) vs lines expressing it (36) | 1.17× lower at baseline in the lines without TFPI | 0.096 | ⚠ within organs, on part of the lines; also absent: STC1, C2orf74-DT, CALCRL |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 164]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.857). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.37; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.3, -16.6); signed map (-35.9, 23.7). **Vector** length 124, 51.4% of its response variance represented; |z| ≥ 3 in 1,180 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | +8.5 | -3.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.5 | -6.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +6.2 | -3.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +6.2 | -4.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.5 | -2.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | -2.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +3.6 | +3.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.6 | -0.4 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +3.4 | +1.1 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | +3.0 | +1.2 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -8.8 | -5.9 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -5.2 | -4.0 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | -5.1 | +3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -4.6 | -3.1 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -6.0 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.2 | -3.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -3.1 | -1.4 |
|  | [[Rapamycin (drug)]] 5 µM |  | -3.1 | -3.1 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -3.0 | -0.9 |

## What is on record

|  |  |
|---|---|
| Name | WD repeat domain 45B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:82,614,562-82,648,553 (-) |
| Ensembl biotype | protein_coding |
| Also known as | WIPI3; previously WDR45L |
| Gene groups (HGNC) | WD repeat domain containing; WIPI family |
| Reactome | 2 pathways, smallest: Macroautophagy; Autophagy |
| Matched by | ensembl_id |

**Function**, from UniProt [Q5MNZ6](https://www.uniprot.org/uniprotkb/Q5MNZ6) (WD repeat domain phosphoinositide-interacting protein 3):

> Component of the autophagy machinery that controls the major intracellular degradation process by which cytoplasmic materials are packaged into autophagosomes and delivered to lysosomes for degradation. Binds phosphatidylinositol 3-phosphate (PtdIns3P), and other phosphoinositides including PtdIns(3,5)P2, forming on membranes of the endoplasmic reticulum upon activation of the upstream ULK1 and PI3 kinases and is recruited at phagophore assembly sites where it regulates the elongation of …

**Summary**, from NCBI Gene [56270](https://www.ncbi.nlm.nih.gov/gene/56270):

> This gene encodes a member of the WIPI or SVP1 family of WD40 repeat-containing proteins. The protein contains seven WD40 repeats that are thought to fold into a beta-propeller structure that mediates protein-protein interactions, and a conserved motif for interaction with phospholipids. The human genome contains several pseudogenes of this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:25072](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25072) · Entrez [56270](https://www.ncbi.nlm.nih.gov/gene/56270) · UniProt [Q5MNZ6](https://www.uniprot.org/uniprotkb/Q5MNZ6) · Ensembl [ENSG00000141580](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000141580)

## Data

Gene col 6554: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6554); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6554, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6554]; `tensor/DDL_lfc|DDL_z.npy` [6554]; `embed/gene_vectors.npy` [6554]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6554 or target_col == 6554). Every well: [[WDR45B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WDR45B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
