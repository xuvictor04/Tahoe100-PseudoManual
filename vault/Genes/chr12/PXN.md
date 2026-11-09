---
symbol: "PXN"
type: "gene"
col: 1574
ensembl_id: "ENSG00000089159"
name: "paxillin"
location: "12q24.23"
module: 147
arm: "+"
pooled_cpm: 100.1
n_lines_expressing: 49
n_dd_up: 10
n_dd_down: 23
n_dd_up_clean: 6
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/147"]
generated_by: "tahoemap"
---

# PXN

*paxillin* — 12q24.23

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 1.55× (z +7.4, q 6e-11, up in 31 of 48 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 1.37× (z +5.3, q 2e-05, up in 25 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (1 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.578× (z -13.0, q 6e-36, down in 38 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TOMM34]] (+0.76, fdr 7e-06), [[ELK3]] (+0.75, fdr 7e-06), [[CORO2B]] (+0.74, fdr 7e-06).
> It is in [[Module 147]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[KCNN4]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 4 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1574.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.55×** | +7.4 | 6e-11 | 31/48 (A498, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.48×** | +6.4 | 5e-08 | 23/41 (A498, A-427, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.38×** | +5.4 | 1e-05 | 30/47 (NCI-H1573, SW480, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.37×** | +5.3 | 2e-05 | 25/47 (Hs 766T, NCI-H1573, …) | top dose only |  |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.31×** | +4.6 | 5e-04 | 27/46 (NCI-H1573, SW 900, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.20×** | +4.4 | 8e-04 | 21/48 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.28×** | +4.2 | 0.002 | 25/47 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.29×** | +4.2 | 0.002 | 25/46 (NCI-H1573, SW 900, …) | rises with dose | position effect removed |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.23×** | +3.5 | 0.033 | 18/46 (SNU-423, SW480, …) | rises with dose | position effect removed |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.32×** | +3.3 | 0.050 | 19/47 (COLO 205, HCT15, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1574.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.578×** | -13.0 | 6e-36 | 38/48 (MIA PaCa-2, PANC-1, …) | top dose only | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.722×** | -7.7 | 3e-12 | 27/46 (PANC-1, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Trametinib (drug)]] 0.5 µM |  | **0.741×** | -6.2 | 9e-08 | 33/47 (AsPC-1, SK-MEL-2, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.695×** | -6.2 | 9e-08 | 34/49 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.743×** | -6.0 | 3e-07 | 30/47 (SK-MEL-2, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.707×** | -5.8 | 5e-07 | 31/47 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~17% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.707×** | -5.8 | 5e-07 | 26/47 (PANC-1, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.720×** | -5.7 | 8e-07 | 32/48 (MIA PaCa-2, SK-MEL-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.705×** | -5.6 | 1e-06 | 27/47 (NCI-H23, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.716×** | -5.4 | 4e-06 | 30/46 (SK-MEL-2, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **0.730×** | -5.1 | 2e-05 | 25/47 (SK-MEL-2, A-172, …) | all doses, stronger at high dose |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.804×** | -5.0 | 2e-05 | 27/48 (MIA PaCa-2, NCI-H23, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.747×** | -4.9 | 5e-05 | 29/48 (SK-MEL-2, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.924× | -4.5 | 3e-04 | 6/49 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.767×** | -4.3 | 7e-04 | 25/49 (NCI-H23, PANC-1, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.778×** | -4.0 | 0.002 | 23/47 (SK-MEL-2, NCI-H23, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.14 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1574. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 251 | 0 | 17 (3 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.503× (z -22.5) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.295× (z -16.2) |
| [[SK-MEL-2 (line)]] | alt | 145 | 0 | 14 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.233× (z -19.6) |
| [[MIA PaCa-2 (line)]] | alt | 180 | 0 | 10 (2 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.449× (z -26.3) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -22.1) |
| [[PANC-1 (line)]] | alt | 269 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -22.0) |
| [[RKO (line)]] | wt | 154 | 0 | 7 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.155× (z -16.5) ⚠ toxic; cell-cycle shift, explains ~42% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.320× (z -14.8) |
| [[AsPC-1 (line)]] | alt | 212 | 3 (3 ⚠) | 2 | [[Homoharringtonine (drug)]] 0.5 µM 2.48× (z +9.1) ⚠ cell-cycle shift, would explain all of this change | [[Trametinib (drug)]] 0.5 µM 0.418× (z -10.6) |
| [[HOP62 (line)]] | alt | 118 | 0 | 5 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.592× (z -19.2) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.411× (z -13.0) |
| [[A-172 (line)]] | wt | 191 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.442× (z -13.1) |
| [[HEC-1-A (line)]] | alt | 120 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.466× (z -11.8) |
| [[LoVo (line)]] | wt | 74.4 | 0 | 3 | — | [[Panobinostat (drug)]] 5 µM 0.341× (z -11.6) |
| [[A498 (line)]] | wt | 60.0 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.94× (z +11.3) ⚠ toxic; transcription drop | — |
| [[A549 (line)]] | wt | 70.3 | 2 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.74× (z +9.3) ⚠ cell-cycle shift, explains ~18% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 2.65× (z +9.0) | — |
| [[A-427 (line)]] | wt | 69.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.67× (z +8.5) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 62.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.257× (z -10.1) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 40.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.33× (z +9.3) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 125 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.422× (z -12.7) |
| [[HCT15 (line)]] | alt | 127 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.393× (z -11.5) |
| [[HepG2_C3A (line)]] | wt | 80.0 | 1 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 3.30× (z +9.6) ⚠ cell-cycle shift, explains ~19% of this change | — |
| [[HS-578T (line)]] | alt | 51.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.496× (z -8.6) |
| [[J82 (line)]] | alt | 94.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.506× (z -10.6) |
| [[LS 180 (line)]] | wt | 97.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.383× (z -12.8) |
| [[NCI-H1792 (line)]] | alt | 35.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.26× (z +11.1) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 84.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.524× (z -9.8) |
| [[NCI-H2347 (line)]] | alt | 96.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.485× (z -10.6) |
| [[AN3 CA (line)]] | alt | 40.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 84.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 45.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 95.2 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 64.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 51.7 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 64.5 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 38.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 152 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 76.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 81.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 55.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 76.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 31.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 64.1 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 17.6 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 31.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 96.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 61.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 84.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 38.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 61.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1574), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TOMM34]] | +0.76 | +0.62 / +0.77 | both halves | 7e-06 |  |
| [[ELK3]] | +0.75 | +0.73 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[CORO2B]] | +0.74 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[ASAP2]] | +0.72 | +0.73 / +0.71 | both halves | 7e-06 | STRING 836 |
| [[SPRY4]] | +0.72 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[CAPN2]] | +0.70 | +0.69 / +0.70 | both halves | 7e-06 |  |
| [[ACTN1]] | +0.69 | +0.68 / +0.66 | both halves | 7e-06 | pathway: Cell junction organization; STRING 730 |
| [[CD59]] | +0.67 | +0.65 / +0.69 | both halves | 7e-06 |  |
| [[PHC2]] | +0.67 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[TOR4A]] | +0.67 | +0.65 / +0.62 | both halves | 7e-06 |  |
| [[CAPRIN2]] | +0.65 | +0.64 / +0.63 | both halves | 7e-06 |  |
| [[STX1A]] | +0.65 | +0.66 / +0.64 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 7, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[KCNN4]] | B | KCNN4 activity raises PXN's level | lines that do not express KCNN4 (12) vs lines expressing it (38) | 1.84× lower at baseline in the lines without KCNN4 | 0.010 | ⚠ within organs, on part of the lines; also absent: RP1, GSPT2, GALC |
| [[CCND1]] | B | CCND1 activity raises PXN's level | lines that do not express CCND1 (7) vs lines expressing it (43) | 2.11× lower at baseline in the lines without CCND1 | 0.015 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |
| [[EPHA2]] | B | EPHA2 activity raises PXN's level | lines that do not express EPHA2 (11) vs lines expressing it (39) | 1.48× lower at baseline in the lines without EPHA2 | 0.026 | ⚠ within organs, on part of the lines; also absent: RHOD, LINC00857, ABLIM2; maybe low, not absent |
| [[EPHA2-AS1]] | B | EPHA2-AS1 activity raises PXN's level | lines that do not express EPHA2-AS1 (16) vs lines expressing it (34) | 1.35× lower at baseline in the lines without EPHA2-AS1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ENSG00000224621, PKP2, ZNF165; maybe low, not absent |
| [[NIBAN2]] | B | NIBAN2 activity raises PXN's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 2.39× lower at baseline in the lines without NIBAN2 | 0.075 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity raises PXN's level | compounds that target MAP2K1: 3 of 4 lower it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.2% of all compounds | 0.084 | ⚠ off-target possible; 3 compounds |
| [[CDCP1]] | B | CDCP1 activity raises PXN's level | lines that do not express CDCP1 (16) vs lines expressing it (34) | 1.31× lower at baseline in the lines without CDCP1 | 0.095 | ⚠ within organs, on part of the lines; also absent: PTK6, TNK1, CHMP4C |
| [[SPRY4-AS1]] | C | SPRY4-AS1 activity raises PXN's level | lines that do not express SPRY4-AS1 (3) vs lines expressing it (47) | 2.90× lower at baseline in the lines without SPRY4-AS1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: OSBPL3, CRYBG3, PAM; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 147]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.749). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.39; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.9, 6.9); signed map (7.6, 45.1). **Vector** length 134, 41.9% of its response variance represented; |z| ≥ 3 in 1,351 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +5.9 | +5.3 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | +5.8 | +5.4 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | +4.8 | +4.6 |
|  | [[Peretinoin (drug)]] 5 µM |  | +4.5 | +4.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.3 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +4.3 | +4.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +4.2 | +4.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +3.6 | +3.3 |
| fall | [[Trametinib (drug)]] 0.5 µM |  | -7.8 | -6.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | -6.8 | -5.7 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -6.6 | -6.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -6.5 | -5.4 |
|  | [[Trametinib (drug)]] 5 µM |  | -6.4 | -6.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -6.3 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | paxillin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.23 — chr12:120,210,439-120,265,771 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | LIM domain containing |
| Hallmark sets | MITOTIC_SPINDLE |
| Reactome | 18 pathways, smallest: Localization of the PINCH-ILK-PARVIN complex to focal adhesions; Regulation of cytoskeletal remodeling and cell spreading by IPP complex components; Regulation of MITF-M-dependent genes involved in extracellular matrix, focal adhesion and epithelial-to-mesenchymal transition |
| Matched by | ensembl_id |

**Function**, from UniProt [P49023](https://www.uniprot.org/uniprotkb/P49023) (Paxillin):

> Cytoskeletal protein involved in actin-membrane attachment at sites of cell adhesion to the extracellular matrix (focal adhesion). Recruits other proteins such as TRIM15 to focal adhesion.

**Summary**, from NCBI Gene [5829](https://www.ncbi.nlm.nih.gov/gene/5829):

> This gene encodes a cytoskeletal protein involved in actin-membrane attachment at sites of cell adhesion to the extracellular matrix (focal adhesion). Alternatively spliced transcript variants encoding different isoforms have been described for this gene. These isoforms exhibit different expression pattern, and have different biochemical, as well as physiological properties (PMID:9054445). [provided by RefSeq, Aug 2011]

**Accessions** — [HGNC:9718](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9718) · Entrez [5829](https://www.ncbi.nlm.nih.gov/gene/5829) · UniProt [P49023](https://www.uniprot.org/uniprotkb/P49023) · Ensembl [ENSG00000089159](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089159)

## Data

Gene col 1574: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1574); `tables/drug_effects.parquet` (34 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1574, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1574]; `tensor/DDL_lfc|DDL_z.npy` [1574]; `embed/gene_vectors.npy` [1574]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1574 or target_col == 1574). Every well: [[PXN — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PXN.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
