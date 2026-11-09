---
symbol: "APOL3"
type: "gene"
col: 4872
ensembl_id: "ENSG00000128284"
name: "apolipoprotein L3"
location: "22q12.3"
module: 70
arm: "+"
pooled_cpm: 5.71
n_lines_expressing: 36
n_dd_up: 26
n_dd_down: 21
n_dd_up_clean: 22
n_dd_down_clean: 18
in_vector_space: true
direction_upstream: 29
direction_downstream: 40
tags: ["gene", "module/070"]
generated_by: "tahoemap"
---

# APOL3

*apolipoprotein L3* — 22q12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (4 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.25× (z +7.5, q 5e-11, up in 19 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 21 drug-doses (3 with an alert ⚠); the strongest is [[Daptomycin (drug)]] 0.5 µM: 0.532× (z -5.8, q 1e-06, down in 12 of 30 measured lines) ⚠ unreliable plate only. The strongest without an alert is [[Panobinostat (drug)]] 5 µM: 0.532× (z -5.8, q 1e-06, down in 19 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GBP4]] (+0.85, fdr 7e-06), [[IDO1]] (+0.77, fdr 7e-06), [[SLC15A3]] (+0.77, fdr 7e-06).
> It is in [[Module 070]], a single-armed module (interferon gamma response).
> Probable direction (from the cell lines, not proof of direct regulation): 29 arrows point to it, the strongest [[FYB1]] → it (grade B ⚠); 40 go from it, the strongest it → [[APOL2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4872.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.25×** | +7.5 | 5e-11 | 19/32 (HS-578T, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.77×** | +5.0 | 1e-04 | 14/26 (NCI-H460, Hs 766T, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.70×** | +4.7 | 5e-04 | 1/10 (PANC-1) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.63×** | +4.5 | 0.001 | 7/18 (A-172, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.61×** | +4.4 | 0.001 | 10/33 (CFPAC-1, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.39×** | +4.3 | 0.001 | 11/31 (HT-29, Hs 766T, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.54×** | +4.3 | 0.001 | 7/32 (CFPAC-1, Hs 766T, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.46×** | +4.2 | 0.002 | 10/31 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.56×** | +4.1 | 0.003 | 11/30 (HS-578T, A-172, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.58×** | +3.9 | 0.005 | 7/23 (HS-578T, A498, …) | inconsistent across doses | low cells (technical?) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.40×** | +3.9 | 0.005 | 8/31 (Hs 766T, CFPAC-1, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Amsacrine (drug)]] 5 µM |  | **1.34×** | +3.9 | 0.005 | 6/32 (A549, HEC-1-A, …) | rises with dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.38×** | +3.8 | 0.006 | 10/32 (Hs 766T, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.51×** | +3.6 | 0.013 | 5/29 (HEC-1-A, Hs 766T, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.49×** | +3.6 | 0.013 | 8/30 (Hs 766T, A549, …) | rises with dose |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.47×** | +3.6 | 0.013 | 9/29 (NCI-H1792, SNU-423, …) | rises with dose |  |
| [[Bimiralisib (drug)]] 0.5 µM |  | **1.66×** | +3.3 | 0.029 | 2/25 (HS-578T, CFPAC-1) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 3 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4872.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **0.532×** | -5.8 | 1e-06 | 12/30 (SW 900, HS-578T, …) | two highest doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.532×** | -5.8 | 1e-06 | 19/32 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.532×** | -5.8 | 1e-06 | 14/32 (SK-MEL-2, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.567×** | -5.0 | 8e-05 | 14/32 (HS-578T, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~16% here); composition shift |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.580×** | -5.0 | 8e-05 | 14/31 (LoVo, A549, …) | top dose only |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.408×** | -4.3 | 0.002 | 13/30 (Hs 766T, HS-578T, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~8% here); composition shift; noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM |  | **0.629×** | -4.2 | 0.002 | 14/31 (HS-578T, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.736×** | -3.9 | 0.006 | 14/30 (LoVo, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.658×** | -3.8 | 0.008 | 13/26 (NCI-H1792, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.663×** | -3.8 | 0.010 | 14/31 (LoVo, COLO 205, …) | inconsistent across doses | cell-cycle shift (explains ~17% here) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.676×** | -3.6 | 0.018 | 10/30 (NCI-H1573, Hs 766T, …) | all doses, flat |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.680×** | -3.5 | 0.021 | 11/32 (HT-29, H4, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.668×** | -3.5 | 0.022 | 14/29 (SK-MEL-2, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.686×** | -3.4 | 0.023 | 11/31 (Hs 766T, Panc 03.27, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.687×** | -3.4 | 0.023 | 8/32 (Hs 766T, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.709×** | -3.1 | 0.058 | 10/30 (PANC-1, H4, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.711×** | -3.1 | 0.059 | 15/30 (RPMI-7951, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.09 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4872. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 52.7 | 0 | 5 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -17.4) ⚠ cell-cycle shift, explains ~42% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.255× (z -9.0) |
| [[A-172 (line)]] | wt | 11.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0170× (z -26.4) ⚠ cell-cycle shift, explains ~42% of this change |
| [[Hs 766T (line)]] | wt | 48.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0750× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 2.84 | 0 | 1 | — | [[Pexidartinib (hydrochloride) (drug)]] 5 µM 0.0415× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 6.38 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.0389× (z -11.4) |
| [[SW 1088 (line)]] | alt | 59.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -8.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[A-427 (line)]] | wt | 0.480 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.66 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.91 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.650 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.90 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.67 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.01 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 16.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.58 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 4.82 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 1.48 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 0.877 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.50 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 8.47 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 0.682 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.84 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.87 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.641 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.563 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 3.14 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 3.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 0.770 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.97 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.662 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 1.45 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.80 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.33 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.23 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.659 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.38 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4872), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GBP4]] | +0.85 | +0.82 / +0.83 | both halves | 7e-06 | STRING 485 |
| [[IDO1]] | +0.77 | +0.70 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[SLC15A3]] | +0.77 | +0.70 / +0.76 | both halves | 7e-06 |  |
| [[CD5L]] | +0.74 | +0.58 / +0.75 | both halves | 7e-06 | **novel candidate** |
| [[IL15RA]] | +0.73 | +0.63 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[PSMB9]] | +0.73 | +0.71 / +0.71 | both halves | 7e-06 |  |
| [[TRANK1]] | +0.73 | +0.64 / +0.75 | both halves | 7e-06 |  |
| [[SAMD9L]] | +0.72 | +0.68 / +0.71 | both halves | 7e-06 |  |
| [[APOL6]] | +0.72 | +0.63 / +0.72 | both halves | 7e-06 | same gene group; STRING 447 |
| [[LINC02100]] | +0.71 | +0.69 / +0.73 | both halves | 7e-06 |  |
| [[TNFSF10]] | +0.70 | +0.59 / +0.75 | both halves | 7e-06 |  |
| [[FLT3LG]] | +0.70 | +0.63 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*29 arrows, 29 of them with an alert ⚠; grade A 0, B 25, C 4. Shown: the 12 strongest; 17 more arrows (17 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FYB1]] | B | FYB1 activity raises APOL3's level | lines that do not express FYB1 (32) vs lines expressing it (18) | 2.68× lower at baseline in the lines without FYB1 | 0.003 | ⚠ within organs, on part of the lines; also absent: AMPH, IRAG2, ENSG00000266450 |
| [[PLAAT4]] | B | PLAAT4 activity raises APOL3's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 2.61× lower at baseline in the lines without PLAAT4 | 0.009 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[MMP13]] | B | MMP13 activity raises APOL3's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 2.19× lower at baseline in the lines without MMP13 | 0.012 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[TNFAIP2]] | B | TNFAIP2 activity raises APOL3's level | lines that do not express TNFAIP2 (22) vs lines expressing it (28) | 2.32× lower at baseline in the lines without TNFAIP2 | 0.020 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, LINC02057, DEPP1 |
| [[EPSTI1]] | B | EPSTI1 activity raises APOL3's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 2.38× lower at baseline in the lines without EPSTI1 | 0.021 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[RSAD2]] | B | RSAD2 activity raises APOL3's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 2.17× lower at baseline in the lines without RSAD2 | 0.024 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[CTSS]] | B | CTSS activity raises APOL3's level | lines that do not express CTSS (15) vs lines expressing it (35) | 2.60× lower at baseline in the lines without CTSS | 0.029 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[GBP1]] | B | GBP1 activity raises APOL3's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 2.63× lower at baseline in the lines without GBP1 | 0.029 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[IL15]] | B | IL15 activity raises APOL3's level | lines that do not express IL15 (10) vs lines expressing it (40) | 2.51× lower at baseline in the lines without IL15 | 0.030 | ⚠ within organs, on part of the lines; also absent: TGFBR2, ITGA3, PSORS1C1; maybe low, not absent |
| [[GPRC5B]] | B | GPRC5B activity raises APOL3's level | lines that do not express GPRC5B (27) vs lines expressing it (23) | 2.46× lower at baseline in the lines without GPRC5B | 0.040 | ⚠ within organs, on part of the lines; also absent: PALMD, FYB1, AK5 |
| [[IFI44]] | B | IFI44 activity raises APOL3's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 2.35× lower at baseline in the lines without IFI44 | 0.043 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[APOL6]] | B | APOL6 activity raises APOL3's level | lines that do not express APOL6 (6) vs lines expressing it (44) | 2.90× lower at baseline in the lines without APOL6 | 0.046 | ⚠ within organs, on part of the lines; also absent: KLF4, S100A13, LGALS3BP; maybe low, not absent |

### Downstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 36, C 4. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[APOL2]] | B | APOL3 activity raises APOL2's level | lines that do not express APOL3 (14) vs lines expressing it (36) | 2.19× lower at baseline in the lines without APOL3 | 0.005 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |
| [[APOL6]] | B | APOL3 activity raises APOL6's level | lines that do not express APOL3 (14) vs lines expressing it (36) | 2.97× lower at baseline in the lines without APOL3 | 0.007 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |
| [[SP140L]] | B | APOL3 activity raises SP140L's level | lines that do not express APOL3 (14) vs lines expressing it (36) | 2.26× lower at baseline in the lines without APOL3 | 0.008 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |
| [[RSAD2]] | B | APOL3 activity raises RSAD2's level | lines that do not express APOL3 (14) vs lines expressing it (36) | 3.41× lower at baseline in the lines without APOL3 | 0.010 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |
| [[GBP2]] | B | APOL3 activity raises GBP2's level | lines that do not express APOL3 (14) vs lines expressing it (36) | 4.29× lower at baseline in the lines without APOL3 | 0.010 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |
| [[SAMD9]] | B | APOL3 activity raises SAMD9's level | lines that do not express APOL3 (14) vs lines expressing it (36) | 3.34× lower at baseline in the lines without APOL3 | 0.016 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |
| [[IFI44]] | B | APOL3 activity raises IFI44's level | lines that do not express APOL3 (14) vs lines expressing it (36) | 2.74× lower at baseline in the lines without APOL3 | 0.020 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |
| [[IL15]] | B | APOL3 activity raises IL15's level | lines that do not express APOL3 (14) vs lines expressing it (36) | 2.70× lower at baseline in the lines without APOL3 | 0.022 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |
| [[OASL]] | B | APOL3 activity raises OASL's level | lines that do not express APOL3 (14) vs lines expressing it (36) | 2.50× lower at baseline in the lines without APOL3 | 0.023 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |
| [[NLRC5]] | B | APOL3 activity raises NLRC5's level | lines that do not express APOL3 (14) vs lines expressing it (36) | 1.91× lower at baseline in the lines without APOL3 | 0.028 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |
| [[TENT5A]] | B | APOL3 activity raises TENT5A's level | lines that do not express APOL3 (14) vs lines expressing it (36) | 2.82× lower at baseline in the lines without APOL3 | 0.034 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |
| [[CASP7]] | B | APOL3 activity raises CASP7's level | lines that do not express APOL3 (14) vs lines expressing it (36) | 1.54× lower at baseline in the lines without APOL3 | 0.036 | ⚠ within organs, on part of the lines; also absent: SAMD9L, APOL1, GBP4 |

## Where it sits

- **Module**: [[Module 070]] — interferon gamma response; 70 genes; every member is in the + arm (projection on the module's main direction 0.813). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (45.1, 51.8); signed map (60.9, 30.0). **Vector** length 71.9, 17.0% of its response variance represented; |z| ≥ 3 in 757 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.59 to 25); *interferon alpha response* (hallmark, mean cos +0.58 to 19); *Antigen processing-Cross presentation* (reactome, mean cos +0.57 to 14).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +4.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | +3.3 | +7.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.1 | +1.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.0 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.0 | +3.1 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.8 | +5.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.3 | +3.6 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -2.5 | -3.9 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.5 | -3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.3 | -5.0 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -2.2 | -3.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.2 | -2.5 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.2 | -3.6 |

## What is on record

|  |  |
|---|---|
| Name | apolipoprotein L3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q12.3 — chr22:36,140,329-36,166,177 (-) |
| Ensembl biotype | protein_coding |
| Also known as | CG12-1, APOLIII |
| Gene groups (HGNC) | Apolipoproteins |
| Matched by | ensembl_id |

**Function**, from UniProt [O95236](https://www.uniprot.org/uniprotkb/O95236) (Apolipoprotein L3):

> May affect the movement of lipids in the cytoplasm or allow the binding of lipids to organelles.

**Summary**, from NCBI Gene [80833](https://www.ncbi.nlm.nih.gov/gene/80833):

> This gene is a member of the apolipoprotein L gene family, and it is present in a cluster with other family members on chromosome 22. The encoded protein is found in the cytoplasm, where it may affect the movement of lipids, including cholesterol, and/or allow the binding of lipids to organelles. In addition, expression of this gene is up-regulated by tumor necrosis factor-alpha in endothelial cells lining the normal and atherosclerotic iliac artery and aorta. Alternative splicing results in …

**Accessions** — [HGNC:14868](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14868) · Entrez [80833](https://www.ncbi.nlm.nih.gov/gene/80833) · UniProt [O95236](https://www.uniprot.org/uniprotkb/O95236) · Ensembl [ENSG00000128284](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000128284)

## Data

Gene col 4872: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4872); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4872, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4872]; `tensor/DDL_lfc|DDL_z.npy` [4872]; `embed/gene_vectors.npy` [4872]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4872 or target_col == 4872). Every well: [[APOL3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/APOL3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
