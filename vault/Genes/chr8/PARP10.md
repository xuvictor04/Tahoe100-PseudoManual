---
symbol: "PARP10"
type: "gene"
col: 10946
ensembl_id: "ENSG00000178685"
name: "poly(ADP-ribose) polymerase family member 10"
location: "8q24.3"
module: 32
arm: "+"
pooled_cpm: 9.92
n_lines_expressing: 49
n_dd_up: 19
n_dd_down: 28
n_dd_up_clean: 17
n_dd_down_clean: 24
in_vector_space: true
direction_upstream: 93
direction_downstream: 23
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# PARP10

*poly(ADP-ribose) polymerase family member 10* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (2 with an alert ⚠); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.63× (z +5.1, q 1e-04, up in 20 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 28 drug-doses (4 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.322× (z -12.3, q 6e-32, down in 35 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC15A3]] (+0.91, fdr 7e-06), [[DHX58]] (+0.88, fdr 7e-06), [[TRIM22]] (+0.87, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 93 arrows point to it, the strongest [[OAS2]] → it (grade B ⚠); 23 go from it, the strongest it → [[IRF9]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10946.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.63×** | +5.1 | 1e-04 | 20/43 (CFPAC-1, NCI-H23, …) | all doses, flat | position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.59×** | +5.0 | 1e-04 | 23/44 (NCI-H2347, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.58×** | +4.9 | 1e-04 | 22/43 (HS-578T, A-172, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.47×** | +4.2 | 0.004 | 16/40 (PANC-1, KATO III, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.05 µM |  | **1.50×** | +4.1 | 0.004 | 12/43 (NCI-H2347, NCI-H460, …) | all doses, flat | position effect removed |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.47×** | +4.0 | 0.005 | 17/44 (HS-578T, RKO, …) | rises with dose |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.29×** | +3.9 | 0.009 | 13/46 (NCI-H2347, SK-MEL-2, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.41×** | +3.5 | 0.027 | 12/45 (Hs 766T, NCI-H2347, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.37×** | +3.4 | 0.036 | 14/45 (Hs 766T, LOX-IMVI, …) | all doses, flat | position effect removed |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.55×** | +3.4 | 0.038 | 11/42 (A-172, NCI-H1792, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.33×** | +3.3 | 0.039 | 12/47 (Hs 766T, COLO 205, …) | all doses, flat | noisy plate (z scaled) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.53×** | +3.3 | 0.039 | 5/38 (NCI-H460, A498, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.35×** | +3.3 | 0.039 | 9/45 (NCI-H2347, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.30×** | +3.3 | 0.039 | 12/47 (AsPC-1, NCI-H2347, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.24×** | +3.3 | 0.040 | 13/46 (A498, LS 180, …) | top dose only | position effect removed |
| [[Thymol (drug)]] 0.5 µM |  | **1.34×** | +3.2 | 0.055 | 11/39 (NCI-H2347, KATO III, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.50×** | +3.1 | 0.055 | 7/43 (A498, SNU-423, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 4 with an alert ⚠; shown: the 15 strongest. 28 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10946.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.322×** | -12.3 | 6e-32 | 35/45 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.404×** | -9.8 | 3e-20 | 34/45 (SNU-423, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.539×** | -9.5 | 6e-19 | 28/45 (NCI-H2347, A-172, …) | rises with dose | position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.425×** | -9.3 | 3e-18 | 35/42 (CFPAC-1, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.429×** | -9.2 | 6e-18 | 31/45 (A-172, NCI-H2347, …) | all doses, flat | cell-cycle shift (explains ~9% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.497×** | -7.6 | 4e-12 | 26/45 (NCI-H2347, A-172, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.499×** | -7.5 | 4e-12 | 30/46 (HS-578T, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.531×** | -6.8 | 5e-10 | 30/45 (MIA PaCa-2, H4, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.653×** | -6.5 | 5e-09 | 26/45 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.555×** | -6.4 | 1e-08 | 24/44 (SNU-423, HepG2/C3A, …) | top dose only |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.573×** | -6.0 | 9e-08 | 25/45 (SHP-77, RKO, …) | all doses, flat | cell-cycle shift (explains ~17% here) |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.578×** | -5.9 | 1e-07 | 25/44 (MIA PaCa-2, RKO, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.583×** | -5.8 | 2e-07 | 27/44 (A498, AsPC-1, …) | rises with dose | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.599×** | -5.6 | 1e-06 | 24/44 (A-172, RPMI-7951, …) | rises with dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.395×** | -5.3 | 6e-06 | 22/41 (MIA PaCa-2, KATO III, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10946. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 17.3 | 0 | 5 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0961× (z -14.8) |
| [[NCI-H2347 (line)]] | alt | 21.3 | 0 | 4 | — | [[Tofacitinib (drug)]] 5 µM 0.260× (z -13.0) |
| [[RKO (line)]] | wt | 14.2 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0561× (z -12.4) |
| [[A498 (line)]] | wt | 23.8 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.347× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.239× (z -10.5) |
| [[AsPC-1 (line)]] | alt | 16.6 | 0 | 3 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.272× (z -9.2) |
| [[CFPAC-1 (line)]] | alt | 15.3 | 0 | 3 | — | [[Belinostat (drug)]] 0.5 µM 0.123× (z -13.0) |
| [[HS-578T (line)]] | alt | 17.6 | 0 | 3 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.117× (z -11.5) |
| [[LoVo (line)]] | wt | 15.0 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.101× (z -14.3) |
| [[RPMI-7951 (line)]] | alt | 18.9 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.170× (z -8.8) |
| [[SNU-423 (line)]] | alt | 12.1 | 0 | 2 | — | [[Auranofin (drug)]] 5 µM 0.0495× (z -14.0) |
| [[A549 (line)]] | wt | 8.00 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.116× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 9.58 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.0438× (z -10.9) |
| [[HOP62 (line)]] | alt | 3.01 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0667× (z -9.9) |
| [[Hs 766T (line)]] | wt | 17.1 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.176× (z -8.9) |
| [[MIA PaCa-2 (line)]] | alt | 12.7 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.155× (z -8.7) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 11.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.107× (z -9.5) ⚠ toxic |
| [[SK-MEL-2 (line)]] | alt | 10.4 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.112× (z -8.5) ⚠ toxic |
| [[A-427 (line)]] | wt | 3.42 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.94 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.51 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.78 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 8.16 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.79 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.44 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.95 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.09 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.30 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.37 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.36 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.09 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.11 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.15 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.18 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.77 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 6.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.49 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 3.02 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10946), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC15A3]] | +0.91 | +0.85 / +0.92 | both halves | 7e-06 | **novel candidate** |
| [[DHX58]] | +0.88 | +0.82 / +0.89 | both halves | 7e-06 | STRING 520 |
| [[TRIM22]] | +0.87 | +0.80 / +0.90 | both halves | 7e-06 | **novel candidate** |
| [[XAF1]] | +0.87 | +0.77 / +0.90 | both halves | 7e-06 | STRING 499 |
| [[OAS2]] | +0.86 | +0.79 / +0.89 | both halves | 7e-06 |  |
| [[HERC6]] | +0.86 | +0.80 / +0.86 | both halves | 7e-06 |  |
| [[PARP9]] | +0.85 | +0.74 / +0.89 | both halves | 7e-06 | same gene group; pathway: Late SARS-CoV-2 Infection Events; STRING 500 |
| [[PARP14]] | +0.85 | +0.77 / +0.86 | both halves | 7e-06 | same gene group; pathway: Late SARS-CoV-2 Infection Events; STRING 820 |
| [[USP18]] | +0.85 | +0.75 / +0.88 | both halves | 7e-06 |  |
| [[RSAD2]] | +0.85 | +0.78 / +0.87 | both halves | 7e-06 |  |
| [[MX1]] | +0.85 | +0.77 / +0.88 | both halves | 7e-06 |  |
| [[IFI35]] | +0.84 | +0.73 / +0.88 | both halves | 7e-06 | STRING 480 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*93 arrows, 93 of them with an alert ⚠; grade A 0, B 62, C 31. Shown: the 12 strongest; 81 more arrows (81 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS2]] | B | OAS2 activity raises PARP10's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.00× lower at baseline in the lines without OAS2 | 2e-04 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[OAS2]] | B | OAS2 activity strengthens PARP10's drug response | lines that do not express OAS2 (13) vs lines expressing it (33) | the lines without OAS2 respond 0.24× as strongly (z diff +2.86); strongest at Auranofin 5 µM: 1.03x vs 0.39x (z diff +4.7) | 5e-04 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1; target measured in part of the lines; artifact flags |
| [[RASGRP3]] | B | RASGRP3 activity raises PARP10's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 2.01× lower at baseline in the lines without RASGRP3 | 0.001 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[SAMD9L]] | B | SAMD9L activity raises PARP10's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 1.92× lower at baseline in the lines without SAMD9L | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[CMPK2]] | B | CMPK2 activity raises PARP10's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.01× lower at baseline in the lines without CMPK2 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[BATF2]] | B | BATF2 activity raises PARP10's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 1.95× lower at baseline in the lines without BATF2 | 0.001 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[PARP9]] | B | PARP9 activity raises PARP10's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 2.37× lower at baseline in the lines without PARP9 | 0.001 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[NRIR]] | B | NRIR activity raises PARP10's level | lines that do not express NRIR (14) vs lines expressing it (36) | 1.76× lower at baseline in the lines without NRIR | 0.002 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7 |
| [[IFI27]] | B | IFI27 activity raises PARP10's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 1.84× lower at baseline in the lines without IFI27 | 0.002 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[SAMD9L]] | B | SAMD9L activity strengthens PARP10's drug response | lines that do not express SAMD9L (17) vs lines expressing it (29) | the lines without SAMD9L respond 0.37× as strongly (z diff +2.61); strongest at Belinostat 5 µM: 0.55x vs 0.24x (z diff +4.2) | 0.002 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22; target measured in part of the lines; artifact flags |
| [[IFI6]] | B | IFI6 activity raises PARP10's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.03× lower at baseline in the lines without IFI6 | 0.003 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[OAS1]] | B | OAS1 activity raises PARP10's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.85× lower at baseline in the lines without OAS1 | 0.003 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |

### Downstream of this gene

*23 arrows, 23 of them with an alert ⚠; grade A 0, B 0, C 23. Shown: the 12 strongest; 11 more arrows (11 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IRF9]] | C | PARP10's natural level strengthens IRF9's drug response | PARP10's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.73; direction not clear | 0.004 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[ADAR]] | C | PARP10's natural level strengthens ADAR's drug response | PARP10's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.71; direction not clear | 0.005 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT5]] | C | PARP10's natural level strengthens IFIT5's drug response | PARP10's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.76; direction not clear | 0.008 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[DDX60]] | C | PARP10's natural level strengthens DDX60's drug response | PARP10's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.74, reverse +0.65; direction not clear | 0.012 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[CMTR1]] | C | PARP10's natural level strengthens CMTR1's drug response | PARP10's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.64; direction not clear | 0.013 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TMEM140]] | C | PARP10's natural level strengthens TMEM140's drug response | PARP10's natural level across 40 lines (lineage-adjusted; a glimpse) | r +0.76, reverse +0.63; direction not clear | 0.015 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[IFI44]] | C | PARP10's natural level strengthens IFI44's drug response | PARP10's natural level across 37 lines (lineage-adjusted; a glimpse) | r +0.79, reverse +0.39; direction not clear | 0.015 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP12]] | C | PARP10's natural level strengthens PARP12's drug response | PARP10's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.72; direction not clear | 0.019 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SAMHD1]] | C | PARP10's natural level strengthens SAMHD1's drug response | PARP10's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.71, reverse +0.72; direction not clear | 0.022 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[HELZ2]] | C | PARP10's natural level strengthens HELZ2's drug response | PARP10's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.74; direction not clear | 0.028 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[HERC6]] | C | PARP10's natural level strengthens HERC6's drug response | PARP10's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.69, reverse +0.70; direction not clear | 0.044 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[UBE2L6]] | C | PARP10's natural level strengthens UBE2L6's drug response | PARP10's natural level across 42 lines (lineage-adjusted; a glimpse) | r +0.70, reverse +0.63; direction not clear | 0.044 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.896). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (47.7, 52.8); signed map (63.8, 30.7). **Vector** length 108, 27.2% of its response variance represented; |z| ≥ 3 in 1,198 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.74 to 56); *interferon gamma response* (hallmark, mean cos +0.75 to 60); *interferon* (control, mean cos +0.80 to 23).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM |  | +8.1 | +2.5 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.5 | +0.9 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.9 | +5.0 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +5.2 | +4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +5.1 | +1.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.6 | +3.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.5 | +4.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.8 | +5.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.1 | +4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.1 | +3.3 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -6.2 | -9.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.9 | -6.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.6 | -5.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.6 | -7.6 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -4.4 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | poly(ADP-ribose) polymerase family member 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:143,977,153-144,012,772 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ14464, ARTD10 |
| Gene groups (HGNC) | Poly(ADP-ribose) polymerases |
| Reactome | 12 pathways, smallest: Maturation of nucleoprotein_9683610; Maturation of nucleoprotein_9694631; Nicotinate metabolism |
| Matched by | ensembl_id |

**Function**, from UniProt [Q53GL7](https://www.uniprot.org/uniprotkb/Q53GL7) (Protein mono-ADP-ribosyltransferase PARP10):

> ADP-ribosyltransferase that mediates mono-ADP-ribosylation of glutamate and aspartate residues on target proteins. In contrast to PARP1 and PARP2, it is not able to mediate poly-ADP-ribosylation. Catalyzes mono-ADP-ribosylation of GSK3B, leading to negatively regulate GSK3B kinase activity. Involved in translesion DNA synthesis in response to DNA damage via its interaction with PCNA.

**Summary**, from NCBI Gene [84875](https://www.ncbi.nlm.nih.gov/gene/84875):

> Poly(ADP-ribose) polymerases (PARPs), such as PARP10, regulate gene transcription by altering chromatin organization by adding ADP-ribose to histones. PARPs can also function as transcriptional cofactors (Yu et al., 2005 [PubMed 15674325]).[supplied by OMIM, Mar 2008]

**Accessions** — [HGNC:25895](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25895) · Entrez [84875](https://www.ncbi.nlm.nih.gov/gene/84875) · UniProt [Q53GL7](https://www.uniprot.org/uniprotkb/Q53GL7) · Ensembl [ENSG00000178685](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178685)

## Data

Gene col 10946: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10946); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10946, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10946]; `tensor/DDL_lfc|DDL_z.npy` [10946]; `embed/gene_vectors.npy` [10946]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10946 or target_col == 10946). Every well: [[PARP10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PARP10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
