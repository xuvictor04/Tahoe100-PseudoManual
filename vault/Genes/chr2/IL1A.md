---
symbol: "IL1A"
type: "gene"
col: 3612
ensembl_id: "ENSG00000115008"
name: "interleukin 1 alpha"
location: "2q14.1"
module: 112
arm: "+"
pooled_cpm: 8.74
n_lines_expressing: 23
n_dd_up: 22
n_dd_down: 17
n_dd_up_clean: 16
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 19
direction_downstream: 25
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# IL1A

*interleukin 1 alpha* — 2q14.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 4.43× (z +16.9, q 0e+00, up in 16 of 19 measured lines).
> Pooled over the cell lines (median), lowered significantly by 17 drug-doses (none with an alert); the strongest is [[Clobetasol propionate (drug)]] 0.5 µM: 0.551× (z -4.9, q 6e-04, down in 13 of 18 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TRAF1]] (+0.75, fdr 7e-06), [[CSF2]] (+0.74, fdr 7e-06), [[CXCL8]] (+0.71, fdr 7e-06).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 19 arrows point to it, the strongest [[CXCL3]] → it (grade B ⚠); 25 go from it, the strongest it → [[CXCL3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 22 in all, 6 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3612.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **4.43×** | +16.9 | 0e+00 | 16/19 (CFPAC-1, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **4.43×** | +11.8 | 2e-29 | 17/19 (J82, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.72×** | +11.5 | 4e-28 | 18/20 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **3.24×** | +9.7 | 5e-20 | 17/18 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **8.88×** | +9.4 | 7e-19 | 18/19 (Panc 03.27, J82, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.41×** | +7.3 | 4e-11 | 15/18 (CFPAC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.03×** | +5.8 | 4e-07 | 17/20 (NCI-H460, HS-578T, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +5.1 | 3e-05 | 9/18 (NCI-H1573, AsPC-1, …) | top dose only | cell-cycle shift (explains ~17% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.93×** | +5.0 | 4e-05 | 1/16 (J82) | inconsistent across doses | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.76×** | +4.7 | 2e-04 | 12/20 (AsPC-1, NCI-H2347, …) | inconsistent across doses | cell-cycle shift (explains ~18% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.74×** | +4.4 | 5e-04 | 5/17 (NCI-H2347, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.68×** | +4.3 | 8e-04 | 2/17 (J82, AsPC-1) | inconsistent across doses | cell-cycle shift (explains ~23% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +4.0 | 0.002 | 1/16 (HS-578T) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.49×** | +3.9 | 0.004 | 10/18 (Panc 03.27, HOP62, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | **1.59×** | +3.8 | 0.005 | 11/20 (NCI-H2347, SW 900, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 0.5 µM |  | **1.82×** | +3.5 | 0.015 | 7/18 (A-172, HOP62, …) | rises with dose | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Gemcitabine (drug)]] 0.5 µM |  | **1.49×** | +3.3 | 0.032 | 6/21 (J82, NCI-H460, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.052 | 5/19 (AsPC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.30×** | +3.0 | 0.071 | 8/20 (NCI-H460, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Cyclosporin A (drug)]] 5 µM |  | **1.43×** | +2.9 | 0.086 | 3/20 (A549, CFPAC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 1 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3612.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.551×** | -4.9 | 6e-04 | 13/18 (NCI-H1792, A-172, …) | two highest doses |  |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.560×** | -4.7 | 6e-04 | 10/18 (NCI-H1792, SW 900, …) | all doses, flat |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.593×** | -4.3 | 0.004 | 16/20 (A549, LOX-IMVI, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **0.592×** | -3.8 | 0.019 | 8/22 (J82, A549, …) | all doses, flat | cell-cycle shift (explains ~7% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.673×** | -3.7 | 0.021 | 12/19 (Hs 766T, A549, …) | all doses, flat | noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.637×** | -3.7 | 0.021 | 8/19 (NCI-H1792, SW 900, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **0.723×** | -3.6 | 0.023 | 11/20 (RPMI-7951, SW 900, …) | top dose only |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.648×** | -3.5 | 0.028 | 12/18 (HS-578T, NCI-H1792, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.732×** | -3.5 | 0.031 | 7/20 (J82, NCI-H1573, …) | all doses, flat |  |
| [[Darinaparsin (drug)]] 5 µM |  | **0.738×** | -3.4 | 0.033 | 7/20 (Panc 03.27, NCI-H460, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ipatasertib (drug)]] 5 µM |  | **0.458×** | -3.3 | 0.042 | 9/19 (SW 900, H4, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.893× | -3.3 | 0.044 | 2/22 (NCI-H1792, HOP62) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.465×** | -3.3 | 0.044 | 12/17 (A549, J82, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.659×** | -3.3 | 0.044 | 8/18 (A549, J82, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.664×** | -3.2 | 0.050 | 9/18 (CFPAC-1, Hs 766T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.681×** | -3.1 | 0.060 | 10/20 (LS 180, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.02 per unit of S-phase module lfc, +0.21 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3612. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 19.2 | 3 | 3 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 7.44× (z +13.1) | [[Dinaciclib (drug)]] 5 µM 0.0528× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 10.5 | 5 | 0 | [[Homoharringtonine (drug)]] 5 µM 34.2× (z +16.7) | — |
| [[NCI-H460 (line)]] | wt | 26.4 | 3 | 1 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 10.8× (z +12.9) | [[Dinaciclib (drug)]] 5 µM 0.189× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[CFPAC-1 (line)]] | alt | 19.5 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 38.1× (z +20.7) | — |
| [[Hs 766T (line)]] | wt | 11.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 22.8× (z +14.4) | — |
| [[HS-578T (line)]] | alt | 7.10 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 14.3× (z +11.0) | — |
| [[J82 (line)]] | alt | 23.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 15.2× (z +17.2) | — |
| [[Panc 03.27 (line)]] | alt | 31.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.1× (z +17.4) | — |
| [[A-172 (line)]] | wt | 12.0 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 16.9× (z +13.8) | — |
| [[A549 (line)]] | wt | 29.8 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.33× (z +9.3) | [[Dinaciclib (drug)]] 0.5 µM 0.112× (z -10.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 5.36 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 60.3× (z +18.5) | — |
| [[RPMI-7951 (line)]] | alt | 14.6 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 15.1× (z +9.4) | — |
| [[LOX-IMVI (line)]] | wt | 34.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 37.3× (z +8.6) | — |
| [[LS 180 (line)]] | wt | 16.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0791× (z -10.5) |
| [[NCI-H1792 (line)]] | alt | 36.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.275× (z -8.5) |
| [[A-427 (line)]] | wt | 0.608 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 1.18 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 1.50 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.652 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.874 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.845 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.21 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.02 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 8.69 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.74 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.852 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.99 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.19 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.27 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.849 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.39 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.678 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 55.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.865 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.817 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 0.812 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.750 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.845 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.909 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 8.72 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.65 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.979 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.788 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3612), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TRAF1]] | +0.75 | +0.71 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 485 |
| [[CSF2]] | +0.74 | +0.67 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 997 |
| [[CXCL8]] | +0.71 | +0.62 / +0.75 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 974 |
| [[IL1B]] | +0.70 | +0.58 / +0.75 | both halves | 7e-06 | same gene group; pathway: HALLMARK_APOPTOSIS; STRING 999; ⚠ same locus (45.3 kb, same strand: neighbours can correlate without regulation) |
| [[IER3]] | +0.69 | +0.68 / +0.75 | both halves | 7e-06 | pathway: HALLMARK_APOPTOSIS |
| [[G0S2]] | +0.69 | +0.66 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB |
| [[PTGS2]] | +0.69 | +0.58 / +0.73 | both halves | 8e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 823 |
| [[LIF]] | +0.65 | +0.64 / +0.64 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 794 |
| [[IRAK2]] | +0.65 | +0.61 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 876 |
| [[NFKBIE]] | +0.64 | +0.62 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_TNFA_SIGNALING_VIA_NFKB; STRING 453 |
| [[PPP4R4]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[GATM]] | +0.63 | +0.56 / +0.65 | both halves | 1e-05 |  |
| [[MIR155HG]] | +0.63 | +0.54 / +0.64 | both halves | 1e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*19 arrows, 19 of them with an alert ⚠; grade A 0, B 6, C 13. Shown: the 12 strongest; 7 more arrows (7 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL3]] | B | CXCL3 activity raises IL1A's level | lines that do not express CXCL3 (14) vs lines expressing it (36) | 3.54× lower at baseline in the lines without CXCL3 | 0.001 | ⚠ within organs, on part of the lines; also absent: MGLL, SPTLC3, PCED1B |
| [[SOX9]] | B | SOX9 activity raises IL1A's level | lines that do not express SOX9 (8) vs lines expressing it (42) | 3.34× lower at baseline in the lines without SOX9 | 0.008 | ⚠ within organs, on part of the lines; also absent: CXCL3, SMOX, TRIM38 |
| [[DUSP10]] | B | DUSP10 activity raises IL1A's level | lines that do not express DUSP10 (11) vs lines expressing it (39) | 3.50× lower at baseline in the lines without DUSP10 | 0.030 | ⚠ within organs, on part of the lines; also absent: GLRX, GBP2, TMEM92-AS1; maybe low, not absent |
| [[NEURL3]] | B | NEURL3 activity raises IL1A's level | lines that do not express NEURL3 (13) vs lines expressing it (37) | 2.54× lower at baseline in the lines without NEURL3 | 0.058 | ⚠ within organs, on part of the lines; also absent: SAA2, SAA4, VSIR; maybe low, not absent |
| [[GEM]] | B | GEM activity raises IL1A's level | lines that do not express GEM (9) vs lines expressing it (41) | 3.30× lower at baseline in the lines without GEM | 0.063 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ALCAM, SHB |
| [[VDR]] | B | VDR activity raises IL1A's level | lines that do not express VDR (8) vs lines expressing it (42) | 2.43× lower at baseline in the lines without VDR | 0.090 | ⚠ within organs, on part of the lines; also absent: TGFBR2, TRIB1, MET |
| [[IL1B]] | C | IL1B activity raises IL1A's level | lines that do not express IL1B (30) vs lines expressing it (20) | 4.29× lower at baseline in the lines without IL1B | 6e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: IL7R, ADAMTS12, EDNRA; co-absent with the target |
| [[BMP2]] | C | BMP2 activity raises IL1A's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 3.01× lower at baseline in the lines without BMP2 | 0.007 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44; co-absent with the target |
| [[ITGA1]] | C | ITGA1 activity raises IL1A's level | lines that do not express ITGA1 (18) vs lines expressing it (32) | 3.00× lower at baseline in the lines without ITGA1 | 0.010 | ⚠ within organs, on part of the lines; co-occurs with KMT2D; also absent: PLOD2, LINC01583, LINC00973; co-absent with the target |
| [[SERPINB7]] | C | SERPINB7 activity raises IL1A's level | lines that do not express SERPINB7 (24) vs lines expressing it (26) | 3.64× lower at baseline in the lines without SERPINB7 | 0.011 | ⚠ within organs, on part of the lines; also absent: BASP1, DNAH11, SLC16A7; co-absent with the target |
| [[IL2RG]] | C | IL2RG activity raises IL1A's level | lines that do not express IL2RG (25) vs lines expressing it (25) | 2.46× lower at baseline in the lines without IL2RG | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000285471, TMPRSS3, ENSG00000276850; co-absent with the target |
| [[MIR155HG]] | C | MIR155HG activity raises IL1A's level | lines that do not express MIR155HG (28) vs lines expressing it (22) | 3.32× lower at baseline in the lines without MIR155HG | 0.013 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA; co-absent with the target |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 15, C 10. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CXCL3]] | B | IL1A activity raises CXCL3's level | lines that do not express IL1A (27) vs lines expressing it (23) | 2.68× lower at baseline in the lines without IL1A | 0.007 | ⚠ within organs, on part of the lines; also absent: EDNRA, ABI3BP, PLAT |
| [[SOX9]] | B | IL1A activity raises SOX9's level | lines that do not express IL1A (27) vs lines expressing it (23) | 1.66× lower at baseline in the lines without IL1A | 0.010 | ⚠ within organs, on part of the lines; also absent: EDNRA, ABI3BP, PLAT |
| [[SHB]] | B | IL1A activity raises SHB's level | lines that do not express IL1A (27) vs lines expressing it (23) | 1.48× lower at baseline in the lines without IL1A | 0.012 | ⚠ within organs, on part of the lines; also absent: EDNRA, ABI3BP, PLAT |
| [[GEM]] | B | IL1A activity raises GEM's level | lines that do not express IL1A (27) vs lines expressing it (23) | 2.15× lower at baseline in the lines without IL1A | 0.013 | ⚠ within organs, on part of the lines; also absent: EDNRA, ABI3BP, PLAT |
| [[HMGN2P46]] | B | IL1A activity raises HMGN2P46's level | lines that do not express IL1A (27) vs lines expressing it (23) | 3.39× lower at baseline in the lines without IL1A | 0.027 | ⚠ within organs, on part of the lines; also absent: EDNRA, ABI3BP, PLAT |
| [[EHD1]] | B | IL1A activity raises EHD1's level | lines that do not express IL1A (27) vs lines expressing it (23) | 1.41× lower at baseline in the lines without IL1A | 0.041 | ⚠ within organs, on part of the lines; also absent: EDNRA, ABI3BP, PLAT |
| [[TNFRSF10B]] | B | IL1A activity raises TNFRSF10B's level | lines that do not express IL1A (27) vs lines expressing it (23) | 1.22× lower at baseline in the lines without IL1A | 0.060 | ⚠ within organs, on part of the lines; also absent: EDNRA, ABI3BP, PLAT |
| [[RIPK2]] | B | IL1A activity raises RIPK2's level | lines that do not express IL1A (27) vs lines expressing it (23) | 1.57× lower at baseline in the lines without IL1A | 0.063 | ⚠ within organs, on part of the lines; also absent: EDNRA, ABI3BP, PLAT |
| [[CD82]] | B | IL1A activity raises CD82's level | lines that do not express IL1A (27) vs lines expressing it (23) | 1.83× lower at baseline in the lines without IL1A | 0.074 | ⚠ within organs, on part of the lines; also absent: EDNRA, ABI3BP, PLAT |
| [[BHLHE40]] | B | IL1A activity raises BHLHE40's level | lines that do not express IL1A (27) vs lines expressing it (23) | 1.61× lower at baseline in the lines without IL1A | 0.078 | ⚠ within organs, on part of the lines; also absent: EDNRA, ABI3BP, PLAT |
| [[NEURL3]] | B | IL1A activity raises NEURL3's level | lines that do not express IL1A (27) vs lines expressing it (23) | 1.40× lower at baseline in the lines without IL1A | 0.083 | ⚠ within organs, on part of the lines; also absent: EDNRA, ABI3BP, PLAT |
| [[NINJ1]] | B | IL1A activity raises NINJ1's level | lines that do not express IL1A (27) vs lines expressing it (23) | 1.82× lower at baseline in the lines without IL1A | 0.093 | ⚠ within organs, on part of the lines; also absent: EDNRA, ABI3BP, PLAT |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.819). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (30.7, 1.5); signed map (41.3, 12.2). **Vector** length 79.6, 26.3% of its response variance represented; |z| ≥ 3 in 667 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *KRAS signaling up* (hallmark, mean cos +0.65 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +6.8 | +11.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.5 | +9.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +4.5 | +16.9 |
|  | [[Harringtonine (drug)]] 5 µM |  | +3.4 | +11.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.4 | +2.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +2.6 | +3.8 |
|  | [[Amsacrine (drug)]] 5 µM |  | +2.1 | +1.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +1.3 |
|  | [[Verteporfin (drug)]] 5 µM |  | +1.4 | +2.4 |
| fall | [[NG25 (drug)]] 5 µM |  | -3.1 | -3.3 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.4 | +0.4 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.4 | +1.0 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -2.3 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.3 | -3.7 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.2 | -4.7 |
|  | [[Budesonide (drug)]] 5 µM |  | -2.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | interleukin 1 alpha |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.1 — chr2:112,773,925-112,784,493 (-) |
| Ensembl biotype | protein_coding |
| Also known as | IL1F1, IL-1A, IL1-ALPHA; previously IL1 |
| Gene groups (HGNC) | Interleukins; Interleukin 1 family |
| Hallmark sets | INFLAMMATORY_RESPONSE, APOPTOSIS, TNFA_SIGNALING_VIA_NFKB, P53_PATHWAY |
| Reactome | 18 pathways, smallest: Interleukin-1 processing; Cell recruitment (pro-inflammatory response); Purinergic signaling in leishmaniasis infection |
| Matched by | ensembl_id |

**Function**, from UniProt [P01583](https://www.uniprot.org/uniprotkb/P01583) (Interleukin-1 alpha):

> Cytokine constitutively present intracellularly in nearly all resting non-hematopoietic cells that plays an important role in inflammation and bridges the innate and adaptive immune systems. After binding to its receptor IL1R1 together with its accessory protein IL1RAP, forms the high affinity interleukin-1 receptor complex. Signaling involves the recruitment of adapter molecules such as MYD88, IRAK1 or IRAK4. In turn, mediates the activation of NF-kappa-B and the three MAPK pathways p38, …

**Summary**, from NCBI Gene [3552](https://www.ncbi.nlm.nih.gov/gene/3552):

> The protein encoded by this gene is a member of the interleukin 1 cytokine family. This cytokine is a pleiotropic cytokine involved in various immune responses, inflammatory processes, and hematopoiesis. This cytokine is produced by monocytes and macrophages as a proprotein, which is proteolytically processed and released in response to cell injury, and thus induces apoptosis. This gene and eight other interleukin 1 family genes form a cytokine gene cluster on chromosome 2. It has been …

**Accessions** — [HGNC:5991](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5991) · Entrez [3552](https://www.ncbi.nlm.nih.gov/gene/3552) · UniProt [P01583](https://www.uniprot.org/uniprotkb/P01583) · Ensembl [ENSG00000115008](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000115008)

## Data

Gene col 3612: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3612); `tables/drug_effects.parquet` (40 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3612, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3612]; `tensor/DDL_lfc|DDL_z.npy` [3612]; `embed/gene_vectors.npy` [3612]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3612 or target_col == 3612). Every well: [[IL1A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IL1A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
