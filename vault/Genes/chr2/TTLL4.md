---
symbol: "TTLL4"
type: "gene"
col: 5774
ensembl_id: "ENSG00000135912"
name: "tubulin tyrosine ligase like 4"
location: "2q35"
module: 26
arm: "-"
pooled_cpm: 24.11
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# TTLL4

*tubulin tyrosine ligase like 4* — 2q35

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (5 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 2.16× (z +6.7, q 1e-08, up in 25 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.460× (z -12.5, q 7e-33, down in 27 of 35 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Auranofin (drug)]] 5 µM: 0.604× (z -8.4, q 6e-15, down in 33 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[WDR5]] (+0.66, fdr 1e-05), [[ASB13]] (+0.66, fdr 1e-05), [[RSAD1]] (+0.65, fdr 7e-06); moves opposite to [[PSMD7-DT]] (-0.62, fdr 3e-05), [[AK9]] (-0.61, fdr 3e-05), [[LRP2BP]] (-0.61, fdr 3e-05).
> It sits in the **-** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[GNAZ]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 5 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5774.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **2.16×** | +6.7 | 1e-08 | 25/48 (SW480, COLO 205, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **1.41×** | +5.7 | 3e-06 | 27/48 (AsPC-1, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.40×** | +5.6 | 4e-06 | 23/48 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.39×** | +5.4 | 8e-06 | 26/48 (NCI-H23, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.38×** | +5.3 | 1e-05 | 25/48 (MIA PaCa-2, NCI-H460, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM |  | **1.38×** | +5.3 | 1e-05 | 23/48 (AsPC-1, HT-29, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **1.37×** | +5.2 | 1e-05 | 26/47 (NCI-H460, MIA PaCa-2, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.37×** | +5.2 | 1e-05 | 24/48 (AsPC-1, HT-29, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.34×** | +4.9 | 6e-05 | 21/47 (NCI-H1792, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.34×** | +4.9 | 6e-05 | 21/46 (SW480, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **1.67×** | +4.5 | 4e-04 | 21/47 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~20% of this change | **1.33×** | +4.4 | 4e-04 | 19/48 (NCI-H460, HS-578T, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **1.24×** | +3.5 | 0.017 | 9/47 (SW480, CFPAC-1, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.23×** | +3.4 | 0.028 | 12/47 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 4 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5774.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.460×** | -12.5 | 7e-33 | 27/35 (NCI-H460, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.526×** | -10.7 | 2e-24 | 32/43 (HEC-1-A, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.561×** | -8.9 | 9e-17 | 24/40 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Auranofin (drug)]] 5 µM |  | **0.604×** | -8.4 | 6e-15 | 33/48 (SK-MEL-2, SNU-423, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.747×** | -6.7 | 2e-09 | 29/47 (COLO 205, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.719×** | -5.3 | 1e-05 | 24/48 (MIA PaCa-2, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~21% of this change | 0.870× | -3.2 | 0.095 | 9/48 (SK-MEL-2, LOX-IMVI, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.05 µM |  | 0.827× | -3.2 | 0.10 | 7/48 (CFPAC-1, A-427, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5774. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 58.9 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.152× (z -12.1) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 46.0 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.120× (z -17.6) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 25.4 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.271× (z -12.4) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 28.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.122× (z -13.8) ⚠ toxic; transcription drop |
| [[SW480 (line)]] | alt | 31.5 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 5.49× (z +9.8) | [[Dinaciclib (drug)]] 0.05 µM 0.157× (z -19.0) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 23.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.424× (z -8.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 27.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0845× (z -16.0) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 30.9 | 0 | 1 | — | [[Pravastatin (sodium) (drug)]] 0.05 µM 0.105× (z -8.7) |
| [[H4 (line)]] | wt | 19.1 | 0 | 1 (1 ⚠) | — | [[Tucidinostat (drug)]] 0.5 µM 0.0603× (z -12.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HEC-1-A (line)]] | alt | 26.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -12.8) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 22.0 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.322× (z -8.6) |
| [[Hs 766T (line)]] | wt | 9.62 | 0 | 1 | — | [[Medroxyprogesterone acetate (drug)]] 0.5 µM 0.101× (z -11.1) |
| [[LoVo (line)]] | wt | 21.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -13.3) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 17.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.222× (z -9.5) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 30.8 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -9.4) |
| [[NCI-H1573 (line)]] | alt | 20.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.316× (z -8.5) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 23.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0945× (z -19.4) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 21.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -11.1) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 24.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -11.9) ⚠ toxic; transcription drop |
| [[SW1417 (line)]] | alt | 33.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.140× (z -15.2) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 20.4 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 36.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 25.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 55.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.3 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 21.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 23.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 32.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 15.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 24.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 20.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5774), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*59 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR5]] | +0.66 | +0.67 / +0.54 | both halves | 1e-05 |  |
| [[ASB13]] | +0.66 | +0.51 / +0.65 | both halves | 1e-05 |  |
| [[RSAD1]] | +0.65 | +0.60 / +0.58 | both halves | 7e-06 |  |
| [[BRAT1]] | +0.65 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ZNF692]] | +0.64 | +0.65 / +0.52 | both halves | 1e-05 |  |
| [[CDK5RAP1]] | +0.63 | +0.66 / +0.53 | both halves | 1e-05 |  |
| [[FAM24B]] | +0.62 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[MTERF3]] | +0.62 | +0.52 / +0.63 | both halves | 1e-05 |  |
| [[ACTR5]] | +0.61 | +0.58 / +0.55 | both halves | 1e-05 |  |
| [[TMEM177]] | +0.61 | +0.38 / +0.59 | both halves | 7e-05 |  |
| [[SLC23A2]] | +0.61 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[DENND6A]] | +0.61 | +0.50 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*41 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PSMD7-DT]] | -0.62 | -0.58 / -0.46 | both halves | 3e-05 |  |
| [[AK9]] | -0.61 | -0.62 / -0.45 | both halves | 3e-05 |  |
| [[LRP2BP]] | -0.61 | -0.61 / -0.45 | both halves | 3e-05 |  |
| [[PDCL3P4]] | -0.61 | -0.62 / -0.48 | both halves | 2e-05 |  |
| [[TSGA10]] | -0.60 | -0.63 / -0.35 | both halves | 1e-04 |  |
| [[SOX2-OT]] | -0.60 | -0.54 / -0.53 | both halves | 1e-05 |  |
| [[CPEB2-DT]] | -0.60 | -0.57 / -0.46 | both halves | 2e-05 |  |
| [[CCDC90B-AS1]] | -0.60 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[PEBP4]] | -0.60 | -0.56 / -0.42 | both halves | 4e-05 |  |
| [[DNAH12]] | -0.60 | -0.63 / -0.38 | both halves | 7e-05 |  |
| [[FAM120AOS]] | -0.59 | -0.64 / -0.39 | both halves | 5e-05 |  |
| [[BCL10-AS1]] | -0.58 | -0.55 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[GNAZ]] | B | GNAZ activity raises TTLL4's level | lines that do not express GNAZ (10) vs lines expressing it (40) | 1.44× lower at baseline in the lines without GNAZ | 0.040 | ⚠ within organs, on part of the lines; also absent: RNF220, TSPAN33, KIF26A; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **-** arm (projection on the module's main direction -0.617). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (-1.0, -2.2); signed map (-39.3, -17.6). **Vector** length 71.0, 12.4% of its response variance represented; |z| ≥ 3 in 868 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +3.5 | +5.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +3.4 | +1.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.8 | +5.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~30% of this change | +2.8 | +3.5 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.6 | +5.3 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.2 | +2.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.2 | +2.9 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +1.6 | +1.4 |
|  | [[TAK-733 (drug)]] 5 µM |  | +1.6 | +2.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.5 | +4.5 |
| fall | [[Auranofin (drug)]] 5 µM |  | -6.0 | -8.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.0 | +0.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -3.7 | -6.7 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -5.3 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -3.1 | -1.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.0 | -1.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -1.2 | -0.7 |
|  | [[Lactate (calcium) (drug)]] 5 µM |  | -1.2 | -2.6 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.1 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | tubulin tyrosine ligase like 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q35 — chr2:218,710,835-218,755,416 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0173 |
| Gene groups (HGNC) | Tubulin tyrosine ligase family |
| Reactome | 1 pathways, smallest: Carboxyterminal post-translational modifications of tubulin |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14679](https://www.uniprot.org/uniprotkb/Q14679) (Tubulin monoglutamylase TTLL4):

> Monoglutamylase which modifies both tubulin and non-tubulin proteins, adding a single glutamate on the gamma-carboxyl group of specific glutamate residues of target proteins. Involved in the side-chain initiation step of the polyglutamylation reaction but not in the elongation step. Preferentially modifies beta-tail tubulin over the alpha-tubulin. Monoglutamylates nucleosome assembly proteins NAP1L1 and NAP1L4. Monoglutamylates nucleotidyltransferase CGAS, leading to inhibition of CGAS …

**Summary**, from NCBI Gene [9654](https://www.ncbi.nlm.nih.gov/gene/9654):

> Predicted to enable tubulin binding activity and tubulin-glutamic acid ligase activity. Predicted to be involved in microtubule cytoskeleton organization and protein polyglutamylation. Predicted to act upstream of or within regulation of blastocyst development. Predicted to be located in cytosol. Predicted to be active in ciliary basal body. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28976](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28976) · Entrez [9654](https://www.ncbi.nlm.nih.gov/gene/9654) · UniProt [Q14679](https://www.uniprot.org/uniprotkb/Q14679) · Ensembl [ENSG00000135912](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135912)

## Data

Gene col 5774: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5774); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5774, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5774]; `tensor/DDL_lfc|DDL_z.npy` [5774]; `embed/gene_vectors.npy` [5774]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5774 or target_col == 5774). Every well: [[TTLL4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TTLL4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
