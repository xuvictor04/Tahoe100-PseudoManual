---
symbol: "RGS10"
type: "gene"
col: 7325
ensembl_id: "ENSG00000148908"
name: "regulator of G protein signaling 10"
location: "10q26.11"
module: 77
arm: "+"
pooled_cpm: 22.56
n_lines_expressing: 46
n_dd_up: 11
n_dd_down: 14
n_dd_up_clean: 5
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 7
direction_downstream: 8
tags: ["gene", "module/077"]
generated_by: "tahoemap"
---

# RGS10

*regulator of G protein signaling 10* — 10q26.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (6 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.33× (z +5.7, q 9e-06, up in 26 of 44 measured lines).
> Pooled over the cell lines (median), lowered significantly by 14 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.466× (z -15.1, q 0e+00, down in 34 of 44 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ATP7B]] (+0.74, fdr 7e-06), [[UQCRH]] (+0.73, fdr 7e-06), [[ANKRD27]] (+0.72, fdr 7e-06); moves opposite to [[COQ7]] (-0.68, fdr 1e-05), [[ZNF747]] (-0.67, fdr 1e-05), [[USP40]] (-0.66, fdr 7e-06).
> It sits in the **+** arm of [[Module 077]].
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[SUCLG2-DT]] → it (grade B ⚠); 8 go from it, the strongest it → [[HEBP1]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 6 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7325.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +5.7 | 9e-06 | 26/44 (SW480, SW1417, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +5.4 | 2e-05 | 22/42 (SW480, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **1.42×** | +4.7 | 4e-04 | 16/31 (LoVo, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **1.40×** | +4.7 | 4e-04 | 25/43 (LOX-IMVI, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.37×** | +4.5 | 9e-04 | 19/44 (Panc 03.27, NCI-H1792, …) | inconsistent across doses | cell-cycle shift (explains ~8% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.36×** | +4.3 | 0.002 | 18/39 (PANC-1, J82, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.35×** | +4.3 | 0.002 | 22/44 (A-172, Panc 03.27, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.35×** | +4.2 | 0.002 | 20/44 (A-172, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~19% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.32×** | +3.9 | 0.006 | 18/44 (SW480, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **1.22×** | +3.9 | 0.006 | 17/43 (SNU-1, C-33 A, …) | top dose only |  |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **1.58×** | +3.1 | 0.087 | 9/37 (A498, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 1 with an alert ⚠. 14 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7325.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.466×** | -15.1 | 0e+00 | 34/44 (SW48, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.528×** | -8.9 | 1e-16 | 34/44 (NCI-H2030, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.563×** | -7.7 | 2e-12 | 33/44 (LoVo, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.441×** | -5.6 | 3e-06 | 26/44 (A498, LOX-IMVI, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.680×** | -5.4 | 8e-06 | 24/44 (HepG2/C3A, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.706×** | -4.9 | 1e-04 | 23/44 (HEC-1-A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.563×** | -3.9 | 0.007 | 15/42 (A-172, KATO III, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.772×** | -3.6 | 0.019 | 20/44 (NCI-H460, HEC-1-A, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~18% of this change | **0.833×** | -3.6 | 0.019 | 16/44 (Hs 766T, HS-578T, …) | top dose only | low cells (technical?) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.751×** | -3.6 | 0.020 | 16/44 (HEC-1-A, SW48, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.777×** | -3.5 | 0.021 | 14/44 (HepG2/C3A, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.840× | -3.5 | 0.026 | 16/44 (A498, NCI-H460, …) | rises with dose |  |
| [[Demeclocycline (drug)]] 5 µM |  | 0.845× | -3.3 | 0.037 | 12/44 (HS-578T, A498, …) | top dose only |  |
| [[ERK5-IN-2 (drug)]] 5 µM |  | **0.627×** | -3.2 | 0.057 | 9/44 (HOP62, SW1417, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.797×** | -3.2 | 0.057 | 8/44 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.796×** | -3.0 | 0.090 | 15/43 (LoVo, LOX-IMVI, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.11 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7325. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 75.6 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.474× (z -10.3) |
| [[A-427 (line)]] | wt | 23.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.154× (z -12.2) |
| [[Hs 766T (line)]] | wt | 24.1 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.348× (z -9.0) |
| [[LS 180 (line)]] | wt | 12.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.116× (z -10.9) |
| [[NCI-H2030 (line)]] | alt | 14.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.125× (z -13.9) |
| [[SW48 (line)]] | wt | 36.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.124× (z -16.5) |
| [[A498 (line)]] | wt | 23.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -12.7) |
| [[A549 (line)]] | wt | 23.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.209× (z -14.2) |
| [[AN3 CA (line)]] | alt | 85.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.321× (z -8.9) |
| [[AsPC-1 (line)]] | alt | 12.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -11.1) |
| [[BT-474 (line)]] | alt | 8.03 | 0 | 1 | — | [[Monocrotaline (drug)]] 0.05 µM 0.0723× (z -9.7) |
| [[C-33 A (line)]] | alt | 26.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.193× (z -9.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 11.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.346× (z -9.5) |
| [[HS-578T (line)]] | alt | 20.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -8.8) |
| [[hTERT-HPNE (line)]] | wt | 40.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.329× (z -10.4) |
| [[J82 (line)]] | alt | 10.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -12.0) |
| [[KATO III (line)]] | alt | 13.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -12.3) |
| [[NCI-H1573 (line)]] | alt | 10.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.138× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 17.5 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.226× (z -12.1) |
| [[NCI-H2347 (line)]] | alt | 71.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.493× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 18.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.432× (z -8.7) |
| [[SNU-1 (line)]] | wt | 29.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.244× (z -10.0) |
| [[A-172 (line)]] | wt | 42.4 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.11 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 15.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 28.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.43 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 22.8 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.4 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 38.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 46.5 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.89 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 23.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.01 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 8.05 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7325), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*62 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ATP7B]] | +0.74 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[UQCRH]] | +0.73 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[ANKRD27]] | +0.72 | +0.65 / +0.64 | both halves | 7e-06 |  |
| [[SLC37A3]] | +0.69 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[RACK1]] | +0.68 | +0.60 / +0.57 | both halves | 1e-05 |  |
| [[TSPAN33]] | +0.68 | +0.44 / +0.66 | both halves | 3e-05 |  |
| [[HEBP1]] | +0.67 | +0.53 / +0.67 | both halves | 1e-05 | pathway: G alpha (i) signalling events |
| [[RPL12]] | +0.67 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[MPST]] | +0.67 | +0.57 / +0.60 | both halves | 9e-06 |  |
| [[WASF3]] | +0.67 | +0.52 / +0.54 | both halves | 1e-05 |  |
| [[TPST2]] | +0.66 | +0.66 / +0.52 | both halves | 1e-05 |  |
| [[MPZL1]] | +0.66 | +0.59 / +0.54 | both halves | 1e-05 |  |

## Genes that move opposite

*38 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COQ7]] | -0.68 | -0.63 / -0.55 | both halves | 1e-05 |  |
| [[ZNF747]] | -0.67 | -0.61 / -0.53 | both halves | 1e-05 |  |
| [[USP40]] | -0.66 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[LIG4]] | -0.66 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[TIA1]] | -0.65 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[CASC9]] | -0.65 | -0.59 / -0.55 | both halves | 1e-05 |  |
| [[ZFP91]] | -0.65 | -0.61 / -0.50 | both halves | 1e-05 |  |
| [[PCNX4-DT]] | -0.65 | -0.69 / -0.30 | both halves | 2e-04 |  |
| [[MIS12]] | -0.65 | -0.60 / -0.54 | both halves | 1e-05 |  |
| [[ZNF764]] | -0.64 | -0.60 / -0.49 | both halves | 1e-05 |  |
| [[ZFX]] | -0.64 | -0.59 / -0.53 | both halves | 1e-05 |  |
| [[BCLAF1]] | -0.64 | -0.58 / -0.58 | both halves | 8e-06 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 6, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SUCLG2-DT]] | B | SUCLG2-DT activity raises RGS10's level | lines that do not express SUCLG2-DT (7) vs lines expressing it (43) | 2.49× lower at baseline in the lines without SUCLG2-DT | 0.005 | ⚠ within organs, on part of the lines; also absent: TMCC2, DRAM1, ELK3; maybe low, not absent |
| [[ARHGAP44]] | B | ARHGAP44 activity raises RGS10's level | lines that do not express ARHGAP44 (16) vs lines expressing it (34) | 1.56× lower at baseline in the lines without ARHGAP44 | 0.064 | ⚠ within organs, on part of the lines; also absent: BEGAIN, MSI1, CHD5; maybe low, not absent |
| [[TSPAN13]] | B | TSPAN13 activity lowers RGS10's level | lines that do not express TSPAN13 (13) vs lines expressing it (37) | 1.64× higher at baseline in the lines without TSPAN13 | 0.066 | ⚠ within organs, on part of the lines; also absent: JUP, MPZL3, MYO5C |
| [[MCOLN2]] | B | MCOLN2 activity raises RGS10's level | lines that do not express MCOLN2 (18) vs lines expressing it (32) | 1.64× lower at baseline in the lines without MCOLN2 | 0.083 | ⚠ within organs, on part of the lines; also absent: DCLK2, MSI1, PARVG |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers RGS10's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |
| [[HDAC6]] | B | HDAC6 activity lowers RGS10's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[RUSC2]] | C | RUSC2 activity raises RGS10's level | lines that do not express RUSC2 (4) vs lines expressing it (46) | 2.72× lower at baseline in the lines without RUSC2 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; also absent: ATP8B3, SOAT1, SPAG17; its own permutation p |

### Downstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 0, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HEBP1]] | C | RGS10 activity raises HEBP1's level | lines that do not express RGS10 (4) vs lines expressing it (46) | 2.07× lower at baseline in the lines without RGS10 | 0.003 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HOMER3, ARHGEF17, CHST3; maybe low, not absent |
| [[RPL12]] | C | RGS10 activity raises RPL12's level | lines that do not express RGS10 (4) vs lines expressing it (46) | 1.55× lower at baseline in the lines without RGS10 | 0.031 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HOMER3, ARHGEF17, CHST3; maybe low, not absent |
| [[RPL32]] | C | RGS10 activity raises RPL32's level | lines that do not express RGS10 (4) vs lines expressing it (46) | 1.46× lower at baseline in the lines without RGS10 | 0.050 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HOMER3, ARHGEF17, CHST3; maybe low, not absent |
| [[RPS24]] | C | RGS10 activity raises RPS24's level | lines that do not express RGS10 (4) vs lines expressing it (46) | 1.44× lower at baseline in the lines without RGS10 | 0.060 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HOMER3, ARHGEF17, CHST3; maybe low, not absent |
| [[MCUB]] | C | RGS10 activity raises MCUB's level | lines that do not express RGS10 (4) vs lines expressing it (46) | 1.98× lower at baseline in the lines without RGS10 | 0.065 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HOMER3, ARHGEF17, CHST3; maybe low, not absent |
| [[TOMM20]] | C | RGS10 activity raises TOMM20's level | lines that do not express RGS10 (4) vs lines expressing it (46) | 1.32× lower at baseline in the lines without RGS10 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HOMER3, ARHGEF17, CHST3; maybe low, not absent |
| [[GPR89B]] | C | RGS10 activity lowers GPR89B's level | lines that do not express RGS10 (4) vs lines expressing it (46) | 1.39× higher at baseline in the lines without RGS10 | 0.092 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HOMER3, ARHGEF17, CHST3; maybe low, not absent |
| [[LIG4]] | C | RGS10 activity lowers LIG4's level | lines that do not express RGS10 (4) vs lines expressing it (46) | 1.61× higher at baseline in the lines without RGS10 | 0.099 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: HOMER3, ARHGEF17, CHST3; maybe low, not absent |

## Where it sits

- **Module**: [[Module 077]]; 59 genes; this gene is in the **+** arm (projection on the module's main direction 0.751). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.44).
- **Nodal map** (x, y) = (-0.5, 1.9); signed map (-40.8, -3.8). **Vector** length 82.9, 19.2% of its response variance represented; |z| ≥ 3 in 685 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.9 | +5.7 |
|  | [[Panobinostat (drug)]] 0.05 µM |  | +5.3 | +4.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +3.9 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +4.6 | +4.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~20% of this change | +3.8 | +4.3 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.6 | +2.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.1 | +2.8 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +1.4 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.0 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM |  | -5.3 | -15.1 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -5.0 | -8.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | -4.4 | -7.7 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -4.2 | -3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.0 | -3.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -3.6 |
|  | [[Belumosudil (drug)]] 5 µM |  | -2.0 | -0.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -2.4 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -1.9 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | regulator of G protein signaling 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q26.11 — chr10:119,499,817-119,542,719 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Regulators of G-protein signaling |
| Reactome | 3 pathways, smallest: G alpha (i) signalling events; GPCR downstream signalling; Signaling by GPCR |
| Matched by | ensembl_id |

**Function**, from UniProt [O43665](https://www.uniprot.org/uniprotkb/O43665) (Regulator of G protein signaling 10):

> Regulates G protein-coupled receptor signaling cascades, including signaling downstream of the muscarinic acetylcholine receptor CHRM2. Inhibits signal transduction by increasing the GTPase activity of G protein alpha subunits, thereby driving them into their inactive GDP-bound form. Modulates the activity of potassium channels that are activated in response to CHRM2 signaling. Activity on GNAZ is inhibited by palmitoylation of the G protein.

**Summary**, from NCBI Gene [6001](https://www.ncbi.nlm.nih.gov/gene/6001):

> Regulator of G protein signaling (RGS) family members are regulatory molecules that act as GTPase activating proteins (GAPs) for G alpha subunits of heterotrimeric G proteins. RGS proteins are able to deactivate G protein subunits of the Gi alpha, Go alpha and Gq alpha subtypes. They drive G proteins into their inactive GDP-bound forms. Regulator of G protein signaling 10 belongs to this family. All RGS proteins share a conserved 120-amino acid sequence termed the RGS domain. This protein …

**Accessions** — [HGNC:9992](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9992) · Entrez [6001](https://www.ncbi.nlm.nih.gov/gene/6001) · UniProt [O43665](https://www.uniprot.org/uniprotkb/O43665) · Ensembl [ENSG00000148908](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000148908)

## Data

Gene col 7325: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7325); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7325, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7325]; `tensor/DDL_lfc|DDL_z.npy` [7325]; `embed/gene_vectors.npy` [7325]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7325 or target_col == 7325). Every well: [[RGS10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RGS10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
