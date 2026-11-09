---
symbol: "EEF1A1"
type: "gene"
col: 7990
ensembl_id: "ENSG00000156508"
name: "eukaryotic translation elongation factor 1 alpha 1"
location: "6q13"
module: 20
arm: "+"
pooled_cpm: 251.11
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 5
n_dd_up_clean: 8
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 1
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# EEF1A1

*eukaryotic translation elongation factor 1 alpha 1* — 6q13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.30× (z +8.9, q 4e-16, up in 42 of 44 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 3.39× (z +7.1, q 3e-10, up in 48 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (2 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.703× (z -3.9, q 0.028, down in 46 of 49 measured lines) ⚠ unreliable plate only; position not correctable. The strongest without an alert is [[Ipatasertib (drug)]] 0.5 µM: 0.586× (z -3.5, q 0.080, down in 36 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EEF1A1P5]] (+0.91, fdr 7e-06), [[RPL4]] (+0.82, fdr 7e-06), [[EIF4H]] (+0.80, fdr 7e-06); moves opposite to [[CROCCP2-1]] (-0.68, fdr 7e-06), [[ZNF503]] (-0.62, fdr 1e-05), [[TRAPPC4]] (-0.62, fdr 4e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CYBRD1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[EEF2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7990.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.30×** | +8.9 | 4e-16 | 42/44 (LoVo, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.22×** | +8.8 | 4e-16 | 44/49 (SHP-77, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **3.39×** | +7.1 | 3e-10 | 48/49 (NCI-H1573, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.98×** | +7.0 | 4e-10 | 41/45 (LoVo, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.61×** | +5.0 | 5e-05 | 44/47 (NCI-H460, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.55×** | +4.9 | 1e-04 | 40/48 (NCI-H460, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.53×** | +4.7 | 2e-04 | 41/48 (NCI-H460, SW480, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +4.3 | 0.001 | 30/49 (NCI-H2347, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.45×** | +4.1 | 0.003 | 42/48 (SW 900, H4, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.43×** | +4.0 | 0.004 | 37/48 (RPMI-7951, C32, …) | two highest doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.94×** | +3.8 | 0.007 | 39/48 (C32, SW48, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.38×** | +3.4 | 0.036 | 36/48 (CFPAC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.096 | 34/48 (C32, RPMI-7951, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Erlotinib (drug)]] 5 µM |  | 1.33× | +3.0 | 0.10 | 32/47 (RKO, SW480, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 3 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7990.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.703×** | -3.9 | 0.028 | 46/49 (PANC-1, NCI-H23, …) | inconsistent across doses |  |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.705×** | -3.9 | 0.028 | 45/49 (HCT15, AN3 CA, …) | inconsistent across doses |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **0.586×** | -3.5 | 0.080 | 36/48 (LS 180, H4, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Azithromycin (hydrate) (drug)]] 5 µM |  | **0.807×** | -3.4 | 0.080 | 35/49 (Hs 766T, SNU-423, …) | top dose only | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.738×** | -3.4 | 0.080 | 37/48 (SW1417, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | 0.765× | -3.0 | 0.25 | 30/48 (SW 1088, PANC-1, …) | rises with dose | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.18 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7990. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 279 | 8 (4 ⚠) | 0 | [[Digitoxin (drug)]] 0.5 µM 3.36× (z +12.4) | — |
| [[LoVo (line)]] | wt | 439 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.24× (z +11.7) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 185 | 3 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.72× (z +11.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A498 (line)]] | wt | 139 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +17.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A549 (line)]] | wt | 217 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.49× (z +11.0) ⚠ toxic; transcription drop | — |
| [[C-33 A (line)]] | alt | 312 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[COLO 205 (line)]] | alt | 90.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.56× (z +11.3) ⚠ toxic; transcription drop | — |
| [[Hs 766T (line)]] | wt | 190 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.55× (z +9.0) ⚠ toxic; transcription drop | — |
| [[MIA PaCa-2 (line)]] | alt | 274 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.57× (z +10.0) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 154 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.43× (z +9.9) ⚠ toxic; transcription drop | — |
| [[SHP-77 (line)]] | alt | 113 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +12.9) ⚠ toxic; transcription drop | — |
| [[SW 900 (line)]] | alt | 141 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +10.4) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 136 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.01× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[A-427 (line)]] | wt | 235 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.472× (z -10.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 151 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +14.9) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[H4 (line)]] | wt | 192 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.83× (z +8.9) ⚠ toxic; transcription drop | — |
| [[HEC-1-A (line)]] | alt | 233 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.90× (z +10.7) ⚠ toxic; transcription drop | — |
| [[HepG2_C3A (line)]] | wt | 312 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.18× (z +8.9) | — |
| [[HT-29 (line)]] | alt | 309 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.68× (z +8.7) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 294 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.447× (z -11.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 297 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.84× (z +11.4) | — |
| [[Panc 03.27 (line)]] | alt | 272 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +10.0) ⚠ toxic; transcription drop | — |
| [[RKO (line)]] | wt | 349 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.68× (z +9.2) ⚠ toxic; transcription drop | — |
| [[SW1417 (line)]] | alt | 163 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.42× (z +8.5) ⚠ toxic; transcription drop | — |
| [[SW480 (line)]] | alt | 284 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.47× (z +9.2) ⚠ toxic; transcription drop | — |
| [[AN3 CA (line)]] | alt | 377 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 265 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 153 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 241 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 357 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 256 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 189 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 284 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 130 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 195 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 442 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 278 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 193 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 421 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 248 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 289 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 285 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 151 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 189 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 514 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 371 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 204 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 481 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7990), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*82 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EEF1A1P5]] | +0.91 | +0.84 / +0.91 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation |
| [[RPL4]] | +0.82 | +0.81 / +0.84 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 997 |
| [[EIF4H]] | +0.80 | +0.74 / +0.81 | both halves | 7e-06 | STRING 494 |
| [[RPL10]] | +0.79 | +0.75 / +0.82 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 977 |
| [[RPL3]] | +0.78 | +0.85 / +0.86 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 995 |
| [[ANKRD30BL]] | +0.76 | +0.68 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[RPS18]] | +0.76 | +0.75 / +0.80 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 986 |
| [[HNRNPA1L3]] | +0.73 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[DHFR]] | +0.73 | +0.62 / +0.72 | both halves | 7e-06 | STRING 436 |
| [[RPS3A]] | +0.72 | +0.72 / +0.72 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 997 |
| [[NONO]] | +0.72 | +0.73 / +0.76 | both halves | 7e-06 | STRING 487 |
| [[RPL18A]] | +0.71 | +0.73 / +0.70 | both halves | 7e-06 | pathway: Eukaryotic Translation Elongation; STRING 996 |

## Genes that move opposite

*18 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 3 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP2-1]] | -0.68 | -0.63 / -0.69 | both halves | 7e-06 |  |
| [[ZNF503]] | -0.62 | -0.51 / -0.71 | both halves | 1e-05 |  |
| [[TRAPPC4]] | -0.62 | -0.41 / -0.67 | both halves | 4e-05 |  |
| [[MTLN]] ⚠ | -0.61 | -0.32 / -0.70 | both halves | 2e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPS18C]] | -0.61 | -0.47 / -0.68 | both halves | 2e-05 |  |
| [[PPP1R35]] ⚠ | -0.61 | -0.43 / -0.61 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ERVK3-1]] | -0.61 | -0.50 / -0.73 | both halves | 1e-05 |  |
| [[INAFM1]] | -0.59 | -0.46 / -0.62 | both halves | 3e-05 |  |
| [[PIGBOS1]] | -0.59 | -0.51 / -0.60 | both halves | 1e-05 |  |
| [[TARS2]] | -0.58 | -0.35 / -0.65 | both halves | 1e-04 |  |
| [[SMIM26]] ⚠ | -0.58 | -0.35 / -0.63 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[ADPRS]] | -0.57 | -0.39 / -0.63 | both halves | 6e-05 |  |
| [[RBX1]] | -0.57 | -0.57 / -0.68 | both halves | 9e-06 | STRING 454 |
| [[MRPL46]] | -0.57 | -0.27 / -0.68 | both halves | 3e-04 |  |
| [[FOXA2]] | -0.57 | -0.43 / -0.64 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYBRD1]] | B | CYBRD1 activity raises EEF1A1's level | lines that do not express CYBRD1 (17) vs lines expressing it (33) | 1.15× lower at baseline in the lines without CYBRD1 | 0.061 | ⚠ within organs, on part of the lines; also absent: MME, BDNF, APOBEC3G |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[EEF2]] | C | EEF1A1's natural level weakens EEF2's drug response | EEF1A1's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.63, reverse -0.35; direction not clear | 0.068 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.729). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-29.3, -25.0); signed map (-21.6, -34.3). **Vector** length 150, 56.9% of its response variance represented; |z| ≥ 3 in 922 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Cap-dependent Translation Initiation* (reactome, mean cos +0.67 to 12); *Eukaryotic Translation Initiation* (reactome, mean cos +0.67 to 12); *L13a-mediated translational silencing of Ceruloplasmin expression* (reactome, mean cos +0.71 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +9.8 | +7.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +9.6 | +8.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +8.5 | +8.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +4.3 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +4.8 | +2.3 |
|  | [[Erlotinib (drug)]] 5 µM |  | +4.6 | +3.0 |
|  | [[Benproperine (phosphate) (drug)]] 0.05 µM |  | +4.5 | +2.2 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | +4.5 | +2.9 |
|  | [[Bimiralisib (drug)]] 5 µM |  | +4.4 | +1.3 |
| fall | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -5.9 | +0.5 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -5.7 | -3.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.2 | -3.5 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -4.7 | -2.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | -4.3 | -2.2 |
|  | [[BAY1125976 (drug)]] 0.5 µM |  | -4.1 | -2.5 |
|  | [[Sapanisertib (drug)]] 0.5 µM |  | -4.0 | -1.9 |
|  | [[Methylprednisolone succinate (drug)]] 0.5 µM |  | -4.0 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation elongation factor 1 alpha 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q13 — chr6:73,489,308-73,525,587 (-) |
| Ensembl biotype | protein_coding |
| Also known as | EE1A1, EF1A1, EF1alpha1; previously EF1A, EEF1A, LENG7 |
| Gene groups (HGNC) | Translational GTPases |
| Reactome | 17 pathways, smallest: Protein methylation; Chaperone Mediated Autophagy; HSF1 activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P68104](https://www.uniprot.org/uniprotkb/P68104) (Elongation factor 1-alpha 1):

> Translation elongation factor that catalyzes the GTP-dependent binding of aminoacyl-tRNA (aa-tRNA) to the A-site of ribosomes during the elongation phase of protein synthesis. Base pairing between the mRNA codon and the aa-tRNA anticodon promotes GTP hydrolysis, releasing the aa-tRNA from EEF1A1 and allowing its accommodation into the ribosome. The growing protein chain is subsequently transferred from the P-site peptidyl tRNA to the A-site aa-tRNA, extending it by one amino acid through …

**Summary**, from NCBI Gene [1915](https://www.ncbi.nlm.nih.gov/gene/1915):

> This gene encodes an isoform of the alpha subunit of the elongation factor-1 complex, which is responsible for the enzymatic delivery of aminoacyl tRNAs to the ribosome. This isoform (alpha 1) is expressed in brain, placenta, lung, liver, kidney, and pancreas, and the other isoform (alpha 2) is expressed in brain, heart and skeletal muscle. This isoform is identified as an autoantigen in 66% of patients with Felty syndrome. This gene has been found to have multiple copies on many chromosomes, …

**Accessions** — [HGNC:3189](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:3189) · Entrez [1915](https://www.ncbi.nlm.nih.gov/gene/1915) · UniProt [P68104](https://www.uniprot.org/uniprotkb/P68104) · Ensembl [ENSG00000156508](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000156508)

## Data

Gene col 7990: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7990); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7990, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7990]; `tensor/DDL_lfc|DDL_z.npy` [7990]; `embed/gene_vectors.npy` [7990]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7990 or target_col == 7990). Every well: [[EEF1A1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EEF1A1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
