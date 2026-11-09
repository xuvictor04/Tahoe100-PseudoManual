---
symbol: "CYP1B1-AS1"
type: "gene"
col: 13880
ensembl_id: "ENSG00000232973"
name: "CYP1B1 antisense RNA 1"
location: "2p22.2"
module: 10
arm: "+"
pooled_cpm: 9.41
n_lines_expressing: 36
n_dd_up: 32
n_dd_down: 9
n_dd_up_clean: 27
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 9
direction_downstream: 14
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# CYP1B1-AS1

*CYP1B1 antisense RNA 1* — 2p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 32 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.91× (z +13.4, q 5e-38, up in 24 of 32 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.554× (z -5.2, q 9e-05, down in 19 of 33 measured lines).
> Its strongest partners by |cos| (83 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 19 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RMDN2-AS1]] (+0.76, fdr 7e-06, ⚠ same locus), [[CYP1B1]] (+0.74, fdr 7e-06, ⚠ same locus), [[ARHGAP15]] (+0.69, fdr 1e-05), [[TENM3-AS1]] (+0.69, fdr 1e-05), [[PSMG3-AS1]] (+0.65, fdr 4e-05); moves opposite to [[ECI2]] (-0.62, fdr 1e-04), [[RMND1]] (-0.59, fdr 1e-04), [[LCMT1]] (-0.57, fdr 5e-04).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[CYP1B1]] → it (grade B ⚠); 14 go from it, the strongest it → [[LINC02615]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 32 in all, 5 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 32 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13880.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.91×** | +13.4 | 5e-38 | 24/32 (A498, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.64×** | +12.2 | 1e-31 | 23/30 (HS-578T, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.54×** | +7.6 | 5e-12 | 5/16 (LoVo, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.32×** | +7.2 | 1e-10 | 13/27 (A498, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.12×** | +6.4 | 2e-08 | 3/12 (HS-578T, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Gemcitabine (drug)]] 0.05 µM |  | **1.60×** | +5.5 | 3e-06 | 22/33 (HT-29, CFPAC-1, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.84×** | +5.4 | 6e-06 | 7/20 (LoVo, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.80×** | +5.2 | 1e-05 | 12/27 (HS-578T, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD-7648 (drug)]] 5 µM |  | **2.98×** | +5.1 | 3e-05 | 16/23 (NCI-H23, HOP62, …) | rises with dose | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.66×** | +4.3 | 1e-03 | 12/31 (NCI-H23, A-427, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +4.2 | 0.002 | 7/30 (HEC-1-A, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Elimusertib hydrochloride (drug)]] 5 µM | ⚠ toxic | **2.43×** | +4.1 | 0.002 | 9/21 (NCI-H23, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Menadione (drug)]] 5 µM |  | **1.62×** | +4.1 | 0.002 | 14/29 (LS 180, CFPAC-1, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.59×** | +4.1 | 0.002 | 8/33 (A-427, HOP62, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +4.1 | 0.002 | 13/34 (HOP62, A498, …) | rises with dose |  |
| [[AZD-7648 (drug)]] 0.5 µM |  | **2.01×** | +4.0 | 0.002 | 9/31 (HOP62, HT-29, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.37×** | +3.9 | 0.003 | 10/34 (A-172, A498, …) | top dose only |  |
| [[Lucanthone (drug)]] 5 µM |  | **1.54×** | +3.7 | 0.008 | 8/33 (BT-474, HT-29, …) | top dose only | position effect removed |
| [[Gemcitabine (drug)]] 5 µM |  | **1.71×** | +3.5 | 0.014 | 6/29 (NCI-H1573, LS 180, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13880.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.554×** | -5.2 | 9e-05 | 19/33 (PANC-1, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.556×** | -4.9 | 2e-04 | 20/33 (PANC-1, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.580×** | -4.8 | 2e-04 | 16/33 (NCI-H460, HT-29, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.605×** | -4.5 | 0.001 | 16/33 (HT-29, NCI-H460, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.614×** | -4.3 | 0.002 | 16/33 (PANC-1, HT-29, …) | two highest doses | cell-cycle shift (explains ~25% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.759×** | -3.5 | 0.048 | 18/33 (HT-29, NCI-H460, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.688×** | -3.3 | 0.071 | 16/33 (PANC-1, BT-474, …) | rises with dose | composition shift |
| [[Rimonabant (drug)]] 5 µM |  | **0.771×** | -3.3 | 0.072 | 6/34 (hTERT-HPNE, SNU-1, …) | all doses, flat | position effect removed |
| [[Tomivosertib (drug)]] 5 µM |  | **0.496×** | -3.3 | 0.072 | 7/28 (NCI-H1792, HT-29, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | 0.518× | -3.1 | 0.13 | 7/32 (NCI-H460, PANC-1, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.25 per unit of S-phase module lfc, -0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13880. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 18.7 | 1 | 6 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.05× (z +8.9) | [[Digitoxin (drug)]] 5 µM 0.0946× (z -13.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.133× (z -11.3) |
| [[NCI-H23 (line)]] | alt | 18.8 | 3 (1 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 10.6× (z +14.7) | [[Digitoxin (drug)]] 5 µM 0.123× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~58% of this change |
| [[NCI-H460 (line)]] | wt | 50.9 | 1 | 3 (2 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.91× (z +10.1) | [[Ixazomib citrate (drug)]] 5 µM 0.166× (z -9.5) |
| [[HS-578T (line)]] | alt | 8.88 | 2 | 1 | [[Homoharringtonine (drug)]] 5 µM 22.2× (z +17.2) | [[Hydroxyurea (drug)]] 0.05 µM 0.0887× (z -8.8) |
| [[MIA PaCa-2 (line)]] | alt | 4.02 | 0 | 2 | — | [[Elagolix sodium (drug)]] 0.5 µM 0.0723× (z -9.2) |
| [[A-427 (line)]] | wt | 14.9 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.195× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A498 (line)]] | wt | 4.97 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.70× (z +10.8) | — |
| [[A549 (line)]] | wt | 5.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.85× (z +8.5) | — |
| [[BT-474 (line)]] | alt | 17.2 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0690× (z -9.6) ⚠ cell-cycle shift, explains ~42% of this change |
| [[H4 (line)]] | wt | 9.56 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +10.3) | — |
| [[HOP62 (line)]] | alt | 5.06 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 10.7× (z +10.4) | — |
| [[HT-29 (line)]] | alt | 16.8 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0961× (z -10.0) ⚠ unreliable plate only |
| [[LoVo (line)]] | wt | 7.68 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.37× (z +9.8) | — |
| [[SW 900 (line)]] | alt | 28.4 | 0 | 1 | — | [[Bortezomib (drug)]] 0.05 µM 0.0863× (z -9.7) |
| [[A-172 (line)]] | wt | 3.18 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.26 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.12 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.32 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.46 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.87 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.86 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 4.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.57 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.77 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.32 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.95 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 1.62 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 3.41 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 6.28 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 9.31 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 8.57 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 26.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 1.82 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.04 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.09 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.80 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 4.27 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 7.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.91 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.80 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 2.29 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13880), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 19 of them with an alert (⚠; 17 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RMDN2-AS1]] | +0.76 | +0.72 / +0.72 | both halves | 7e-06 | same gene group; ⚠ same locus (6.4 kb: neighbours can correlate without regulation) |
| [[CYP1B1]] | +0.74 | +0.72 / +0.73 | both halves | 7e-06 | ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[ARHGAP15]] | +0.69 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[TENM3-AS1]] | +0.69 | +0.69 / +0.49 | both halves | 1e-05 | same gene group |
| [[PSMG3-AS1]] | +0.65 | +0.69 / +0.42 | both halves | 4e-05 | same gene group |
| [[PPEF1]] | +0.65 | +0.67 / +0.53 | both halves | 1e-05 |  |
| [[LEKR1]] | +0.65 | +0.67 / +0.42 | both halves | 4e-05 |  |
| [[DENND5B-AS1]] | +0.64 | +0.67 / +0.42 | both halves | 4e-05 | same gene group |
| [[LINC01569]] | +0.64 | +0.74 / +0.45 | both halves | 3e-05 |  |
| [[LINC00886]] | +0.64 | +0.69 / +0.40 | both halves | 4e-05 |  |
| [[NOVA1]] | +0.63 | +0.60 / +0.57 | both halves | 9e-06 |  |
| [[TMEM202-AS1]] | +0.63 | +0.65 / +0.37 | both halves | 9e-05 | same gene group |
| [[DRAIC]] | +0.62 | +0.65 / +0.37 | both halves | 8e-05 |  |
| [[SEPTIN7-DT]] | +0.62 | +0.66 / +0.37 | both halves | 8e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ECI2]] | -0.62 | -0.60 / -0.32 | both halves | 1e-04 |  |
| [[RMND1]] | -0.59 | -0.36 / -0.44 | both halves | 1e-04 |  |
| [[LCMT1]] | -0.57 | -0.57 / -0.24 | both halves | 5e-04 |  |
| [[NBPF3]] | -0.57 | -0.57 / -0.25 | both halves | 4e-04 |  |
| [[SHQ1]] | -0.55 | -0.57 / -0.27 | both halves | 3e-04 |  |
| [[ORC3]] | -0.55 | -0.49 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 9, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CYP1B1]] | B | CYP1B1 activity raises CYP1B1-AS1's level | lines that do not express CYP1B1 (29) vs lines expressing it (21) | 3.42× lower at baseline in the lines without CYP1B1 | 4e-05 | ⚠ within organs, on part of the lines; also absent: EFEMP1, CCL2, ENSG00000282849 |
| [[BASP1-AS1]] | B | BASP1-AS1 activity raises CYP1B1-AS1's level | lines that do not express BASP1-AS1 (28) vs lines expressing it (22) | 2.14× lower at baseline in the lines without BASP1-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: ENSG00000282849, LRRC63, FGF14 |
| [[RMDN2-AS1]] | B | RMDN2-AS1 activity raises CYP1B1-AS1's level | lines that do not express RMDN2-AS1 (14) vs lines expressing it (36) | 2.58× lower at baseline in the lines without RMDN2-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: EHD3, PLOD2, ZNF43; maybe low, not absent |
| [[FLRT2]] | B | FLRT2 activity raises CYP1B1-AS1's level | lines that do not express FLRT2 (29) vs lines expressing it (21) | 1.90× lower at baseline in the lines without FLRT2 | 0.035 | ⚠ within organs, on part of the lines; also absent: KCNMA1, FLI1, IL13RA2 |
| [[TOP2A]] | B | TOP2A activity lowers CYP1B1-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.2% of all compounds | 0.047 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[RASSF8-AS1]] | B | RASSF8-AS1 activity raises CYP1B1-AS1's level | lines that do not express RASSF8-AS1 (14) vs lines expressing it (36) | 1.95× lower at baseline in the lines without RASSF8-AS1 | 0.057 | ⚠ within organs, on part of the lines; also absent: RASSF8, B4GALNT1, ENSG00000285804 |
| [[MYPN]] | B | MYPN activity raises CYP1B1-AS1's level | lines that do not express MYPN (29) vs lines expressing it (21) | 2.02× lower at baseline in the lines without MYPN | 0.067 | ⚠ within organs, on part of the lines; also absent: COL4A6, EPGN, FLRT2 |
| [[P3H2-AS1]] | B | P3H2-AS1 activity raises CYP1B1-AS1's level | lines that do not express P3H2-AS1 (30) vs lines expressing it (20) | 1.79× lower at baseline in the lines without P3H2-AS1 | 0.073 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: P3H2, SRGN, KIRREL3 |
| [[MEF2C-AS1]] | B | MEF2C-AS1 activity raises CYP1B1-AS1's level | lines that do not express MEF2C-AS1 (16) vs lines expressing it (34) | 2.05× lower at baseline in the lines without MEF2C-AS1 | 0.086 | ⚠ within organs, on part of the lines; also absent: MEF2C, RGS2, ADGRL4 |

### Downstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02615]] | B | CYP1B1-AS1 activity raises LINC02615's level | lines that do not express CYP1B1-AS1 (14) vs lines expressing it (36) | 1.87× lower at baseline in the lines without CYP1B1-AS1 | 0.006 | ⚠ within organs, on part of the lines; also absent: KCNMA1, ENOX1, PDGFC; maybe low, not absent |
| [[RUSC1-AS1]] | B | CYP1B1-AS1 activity raises RUSC1-AS1's level | lines that do not express CYP1B1-AS1 (14) vs lines expressing it (36) | 1.23× lower at baseline in the lines without CYP1B1-AS1 | 0.012 | ⚠ within organs, on part of the lines; also absent: KCNMA1, ENOX1, PDGFC; maybe low, not absent |
| [[RASSF8-AS1]] | B | CYP1B1-AS1 activity raises RASSF8-AS1's level | lines that do not express CYP1B1-AS1 (14) vs lines expressing it (36) | 2.50× lower at baseline in the lines without CYP1B1-AS1 | 0.014 | ⚠ within organs, on part of the lines; also absent: KCNMA1, ENOX1, PDGFC; maybe low, not absent |
| [[CYP1B1]] | B | CYP1B1-AS1 activity raises CYP1B1's level | lines that do not express CYP1B1-AS1 (14) vs lines expressing it (36) | 3.77× lower at baseline in the lines without CYP1B1-AS1 | 0.020 | ⚠ within organs, on part of the lines; also absent: KCNMA1, ENOX1, PDGFC; maybe low, not absent |
| [[CCDC90B-AS1]] | B | CYP1B1-AS1 activity raises CCDC90B-AS1's level | lines that do not express CYP1B1-AS1 (14) vs lines expressing it (36) | 1.38× lower at baseline in the lines without CYP1B1-AS1 | 0.035 | ⚠ within organs, on part of the lines; also absent: KCNMA1, ENOX1, PDGFC; maybe low, not absent |
| cells under [[Pitavastatin (Calcium) (drug)]] 5 µM | B | CYP1B1-AS1 activity lowers the cells' numbers under Pitavastatin (Calcium) 5 µM (makes them more sensitive) | lines that do not express CYP1B1-AS1 (14) vs lines expressing it (34) | the lines without CYP1B1-AS1: 1.21× the cells of the other lines | 0.037 | ⚠ within organs, on part of the lines; also absent: KCNMA1, ENOX1, PDGFC; maybe low, not absent |
| [[PIGV]] | B | CYP1B1-AS1 activity raises PIGV's level | lines that do not express CYP1B1-AS1 (14) vs lines expressing it (36) | 1.25× lower at baseline in the lines without CYP1B1-AS1 | 0.042 | ⚠ within organs, on part of the lines; also absent: KCNMA1, ENOX1, PDGFC; maybe low, not absent |
| [[BASP1-AS1]] | B | CYP1B1-AS1 activity raises BASP1-AS1's level | lines that do not express CYP1B1-AS1 (14) vs lines expressing it (36) | 2.13× lower at baseline in the lines without CYP1B1-AS1 | 0.061 | ⚠ within organs, on part of the lines; also absent: KCNMA1, ENOX1, PDGFC; maybe low, not absent |
| [[CSGALNACT1]] | B | CYP1B1-AS1 activity raises CSGALNACT1's level | lines that do not express CYP1B1-AS1 (14) vs lines expressing it (36) | 3.17× lower at baseline in the lines without CYP1B1-AS1 | 0.066 | ⚠ within organs, on part of the lines; also absent: KCNMA1, ENOX1, PDGFC; maybe low, not absent |
| [[DPH6-DT]] | B | CYP1B1-AS1 activity raises DPH6-DT's level | lines that do not express CYP1B1-AS1 (14) vs lines expressing it (36) | 1.48× lower at baseline in the lines without CYP1B1-AS1 | 0.072 | ⚠ within organs, on part of the lines; also absent: KCNMA1, ENOX1, PDGFC; maybe low, not absent |
| cells under [[Ouabain (Octahydrate) (drug)]] 0.5 µM | B | CYP1B1-AS1 activity lowers the cells' numbers under Ouabain (Octahydrate) 0.5 µM (makes them more sensitive) | lines that do not express CYP1B1-AS1 (14) vs lines expressing it (34) | the lines without CYP1B1-AS1: 1.30× the cells of the other lines | 0.089 | ⚠ within organs, on part of the lines; also absent: KCNMA1, ENOX1, PDGFC; maybe low, not absent |
| [[PBLD]] | B | CYP1B1-AS1 activity raises PBLD's level | lines that do not express CYP1B1-AS1 (14) vs lines expressing it (36) | 1.30× lower at baseline in the lines without CYP1B1-AS1 | 0.090 | ⚠ within organs, on part of the lines; also absent: KCNMA1, ENOX1, PDGFC; maybe low, not absent |

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.702). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (31.4, 23.3); signed map (48.3, 24.5). **Vector** length 71.9, 16.2% of its response variance represented; |z| ≥ 3 in 747 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +13.4 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.7 | +12.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.6 | +6.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.3 | +7.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.9 | +5.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.0 | +3.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +2.1 | +4.3 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.1 | +1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +0.7 |
| fall | [[Ixazomib citrate (drug)]] 5 µM |  | -3.2 | -5.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | -3.1 | -4.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -2.6 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | -2.2 | -4.9 |
|  | [[Mebendazole (drug)]] 5 µM |  | -2.0 | -2.7 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | -1.8 | -2.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.6 | -2.5 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -1.6 | -3.1 |

## What is on record

|  |  |
|---|---|
| Name | CYP1B1 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 2p22.2 — chr2:38,073,447-38,231,651 (+) |
| Ensembl biotype | lncRNA |
| Also known as | MGC34824; previously C2orf58 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [285154](https://www.ncbi.nlm.nih.gov/gene/285154):

> Predicted to enable U4 snRNA binding activity. Predicted to be involved in formation of quadruple SL/U4/U5/U6 snRNP and spliceosomal tri-snRNP complex assembly. Predicted to be part of U4/U6 x U5 tri-snRNP complex and U6 snRNP. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28543](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28543) · Entrez [285154](https://www.ncbi.nlm.nih.gov/gene/285154) · Ensembl [ENSG00000232973](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000232973)

## Data

Gene col 13880: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13880); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13880, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13880]; `tensor/DDL_lfc|DDL_z.npy` [13880]; `embed/gene_vectors.npy` [13880]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13880 or target_col == 13880). Every well: [[CYP1B1-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CYP1B1-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
