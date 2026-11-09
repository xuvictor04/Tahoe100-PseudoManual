---
symbol: "LAMC2"
type: "gene"
col: 656
ensembl_id: "ENSG00000058085"
name: "laminin subunit gamma 2"
location: "1q25.3"
module: 34
arm: "+"
pooled_cpm: 202.58
n_lines_expressing: 23
n_dd_up: 25
n_dd_down: 43
n_dd_up_clean: 16
n_dd_down_clean: 42
in_vector_space: true
direction_upstream: 66
direction_downstream: 91
tags: ["gene", "module/034"]
generated_by: "tahoemap"
---

# LAMC2

*laminin subunit gamma 2* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.84× (z +14.0, q 2e-41, up in 11 of 22 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.33× (z +5.4, q 7e-06, up in 9 of 21 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (1 with an alert ⚠); the strongest is [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM: 0.495× (z -8.6, q 3e-15, down in 17 of 21 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PLEK2]] (+0.74, fdr 7e-06), [[FERMT1]] (+0.72, fdr 7e-06), [[ITGA2]] (+0.72, fdr 7e-06).
> It is in [[Module 034]], a single-armed module (Type I hemidesmosome assembly).
> Probable direction (from the cell lines, not proof of direct regulation): 66 arrows point to it, the strongest [[PLEK2]] → it (grade B ⚠); 91 go from it, the strongest it → [[MET]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 9 with an alert ⚠; shown: the 15 strongest and the 8 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 656.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.84×** | +14.0 | 2e-41 | 11/22 (HCT15, SW 900, …) | all doses, flat | cell-cycle shift (explains ~4% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +9.5 | 8e-19 | 9/20 (HCT15, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.89×** | +8.2 | 6e-14 | 10/20 (HCT15, SW 900, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~64% of this change | **1.38×** | +6.1 | 2e-07 | 10/21 (HT-29, A-172, …) | all doses, stronger at high dose | composition shift |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **1.53×** | +5.7 | 2e-06 | 16/21 (HT-29, LS 180, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.33×** | +5.4 | 7e-06 | 9/21 (KATO III, SW480, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.32×** | +5.3 | 8e-06 | 11/22 (HT-29, LS 180, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **1.40×** | +4.5 | 4e-04 | 10/21 (COLO 205, SW 900, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.38×** | +4.4 | 8e-04 | 15/21 (HT-29, LS 180, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 5 µM |  | **1.39×** | +4.2 | 0.001 | 18/21 (HT-29, LS 180, …) | all doses, stronger at high dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.35×** | +4.0 | 0.003 | 12/21 (HT-29, LS 180, …) | rises with dose |  |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.94×** | +3.9 | 0.004 | 5/16 (NCI-H2347, AsPC-1, …) | top dose only | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | **1.34×** | +3.9 | 0.004 | 15/21 (HT-29, LS 180, …) | all doses, stronger at high dose |  |
| [[PF-06260933 (drug)]] 5 µM |  | **1.88×** | +3.7 | 0.008 | 17/21 (SW480, LS 180, …) | top dose only | noisy plate (z scaled) |
| [[Cyclosporin A (drug)]] 5 µM |  | **1.31×** | +3.7 | 0.009 | 13/21 (KATO III, AsPC-1, …) | rises with dose |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.32×** | +3.6 | 0.011 | 18/21 (HEC-1-A, Panc 03.27, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +3.5 | 0.014 | 9/22 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.43×** | +3.4 | 0.018 | 3/21 (SW 900, SW480, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[vincristine (drug)]] 5 µM |  | **1.78×** | +3.4 | 0.019 | 9/21 (LS 180, HT-29, …) | rises with dose | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.029 | 10/21 (HT-29, LS 180, …) | rises with dose | low cells (technical?); noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.032 | 12/21 (AsPC-1, Hs 766T, …) | all doses, flat | low cells (technical?) |
| [[Ferulic acid (drug)]] 0.05 µM |  | **1.30×** | +3.2 | 0.032 | 9/21 (SW 900, CFPAC-1, …) | inconsistent across doses | position effect removed |
| [[Cyclosporin A (drug)]] 0.5 µM |  | **1.25×** | +3.0 | 0.071 | 10/21 (KATO III, AsPC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 44 in all, 1 with an alert ⚠; shown: the 15 strongest. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 656.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.495×** | -8.6 | 3e-15 | 17/21 (SW48, SW480, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.647×** | -8.0 | 3e-13 | 19/21 (SW480, SW48, …) | all doses, flat |  |
| [[Trametinib (drug)]] 5 µM |  | **0.539×** | -7.7 | 3e-12 | 20/23 (SW48, SW480, …) | all doses, flat | cell-cycle shift (explains ~3% here); noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **0.627×** | -7.6 | 4e-12 | 19/21 (SW48, SW480, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.631×** | -7.3 | 3e-11 | 18/21 (SW48, NCI-H1573, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **0.689×** | -6.8 | 8e-10 | 18/22 (SW48, HEC-1-A, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **0.620×** | -6.4 | 2e-08 | 18/22 (SW48, LoVo, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.633×** | -6.1 | 9e-08 | 18/22 (SW48, SW480, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.634×** | -6.0 | 9e-08 | 14/21 (A549, HS-578T, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **0.631×** | -5.9 | 2e-07 | 19/21 (SW48, NCI-H1573, …) | all doses, stronger at high dose | position effect removed |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **0.646×** | -5.5 | 2e-06 | 19/21 (SW48, A549, …) | inconsistent across doses |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **0.677×** | -5.2 | 1e-05 | 18/21 (SW48, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.683×** | -5.1 | 2e-05 | 13/21 (HEC-1-A, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.699×** | -4.8 | 7e-05 | 15/21 (A549, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.699×** | -4.8 | 7e-05 | 15/21 (A549, HS-578T, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.32 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 656. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW48 (line)]] | wt | 718 | 0 | 15 (2 ⚠) | — | [[Binimetinib (drug)]] 0.5 µM 0.211× (z -12.9) |
| [[HEC-1-A (line)]] | alt | 516 | 0 | 11 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -17.6) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.267× (z -10.9) |
| [[A549 (line)]] | wt | 261 | 0 | 10 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.305× (z -12.0) ⚠ cell-cycle shift, explains ~53% of this change · without an alert: [[Budesonide (drug)]] 0.05 µM 0.266× (z -9.5) |
| [[NCI-H1573 (line)]] | alt | 1,223 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.173× (z -17.0) ⚠ cell-cycle shift, explains ~64% of this change · without an alert: [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM 0.213× (z -10.2) |
| [[HT-29 (line)]] | alt | 64.8 | 7 (4 ⚠) | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.97× (z +11.8) | — |
| [[SW480 (line)]] | alt | 93.8 | 0 | 5 | — | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM 0.326× (z -10.6) |
| [[COLO 205 (line)]] | alt | 111 | 2 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 8.55× (z +13.3) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[HCT15 (line)]] | alt | 64.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.99× (z +9.7) ⚠ toxic; transcription drop | — |
| [[LoVo (line)]] | wt | 190 | 1 (1 ⚠) | 1 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.49× (z +8.7) ⚠ cell-cycle shift, explains ~88% of this change | [[Digitoxin (drug)]] 5 µM 0.294× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change |
| [[KATO III (line)]] | alt | 156 | 1 (1 ⚠) | 0 | [[Harringtonine (drug)]] 0.5 µM 2.49× (z +8.5) ⚠ cell-cycle shift, explains ~27% of this change | — |
| [[LS 180 (line)]] | wt | 218 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 2.34× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 150 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -15.2) ⚠ cell-cycle shift, explains ~64% of this change |
| [[SW 900 (line)]] | alt | 72.0 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 0.5 µM 3.50× (z +8.9) ⚠ cell-cycle shift, explains ~34% of this change | — |
| [[A-172 (line)]] | wt | 97.3 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 15.9 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 14.0 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 32.9 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 764 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 49.6 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 18.0 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 18.4 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 903 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.7 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 19.9 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 19.2 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 46.3 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 373 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 116 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 29.0 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 47.6 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 22.3 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.9 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 25.5 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 525 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 26.6 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 896 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 26.4 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 164 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.1 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 683 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 47.1 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 18.7 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 23.3 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 19.1 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.7 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 17.9 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 20.8 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 35.3 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 20.8 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 144 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 656), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PLEK2]] | +0.74 | +0.72 / +0.72 | both halves | 7e-06 |  |
| [[FERMT1]] | +0.72 | +0.73 / +0.67 | both halves | 7e-06 | STRING 484 |
| [[ITGA2]] | +0.72 | +0.69 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_APICAL_JUNCTION; STRING 883 |
| [[C6orf141]] | +0.71 | +0.72 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[LAMA3]] | +0.71 | +0.69 / +0.69 | both halves | 7e-06 | same gene group; pathway: HALLMARK_APICAL_JUNCTION; STRING 998 |
| [[CDCP1]] | +0.70 | +0.70 / +0.65 | both halves | 7e-06 |  |
| [[DHRS9]] | +0.70 | +0.61 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[LAMB3]] | +0.68 | +0.69 / +0.71 | both halves | 7e-06 | same gene group; pathway: HALLMARK_APICAL_JUNCTION; STRING 999 |
| [[ITGA6]] | +0.68 | +0.69 / +0.64 | both halves | 7e-06 | pathway: Assembly of collagen fibrils and other multimeric structures; STRING 898 |
| [[GJB3]] | +0.67 | +0.69 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_ESTROGEN_RESPONSE_LATE; STRING 410 |
| [[TMC7]] | +0.66 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[FGD6]] | +0.66 | +0.62 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*66 arrows, 66 of them with an alert ⚠; grade A 0, B 24, C 42. Shown: the 12 strongest; 54 more arrows (54 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLEK2]] | B | PLEK2 activity raises LAMC2's level | lines that do not express PLEK2 (17) vs lines expressing it (33) | 3.42× lower at baseline in the lines without PLEK2 | 0.018 | ⚠ within organs, on part of the lines; also absent: CDCP1, SAMD12, SDR16C5 |
| [[PRAG1]] | B | PRAG1 activity raises LAMC2's level | lines that do not express PRAG1 (16) vs lines expressing it (34) | 3.97× lower at baseline in the lines without PRAG1 | 0.018 | ⚠ within organs, on part of the lines; also absent: ANO9, EPS8L2, PDGFB; maybe low, not absent |
| [[ITGA2]] | B | ITGA2 activity raises LAMC2's level | lines that do not express ITGA2 (11) vs lines expressing it (39) | 3.39× lower at baseline in the lines without ITGA2 | 0.024 | ⚠ within organs, on part of the lines; also absent: GPR39, ATXN1-AS1, MET |
| [[FAM107B]] | B | FAM107B activity raises LAMC2's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 3.39× lower at baseline in the lines without FAM107B | 0.031 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[ZNF185]] | B | ZNF185 activity raises LAMC2's level | lines that do not express ZNF185 (15) vs lines expressing it (35) | 3.73× lower at baseline in the lines without ZNF185 | 0.031 | ⚠ within organs, on part of the lines; also absent: HTR1D, KLF5, IL18 |
| [[LYPD3]] | B | LYPD3 activity raises LAMC2's level | lines that do not express LYPD3 (15) vs lines expressing it (35) | 3.53× lower at baseline in the lines without LYPD3 | 0.037 | ⚠ within organs, on part of the lines; also absent: ENSG00000259345, ENSG00000256982, IGSF9; maybe low, not absent |
| [[MET]] | B | MET activity raises LAMC2's level | lines that do not express MET (9) vs lines expressing it (41) | 4.67× lower at baseline in the lines without MET | 0.038 | ⚠ within organs, on part of the lines; also absent: TGFBR2, PHLDA2, VDR |
| [[LINC00707]] | B | LINC00707 activity raises LAMC2's level | lines that do not express LINC00707 (26) vs lines expressing it (24) | 2.46× lower at baseline in the lines without LINC00707 | 0.048 | ⚠ within organs, on part of the lines; also absent: ENSG00000285845, ENSG00000285743, LINP1 |
| [[TGFA]] | B | TGFA activity raises LAMC2's level | lines that do not express TGFA (17) vs lines expressing it (33) | 3.18× lower at baseline in the lines without TGFA | 0.049 | ⚠ within organs, on part of the lines; also absent: AQP3, ELF3, VIPR1 |
| [[TOR4A]] | B | TOR4A activity raises LAMC2's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 3.91× lower at baseline in the lines without TOR4A | 0.050 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[PLAU]] | B | PLAU activity raises LAMC2's level | lines that do not express PLAU (26) vs lines expressing it (24) | 2.87× lower at baseline in the lines without PLAU | 0.053 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3 |
| [[PLCXD2]] | B | PLCXD2 activity raises LAMC2's level | lines that do not express PLCXD2 (7) vs lines expressing it (43) | 2.79× lower at baseline in the lines without PLCXD2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SOX4; maybe low, not absent |

### Downstream of this gene

*91 arrows, 91 of them with an alert ⚠; grade A 0, B 55, C 36. Shown: the 12 strongest; 79 more arrows (79 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MET]] | B | LAMC2 activity raises MET's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 3.73× lower at baseline in the lines without LAMC2 | 0.001 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[EHD1]] | B | LAMC2 activity raises EHD1's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 1.77× lower at baseline in the lines without LAMC2 | 0.005 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[OSBPL3]] | B | LAMC2 activity raises OSBPL3's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 2.10× lower at baseline in the lines without LAMC2 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[S100A11]] | B | LAMC2 activity raises S100A11's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 1.90× lower at baseline in the lines without LAMC2 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[ARHGAP27]] | B | LAMC2 activity raises ARHGAP27's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 2.57× lower at baseline in the lines without LAMC2 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[FAM107B]] | B | LAMC2 activity raises FAM107B's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 2.24× lower at baseline in the lines without LAMC2 | 0.011 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[YOD1]] | B | LAMC2 activity raises YOD1's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 1.94× lower at baseline in the lines without LAMC2 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[PLEKHM1P1]] | B | LAMC2 activity raises PLEKHM1P1's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 1.49× lower at baseline in the lines without LAMC2 | 0.013 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[S100A16]] | B | LAMC2 activity raises S100A16's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 2.68× lower at baseline in the lines without LAMC2 | 0.016 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[EPHA2]] | B | LAMC2 activity raises EPHA2's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 3.18× lower at baseline in the lines without LAMC2 | 0.018 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[KPNA7]] | B | LAMC2 activity raises KPNA7's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 2.32× lower at baseline in the lines without LAMC2 | 0.021 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |
| [[SERPINB1]] | B | LAMC2 activity raises SERPINB1's level | lines that do not express LAMC2 (27) vs lines expressing it (23) | 3.65× lower at baseline in the lines without LAMC2 | 0.022 | ⚠ within organs, on part of the lines; also absent: ENSG00000287929, TNS4, HS3ST1 |

## Where it sits

- **Module**: [[Module 034]] — Type I hemidesmosome assembly; 137 genes; every member is in the + arm (projection on the module's main direction 0.818). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.24; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (41.6, 2.9); signed map (4.9, 41.8). **Vector** length 122, 45.4% of its response variance represented; |z| ≥ 3 in 994 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +7.3 | +5.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.2 | +9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.7 | +3.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +14.0 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.3 | +8.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | +3.7 | +4.2 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | +3.3 | +4.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | +2.9 | +3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +5.3 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -5.1 | -8.6 |
|  | [[Trametinib (drug)]] 5 µM |  | -4.8 | -7.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.6 | -6.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -4.4 | -8.0 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.3 | -7.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.2 | -7.6 |

## What is on record

|  |  |
|---|---|
| Name | laminin subunit gamma 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:183,186,238-183,245,127 (+) |
| Ensembl biotype | protein_coding |
| Also known as | nicein-100kDa, kalinin-105kDa, BM600-100kDa; previously EBR2, LAMB2T, LAMNB2, EBR2A |
| Gene groups (HGNC) | Laminin subunits |
| Hallmark sets | APICAL_JUNCTION, ESTROGEN_RESPONSE_LATE, EPITHELIAL_MESENCHYMAL_TRANSITION |
| Reactome | 24 pathways, smallest: Type I hemidesmosome assembly; Anchoring fibril formation; Attachment of bacteria to epithelial cells |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13753](https://www.uniprot.org/uniprotkb/Q13753) (Laminin subunit gamma-2):

> Binding to cells via a high affinity receptor, laminin is thought to mediate the attachment, migration and organization of cells into tissues during embryonic development by interacting with other extracellular matrix components. Ladsin exerts cell-scattering activity toward a wide variety of cells, including epithelial, endothelial, and fibroblastic cells.

**Summary**, from NCBI Gene [3918](https://www.ncbi.nlm.nih.gov/gene/3918):

> Laminins, a family of extracellular matrix glycoproteins, are the major noncollagenous constituent of basement membranes. They have been implicated in a wide variety of biological processes including cell adhesion, differentiation, migration, signaling, neurite outgrowth and metastasis. Laminins, composed of 3 non identical chains: laminin alpha, beta and gamma (formerly A, B1, and B2, respectively), have a cruciform structure consisting of 3 short arms, each formed by a different chain, and a …

**Accessions** — [HGNC:6493](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6493) · Entrez [3918](https://www.ncbi.nlm.nih.gov/gene/3918) · UniProt [Q13753](https://www.uniprot.org/uniprotkb/Q13753) · Ensembl [ENSG00000058085](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000058085)

## Data

Gene col 656: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 656); `tables/drug_effects.parquet` (69 rows, flagged included); `relations/gene_relations.parquet` (col_a == 656, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 656]; `tensor/DDL_lfc|DDL_z.npy` [656]; `embed/gene_vectors.npy` [656]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 656 or target_col == 656). Every well: [[LAMC2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LAMC2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
