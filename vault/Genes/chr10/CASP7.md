---
symbol: "CASP7"
type: "gene"
col: 9190
ensembl_id: "ENSG00000165806"
name: "caspase 7"
location: "10q25.3"
module: 32
arm: "+"
pooled_cpm: 28.62
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 10
n_dd_up_clean: 20
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 12
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# CASP7

*caspase 7* — 10q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.48× (z +10.1, q 4e-21, up in 36 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.613× (z -8.9, q 3e-16, down in 32 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GBP3]] (+0.70, fdr 7e-06), [[NMI]] (+0.70, fdr 7e-06), [[APOL2]] (+0.70, fdr 7e-06); moves opposite to [[ODF2]] (-0.54, fdr 3e-05), [[OSBPL8]] (-0.53, fdr 4e-05), [[ERGIC1]] (-0.52, fdr 1e-04).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 12 arrows point to it, the strongest [[NMRAL2P-1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9190.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.48×** | +10.1 | 4e-21 | 36/45 (MIA PaCa-2, J82, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.74×** | +9.5 | 6e-19 | 33/47 (A498, SW480, …) | all doses, flat | cell-cycle shift (explains ~20% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.64×** | +8.9 | 8e-17 | 30/48 (SW480, A498, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.61×** | +8.6 | 1e-15 | 29/47 (PANC-1, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.49×** | +7.2 | 7e-11 | 32/47 (NCI-H2347, SNU-423, …) | two highest doses | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.44×** | +6.6 | 4e-09 | 25/48 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.96×** | +6.4 | 2e-08 | 23/39 (C32, SK-MEL-2, …) | all doses, flat | cell-cycle shift (explains ~18% here); noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.43×** | +6.2 | 4e-08 | 24/46 (NCI-H460, AsPC-1, …) | rises with dose | position effect removed |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **1.26×** | +5.8 | 4e-07 | 21/48 (NCI-H2347, KATO III, …) | rises with dose | low cells (technical?) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.26×** | +5.2 | 1e-05 | 20/48 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.32×** | +5.2 | 1e-05 | 25/48 (AsPC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.32×** | +5.0 | 3e-05 | 17/47 (NCI-H460, AsPC-1, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.30×** | +4.8 | 7e-05 | 21/48 (A498, NCI-H2347, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.28×** | +4.7 | 1e-04 | 15/48 (AsPC-1, NCI-H460, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | 1.19× | +4.4 | 4e-04 | 16/48 (NCI-H460, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **1.30×** | +4.4 | 4e-04 | 14/48 (AsPC-1, NCI-H460, …) | all doses, flat |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.29×** | +4.3 | 5e-04 | 16/46 (AsPC-1, LS 180, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 1.18× | +4.3 | 6e-04 | 18/48 (SW1417, SW480, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 4 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9190.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.613×** | -8.9 | 3e-16 | 32/48 (NCI-H460, KATO III, …) | two highest doses | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.658×** | -7.6 | 6e-12 | 32/48 (NCI-H460, A498, …) | two highest doses | cell-cycle shift (explains ~5% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.703×** | -5.9 | 5e-07 | 23/35 (SW480, A-172, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.757×** | -5.1 | 5e-05 | 23/48 (NCI-H460, A549, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.596×** | -4.9 | 9e-05 | 22/48 (HT-29, A549, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~20% here); composition shift; noisy plate (z scaled) |
| [[Tofacitinib (drug)]] 5 µM |  | 0.840× | -4.5 | 5e-04 | 15/48 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~44% of this change | **0.784×** | -4.3 | 0.001 | 17/33 (NCI-H460, NCI-H1792, …) | all doses, flat | composition shift |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.792×** | -4.3 | 0.001 | 21/48 (SHP-77, A549, …) | two highest doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **0.811×** | -3.8 | 0.008 | 20/41 (LS 180, SW1417, …) | all doses, flat | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~59% of this change | **0.814×** | -3.8 | 0.009 | 20/46 (LS 180, NCI-H460, …) | inconsistent across doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.713×** | -3.2 | 0.063 | 8/45 (HS-578T, LOX-IMVI, …) | rises with dose | noisy plate (z scaled) |
| [[Bendamustine (drug)]] 5 µM |  | 0.843× | -3.0 | 0.12 | 11/45 (SNU-1, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.00 per unit of S-phase module lfc, -0.28 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9190. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 137 | 0 | 9 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.214× (z -18.9) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.153× (z -16.3) |
| [[A498 (line)]] | wt | 30.0 | 2 | 1 | [[Bortezomib (drug)]] 0.05 µM 3.04× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.370× (z -9.6) |
| [[A-172 (line)]] | wt | 33.6 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.370× (z -8.8) |
| [[KATO III (line)]] | alt | 30.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -9.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.336× (z -9.3) |
| [[LS 180 (line)]] | wt | 31.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.262× (z -11.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change |
| [[NCI-H23 (line)]] | alt | 13.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.163× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~66% of this change |
| [[PANC-1 (line)]] | alt | 22.9 | 2 | 0 | [[Harringtonine (drug)]] 0.5 µM 3.23× (z +12.0) | — |
| [[SK-MEL-2 (line)]] | alt | 23.1 | 0 | 2 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0682× (z -17.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 12.8 | 0 | 1 | — | [[Brimonidine (drug)]] 0.5 µM 0.151× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 16.1 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.146× (z -11.4) |
| [[SHP-77 (line)]] | alt | 11.9 | 0 | 1 | — | [[Trimetrexate (drug)]] 0.05 µM 0.180× (z -8.5) |
| [[SW48 (line)]] | wt | 14.3 | 0 | 1 | — | [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.0943× (z -10.0) |
| [[SW480 (line)]] | alt | 22.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.329× (z -9.3) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 29.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 15.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 25.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 11.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 22.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 16.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 33.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.7 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 41.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 16.0 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 15.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.8 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 24.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 18.5 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 31.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 29.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 36.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 33.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 39.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9190), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GBP3]] | +0.70 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[NMI]] | +0.70 | +0.67 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[APOL2]] | +0.70 | +0.63 / +0.67 | both halves | 7e-06 |  |
| [[ERAP2]] | +0.68 | +0.62 / +0.55 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT |
| [[IL15RA]] | +0.67 | +0.58 / +0.63 | both halves | 8e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[BTN3A3]] | +0.66 | +0.57 / +0.57 | both halves | 1e-05 |  |
| [[PHF11]] | +0.64 | +0.56 / +0.57 | both halves | 1e-05 |  |
| [[APOBEC3F]] | +0.64 | +0.55 / +0.54 | both halves | 1e-05 | pathway: HALLMARK_COMPLEMENT |
| [[GBP1]] | +0.63 | +0.61 / +0.58 | both halves | 8e-06 |  |
| [[PRRG4]] | +0.62 | +0.52 / +0.50 | both halves | 1e-05 |  |
| [[MOV10]] | +0.62 | +0.46 / +0.52 | both halves | 2e-05 |  |
| [[APOL6]] | +0.62 | +0.52 / +0.57 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ODF2]] | -0.54 | -0.55 / -0.43 | both halves | 3e-05 |  |
| [[OSBPL8]] | -0.53 | -0.49 / -0.41 | both halves | 4e-05 |  |
| [[ERGIC1]] | -0.52 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[CNN2]] | -0.50 | -0.42 / -0.37 | both halves | 7e-05 |  |
| [[HPCAL1]] | -0.50 | -0.44 / -0.29 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 12, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NMRAL2P-1]] | B | NMRAL2P-1 activity raises CASP7's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 1.61× lower at baseline in the lines without NMRAL2P-1 | 0.011 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[GBP4]] | B | GBP4 activity raises CASP7's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 1.28× lower at baseline in the lines without GBP4 | 0.017 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[RSAD2]] | B | RSAD2 activity raises CASP7's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 1.53× lower at baseline in the lines without RSAD2 | 0.026 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[APOL3]] | B | APOL3 activity raises CASP7's level | lines that do not express APOL3 (14) vs lines expressing it (36) | 1.54× lower at baseline in the lines without APOL3 | 0.036 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |
| [[GBP1]] | B | GBP1 activity raises CASP7's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 1.35× lower at baseline in the lines without GBP1 | 0.042 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[NMRAL2P]] | B | NMRAL2P activity raises CASP7's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 1.50× lower at baseline in the lines without NMRAL2P | 0.067 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |
| [[SAMD9L]] | B | SAMD9L activity raises CASP7's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 1.34× lower at baseline in the lines without SAMD9L | 0.068 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[CASP10]] | B | CASP10 activity raises CASP7's level | lines that do not express CASP10 (19) vs lines expressing it (31) | 1.38× lower at baseline in the lines without CASP10 | 0.084 | ⚠ within organs, on part of the lines; also absent: RARRES1, TRIM22, ACSL5 |
| [[MAP2K1]] | B | MAP2K1 activity lowers CASP7's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 3.9% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[SAMD9]] | B | SAMD9 activity raises CASP7's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 1.26× lower at baseline in the lines without SAMD9 | 0.093 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[HDAC6]] | B | HDAC6 activity raises CASP7's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[IFIT2]] | B | IFIT2 activity raises CASP7's level | lines that do not express IFIT2 (8) vs lines expressing it (42) | 1.38× lower at baseline in the lines without IFIT2 | 0.0997 | ⚠ within organs, on part of the lines; also absent: IFIT3, ENSG00000235609, TRIM38 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.556). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (44.8, 53.1); signed map (61.0, 31.2). **Vector** length 106, 24.7% of its response variance represented; |z| ≥ 3 in 1,158 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +6.6 | +8.9 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +6.6 | +9.5 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +5.8 | +6.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +5.3 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +5.2 | +7.2 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.8 | +6.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.4 | +4.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +4.2 | +4.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.1 | +3.9 |
| fall | [[Panobinostat (drug)]] 5 µM |  | -6.2 | -7.6 |
|  | [[Belinostat (drug)]] 5 µM |  | -5.4 | -5.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -5.4 | -8.9 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -3.4 | -4.5 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -3.0 | -4.3 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -2.8 | -2.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.7 | -1.7 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.6 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | caspase 7 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q25.3 — chr10:113,679,162-113,730,907 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MCH3, CMH-1, ICE-LAP3 |
| Gene groups (HGNC) | Caspases |
| Hallmark sets | APOPTOSIS, COMPLEMENT, INTERFERON_GAMMA_RESPONSE, OXIDATIVE_PHOSPHORYLATION |
| Reactome | 12 pathways, smallest: Activation of caspases through apoptosome-mediated cleavage; SMAC (DIABLO) binds to IAPs; SMAC(DIABLO)-mediated dissociation of IAP:caspase complexes |
| Matched by | ensembl_id |

**Function**, from UniProt [P55210](https://www.uniprot.org/uniprotkb/P55210) (Caspase-7):

> Thiol protease involved in different programmed cell death processes, such as apoptosis, pyroptosis or granzyme-mediated programmed cell death, by proteolytically cleaving target proteins. Has a marked preference for Asp-Glu-Val-Asp (DEVD) consensus sequences, with some plasticity for alternate non-canonical sequences. Its involvement in the different programmed cell death processes is probably determined by upstream proteases that activate CASP7 (By similarity). Acts as an effector caspase …

**Summary**, from NCBI Gene [840](https://www.ncbi.nlm.nih.gov/gene/840):

> This gene encodes a member of the cysteine-aspartic acid protease (caspase) family. Sequential activation of caspases plays a central role in the execution-phase of cell apoptosis. Caspases exist as inactive proenzymes which undergo proteolytic processing at conserved aspartic residues to produce two subunits, large and small, that dimerize to form the active enzyme. The precursor of the encoded protein is cleaved by caspase 3 and 10, is activated upon cell death stimuli and induces apoptosis. …

**Accessions** — [HGNC:1508](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:1508) · Entrez [840](https://www.ncbi.nlm.nih.gov/gene/840) · UniProt [P55210](https://www.uniprot.org/uniprotkb/P55210) · Ensembl [ENSG00000165806](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000165806)

## Data

Gene col 9190: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9190); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9190, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9190]; `tensor/DDL_lfc|DDL_z.npy` [9190]; `embed/gene_vectors.npy` [9190]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9190 or target_col == 9190). Every well: [[CASP7 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CASP7.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
